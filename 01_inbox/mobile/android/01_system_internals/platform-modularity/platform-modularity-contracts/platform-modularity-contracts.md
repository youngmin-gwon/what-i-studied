---
title: "Platform Modularity Contracts"
tags: ["android", "android/system-internals"]
---

# Platform Modularity Contracts

Android platform modularity를 update boundary별로 나눈 정본 모음이다.

## Notes

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
