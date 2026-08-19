---
title: B4-navigation-and-deeplink
tags: [android, navigation, deeplink, navigation3, topic-synthesis]
aliases: [Navigation Topic, 내비게이션과 딥링크 합성]
date modified: 2026-08-04 19:45:00 +09:00
date created: 2026-08-04 16:00:00 +09:00
---

## B4 · 내비게이션과 딥링크

> **이 문서의 목적**: 앱 내 화면 이동, Back Stack 관리, 그리고 외부로부터 앱을 여는 딥링크의 동작 원리를 이해한다. 이 vault 는 legacy Fragment 기반 Navigation Component(XML `NavGraph`/`NavHost`/`NavController`, `popUpTo`, 문자열 route)를 원자 노트로 다루지 않는다 — 실제로 깊게 다루는 것은 Navigation 3 다. 아래 표는 legacy 개념이 아니라 vault 가 실제로 가진 Navigation 3 원자 노트로 구성했다.

---

### 1. NavKey 와 Back Stack: 앱이 소유하는 navigation 상태

Navigation 3 의 핵심은 back stack 자체가 프레임워크가 아니라 앱이 소유하는 평범한 상태(리스트)라는 점이다. `NavKey` 는 화면을 가리키는 안정적인 식별자이고, task 의 activity back stack 과 앱 내부 navigation back stack 은 서로 다른 두 개의 스택이다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [NavKey와 back stack은 앱이 소유하는 navigation 상태다](../../02_app_framework/navigation/navigation3/navigation3/navkey-and-back-stack-are-app-owned-navigation-state.md) | back stack 이 Compose 상태(리스트)로 직접 관리된다 |
| [Android Task와 앱 back stack은 다른 상태다](../../02_app_framework/navigation/navigation3/navigation3/android-task-and-app-back-stack-are-different-stacks.md) | OS task stack 과 앱 내부 NavKey 스택을 혼동하면 안 되는 이유 |

---

### 2. Back Stack 복원과 route key 안정성

프로세스 사망 뒤에도 화면 위치를 복원하려면 back stack 이 저장 가능해야 하고, 저장된 key 가 앱 재시작 후에도 같은 화면을 가리켜야 한다. `route key` 는 UI 클래스가 아니라 직렬화 가능한 안정적 식별자여야 한다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [Navigation 3 back stack은 저장 가능한 navigation state로 복원해야 한다](../../02_app_framework/navigation/navigation3/navigation3/navigation3-back-stack-needs-saveable-restoration.md) | 프로세스 사망 복원을 견디는 back stack 저장 |
| [Navigation 3 route key는 UI 클래스가 아니라 안정적인 직렬화 식별자다](../../02_app_framework/navigation/navigation3/navigation3/route-key-should-be-stable-and-serializable.md) | 복원 가능하고 딥링크 변환이 가능한 key 설계 |

---

### 3. 렌더링과 구성의 분리: NavDisplay, EntryProvider, SceneStrategy

Navigation 3 는 "어떤 화면을 보여줄지 결정하는 것"과 "그 화면을 실제로 어떻게 그릴지"를 분리한다. `NavDisplay`/`EntryProvider` 는 route registry 와 렌더링을 나누고, `SceneStrategy`/`SceneDecorator` 는 여러 entry 를 하나의 scene 으로 조합하는 정책과 그 렌더링을 감싸는 정책을 나눈다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [NavDisplay와 entry provider의 경계](../../02_app_framework/navigation/navigation3/navigation3/navdisplay-and-entry-provider-separate-rendering-from-route-registry.md) | route 등록과 실제 렌더링 책임을 분리 |
| [SceneStrategy는 entry를 조합하고 SceneDecorator는 렌더링을 감싼다](../../02_app_framework/navigation/navigation3/navigation3/scene-strategy-composes-entries-while-decorator-wraps-rendering.md) | 화면 구성 정책과 렌더링 정책의 철저한 분리(대화면 적응형 레이아웃과 직결) |

---

### 4. 딥링크: 외부 URI → 앱 화면

딥링크는 외부 앱, 웹 브라우저, 푸시 알림 등에서 특정 URI 를 통해 앱의 특정 화면으로 직접 진입하게 하는 기술이다. Navigation 3 에서는 URI 를 곧바로 `NavKey` 로 변환하는 지점이 명시적 계약이다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [Android 딥 링크는 외부 URI 계약이다](../../02_app_framework/navigation/intents-and-deep-links/deep-link/deep-link-is-external-uri.md) | 딥링크를 "화면 이동"이 아니라 "신뢰 경계를 넘는 외부 입력"으로 다뤄야 하는 이유 |
| [Navigation 3 deep link는 URI를 NavKey로 변환한다](../../02_app_framework/navigation/navigation3/navigation3/navigation3-deep-link-converts-uri-to-navkey.md) | URI 파싱 결과를 back stack 에 넣기 전 거치는 변환 지점 |

---

### 5. Intent Filter와 App Links

딥링크가 동작하려면 `AndroidManifest.xml` 에 올바른 Intent Filter 가 선언되어야 하며, App Links 를 사용할 경우 `assetlinks.json` 검증을 거쳐야 시스템 딥링크 선택 대화상자가 생략된다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [action, category, data 매칭은 서로 다른 조건이다](../../02_app_framework/navigation/intents-and-deep-links/intent-manifest/intent-filter-matches-action-category-data.md) | Intent Filter 가 세 조건을 각각 별도로 매칭한다는 계약 |
| [Android App Link는 검증된 HTTPS 딥 링크다](../../02_app_framework/navigation/intents-and-deep-links/deep-link/app-link-is-verified-https-deep-link.md) | `autoVerify` 와 Digital Asset Links 검증이 대화상자를 생략시키는 조건 |
| [매니페스트와 assetlinks는 서로 다른 역할이다](../../02_app_framework/navigation/intents-and-deep-links/deep-link/manifest-and-assetlinks-have-distinct-roles.md) | 매니페스트 선언(수신 의사)과 assetlinks.json(도메인 소유권 증명)의 책임 분리 |

---

### 6. 앱 밖 웹 콘텐츠는 다른 계약: Custom Tabs / WebView

딥링크가 화면 "안으로" 들어오는 경로라면, 앱이 화면 "밖으로" 웹 콘텐츠를 열어야 할 때는 navigation 이 아니라 신뢰 경계 문제가 된다. Custom Tabs 와 WebView 는 서로 다른 프로세스·신뢰 모델을 가진다(Phase 9 에서 신설된 클러스터).

| 원자 노트 | 핵심 명제 |
|---|---|
| [Custom Tabs는 브라우저의 신뢰 경계를 공유하고 앱 WebView 프로세스와는 다르다](../../02_app_framework/navigation/custom-tabs/custom-tabs/custom-tabs-share-browser-trust-boundary-instead-of-app-webview-process.md) | 외부 링크를 열 때 Custom Tabs 와 인앱 WebView 중 무엇을 선택할지의 기준 |

---

### 이 주제와 연결된 Worked Example

| Worked Example | 연결 포인트 |
|---|---|
| [Deep Link가 올바른 Task와 화면 상태로 열리기까지](../worked-examples/03-deep-link-to-correct-task-and-screen-state.md) | 알림/외부 URI 진입 시 올바른 Task·Back Stack 합성, 성공/인증필요 두 경로 |

---

### 이 주제와 연결된 Diagnostic Runbook

| Runbook | 연결 포인트 |
|---|---|
| [앱 실행이 느리거나 첫 프레임이 뜨지 않는다](../diagnostic-runbooks/01-app-launch-slow-or-fails.md) | 딥링크가 콜드 스타트를 트리거하는 경로에서 동일한 launch 지연 진단 절차가 적용된다 |

---

### 더 깊이 들어갈 때 (Learning Spine)

- [4장 매니페스트에서 컴포넌트 실행까지](../learning-spine/04-manifest-to-component-execution.md) — Intent 해석(action/category/data 매칭)과 exported·permission 게이트를 다룬다. Intent Filter/App Links 절과 직결된다.
- [5장 화면, 프로세스, task와 사용자 상태는 독립적인 lifetime을 가진다](../learning-spine/05-independent-lifetimes-of-screen-process-task-and-state.md) — task/back stack lifetime 모델을 다룬다. Navigation 3 back stack 복원 절과 직결된다.
