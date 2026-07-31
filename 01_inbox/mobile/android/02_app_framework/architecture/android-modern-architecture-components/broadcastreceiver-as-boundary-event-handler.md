# BroadcastReceiver: 시스템 방송 수신기에서 "경계 이벤트 처리기"로

상위 노트: [[android-modern-architecture-components]]

### 5-1. BroadcastReceiver란?

`BroadcastReceiver`는 OS나 다른 앱이 보내는 이벤트 방송을 받는 컴포넌트입니다.

예를 들어 아래 같은 상황이 방송처럼 전달될 수 있습니다.

* 기기 부팅 완료
* 충전기 연결/해제
* 시간대 변경
* 앱 설치/삭제
* 알림 액션 버튼 클릭
* SMS 수신 같은 특수 이벤트

```kotlin
class BootCompletedReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action == Intent.ACTION_BOOT_COMPLETED) {
            // 부팅 이후 필요한 작업 예약
        }
    }
}
```

```xml

<receiver android:name=".BootCompletedReceiver" android:exported="false">
    <intent-filter>
        <action android:name="android.intent.action.BOOT_COMPLETED" />
    </intent-filter>
</receiver>
```

### 5-2. BroadcastReceiver의 핵심 제약

`BroadcastReceiver.onReceive()`는 짧게 끝나야 합니다.

Receiver는 **긴 작업을 직접 수행하는 곳이 아니라, 긴 작업을 예약하거나 앱 내부로 이벤트를 넘기는 곳**입니다.

```kotlin
class BootCompletedReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action == Intent.ACTION_BOOT_COMPLETED) {
            val request = OneTimeWorkRequestBuilder<RefreshTokenWorker>().build()
            WorkManager.getInstance(context).enqueueUniqueWork(
                "refresh-token-after-boot",
                ExistingWorkPolicy.KEEP,
                request,
            )
        }
    }
}
```

### 5-3. 왜 BroadcastReceiver 사용이 줄었나?

과거에는 앱들이 시스템 방송을 광범위하게 받아서 백그라운드 작업을 시작했습니다. 예를 들어 네트워크가 바뀔 때마다 여러 앱이 동시에 깨어나 서버 동기화를 시도할 수 있었습니다.

이 방식은 배터리와 성능에 매우 나쁩니다. 그래서 Android는 암시적 브로드캐스트와 백그라운드 실행을 점점 제한했고, 앱 내부 이벤트 전달은 더 이상 Receiver에 의존하지
않는 방향으로 바뀌었습니다.

### 5-4. 현대 대체재: Kotlin Flow / StateFlow / SharedFlow

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

### 5-5. BroadcastReceiver vs Flow 선택 기준

| 상황                             | 선택                                         |
|:-------------------------------|:-------------------------------------------|
| OS가 보내는 부팅 완료 이벤트를 받아야 함       | BroadcastReceiver                          |
| 알림의 "답장", "삭제", "확인" 액션을 받아야 함 | BroadcastReceiver 또는 PendingIntent 대상 컴포넌트 |
| 앱 내부 로그인 상태 변경을 여러 화면이 알아야 함   | StateFlow/SharedFlow                       |
| DB 변경을 화면이 자동 반영해야 함           | Room + Flow                                |
| 네트워크 연결 상태를 UI가 구독해야 함         | callbackFlow + StateFlow                   |
| 다른 앱이 내 데이터를 조회해야 함            | ContentProvider                            |

> [!TIP]
> Receiver는 "앱 밖에서 들어온 방송을 받는 문"입니다. 앱 안에서 컴포넌트끼리 대화하려고 Receiver를 쓰면 구조가 불필요하게 무거워집니다.

---
