---
title: A3-kernel-hal-driver
tags: [android, system_internals, kernel, hal, drivers]
aliases: [A3: 커널·HAL·드라이버 계층, Kernel and HAL Layer, Android OS Foundations]
date created: 2026-08-04 16:00:00 +09:00
date modified: 2026-08-04 21:30:00 +09:00
---

## A3. 커널·HAL·드라이버 계층 (Kernel, HAL, and Driver)

이 문서는 Android 플랫폼의 최하단에 위치한 커널과 하드웨어 추상화 계층(HAL), 그리고 드라이버 간의 상호작용을 통합적으로 이해하기 위한 주제 합성(Topic Synthesis) 문서입니다. 소프트웨어 프레임워크가 실제 디바이스 하드웨어를 어떻게 안전하고 일관된 방식으로 제어하는지 그 계약을 설명합니다.

### 1. 이 주제를 읽기 전에

안드로이드 플랫폼의 전체 실행 계층에 대한 기본적인 이해가 선행되어야 합니다. 특히 시스템 서비스(System Services)가 어떻게 하드웨어 기능에 접근하는지, 그리고 프로세스 격리와 보안 정책이 어떻게 적용되는지에 대한 배경지식이 필요합니다.

### 2. 전체 조망도

```mermaid
graph TD
    Framework[Android Framework (Java/Kotlin)]
    SystemServices[System Services (C++/Java)]
    HAL[Hardware Abstraction Layer (HAL)]
    Kernel[Android Kernel (Linux + GKI)]
    Drivers[Vendor Kernel Drivers]
    Hardware[Physical Hardware]

    Framework -->|Binder IPC| SystemServices
    SystemServices -->|AIDL/HIDL| HAL
    HAL -->|Syscalls/IOCTL| Kernel
    Kernel -->|VFS/Subsystem| Drivers
    Drivers -->|Register Access| Hardware
    
    classDef framework fill:#e3f2fd,stroke:#1e88e5;
    classDef hal fill:#fff3e0,stroke:#fb8c00;
    classDef kernel fill:#e8f5e9,stroke:#43a047;
    class Framework,SystemServices framework;
    class HAL hal;
    class Kernel,Drivers kernel;
```

### 3. 하위 개념 및 원자 노트 합성

커널과 HAL 계층은 시스템의 안정성, 호환성, 전력 관리의 핵심입니다. 프레임워크는 HAL을 통해 하드웨어를 추상화하고, 커널은 시스템 자원을 스케줄링하고 보호합니다.

*   **HAL과 벤더 분리 (Treble & HAL Contracts)**
    안드로이드 프레임워크와 벤더 하드웨어 구현 간의 의존성을 끊기 위해 Project Treble이 도입되었습니다. HAL은 안정적인 IPC 인터페이스(AIDL/HIDL)를 제공하며, 시스템 업데이트 시 하위 호환성을 보장하는 핵심 계약입니다.
    *   [HAL은 framework와 vendor 구현 사이의 안정된 userspace contract다](../../01_system_internals/kernel-and-hal/hal-native-contracts/hal-is-stable-userspace-contract-between-framework-and-vendor.md): HAL은 프레임워크와 벤더 간의 안정적인 유저스페이스 계약입니다.
    *   [Treble은 system과 vendor 업데이트 경계를 stable interface로 분리한다](../../01_system_internals/kernel-and-hal/hal-native-contracts/treble-separates-system-and-vendor-through-stable-interfaces.md): Treble은 안정된 인터페이스를 통해 시스템과 벤더를 분리합니다.
    *   [AIDL HAL 은 신규 HAL 의 현재 stable interface 표준이다](../../01_system_internals/kernel-and-hal/hal-native-contracts/aidl-hal-is-current-stable-interface-for-new-hals.md): AIDL HAL은 최신 HAL 구현을 위한 안정적인 인터페이스 표준입니다.

*   **Android 커널과 GKI (Generic Kernel Image)**
    안드로이드 커널은 리눅스 메인라인 커널을 기반으로 모바일 환경에 필요한 정책(전력, 메모리 등)을 추가한 형태입니다. GKI는 핵심 커널 코어와 벤더 모듈을 분리하여 커널 파편화를 줄이고 업데이트를 용이하게 합니다.
    *   [Android kernel은 Linux에 모바일 플랫폼 정책을 더한 커널이다](../../01_system_internals/kernel-and-hal/kernel-contracts/android-kernel-is-linux-plus-mobile-platform-policy.md): 안드로이드 커널은 리눅스 커널에 모바일 플랫폼 정책을 더한 것입니다.
    *   [GKI는 공통 core kernel과 vendor module을 분리한다](../../01_system_internals/kernel-and-hal/kernel-contracts/gki-splits-generic-core-from-vendor-modules.md): GKI는 제네릭 코어 커널과 벤더 특화 모듈을 분리합니다.

*   **전력 관리 및 백그라운드 정책 (Wakelocks)**
    안드로이드 커널의 특징 중 하나는 적극적인 전력 관리입니다. 시스템은 기본적으로 깊은 수면(Deep Sleep) 상태로 전환되려 하며, 프로세스는 이를 막기 위해 Wakelock과 같은 커널 수준의 블로커를 사용해야 합니다.
    *   [Wakelock은 background work 권한이 아니라 suspend blocker다](../../01_system_internals/kernel-and-hal/kernel-contracts/wakelocks-are-suspend-blockers-not-background-work-permission.md): Wakelock은 단순히 백그라운드 작업 권한이 아니라 커널의 Suspend 블로커입니다.

### 4. 이 주제와 연결된 Worked Example

실제 앱 동작 과정에서 HAL과 커널이 어떻게 관여하는지 구체적인 사례를 통해 확인합니다.
*   [사진 촬영, preview, 저장, 업로드까지 (Photo Capture, Preview, Save, and Upload)](../worked-examples/02-photo-capture-preview-save-upload.md): Camera HAL이 센서 하드웨어와 어떻게 통신하고 버퍼를 프레임워크로 전달하는지 볼 수 있습니다.
*   [process death 뒤 편집 상태와 background work 복구](../worked-examples/05-process-death-recovery-of-edit-state-and-background-work.md): 메모리 압박 시 커널(LMKD)이 어떻게 프로세스를 종료시키고 상태를 보존하는지에 대한 사례입니다.

### 5. 이 주제와 연결된 Diagnostic Runbook

커널 및 HAL 계층의 문제(예: 드라이버 오동작, 시스템 자원 고갈 등)를 진단하기 위한 런북입니다.
*   [ANR(Application Not Responding)이 발생한다](../diagnostic-runbooks/02-anr.md): 느린 I/O나 커널 수준의 락으로 인해 발생할 수 있는 시스템 응답 지연을 진단합니다.
*   [백그라운드 작업이 지연되거나 실행되지 않는다](../diagnostic-runbooks/05-background-work-delayed-or-not-running.md): 기기 수면 상태 및 Wakelock 실패로 인한 백그라운드 작업 지연을 파악합니다.

### 6. 더 깊이 들어갈 때 (Learning Spine)

커널과 HAL 계층을 넘어 플랫폼의 실행 계층 전반과 하드웨어 접근 제어로 지식을 확장하려면 다음 챕터를 학습하세요.
*   [Android 플랫폼 실행 계층과 호출 경로](../learning-spine/02-android-platform-execution-layers-and-call-paths.md)
*   [기기 기능 발견과 background execution](../learning-spine/10-device-capability-discovery-and-background-execution.md)
