# 현대 대체재: Kotlin Flow / StateFlow / SharedFlow

앱 내부에서 "로그인 상태가 바뀌었다", "장바구니가 갱신됐다", "네트워크 상태가 바뀌었다" 같은 이벤트를 전달하려고 BroadcastReceiver를 쓰는 것은 현대 구조에서는
과합니다.

앱 내부 상태와 이벤트는 `Flow`, `StateFlow`, `SharedFlow`, `Channel`이 더 적합합니다.

| 도구             | 용도                        | 대표 예시                     | 비유      |
|:---------------|:--------------------------|:--------------------------|:--------|
| **Flow**       | 시간에 따라 여러 값을 내보내는 비동기 스트림 | Room DB 변경 관찰, 네트워크 상태 관찰 | 물길      |
| **StateFlow**  | 현재 상태를 항상 1개 보관하고 최신값 제공  | 화면 UI 상태, 로그인 세션 상태       | 전광판     |
| **SharedFlow** | 여러 구독자에게 이벤트 발행           | Snackbar, Toast, 네비게이션 신호 | 사내 방송   |
| **Channel**    | 한 소비자에게 큐 형태로 이벤트 전달      | 순서가 중요한 단일 소비 이벤트         | 번호표 대기열 |

> [!IMPORTANT]
> 이 도구들은 **앱 내부 프로세스 안에서** 상태와 이벤트를 전달하는 Kotlin 도구입니다. 다른 앱으로 데이터를 공개하거나 전달하는 수단이 아닙니다. 앱 밖으로 데이터를
> 열어야 하면 `ContentProvider`, 파일 공유는 `FileProvider`, 한 번의 요청 전달은 `Intent`를 사용합니다.

```kotlin
sealed interface LoginEvent {
    data object Success : LoginEvent
}

class AuthRepository {
    private val _loginEvents = MutableSharedFlow<LoginEvent>()
    val loginEvents: SharedFlow<LoginEvent> = _loginEvents.asSharedFlow()

    suspend fun login(email: String, password: String) {
        // API 호출
        _loginEvents.emit(LoginEvent.Success)
    }
}
```

```kotlin
class HomeViewModel(
    authRepository: AuthRepository,
) : ViewModel() {
    init {
        viewModelScope.launch {
            authRepository.loginEvents.collect { event ->
                when (event) {
                    LoginEvent.Success -> {
                        // 홈 데이터 새로고침
                    }
                }
            }
        }
    }
}
```
