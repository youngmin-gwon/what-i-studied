---
title: android-connectivity
tags: ["android", "android/system-internals"]
aliases: ["Android connectivity map", "android-connectivity"]
date modified: 2026-08-03 17:24:20 +09:00
date created: 2026-07-31 23:20:00 +09:00
---

## Android 연결성과 네트워크 지도

Android 네트워크는 Wi-Fi, cellular, Ethernet, VPN 같은 transport 를 그대로 앱에 노출하는 구조가 아니다. 앱은 `ConnectivityManager` 가 제공하는 `Network`, `NetworkCapabilities`, `LinkProperties`, 정책 상태를 보고 현재 작업에 맞는 연결성을 판단해야 한다.

이 폴더는 네 계층을 분리해서 다룬다: 앱이 직접 부르는 app API(`ConnectivityManager`, `Network`, `VpnService`, `WifiManager`), 그 상태를 계산하는 framework service(`ConnectivityService`), 실제 routing/DNS/firewall 을 집행하는 native service(`netd`), 그 아래 kernel/HAL(netfilter/eBPF, radio driver). 앱 코드가 바꿀 수 있는 것은 첫 번째 계층뿐이고, 나머지는 `dumpsys connectivity`, `dumpsys netpolicy`, `dumpsys wifi` 같은 관찰 신호로만 접근한다.

### 정본 노트
- [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md) — 읽는 순서, 문제 분류 기준, 비슷한 노트 차이는 여기가 정본이다.

### 판단 기준

Connectivity 노트는 app API 에서 보이는 network 상태와 system service 가 실제로 적용하는 routing, DNS, policy 상태를 분리해 읽는다. 어떤 문제든 먼저 "이건 app API 가 보는 상태 문제인가, system 이 결정한 정책 문제인가"부터 나눈다.

### 경계

연결 성공 여부만 보지 말고 default network, requested network, metered policy, VPN, private DNS, captive portal 상태를 함께 확인한다. system_server 가 ConnectivityService 를 어떻게 띄우고 조율하는지는 이 폴더의 정본이 아니며 [system_server와 ActivityManager 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md) 으로 연결한다.

### 관련 노트

- [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)
- [Android 보안 샌드박스](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/android-app-sandbox-is-uid-and-process-boundary.md)
