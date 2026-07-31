# Doze / App Standby

상위 노트: [[android-glossary]]

**정의**: 배터리 절약을 위한 앱 활동 제한 모드

**상세**:

- **Doze**: 기기가 움직이지 않고 화면 꺼진 상태가 지속되면 네트워크/Wakelock/AlarmManager 제한
- **App Standby**: 미사용 앱의 백그라운드 작업 제한

**Doze 단계**:

```
화면 꺼짐 → 30분 대기 → Light Doze (제한 시작)
           → 1시간 대기 → Deep Doze (완전 제한)
```

**예외 목록**:

```kotlin
// 배터리 최적화 제외 요청
val intent = Intent(Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS)
intent.data = Uri.parse("package:$packageName")
startActivity(intent)
```

**테스트**:

```bash
# Doze 강제 진입
adb shell dumpsys deviceidle force-idle

# 해제
adb shell dumpsys deviceidle unforce
```

**관련**: [[android-performance-and-debug]]

---

### F
