# Breakpoint Debugging

상위 노트: [android-debugging-techniques](01_inbox/mobile/android/06_testing_performance/debugging/android-debugging-techniques.md)

##### Android Studio Debugger

```kotlin
fun processData(items: List<Item>) {
    items.forEach { item ->
        // 여기에 브레이크포인트 설정
        val result = transform(item)
        save(result)
    }
}
```

**조건부 브레이크포인트:**

```kotlin
// 브레이크포인트 우클릭 → Condition
item.id == "특정ID"
```

**로그 브레이크포인트:**

```kotlin
// Evaluate and log: "Processing item: " + item.id
// Suspend: 체크 해제
```

##### JDWP (Java Debug Wire Protocol)

```bash
# 디버그 가능한 프로세스 확인
adb jdwp

# 포트 포워딩
adb forward tcp:8700 jdwp:12345

# Android Studio 에서 Attach to Process
```
