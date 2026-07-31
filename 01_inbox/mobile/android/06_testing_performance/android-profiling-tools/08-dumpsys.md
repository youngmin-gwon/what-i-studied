# dumpsys

상위 노트: [[android-profiling-tools]]

시스템 서비스 정보 확인.

```bash
# 메모리
adb shell dumpsys meminfo com.example.app

# CPU
adb shell dumpsys cpuinfo

# 배터리
adb shell dumpsys batterystats com.example.app

# 그래픽
adb shell dumpsys gfxinfo com.example.app

# Activity
adb shell dumpsys activity com.example.app

# 네트워크
adb shell dumpsys netstats

# 알람
adb shell dumpsys alarm
```
