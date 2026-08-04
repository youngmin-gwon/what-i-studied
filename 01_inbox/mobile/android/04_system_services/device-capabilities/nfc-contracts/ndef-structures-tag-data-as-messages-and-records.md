---
title: ndef-structures-tag-data-as-messages-and-records
tags: ["android", "android/system-services"]
aliases: ["NDEF는 태그 데이터를 메시지와 레코드로 구조화한다"]
date modified: 2026-08-04 15:30:00 +09:00
date created: 2026-07-31 17:46:00 +09:00
---

## NDEF는 태그 데이터를 메시지와 레코드로 구조화한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [NFC와 비접촉 기능 계약](./nfc-contracts.md)

### 개념

NDEF는 NFC Data Exchange Format의 약자로 태그 데이터를 구조화한다.
NDEF 메시지는 하나 이상의 NDEF 레코드로 구성된다.
레코드는 TNF, type, id, payload 필드를 가진다.
첫 레코드는 Android가 메시지의 MIME 타입이나 URI를 추론하는 기준이 된다.
따라서 여러 레코드 메시지를 만들 때 첫 레코드의 의미를 명확히 해야 한다.

### 읽기 흐름

1. 장치에서 NFC가 지원되고 켜져 있는지 확인한다.
2. 태그가 발견되면 인텐트에서 Tag 객체를 얻는다.
3. Ndef.get(tag)으로 NDEF 접근 가능 여부를 확인한다.
4. connect 후 ndefMessage를 읽고 close한다.
5. 레코드의 TNF와 타입을 검증한 뒤 payload를 애플리케이션 모델로 변환한다.
예외와 연결 종료를 처리해야 하며, 블로킹 I/O는 메인 스레드에서 수행하지 않는다.

### 디스패치

ACTION_NDEF_DISCOVERED는 NDEF 데이터가 MIME 타입 또는 URI로 매핑될 때 사용된다.
ACTION_TECH_DISCOVERED는 기술 목록을 기준으로 처리할 때 사용된다.
ACTION_TAG_DISCOVERED는 더 일반적인 최후의 처리 경로다.
인텐트 필터를 넓게 잡으면 다른 앱과의 선택 충돌이 늘어날 수 있다.
업무에 필요한 MIME 타입이나 URI 스킴만 선언하는 편이 예측 가능하다.

### 쓰기 흐름

쓰기 전 태그의 isWritable과 maxSize를 확인한다.
기존 메시지를 덮어쓸 수 있는지와 새 메시지 크기를 검증한다.
NdefMessage를 만든 뒤 connect, writeNdefMessage, close 순으로 처리한다.
쓰기 실패가 발생할 수 있으므로 사용자에게 성공을 확정하기 전에 결과를 확인한다.
읽기 전용 태그는 쓰기 시도 자체를 하지 않는다.

### 레코드 선택

URI는 가능하면 Android의 URI 레코드 생성 도우미를 사용한다.
MIME 데이터는 앱이 소유한 타입을 명확히 정하고 payload 버전을 포함할 수 있다.
외부 타입 레코드는 네임스페이스와 타입을 안정적으로 관리해야 한다.
payload를 신뢰하지 말고 길이, 인코딩, 스키마, 버전을 검증한다.
태그에는 비밀값이나 장기 인증 토큰을 평문으로 저장하지 않는다.

### NDEF가 아닌 태그

NDEF로 해석되지 않는 태그는 android.nfc.tech 클래스로 직접 다룰 수 있다.
이 경우 앱이 태그별 원시 프로토콜과 프레이밍을 직접 책임진다.
지원 범위와 실패 동작이 넓어지므로 NDEF로 충분한 요구에는 저수준 API를 피한다.

### 공식 문서

- https://developer.android.com/develop/connectivity/nfc/nfc
- https://developer.android.com/develop/connectivity/nfc/advanced-nfc
