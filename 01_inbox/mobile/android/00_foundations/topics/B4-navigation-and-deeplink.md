---
title: B4-navigation-and-deeplink
tags: [android, navigation, deeplink, navigation3, topic-synthesis]
aliases: [Navigation Topic, 내비게이션과 딥링크 합성]
date modified: 2026-08-04 16:30:00 +09:00
date created: 2026-08-04 16:00:00 +09:00
---

## B4 · 내비게이션과 딥링크

> **이 문서의 목적**: 앱 내 화면 이동, 데이터 전달, 그리고 외부로부터 앱을 여는 딥링크의 동작 원리를 이해한다. Jetpack Navigation Component 와 Compose Navigation 의 결합, 그리고 최신 Navigation 3 패러다임을 다룬다.

---

### 1. Navigation Component 핵심 개념 (NavHost, NavController, NavGraph)

Navigation Component 는 화면 간의 전환을 선언적이고 안전하게 관리한다. 뼈대가 되는 `NavGraph` 는 모든 가능한 이동 경로를 정의하고, `NavHost` 는 화면이 표시되는 빈 컨테이너이며, `NavController` 는 실제 화면 이동을 지휘하는 조종사 역할을 한다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [NavGraph는 앱의 모든 탐색 경로를 정의하는 지도다](../../02_app_framework/navigation/core/navgraph-defines-all-navigation-paths.md) | XML 또는 Kotlin DSL 을 활용한 라우팅 트리 |
| [NavController는 화면 이동과 Back Stack 조작을 수행한다](../../02_app_framework/navigation/core/navcontroller-executes-navigation-and-back-stack-mutations.md) | navigate() 와 popBackStack() 의 역할 |

---

### 2. Back Stack과 화면 전환

NavController 가 이동을 수행할 때마다 화면은 Back Stack 에 쌓인다. 단순히 스택에 푸시하는 것 외에도 `popUpTo` 와 `launchSingleTop` 속성을 사용해 스택 중복을 방지하거나 특정 지점까지 화면을 비우는 등 정교한 백 스택 조작이 가능하다. 

| 원자 노트 | 핵심 명제 |
|---|---|
| [popUpTo는 특정 목적지까지 Back Stack을 비운다](../../02_app_framework/navigation/core/popupto-clears-back-stack-to-specific-destination.md) | 순환 참조 방지 및 완료된 흐름(예: 로그인) 제거 |
| [launchSingleTop은 동일한 화면의 다중 인스턴스를 막는다](../../02_app_framework/navigation/core/launchsingletop-prevents-multiple-instances-of-same-screen.md) | 같은 탭 반복 클릭 시 스택 쌓임 방지 |

---

### 3. Compose Navigation 통합

Jetpack Compose 에서는 화면을 Composable 함수로 구성하며, `NavHost` 도 Composable 로 대체된다. 화면 이동 시 인자(Arguments)를 전달할 때 URL 문자열과 유사한 형태를 사용하며, 최근에는 Type-safe 한 객체 기반 라우팅이 도입되어 컴파일 시점에 오류를 방지한다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [Compose Navigation은 Composable 간의 이동을 URL 방식으로 처리한다](../../02_app_framework/navigation/compose/compose-navigation-handles-transitions-via-url-routing.md) | route 문자열과 arguments 추출 방식 |
| [Type-safe Navigation은 직렬화된 객체로 경로와 인자를 검증한다](../../02_app_framework/navigation/compose/type-safe-navigation-validates-routes-with-serialized-objects.md) | kotlinx.serialization 기반 안전한 인자 전달 |

---

### 4. 딥링크: 외부 URI → 앱 화면

딥링크는 외부 앱, 웹 브라우저, 푸시 알림 등에서 특정 URI 를 통해 앱의 특정 화면으로 직접 진입하게 하는 기술이다. Navigation Component 는 URI 매칭을 통해 올바른 목적지로 라우팅함과 동시에, 진입 시 가상의 Back Stack 을 생성해 사용자가 '뒤로 가기'를 누를 때 앱의 홈 화면으로 자연스럽게 돌아가게 만든다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [Deep Link는 URI를 통해 앱 내부 특정 화면으로 직접 라우팅한다](../../02_app_framework/navigation/deeplink/deep-link-routes-directly-to-internal-screen.md) | 명시적/암시적 딥링크와 Navigation Graph 통합 |
| [Navigation은 딥링크 진입 시 가상의 Back Stack을 합성한다](../../02_app_framework/navigation/deeplink/navigation-synthesizes-virtual-back-stack-for-deep-links.md) | TaskStackBuilder 를 이용한 자연스러운 뒤로 가기 경험 |

---

### 5. Intent Filter와 Task 관리

딥링크가 동작하려면 `AndroidManifest.xml` 에 올바른 Intent Filter 가 선언되어야 하며, 앱 링크 (App Links)를 사용할 경우 `assetlinks.json` 검증을 거친다. 외부 진입 시 기존 Task 를 재사용할지 새 Task 를 만들지 결정하는 것은 `launchMode` 와 연계되어 작동한다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [Intent Filter는 시스템이 딥링크를 앱으로 전달하는 관문이다](../../02_app_framework/navigation/deeplink/intent-filter-is-the-gateway-for-deep-links.md) | scheme, host, pathPrefix 구성 원칙 |
| [Android App Links는 도메인 소유권을 검증하여 딥링크 대화상자를 제거한다](../../02_app_framework/navigation/deeplink/android-app-links-verify-domain-ownership-to-skip-dialog.md) | autoVerify 와 Digital Asset Links 동작 |

---

### 6. Navigation 3 (새 API)

Navigation 3 패러다임은 백 스택 자체를 앱 내부의 일반 Compose 상태(List)로 간주한다. NavKey 와 백 스택은 뷰에 종속되지 않는 안정적인 직렬화 식별자로 설계되며, SceneStrategy 와 Decorator 를 통해 화면 구성 및 렌더링을 완전히 분리한다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [NavKey와 back stack은 앱이 소유하는 navigation 상태다](../../02_app_framework/navigation/navigation3/navigation3-contracts/navkey-and-back-stack-are-app-owned-navigation-state.md) | 백 스택을 Compose State 로 직접 관리 |
| [Navigation 3 route key는 UI 클래스가 아니라 안정적인 직렬화 식별자다](../../02_app_framework/navigation/navigation3/navigation3-contracts/route-key-should-be-stable-and-serializable.md) | 복원 가능하고 딥링크 변환이 가능한 key 설계 |
| [SceneStrategy는 entry를 조합하고 SceneDecorator는 렌더링을 감싼다](../../02_app_framework/navigation/navigation3/navigation3-contracts/scene-strategy-composes-entries-while-decorator-wraps-rendering.md) | 렌더링 정책과 화면 구성 정책의 철저한 분리 |
| [Navigation 3 back stack은 저장 가능한 navigation state로 복원해야 단다](../../02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-back-stack-needs-saveable-restoration.md) | 프로세스 사망 복원을 견디는 백 스택 저장 |

---

### 이 주제와 연결된 Worked Example

| Worked Example | 연결 포인트 |
|---|---|
| [WE 03 · Deep Link Navigation Resolving](../worked-examples/03-deep-link-navigation-resolving.md) | 알림을 통한 딥링크 진입 및 올바른 Task/Back Stack 합성 |
| [WE 04 · Multi-module Navigation Setup](../worked-examples/04-multi-module-navigation-setup.md) | 피처 모듈 간의 의존성 없는 네비게이션 설계 |

---

### 이 주제와 연결된 Diagnostic Runbook

| Runbook | 연결 포인트 |
|---|---|
| [RB 01 · App Launch Performance](../diagnostic-runbooks/01-app-launch-performance.md) | 딥링크 처리 과정에서 발생하는 콜드 스타트 지연 해결 |
| [RB 08 · Deep Link Routing Failure](../diagnostic-runbooks/08-deep-link-routing-failure.md) | URI 파싱 실패 및 Intent Filter 매칭 문제 추적 |

---

### 더 깊이 들어갈 때 (Learning Spine)

- **Chapter 05 · Architecture** — 멀티 모듈 아키텍처에서의 네비게이션 설계
- **Chapter 01 · App Component** — Task 및 프로세스 관리에 대한 더 깊은 이해
- **Chapter 04 · UI Layer** — Compose 와 Adaptive Scaffold 기반 레이아웃에서의 Navigation
