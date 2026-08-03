---
title: "전력 상태 접근 계약"
tags: ["android", "android/system-services"]
---

# 전력 상태 접근 계약

이 지도는 앱이 전력 상태를 관찰하고 제어하는 지점을 wake lock, 배터리 상태 관찰, background 실행 제한과의 경계로 나눈다.

## 읽는 순서

1. [PowerManager 웨이크락은 화면과 CPU를 분리해서 제어한다](01_inbox/mobile/android/04_system_services/system-state/power-contracts/wakelock-controls-cpu-and-screen-separately.md)에서 어떤 wake lock 종류가 무엇을 켜두는지 본다.
2. [BatteryManager는 순간 배터리 상태를 관찰 전용으로 노출한다](01_inbox/mobile/android/04_system_services/system-state/power-contracts/batterymanager-exposes-read-only-instantaneous-state.md)에서 배터리 정보 조회와 제어의 경계를 본다.
3. [배터리 최적화 예외는 예외 상황을 위한 것이지 기본 설계가 아니다](01_inbox/mobile/android/04_system_services/system-state/power-contracts/battery-optimization-exemption-is-for-exceptions-not-default-design.md)에서 Doze/App Standby와의 관계를 정리한다.

## 문제 분류

| 증상 | 먼저 확인할 경계 |
| --- | --- |
| 작업 중 화면/CPU가 꺼짐 | 적절한 wake lock을 획득했는지, release 타이밍이 맞는지 |
| wake lock을 잡았는데도 배터리 최적화로 작업이 지연됨 | wake lock과 Doze 예외는 별개라는 점 |
| 배터리 잔량 UI가 부정확 | BatteryManager 브로드캐스트 수신 주기와 캐시 타이밍 |
| 사용자가 배터리 최적화 제외를 계속 요구받음 | 정말 예외가 필요한 기능인지, WorkManager/FGS로 대체 가능한지 |

## 책임 경계

- wake lock은 "화면/CPU를 깨워둔다"는 즉시적 제어이고, 배터리 최적화 예외는 "Doze/App Standby 제한에서 앱을 뺀다"는 정책적 예외다. 서로 다른 계층이며 하나가 다른 하나를 대체하지 않는다.
- 배터리 상태 조회(BatteryManager)는 읽기 전용이며 앱이 충전 정책을 제어할 수는 없다.
- 백그라운드 작업의 실행 수단 선택(WorkManager, FGS 등) 자체는 이 지도가 아니라 `04_system_services/background-and-notifications/background-work-contracts`가 다룬다.

## 노트 목록

- [PowerManager 웨이크락은 화면과 CPU를 분리해서 제어한다](01_inbox/mobile/android/04_system_services/system-state/power-contracts/wakelock-controls-cpu-and-screen-separately.md)
- [BatteryManager는 순간 배터리 상태를 관찰 전용으로 노출한다](01_inbox/mobile/android/04_system_services/system-state/power-contracts/batterymanager-exposes-read-only-instantaneous-state.md)
- [배터리 최적화 예외는 예외 상황을 위한 것이지 기본 설계가 아니다](01_inbox/mobile/android/04_system_services/system-state/power-contracts/battery-optimization-exemption-is-for-exceptions-not-default-design.md)

검증일: 2026-08-03. [PowerManager 문서](https://developer.android.com/reference/android/os/PowerManager)와 [배터리 최적화 가이드](https://developer.android.com/training/monitoring-device-state/doze-standby)를 기준으로 확인했다.
