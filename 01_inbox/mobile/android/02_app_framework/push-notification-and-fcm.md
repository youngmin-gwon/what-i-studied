---
title: push-notification-and-fcm
tags: [android, messaging, fcm, push-notification, notification-manager]
---

# Push Notification & FCM (실시간 푸시 알림 및 메시징)

## 1. 개념 & 비유 (Concept & Real-World Analogy)

### 개념
**Firebase Cloud Messaging (FCM)**은 모바일 기기에 메시지 및 푸시 알림을 무료로 안전하게 전송할 수 있는 교차 플랫폼 데이터 메시징 솔루션입니다. Android 디바이스는 고유한 **FCM Registration Token**을 발급받아 백엔드 서버에 등록하며, 서버는 이 토큰을 목적지 주소 삼아 메시지를 전송합니다. Android OS의 `NotificationManager` 및 `NotificationChannel`을 통해 포그라운드/백그라운드 상태에 따라 적절한 팝업 알림을 표시하게 됩니다.

### 실생활 비유: 등기 등재 등기 우체부 (Registered Express Courier)
FCM 서비스는 **국제 등기 우체국 시스템**입니다.
앱이 설치되면 전 세계에 단 하나뿐인 주소표인 **FCM 토큰(집 주소)**을 발급받아 본사(WAS Server)에 등록해 둡니다. 백엔드가 손님(디바이스)에게 특급 선물(알림 데이터)을 보내고 싶을 때, 우체국(FCM Server)에 선물 상자를 맡깁니다.
등기 우체부(Android OS & Google Play Services)는 손님이 자고 있거나(백그라운드/도즈 모드), 외출 중이어도 대문 앞 배시시 알림함(`NotificationManager`)에 안전하게 배달 봉투를 꽂아둡니다.

---

## 2. 핵심 구성 요소 & 동작 원리 (Core Components & How It Works)

### 핵심 구성 요소
1. **`FirebaseMessagingService`**: FCM 토큰의 생성/갱신(`onNewToken`) 이벤트와 수신된 푸시 페이로드(`onMessageReceived`)를 처리하는 안드로이드 백그라운드 서비스 클래스입니다.
2. **FCM Token (Registration Token)**: 특정 앱 인스턴스와 디바이스 조합을 고유하게 식별하는 암호화 스트링 주소입니다.
3. **Message Payloads**:
   - **Notification Payload**: OS가 백그라운드 상태일 때 자동으로 상단 트레이 알림을 생성합니다 (`title`, `body`).
   - **Data Payload**: 앱이 직접 처리하는 커스텀 Key-Value 페이로드로, 포그라운드/백그라운드에 관계없이 `onMessageReceived`로 전달됩니다.
4. **`NotificationChannel`**: Android 8.0(API level 26) 이상에서 필수로 요구되는 알림 그룹 구분자(중요도, 소리, 진동 패턴 정의)입니다.
5. **`NotificationManager` & `NotificationCompat.Builder`**: OS 시스템 영역에 푸시 UI 팝업을 빌드하고 노출하는 안드로이드 시스템 서비스입니다.

### 동작 흐름도 (Mermaid Diagram)

```mermaid
flowchart TD
    subgraph Client Device (Android)
        APP[Android App]
        FMS[FirebaseMessagingService]
        NM[NotificationManager & Channel]
    end

    subgraph Firebase Cloud Services
        FCM[FCM Gateway Server]
    end

    subgraph App Backend Server
        WAS[App Server / WAS]
    end

    APP -->|"1. Request FCM Token"| FCM
    FCM -->|"2. Issue Token"| APP
    APP -->|"3. Register Token"| WAS

    WAS -->|"4. Send Push Payload + Token"| FCM
    FCM -->|"5. Deliver Push Packet"| FMS

    FMS -->|"6. Foreground: onMessageReceived"| APP
    FMS -->|"7. Build Notification UI"| NM
    FCM -->|"8. Background: OS Auto System Tray"| NM
    NM -->|"9. Display Banner / Sound"| USER((User Screen))
```

---

## 3. 코드 예제 & 사용 방법 (Code Example & Implementation)

### Step 1: `FirebaseMessagingService` 구현
```kotlin
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import android.os.Build
import androidx.core.app.NotificationCompat
import com.google.firebase.messaging.FirebaseMessagingService
import com.google.firebase.messaging.RemoteMessage

class MyFirebaseMessagingService : FirebaseMessagingService() {

    // 새로운 FCM 토큰이 발급되었을 때 호출 (앱 설치, 데이터 삭제 등)
    override fun onNewToken(token: String) {
        super.onNewToken(token)
        sendTokenToServer(token)
    }

    // 포그라운드 상태이거나 Data Payload 수신 시 호출
    override fun onMessageReceived(remoteMessage: RemoteMessage) {
        super.onMessageReceived(remoteMessage)

        val title = remoteMessage.notification?.title ?: remoteMessage.data["title"] ?: "새 알림"
        val body = remoteMessage.notification?.body ?: remoteMessage.data["body"] ?: ""

        showNotification(title, body)
    }

    private fun sendTokenToServer(token: String) {
        // App Backend REST API를 통해 토큰 전송 로직 수행
    }

    private fun showNotification(title: String, body: String) {
        val notificationManager = getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        val channelId = "default_channel_id"

        // Android 8.0 이상 NotificationChannel 생성 필수
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            val channel = NotificationChannel(
                channelId,
                "기본 알림 채널",
                NotificationManager.IMPORTANCE_HIGH
            ).apply {
                description = "주요 공지 및 업데이트 알림을 수신합니다."
            }
            notificationManager.createNotificationChannel(channel)
        }

        val intent = Intent(this, MainActivity::class.java).apply {
            flags = Intent.FLAG_ACTIVITY_CLEAR_TOP or Intent.FLAG_ACTIVITY_SINGLE_TOP
        }
        val pendingIntent = PendingIntent.getActivity(
            this,
            0,
            intent,
            PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
        )

        val notificationBuilder = NotificationCompat.Builder(this, channelId)
            .setSmallIcon(R.drawable.ic_notification)
            .setContentTitle(title)
            .setContentText(body)
            .setAutoCancel(true)
            .setPriority(NotificationCompat.PRIORITY_HIGH)
            .setContentIntent(pendingIntent)

        notificationManager.notify(System.currentTimeMillis().toInt(), notificationBuilder.build())
    }
}
```

### Step 2: `AndroidManifest.xml` 서비스 및 런타임 권한 등록
```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <!-- Android 13 (API 33) 이상 런타임 알림 권한 -->
    <uses-permission android:name="android.permission.POST_NOTIFICATIONS" />

    <application>
        <service
            android:name=".MyFirebaseMessagingService"
            android:exported="false">
            <intent-filter>
                <action android:name="com.google.firebase.MESSAGING_EVENT" />
            </intent-filter>
        </service>
    </application>
</manifest>
```

### Step 3: Android 13+ 런타임 권한 요청 (Activity/Compose)
```kotlin
import android.Manifest
import android.content.pm.PackageManager
import android.os.Build
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat

class MainActivity : AppCompatActivity() {

    private val requestPermissionLauncher = registerForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { isGranted: Boolean ->
        if (isGranted) {
            // 알림 권한 허용됨
        } else {
            // 알림 권한 거부됨
        }
    }

    private fun checkNotificationPermission() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
            if (ContextCompat.checkSelfPermission(this, Manifest.permission.POST_NOTIFICATIONS)
                != PackageManager.PERMISSION_GRANTED) {
                requestPermissionLauncher.launch(Manifest.permission.POST_NOTIFICATIONS)
            }
        }
    }
}
```

---

## 4. 주의사항 & 팁 (Key Considerations & Best Practices)

1. **Android 13 (API 33) POST_NOTIFICATIONS 권한**: API 레벨 33부터 런타임 알림 권한이 필수가 되었으며, 사용자가 승인하지 않으면 알림이 표시되지 않습니다.
2. **Notification Payload 대 Data Payload 동작 차이**:
   - **Notification Payload만 포함 시**: 백그라운드에서 `onMessageReceived`가 호출되지 않고 OS가 직접 시스템 트레이에 알림을 띄웁니다.
   - **Data Payload 활용 권장**: 백그라운드에서도 앱 로직 연동이나 딥링크 처리(Deep Linking)가 필요한 경우 Data Payload 형태로 송신해야 `onMessageReceived` 또는 Intent Extra로 안정적인 데이터 파싱이 가능합니다.
3. **PendingIntent Flag Immutable**: Android 12(API 31) 이상에서는 `PendingIntent` 생성 시 `FLAG_IMMUTABLE` 또는 `FLAG_MUTABLE`을 명시하지 않으면 Crash가 발생합니다.
4. **FCM Token 갱신 대응**: 앱 삭제 후 재설치, 기기 복원, 토큰 만료 시 `onNewToken`이 비동기적으로 트리거되므로 서버 DB 토큰 동기화 코드가 항상 준비되어 있어야 합니다.

---

## 5. 연관 개념 & 참고 링크 (Related Concepts & Relative Markdown Links)

- [Hilt DI Architecture](hilt-di.md) - Service에 의존성 주입을 위한 `@AndroidEntryPoint` 적용
- [Dagger DI Architecture](dagger-di.md) - FCM Service 컴포넌트 그래프 연동
- [Paging 3 Architecture](paging-3.md) - 실시간 알림 데이터 수신 시 페이징 데이터 갱신 연동
