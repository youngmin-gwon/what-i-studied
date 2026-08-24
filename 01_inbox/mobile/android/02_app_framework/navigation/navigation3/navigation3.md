---
title: navigation3
tags: [android, android/navigation, android/navigation3]
aliases: ["Navigation 3 계약", "Navigation 3 Contracts"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Navigation 3 계약 (Navigation 3 Contracts)

Jetpack Navigation 3 환경에서 타입 안전 내비게이션, 앱 소유 백스택, 렌더링 엔진 분리를 실현하기 위한 핵심 아키텍처 계약 모음이다.

---

### 핵심 계약 가이드라인

1. **상태 소유권 및 타입 안정성 계약**:
   - 목적지는 식별자와 파라미터를 캡슐화한 `@Serializable NavKey`로 정의하며, 백스택(`NavBackStack`)은 앱 프레임워크가 소유하는 단방향 상태로 관리한다.
2. **렌더링과 레지스트리 분리 계약**:
   - `EntryProvider`는 라우트 키와 컴포저블 렌더링 로직을 매핑하고, `NavDisplay`는 백스택과 `SceneStrategy`를 받아 실제 UI를 렌더링한다.
3. **상태 보존 및 복원 계약**:
   - 모든 `NavKey`는 프로세스 사망 후 복원될 수 있도록 저장 가능(`rememberSaveable` / `@Serializable`)해야 하며, 각 화면의 로컬 뷰 상태는 `SaveableStateHolder`로 보호된다.

---

### 하위 세부 계약 목록

- [NavKey와 back stack은 앱이 소유하는 navigation 상태다](navkey-back-stack-ownership.md)
- [Route key는 안정적인 직렬화 식별자다](route-key-serialization.md)
- [NavDisplay와 entry provider는 렌더링과 route registry를 분리한다](navdisplay-entry-provider.md)
- [Metadata와 SceneStrategy는 표시 정책을 전달한다](metadata-scene-strategy.md)
- [SceneStrategy는 entry를 조합하고 decorator는 렌더링을 감싼다](scene-strategy-decorators.md)
- [Navigation 3 back stack은 저장 가능한 navigation state로 복원해야 한다](navigation3-back-stack-restoration.md)
- [Navigation 3 deep link는 URI를 NavKey로 변환한다](navigation3-deep-link-routing.md)
- [Navigation 3 transition과 back policy는 같은 stack 상태를 공유해야 한다](navigation3-transitions-back-policy.md)
- [Android task와 app back stack은 서로 다른 스택이다](task-vs-app-back-stack.md)
- [Navigation 3 metadata 예시는 Kotlin 문법을 쓰지만 문법 자체가 navigation 계약은 아니다](navigation3-metadata-syntax.md)
- [Navigation 3 Scene & SceneStrategy](navigation3-scene-and-strategy.md) - window size에 따른 single/multi-pane 실전 적용
- [NavigationSuiteScaffold](../adaptive/navigation-suite-scaffold.md) - Material3 Top-Level Navigation Chrome adaptive 전환
- [NavigationSuiteScaffold vs Navigation 3 Scene](../adaptive/navigation-suite-scaffold-vs-navigation3-scene.md) - Outer Chrome과 Inner Content Layout의 역할 비교 및 결합 아키텍처

---

### 상위 및 연관 지도

- 상위 가이드: [Jetpack Navigation 3 가이드](jetpack-navigation-3-guide.md)
- 연관 가이드: [Android Navigation 진입 계약](../../navigation/navigation.md)
