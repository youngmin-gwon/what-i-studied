# Top-level Destination별 Back Stack

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
