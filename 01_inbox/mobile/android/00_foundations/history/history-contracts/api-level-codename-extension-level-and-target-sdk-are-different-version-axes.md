---
title: api-level-codename-extension-level-and-target-sdk-are-different-version-axes
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-03 17:22:14 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

## API level, codename, extension level, targetSdkVersion 은 서로 다른 version 축이다

Android version 을 말할 때 API level, dessert codename, SDK Extension level, minor SDK version, `compileSdk`, `targetSdkVersion` 을 섞으면 판단이 흐려진다. API level 은 platform SDK surface 의 major 번호이고, codename 은 release 식별자다. extension level 은 Mainline module 을 통해 추가된 일부 API availability 를, `SDK_INT_FULL` 은 major/minor platform release 를 구분한다.

`compileSdk` 는 소스가 어떤 SDK API 로 compile 될 수 있는지 정하고, `targetSdkVersion` 은 앱에 적용할 target-gated behavior contract 를 선택한다. device 가 Android 17 이어도 target 이 낮으면 일부 동작은 compatibility behavior 를 거칠 수 있지만, 모든 앱에 적용되는 runtime 변화까지 피하는 것은 아니다. Extension API 는 device API level 과 별도로 extension version 조건을 만족하는지 검사한다.

2026 년 8 월 3 일 검증 기준 API 36 은 Android 16/Baklava, API 37 은 Android 17/Cinnamon Bun 으로 문서화되어 있다. `SDK_INT_FULL` 과 `VERSION_CODES_FULL` 은 API level 36 에 추가되었으며 minor release 를 포함한 순서를 표현한다. 구체 상수와 배포 상태는 사용 시점의 공식 reference 에서 다시 확인한다.

관련 노트: [SDK Extensions](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/sdk-extensions-express-api-availability-beyond-sdk-int.md), [packaging/deployment](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md).

공식 문서(2026-08-03 검증): [Build.VERSION](https://developer.android.com/reference/android/os/Build.VERSION), [Build.VERSION_CODES](https://developer.android.com/reference/android/os/Build.VERSION_CODES), [VERSION_CODES_FULL](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES_FULL)
