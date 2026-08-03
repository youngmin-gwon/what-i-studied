---
title: biometricprompt-authorizes-keystore-key-use
tags: []
aliases: []
date modified: 2026-08-03 18:14:27 +09:00
date created: 2026-07-31 17:04:40 +09:00
---

## BiometricPrompt 는 Keystore 키 사용을 인가한다

### BiometricPrompt 는 Keystore 키 사용 권한을 여는 장치다

상위 문서: [보안 저장소 계약](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/secure-storage-contracts.md)

관련 노트: [Android Keystore 키는 비추출성으로 보호한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/android-keystore-protects-keys-by-non-exportability.md)

#### 핵심 주장

[BiometricPrompt](https://developer.android.com/reference/androidx/biometric/BiometricPrompt) 는 단순히 화면 진입을 허용하는 UI 가 아니다.

Keystore 키에 사용자 인증 조건을 설정하면, 인증 성공 뒤에만 키 연산을 수행하도록 연결할 수 있다.

#### 인증과 키 사용의 차이

앱이 BiometricPrompt 의 성공 콜백을 받았다는 사실만으로 모든 비밀 데이터를 복호화할 수 있게 만들면 안 된다.

중요한 것은 키 생성 시 사용자 인증을 키의 사용 조건으로 묶는 것이다.

인증 성공 뒤 반환된 `Cipher` 를 사용하거나, 인증으로 해제된 Keystore 키를 사용한다.

이렇게 해야 인증 결과와 실제 암호 연산 사이의 연결이 생긴다.

#### 인증 등급

- `BIOMETRIC_STRONG` 은 보안 강도가 높은 생체 인증 클래스다.
- `BIOMETRIC_WEAK` 은 더 낮은 등급이며 고위험 키 사용 조건으로 적합하지 않을 수 있다.
- `DEVICE_CREDENTIAL` 을 허용하면 기기 PIN, 패턴, 비밀번호가 대체 인증 수단이 될 수 있다.
- 허용할 인증자의 조합은 데이터의 위험도와 사용자 경험을 함께 보고 정한다.

#### 키 생성 정책

키에 사용자 인증을 요구할 때는 인증 유효 시간과 생체 등록 변경 시 동작을 명시한다.

짧은 인증 유효 시간은 보안을 높이지만 반복 인증을 늘린다.

새 지문이나 얼굴을 등록했을 때 키를 무효화하는 정책은 기존 사용자의 재인증 흐름과 함께 설계한다.

키가 무효화되면 암호문을 조용히 삭제하지 말고 사용자에게 재로그인이나 복구 절차를 제공한다.

#### 일반 흐름

1. 사용자가 보호된 기능을 요청한다.
2. `BiometricManager` 로 지원 가능한 인증자를 확인한다.
3. 키 사용에 필요한 `Cipher` 를 준비한다.
4. `BiometricPrompt` 에 암호화 객체를 연결해 인증을 요청한다.
5. 성공 콜백에서 해당 Cipher 로 복호화 또는 서명을 수행한다.
6. 실패, 취소, 잠금 상태를 각각 구분해 처리한다.

#### 설계 주의점

생체 정보 자체를 앱이 저장하거나 처리하는 것이 아니라 시스템 인증 결과를 사용한다.

인증 성공 콜백만 별도 플래그에 저장해 나중에 키를 쓰게 하는 방식은 권한의 범위를 넓힌다.

화면이 백그라운드로 가거나 인증 요청이 취소되면 작업을 중단한다.

인증을 우회하는 테스트용 플래그가 출시 빌드에 남지 않도록 한다.

#### 적합한 보호 대상

- 장기 액세스 토큰 복호화
- 개인 키를 이용한 서명
- 결제나 계정 변경처럼 재인증이 필요한 작업

단순한 앱 진입 화면에는 서버 세션 정책이나 일반 인증 흐름이 더 적합할 수 있다.
