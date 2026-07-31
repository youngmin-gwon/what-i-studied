# BroadcastReceiver란?

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
