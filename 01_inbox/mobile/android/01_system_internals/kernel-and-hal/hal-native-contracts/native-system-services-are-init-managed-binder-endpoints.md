---
title: Native system services are init managed Binder endpoints
tags: [android, android/native, android/system-internals]
aliases: [native service, servicemanager, init.rc]
date modified: 2026-07-31 23:58:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

# Native system services are init managed Binder endpoints

Native system service는 C/C++/Rust로 구현된 process 또는 process 안의 Binder endpoint일 수 있다. HAL과 달리 반드시 hardware abstraction contract를 제공하는 것은 아니며, framework-facing orchestration service인 경우도 많다.

`init`은 `.rc` service definition에 따라 process를 시작하고 class, disabled, oneshot, interface 같은 lifecycle 정보를 적용한다. 반면 `servicemanager`는 Binder object의 이름 등록과 조회를 담당하는 context manager다.

SurfaceFlinger, AudioFlinger, codec 관련 service는 native service의 예시지만, 각각의 HAL이나 driver와 같은 계층은 아니다. 예를 들어 AudioFlinger는 audio framework/native service이고, Audio HAL은 그 아래 hardware-facing contract다.

관련 노트: [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md), [AIDL HAL은 신규 HAL의 현재 stable interface 선택지다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/aidl-hal-is-current-stable-interface-for-new-hals.md)

출처: [AOSP AIDL overview](https://source.android.com/docs/core/architecture/aidl), [AOSP AIDL for HALs](https://source.android.com/docs/core/architecture/aidl/aidl-hals)
