# Dispatcher: 어떤 스레드에서 실행할지 정하는 관리자

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
