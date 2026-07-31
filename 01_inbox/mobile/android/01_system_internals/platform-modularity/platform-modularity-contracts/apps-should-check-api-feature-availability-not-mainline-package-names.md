---
title: "앱은 Mainline package 이름보다 API와 feature availability를 확인해야 한다"
tags: ["android", "android/system-internals"]
---

# 앱은 Mainline package 이름보다 API와 feature availability를 확인해야 한다

앱 코드가 관심 가져야 하는 것은 보통 `com.android.wifi`나 `com.android.sdkext` 같은 package 이름 자체가 아니라 사용할 기능이 현재 device에서 안전하게 사용 가능한지다.

API 호출은 `Build.VERSION.SDK_INT`, `SdkExtensions.getExtensionVersion`, Jetpack compatibility helper, `PackageManager.hasSystemFeature`, permission/runtime 상태를 조합해 확인한다. module package version이나 Play system update 상태를 앱 logic에 직접 하드코딩하면 device/release 차이에 취약하다.

플랫폼 모듈화는 앱에게 "OS 내부가 더 자주 업데이트될 수 있다"는 조건을 만든다. 앱은 내부 module identity보다 공개된 compatibility surface만 신뢰해야 한다.

관련 노트: [SDK Extensions](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/sdk-extensions-express-api-availability-beyond-sdk-int.md), [permissions 정본](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-contracts.md).

공식 문서: [SDK Extensions](https://developer.android.com/guide/sdk-extensions), [SdkExtensions API](https://developer.android.com/reference/android/os/ext/SdkExtensions)
