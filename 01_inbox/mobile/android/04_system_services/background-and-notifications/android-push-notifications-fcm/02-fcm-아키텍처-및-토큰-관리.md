# FCM 아키텍처 및 토큰 관리

앱이 처음 실행되면 FCM 서버로부터 고유한 **Registration Token**을 발급받는다. 서버는 이 토큰을 기반으로 특정 기기를 식별한다.

```kotlin
// FirebaseMessagingService 구현
class MyFcmService : FirebaseMessagingService() {

    override fun onNewToken(token: String) {
        // 새 토큰이 발급됨. 서버(App Server)에 전송하여 저장해야 함
        sendTokenToServer(token)
    }

    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        // 메시지 수신 시 호출 (Data 페이로드가 포함된 경우 필수 호출)
        handleMessage(remoteMessage)
    }
}
```
