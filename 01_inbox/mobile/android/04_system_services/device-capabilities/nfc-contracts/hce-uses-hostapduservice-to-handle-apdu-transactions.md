---
title: hce-uses-hostapduservice-to-handle-apdu-transactions
tags: ["android", "android/system-services"]
aliases: ["HCE는 HostApduService가 APDU 거래를 처리하는 모델이다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 17:46:00 +09:00
---

## HCE는 HostApduService가 APDU 거래를 처리하는 모델이다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [NFC와 비접촉 기능 계약](./nfc-contracts.md)

### HCE의 의미

`HCE`(Host Card Emulation, 물리적 보안 칩 대신 호스트 OS 소프트웨어가 카드 에뮬레이션을 처리하는 기술)는 Secure Element 대신 호스트 CPU가 NFC 카드 에뮬레이션을 처리하는 방식이다.
Android 앱은 HostApduService를 구현해 외부 리더와 APDU를 교환한다.
서비스는 UI 없이 백그라운드에서 시작될 수 있어 교통, 멤버십, 결제에 적합하다.
HCE가 보안 결제 자체를 의미하는 것은 아니며, 애플리케이션 보안은 별도로 필요하다.

### 지원 프로토콜

Android HCE의 필수 대상은 NFC-Forum `ISO-DEP`(ISO/IEC 14443-4 표준 기반의 비접촉 스마트카드 전송 프로토콜) 기반 카드다.
ISO-DEP는 ISO/IEC 14443-4 위에서 동작한다.
`APDU`(Application Protocol Data Unit, 스마트카드 프로토콜에서 헤더와 페이로드로 구성된 명령/응답 데이터 규격) 형식은 ISO/IEC 7816-4 애플리케이션 프로토콜을 따른다.
Nfc-A 위 ISO-DEP 에뮬레이션은 필수이고 Nfc-B는 선택적 지원이다.
리더는 카드 UID를 인증이나 영구 식별자로 사용하면 안 된다.

### 서비스 구현

HostApduService의 processCommandApdu는 명령 APDU를 받고 응답 바이트를 반환한다.
onDeactivated는 링크가 끊기거나 다른 서비스가 선택될 때 정리 작업을 수행한다.
응답은 단말의 시간 제한 안에 반환되어야 하므로 무거운 작업을 경로에서 줄인다.
상태 머신으로 SELECT, 인증, 데이터 조회, 완료 응답을 명시한다.
알 수 없는 명령에는 프로토콜에 맞는 오류 상태를 반환한다.

### 관찰 가능한 신호

`adb shell dumpsys nfc`로 등록된 HCE 서비스 목록, AID 라우팅 테이블, 현재 선택된 서비스를 확인할 수 있다. `onDeactivated(int reason)`은 `DEACTIVATION_LINK_LOSS`(태그가 리더에서 물리적으로 이탈)와 `DEACTIVATION_DESELECTED`(다른 AID/서비스가 선택됨)를 구분해 전달하므로, 두 값을 로그에서 분리해 기록하면 거래 중단 원인을 재현할 수 있다.

### AID 라우팅

`AID`(Application Identifier, ISO/IEC 7816-4에 정의된 스마트카드 애플리케이션 고유 식별자 코드)는 리더가 카드 애플리케이션을 선택하기 위한 Application ID다.
HCE 서비스 메타데이터에 AID 그룹과 AID 필터를 선언한다.
결제용 서비스는 payment 카테고리를 사용해 지갑 앱으로 식별될 수 있다.
기존 결제 인프라와 연동하면 해당 네트워크가 요구하는 AID를 사용해야 한다.
서로 다른 앱이 같은 AID를 선언하면 기본 선택과 라우팅 정책을 점검한다.

### 보안 경계

Android 시스템만 NFC 서비스에 바인딩할 수 있도록 서비스 권한이 보호된다.
하지만 서비스가 반환하는 카드 데이터의 출처와 유효성은 앱이 책임진다.
토큰, 키, 사용자 상태는 앱 샌드박스와 적절한 키 관리로 보호한다.
APDU 입력은 길이, 명령 코드, 상태 전이를 검증한다.
리더가 UID에 의존하지 않도록 설계하고 실제 인증은 암호 프로토콜로 수행한다.

### 공식 문서

- https://developer.android.com/develop/connectivity/nfc/hce
- https://developer.android.com/reference/android/nfc/cardemulation/HostApduService
