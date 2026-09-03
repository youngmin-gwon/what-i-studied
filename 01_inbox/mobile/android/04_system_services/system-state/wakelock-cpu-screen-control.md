---
title: wakelock-cpu-screen-control
tags: ["android", "android/system-services"]
aliases: ["PowerManager 웨이크락은 화면과 CPU를 분리해서 제어한다"]
date modified: 2026-08-06 14:59:18 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## PowerManager 웨이크락은 화면과 CPU를 분리해서 제어한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../android-system-services-and-device-capabilities.md)
배경 지식: [프로세스 상태와 생명주기](../../../../operating-systems/process-states-lifecycle.md)
관련 지도: [전력 상태 접근 계약](power.md)

### 핵심 정의

**PowerManager.WakeLock**(웨이크락)은 앱이 작업하는 동안 기기의 절전 진입을 제한하는 전원 락이다. 현재 일반 앱의 핵심 선택지는 화면이 꺼져도 CPU 실행을 유지하는 `PARTIAL_WAKE_LOCK`이다. 과거 화면용 `SCREEN_DIM_WAKE_LOCK`/`SCREEN_BRIGHT_WAKE_LOCK`은 API 17에서 deprecated됐으며, 화면 유지에는 View/Window API를 사용한다.

### 메커니즘

wake lock을 획득(`acquire()`)하면 시스템은 해당 종류의 절전 진입을 막는다. `PARTIAL_WAKE_LOCK`만 획득한 상태에서 사용자가 전원 버튼을 눌러 화면을 끄면, 화면은 꺼지지만 CPU는 계속 실행되어 백그라운드 작업(예: 음악 재생, 다운로드)이 이어질 수 있다. wake lock은 참조 카운트를 가질 수 있어 여러 곳에서 acquire해도 마지막 release까지 유지된다.

release를 누락하면 CPU가 계속 깨어 있어 배터리를 소모하며, 이는 앱이 앱 대기(App Standby)나 배터리 최적화 대상으로 분류되는 원인이 되기도 한다.

### 판단 기준

- 화면을 켜둘 필요가 있는지, CPU만 깨어 있으면 되는지를 먼저 구분한다. 대부분의 백그라운드 작업은 `PARTIAL_WAKE_LOCK`으로 충분하다.
- 재생·예약 작업처럼 프레임워크가 수명을 관리할 수 있는 경우에는 미디어 스택이나 WorkManager 등 해당 API의 전력 관리를 우선 검토한다. foreground service라는 사실만으로 CPU wake lock이 자동 보장되지는 않는다.
- `acquire()`에는 timeout을 지정하는 오버로드를 사용해, 코드 경로 오류로 release가 누락돼도 시스템이 강제로 해제하도록 방어한다.

### 최소 안전 보유 범위

매니페스트에 `android.permission.WAKE_LOCK`을 선언하고, 필요한 가장 짧은 구간만 timeout과 `finally`로 감싼다.

```kotlin
val power = context.getSystemService(PowerManager::class.java)
val lock = power.newWakeLock(
    PowerManager.PARTIAL_WAKE_LOCK,
    "com.example.app:upload"
)

lock.acquire(30_000L)
try {
    uploadOneBoundedBatch()
} finally {
    if (lock.isHeld) lock.release()
}
```

timeout은 정상 종료 로직을 대신하지 않는 마지막 안전망이다. 화면만 계속 보이게 하려면 activity/window의 `FLAG_KEEP_SCREEN_ON` 또는 View의 `android:keepScreenOn`을 쓰며, deprecated 화면 wake lock을 새로 도입하지 않는다.

### 경계

- 이 노트는 wake lock이 즉시적으로 화면/CPU를 제어하는 메커니즘까지 다룬다. 배터리 최적화(Doze/App Standby) 예외 목록에 앱을 넣는 것은 별개의 정책이며 [배터리 최적화 예외는 예외 상황을 위한 것이지 기본 설계가 아니다](battery-optimization-exemption.md)가 다룬다.
- 지속적인 백그라운드 작업 실행 수단 자체(FGS vs WorkManager 선택)는 `04_system_services/background-and-notifications/background-work-contracts`가 다룬다.

### 관찰 가능한 신호

획득·해제·timeout 경로를 동일한 태그와 작업 ID로 기록한다. `adb shell dumpsys power`에서 현재 wake lock 태그와 보유 UID를 확인하고, Battery Historian/전력 trace에서 작업 종료 뒤에도 태그가 남는지 본다. 화면 유지 요구라면 화면 off 이후 CPU만 남는지와 activity 종료 시 flag가 사라지는지도 별도로 검증한다.

### 공식 문서

- https://developer.android.com/reference/android/os/PowerManager.WakeLock
- https://developer.android.com/training/scheduling/wakelock

검증일: 2026-08-06. `PARTIAL_WAKE_LOCK`의 CPU 유지 범위, timeout acquire, deprecated 화면 wake lock 대신 `FLAG_KEEP_SCREEN_ON`/`keepScreenOn`을 쓰는 현재 권고를 확인했다.
