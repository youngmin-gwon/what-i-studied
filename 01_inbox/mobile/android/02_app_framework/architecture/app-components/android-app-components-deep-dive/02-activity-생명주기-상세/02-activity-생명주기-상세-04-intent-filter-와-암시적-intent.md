# Intent Filter 와 암시적 Intent

Activity 가 어떤 작업을 처리할 수 있는지 선언한다. Intent 에 대한 자세한 내용은 [android-intent-and-ipc](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-intent-and-ipc.md) 참고.

```xml
<activity android:name=".ShareActivity">
    <intent-filter>
        <action android:name="android.intent.action.SEND" />
        <category android:name="android.intent.category.DEFAULT" />
        <data android:mimeType="text/plain" />
    </intent-filter>
</activity>
```

```kotlin
// 암시적 Intent 로 공유
val sendIntent = Intent().apply {
    action = Intent.ACTION_SEND
    putExtra(Intent.EXTRA_TEXT, "공유할 텍스트")
    type = "text/plain"
}
val shareIntent = Intent.createChooser(sendIntent, null)
startActivity(shareIntent)
```

>[!WARNING] **Android 11+ `<queries>` 태그 필수**
>암시적 Intent 로 외부 앱을 실행하거나 `resolveActivity()` 를 호출하려면 매니페스트에 `<queries>` 를 선언해야 한다. 미선언 시 대상 앱이 보이지 않아 `null` 반환.
>상세는 [android-intent-and-ipc](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-intent-and-ipc.md) 참고.
