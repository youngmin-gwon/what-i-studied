---
title: "Android NFC는 리더, 태그, 카드 에뮬레이션 모드로 나뉜다"
tags: ["android", "android/system-services"]
---

# Android NFC는 리더, 태그, 카드 에뮬레이션 모드로 나뉜다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [NFC와 비접촉 기능 계약](01_inbox/mobile/android/04_system_services/device-capabilities/nfc-contracts/nfc-contracts.md)

## 핵심 정의

NFC는 가까운 거리에서 장치와 태그가 통신하는 무선 기술이다.
Android NFC는 크게 리더/라이터 모드와 카드 에뮬레이션 모드로 나뉜다.
리더/라이터 모드에서는 휴대전화가 수동 태그를 읽거나 쓴다.
카드 에뮬레이션 모드에서는 휴대전화가 외부 리더에 카드처럼 보인다.

## 세 가지 문제를 분리하기

첫째, 태그를 발견하고 데이터를 해석하는 문제는 태그 디스패치의 영역이다.
둘째, 태그와 원시 바이트를 교환하는 문제는 TagTechnology API의 영역이다.
셋째, 결제 단말과 APDU를 교환하는 문제는 카드 에뮬레이션의 영역이다.
NDEF 태그와 HCE 결제는 모두 NFC를 사용하지만 같은 프로토콜 흐름이 아니다.

## Android API의 위치

NfcAdapter는 장치의 NFC 어댑터와 기본 기능 접근점이다.
Tag는 발견된 태그의 식별자와 지원 기술 목록을 담는다.
Ndef는 NDEF로 포맷된 태그의 메시지 읽기와 쓰기를 제공한다.
NdefFormatable은 포맷 가능한 태그를 NDEF로 초기화할 때 사용한다.
NfcA, NfcB, NfcF, NfcV는 기술별 저수준 통신을 제공한다.
IsoDep는 ISO-DEP 기반 통신에 사용되며 HCE 리더 구현과도 관련된다.

## 시스템이 앱을 선택하는 방식

NDEF 태그를 발견하면 Android는 첫 레코드의 형식과 타입을 해석한다.
해석 결과가 MIME 타입 또는 URI이면 관련 인텐트를 태그 디스패치로 전달한다.
해석할 수 없거나 NDEF가 아니면 기술 기반 디스패치가 사용될 수 있다.
앱은 매니페스트 인텐트 필터로 관심 있는 태그 유형을 선언한다.
화면이 잠금 해제된 상태에서 NFC가 켜져 있어야 일반적인 태그 검색이 가능하다.

## 설계 원칙

NDEF로 표현 가능한 데이터는 NDEF를 우선 사용한다.
지원 태그 기술을 모를 때는 런타임에 NFC 어댑터와 기술 목록을 확인한다.
장치별 안테나 위치, 지원 기술, 태그 품질, 통신 시간 차이를 테스트에 포함한다.
결제는 태그 읽기 UX와 분리해 인증, 토큰, 재시도, 오프라인 정책을 설계한다.
NFC 기능이 선택 사항이면 하드웨어 필수 선언 대신 런타임 대응을 고려한다.

## 공식 문서

- https://developer.android.com/develop/connectivity/nfc
- https://developer.android.com/develop/connectivity/nfc/nfc
- https://developer.android.com/develop/connectivity/nfc/advanced-nfc
