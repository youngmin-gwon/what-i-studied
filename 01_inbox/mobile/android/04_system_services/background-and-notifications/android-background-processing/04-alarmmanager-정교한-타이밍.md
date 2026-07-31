# AlarmManager (정교한 타이밍)

정확한 시간에 특정 작업을 수행해야 할 때(알람 시계, 약 복용 알림) 사용한다.

```kotlin
val alarmManager = context.getSystemService(Context.ALARM_SERVICE) as AlarmManager
val intent = Intent(context, AlarmReceiver::class.java)
val pendingIntent = PendingIntent.getBroadcast(
    context, 0, intent, PendingIntent.FLAG_IMMUTABLE
)

// 정확한 시간 예약 (Android 12+ 에서는 SCHEDULE_EXACT_ALARM 권한 확인 필수)
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.S && alarmManager.canScheduleExactAlarms()) {
    alarmManager.setExactAndAllowWhileIdle(
        AlarmManager.RTC_WAKEUP,
        triggerTimeMillis,
        pendingIntent
    )
}
```
