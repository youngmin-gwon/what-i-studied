# Android System Map

이 문서는 Android를 처음 볼 때의 system map이다. 세부 구현은 각 정본으로 이동한다.

## Foundation Notes

- [Android는 앱 SDK만이 아니라 계층형 모바일 플랫폼이다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/android-is-layered-mobile-platform-not-just-an-app-sdk.md)
- [Android stack boundary는 문제가 어느 층에 속하는지 판단하게 해 준다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/android-stack-boundaries-explain-where-a-problem-belongs.md)
- [앱 실행은 Launcher, system_server, Zygote, ActivityThread를 지나는 경로다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/app-launch-crosses-launcher-system-server-zygote-and-activitythread.md)
- [Android 보안은 UID sandbox, permission, SELinux, verified boot가 나뉜 계층이다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/android-security-is-layered-from-uid-sandbox-to-permissions-and-verified-boot.md)
- [Android 지식 지도는 runtime, app framework, services, security, tooling으로 나누어 읽는다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/android-knowledge-map-is-organized-by-runtime-app-framework-services-security-and-tooling.md)
- [사진 찍기 예시는 permission, intent, UI, media, HAL, storage 경계를 함께 지난다](01_inbox/mobile/android/00_foundations/overview/foundation-contracts/camera-example-crosses-permission-intent-ui-media-hal-and-storage-boundaries.md)

## Reading Routes

- Runtime/process: [boot/runtime](01_inbox/mobile/android/01_system_internals/boot-and-runtime/android-boot-and-runtime.md), [system_server](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md), [Zygote/runtime](01_inbox/mobile/android/01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-runtime-contracts.md)
- Kernel/HAL: [kernel](01_inbox/mobile/android/01_system_internals/kernel-and-hal/android-kernel-runtime.md), [HAL/native boundary](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-boundary.md)
- App framework: [app architecture](01_inbox/mobile/android/02_app_framework/architecture/android-app-architecture.md), [app components](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components.md), [Context](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context-boundaries.md)
- UI/data: [Compose runtime](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md), [Compose UI](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-layout-animation-accessibility.md), [storage](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md)
- Security/debugging: [security](01_inbox/mobile/android/05_security_privacy/security-practices/android-security-practices.md), [debugging](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/debugging-contracts.md), [performance](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/performance-contracts.md)
