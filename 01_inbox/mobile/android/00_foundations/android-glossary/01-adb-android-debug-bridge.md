# ADB (Android Debug Bridge)

상위 노트: [[android-glossary]]

**정의**: PC 와 안드로이드 기기를 연결하는 명령줄 도구

**상세**:

개발/디버깅 시 필수 도구로, USB 또는 Wi-Fi 를 통해 기기에 명령을 전송하고 로그를 확인한다. 앱 설치, 파일 전송, 쉘 접근, 디버깅 등 다양한 작업에 사용된다.

**예시**:

```bash
# 연결된 기기 확인
adb devices

# 앱 설치
adb install app-debug.apk

# 로그 확인
adb logcat

# 쉘 접근
adb shell
```

**관련**: [android-debugging-techniques](../06_testing_performance/android-debugging-techniques.md)

---
