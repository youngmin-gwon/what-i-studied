---
title: "AOSP build는 source, device, vendor configuration으로 product image를 조립한다"
tags: [android, android/aosp, android/build]
aliases: [AOSP build]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# AOSP build는 source, device, vendor configuration으로 product image를 조립한다

상위 문서: [Platform customization contracts](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md)

AOSP build는 앱 하나를 컴파일하는 작업이 아니라 platform source, device tree, kernel/vendor artifact, product configuration을 묶어 boot/system/vendor/product 같은 image를 만드는 작업이다.

그래서 실패 원인도 Gradle 앱 빌드와 다르다. source sync, lunch target, Soong/Make module graph, generated intermediates, signing key, partition size, sepolicy, VINTF manifest가 모두 build 결과에 영향을 준다.

## 실무 규칙

- build target은 제품 정의와 partition 결과물을 함께 의미한다.
- Soong/Make module 이름 충돌과 visibility를 먼저 확인한다.
- vendor blob이나 kernel artifact가 없으면 framework source만으로 device image를 완성할 수 없다.
- 빌드 성공은 boot 성공, CTS 통과, OTA 가능성을 보장하지 않는다.

관련 노트: [Device bring-up은 board, kernel, HAL, VINTF, sepolicy 통합이다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/device-bring-up-is-board-kernel-hal-vintf-and-sepolicy-integration.md)
