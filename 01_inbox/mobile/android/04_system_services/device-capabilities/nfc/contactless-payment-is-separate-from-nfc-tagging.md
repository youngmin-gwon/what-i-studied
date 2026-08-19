---
title: contactless-payment-is-separate-from-nfc-tagging
tags: ["android", "android/system-services"]
aliases: ["비접촉 결제는 NFC 태깅과 별도 엔지니어링 문제다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 17:46:00 +09:00
---

## 비접촉 결제는 NFC 태깅과 별도 엔지니어링 문제다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [NFC와 비접촉 기능 계약](./nfc.md)

### 결제와 태깅의 차이

NDEF 태깅은 URI, MIME, 애플리케이션 데이터를 읽고 쓰는 흐름이다.
비접촉 결제는 리더가 카드 애플리케이션을 선택하고 APDU를 교환하는 흐름이다.
따라서 태그 읽기 코드를 확장한다고 결제 기능이 완성되지 않는다.
결제는 HCE, `Secure Element`(기기 내부에 위치하여 암호화 키와 결제 자격 증명을 물리적으로 안전하게 보호하는 전용 하드웨어 보안 칩), 결제 네트워크 규격의 조합을 별도로 설계한다.

### 구현 전 확인

기기에 NFC 하드웨어와 필요한 카드 에뮬레이션 기능이 있는지 확인한다.
HCE 기능 필수 여부는 uses-feature와 제품의 핵심 경로를 기준으로 결정한다.
기본 지갑 역할, payment AID, 화면 잠금 정책을 제품 요구와 대조한다.
사용할 리더가 ISO-DEP와 요구 APDU를 지원하는지 테스트 장비로 확인한다.

### 거래 상태

거래 시작, 리더 선택, 인증, 데이터 교환, 승인, 종료를 명시적인 상태로 둔다.
각 상태에 진입할 수 있는 APDU와 반환할 상태 워드를 문서화한다.
onDeactivated가 호출되면 진행 중 상태와 임시 데이터를 안전하게 정리한다.
네트워크 지연이 NFC 시간 제한을 넘지 않도록 사전 토큰화나 캐시를 고려한다.
캐시된 결제 자격은 재사용, 만료, 폐기 정책을 가져야 한다.

### 보안

NFC 통신이 짧은 거리라는 사실만으로 도청과 릴레이 위험이 사라지지 않는다.
민감한 자격 증명은 평문 APDU나 NDEF payload에 넣지 않는다.
앱 샌드박스, Android Keystore, 서버 측 토큰 검증을 역할에 맞게 사용한다.
서비스 입력은 신뢰하지 않고 길이, 순서, 인증 상태, 재전송을 검증한다.
거래 로그에는 원본 PAN이나 비밀 키 대신 추적 가능한 비민감 식별자를 남긴다.

### 기기 호환성

NFC 안테나 위치와 감도, 화면 및 잠금 상태, 제조사 구현이 기기마다 다르다.
여러 제조사와 OS 버전에서 탭 위치, 성공률, 응답 시간, 중단 복구를 측정한다.
리더 종류, 카드 시뮬레이터, 실제 POS를 나눠 테스트한다.
Observe Mode를 사용하는 경우 폴링 프레임과 실제 APDU를 각각 수집한다.

### 관찰 가능한 신호

`adb shell dumpsys nfc`의 카드 에뮬레이션 섹션에서 등록된 AID 라우팅 테이블과 현재 기본으로 선택된 payment 서비스를 확인할 수 있다. 거래가 중단되는 시점은 `HostApduService.onDeactivated(int reason)`에 전달되는 `DEACTIVATION_LINK_LOSS`(리더에서 태그가 물리적으로 이탈)와 `DEACTIVATION_DESELECTED`(다른 AID/서비스로 전환)를 구분해 로그로 남기면, 태깅 실패와 서비스 선택 충돌을 서로 다른 원인으로 재현할 수 있다.

### 운영 기준

성공만이 아니라 실패 원인, 타임아웃, 취소, 서비스 선택 충돌을 관찰한다.
결제 실패 시 사용자가 재시도할 수 있는 명확한 경로를 제공한다.
공식 Android API와 대상 API 수준의 변경점을 릴리스마다 다시 확인한다.
문서에 없는 미래 기능이나 마케팅 주장은 구현 요구 사항으로 사용하지 않는다.

### 공식 문서

- https://developer.android.com/develop/connectivity/nfc
- https://developer.android.com/develop/connectivity/nfc/hce
- https://developer.android.com/develop/connectivity/nfc/advanced-nfc
