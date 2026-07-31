# 멀티 인스턴스 (Multi-instance)

생산성 향상을 위해 한 앱의 창을 여러 개 띄우는 기능이 중요하다. (예: 브라우저 탭, 메모장 여러 개)

```kotlin
val intent = Intent(this, MainActivity::class.java).apply {
    addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_MULTIPLE_TASK)
}
startActivity(intent)
```

---
