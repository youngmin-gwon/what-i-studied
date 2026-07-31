# ANR (Application Not Responding)

상위 노트: [[android-glossary]]

**정의**: 앱이 5 초 이상 응답하지 않을 때 표시되는 경고

**상세**:

메인 스레드가 블로킹되면 발생한다. 원인은 네트워크 요청, 디스크 I/O, 무한 루프 등이다. ANR 발생 시 `/data/anr/traces.txt` 에 스택 트레이스가 기록된다.

**해결**:

```kotlin
// ❌ 메인 스레드에서 네트워크 (ANR 발생!)
val data = api.getData()

// ✅ 코루틴 사용
lifecycleScope.launch {
    val data = withContext(Dispatchers.IO) {
        api.getData()
    }
    updateUI(data)
}
```

**디버깅**:

```bash
adb pull /data/anr/traces.txt
```

**관련**: [android-debugging-techniques](../06_testing_performance/android-debugging-techniques.md)

---
