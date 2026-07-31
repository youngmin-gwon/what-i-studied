---
title: 04-broadcastreceiver-상세
tags: []
aliases: []
date modified: 2026-07-31 16:29:44 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## BroadcastReceiver 상세

상위 노트: [android-app-components-deep-dive](01_inbox/mobile/android/02_app_framework/architecture/app-components/android-app-components-deep-dive.md)

시스템이나 앱이 보내는 방송을 받는다.

### 등록 방식

**Manifest 등록** (정적):

```xml
<receiver android:name=".BootReceiver"
    android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.BOOT_COMPLETED" />
    </intent-filter>
</receiver>
```

**코드 등록** (동적, 권장):

```kotlin
class MainActivity : AppCompatActivity() {
    private val receiver = object : BroadcastReceiver() {
        override fun onReceive(context: Context?, intent: Intent?) {
            when (intent?.action) {
                Intent.ACTION_BATTERY_LOW -> {
                    // 배터리 부족 처리
                }
            }
        }
    }
    
    override fun onResume() {
        super.onResume()
        val filter = IntentFilter(Intent.ACTION_BATTERY_LOW)
        registerReceiver(receiver, filter)
    }
    
    override fun onPause() {
        super.onPause()
        unregisterReceiver(receiver)
    }
}
```

### 제약사항

- Android 8.0+ 에서 암시적 브로드캐스트 수신이 크게 제한됨
- `onReceive()` 는 10 초 안에 완료해야 함 ([ANR](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md#anr) 방지)
- 긴 작업은 [WorkManager](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md#workmanager) 나 `goAsync()` 사용

```kotlin
class MyReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        val pendingResult = goAsync()
        
        CoroutineScope(Dispatchers.IO).launch {
            try {
                // 긴 작업 수행
                delay(5000)
            } finally {
                pendingResult.finish()
            }
        }
    }
}
```
