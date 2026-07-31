# Intent 의 구성 요소

상위 노트: [android-intent-and-ipc](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/android-intent-and-ipc.md)

```kotlin
val intent = Intent().apply {
    action = Intent.ACTION_VIEW          // 무엇을 할 것인가
    data = Uri.parse("https://example.com") // 대상 데이터
    type = "text/html"                    // MIME 타입
    component = ComponentName(             // 명시적 대상 (옵션)
        "com.example", "com.example.MainActivity"
    )
    putExtra("key", "value")              // 추가 데이터
    addCategory(Intent.CATEGORY_BROWSABLE) // 분류
    addFlags(Intent.FLAG_ACTIVITY_NEW_TASK) // 동작 플래그
}
```

| 속성 | 역할 | 예시 |
|------|------|------|
| **action** | 수행할 작업 | `ACTION_VIEW`, `ACTION_SEND`, `ACTION_DIAL` |
| **data** | 작업 대상 URI | `tel:010-1234-5678`, `content://contacts/1` |
| **type** | MIME 타입 | `image/jpeg`, `text/plain` |
| **component** | 명시적 대상 클래스 | `ComponentName(pkg, cls)` |
| **extras** | 번들 데이터 | `putExtra("userId", "123")` |
| **category** | 추가 분류 | `CATEGORY_LAUNCHER`, `CATEGORY_BROWSABLE` |
| **flags** | 동작 제어 | `FLAG_ACTIVITY_CLEAR_TOP` |
