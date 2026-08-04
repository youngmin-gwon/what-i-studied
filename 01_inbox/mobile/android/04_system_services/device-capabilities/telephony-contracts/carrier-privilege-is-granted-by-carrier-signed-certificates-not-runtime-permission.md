---
title: carrier-privilege-is-granted-by-carrier-signed-certificates-not-runtime-permission
tags: ["android", "android/system-services"]
aliases: ["Carrier privilege는 런타임 권한 없이 통신사 서명 인증서로 부여된다"]
date modified: 2026-08-04 15:00:00 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## Carrier privilege는 런타임 권한 없이 통신사 서명 인증서로 부여된다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [텔레포니 접근 계약](./telephony-contracts.md)

### 핵심 정의

통신사(carrier) 앱은 일반적인 런타임 permission 요청 대화상자를 거치지 않고, SIM(UICC)에 저장된 인증서 해시가 앱의 서명 인증서 해시와 일치하는지로 특권(carrier privilege)을 부여받는다. 이 앱은 사용자 승인 없이도 APN 설정 변경, 특정 통신 관련 API 호출 같은 통신사 전용 작업을 수행할 수 있다.

### 메커니즘

SIM 카드는 `ARA-M`/`ARF` 규격에 따라 신뢰할 특정 서명 인증서 해시 목록을 저장한다. `TelephonyManager.hasCarrierPrivileges()`는 현재 앱의 서명이 삽입된 SIM의 신뢰 목록에 있는지 확인한다. 일치하면 시스템은 해당 앱을 사용자 승인 절차 없이 통신사 특권 API 호출 대상으로 인정한다. 이 신뢰는 사용자의 permission 승인이 아니라 SIM 발급 시점에 통신사가 미리 심어둔 데이터에서 나온다.

### 판단 기준

- 통신사가 아닌 일반 앱 개발자는 carrier privilege가 필요한 API(예: 특정 APN 설정 변경, 캐리어 구성 오버라이드)를 사용할 수 없다는 전제를 갖는다. 이는 코드로 우회할 수 있는 문제가 아니라 SIM 발급 주체의 신뢰 관계다.
- 통신사와 협업하는 앱(운영사 자체 앱)을 개발하는 경우, SIM에 서명 해시를 심는 절차는 개발자가 아니라 통신사와의 협의 및 SIM 프로파일링 과정에서 결정된다.
- carrier privilege 여부가 SIM 교체나 eSIM 프로필 전환에 따라 바뀔 수 있다는 점을 상태 확인 로직에 반영한다.

### 경계

- 이 노트는 carrier privilege라는 신뢰 경로 자체를 다룬다. 일반 permission 기반 telephony 조회는 [TelephonyManager 권한은 READ_PHONE_STATE와 READ_PHONE_NUMBERS로 세분화된다](./telephonymanager-permissions-split-into-phone-state-and-phone-numbers.md)가 다룬다.
- 앱 서명 자체의 키 관리, 서명 체계는 `03_packaging_deployment`가 다룬다.

### 관찰 가능한 신호

`TelephonyManager.hasCarrierPrivileges()`를 런타임에 호출해 boolean 결과로 직접 확인할 수 있다. `adb shell dumpsys telephony.registry`에서도 carrier privilege가 부여된 패키지 목록이 나타날 수 있다(OEM/플랫폼 버전에 따라 출력 형식이 다르다).

### 공식 문서

- https://source.android.com/docs/core/connect/uicc
- https://developer.android.com/reference/android/telephony/TelephonyManager#hasCarrierPrivileges()
