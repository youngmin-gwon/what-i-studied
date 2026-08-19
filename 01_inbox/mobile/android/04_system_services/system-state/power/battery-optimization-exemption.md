---
title: battery-optimization-exemption-is-for-exceptions-not-default-design
tags: ["android", "android/system-services"]
aliases: ["배터리 최적화 예외는 예외 상황을 위한 것이지 기본 설계가 아니다"]
date modified: 2026-08-06 14:59:18 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## 배터리 최적화 예외는 예외 상황을 위한 것이지 기본 설계가 아니다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [전력 상태 접근 계약](./power.md)

### 핵심 정의

`PowerManager.isIgnoringBatteryOptimizations()`와 배터리 최적화 설정 인텐트는 앱을 Doze/App Standby 제한에서 **부분적으로** 제외해 달라고 사용자에게 요청·확인하는 경로다. 이 예외는 실시간 통신처럼 핵심 기능이 Doze로 직접 손상되는 소수 사례를 위한 것이며, 일반적인 백그라운드 작업의 기본 해법이 아니다.

### 메커니즘

사용자가 이 예외를 승인하면 앱은 Doze 중 네트워크를 사용하고 partial wake lock을 유지할 수 있다. 하지만 일반 `AlarmManager` 알람 같은 다른 제한은 남고, API 수준에 따라 jobs/sync도 계속 지연될 수 있으므로 "전력 정책 완전 해제"가 아니다. Google Play는 직접 예외 요청을 핵심 기능에 필요한 사례로 제한한다.

### 판단 기준

- 지연 가능한 작업(동기화, 업로드, 정기 갱신)은 예외를 요청하지 말고 WorkManager의 제약 조건과 Doze 유지보수 윈도우를 그대로 활용한다.
- 정말 즉시성이 필요한 작업(수신 전화 유사 알림, 정시 알람)만 예외 요청 대상으로 좁힌다. 이 경우에도 `AlarmManager`의 exact alarm이나 FGS 같은 더 좁은 범위의 메커니즘으로 대체 가능한지 먼저 검토한다.
- 사용자가 예외를 거부할 수 있으므로, 예외가 없는 상태에서도 앱이 허용 가능한 지연 안에서 동작하도록 기본 설계를 먼저 갖춘다.

### 최소 상태 확인과 요청 흐름

대부분의 앱은 특정 앱을 즉시 예외로 넣는 요청 대신 전체 최적화 설정 화면을 열어 사용자가 판단하게 한다. 직접 요청이 정책상 허용되는 앱만 `REQUEST_IGNORE_BATTERY_OPTIMIZATIONS`를 선언하고 package URI가 붙은 직접 요청을 사용한다.

```kotlin
val power = context.getSystemService(PowerManager::class.java)
val packageName = context.packageName

if (!power.isIgnoringBatteryOptimizations(packageName)) {
    context.startActivity(
        Intent(Settings.ACTION_IGNORE_BATTERY_OPTIMIZATION_SETTINGS)
            .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
    )
}

// 사용자가 돌아오면 isIgnoringBatteryOptimizations(packageName)을 다시 읽는다.
```

설정 화면을 열었다는 사실이나 Activity result를 승인으로 간주하지 않는다. 복귀·다음 실행 시 상태를 다시 읽고, 거부·설정 activity 부재·OEM별 화면 차이를 fallback UX로 처리한다.

### 경계

- 이 노트는 배터리 최적화 예외라는 정책적 경로를 다룬다. wake lock으로 CPU를 즉시 깨우는 것은 별개의 메커니즘이며 [PowerManager 웨이크락은 화면과 CPU를 분리해서 제어한다](./wakelock-cpu-screen-control.md)가 다룬다.
- Doze/App Standby의 구체적인 단계별 제한과 백그라운드 실행 수단 선택 전체는 `04_system_services/background-and-notifications/background-work-contracts`가 다룬다.

### 관찰 가능한 신호

앱의 `isIgnoringBatteryOptimizations()` 값과 `adb shell dumpsys deviceidle whitelist`의 예외 목록을 대조한다. `adb shell dumpsys battery unplug` 후 `adb shell dumpsys deviceidle force-idle`로 Doze에 진입시켜 네트워크·partial wake lock은 허용되는지, 일반 알람이나 예약 작업은 여전히 지연되는지를 각각 측정한다.

### 공식 문서

- https://developer.android.com/training/monitoring-device-state/doze-standby
- https://developer.android.com/reference/android/os/PowerManager#isIgnoringBatteryOptimizations(java.lang.String)

검증일: 2026-08-06. 예외 앱은 Doze 중 네트워크와 partial wake lock을 사용할 수 있지만 다른 제한이 남는 "부분 예외"이며, 직접 요청은 Play 정책상 핵심 기능이 영향받는 경우로 제한됨을 확인했다.
