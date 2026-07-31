# 알림(Notification)에서의 딥링크

```kotlin
fun createDeepLinkNotification(context: Context, productId: String) {
    val deepLinkIntent = Intent(
        Intent.ACTION_VIEW,
        Uri.parse("https://www.example.com/product/$productId"),
        context,
        MainActivity::class.java
    )
    
    val pendingIntent = TaskStackBuilder.create(context).run {
        addNextIntentWithParentStack(deepLinkIntent)
        getPendingIntent(0, PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT)
    }
    
    val notification = NotificationCompat.Builder(context, CHANNEL_ID)
        .setContentTitle("새 상품 알림")
        .setContentText("관심 상품이 할인 중입니다")
        .setContentIntent(pendingIntent)
        .setAutoCancel(true)
        .build()
    
    NotificationManagerCompat.from(context).notify(NOTIFICATION_ID, notification)
}
```
