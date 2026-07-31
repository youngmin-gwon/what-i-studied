# 멀티 윈도우와 Activity 인스턴스

### 6-1. 안드로이드 태블릿도 iPad처럼 여러 창을 지원하나?

**네, 완벽하게 가능합니다.** Android Nougat(API 24)부터 멀티 윈도우를 지원하며, 화면 분할(Split Screen), 팝업 창(Freeform), 다중 인스턴스(Multi-instance)까지 지원합니다.

### 6-2. 멀티 윈도우를 위해 Activity를 여러 개 만들어야 할까?

**아닙니다.** 개발자가 `MainActivity2`, `MainActivity3`을 따로 만드는 게 아니라, 시스템이 `MainActivity`라는 설계도를 가지고 **여러 인스턴스를 독립적으로 찍어냅니다**.

이는 **SwiftUI의 `WindowGroup`이 여러 윈도우 인스턴스를 찍어내는 철학**과 본질적으로 매우 닮아있습니다.

```xml
<!-- 매니페스트에 딱 한 줄의 옵션만 필요 -->
<activity
    android:name=".MainActivity"
    android:launchMode="standard" />
```

새 창 띄우기 코드 예시:
```kotlin
val intent = Intent(context, MainActivity::class.java).apply {
    addFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_LAUNCH_ADJACENT)
    data = Uri.parse("https://example.com/mail/45")
}
context.startActivity(intent)
```

---
