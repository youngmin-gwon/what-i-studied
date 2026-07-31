# API level, codename, extension level, targetSdkVersion은 서로 다른 version 축이다

Android version을 말할 때 API level, dessert codename, SDK Extension level, targetSdkVersion을 섞으면 판단이 흐려진다. API level은 platform SDK surface의 큰 번호이고, codename은 release 식별자이며, extension level은 module update를 통해 제공되는 일부 API availability를 표현한다.

targetSdkVersion은 앱이 어떤 behavior-change contract를 수락하는지 나타낸다. device가 Android 17이어도 앱 target이 낮으면 일부 동작은 compatibility mode를 거칠 수 있고, 반대로 extension API는 낮은 API level 기기에서도 extension version 조건을 만족하면 사용할 수 있다.

2026년 기준 API 36은 Android 16/Baklava, API 37은 Android 17/Cinnamon Bun으로 문서화되어 있다. Android 16부터 minor SDK version 축도 `VERSION_CODES_FULL`에 드러난다.

관련 노트: [SDK Extensions](01_inbox/mobile/android/01_system_internals/platform-modularity/platform-modularity-contracts/sdk-extensions-express-api-availability-beyond-sdk-int.md), [packaging/deployment](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md).

공식 문서: [Build.VERSION_CODES](https://developer.android.com/reference/android/os/Build.VERSION_CODES), [VERSION_CODES_FULL](https://developer.android.com/reference/kotlin/android/os/Build.VERSION_CODES_FULL)
