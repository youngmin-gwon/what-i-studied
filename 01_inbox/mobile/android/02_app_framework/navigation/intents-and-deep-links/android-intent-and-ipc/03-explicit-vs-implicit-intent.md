# Explicit vs Implicit Intent

상위 노트: [android-intent-and-ipc](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-intent-and-ipc.md)

##### Explicit Intent (명시적)

대상 컴포넌트를 정확히 지정한다. **앱 내부 화면 전환**에 사용.

```kotlin
// 같은 앱 내에서 Activity 시작
val intent = Intent(this, DetailActivity::class.java).apply {
    putExtra("USER_ID", userId)
}
startActivity(intent)

// 서비스 시작
Intent(this, DownloadService::class.java).also { intent ->
    startService(intent)
}
```

>[!CAUTION] **Devil's Advocate : Single-Activity 시대에서의 Explicit Intent**
>현대 앱에서 Activity 간 `startActivity(intent)` 호출은 **거의 사라졌다**. 화면 전환은 `Navigation Compose` (또는 Navigation Component)로 처리하며, Explicit Intent 는 **외부 앱 실행**(카메라, 설정 등)이나 **Service 시작** 용도로만 남아있다.
>[android-deep-links](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-deep-links.md) 에서 Navigation 기반 딥링크 처리를 참고하라.

##### Implicit Intent (암시적)

대상을 지정하지 않고 **action + data** 로 시스템에 위임한다.

```kotlin
// 웹페이지 열기
val webIntent = Intent(Intent.ACTION_VIEW, Uri.parse("https://developer.android.com"))
startActivity(webIntent)

// 전화 걸기
val dialIntent = Intent(Intent.ACTION_DIAL, Uri.parse("tel:010-1234-5678"))
startActivity(dialIntent)

// 공유하기
val shareIntent = Intent(Intent.ACTION_SEND).apply {
    type = "text/plain"
    putExtra(Intent.EXTRA_TEXT, "공유할 내용")
}
startActivity(Intent.createChooser(shareIntent, "공유 방법 선택"))
```

##### 안전한 Implicit Intent 사용

```kotlin
// ✅ 처리할 수 있는 앱이 있는지 확인 (크래시 방지)
val intent = Intent(Intent.ACTION_VIEW, Uri.parse("geo:37.5665,126.9780"))
if (intent.resolveActivity(packageManager) != null) {
    startActivity(intent)
} else {
    // 지도 앱이 설치되어 있지 않음
    Toast.makeText(this, "지도 앱을 설치해주세요", Toast.LENGTH_SHORT).show()
}
```
