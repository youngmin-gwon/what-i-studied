# Service란?

`Service`는 화면 없이 실행되는 컴포넌트입니다.

전통적으로는 아래 같은 작업에 Service를 많이 사용했습니다.

* 음악 재생
* 파일 다운로드/업로드
* 위치 추적
* 주기적인 서버 동기화
* 블루투스/센서 연결 유지

```kotlin
class MusicService : Service() {
    override fun onBind(intent: Intent?): IBinder? = null

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        // 백그라운드 음악 재생 시작
        return START_STICKY
    }
}
```

```xml

<service android:name=".MusicService" android:exported="false" />
```
