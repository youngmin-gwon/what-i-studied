# Foreground Service 예시

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
