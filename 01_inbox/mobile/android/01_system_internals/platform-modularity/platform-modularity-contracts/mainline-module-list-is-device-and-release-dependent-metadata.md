# Mainline module 목록은 release와 device에 따라 달라지는 metadata다

Mainline module 목록은 고정된 암기표가 아니다. Android release가 올라가며 module이 추가되고, module package format도 APK 또는 APEX로 다를 수 있으며, device와 build flavor에 따라 Google package name과 AOSP package name이 다를 수 있다.

공식 목록은 adbd, ART, Bluetooth, Conscrypt, DNS Resolver, Media, MediaProvider, PermissionController, SDK Extensions, Time Zone Data, Wi-Fi 같은 module을 포함하지만 이 목록 자체는 최신 문서 확인 대상이다.

기기에서 module identity가 필요하면 ModuleMetadata와 PackageManager가 제공하는 module metadata를 확인하는 쪽이 맞다. 앱 기능 분기는 package name 나열보다 API/feature availability check를 우선한다.

관련 노트: [ModuleMetadata](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/modulemetadata-describes-mainline-modules-on-a-device.md), [앱 availability check](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apps-should-check-api-feature-availability-not-mainline-package-names.md).

공식 문서: [Mainline available modules](https://source.android.com/docs/core/ota/modular-system), [ModuleMetadata](https://source.android.com/docs/core/ota/modular-system/metadata)
