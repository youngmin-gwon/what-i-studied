---
title: telephonymanager-permissions-split-into-phone-state-and-phone-numbers
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-04 15:00:00 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## TelephonyManager 권한은 READ_PHONE_STATE와 READ_PHONE_NUMBERS로 세분화된다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [텔레포니 접근 계약](01_inbox/mobile/android/04_system_services/device-capabilities/telephony-contracts/telephony-contracts.md)

### 핵심 정의

`TelephonyManager`가 노출하는 정보는 민감도에 따라 서로 다른 permission으로 나뉜다. 통화 상태(수신/발신 중 여부 등)는 `READ_PHONE_STATE`, 전화번호 자체는 `READ_PHONE_NUMBERS`가 필요하며, IMEI 같은 기기 식별자는 Android 10 이후 일반 서드파티 앱에는 사실상 차단되어 시스템 앱이나 특별 승인된 경우로 제한된다.

### 메커니즘

과거 `READ_PHONE_STATE` 하나로 통화 상태부터 전화번호, 기기 식별자까지 폭넓게 접근할 수 있었으나, 개인정보 보호 강화로 세분화됐다. 앱이 필요한 정보 이상으로 넓은 permission을 요청하면 Play 정책 심사에서 사유 소명을 요구받거나 거부될 수 있다. `getDeviceId()`, `getImei()` 같은 API는 Android 10+ 에서 대부분의 앱에 `null` 반환 또는 `SecurityException`으로 막힌다.

### 판단 기준

- 전화번호 확인 자동화(예: SMS 인증 대체)가 목적이면 `READ_PHONE_NUMBERS` 단독으로 충분한지, 아니면 SMS Retriever API 같은 permission-less 대안이 더 적합한지 먼저 검토한다.
- 기기 식별을 목적으로 IMEI를 시도하지 말고, 앱 고유 식별에는 `Instance ID`나 앱이 생성한 UUID를 사용한다. IMEI 접근은 대부분의 일반 앱 시나리오에서 정당화되지 않는다.
- 통화 상태만 필요하면(예: 통화 중 알림 음소거) `READ_PHONE_STATE`로 충분하며 더 넓은 권한을 요청하지 않는다.

### 경계

- 이 노트는 permission 세분화까지 다룬다. 멀티 SIM 환경에서 어떤 SIM의 정보를 조회할지는 [SubscriptionManager는 멀티 SIM에서 논리적 구독과 물리 슬롯을 분리한다](01_inbox/mobile/android/04_system_services/device-capabilities/telephony-contracts/subscriptionmanager-separates-logical-subscriptions-from-physical-slots.md)가 다룬다.
- 통신사 서명 기반의 특권적 접근(일반 permission 체계 밖)은 [Carrier privilege는 런타임 권한 없이 통신사 서명 인증서로 부여된다](01_inbox/mobile/android/04_system_services/device-capabilities/telephony-contracts/carrier-privilege-is-granted-by-carrier-signed-certificates-not-runtime-permission.md)가 다룬다.

### 관찰 가능한 신호

`adb shell dumpsys package <pkg>`의 runtime permissions에서 `READ_PHONE_STATE`/`READ_PHONE_NUMBERS` grant 여부를 확인한다. 식별자 API가 `null`을 반환하면 permission 거부가 아니라 OS 버전 자체의 정책적 차단인지부터 targetSdkVersion과 함께 확인한다.

### 공식 문서

- https://developer.android.com/reference/android/telephony/TelephonyManager
- https://developer.android.com/training/articles/user-data-ids
