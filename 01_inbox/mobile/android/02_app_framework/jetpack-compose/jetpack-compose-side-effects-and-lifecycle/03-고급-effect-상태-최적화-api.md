# 고급 Effect & 상태 최적화 API

상위 노트: [[jetpack-compose-side-effects-and-lifecycle]]

### 3-1. `rememberUpdatedState` (값 업데이트 유지)
* **목적**: Effect가 재생성(Re-launch)되는 비용을 피하면서, 비동기 작업 중에도 항상 최신의 변수 값을 참조하도록 보장합니다.
* **동작**: `rememberUpdatedState`로 값을 감싸면, Effect의 `key`를 변경하지 않아도 코루틴 내부에서 항상 최신 상태를 읽어올 수 있습니다.
* **주요 사용처**: 시간 경과 후 실행되는 콜백(예: Timer, Timeout) 등에서, 최신 이벤트 핸들러를 실행하되 이펙트를 처음부터 재시작하고 싶지 않을 때.

```kotlin
@Composable
fun TimeoutHandler(onTimeout: () -> Unit) {
    // onTimeout 람다가 변경되더라도 LaunchedEffect가 재시작되지 않도록 감싸줍니다.
    val currentOnTimeout by rememberUpdatedState(onTimeout)

    LaunchedEffect(Unit) {
        delay(5000L) // 5초 대기
        currentOnTimeout() // 이펙트 재시작 없이 항상 가장 최신의 onTimeout 실행
    }
}
```

---

### 3-2. `derivedStateOf` (파생 상태 최적화)
* **목적**: 자주 변경되는 상태(State)들로부터 특정 조건의 파생 상태를 만들 때, 불필요한 재구성(Recomposition) 횟수를 제한합니다.
* **동작**: 내부 상태가 아무리 많이 변하더라도 계산된 결과 값 자체가 변경될 때만 수신처에 재구성을 유발합니다.
* **주요 사용처**: 스크롤 위치 계산, 리스트 필터링, 조건부 UI 노출 판정.

```kotlin
@Composable
fun ScrollTargetList(lazyListState: LazyListState) {
    // 스크롤 인덱스는 스크롤할 때마다 계속 변경되지만, 
    // derivedStateOf를 쓰면 '5개 이상 스크롤되었는지 여부'가 바뀔 때만 Recomposition이 실행됩니다.
    val showButton by remember {
        derivedStateOf {
            lazyListState.firstVisibleItemIndex > 5
        }
    }

    if (showButton) {
        FloatingActionButton(onClick = { /* ... */ })
    }
}
```

---

### 3-3. `produceState` (비-Compose 소스를 State로 변환)
* **목적**: RxJava, Flow, Callbacks, 외부 Promise 등 Compose가 아닌 비동기 데이터 소스를 Compose가 읽을 수 있는 `State<T>` 형태로 변환합니다.
* **동작**: `LaunchedEffect`와 상태 저장이 합쳐진 형태의 간편 API입니다.

```kotlin
@Composable
fun loadNetworkImage(url: String, imageRepository: ImageRepository): State<ImageState> {
    // url이 바뀔 때마다 실행되며 결과를 Compose State로 노출
    return produceState<ImageState>(initialValue = ImageState.Loading, url) {
        value = try {
            val image = imageRepository.downloadImage(url)
            ImageState.Success(image)
        } catch (e: Exception) {
            ImageState.Error(e)
        }
    }
}
```

---

### 3-4. `snapshotFlow` (Compose State를 Flow로 변환)
* **목적**: Compose State의 변화를 감지하여 Reactive Stream(Flow)으로 변환한 뒤, Flow 연산자(filter, debounce 등)를 적용할 수 있게 해줍니다.

```kotlin
@Composable
fun SearchAnalytics(lazyListState: LazyListState) {
    LaunchedEffect(lazyListState) {
        snapshotFlow { lazyListState.firstVisibleItemIndex }
            .distinctUntilChanged()
            .filter { it > 0 }
            .collect { index ->
                analytics.trackUserReachedIndex(index)
            }
    }
}
```

---
