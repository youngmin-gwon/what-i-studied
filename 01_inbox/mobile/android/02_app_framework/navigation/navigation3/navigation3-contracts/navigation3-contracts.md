---
title: navigation3-contracts
tags: [android, android/navigation, android/navigation3]
aliases: ["Navigation 3 계약"]
date modified: 2026-08-04 14:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Navigation 3 계약

Navigation 3 의 핵심은 앱이 `NavKey` back stack 상태를 소유하고, `NavDisplay` 가 그 상태를 화면으로 렌더링한다는 점이다. OS Intent 해석과 앱 내부 back stack 관리를 섞지 않는다.

### 정본 노트

- [NavKey와 back stack은 앱이 소유하는 navigation 상태다](./navkey-and-back-stack-are-app-owned-navigation-state.md)
- [Navigation 3 route key는 UI 클래스가 아니라 안정적인 직렬화 식별자다](./route-key-should-be-stable-and-serializable.md)
- [Navigation 3 back stack은 저장 가능한 navigation state로 복원해야 한다](./navigation3-back-stack-needs-saveable-restoration.md)
- [NavDisplay와 entry provider는 렌더링과 route registry를 분리한다](./navdisplay-and-entry-provider-separate-rendering-from-route-registry.md)
- [Metadata와 SceneStrategy는 표시 정책을 전달한다](./metadata-and-scene-strategy-carry-display-policy.md)
- [Navigation 3 metadata 예제의 Kotlin 문법은 navigation 계약이 아니다](./navigation3-metadata-examples-use-kotlin-syntax-but-syntax-is-not-navigation-contract.md)
- [SceneStrategy는 entry를 조합하고 SceneDecorator는 렌더링을 감싼다](./scene-strategy-composes-entries-while-decorator-wraps-rendering.md)
- [Navigation 3 transition과 predictive back은 같은 stack state를 기준으로 해야 한다](./navigation3-transition-and-back-policy-must-share-stack-state.md)
- [Navigation 3 deep link는 URI를 NavKey로 변환한다](./navigation3-deep-link-converts-uri-to-navkey.md)
- [Android task와 앱 back stack은 다른 스택이다](./android-task-and-app-back-stack-are-different-stacks.md)

관련 지도: [Android Navigation 진입 계약](../../navigation-contracts/navigation-contracts.md), [Adaptive Navigation 계약](../../adaptive-navigation/adaptive-navigation-contracts/adaptive-navigation-contracts.md)
