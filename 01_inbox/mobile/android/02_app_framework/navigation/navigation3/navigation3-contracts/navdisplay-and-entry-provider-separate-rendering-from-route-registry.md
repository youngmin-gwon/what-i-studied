# NavDisplay와 entry provider의 경계

상위 문서: [Navigation 3 계약](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-contracts.md)
관련 정본: [NavKey와 back stack은 앱이 소유하는 navigation 상태다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navkey-and-back-stack-are-app-owned-navigation-state.md)


## 역할 분리

`NavDisplay`는 back stack을 관찰하고 현재 entry들을 실제 Compose 화면으로 표시한다.
`entryProvider`는 `NavKey`를 `NavEntry`와 content로 바꾸는 registry다.
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

`NavDisplay`가 맡는 일은 렌더링 파이프라인의 조립이다.

- back stack에서 현재 entry를 선택한다.
- entry decorator를 적용한다.
- scene strategy로 표시 단위를 결정한다.
- 필요한 경우 transition과 back 처리를 연결한다.

`entryProvider`가 맡는 일은 타입별 화면 경계다.

- route key를 feature 화면에 필요한 인자로 변환한다.
- 화면에 navigation callback을 주입한다.
- scene 배치에 필요한 metadata를 route와 함께 선언한다.
- feature module이 자신의 route와 content를 소유하게 한다.

screen 함수가 전역 back stack을 직접 참조하면 화면과 앱 상태가 강하게 결합된다.
route-level composable이 `onOpenDetail`, `onClose` 같은 callback을 주입하는 편이 테스트하기 쉽다.
entry provider를 feature별 함수로 만들고 app layer에서 합치면 모듈 경계도 선명해진다.

```kotlin
fun trainingEntries(backStack: NavBackStack<NavKey>) = entryProvider {
    entry<TrainingRoute> {
        TrainingListScreen(onSelect = { backStack.add(TrainingDetailRoute(it)) })
    }
}
```

entry decorator는 모든 destination에 필요한 공통 수명주기만 담당한다.
`rememberSaveableStateHolderNavEntryDecorator`는 entry별 saveable 상태를 보존한다.
`rememberViewModelStoreNavEntryDecorator`는 entry별 ViewModel 저장소를 제공한다.
공통 logging이나 의존성 scope가 아니라면 custom decorator를 늘리지 않는다.
