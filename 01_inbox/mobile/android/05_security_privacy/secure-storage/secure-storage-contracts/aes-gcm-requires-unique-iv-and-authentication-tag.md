---
title: aes-gcm-requires-unique-iv-and-authentication-tag
tags: []
aliases: []
date modified: 2026-07-31 18:18:28 +09:00
date created: 2026-07-31 17:04:40 +09:00
---

# aes-gcm-requires-unique-iv-and-authentication-tag

## Android AES-GCM 은 IV 와 인증 태그를 함께 관리한다

상위 문서: [보안 저장소 계약](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/secure-storage-contracts.md)
관련 노트: [Android Keystore 키는 비추출성으로 보호한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/android-keystore-protects-keys-by-non-exportability.md), [Android 민감 데이터는 암호화와 키 소유권을 함께 설계한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/sensitive-data-requires-encryption-and-key-ownership.md)


### 핵심 주장

AES-GCM 은 기밀성과 무결성을 함께 제공하는 인증 암호 방식이다.

그러나 키마다 IV 를 재사용하면 보안성이 무너질 수 있으므로, 암호화마다 새 IV 를 생성하고 복호화에 전달해야 한다.

### 저장 형식

하나의 레코드는 최소한 다음 요소를 갖는다.

- 키를 식별할 수 있는 버전 또는 별칭 정보
- 암호화 시 생성한 무작위 IV
- AES-GCM 이 만든 암호문과 인증 태그
- 필요하다면 버전, 스키마, 알고리즘 식별자

IV 는 비밀일 필요가 없으므로 암호문과 함께 저장할 수 있다.

반대로 인증 태그는 암호문 검증에 필요하므로 버리거나 잘라내면 안 된다.

JCA 구현에서는 `doFinal` 결과에 태그가 붙어 반환되는 형태가 일반적이다.

### IV 규칙

- 같은 키로 암호화할 때 IV 는 매번 새로 생성해야 한다.
- `Cipher.init(ENCRYPT_MODE, key)` 가 생성한 IV 를 `cipher.iv` 로 받아 저장한다.
- 복호화 시 저장한 IV 를 `GCMParameterSpec` 으로 다시 전달한다.
- IV 를 고정 상수, 사용자 ID, 타임스탬프만으로 만들지 않는다.
- 난수 생성은 플랫폼의 보안 난수원을 사용한다.

### 인증 태그 규칙

GCM 은 복호화할 때 암호문과 태그를 검증한다.

데이터가 변조되거나 키·IV 가 맞지 않으면 `doFinal` 이 실패해야 한다.

이 실패를 무시하고 일부 평문을 사용해서는 안 된다.

태그 길이는 생성과 복호화에서 일관되게 설정한다.

예시의 `GCMParameterSpec(128, iv)` 는 128 비트 인증 태그를 사용한다는 뜻이다.

### 추가 인증 데이터

레코드 유형이나 사용자 식별자처럼 암호화하지 않지만 변조되어서는 안 되는 값은 AAD 로 인증할 수 있다.

암호화와 복호화에서 동일한 AAD 를 전달해야 검증이 성공한다.

AAD 에 넣은 값도 비밀이 아니므로 별도로 숨겨지지는 않는다.

### 구현 흐름

1. Keystore 에서 AES 키를 얻는다.
2. `AES/GCM/NoPadding` Cipher 를 생성한다.
3. 암호화 모드로 초기화하고 플랫폼이 만든 IV 를 보관한다.
4. 평문을 `doFinal` 로 처리해 암호문과 태그를 저장한다.
5. 복호화 시 IV 와 같은 AAD 를 사용한다.
6. 인증 실패를 데이터 손상 또는 공격 가능성으로 처리한다.

### 주의점

문자열을 바이트로 바꿀 때 문자셋을 명시해 플랫폼 차이를 없앤다.

암호화 결과를 Base64 로 직렬화할 수 있지만, Base64 는 암호화가 아니다.

로그, 예외 메시지, 분석 이벤트에 평문과 암호키를 남기지 않는다.
