---
title: navdisplay-and-entry-provider-separate-rendering-from-route-registry
tags: [android, android/navigation, android/navigation3]
aliases: ["NavDisplay 와 entry provider 의 경계"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## **NavDisplay**(백스택의 현재 상태에 맞춰 최상단 씬 화면을 실제로 렌더링하고 UI 전환 효과를 처리하는 컴포저블 컨테이너) 와 entry provider 의 경계

상위 문서: [Navigation 3 계약](navigation3-contracts.md)

관련 노트: [NavKey와 back stack은 앱이 소유하는 navigation 상태다](navkey-and-back-stack-are-app-owned-navigation-state.md)

### 역할 분리

`NavDisplay` 는 back stack 을 관찰하고 현재 entry 들을 실제 Compose 화면으로 표시한다.

`**entryProvider**(NavKey를 전달받아 이에 대응하는 화면 렌더링 컴포저블 블록을 매핑해 주는 라우트 레지스트리 함수)` 는 `NavKey` 를 `NavEntry` 와 content 로 바꾸는 registry 다.

두 구성 요소를 분리하면 상태 모델과 화면 생성 규칙을 독립적으로 검증할 수 있다.

```kotlin
NavDisplay(
    backStack = backStack,
    onBack = { backStack.removeLastOrNull() },
    entryProvider = entryProvider {
        entry<DashboardRoute> { DashboardScreen() }
        entry<TrainingDetailRoute> { route ->
            TrainingDetailScreen(trainingId = route.id)
        }
    },
)
```

`NavDisplay` 가 맡는 일은 렌더링 파이프라인의 조립이다.

- back stack 에서 현재 entry 를 선택한다.
- entry decorator 를 적용한다.
- scene strategy 로 표시 단위를 결정한다.
- 필요한 경우 transition 과 back 처리를 연결한다.

`entryProvider` 가 맡는 일은 타입별 화면 경계다.

- route key 를 feature 화면에 필요한 인자로 변환한다.
- 화면에 navigation callback 을 주입한다.
- scene 배치에 필요한 metadata 를 route 와 함께 선언한다.
- feature module 이 자신의 route 와 content 를 소유하게 한다.

screen 함수가 전역 back stack 을 직접 참조하면 화면과 앱 상태가 강하게 결합된다.

route-level composable 이 `onOpenDetail`, `onClose` 같은 callback 을 주입하는 편이 테스트하기 쉽다.

entry provider 를 feature 별 함수로 만들고 app layer 에서 합치면 모듈 경계도 선명해진다.

```kotlin
fun trainingEntries(backStack: NavBackStack<NavKey>) = entryProvider {
    entry<TrainingRoute> {
        TrainingListScreen(onSelect = { backStack.add(TrainingDetailRoute(it)) })
    }
}
```

entry decorator 는 모든 destination 에 필요한 공통 수명주기만 담당한다.

`rememberSaveableStateHolderNavEntryDecorator` 는 entry 별 saveable 상태를 보존한다.

`rememberViewModelStoreNavEntryDecorator` 는 entry 별 ViewModel 저장소를 제공한다.

공통 logging 이나 의존성 scope 가 아니라면 custom decorator 를 늘리지 않는다.
