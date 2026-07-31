---
title: android-keystore-protects-keys-by-non-exportability
tags: []
aliases: []
date modified: 2026-07-31 18:18:22 +09:00
date created: 2026-07-31 17:04:40 +09:00
---

# android-keystore-protects-keys-by-non-exportability

## Android Keystore 키는 비추출성으로 보호한다

상위 문서: [보안 저장소 계약](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/secure-storage-contracts.md)
관련 노트: [Android AES-GCM은 IV와 인증 태그를 함께 관리한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/aes-gcm-requires-unique-iv-and-authentication-tag.md), [BiometricPrompt는 Keystore 키 사용 권한을 여는 장치다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/biometricprompt-authorizes-keystore-key-use.md)

### 핵심 주장

[Android Keystore](https://developer.android.com/privacy-and-security/keystore) 는 앱이 암호키 원본을 읽어 가는 저장소가 아니다.

키를 보호된 영역에서 생성하고, 허용된 암호 연산만 수행하게 하는 키 사용 경계다.

### 비추출성

- Keystore 에 생성한 키의 원본 바이트는 일반 앱 코드로 내보낼 수 없다.
- 앱은 키 객체를 받아 `Cipher` 같은 API 에 전달하고 연산 결과만 받는다.
- 키를 문자열, `ByteArray`, 환경 변수로 변환해 별도 저장하는 설계는 이 경계를 무너뜨린다.
- 키 별칭(alias)은 키 자체가 아니라 Keystore 항목을 찾기 위한 식별자다.
- 별칭을 숨기는 것만으로는 비밀 보호가 되지 않는다.

### 하드웨어 지원

기기는 지원 범위에 따라 키 연산을 TEE 또는 StrongBox 에서 수행할 수 있다.

TEE 는 신뢰 실행 환경이고, StrongBox 는 별도 보안 하드웨어를 사용하는 더 강한 격리 경로다.

모든 기기가 StrongBox 를 제공하는 것은 아니므로 런타임 지원 여부를 확인해야 한다.

`setIsStrongBoxBacked(true)` 를 무조건 성공한다고 가정하면 키 생성이 실패할 수 있다.

필요한 보안 수준과 호환성 요구를 정한 뒤 지원 기기에서만 StrongBox 를 선택한다.

### KeyMint 와 권한

Android 의 하드웨어 추상화 계층은 키의 목적, 알고리즘, 패딩, 사용자 인증 요구를 적용한다.

앱은 키 생성 시 `PURPOSE_ENCRYPT` 와 `PURPOSE_DECRYPT` 처럼 허용할 목적을 지정한다.

AES-GCM 키라면 GCM 블록 모드와 `NoPadding` 을 함께 지정한다.

키를 만들고 난 뒤에는 이러한 사용 제약을 임의로 완화할 수 없다.

### 생명주기

- 앱 데이터 삭제와 함께 키를 삭제하면 해당 암호문은 복호화할 수 없다.
- 새 기기로 암호문만 옮기면 원래 기기의 Keystore 키가 없어 복구되지 않는다.
- 생체 등록 변경 등 설정에 따라 키가 무효화될 수 있다.
- 키 무효화는 예외 상황이 아니라 마이그레이션과 재인증 흐름에서 처리해야 할 상태다.
- 키 재생성 전에 기존 암호문을 복구할 수 있는지 제품 정책을 결정한다.

### 피해야 할 설계

- APK 안에 AES 키를 상수로 넣는다.
- Keystore 키를 `encoded` 값으로 추출해 서버나 파일에 저장한다.
- 암호문과 키를 같은 일반 파일에 함께 저장한다.
- 기기 보안 기능의 사용 가능 여부를 확인하지 않고 하드웨어 백킹을 단정한다.

### 결론

Keystore 의 장점은 키를 감추는 데만 있지 않다.

키의 소유자를 앱 코드에서 보호된 키 관리 시스템으로 옮기고, 사용 조건을 정책으로 고정하는 데 있다.

앱은 키를 읽는 대신 Keystore 가 허용한 연산을 호출해야 한다.
