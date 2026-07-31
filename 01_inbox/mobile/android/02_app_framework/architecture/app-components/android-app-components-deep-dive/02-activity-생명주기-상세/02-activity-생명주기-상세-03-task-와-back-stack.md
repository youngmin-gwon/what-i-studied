# Task 와 Back Stack

Task 는 사용자가 작업을 수행하는 Activity 의 스택이다.

- **Standard**: 기본 모드. 매번 새 인스턴스 생성.
- **SingleTop**: 스택 최상단에 이미 있으면 `onNewIntent()` 호출, 아니면 새로 생성.
- **SingleTask**: Task 내에 하나만 존재. 이미 있으면 위의 Activity 들을 모두 제거.
- **SingleInstance**: 독립된 Task 에 혼자 존재. 다른 Activity 와 스택을 공유하지 않음.

```xml
<!-- AndroidManifest.xml -->
<activity
    android:name=".MainActivity"
    android:launchMode="singleTop" />
```

```kotlin
// 프로그래밍 방식으로 제어
val intent = Intent(this, DetailActivity::class.java).apply {
    flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP
}
startActivity(intent)
```
