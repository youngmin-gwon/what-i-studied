# Binder

상위 노트: [[android-glossary]]

**정의**: 안드로이드의 프로세스 간 통신 (IPC) 메커니즘

**상세**:

커널 드라이버 기반으로 앱과 시스템 서비스 간 메시지를 전달한다. 전통적인 Unix IPC 와 달리 자동으로 호출자의 UID/PID 를 확인하고 권한을 검사한다. 하나의 메모리 복사만으로 데이터 전달이 가능하여 성능이 우수하다.

**예시**:

```kotlin
// 시스템 서비스 호출 (내부적으로 Binder)
val am = getSystemService(ActivityManager::class.java)
val memoryInfo = ActivityManager.MemoryInfo()
am.getMemoryInfo(memoryInfo)
```

**디버깅**:

```bash
# Binder 서비스 목록
adb shell service list

# 특정 서비스 정보
adb shell dumpsys activity services
```

**관련**: [android-binder-and-ipc](../01_system_internals/android-binder-and-ipc.md)

---
