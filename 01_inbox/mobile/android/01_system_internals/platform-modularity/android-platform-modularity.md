---
title: "Android Platform Modularity"
tags: ["android", "android/system-internals"]
aliases: ["Android Platform Modularity"]
date modified: 2026-08-03 16:30:00 +09:00
date created: 2026-07-31 23:05:30 +09:00
---

# Android Platform Modularity

Android platform modularity는 앱 구조가 아니라 OS update, compatibility, fragmentation 경계를 설명하는 system internals 주제다.

## 정본 노트

- [Android 플랫폼 모듈화는 system, vendor, kernel 업데이트 경계를 층위별로 나눈다](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/android-platform-modularity-splits-update-boundaries-by-system-layer.md)
- [Mainline은 선택된 system component를 정규 플랫폼 release 밖에서 업데이트한다](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/mainline-updates-selected-system-components-outside-normal-platform-releases.md)
- [Mainline module update는 임의의 새 public API 배포와 같지 않다](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/mainline-module-updates-do-not-equal-arbitrary-new-public-apis.md)
- [Mainline module 목록은 release와 device에 따라 달라지는 metadata다](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/mainline-module-list-is-device-and-release-dependent-metadata.md)
- [APEX는 APK 모델로 다루기 어려운 lower-level system module을 담는다](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apex-packages-lower-level-system-modules-that-apk-cannot-model-well.md)
- [APEX activation은 boot-time mount, version selection, rollback 경계다](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apex-activation-uses-boot-time-mounting-version-selection-and-rollback.md)
- [APEX build와 device support는 앱 개발 API가 아니라 플랫폼 통합 계약이다](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apex-build-and-device-support-are-platform-integration-contracts.md)
- [SDK Extensions는 SDK_INT만으로 표현되지 않는 API availability를 나타낸다](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/sdk-extensions-express-api-availability-beyond-sdk-int.md)
- [SDK Extension API 사용은 compileSdkExtension과 runtime check가 모두 필요하다](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/sdk-extension-compile-sdk-extension-and-runtime-check-are-separate-steps.md)
- [ModuleMetadata는 기기에 있는 Mainline module 목록을 설명한다](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/modulemetadata-describes-mainline-modules-on-a-device.md)
- [앱은 Mainline package 이름보다 API와 feature availability를 확인해야 한다](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apps-should-check-api-feature-availability-not-mainline-package-names.md)

## 이미 존재하는 인접 정본

- [Treble separates system and vendor through stable interfaces](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/treble-separates-system-and-vendor-through-stable-interfaces.md)
- [VINTF declares framework/vendor compatibility](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/vintf-declares-framework-vendor-compatibility.md)
- [GKI splits generic core from vendor modules](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/gki-splits-generic-core-from-vendor-modules.md)
- [KMI stability](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/kmi-is-stable-only-within-a-gki-lts-and-android-branch.md)

## 읽는 기준

Mainline/APEX/SDK Extensions는 이 map에서 읽는다. HAL/VINTF/Treble은 [HAL/native boundary 정본](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hal-native-contracts.md)에서 읽고, GKI/KMI는 [kernel 정본](01_inbox/mobile/android/01_system_internals/kernel-and-hal/android-kernel-runtime.md)에서 읽는다.

## 문제 분류 기준

- "이 API가 왜 이 기기에서만 없지"처럼 앱 API 존재 여부가 궁금하면 -> [SDK Extensions](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/sdk-extensions-express-api-availability-beyond-sdk-int.md)와 [앱은 Mainline package 이름보다 API와 feature availability를 확인해야 한다](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apps-should-check-api-feature-availability-not-mainline-package-names.md)로 간다.
- OTA/Play system update 이후 기기 동작이 바뀌었다면 -> [Mainline](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/mainline-updates-selected-system-components-outside-normal-platform-releases.md)과 [APEX activation](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apex-activation-uses-boot-time-mounting-version-selection-and-rollback.md)으로 간다.
- 플랫폼/기기 빌드 관점에서 module을 새로 추가하거나 지원해야 한다면 -> [APEX build/device support](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apex-build-and-device-support-are-platform-integration-contracts.md)로 간다. 이는 앱 개발자 질문이 아니다.
- 이 영역은 대부분 앱 코드가 제어할 수 없는 platform 계층이므로, 판단은 항상 "이 device/release에서 무엇이 관찰되는가"(module 목록, extension version, dumpsys)로 시작한다.

공식 문서: [Mainline](https://source.android.com/docs/core/ota/modular-system), [APEX file format](https://source.android.com/docs/core/ota/apex), [SDK Extensions](https://developer.android.com/guide/sdk-extensions)
