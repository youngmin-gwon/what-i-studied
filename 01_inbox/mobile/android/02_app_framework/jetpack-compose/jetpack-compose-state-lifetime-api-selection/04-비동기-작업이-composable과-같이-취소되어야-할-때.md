# 비동기 작업이 Composable과 같이 취소되어야 할 때

상위 노트: [[jetpack-compose-state-lifetime-api-selection]]

composition 진입 시 시작하고, key가 바뀌거나 composable이 사라지면 취소되어야 하는 coroutine은 `LaunchedEffect`를 씁니다.

```kotlin
@Composable
fun ProductRoute(
    productId: String,
    viewModel: ProductViewModel,
) {
    LaunchedEffect(productId) {
        viewModel.load(productId)
    }
}
```

적합한 작업:

- 특정 key가 바뀔 때 ViewModel에 load 요청
- 일회성 event 수집 후 snackbar/navigation 처리
- animation 시작
- UI-local async 작업

주의할 점:

- Composable body에서 직접 `repository.load()`를 호출하지 않습니다.
- `LaunchedEffect(Unit)`은 해당 composition 생명 동안 한 번만 실행됩니다. 내부에서 쓰는 값이 바뀌어야 하면 key에 넣거나
  `rememberUpdatedState`를 씁니다.
- 화면 비즈니스 작업은 가능하면 ViewModel의 `viewModelScope`에서 처리하고, `LaunchedEffect`는 UI와 lifecycle에 묶인 트리거로 둡니다.

---
