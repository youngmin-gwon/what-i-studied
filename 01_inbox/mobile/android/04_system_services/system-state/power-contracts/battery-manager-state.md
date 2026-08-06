---
title: batterymanager-exposes-read-only-instantaneous-state
tags: ["android", "android/system-services"]
aliases: ["BatteryManager는 순간 배터리 상태를 관찰 전용으로 노출한다"]
date modified: 2026-08-06 14:59:18 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## BatteryManager는 순간 배터리 상태를 관찰 전용으로 노출한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [전력 상태 접근 계약](./power-contracts.md)

### 핵심 정의

`BatteryManager`와 `ACTION_BATTERY_CHANGED` 브로드캐스트는 현재 배터리 잔량, 충전 상태, 충전 방식(AC/USB/무선) 등을 읽기 전용으로 제공한다. 앱은 이 정보를 관찰만 할 수 있으며 충전 속도나 충전 여부 자체를 제어할 수 없다.

### 메커니즘

`ACTION_BATTERY_CHANGED`는 sticky 브로드캐스트로 등록되어 있어, 리시버를 등록하는 즉시 마지막 상태를 바로 받을 수 있다(별도의 배터리 변화를 기다릴 필요가 없다). 반면 `ACTION_POWER_CONNECTED`/`ACTION_POWER_DISCONNECTED`는 상태 전환 시점에만 발생하는 일반 브로드캐스트다. `BatteryManager.getIntProperty()`로 현재 잔량 등 개별 값을 직접 조회할 수도 있다.

### 판단 기준

- 배터리 잔량을 UI에 실시간처럼 보이게 하려면 sticky 브로드캐스트로 초기값을 얻고, 이후 변화는 브로드캐스트 수신으로 갱신한다. 폴링은 불필요하다.
- 배터리 부족을 이유로 기능을 제한하려면 `ACTION_BATTERY_LOW`/`ACTION_BATTERY_OKAY`처럼 시스템이 이미 임계값 판단을 마친 브로드캐스트를 우선 활용하고, 임의의 퍼센트 기준을 직접 정의하지 않는다.
- 충전 여부에 따라 무거운 background 작업(백업, 동기화)을 미루는 정책은 WorkManager의 `setRequiresCharging()` 제약으로 표현하는 것이 브로드캐스트를 직접 관찰하는 것보다 안정적이다.

### 최소 안전 스냅샷

sticky 브로드캐스트의 마지막 값을 nullable 스냅샷으로 읽고, 잔량과 scale이 유효할 때만 비율을 계산한다.

```kotlin
val battery = context.registerReceiver(
    null,
    IntentFilter(Intent.ACTION_BATTERY_CHANGED)
) ?: return BatterySnapshot.Unavailable

val level = battery.getIntExtra(BatteryManager.EXTRA_LEVEL, -1)
val scale = battery.getIntExtra(BatteryManager.EXTRA_SCALE, -1)
val status = battery.getIntExtra(BatteryManager.EXTRA_STATUS, -1)
val plugged = battery.getIntExtra(BatteryManager.EXTRA_PLUGGED, 0)

val percent = if (level >= 0 && scale > 0) {
    level * 100f / scale
} else null

return BatterySnapshot(percent, status, plugged)
```

`status == BATTERY_STATUS_UNKNOWN`, null Intent, 음수 level, 0 이하 scale을 실제 0%와 구분한다. 장기 작업 예약은 이 순간 스냅샷을 근거로 직접 루프를 돌리지 말고 WorkManager의 charging/battery-not-low 제약에 맡긴다.

### 경계

- 이 노트는 배터리 상태 관찰까지 다룬다. CPU/화면을 실제로 켜두는 제어는 [PowerManager 웨이크락은 화면과 CPU를 분리해서 제어한다](./wakelock-cpu-screen-control.md)가 다룬다.
- 배터리 소모 자체를 분석하는 프로파일링 도구(Battery Historian 등)는 `06_testing_performance`가 다룬다.

### 관찰 가능한 신호

앱이 파싱한 level/scale/status/plugged 원값과 계산된 percent를 함께 기록하고 `adb shell dumpsys battery`와 대조한다. `adb shell dumpsys battery set level <n>` 및 충전 source 설정으로 UI를 재현하되, 테스트 후 반드시 `adb shell dumpsys battery reset`으로 실제 하드웨어 보고로 되돌린다.

### 공식 문서

- https://developer.android.com/reference/android/os/BatteryManager
- https://developer.android.com/training/monitoring-device-state/battery-monitoring

검증일: 2026-08-06. `ACTION_BATTERY_CHANGED`가 초기 상태를 얻는 sticky broadcast이며, 잔량 비율은 `EXTRA_LEVEL`과 `EXTRA_SCALE`을 함께 사용해야 한다는 계약을 확인했다.
