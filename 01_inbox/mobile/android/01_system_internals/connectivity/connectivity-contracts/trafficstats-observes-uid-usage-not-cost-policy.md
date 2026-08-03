---
title: trafficstats-observes-uid-usage-not-cost-policy
tags: ["android", "android/system-internals"]
aliases: []
date modified: 2026-08-03 17:24:41 +09:00
date created: 2026-07-31 21:50:22 +09:00
---

## TrafficStats 는 UID 단위 사용량 관찰이지 비용 정책 결정자가 아니다

상위 문서: [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

`TrafficStats` 는 UID 나 전체 장치의 누적 네트워크 사용량을 관찰하는 API 다. 이 값은 사용량 표시와 진단에는 유용하지만, 앱이 Data Saver 나 metered policy 를 직접 대체해서 판단하는 근거가 아니다.

### 실무 규칙

- `UNSUPPORTED` 반환 가능성을 처리한다.
- UID 단위 값은 여러 process 와 shared UID, system accounting 구현의 영향을 받을 수 있다.
- 사용자에게 과금 위험을 안내하려면 TrafficStats 보다 metered/Data Saver/cellular policy 를 우선 본다.
- 세션별 측정은 앱 내부 tagging 이나 request layer telemetry 와 함께 설계한다.

### 관련 문서

- [Metered와 Data Saver는 백그라운드 네트워크 비용 정책이다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/metered-and-data-saver-are-background-network-cost-policy.md)
- [netd는 framework 요청을 routing, DNS, firewall, tethering 동작으로 집행한다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/netd-enforces-routing-dns-firewall-and-tethering-operations.md)

공식 문서: [TrafficStats](https://developer.android.com/reference/android/net/TrafficStats)
