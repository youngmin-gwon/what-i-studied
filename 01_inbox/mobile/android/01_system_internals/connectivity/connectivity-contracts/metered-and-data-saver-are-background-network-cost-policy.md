---
title: metered-and-data-saver-are-background-network-cost-policy
tags: ["android", "android/system-internals"]
aliases: []
date modified: 2026-08-03 17:24:33 +09:00
date created: 2026-07-31 21:50:22 +09:00
---

## Metered 와 Data Saver 는 백그라운드 네트워크 비용 정책이다

상위 문서: [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

Metered network 와 Data Saver 는 단순히 Wi-Fi 인지 cellular 인지의 문제가 아니다. 사용자의 요금제, 네트워크 정책, 앱 whitelist, foreground/background 상태에 따라 백그라운드 데이터 사용 가능성과 권장 동작이 달라진다.

### 실무 규칙

- 큰 sync, preload, media download 는 `NET_CAPABILITY_NOT_METERED` 또는 사용자 동의를 기준으로 제한한다.
- Data Saver 가 켜졌다면 background transfer 를 줄이고 foreground 사용자 요청만 우선 처리한다.
- `restrictBackgroundStatus` 는 disabled, enabled, whitelisted 상태를 구분한다.
- 네트워크 비용 정책은 앱 UX 와 WorkManager constraint 에도 반영한다.

### 관련 문서

- [배터리, 네트워크, 저장소 효율은 리소스 정책이다](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/battery-network-storage-efficiency-is-resource-policy.md)
- [백그라운드 작업 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)

공식 문서: [ConnectivityManager.getRestrictBackgroundStatus](https://developer.android.com/reference/android/net/ConnectivityManager#getRestrictBackgroundStatus())
