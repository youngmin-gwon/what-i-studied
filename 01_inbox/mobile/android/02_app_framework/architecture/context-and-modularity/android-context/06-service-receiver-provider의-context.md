# Service, Receiver, Provider의 Context

상위 노트: [android-context](01_inbox/mobile/android/02_app_framework/architecture/context-and-modularity/android-context.md)

### 6-1. Service Context

`Service`도 `Context`입니다. Foreground Service에서 알림 채널, 알림 매니저, 파일, 리소스에 접근할 때 사용합니다.

```kotlin
class MusicService : Service() {
    override fun onCreate() {
        super.onCreate()

        val notificationManager =
            getSystemService(NotificationManager::class.java)
    }
}
```

Service Context는 화면 UI를 소유하지 않습니다. Dialog 같은 화면 UI를 직접 띄우는 역할로 쓰면 구조가 어색해집니다.

### 6-2. BroadcastReceiver의 Context

`BroadcastReceiver.onReceive()`로 들어오는 `context`는 짧은 처리에 사용합니다.

```kotlin
class BootReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action == Intent.ACTION_BOOT_COMPLETED) {
            WorkManager.getInstance(context.applicationContext)
                .enqueue(OneTimeWorkRequestBuilder<SyncWorker>().build())
        }
    }
}
```

Receiver에서는 긴 작업을 직접 하지 말고, `WorkManager`나 foreground service로 넘기는 편이 맞습니다.

### 6-3. ContentProvider의 Context

`ContentProvider` 내부에서는 `context`로 DB, 파일, 리소스에 접근할 수 있습니다.

```kotlin
class MyProvider : ContentProvider() {
    override fun onCreate(): Boolean {
        val appContext = context?.applicationContext ?: return false
        // DB 초기화 등
        return true
    }
}
```

Provider는 앱 간 데이터 창구이므로 UI 작업보다 데이터 접근 경계로 보는 편이 맞습니다.

---
