---
title: android-kernel-is-linux-plus-mobile-platform-policy
tags: [android, android/kernel, linux]
aliases: [Android Kernel, 안드로이드 커널]
date modified: 2026-08-05 14:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

## Android kernel 은 Linux 에 모바일 플랫폼 정책을 더한 커널이다

상위 문서: [Kernel contracts](kernel-contracts.md)

배경 지식: [IPC](../../../../../operating-systems/ipc-mechanisms.md), [DAC](../../../../../../02_references/operating-systems/kernel.md), [SELinux/MAC](../../../../../linux/security/selinux.md)

Android kernel 은 upstream Linux LTS(Long Term Support)를 기반으로 하지만, 배터리 구동 환경의 제약, 다수의 앱 샌드박싱, 저지연 그래픽 zero-copy, 엄격한 하드웨어 액세스 보안을 만족하도록 모바일 플랫폼 정책을 추가/개조한 커널이다.

핵심 차이는 "Linux 와 완전히 분리된 OS 커널"이 아니라, "대규모 모바일 제품 출하를 위해 Linux kernel 핵심 기능을 수용하고 그 위에 Android 고유 서브시스템(Binder, Energy Aware Scheduler, SystemSuspend, PSI/LMKD, DMA-BUF heaps)을 통합했다"는 점이다.

---

### 메커니즘: Standard Linux vs Android Kernel 서브시스템 비교

```mermaid
graph TD
    subgraph Upstream Linux Kernel
        A1[System V IPC / Unix Domain Sockets]
        A2[ACPI / Standard Suspend]
        A3[Standard OOM Killer]
        A4[Standard DAC / POSIX Permissions]
    end
    subgraph Android Kernel Platform Policy
        B1"[binder ipc (/dev/binderfs)\n(Kernel-mediated capability & zero-copy transfer)"]
        B2["SystemSuspend / Suspend Blockers\n(Wakelocks & Autosleep)"]
        B3["PSI (Pressure Stall Information) + LMKD\n(Userspace Memory Reclaim)"]
        B4["SELinux MAC Policy + Android Sandbox\n(App Isolation by UID/GID)"]
    end
    A1 <--> B1
    A2 <--> B2
    A3 <--> B3
    A4 <--> B4
```

1. **[IPC](../../../../../operating-systems/ipc-mechanisms.md) & RPC**: 일반 Linux 가 Socket/Pipe/Message Queue 위주인 반면, Android 는 커널 드라이버 수준에서 오브젝트 참조 변환과 권한 주입을 처리하는 `binderfs` 를 핵심 IPC 로 채택.
2. **전력 관리 (Power Management)**: 사용자가 입력을 멈추면 디바이스를 즉시 딥 슬립(Suspend-to-RAM) 상태로 전원 전환하는 `SystemSuspend` 및 `autosleep` 서브시스템 동작. 일반 Linux 의 ACPI 기반 표준 suspend 와 달리, Android 는 앱이 wakelock 을 명시적으로 걸지 않는 한 적극적으로 재운다.
3. **메모리 회수 (Memory Reclaim)**: 전통적인 커널 internal OOM Killer 대신 kernel PSI(Pressure Stall Information) 서브시스템이 메모리 실시간 경합을 감지하고, userspace daemon 인 `lmkd` 가 프로세스 중요도(oom_adj)에 따라 사전에 킬 수행.
4. **공유 메모리 (Shared Buffer)**: 과거 `ashmem` 및 `ION` 에서 modern Linux 의 `DMA-BUF heaps` 규격으로 통합되어 GPU, Display, Camera 간 버퍼 복사 없는(Zero-copy) 그래픽 메모리 전달.
5. **권한 모델**: 일반 Linux 는 파일 소유자가 권한을 결정하는 [DAC](../../../../../../02_references/operating-systems/kernel.md)만으로도 동작하지만, Android 는 그 위에 [SELinux MAC](../../../../../linux/security/selinux.md) 정책을 강제로 얹는다 — 프로세스가 root 권한을 얻어도 SELinux 정책이 파일 접근을 차단할 수 있다는 점이 DAC 단독 모델과의 핵심 차이다.

---

### Android 커널 드라이버 마운트 및 바인딩 예시

```cpp
// Kernel Binderfs 마운트 및 노드 생성 예시 (System init 단계)
#include <sys/mount.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

void init_binderfs() {
    // 1. binderfs 가상 파일시스템 마운트
    mkdir("/dev/binderfs", 0755);
    mount("binder", "/dev/binderfs", "binder", MS_NODEV | MS_NOEXEC | MS_NOSUID, NULL);

    // 2. /dev/binder 심볼릭 링크 생성 (기존 호환성 유지를 위함)
    symlink("/dev/binderfs/binder", "/dev/binder");
    symlink("/dev/binderfs/hwbinder", "/dev/hwbinder");
    symlink("/dev/binderfs/vndbinder", "/dev/vndbinder");
}
```

---

### 실무 규칙

- 앱 개발자는 대부분 Framework Java/Kotlin API 수준에서 자원을 사용하지만, ANR, 메모리 킬(LMK), 그래픽 프레임 드랍(Jank), 배터리 소모(WakeLock Leak) 현상을 추적할 때는 커널 서브시스템의 관측 신호까지 내려가 분석해야 한다.
- Android 커널 수정은 과거의 임의적인 모듈 커스텀 방식에서 벗어나, GKI(Generic Kernel Image) 가이드라인에 따라 KMI(Kernel Module Interface)를 준수하는 모듈 구조로 구현되어야 한다.

---

### 관측 가능한 증거 (Observable Evidence)

1. **Android 전용 가상 파일시스템 마운트 상태 확인**:
   ```bash
   adb shell cat /proc/filesystems | grep -E "binder|pstore|selinuxfs"
   # nodev binder
   # nodev selinuxfs
   # nodev pstore
   ```
2. **Binderfs 노드 활성화 상태 검증**:
   ```bash
   adb shell ls -la /dev/binderfs
   # crw-rw-rw- 1 root root 511, 0 binder
   # crw-rw-rw- 1 root root 511, 1 hwbinder
   # crw-rw-rw- 1 root root 511, 2 vndbinder
   ```
3. **Wakelock 커널 활성화 서브시스템 노드 조회**:
   ```bash
   adb shell cat /sys/power/wake_lock
   # 활성화된 suspend blocker 목록 출력
   ```

---

### 관련 문서

- [ACK는 upstream LTS와 Android release를 잇는다](android-common-kernel-bridges-upstream-lts-and-android-releases.md)
- [GKI는 공통 core kernel과 vendor module을 분리한다](gki-splits-generic-core-from-vendor-modules.md)
- [HAL은 framework와 vendor 구현 사이의 안정된 userspace contract다](../hal-native-contracts/hal-is-stable-userspace-contract-between-framework-and-vendor.md)

공식 문서: [AOSP Kernel Architecture](https://source.android.com/docs/core/architecture/kernel)
