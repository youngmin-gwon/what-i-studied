---
title: "Android 연결성과 네트워크 지도"
tags: ["android", "android/system-internals"]
---

# Android 연결성과 네트워크 지도

Android 네트워크는 Wi-Fi, cellular, Ethernet, VPN 같은 transport를 그대로 앱에 노출하는 구조가 아니다. 앱은 `ConnectivityManager`가 제공하는 `Network`, `NetworkCapabilities`, `LinkProperties`, 정책 상태를 보고 현재 작업에 맞는 연결성을 판단해야 한다.

## 정본 노트
- [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

## 판단 기준

Connectivity 노트는 app API에서 보이는 network 상태와 system service가 실제로 적용하는 routing, DNS, policy 상태를 분리해 읽는다.

## 경계

연결 성공 여부만 보지 말고 default network, requested network, metered policy, VPN, private DNS, captive portal 상태를 함께 확인한다.
