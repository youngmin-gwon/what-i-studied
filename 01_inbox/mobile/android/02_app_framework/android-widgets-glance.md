# [[mobile-security]] > [[android-widgets-glance]]

## Widgets & Glance: Snapshot UX

안드로이드 홈 화면에서 한눈에 정보를 제공하는 **홈 화면 위젯(App Widgets)**과 이를 Compose 방식으로 구현하는 **Jetpack Glance** 기술을 분석합니다. 

단순히 정보를 표시하는 것을 넘어, 다른 프로세스(홈 화면)에서 렌더링되는 `RemoteViews`의 제약을 이해하고 효율적인 데이터 갱신 및 실시간 현황(Ongoing Notifications)을 제공하는 전략을 수립하는 것이 목표입니다.

---

### 💡 Context: 위젯의 진화와 Glance의 가치

전통적인 XML 기반 위젯 개발은 복잡하고 오류가 잦았으나, Jetpack Glance는 Compose의 선언형 모델을 도입하여 이를 획기적으로 개선했습니다. 이제 복잡한 레이아웃과 데이터 바인딩을 보다 직관적으로 처리할 수 있습니다. [[android-ui-system]]의 확장된 개념입니다.

> [!NOTE] **상호 참조**
> iOS의 위젯 및 라이브 액티비티 방식은 [[apple-widgets-live-activities]]를 참고하세요.

---

### 1. Jetpack Glance (권장)

`RemoteViews`를 직접 다루는 대신, Compose의 선언형 문법을 사용하여 위젯을 정의한다.

#### GlanceWidget 구현

```kotlin
class MyAppWidget : GlanceAppWidget() {

    override suspend fun provideGlance(context: Context, id: GlanceId) {
        // 데이터 준비 (DataStore 등에서 읽어오기)
        val data = repository.getData()

        provideContent {
            GlanceContent(data)
        }
    }

    @Composable
    private fun GlanceContent(data: MyData) {
        Column(
            modifier = GlanceModifier.fillMaxSize()
                .background(GlanceTheme.colors.surface),
            verticalAlignment = Alignment.CenterVertically,
            horizontalAlignment = Alignment.CenterHorizontally
        ) {
            Text(text = data.title, style = TextStyle(fontSize = 18.sp))
            Button(text = "새로고침", onClick = actionRunCallback<RefreshAction>())
        }
    }
}
```

### 2. RemoteViews (레거시/내부 동작 방식)

안드로이드 위젯은 다른 프로세스(시스템 홈 화면)에서 그려지기 때문에 통상적인 뷰 계층 구조를 가질 수 없다. `RemoteViews`는 이 제약을 극복하기 위해 "특정 뷰를 이렇게 그려라"는 명령의 집합이다.

> [!CAUTION] **Devil's Advocate : RemoteViews 직접 만지는 것은 위험**
> `RemoteViews`를 직접 코딩하면 레이아웃 XML과 소스 코드가 분리되어 가독성이 떨어지며, `PendingIntent` 관리가 매우 번잡해진다. 신규 위젯은 무조건 Glance를 사용하라.

### 🏛️ 핵심 아키텍처 및 상태 관리

위젯은 라이프사이클이 짧으며, 데이터 갱신 시 OS에 명시적으로 요청해야 한다.

```kotlin
// 데이터 업데이트 시 위젯 갱신 (WorkManager 등에서 호출)
viewModelScope.launch {
    GlanceAppWidgetManager(context).getGlanceIds(MyAppWidget::class.java).forEach { id ->
        MyAppWidget().update(context, id)
    }
}
```

### 🚀 실시간 현황: Ongoing Notifications & Live Updates

iOS의 **Live Activities**에 대응하는 안드로이드의 전략은 전통적인 **Ongoing Notifications**에서 최신 **Live Updates** 트렌드로 진화하고 있다.

#### 1. Ongoing Notifications (진행 중인 알림)

가장 보편적인 방법으로, `Foreground Service`와 결합하여 잠금 화면과 알림창에 실시간 정보를 고정한다.

```kotlin
val builder = NotificationCompat.Builder(context, CHANNEL_ID)
    .setSmallIcon(R.drawable.ic_delivery)
    .setContentTitle("배달 현황")
    .setContentText("라이더가 출발했습니다 (5분 내 도착)")
    .setOngoing(true) // 사용자가 스와이프해서 지울 수 없음
    .setOnlyAlertOnce(true) // 업데이트 시 소리/진동 중복 방지
    .setForegroundServiceBehavior(NotificationCompat.FOREGROUND_SERVICE_IMMEDIATE)
```

#### 2. RemoteViews Custom Layout

알림창 내부의 레이아웃을 직접 디자인하여 iOS Live Activity 와 유사한 커스텀 UI를 제공할 수 있다.

```kotlin
val remoteViews = RemoteViews(packageName, R.layout.notification_delivery_status)
remoteViews.setTextViewText(R.id.status_text, "도착 임박!")
builder.setCustomContentView(remoteViews)
```

#### 3. Android 16+ Live Updates (표준화된 실시간 갱신)

Android 16부터는 일관성 없는 알림 레이아웃을 지양하고, 시스템이 직접 렌더링하는 **Live Updates** 프레임워크가 도입되었다.

- **ProgressStyle**: 알림 템플릿에 `ProgressStyle`을 적용하면 진행률(Progress), 예상 시간(ETA), 실시간 상태 텍스트가 알림창 최상단에 고정된다.
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


> [!TIP] **iOS 비교: Live Activities vs Android Live Updates**
> - **iOS**: `ActivityKit`을 통해 잠금 화면 하단과 Dynamic Island를 전용 레이아웃으로 점유함.
> - **Android**: 알림(Notification) 시스템의 확장성(Ongoing, Custom Views)을 활용하며, Android 16부터는 시스템 최상단 칩(Chip) 영역까지 활용 범위가 넓어짐.

### See Also

- [[android-ui-system]]
- [[android-compose-internals]]
- [[android-background-processing]]
- [[android-persistence-room-datastore]]
