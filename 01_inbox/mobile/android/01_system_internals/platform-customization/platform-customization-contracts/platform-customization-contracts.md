---
title: Platform customization contracts
tags: [android, android/aosp, android/system-internals]
aliases: [Android platform customization, AOSP customization]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

Android platform customization은 앱 설정 문제가 아니라 AOSP source, product configuration, partition ownership, vendor boundary, signing, compatibility test가 맞물리는 플랫폼 통합 문제다.

## 정본 노트

- [AOSP는 완성된 Google 기기 경험이 아니라 기본 플랫폼이다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/aosp-is-base-platform-not-complete-google-device-experience.md)
- [product, vendor, odm, system_ext는 customization ownership을 나눈다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/product-vendor-odm-and-system-ext-split-customization-ownership.md)
- [product configuration은 package, property, permission, overlay를 선택한다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/product-configuration-selects-packages-properties-permissions-and-overlays.md)
- [RRO는 target APK를 다시 빌드하지 않고 resource를 바꾼다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/rro-changes-resources-without-rebuilding-target-apk.md)
- [GMS는 AOSP가 아니라 라이선스된 Google services layer다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/gms-is-licensed-google-services-layer-not-aosp.md)
- [AOSP build는 source, device, vendor configuration으로 product image를 조립한다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/aosp-build-assembles-product-images-from-source-device-and-vendor-configuration.md)
- [Device bring-up은 board, kernel, HAL, VINTF, sepolicy 통합이다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/device-bring-up-is-board-kernel-hal-vintf-and-sepolicy-integration.md)
- [Platform compatibility test는 앱 기능이 아니라 device contract를 검증한다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-compatibility-tests-validate-device-contracts-not-app-features.md)
- [Platform signing과 release key는 update와 privilege boundary를 정의한다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-signing-and-release-keys-define-update-and-privilege-boundaries.md)
- [OEM API는 stable contract가 없으면 compatibility risk다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/oem-api-is-compatibility-risk-unless-backed-by-stable-contract.md)
- [Custom ROM 작업은 앱 개발이 아니라 플랫폼 통합이다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/custom-rom-work-is-platform-integration-not-app-development.md)
- [Platform debugging은 build, boot, service, VINTF, sepolicy, CTS를 분리한다](01_inbox/mobile/android/01_system_internals/platform-customization/platform-customization-contracts/platform-debugging-separates-build-boot-service-vintf-sepolicy-and-cts.md)

## 다른 정본으로 넘길 경계

- Treble, VINTF, HAL 구현은 [HAL native contracts](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hal-native-contracts.md)로 둔다.
- Mainline, APEX, SDK Extension은 [Platform Modularity Contracts](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/platform-modularity-contracts.md)로 둔다.
- AVB와 boot chain은 [AVB는 부팅 이미지의 신뢰와 rollback 방지를 검증한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/boot-flow-contracts/avb-verifies-boot-images-and-rollback-protection.md)로 둔다.
- 앱 release, Play 배포, APK/AAB signing은 [Release distribution contracts](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/release-distribution-contracts.md)로 둔다.
