# APEX 확인

상위 노트: [[android-modular-system]]

```bash
# 설치된 APEX 목록
adb shell pm list packages --apex-only

# APEX 정보
adb shell pm dump com.android.runtime

# 마운트된 APEX
adb shell ls /apex/

# APEX 버전
adb shell dumpsys apex
```
