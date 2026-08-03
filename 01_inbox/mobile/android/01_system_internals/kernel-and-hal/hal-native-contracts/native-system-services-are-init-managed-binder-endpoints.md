---
title: native-system-services-are-init-managed-binder-endpoints
tags: [android, android/native, android/system-internals]
aliases: [init.rc, native service, servicemanager]
date modified: 2026-08-03 17:25:49 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

## Native system services are init managed Binder endpoints

Native system service 는 C/C++/Rust 로 구현된 process 또는 process 안의 Binder endpoint 일 수 있다. HAL 과 달리 반드시 hardware abstraction contract 를 제공하는 것은 아니며, framework-facing orchestration service 인 경우도 많다.

`init` 은 `.rc` service definition 에 따라 process 를 시작하고 class, disabled, oneshot, interface 같은 lifecycle 정보를 적용한다. 반면 `servicemanager` 는 Binder object 의 이름 등록과 조회를 담당하는 context manager 다.

SurfaceFlinger, AudioFlinger, codec 관련 service 는 native service 의 예시지만, 각각의 HAL 이나 driver 와 같은 계층은 아니다. 예를 들어 AudioFlinger 는 audio framework/native service 이고, Audio HAL 은 그 아래 hardware-facing contract 다.

관련 노트: [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md), [AIDL HAL은 신규 HAL의 현재 stable interface 선택지다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/aidl-hal-is-current-stable-interface-for-new-hals.md)

출처: [AOSP AIDL overview](https://source.android.com/docs/core/architecture/aidl), [AOSP AIDL for HALs](https://source.android.com/docs/core/architecture/aidl/aidl-hals)
