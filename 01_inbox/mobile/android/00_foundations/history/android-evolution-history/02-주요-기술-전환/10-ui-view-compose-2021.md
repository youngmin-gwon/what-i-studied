---
title: 10-ui-view-compose-2021
tags: []
aliases: []
date modified: 2026-07-31 15:42:51 +09:00
date created: 2026-07-31 15:38:23 +09:00
---

## UI: View → Compose (2021)

상위 노트: [[02-주요-기술-전환]]

**View System** (2008- 현재):

```xml
<!-- XML로 정의 -->
<LinearLayout>
    <TextView android:text="Hello" />
    <Button android:id="@+id/button" />
</LinearLayout>
```

```kotlin
// 코드로 조작
val button = findViewById<Button>(R.id.button)
button.setOnClickListener { }
```

**문제**:

- XML 과 코드 분리 → 유지보수 어려움
- Boilerplate 많음
- 상태 관리 복잡

**Jetpack Compose** (2021):

```kotlin
@Composable
fun Greeting(name: String) {
    var count by remember { mutableStateOf(0) }

    Column {
        Text("Hello $name")
        Button(onClick = { count++ }) {
            Text("Clicked $count times")
        }
    }
}
```

**장점**:

- 선언형 UI (React/SwiftUI 와 유사)
- 상태 자동 업데이트
- Preview 지원
