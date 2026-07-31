---
title: "네트워크 디버깅은 앱 API 상태와 system network state를 대조한다"
tags: ["android", "android/system-internals"]
---

# 네트워크 디버깅은 앱 API 상태와 system network state를 대조한다

상위 문서: [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

Android 네트워크 문제는 앱 HTTP 오류만 보면 원인을 알기 어렵다. 앱이 본 `NetworkCapabilities`, system default network, DNS/link properties, VPN, Data Saver, captive portal, netd/routing 상태를 같은 시점에서 대조해야 한다.

## 점검 순서

- 앱 로그에서 사용한 `Network`, capability, endpoint, timeout 종류를 기록한다.
- `dumpsys connectivity`, `cmd connectivity`, `dumpsys netpolicy`, `dumpsys wifi`로 system state를 본다.
- DNS 문제는 Private DNS, VPN, captive portal, resolver 로그를 함께 본다.
- 비용 문제는 metered/Data Saver/uid policy와 WorkManager constraint를 확인한다.
- 성능 문제는 재시도 폭주, radio wakeup, payload 크기, compression/cache, server latency를 분리한다.

## 관련 문서

- [디버깅 계약](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/debugging-contracts.md)
- [배터리, 네트워크, 저장소 효율은 리소스 정책이다](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/battery-network-storage-efficiency-is-resource-policy.md)
