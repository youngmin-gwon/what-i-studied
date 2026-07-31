# Mainline module update는 임의의 새 public API 배포와 같지 않다

Mainline module update가 곧 앱이 바로 호출할 수 있는 새 public SDK API를 뜻하지는 않는다. Mainline module은 SDK API, System API, stable C API, stable AIDL 같은 compatibility가 보장되는 경계 안에서 나머지 platform과 통신해야 한다.

앱 개발자에게 중요한 질문은 "이 module이 업데이트됐는가"보다 "내가 호출하려는 API가 이 device에서 사용 가능한가"다. 이 판단에는 `Build.VERSION.SDK_INT`, SDK Extension version, Jetpack helper, feature check가 필요할 수 있다.

SDK Extensions는 이 gap을 메우기 위한 별도 availability model이다. Mainline이 delivery mechanism이라면 SDK Extensions는 일부 API의 compile/runtime availability를 표현하는 app-facing 계약이다.

관련 노트: [SDK Extensions](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/sdk-extensions-express-api-availability-beyond-sdk-int.md), [앱의 availability check](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/apps-should-check-api-feature-availability-not-mainline-package-names.md).

공식 문서: [Mainline](https://source.android.com/docs/core/ota/modular-system), [SDK Extensions](https://developer.android.com/guide/sdk-extensions)
