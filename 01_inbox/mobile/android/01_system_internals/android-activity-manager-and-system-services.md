---
title: android-activity-manager-and-system-services
tags: []
aliases: []
date modified: 2026-04-05 17:42:30 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [[mobile-security]] > [[android-activity-manager-and-system-services]]

### ActivityManager & System Services: The OS Brain

**ActivityManagerService(AMS)**와 **ActivityTaskManagerService(ATMS)**는 안드로이드의 핵심인 **앱 생명주기 관리자**입니다. 이들은 새로운 앱의 시작, 화면 전환, 그리고 메모리 부족 시의 프로세스 종료 등 시스템 전체의 자원을 조율하는 중추적인 역할을 수행합니다.

---

#### 💡 Context: 왜 중앙 관리가 필요한가?

모바일 환경은 데스크톱보다 메모리 자원이 훨씬 제한적이며 배터리 소모에 민감합니다.

- **Efficient Multitasking**: 사용자가 홈 버튼을 눌러 앱을 떠날 때, 시스템은 해당 앱을 완전히 종료하지 않고 캐시 상태로 유지하여 재시작 속도를 높입니다.
- **Priority-based Killing**: 메모리가 부족해지면 시스템은 현재 사용자가 보지 않는 우선순위가 낮은 앱부터 차례로 정리하여 포그라운드 앱의 부드러운 작동을 보장합니다. (LMKD 협업)
- **Centralized Governance**: 모든 프로세스의 생성과 소멸은 **System Server** 내의 이 서비스들을 통해 엄격하게 통제됩니다.

---

#### 🧱 AMS vs ATMS 분리 (Android 10+)

안드로이드 10 이전에는 AMS 가 모든 기능을 담당하는 거대 클래스(3 만 줄 이상)였으나, 현재는 책임이 분리되었습니다.

- **ActivityTaskManagerService (ATMS)**: Activity, Task 스택, Window 관리 등 **사용자 인터페이스(UI) 중심**의 전환을 담당합니다.
- **ActivityManagerService (AMS)**: 프로세스 생성, Service/Broadcast 관리, 권한 검사 등 **백그라운드 중심**의 운영을 담당합니다.

---

#### ⚖️ 프로세스 우선순위 및 OOM Adjuster

안드로이드는 프로세스의 현재 상태에 따라 **ADJ 점수**를 부여하며, 이 점수가 높을수록 시스템에 의해 먼저 종료될 가능성이 높아집니다.

1. **FOREGROUND_APP (ADJ 0)**: 현재 사용자의 입력을 받고 있는 앱. 최우선 보호 대상.
2. **VISIBLE_APP (ADJ 100)**: 화면에 보이지만 포커스는 없는 앱.
3. **PERCEPTIBLE_APP (ADJ 200)**: 보이지 않지만 음악 재생 등 사용자가 인지할 수 있는 작업을 수행 중인 앱.
4. **CACHED_APP (ADJ 900~999)**: 백그라운드에서 캐시된 앱. 메모리 부족 시 가장 먼저 정리됩니다.

---

#### 🛡️ ANR (App Not Responding) 감지

시스템 서비스는 앱이 제시간에 반응하지 않을 경우 사용자에게 알리고 앱을 종료시킬 수 있는 Watchdog 기능을 수행합니다.

- **Input Timeout**: 5 초간 입력 이벤트에 응답하지 않는 경우.
- **Broadcast Timeout**: 포그라운드 10 초, 백그라운드 60 초 내에 처리가 완료되지 않는 경우.
- **Service Timeout**: 20 초 내에 서비스 시작 절차가 완료되지 않는 경우.

---

#### 📚 연관 문서 및 심화 학습
- [[android-binder-and-ipc]] - 시스템 서비스 통신과 Binder 기술
- [[android-zygote-and-runtime]] - 새로운 앱 프로세스가 생성되는 과정
- [[android-kernel]] - LMKD 와의 메모리 관리 협업
- [[mobile-android-foundation-security]] - 권한 검사 및 샌드박싱 보안
- [[android-process-and-memory]] - 메모리 관리 아키텍처 상세
- [[android-performance-and-debug]] - dumpsys 등을 활용한 실전 디버깅
��라운드) / 60 초 (백그라운드)
1. Service 20 초 미응답

#### Rescue Party

반복 크래시/ANR 시 복구 시도:

```
Level 1: 위험 권한 리셋
Level 2: 모든 앱 데이터 삭제
Level 3: 공장 초기화 제안
```

---

### 디버깅

#### dumpsys activity

```bash
# Activity 스택
adb shell dumpsys activity activities

# 프로세스 목록
adb shell dumpsys activity processes

# 서비스 상태
adb shell dumpsys activity services

# 최근 앱
adb shell dumpsys activity recents

# OOM Adj 점수
adb shell dumpsys activity oom
```

#### cmd activity

```bash
# Activity 강제 시작
adb shell am start -n com.example/.MainActivity

# Service 시작
adb shell am startservice -n com.example/.MyService

# Broadcast 전송
adb shell am broadcast -a android.intent.action.BOOT_COMPLETED

# 프로세스 종료
adb shell am force-stop com.example

# 앱 데이터 삭제
adb shell pm clear com.example
```

---

### 학습 리소스

**공식 문서**:

- [ActivityManager](../../../../https:/developer.android.com/reference/android/app/ActivityManager.md)
- [Services](../../../../https:/developer.android.com/guide/components/services.md)
- [Processes and App Lifecycle](../../../../https:/developer.android.com/guide/components/activities/process-lifecycle.md)

**소스 코드**:

- [ActivityManagerService](../../../../https:/cs.android.com/android/platform/superproject/+/master:frameworks/base/services/core/java/com/android/server/am/ActivityManagerService.java.md)
- [ActivityTaskManagerService](../../../../https:/cs.android.com/android/platform/superproject/+/master:frameworks/base/services/core/java/com/android/server/wm/ActivityTaskManagerService.java.md)

---

### 연결 문서

[android-binder-and-ipc](android-binder-and-ipc.md) - System Service 통신

[android-zygote-and-runtime](android-zygote-and-runtime.md) - 프로세스 생성

[android-kernel](android-kernel.md) - LMKD 와 메모리 관리

[android-security-and-sandboxing](../05_security_privacy/android-security-and-sandboxing.md) - 권한 검사

[android-process-and-memory](android-process-and-memory.md) - 메모리 관리 상세
