---
title: battery-optimization-exemption-is-for-exceptions-not-default-design
tags: ["android", "android/system-services"]
aliases: ["배터리 최적화 예외는 예외 상황을 위한 것이지 기본 설계가 아니다"]
date modified: 2026-08-04 15:00:00 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## 배터리 최적화 예외는 예외 상황을 위한 것이지 기본 설계가 아니다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [전력 상태 접근 계약](./power-contracts.md)

### 핵심 정의

`PowerManager.isIgnoringBatteryOptimizations()`와 `ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS` 인텐트는 앱을 Doze/App Standby의 CPU·네트워크 제한 대상에서 제외해 달라고 사용자에게 요청하는 경로다. 이 예외는 실시간 통신, 알람 앱처럼 정확한 시점에 반드시 깨어나야 하는 소수 사례를 위한 것이며, 일반적인 백그라운드 작업의 기본 해법이 아니다.

### 메커니즘

사용자가 이 예외를 승인하면 앱은 Doze의 유지보수 윈도우를 기다리지 않고 네트워크 접근과 wake lock을 상대적으로 자유롭게 사용할 수 있다. 그러나 Google Play는 이 권한 요청을 정당한 사유(예: VoIP, 예정된 알람) 없이 사용하는 것을 정책으로 제한하며, 심사 과정에서 사용 목적 소명을 요구할 수 있다.

### 판단 기준

- 지연 가능한 작업(동기화, 업로드, 정기 갱신)은 예외를 요청하지 말고 WorkManager의 제약 조건과 Doze 유지보수 윈도우를 그대로 활용한다.
- 정말 즉시성이 필요한 작업(수신 전화 유사 알림, 정시 알람)만 예외 요청 대상으로 좁힌다. 이 경우에도 `AlarmManager`의 exact alarm이나 FGS 같은 더 좁은 범위의 메커니즘으로 대체 가능한지 먼저 검토한다.
- 사용자가 예외를 거부할 수 있으므로, 예외가 없는 상태에서도 앱이 허용 가능한 지연 안에서 동작하도록 기본 설계를 먼저 갖춘다.

### 경계

- 이 노트는 배터리 최적화 예외라는 정책적 경로를 다룬다. wake lock으로 CPU를 즉시 깨우는 것은 별개의 메커니즘이며 [PowerManager 웨이크락은 화면과 CPU를 분리해서 제어한다](./wakelock-controls-cpu-and-screen-separately.md)가 다룬다.
- Doze/App Standby의 구체적인 단계별 제한과 백그라운드 실행 수단 선택 전체는 `04_system_services/background-and-notifications/background-work-contracts`가 다룬다.

### 관찰 가능한 신호

`adb shell dumpsys deviceidle whitelist`로 배터리 최적화 예외 목록에 포함된 패키지를 확인할 수 있다. `adb shell dumpsys battery unplug` 후 `adb shell dumpsys deviceidle force-idle`로 Doze 상태를 강제 진입시켜 예외 여부에 따른 동작 차이를 재현할 수 있다.

### 공식 문서

- https://developer.android.com/training/monitoring-device-state/doze-standby
- https://developer.android.com/reference/android/os/PowerManager#isIgnoringBatteryOptimizations(java.lang.String)
