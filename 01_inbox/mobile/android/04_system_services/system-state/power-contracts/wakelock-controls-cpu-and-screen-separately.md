---
title: wakelock-controls-cpu-and-screen-separately
tags: ["android", "android/system-services"]
aliases: ["PowerManager 웨이크락은 화면과 CPU를 분리해서 제어한다"]
date modified: 2026-08-04 15:00:00 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## PowerManager 웨이크락은 화면과 CPU를 분리해서 제어한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [전력 상태 접근 계약](./power-contracts.md)

### 핵심 정의

`PowerManager.WakeLock`은 플래그 조합에 따라 CPU만 켜둘지, 화면까지 켜둘지, 화면 밝기까지 유지할지를 선택적으로 제어한다. `PARTIAL_WAKE_LOCK`은 CPU만 깨워두고 화면/키보드는 꺼질 수 있으며, `SCREEN_DIM_WAKE_LOCK`/`SCREEN_BRIGHT_WAKE_LOCK`(API 17에서 deprecated)은 화면까지 켜둔다.

### 메커니즘

wake lock을 획득(`acquire()`)하면 시스템은 해당 종류의 절전 진입을 막는다. `PARTIAL_WAKE_LOCK`만 획득한 상태에서 사용자가 전원 버튼을 눌러 화면을 끄면, 화면은 꺼지지만 CPU는 계속 실행되어 백그라운드 작업(예: 음악 재생, 다운로드)이 이어질 수 있다. wake lock은 참조 카운트를 가질 수 있어 여러 곳에서 acquire해도 마지막 release까지 유지된다.

release를 누락하면 CPU가 계속 깨어 있어 배터리를 소모하며, 이는 앱이 앱 대기(App Standby)나 배터리 최적화 대상으로 분류되는 원인이 되기도 한다.

### 판단 기준

- 화면을 켜둘 필요가 있는지, CPU만 깨어 있으면 되는지를 먼저 구분한다. 대부분의 백그라운드 작업은 `PARTIAL_WAKE_LOCK`으로 충분하다.
- 재생/녹음처럼 지속적인 작업에는 wake lock을 직접 관리하기보다 `MediaSessionCompat`나 foreground service의 관리형 wake lock을 우선 검토한다. 수동 wake lock은 예외 처리 누락 시 release가 안 되는 위험이 크다.
- `acquire()`에는 timeout을 지정하는 오버로드를 사용해, 코드 경로 오류로 release가 누락돼도 시스템이 강제로 해제하도록 방어한다.

### 경계

- 이 노트는 wake lock이 즉시적으로 화면/CPU를 제어하는 메커니즘까지 다룬다. 배터리 최적화(Doze/App Standby) 예외 목록에 앱을 넣는 것은 별개의 정책이며 [배터리 최적화 예외는 예외 상황을 위한 것이지 기본 설계가 아니다](./battery-optimization-exemption-is-for-exceptions-not-default-design.md)가 다룬다.
- 지속적인 백그라운드 작업 실행 수단 자체(FGS vs WorkManager 선택)는 `04_system_services/background-and-notifications/background-work-contracts`가 다룬다.

### 관찰 가능한 신호

`adb shell dumpsys power`에서 현재 보유 중인 wake lock 목록, 보유 시간, 보유 UID를 확인할 수 있다. release 누락으로 인한 장시간 보유는 이 출력에서 비정상적으로 긴 held time으로 나타난다.

### 공식 문서

- https://developer.android.com/reference/android/os/PowerManager.WakeLock
- https://developer.android.com/training/scheduling/wakelock
