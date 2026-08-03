---
title: sdk-extension-compile-sdk-extension-and-runtime-check-are-separate-steps
tags: ["android", "android/system-internals"]
aliases: ["SDK Extension API 사용은 compileSdkExtension과 runtime check가 모두 필요하다"]
date modified: 2026-08-03 17:26:49 +09:00
date created: 2026-07-31 23:05:30 +09:00
---

## SDK Extension API 사용은 compileSdkExtension 과 runtime check 가 모두 필요하다

SDK Extension API 를 쓰려면 compile 시점과 runtime 시점을 분리해야 한다. compile 시점에는 필요한 API 를 포함하는 SDK platform 과 `compileSdkExtension` 을 지정해야 하고, runtime 에는 대상 device 의 extension version 이 충분한지 확인해야 한다.

compileSdkExtension 만 올리면 모든 device 에서 해당 API 가 존재한다고 보장되는 것이 아니다. 반대로 device 가 extension version 을 갖고 있어도 앱이 해당 API 를 compile 할 수 있는 SDK 로 빌드되지 않으면 호출할 수 없다.

Lint 와 Android Studio 는 extension version 이 필요한 API 호출을 감지하고 check 생성을 도울 수 있다. 그래도 fallback path 와 feature behavior 는 앱 설계에서 명시해야 한다.

관련 노트: [SDK Extensions](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/sdk-extensions-express-api-availability-beyond-sdk-int.md), [앱 availability check](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apps-should-check-api-feature-availability-not-mainline-package-names.md).

공식 문서: [SDK Extensions](https://developer.android.com/guide/sdk-extensions)
