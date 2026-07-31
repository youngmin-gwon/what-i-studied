# PendingIntent

상위 노트: [[android-intent-and-ipc]]

다른 앱(시스템)이 **우리 앱 대신** 나중에 Intent 를 실행할 수 있도록 하는 토큰이다. 주로 **알림(Notification)**, **AlarmManager**, **위젯** 에서 사용된다.

```kotlin
// 알림 클릭 시 실행할 PendingIntent
val intent = Intent(context, MainActivity::class.java).apply {
    flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
}

val pendingIntent = PendingIntent.getActivity(
    context,
    REQUEST_CODE,
    intent,
    PendingIntent.FLAG_IMMUTABLE  // Android 12+ 필수
)

val notification = NotificationCompat.Builder(context, CHANNEL_ID)
    .setContentTitle("새 메시지")
    .setContentText("확인하세요")
    .setContentIntent(pendingIntent)     // 클릭 시 실행
    .setAutoCancel(true)                 // 클릭 후 알림 제거
    .build()
```

##### PendingIntent 보안 (Android 12+ 필수)

```kotlin
// ✅ FLAG_IMMUTABLE (기본, 대부분의 경우)
// → 수신 앱이 Intent 내용을 수정 불가
PendingIntent.getActivity(ctx, 0, intent, PendingIntent.FLAG_IMMUTABLE)

// ✅ FLAG_MUTABLE (인라인 답장 등 특수한 경우만)
// → 수신 앱이 extras 를 수정 가능
PendingIntent.getActivity(ctx, 0, intent, PendingIntent.FLAG_MUTABLE)

// ✅ FLAG_ONE_SHOT (일회성 작업)
// → 한 번 실행하면 재사용 불가 (리플레이 공격 방지)
PendingIntent.getActivity(ctx, 0, intent,
    PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_ONE_SHOT)
```

>[!CAUTION] **Android 12+ 에서 Mutability 미지정 시 크래시**
>`FLAG_IMMUTABLE` 또는 `FLAG_MUTABLE` 중 하나를 반드시 지정해야 한다. 미지정 시 `IllegalArgumentException` 발생.
