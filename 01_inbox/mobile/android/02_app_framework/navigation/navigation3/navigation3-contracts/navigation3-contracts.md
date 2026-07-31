# Navigation 3 계약

Navigation 3의 핵심은 앱이 `NavKey` back stack 상태를 소유하고, `NavDisplay`가 그 상태를 화면으로 렌더링한다는 점이다. OS Intent 해석과 앱 내부 back stack 관리를 섞지 않는다.

## 정본 노트

- [NavKey와 back stack은 앱이 소유하는 navigation 상태다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navkey-and-back-stack-are-app-owned-navigation-state.md)
- [NavDisplay와 entry provider는 렌더링과 route registry를 분리한다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navdisplay-and-entry-provider-separate-rendering-from-route-registry.md)
- [Metadata와 SceneStrategy는 표시 정책을 전달한다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/metadata-and-scene-strategy-carry-display-policy.md)
- [Navigation 3 deep link는 URI를 NavKey로 변환한다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-deep-link-converts-uri-to-navkey.md)
- [Android task와 앱 back stack은 다른 스택이다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/android-task-and-app-back-stack-are-different-stacks.md)

관련 지도: [Android Navigation 진입 계약](01_inbox/mobile/android/02_app_framework/navigation/navigation-contracts/navigation-contracts.md), [Adaptive Navigation 계약](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/adaptive-navigation-contracts.md)
