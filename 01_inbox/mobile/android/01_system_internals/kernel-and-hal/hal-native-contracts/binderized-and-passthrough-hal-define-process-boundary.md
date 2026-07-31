---
title: Binderized and passthrough HAL define process boundary
tags: [android, android/native, android/system-internals]
aliases: [Binderized HAL, Passthrough HAL]
date modified: 2026-07-31 23:58:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

Binderized HAL은 HAL service가 client와 다른 process에서 Binder IPC로 호출되는 형태다. process가 분리되면 crash isolation, SELinux domain 분리, service registration 같은 장점이 생기지만 IPC 비용과 lifecycle 관리도 생긴다.

Passthrough HAL은 client process 안에서 HAL 구현을 직접 호출하는 형태다. legacy 구현을 감싸거나 제한된 same-process HAL로 쓰일 수 있지만, 모든 HAL이 별도 process라고 말하면 이 예외를 놓친다.

따라서 “HAL crash가 system server를 죽이지 않는다”는 문장은 binderized HAL에 대해서만 조심스럽게 쓸 수 있다. process boundary가 어디에 있는지 확인해야 crash 영향과 보안 경계를 판단할 수 있다.

관련 노트: [HIDL은 legacy Treble interface이지 신규 기본값이 아니다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hidl-is-legacy-treble-interface-not-new-default.md), [Native service 디버깅은 init, Binder, VINTF, SELinux, tombstone을 분리한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/native-service-debugging-separates-init-binder-vintf-selinux-and-tombstones.md)

출처: [AOSP HAL overview](https://source.android.com/docs/core/architecture/hal)
