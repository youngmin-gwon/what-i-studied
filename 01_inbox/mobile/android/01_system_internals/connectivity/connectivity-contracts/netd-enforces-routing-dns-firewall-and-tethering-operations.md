---
title: netd-enforces-routing-dns-firewall-and-tethering-operations
tags: ["android", "android/system-internals"]
aliases: []
date modified: 2026-08-03 17:24:34 +09:00
date created: 2026-07-31 21:50:22 +09:00
---

## netd 는 framework 요청을 routing, DNS, firewall, tethering 동작으로 집행한다

상위 문서: [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

`netd` 는 Android framework 의 네트워크 정책을 kernel networking 동작으로 집행하는 native daemon 이다. routing table, DNS resolver, firewall rule, bandwidth control, tethering 관련 저수준 작업은 framework service 와 netd 경계를 지나 실행된다.

### 판단 기준

- 앱은 보통 netd 를 직접 다루지 않고 framework API 를 통해 간접 영향을 받는다.
- DNS, routing, firewall 문제는 ConnectivityService state 와 netd state 를 함께 봐야 한다.
- Android 버전에 따라 iptables, nftables, eBPF 기반 accounting 과 filtering 의 구현 세부가 달라질 수 있다.
- OEM 네트워크 stack 변경은 framework API 는 같아도 netd 이하 동작을 바꿀 수 있다.

### 관련 문서

- [system service는 Binder endpoint이자 플랫폼 정책 집행자다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-service-is-binder-endpoint-and-platform-policy-enforcer.md)
- [TrafficStats는 UID 단위 사용량 관찰이지 비용 정책 결정자가 아니다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/trafficstats-observes-uid-usage-not-cost-policy.md)

공식 문서: [Connectivity module](https://source.android.com/docs/core/architecture/modular-system/connectivity)
