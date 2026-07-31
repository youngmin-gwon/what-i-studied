---
title: "ConnectivityService는 네트워크 선택과 정책 적용의 system service다"
tags: ["android", "android/system-internals"]
---

# ConnectivityService는 네트워크 선택과 정책 적용의 system service다

상위 문서: [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

ConnectivityService는 Wi-Fi, cellular, Ethernet, VPN 같은 네트워크를 수집하고 앱별 default network, validation, metered 여부, Data Saver, VPN 적용, user preference를 종합해 라우팅 결정을 내리는 system service다.

## 판단 기준

- 앱은 transport 우선순위를 직접 정하지 않고, 시스템이 선택한 default network와 capability를 관찰한다.
- 특정 요구가 있을 때만 `NetworkRequest`로 별도 네트워크를 요청한다.
- VPN은 실제 물리 network 위에 올라가는 virtual network일 수 있으며 앱의 default network로 보일 수 있다.
- background 제한과 enterprise policy는 같은 물리 연결에서도 앱별 접근 가능성을 바꿀 수 있다.

## 관련 문서

- [system service는 Binder endpoint이자 플랫폼 정책 집행자다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-service-is-binder-endpoint-and-platform-policy-enforcer.md)
- [Network는 특정 연결 인스턴스이고 transport는 그 속성 중 하나다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/network-is-connection-instance-and-transport-is-only-one-capability.md)

공식 문서: [ConnectivityManager](https://developer.android.com/reference/android/net/ConnectivityManager)
