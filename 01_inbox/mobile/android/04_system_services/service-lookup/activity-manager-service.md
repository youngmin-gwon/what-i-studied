---
title: activity-manager-service
tags: [activity-manager, ams, android, atms, backstack, lifecycle, system-services]
aliases: [ActivityManagerService, ActivityTaskManagerService, AMS, ATMS]
date modified: 2026-08-20 17:13:06 +09:00
date created: 2026-08-07 13:34:00 +09:00
---

## ActivityManagerService (AMS) & ActivityTaskManagerService (ATMS)

### 1. 개요 (Overview)

**ActivityManagerService (AMS)** 와 **ActivityTaskManagerService (ATMS)** 는 [system_server](../../01_system_internals/boot-and-runtime/system-server/system-server.md) 내부에서 상주하며 **안드로이드 4 대 앱 컴포넌트([Activity](../../02_app_framework/architecture/app-components/activity.md), [Service](../../02_app_framework/architecture/app-components/service.md), [BroadcastReceiver](../../02_app_framework/architecture/app-components/broadcast-receiver.md), [ContentProvider](../../02_app_framework/architecture/app-components/content-provider.md))의 컴포넌트 수명주기(Lifecycle), [앱 프로세스](../../01_system_internals/boot-and-runtime/zygote-runtime/zygote-runtime.md) 생성/수거, Task 백스택(Backstack) 및 [윈도우 계층 구조(WMS)](window-manager-service.md) 를 관제하는 안드로이드 중심 시스템 서비스**이다.

Android 10(Q) 이전에는 AMS 가 모든 책임을 전담했으나, Android 10 이상부터 멀티 윈도우, 화면 분할, 폴더블 UI 처리를 정밀화하기 위해 **[Activity](../../02_app_framework/architecture/app-components/activity.md) 수명주기 및 Task 백스택 관리는 ATMS (ActivityTaskManagerService)** 로 아키텍처가 분리되었고, **[앱 프로세스](../../01_system_internals/boot-and-runtime/zygote-runtime/zygote-runtime.md) OOM 점수([LMK](../../01_system_internals/kernel-and-hal/kernel/lmkd-memory-pressure.md)) 및 백그라운드 서비스 관리는 AMS** 가 전담한다.

---

#### 초보자를 위한 쉽게 이해하는 비유

- **AMS & ATMS (시청 주민등록국과 무대 연극 연출 감독)**:
  - **AMS (주민등록 주민과장)**: [앱 프로세스](../../01_system_internals/boot-and-runtime/zygote-runtime/zygote-runtime.md)가 [Zygote](../../01_system_internals/boot-and-runtime/zygote-runtime/zygote-runtime.md) 에서 태어나고, 생존 점수([oom_score_adj](../../01_system_internals/kernel-and-hal/kernel/lmkd-memory-pressure.md))를 매기며, 메모리가 부족할 때 [LMK](../../01_system_internals/kernel-and-hal/kernel/lmkd-memory-pressure.md) 로 수거하는 종합 인적 프로세스 관리자.
  - **ATMS (연극 무대 연출 감독)**: 현재 주연 배우([Activity](../../02_app_framework/architecture/app-components/activity.md))가 무대 전면에 나올지, 뒤로 들어갈지(Backstack), [윈도우 계층(WMS)](window-manager-service.md) 을 나누어 띄울지를 전문 지휘하는 무대 총감독.

```mermaid
graph TD
    AppLaunch["Activity / Component 시작 요청"] --> ATMS["ActivityTaskManagerService (ATMS)"]
    ATMS -->|"1. Task / 백스택 계산"| StackMgmt["TaskRecord / ActivityRecord 갱신"]
    ATMS -->|"2. 앱 프로세스 존재 확인"| AMS["ActivityManagerService (AMS)"]
    AMS -->|"3. 프로세스 없으면 Zygote fork"| Zygote["Zygote Socket 요청"]
    AMS -->|"4. oom_score_adj 점수 계산"| LMK["Low Memory Killer (lmkd) 갱신"]
```

---

### 2. AMS 대 ATMS 역할 분담 비교

| 구분 | ActivityManagerService (AMS) | ActivityTaskManagerService (ATMS) |
| :--- | :--- | :--- |
| **주요 책임** | **[프로세스](../../01_system_internals/boot-and-runtime/zygote-runtime/zygote-runtime.md) 수명주기, OOM 점수([LMK](../../01_system_internals/kernel-and-hal/kernel/lmkd-memory-pressure.md)), Memory Trim** | **[Activity](../../02_app_framework/architecture/app-components/activity.md) 수명주기, Task, Recents, Multi-Window** |
| **관련 컴포넌트**| [Service](../../02_app_framework/architecture/app-components/service.md), [BroadcastReceiver](../../02_app_framework/architecture/app-components/broadcast-receiver.md), [ContentProvider](../../02_app_framework/architecture/app-components/content-provider.md) | [Activity 메인 컴포넌트](../../02_app_framework/architecture/app-components/activity.md) |
| **생성 시점** | Android OS 극초기부터 하부 관제 | Android 10(Q) 이상에서 AMS 로부터 아키텍처 분리 |
| **핵심 클래스** | `ProcessRecord`, `OomAdjuster` | `ActivityRecord`, `Task`, `ActivityTaskSupervisor` |

---

### 3. 관측 가능 증거 및 CLI 명령어

`adb shell` 로 현재 AMS 와 ATMS 가 관리 중인 Task 백스택 및 프로세스 상태를 관측할 수 있다:

```bash
# 1. ATMS 가 관리 중인 현재 활성 Activity 백스택 및 Task 덤프
adb shell dumpsys activity activities

# 2. AMS 가 관리 중인 프로세스 LRU 리스트 및 oom_score_adj 덤프
adb shell dumpsys activity processes
```

---

### 4. 연결 문서 (Related Links)

- [system_server 표준 레퍼런스](../../01_system_internals/boot-and-runtime/system-server/system-server.md) - AMS & ATMS 를 호스팅하는 프레임워크 프로세스
- [WindowManagerService (WMS)](window-manager-service.md) - 윈도우 계층 구조 및 레이아웃 관리
- [ServiceManager](service-manager.md) - AMS & ATMS 바인더 핸들 조회
- [Context.getSystemService()](get-system-service.md) - 앱에서 ActivityManager 프록시 습득
- [Low Memory Killer (LMK)](../../01_system_internals/kernel-and-hal/kernel/lmkd-memory-pressure.md) - AMS 가 oom_score_adj 주입하는 메모리 회수기
- [Zygote 와 ART 런타임 심층 계약](../../01_system_internals/boot-and-runtime/zygote-runtime/zygote-runtime.md) - AMS 요청으로 앱 프로세스 fork
- [Binder IPC](../../01_system_internals/ipc-and-process/binder-ipc.md) - 앱과 AMS/ATMS 간 IPC 디스패치
- [Android 4대 앱 컴포넌트](../../02_app_framework/architecture/app-components/android-app-components.md) - Activity, Service, Receiver, Provider
