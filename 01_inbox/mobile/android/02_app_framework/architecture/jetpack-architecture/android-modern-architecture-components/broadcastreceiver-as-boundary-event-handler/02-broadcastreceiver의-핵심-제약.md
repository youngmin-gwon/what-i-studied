# BroadcastReceiver의 핵심 제약

`BroadcastReceiver.onReceive()`는 짧게 끝나야 합니다.

Receiver는 **긴 작업을 직접 수행하는 곳이 아니라, 긴 작업을 예약하거나 앱 내부로 이벤트를 넘기는 곳**입니다.

```kotlin
class BootCompletedReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        if (intent.action == Intent.ACTION_BOOT_COMPLETED) {
            val request = OneTimeWorkRequestBuilder<RefreshTokenWorker>().build()
            WorkManager.getInstance(context).enqueueUniqueWork(
                "refresh-token-after-boot",
                ExistingWorkPolicy.KEEP,
                request,
            )
        }
    }
}
```
