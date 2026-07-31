# Adaptive Layout & Navigation 프로젝트 적용 의견

> 이 문서는 [[adaptive-layout-and-navigation]]의 공식 문서 정리와 분리된 프로젝트 적용 판단입니다.

---

## 1. 이 프로젝트의 권장 큰 구조

이 앱은 로그인 전/후 흐름이 명확히 나뉩니다.

```text
MainActivity
 -> MyBenefitApp
     -> SplashScreen API가 session loading 동안 유지
     -> signed out: AuthFlow
     -> signed in: MainScaffold
```

`AuthFlow`는 로그인 전 route만 가집니다.

```text
AuthFlow
 └─ NavDisplay
     ├─ SignInRoute
     ├─ SignUpRoute
     ├─ IdRecoveryRoute
     └─ PasswordRecoveryRoute
```

`MainScaffold`는 로그인 후 앱의 persistent frame입니다.

```text
MainScaffold
 ├─ NavigationSuiteScaffold
 │   ├─ compact: navigation bar
 │   └─ expanded: navigation rail / drawer
 └─ selected top-level destination NavDisplay
```

---

## 2. Route Marker

현재는 다음 두 marker만 유지하는 것을 추천합니다.

```kotlin
interface AuthRoute : NavKey
interface MainFeatureTopLevelRoute : NavKey
```

`MainFeatureTopLevelRoute`는 로그인 필요 여부가 아니라 adaptive navigation item 여부를 의미합니다.

```text
MainFeatureTopLevelRoute
= phone에서는 bottom bar item
= tablet/foldable에서는 rail/drawer item
= 각 main feature의 root route
```

`ProtectedRoute`는 당장 도입하지 않는 편이 좋습니다. 현재 규칙이 "AuthRoute가 아니면 로그인 필요"라면 helper로 충분합니다.

```kotlin
fun requiresSignedIn(route: NavKey): Boolean {
    return route !is AuthRoute
}
```

나중에 로그인 없이 볼 수 있는 non-auth route가 생기면 `ProtectedRoute` 또는 `PublicRoute`를 도입합니다.

---

## 3. Top-level Destination별 Back Stack

`replaceTopLevel()`로 단일 back stack을 갈아끼우는 방식은 탭별 state 보존에 약합니다.

이 앱은 `dashboard`, `measure`, `training`, `training record`, `settings`에 하위 페이지가 생길 가능성이 높으므로 top-level destination별 back stack을 유지하는 편이 낫습니다.

```text
Dashboard stack:
DashboardRoute

Measure stack:
MeasureRoute -> MeasureDetailRoute(id)

Training stack:
TrainingRoute -> TrainingDetailRoute(id)

Settings stack:
SettingsRoute -> AccountSettingsRoute
```

탭 전환은 route 교체가 아니라 selected destination 변경입니다.

```kotlin
var selectedDestination by rememberSaveable {
    mutableStateOf(MainDestination.Dashboard)
}
```

---

## 4. Deep Link 처리

Deep link는 app layer에서 route로 변환합니다.

```text
https://example.com/training/123
 -> TrainingDetailRoute("123")
```

session 상태에 따라 다르게 처리합니다.

```text
SignedIn:
 -> selectedDestination = Training
 -> trainingBackStack = [TrainingRoute, TrainingDetailRoute("123")]

SignedOut:
 -> pendingRoute = TrainingDetailRoute("123")
 -> AuthFlow(SignInRoute)
 -> 로그인 성공 후 MainScaffold로 이동
```

---

## 5. Scene 도입 기준

Navigation 3 `Scene`은 처음부터 모든 route에 넣을 필요는 없습니다.

도입하지 않는 경우:

- placeholder 화면
- 단순 single screen flow
- 아직 list/detail route가 없는 feature

도입 검토 대상:

- `TrainingRoute` + `TrainingDetailRoute`
- `MeasureRoute` + `MeasureResultRoute`
- `TrainingRecordRoute` + `TrainingRecordDetailRoute`

`NavigationSuiteScaffold`와 Navigation 3 `Scene`은 같이 사용할 수 있습니다.

```text
MainScaffold
 └─ NavigationSuiteScaffold
     └─ selected tab NavDisplay
         └─ sceneStrategies = listOf(...)
```

다만 feature 내부 list-detail 화면은 `NavigableListDetailPaneScaffold`와 custom `SceneStrategy` 중 하나를 선택하는 편이 좋습니다.

---

## 6. 추천 적용 순서

```text
1. MainActivity는 SplashScreen API + setContent만 담당
2. app/ui/MyBenefitApp.kt 생성
3. app/ui/AuthFlow.kt 생성
4. app/ui/MainScaffold.kt 생성
5. MainScaffold에서 NavigationSuiteScaffold 사용
6. MainFeatureTopLevelRoute별 back stack 유지
7. app에 deep link parser 추가
8. Training/Measure 같은 list-detail feature가 생기면 adaptive pane 또는 Scene 검토
```

---

## 7. 이름 선택

공식 문서가 `Shell`이나 `Flow`를 표준 명명으로 강제하지는 않습니다.

이 프로젝트에서는 다음 이름이 가장 자연스럽습니다.

```text
MyBenefitApp
- app root composable

AuthFlow
- 로그인 전 연속 흐름

MainScaffold
- 로그인 후 persistent adaptive frame

MainDestination
- adaptive navigation item 정의
```

