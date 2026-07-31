# Service 심화

상위 노트: [[android-app-components-deep-dive]]

Service 는 백그라운드에서 오래 실행되는 작업을 처리한다.

##### Service 종류

1. **Foreground Service**: 사용자가 인지할 수 있는 작업 (음악 재생, 운동 추적). 알림이 필수.
2. **Background Service**: Android 8.0+ 에서 크게 제한됨. WorkManager 사용 권장.
3. **Bound Service**: 클라이언트 - 서버 인터페이스 제공. 바인드된 컴포넌트가 없으면 종료.

>[!CAUTION] **Android 14+ Foreground Service Type 필수 선언**
>Android 14(API 34)부터 Foreground Service 시작 시 반드시 **`foregroundServiceType`** 을 매니페스트에 명시해야 한다. 미선언 시 `MissingForegroundServiceTypeException` 발생.
>또한, 각 타입별로 **필요한 권한**이 다르며, `FOREGROUND_SERVICE_SPECIAL_USE` 등의 새 타입이 추가되었다.
>
>**필수 선언 타입**: `camera`, `connectedDevice`, `dataSync`, `health`, `location`, `mediaPlayback`, `mediaProjection`, `microphone`, `phoneCall`, `remoteMessaging`, `shortService`, `specialUse`, `systemExempted`

```xml
<!-- Android 14+ 필수: type 미선언 시 크래시 -->
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
<uses-permission android:name="android.permission.FOREGROUND_SERVICE_MEDIA_PLAYBACK" />

<service
    android:name=".MusicService"
    android:foregroundServiceType="mediaPlayback"
    android:exported="false" />
```

```kotlin
// 코드에서도 type 명시 필수 (Android 14+)
ServiceCompat.startForeground(
    this,
    NOTIFICATION_ID,
    notification,
    ServiceInfo.FOREGROUND_SERVICE_TYPE_MEDIA_PLAYBACK  // 필수
)
```

##### Foreground Service 예시

```kotlin
class MusicService : Service() {
    private val CHANNEL_ID = "music_channel"
    private val NOTIFICATION_ID = 1
    
    override fun onCreate() {
        super.onCreate()
        createNotificationChannel()
    }
    
    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        val notification = NotificationCompat.Builder(this, CHANNEL_ID)
            .setContentTitle("음악 재생 중")
            .setContentText("노래 제목")
            .setSmallIcon(R.drawable.ic_music)
            .build()
        
        startForeground(NOTIFICATION_ID, notification)
        
        // 작업 수행
        
        return START_STICKY // 시스템이 종료했다가 재시작
    }
    
    private fun createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(
                CHANNEL_ID,
                "음악 재생",
                NotificationManager.IMPORTANCE_LOW
            )
            val manager = getSystemService(NotificationManager::class.java)
            manager.createNotificationChannel(channel)
        }
    }
    
    override fun onBind(intent: Intent?): IBinder? = null
}
```

```xml
<!-- AndroidManifest.xml -->
<service
    android:name=".MusicService"
    android:foregroundServiceType="mediaPlayback"
    android:exported="false" />
```

##### Bound Service 와 AIDL

[android-binder-and-ipc](../01_system_internals/android-binder-and-ipc.md) 를 통해 프로세스 간 통신이 가능하다.

```kotlin
// 같은 프로세스 내 Binder
class LocalService : Service() {
    private val binder = LocalBinder()
    
    inner class LocalBinder : Binder() {
        fun getService(): LocalService = this@LocalService
    }
    
    override fun onBind(intent: Intent): IBinder = binder
    
    fun getRandomNumber(): Int = Random.nextInt(100)
}

// Activity 에서 바인드
class MainActivity : AppCompatActivity() {
    private var service: LocalService? = null
    private var bound = false
    
    private val connection = object : ServiceConnection {
        override fun onServiceConnected(name: ComponentName?, binder: IBinder?) {
            val localBinder = binder as LocalService.LocalBinder
            service = localBinder.getService()
            bound = true
        }
        
        override fun onServiceDisconnected(name: ComponentName?) {
            bound = false
        }
    }
    
    override fun onStart() {
        super.onStart()
        Intent(this, LocalService::class.java).also { intent ->
            bindService(intent, connection, Context.BIND_AUTO_CREATE)
        }
    }
    
    override fun onStop() {
        super.onStop()
        if (bound) {
            unbindService(connection)
            bound = false
        }
    }
}
```
