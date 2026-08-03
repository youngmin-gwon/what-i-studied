---
title: "Device bring-up은 board, kernel, HAL, VINTF, sepolicy 통합이다"
tags: [android, android/aosp, android/device]
aliases: [Android device bring-up]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Device bring-up은 board, kernel, HAL, VINTF, sepolicy 통합이다

상위 문서: [Platform customization contracts](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md)

Device bring-up은 Android image가 특정 하드웨어에서 부팅하고 핵심 기능을 안정적으로 노출하도록 board config, bootloader, kernel, device tree, HAL, VINTF, init rc, sepolicy를 맞추는 과정이다.

핵심은 “코드가 컴파일되는가”가 아니라 각 boundary가 서로 호환되는가다. HAL이 등록되지 않으면 framework service가 기능을 찾지 못하고, sepolicy가 맞지 않으면 service가 실행되어도 필요한 파일이나 Binder service에 접근하지 못한다.

## 실무 규칙

- bring-up 문제는 boot, init service, HAL registration, VINTF, sepolicy 순서로 좁힌다.
- kernel log와 init log는 logcat보다 먼저 필요한 경우가 많다.
- device manifest와 framework compatibility matrix를 함께 검증한다.
- 임시 permissive나 broad allow rule은 원인 분석용으로만 제한한다.

관련 노트: [VINTF는 framework/vendor 호환성을 선언한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/vintf-declares-framework-vendor-compatibility.md), [GKI는 공통 core kernel과 vendor module을 분리한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/gki-splits-generic-core-from-vendor-modules.md)
