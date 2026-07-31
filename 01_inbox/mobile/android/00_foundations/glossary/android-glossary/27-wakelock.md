# Wakelock

상위 노트: [[android-glossary]]

**정의**: 기기가 절전 모드로 진입하는 것을 막는 잠금

**상세**:

화면이 꺼져도 CPU/네트워크를 유지해야 할 때 사용한다. 잘못 사용하면 배터리를 심하게 소모하므로 꼭 필요할 때만 짧게 사용해야 한다.

**사용**:

```kotlin
val powerManager = getSystemService(PowerManager::class.java)
val wakeLock = powerManager.newWakeLock(
    PowerManager.PARTIAL_WAKE_LOCK,
    "MyApp::MyWakelockTag"
)

// 획득
wakeLock.acquire(10 * 60 * 1000L)  // 10분 타임아웃

// 해제 (필수!)
wakeLock.release()
```

**디버깅**:

```bash
# Wakelock 확인
adb shell dumpsys power | grep Wake

# 배터리 사용량
adb shell dumpsys batterystats
```

**관련**: [[android-performance-and-debug]]

---
