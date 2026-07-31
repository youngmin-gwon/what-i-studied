# 🚀 실시간 현황: Ongoing Notifications & Live Updates

iOS 의 **Live Activities**에 대응하는 안드로이드의 전략은 전통적인 **Ongoing Notifications**에서 최신 **Live Updates** 트렌드로 진화하고 있다.

##### 1. Ongoing Notifications (진행 중인 알림)

가장 보편적인 방법으로, `Foreground Service` 와 결합하여 잠금 화면과 알림창에 실시간 정보를 고정한다.

```kotlin
val builder = NotificationCompat.Builder(context, CHANNEL_ID)
    .setSmallIcon(R.drawable.ic_delivery)
    .setContentTitle("배달 현황")
    .setContentText("라이더가 출발했습니다 (5분 내 도착)")
    .setOngoing(true) // 사용자가 스와이프해서 지울 수 없음
    .setOnlyAlertOnce(true) // 업데이트 시 소리/진동 중복 방지
    .setForegroundServiceBehavior(NotificationCompat.FOREGROUND_SERVICE_IMMEDIATE)
```

##### 2. RemoteViews Custom Layout

알림창 내부의 레이아웃을 직접 디자인하여 iOS Live Activity 와 유사한 커스텀 UI 를 제공할 수 있다.

```kotlin
val remoteViews = RemoteViews(packageName, R.layout.notification_delivery_status)
remoteViews.setTextViewText(R.id.status_text, "도착 임박!")
builder.setCustomContentView(remoteViews)
```

##### 3. Android 16+ Live Updates (표준화된 실시간 갱신)

Android 16 부터는 일관성 없는 알림 레이아웃을 지양하고, 시스템이 직접 렌더링하는 **Live Updates** 프레임워크가 도입되었다.

- **ProgressStyle**: 알림 템플릿에 `ProgressStyle` 을 적용하면 진행률(Progress), 예상 시간(ETA), 실시간 상태 텍스트가 알림창 최상단에 고정된다.
- **Status Bar Chip**: 사용자가 앱을 벗어나도 상태바 공간에 **Pill-shaped Chip**이 유지되어 실시간 정보를 계속 확인할 수 있다. (iOS Dynamic Island 대칭 기능)

```kotlin
// Android 16 (Baklava) 라이브 업데이트 예시
val updateTemplate = LiveUpdateTemplate.Builder()
    .setProgress(current = 60, total = 100)
    .setStateText("라이더가 이동 중입니다")
    .setEstimatedArrivalTime(etaMillis)
    .build()

notificationManager.notifyLiveUpdate(ID, updateTemplate)
```

>[!TIP] **iOS 비교: Live Activities vs Android Live Updates**
> - **iOS**: `ActivityKit` 을 통해 잠금 화면 하단과 Dynamic Island 를 전용 레이아웃으로 점유함.
> - **Android**: 알림(Notification) 시스템의 확장성(Ongoing, Custom Views)을 활용하며, Android 16 부터는 시스템 최상단 칩(Chip) 영역까지 활용 범위가 넓어짐.
