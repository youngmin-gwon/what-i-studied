# 디버깅

상위 노트: [[android-app-components-deep-dive]]

```bash
# Activity 스택 확인
adb shell dumpsys activity activities

# Service 목록
adb shell dumpsys activity services

# BroadcastReceiver 히스토리
adb shell dumpsys activity broadcasts

# ContentProvider 확인
adb shell dumpsys activity providers
```
