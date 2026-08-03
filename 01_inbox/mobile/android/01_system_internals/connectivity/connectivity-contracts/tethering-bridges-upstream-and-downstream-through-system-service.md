---
title: "테더링은 개인 hotspot 기능이 아니라 upstream과 downstream을 잇는 system service다"
tags: ["android", "android/system-internals"]
---

# 테더링은 개인 hotspot 기능이 아니라 upstream과 downstream을 잇는 system service다

상위 문서: [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

Tethering은 cellular, Ethernet, Wi-Fi 같은 upstream 연결을 Wi-Fi hotspot, USB, Bluetooth 같은 downstream으로 공유하는 system service 기능이다. 앱 기능이라기보다 carrier policy, device policy, permission, system UI가 함께 제어하는 플랫폼 기능이다.

## 판단 기준

- 일반 앱은 임의로 tethering을 켜고 NAT/firewall을 구성할 수 있다고 가정하면 안 된다.
- hotspot availability는 carrier, device owner, user setting, hardware capability의 영향을 받는다.
- tethering 디버깅은 upstream 선택, downstream interface, DHCP, DNS forwarding, firewall/NAT rule을 나눠 본다.
- local-only hotspot은 인터넷 공유 tethering과 구분한다.

## 관련 문서

- [Wi-Fi API는 스캔, 제안, 요청, 로컬 연결을 분리한다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/wifi-apis-separate-scan-suggestion-request-and-local-connectivity.md)
- [netd는 framework 요청을 routing, DNS, firewall, tethering 동작으로 집행한다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/netd-enforces-routing-dns-firewall-and-tethering-operations.md)

공식 문서: [TetheringManager](https://developer.android.com/reference/android/net/TetheringManager)
