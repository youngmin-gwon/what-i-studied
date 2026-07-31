---
title: HAL is a stable userspace contract between framework and vendor
tags: [android, android/native, android/system-internals]
aliases: [HAL, Hardware Abstraction Layer]
date modified: 2026-07-31 23:58:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

HAL은 하드웨어 제조사 구현을 Android framework 코드와 분리하기 위한 표준 userspace interface다. HAL service가 kernel driver를 호출할 수는 있지만, HAL 자체를 kernel wrapper나 driver와 동일시하면 계층이 흐려진다.

Framework 또는 system component는 HAL client가 되고, vendor/device-specific 구현은 HAL service가 된다. 핵심은 카메라, 오디오, 센서 같은 하드웨어별 차이를 framework가 직접 알지 않아도 된다는 점이다.

Android 8 이전에도 HAL은 존재했지만, Treble 이후 HAL interface와 cross-partition 호환성의 의미가 훨씬 강해졌다. AOSP HAL overview는 HAL을 lower-level device-specific 기능을 higher-level layer와 분리하는 표준 interface로 설명한다.

관련 노트: [Treble은 system과 vendor 업데이트 경계를 stable interface로 분리한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/treble-separates-system-and-vendor-through-stable-interfaces.md), [Android kernel runtime](01_inbox/mobile/android/01_system_internals/kernel-and-hal/android-kernel-runtime.md)

출처: [AOSP HAL overview](https://source.android.com/docs/core/architecture/hal)
