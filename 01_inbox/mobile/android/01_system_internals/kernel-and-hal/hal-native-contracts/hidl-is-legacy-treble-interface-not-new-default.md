---
title: hidl-is-legacy-treble-interface-not-new-default
tags: [android, android/native, android/system-internals]
aliases: [HIDL]
date modified: 2026-08-03 17:25:44 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

## HIDL is legacy Treble interface not new default

HIDL 은 Treble 시대에 HAL interface 를 명시적으로 정의하고 versioning 과 Binder IPC 를 제공하기 위해 도입된 HAL interface definition language 다. Android 8 이후 HAL 을 system/vendor 경계에서 안정적으로 호출하기 위한 중요한 전환점이었다.

하지만 현재 신규 HAL 의 기본 방향은 HIDL 이 아니다. AOSP HIDL 문서는 "As of Android 10, HIDL is deprecated and has been replaced by AIDL"이라고 명시하며, 가능한 경우 HAL 을 AIDL 로 전환하라고 안내한다. AIDL 이 HAL 구현에 쓰일 수 있게 된 시점은 Android 11 이므로, deprecation 선언과 대체 경로가 널리 쓰이기 시작한 시점 사이에는 시차가 있다. 기존 HIDL HAL 은 여전히 지원될 수 있으므로 "HIDL 이 사라졌다"가 아니라 "신규 선택의 중심이 AIDL 로 이동했다"가 정확하다.

HIDL 자체와 binderized/passthrough 실행 형태를 섞어 말하지 않는 것이 중요하다. HIDL HAL 도 process boundary 를 어떻게 두는지에 따라 호출 비용, crash 영향, SELinux 경계가 달라진다.

관련 노트: [AIDL HAL은 신규 HAL의 현재 stable interface 선택지다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/aidl-hal-is-current-stable-interface-for-new-hals.md), [Binderized HAL과 passthrough HAL은 process boundary를 다르게 둔다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/binderized-and-passthrough-hal-define-process-boundary.md)

출처: [AOSP HIDL](https://source.android.com/docs/core/architecture/hidl), [AOSP HAL overview](https://source.android.com/docs/core/architecture/hal)
