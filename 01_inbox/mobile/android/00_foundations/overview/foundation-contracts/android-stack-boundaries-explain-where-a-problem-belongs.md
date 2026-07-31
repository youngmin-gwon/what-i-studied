# Android stack boundary는 문제가 어느 층에 속하는지 판단하게 해 준다

Android 문제를 진단할 때 첫 질문은 "어떤 API를 썼나"가 아니라 "어느 boundary가 실패했나"다. UI frame deadline이면 rendering/runtime 문제이고, app launch면 Activity/system_server/zygote 문제이며, 외부 호출이면 Intent/Manifest/security boundary 문제다.

Kernel과 HAL은 device capability를 제공하고, native/service layer는 system policy를 구현하며, framework는 app-facing API와 lifecycle을 노출한다. 앱 코드는 이 boundary 위에서 상태, navigation, data, background work를 설계한다.

이 구분을 지키면 같은 내용을 overview, architecture, security, debugging 문서가 반복하지 않는다.

관련 정본: [boot/runtime](01_inbox/mobile/android/01_system_internals/boot-and-runtime/android-boot-and-runtime.md), [graphics/media](01_inbox/mobile/android/01_system_internals/graphics-and-media/android-graphics-media-runtime.md), [app components](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components.md), [debugging](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/debugging-contracts.md).
