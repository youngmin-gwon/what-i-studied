# 디버깅

상위 노트: [[android-intent-and-ipc]]

```bash
# Intent 로 Activity 시작 테스트
adb shell am start -a android.intent.action.VIEW -d "https://example.com"

# 특정 앱의 Activity 시작
adb shell am start -n com.example.app/.MainActivity --es "key" "value"

# Broadcast 전송
adb shell am broadcast -a com.example.MY_ACTION

# PendingIntent 관련 정보
adb shell dumpsys activity intents
```
