---
title: runtime-debugging-separates-profile-compile-filter-and-jit-state
tags: [android, android/boot-runtime, android/runtime, android/system-internals]
aliases: ["런타임 디버깅은 profile, compile filter, JIT 상태를 분리해서 본다"]
date modified: 2026-08-03 17:24:04 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 런타임 디버깅은 profile, compile filter, JIT 상태를 분리해서 본다

상위 문서: [Zygote 런타임 계약](zygote-runtime-contracts.md)

ART 런타임 환경에서 발생하는 앱 스타트업 지연, 프레임 드롭(Jank), GC 수면 이슈를 정확히 진단하기 위해서는 단일 디버그 로그에 의존하지 않고, (1) JIT Code Cache 메모리 상태, (2) 현재 적용된 Compile Filter 상태 (`verify`, `speed`, `speed-profile`), 그리고 (3) Baseline Profile 및 Local `.prof` 덤프 상태를 명확히 분리하여 종합 분석해야 한다.

### 내부 동작 메커니즘 (Internal Mechanism)

1. **Compile Filter Spectrum**:
   - `assume-verified` / `extract`: 바이트코드 검증 생략 혹은 APK에서 DEX만 추출.
   - `verify`: DEX 바이트코드 검증만 수행 (런타임 시 Interpreter / JIT 구동).
   - `quicken`: DEX 바이트코드 명령어 일부만 단순 디코딩 최적화 (구버전 호환용).
   - `space` / `space-profile`: 디스크 점유율을 줄이는 방향으로 크기 제한 AOT 컴파일.
   - `speed-profile`: Profile `.prof`에 수집된 핫 메서드만 선택적 AOT 컴파일 (권장 기본값).
   - `speed`: 앱의 모든 메서드를 완전한 AOT 네이티브 기계어(`.odex`)로 사전 컴파일.
   - `everything`: 모든 메서드 및 디버그 심볼 정보까지 포함하여 최대 컴파일.
2. **JIT State Inspection**:
   - JIT 컴파일러의 런타임 동작 여부는 System Property `dalvik.vm.usejit` 및 JIT Code Cache 덤프를 통해 파악한다.
3. **Profile State Inspection**:
   - 앱 런타임 실행 중 수집된 가변 프로파일 데이터는 `/data/misc/profiles/cur/0/<package>/primary.prof`에 저장된다.
   - 백그라운드 컴파일 시 합쳐진 기준 참조 프로파일(Reference Profile)은 `/data/misc/profiles/ref/<package>/primary.prof`로 동기화 관리된다.

```mermaid
flowchart LR
    APP["Running App Process"] -->|Inspect JIT Cache| JIT["JIT Code Cache & Compiler Thread"]
    APP -->|Inspect Filter| CF["Compile Filter
(verify / speed-profile / speed)"]
    APP -->|Inspect Profile| PROF["Profile Binary
(/data/misc/profiles/...)"]

    JIT -->|dumpsys meminfo| LOG1["JIT Memory Footprint"]
    CF -->|dumpsys package| LOG2["Installed Filter Target"]
    PROF -->|profman| LOG3["Profile Dump Analysis"]
```

### 코드 및 구체 예시 (Concrete Snippets)

`profman` CLI 툴을 사용한 Profile 파일 바이너리 내용 분석 예시:

```bash
# 프로파일 분석 CLI를 사용하여 프로파일 텍스트 덤프 출력
adb shell profman --dump-only --profile-file=/data/misc/profiles/cur/0/com.example.app/primary.prof
```

### 관측 가능 증거 (Observable Evidence)

`adb shell`을 통해 ART 런타임 컴파일 상태를 다각도로 검증할 수 있다:

```bash
# 1. 대상 앱의 현재 Compile Filter 상태 확인
adb shell dumpsys package com.example.app | grep -i "compiler-filter"
# 출력 예시:
# compilation_filter=speed-profile

# 2. JIT 메모리 점유율 관측
adb shell dumpsys meminfo com.example.app | grep -i "JIT"

# 3. 수동으로 Compile Filter 변경 및 성능 테스트
adb shell cmd package compile -m speed -f com.example.app
adb shell cmd package compile -reset com.example.app
```

### 관련 문서

- [art-runs-dex-with-interpretation-jit-and-aot](art-runs-dex-with-interpretation-jit-and-aot.md)
- [profile-guided-compilation-splits-install-runtime-and-idle-costs](profile-guided-compilation-splits-install-runtime-and-idle-costs.md)

공식 문서: [Evaluating ART Performance](https://source.android.com/docs/core/runtime/art-artifacts)
