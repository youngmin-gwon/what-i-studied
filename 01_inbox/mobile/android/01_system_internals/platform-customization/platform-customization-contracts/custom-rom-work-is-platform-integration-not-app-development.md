---
title: "Custom ROM 작업은 앱 개발이 아니라 플랫폼 통합이다"
tags: [android, android/aosp, android/custom-rom]
aliases: [Custom ROM]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Custom ROM 작업은 앱 개발이 아니라 플랫폼 통합이다

상위 문서: [Platform customization contracts](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md)

Custom ROM 작업은 UI 테마나 앱 패키지 교체만이 아니라 device tree, kernel, vendor blobs, HAL, sepolicy, signing, OTA, compatibility test를 함께 다루는 플랫폼 통합 작업이다.

기존 ROM 프로젝트의 build command만 따라 하면 특정 device에서는 부팅해도 camera, modem, fingerprint, DRM, payment, Play certification 같은 경계가 깨질 수 있다. ROM 문서는 항상 device support와 certification/fallback 여부를 분리해야 한다.

## 실무 규칙

- device tree와 vendor blob 출처, license, update 가능성을 기록한다.
- kernel/HAL 변경은 VINTF와 sepolicy 변경까지 추적한다.
- GMS 포함 여부와 Play certification 상태를 명확히 분리한다.
- userdebug 편의 설정을 production security posture로 착각하지 않는다.

관련 노트: [Device bring-up은 board, kernel, HAL, VINTF, sepolicy 통합이다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/device-bring-up-is-board-kernel-hal-vintf-and-sepolicy-integration.md), [GMS는 AOSP가 아니라 라이선스된 Google services layer다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/gms-is-licensed-google-services-layer-not-aosp.md)
