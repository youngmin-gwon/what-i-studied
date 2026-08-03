---
title: sdk-extensions-express-api-availability-beyond-sdk-int
tags: ["android", "android/system-internals"]
aliases: ["SDK Extensions는 SDK_INT만으로 표현되지 않는 API availability를 나타낸다"]
date modified: 2026-08-03 17:26:49 +09:00
date created: 2026-07-31 23:05:30 +09:00
---

## SDK Extensions 는 SDK_INT 만으로 표현되지 않는 API availability 를 나타낸다

SDK Extensions 는 modular system component update 를 통해 일부 API 가 이전 Android API level 기기에도 제공될 수 있음을 표현한다. Android 11(API 30) 이상 기기는 extension version set 을 가질 수 있고, API reference 에는 어떤 extension version 부터 API 를 쓸 수 있는지가 표시된다.

`Build.VERSION.SDK_INT >= 33` 같은 check 는 여전히 유효하지만, extension API 는 더 낮은 platform API level 에서도 특정 extension version 이상이면 사용 가능할 수 있다. 그래서 SDK_INT 만 보면 false negative 가 생길 수 있다.

앱은 `SdkExtensions.getExtensionVersion(…)` 또는 Jetpack helper 를 사용해 runtime availability 를 확인한다. 이 값은 public API 사용 가능성을 판단하는 계약이지, 개별 Mainline package version 을 직접 추적하라는 뜻이 아니다.

관련 노트: [compile/runtime check](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/sdk-extension-compile-sdk-extension-and-runtime-check-are-separate-steps.md), [앱 availability check](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apps-should-check-api-feature-availability-not-mainline-package-names.md).

공식 문서: [SDK Extensions](https://developer.android.com/guide/sdk-extensions), [SdkExtensions API](https://developer.android.com/reference/android/os/ext/SdkExtensions)
