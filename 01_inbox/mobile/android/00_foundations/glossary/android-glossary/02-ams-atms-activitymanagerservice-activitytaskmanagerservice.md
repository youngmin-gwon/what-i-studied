# AMS/ATMS (ActivityManagerService / ActivityTaskManagerService)

상위 노트: [[android-glossary]]

**정의**: 앱 생명주기와 Activity 스택을 관리하는 시스템 서비스

**상세**:

Android 10 부터 분리되었다. AMS 는 프로세스/Service/Broadcast 를 관리하고, ATMS 는 Activity/Task/Window 를 담당한다. 앱 시작, 종료, 프로세스 우선순위 결정 등 핵심 역할을 한다.

**예시**:

```bash
# Activity 스택 확인
adb shell dumpsys activity activities

# 프로세스 목록
adb shell dumpsys activity processes
```

**관련**: [[android-activity-manager-and-system-services]]

---
