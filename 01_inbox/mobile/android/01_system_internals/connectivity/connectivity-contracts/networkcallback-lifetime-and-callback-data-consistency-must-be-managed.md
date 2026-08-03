---
title: networkcallback-lifetime-and-callback-data-consistency-must-be-managed
tags: ["android", "android/system-internals"]
aliases: []
date modified: 2026-08-03 17:24:38 +09:00
date created: 2026-07-31 21:50:22 +09:00
---

## NetworkCallback 은 등록 수명과 콜백 데이터의 일관성을 함께 관리해야 한다

상위 문서: [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

`NetworkCallback` 은 네트워크 상태 변경을 받는 observer 이면서 동시에 시스템 자원을 점유하는 등록 객체다. 등록한 callback 은 앱이 필요로 하는 수명에 맞춰 해제해야 하고, callback 안에서는 전달받은 `NetworkCapabilities` 와 `LinkProperties` 를 우선 사용해야 한다.

### 실무 규칙

- 같은 callback 인스턴스를 동시에 여러 등록에 재사용하지 않는다.
- 화면 수명, service 수명, repository 수명 중 어느 수명에 묶을지 명확히 한다.
- callback 안에서 `getNetworkCapabilities()` 같은 synchronous getter 를 다시 호출하면 race 로 오래된 값 또는 null 을 볼 수 있다.
- Android 는 UID 당 outstanding network request/callback 수를 제한하므로 누수는 실제 예외로 이어질 수 있다.
- Wi-Fi location-sensitive 정보가 필요하면 `FLAG_INCLUDE_LOCATION_INFO` 와 권한 요구를 함께 검토한다.

### 관련 문서

- [Android 상태 관리 정본 지도](01_inbox/mobile/android/02_app_framework/architecture/state-management/android-state-management.md)
- [기본 네트워크와 요청 네트워크는 서로 다른 수명 계약을 가진다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/default-network-and-requested-network-have-different-lifetimes.md)

공식 문서: [ConnectivityManager.NetworkCallback](https://developer.android.com/reference/android/net/ConnectivityManager.NetworkCallback)
