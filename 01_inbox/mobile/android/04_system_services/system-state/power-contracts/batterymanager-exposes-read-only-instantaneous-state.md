---
title: "BatteryManager는 순간 배터리 상태를 관찰 전용으로 노출한다"
tags: ["android", "android/system-services"]
---

# BatteryManager는 순간 배터리 상태를 관찰 전용으로 노출한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [전력 상태 접근 계약](01_inbox/mobile/android/04_system_services/system-state/power-contracts/power-contracts.md)

## 핵심 정의

`BatteryManager`와 `ACTION_BATTERY_CHANGED` 브로드캐스트는 현재 배터리 잔량, 충전 상태, 충전 방식(AC/USB/무선) 등을 읽기 전용으로 제공한다. 앱은 이 정보를 관찰만 할 수 있으며 충전 속도나 충전 여부 자체를 제어할 수 없다.

## 메커니즘

`ACTION_BATTERY_CHANGED`는 sticky 브로드캐스트로 등록되어 있어, 리시버를 등록하는 즉시 마지막 상태를 바로 받을 수 있다(별도의 배터리 변화를 기다릴 필요가 없다). 반면 `ACTION_POWER_CONNECTED`/`ACTION_POWER_DISCONNECTED`는 상태 전환 시점에만 발생하는 일반 브로드캐스트다. `BatteryManager.getIntProperty()`로 현재 잔량 등 개별 값을 직접 조회할 수도 있다.

## 판단 기준

- 배터리 잔량을 UI에 실시간처럼 보이게 하려면 sticky 브로드캐스트로 초기값을 얻고, 이후 변화는 브로드캐스트 수신으로 갱신한다. 폴링은 불필요하다.
- 배터리 부족을 이유로 기능을 제한하려면 `ACTION_BATTERY_LOW`/`ACTION_BATTERY_OKAY`처럼 시스템이 이미 임계값 판단을 마친 브로드캐스트를 우선 활용하고, 임의의 퍼센트 기준을 직접 정의하지 않는다.
- 충전 여부에 따라 무거운 background 작업(백업, 동기화)을 미루는 정책은 WorkManager의 `setRequiresCharging()` 제약으로 표현하는 것이 브로드캐스트를 직접 관찰하는 것보다 안정적이다.

## 경계

- 이 노트는 배터리 상태 관찰까지 다룬다. CPU/화면을 실제로 켜두는 제어는 [PowerManager 웨이크락은 화면과 CPU를 분리해서 제어한다](01_inbox/mobile/android/04_system_services/system-state/power-contracts/wakelock-controls-cpu-and-screen-separately.md)가 다룬다.
- 배터리 소모 자체를 분석하는 프로파일링 도구(Battery Historian 등)는 `06_testing_performance`가 다룬다.

## 관찰 가능한 신호

`adb shell dumpsys battery`로 현재 배터리 레벨, 충전 상태, AC/USB 연결 여부를 즉시 확인할 수 있다. `adb shell dumpsys battery set level <n>`으로 값을 임의로 바꿔 저잔량 UI를 테스트할 수 있다(테스트 후 `reset`으로 되돌려야 한다).

## 공식 문서

- https://developer.android.com/reference/android/os/BatteryManager
- https://developer.android.com/training/monitoring-device-state/battery-monitoring
