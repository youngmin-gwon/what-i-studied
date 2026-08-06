---
title: zygote-fork-saves-memory-while-copy-on-write-pages-stay-clean
tags: [android, android/boot-runtime, android/runtime, android/system-internals]
aliases: ["Zygote fork의 메모리 이점은 copy-on-write가 유지될 때 생긴다"]
date modified: 2026-08-05 16:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Zygote fork 의 메모리 이점은 copy-on-write 가 유지될 때 생긴다

상위 문서: [Zygote 런타임 계약](zygote-runtime-contracts.md)
배경 지식: [fork()](../../../../../operating-systems/process-states-lifecycle.md), [Copy-On-Write/가상 메모리](../../../../../../02_references/operating-systems/virtual-memory.md), [데드락](../../../../../operating-systems/deadlock.md)

Zygote의 **[`fork()`](../../../../../operating-systems/process-states-lifecycle.md)**(부모 프로세스의 메모리 이미지를 그대로 복제해 거의 동일한 새 자식 프로세스를 만드는 POSIX 시스템 콜) 아키텍처가 제공하는 핵심 RAM 절감 이점은 부모 프로세스인 Zygote가 사전 로드(Preload)한 프레임워크 클래스, 자원(Resources), Native 공유 라이브러리가 Linux Kernel의 **[Copy-On-Write (COW)](../../../../../../02_references/operating-systems/virtual-memory.md)**(페이지를 즉시 복사하지 않고 부모/자식이 공유하다가, 어느 한쪽이 실제로 쓰기를 시도하는 순간에만 그 페이지를 복사하는 지연 복사 기법) 메커니즘을 통해 모든 앱 프로세스 간에 **Shared Clean Pages**로 물리 메모리를 공동 공유할 때 실현된다.

### 내부 동작 메커니즘 (Internal Mechanism)

1. **Shared RAM Allocation via `fork()`**:
   - Zygote가 부팅 과정에서 약 4,000 여 개의 프레임워크 핵심 Java 클래스(`/system/etc/preloaded-classes`), 공통 시스템 리소스(`framework-res.apk`), Native 공유 라이브러리(`libandroid_runtime.so`)를 미리 힙에 로드(Preload)한다.
   - Zygote가 자식 앱 프로세스를 `fork()`할 때 커널은 물리 메모리 페이지를 새로 복사하지 않고, 가상 메모리 페이지 테이블(Page Table)의 읽기 전용(Read-Only) 포인터만 자식에게 복제 바인딩한다.
   - 따라서 프레임워크 Java 클래스, 서체(Fonts), 공통 뷰 드로어블 메타데이터는 단 1벌만 RAM에 존재하고 수십 개 앱이 공유한다.
2. **Single-Threaded Constraint Before `fork()`**:
   - POSIX `fork()` 특성상 부모 프로세스의 다른 스레드가 뮤텍스(Mutex) 락을 쥐고 있는 상태에서 `fork()`를 수행하면 자식 프로세스에는 락을 해제해줄 스레드가 존재하지 않아 즉시 **[데드락(Deadlock)](../../../../../operating-systems/deadlock.md)**(서로가 상대방이 들고 있는 자원을 기다리며 아무도 더 진행하지 못하는 영구 정지 상태)이 발생한다.
   - AOSP Zygote는 `fork()` 직전 백그라운드 스레드 풀(USAP 헬퍼 등)을 일시 정지하거나 단일 스레드 상태임을 보증(`Zygote.nativeForkAndSpecialize` 스레드 검증)한 후 `fork()`를 수행한다.
3. **Page Dirtying (Dirty Pages Conversion)**:
   - 만약 앱 프로세스가 런타임에 Zygote가 Preload한 전역 객체의 정적 변수(Static Field)를 수정하거나 메모리를 새로 할당하면, 커널 MMU(Memory Management Unit)는 Page Fault를 발생시켜 해당 4KB 메모리 페이지만 자식 프로세스 고유 메모리(**Private Dirty Page**)로 물리 복사한다.
4. **Dirty Page 관리 파급력**:
   - 앱이 Zygote 공유 객체에 값을 쓸수록 Shared Clean Page가 감소하고 Private Dirty Page가 증가하여 디바이스 전체 RAM 절감 효율이 급격히 저하된다.

```mermaid
flowchart TD
    ZYG["Zygote Parent Memory
(Preloaded Classes & Resources)"] -->|fork()| APP1["App 1 Virtual Memory"]
    ZYG -->|fork()| APP2["App 2 Virtual Memory"]
    
    APP1 & APP2 -->|Read Only (Shared)| PHY["Physical RAM: Shared Clean Pages
(Single Memory Copy)"]
    
    APP1 -->|Write to Preloaded Object| FAULT["MMU Page Fault (COW Trigger)"]
    FAULT -->|Duplicate 4KB Page| DIRTY["App 1 Private Dirty Page
(RAM Consumed Independently)"]

    style PHY fill:#e8f5e9,stroke:#388e3c
    style DIRTY fill:#ffcdd2,stroke:#b71c1c
```

### 코드 및 구체 예시 (Concrete Snippets)

`procrank` 또는 `meminfo`를 통해 PSS/USS 및 Shared Clean/Dirty 메모리를 확인하는 분석 스니펫:

```bash
# 앱 프로세스의 메모리 맵(smaps_rollup) 상세 분석
adb shell cat /proc/$(adb shell pidof com.example.app)/smaps_rollup
# 출력 주요 항목 예시:
# Rss:               85400 kB
# Pss:               32100 kB (공유 메모리를 나눈 가상 실제 점유량)
# Shared_Clean:      42000 kB (Zygote와 완벽히 공유 중인 메모리 영역)
# Shared_Dirty:       1200 kB
# Private_Dirty:     28000 kB (앱 고유 힙 메모리 및 COW 복사 페이지)
```

### 관측 가능 증거 (Observable Evidence)

`adb shell`을 사용하여 앱 프로세스의 Shared Clean Page 수치와 PSS(Proportional Set Size) 비율을 측정할 수 있다:

```bash
# 전체 프로세스별 PSS 및 Shared/Private 메모리 점유율 조회
adb shell dumpsys meminfo com.example.app

# system_server 및 Zygote 자식 프로세스 간 Shared Clean 비율 관측
adb shell procrank # (디버그 빌드 환경 지원 시)
```

### 관련 문서

- [Zygote Preload State](zygote-preload-state.md)
- [app-process-specializes-before-activitythread-attaches-to-framework](app-process-specializes-before-activitythread-attaches-to-framework.md)

공식 문서: [Overview of Android Memory Management](https://developer.android.com/topic/performance/memory-overview)
