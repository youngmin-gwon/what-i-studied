---
title: mainline-module-updates-do-not-equal-arbitrary-new-public-apis
tags: ["android", "android/system-internals"]
aliases: ["Mainline module update는 임의의 새 public API 배포와 같지 않다"]
date modified: 2026-08-03 17:26:44 +09:00
date created: 2026-07-31 23:05:30 +09:00
---

## Mainline module update 는 임의의 새 public API 배포와 같지 않다

Mainline module update 가 곧 앱이 바로 호출할 수 있는 새 public SDK API 를 뜻하지는 않는다. Mainline module 은 SDK API, System API, stable C API, stable AIDL 같은 compatibility 가 보장되는 경계 안에서 나머지 platform 과 통신해야 한다.

앱 개발자에게 중요한 질문은 "이 module 이 업데이트됐는가"보다 "내가 호출하려는 API 가 이 device 에서 사용 가능한가"다. 이 판단에는 `Build.VERSION.SDK_INT`, SDK Extension version, Jetpack helper, feature check 가 필요할 수 있다.

SDK Extensions 는 이 gap 을 메우기 위한 별도 availability model 이다. Mainline 이 delivery mechanism 이라면 SDK Extensions 는 일부 API 의 compile/runtime availability 를 표현하는 app-facing 계약이다.

관련 노트: [SDK Extensions](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/sdk-extensions-express-api-availability-beyond-sdk-int.md), [앱의 availability check](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apps-should-check-api-feature-availability-not-mainline-package-names.md).

공식 문서: [Mainline](https://source.android.com/docs/core/ota/modular-system), [SDK Extensions](https://developer.android.com/guide/sdk-extensions)
