---
title: android-activity-manager-and-system-services
tags: [android, android/ams, android/system-services]
aliases: []
date modified: 2025-12-16 20:28:32 +09:00
date created: 2025-12-16 15:24:09 +09:00
---

## ActivityManager & System Services android android/system-services android/ams

앱의 생명주기와 화면 전환을 돌보는 주인공은 ActivityManagerService(AMS) 와 ActivityTaskManagerService(ATMS) 다. 낯선 용어는 [[android-glossary]] 에서 확인한다.

### 왜 중요한가
- 어떤 앱이 살아 있고 우선순위가 높은지 정한다.
- 화면 이동, 창 쌓기, 멀티 윈도우, 최근 앱 등을 관리한다.
- 시스템 메모리가 부족할 때 어떤 앱을 먼저 닫을지 판단한다.

### 앱 생명주기
- Activity 는 시작→보임→포커스→정지→종료 단계를 돈다.
- Task/Back stack 은 사용자가 뒤로가기를 눌렀을 때 돌아갈 화면 순서를 담는다.
- 백그라운드에서 멋대로 시작하는 것을 막아 배터리와 보안을 지킨다.

### 프로세스 관리
- 프로세스마다 "중요도" 점수를 매긴다 (앞에 보이는 앱이 가장 중요).
- [[android-glossary#lmkd|LMKD]] 가 점수가 낮은 프로세스부터 닫아 메모리를 확보한다.
- freezer/compaction 같은 기능으로 백그라운드 프로세스를 잠시 얼리거나 눌러 메모리를 줄인다.

### 브로드캐스트와 작업 예약
- BroadcastReceiver 는 짧게 처리하고, 길면 [[android-glossary#workmanager|WorkManager/JobScheduler]] 에 맡긴다.
- JobScheduler 는 "충전 중일 때만", "와이파이일 때만" 같은 조건을 걸 수 있다.
- AlarmManager 는 정확 알람을 제한해 배터리를 지킨다.

### 창과 입력
- WindowManager 는 화면 레이어와 회전을 다룬다. SurfaceFlinger 와 연결되어 실제로 그린다.
- InputDispatcher 가 포커스 창으로 터치/키 이벤트를 보낸다. 오래 막히면 [[android-glossary#anr|ANR]].

### 패키지/설치
- PackageManager 가 앱을 스캔하고 권한을 기록한다.
- 설치 후 [[android-glossary#dex|dexopt]] 로 실행 속도를 조정한다.

### 네트워크·위치
- ConnectivityService 가 어떤 네트워크를 쓸지 결정하고, Private DNS/VPN 정책을 적용한다.
- Location 서비스는 백그라운드 위치를 제한해 프라이버시를 지킨다.

### 안정성 장치
- system_server watchdog 이 멈춘 스레드를 감시한다.
- 반복 크래시나 부팅 실패가 이어지면 Rescue Party 가 설정을 초기화해 복구를 시도한다.

### 디버깅
- `adb shell dumpsys activity`/`cmd activity` 로 상태를 본다.
- [[android-glossary#bugreport|Bugreport]] 에 task/메모리/ANR 정보가 들어 있다.

### 더 보기

[[android-security-and-sandboxing]]: 권한/보안 정책.

[[android-performance-and-debug]]: ANR/성능 추적.

[[android-evolution-history]]: 백그라운드 제한 변화.
