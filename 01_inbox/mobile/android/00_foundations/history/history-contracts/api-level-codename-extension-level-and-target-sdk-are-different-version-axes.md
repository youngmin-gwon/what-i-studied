---
title: api-level-codename-extension-level-and-target-sdk-are-different-version-axes
tags: ["android", "android/foundations"]
aliases: []
date modified: 2026-08-01 01:08:01 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

## API level, codename, extension level, targetSdkVersion 은 서로 다른 version 축이다

Android version 을 말할 때 API level, dessert codename, SDK Extension level, targetSdkVersion 을 섞으면 판단이 흐려진다. API level 은 platform SDK surface 의 큰 번호이고, codename 은 release 식별자이며, extension level 은 module update 를 통해 제공되는 일부 API availability 를 표현한다.

targetSdkVersion 은 앱이 어떤 behavior-change contract 를 수락하는지 나타낸다. device 가 Android 17 이어도 앱 target 이 낮으면 일부 동작은 compatibility mode 를 거칠 수 있고, 반대로 extension API 는 낮은 API level 기기에서도 extension version 조건을 만족하면 사용할 수 있다.

2026 년 기준 API 36 은 Android 16/Baklava, API 37 은 Android 17/Cinnamon Bun 으로 문서화되어 있다. Android 16 부터 minor SDK version 축도 `VERSION_CODES_FULL` 에 드러난다.

관련 노트: [SDK Extensions](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/sdk-extensions-express-api-availability-beyond-sdk-int.md), [packaging/deployment](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md).

공식 문서: [Build.VERSION_CODES](https://developer.android.com/reference/android/os/Build.VERSION_CODES), [VERSION_CODES_FULL](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES_FULL)
