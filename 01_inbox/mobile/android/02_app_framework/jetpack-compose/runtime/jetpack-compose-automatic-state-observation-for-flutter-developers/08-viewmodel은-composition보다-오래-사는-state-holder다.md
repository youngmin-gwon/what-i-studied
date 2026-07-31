# ViewModel은 Composition보다 오래 사는 state holder다

상위 노트: [jetpack-compose-automatic-state-observation-for-flutter-developers](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/jetpack-compose-automatic-state-observation-for-flutter-developers.md)

Flutter 개발자가 ViewModel을 `StatefulWidget.State`처럼 이해하면 수명이 꼬입니다.

ViewModel은 Composition 밖에 있고, configuration change 후에도 유지됩니다. Flutter로 비유하면 화면 단위 Riverpod Notifier나
Bloc에
더 가깝습니다.

```kotlin
@Composable
fun ProfileRoute(
    viewModel: ProfileViewModel,
) {
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    ProfileScreen(
        uiState = uiState,
        onRefresh = viewModel::refresh,
    )
}
```

이 구조에서 책임은 나뉩니다.

| 계층              | 책임                                        |
|:----------------|:------------------------------------------|
| `ProfileScreen` | 상태를 읽어 UI를 그림, 이벤트 callback 호출            |
| `ProfileRoute`  | ViewModel 상태를 Compose State로 수집하고 연결      |
| ViewModel       | 화면 정책, API 호출, repository 연동, UI state 생산 |
| Repository      | 데이터 source, 캐시, 저장소, 네트워크 경계              |

Composable은 ViewModel의 상태를 소비하지만, ViewModel은 `remember`로 만들거나 Composition 수명에 묶는 대상이 아닙니다.

---
