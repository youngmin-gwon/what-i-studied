# SDK Extensions는 SDK_INT만으로 표현되지 않는 API availability를 나타낸다

SDK Extensions는 modular system component update를 통해 일부 API가 이전 Android API level 기기에도 제공될 수 있음을 표현한다. Android 11(API 30) 이상 기기는 extension version set을 가질 수 있고, API reference에는 어떤 extension version부터 API를 쓸 수 있는지가 표시된다.

`Build.VERSION.SDK_INT >= 33` 같은 check는 여전히 유효하지만, extension API는 더 낮은 platform API level에서도 특정 extension version 이상이면 사용 가능할 수 있다. 그래서 SDK_INT만 보면 false negative가 생길 수 있다.

앱은 `SdkExtensions.getExtensionVersion(...)` 또는 Jetpack helper를 사용해 runtime availability를 확인한다. 이 값은 public API 사용 가능성을 판단하는 계약이지, 개별 Mainline package version을 직접 추적하라는 뜻이 아니다.

관련 노트: [compile/runtime check](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/sdk-extension-compile-sdk-extension-and-runtime-check-are-separate-steps.md), [앱 availability check](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apps-should-check-api-feature-availability-not-mainline-package-names.md).

공식 문서: [SDK Extensions](https://developer.android.com/guide/sdk-extensions), [SdkExtensions API](https://developer.android.com/reference/android/os/ext/SdkExtensions)
