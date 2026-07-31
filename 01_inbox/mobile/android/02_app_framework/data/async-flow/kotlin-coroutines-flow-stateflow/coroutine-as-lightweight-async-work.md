# Coroutine: 가벼운 비동기 작업 단위

상위 노트: [[kotlin-coroutines-flow-stateflow]]

### 2-1. Coroutine이란?

Coroutine은 Kotlin이 제공하는 **가벼운 비동기 실행 단위**입니다.

스레드와 비슷하게 "어떤 일을 따로 실행한다"는 느낌은 있지만, 스레드 자체는 아닙니다.

| 구분     | Thread             | Coroutine                  |
|:-------|:-------------------|:---------------------------|
| 정체     | OS가 관리하는 무거운 실행 단위 | Kotlin 런타임이 관리하는 가벼운 작업 단위 |
| 비용     | 생성/전환 비용이 큼        | 매우 많이 만들어도 상대적으로 가벼움       |
| 중단     | 스레드가 실제로 막힘        | 중단 지점에서 쉬었다가 나중에 재개        |
| 코드 스타일 | 콜백/동기화 코드가 많아지기 쉬움 | 순차 코드처럼 읽히는 비동기 코드         |

쉽게 말하면 Coroutine은 **기다릴 때 자리를 비켜주는 작업 단위**입니다.

```kotlin
viewModelScope.launch {
    val user = userRepository.fetchUser()
    val benefits = benefitRepository.fetchBenefits(user.id)
    _uiState.value = BenefitUiState.Success(benefits)
}
```

위 코드는 위에서 아래로 읽힙니다. 하지만 `fetchUser()`나 `fetchBenefits()`가 오래 걸릴 때 메인 스레드를 붙잡고 멈추는 것이 아니라, Coroutine이
잠시 중단되었다가 결과가 오면 다시 이어서 실행됩니다.

### 2-2. `suspend` 함수란?

`suspend`는 "이 함수는 중간에 멈췄다가 다시 이어질 수 있다"는 표시입니다.

```kotlin
suspend fun fetchBenefits(): List<Benefit> {
    return api.getBenefits()
}
```

`suspend` 함수는 일반 함수처럼 값을 반환하지만, 내부에서 네트워크, DB, 파일 작업처럼 오래 걸리는 일을 안전하게 기다릴 수 있습니다.

> [!IMPORTANT]
> `suspend`는 "무조건 백그라운드에서 실행된다"는 뜻이 아닙니다. 단지 **중단 가능하다**는 뜻입니다. 실제로 어느 스레드에서 실행할지는 Coroutine
> Dispatcher가 결정합니다.

### 2-3. CoroutineScope: Coroutine의 작업장

Coroutine은 아무 데서나 막 띄우면 안 됩니다. 어디에 소속된 작업인지가 중요합니다.

이 소속 범위를 `CoroutineScope`라고 합니다.

| Scope                      | 수명                               | 대표 사용처                        |
|:---------------------------|:---------------------------------|:------------------------------|
| `viewModelScope`           | ViewModel이 사라질 때까지               | 화면 상태 로딩, 유저 액션 처리            |
| `lifecycleScope`           | Activity/Fragment Lifecycle까지    | 생명주기와 직접 연결된 작업               |
| `rememberCoroutineScope()` | Composable이 Composition에 남아있는 동안 | Snackbar, Drawer 열기 같은 UI 이벤트 |
| WorkManager 내부 Scope       | Worker 실행 중                      | 앱이 꺼져도 보장되어야 하는 백그라운드 작업      |

가장 많이 쓰는 것은 `viewModelScope`입니다.

```kotlin
class BenefitViewModel(
    private val repository: BenefitRepository,
) : ViewModel() {
    fun refresh() {
        viewModelScope.launch {
            repository.refreshBenefits()
        }
    }
}
```

ViewModel이 제거되면 `viewModelScope` 안에서 실행 중인 Coroutine도 함께 취소됩니다.

### 2-4. Job: 실행 중인 Coroutine의 손잡이

`launch`를 호출하면 `Job`이 반환됩니다.

`Job`은 실행 중인 Coroutine을 추적하고 취소할 수 있는 손잡이입니다.

```kotlin
private var searchJob: Job? = null

fun search(keyword: String) {
    searchJob?.cancel()
    searchJob = viewModelScope.launch {
        val result = repository.search(keyword)
        _uiState.value = SearchUiState.Success(result)
    }
}
```

검색어가 바뀔 때 이전 검색을 취소하고 최신 검색만 유지하는 패턴입니다. 다만 Flow를 쓰면 이 패턴은 보통 `debounce` + `flatMapLatest`로 더 깔끔하게
표현할 수 있습니다.

### 2-5. Dispatcher: 어떤 스레드에서 실행할지 정하는 관리자

Coroutine은 Dispatcher를 통해 실제 실행 스레드를 고릅니다.

| Dispatcher               | 용도                      |
|:-------------------------|:------------------------|
| `Dispatchers.Main`       | UI 상태 변경, Compose 상태 갱신 |
| `Dispatchers.IO`         | 네트워크, 파일, DB I/O        |
| `Dispatchers.Default`    | CPU 계산, 정렬, JSON 대량 파싱  |
| `StandardTestDispatcher` | Coroutine 테스트           |

```kotlin
suspend fun loadLargeFile(): String {
    return withContext(Dispatchers.IO) {
        file.readText()
    }
}
```

`withContext`는 Coroutine 안에서 실행 환경을 잠시 바꾸는 함수입니다.

> [!TIP]
> Retrofit, Room처럼 Coroutine을 공식 지원하는 라이브러리는 내부에서 적절한 스레드 처리를 해주는 경우가 많습니다. 그래도 파일 I/O나 직접 만든 블로킹
> 코드는 `Dispatchers.IO`로 보내는 습관이 안전합니다.

---
