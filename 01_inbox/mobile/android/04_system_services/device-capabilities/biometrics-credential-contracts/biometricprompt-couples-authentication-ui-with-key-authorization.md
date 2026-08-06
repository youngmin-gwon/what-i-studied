---
title: biometricprompt-couples-authentication-ui-with-key-authorization
tags: ["android", "android/system-services"]
aliases: ["BiometricPrompt는 인증 UI와 키 사용 승인을 함께 처리한다"]
date modified: 2026-08-06 14:48:27 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## BiometricPrompt는 인증 UI와 키 사용 승인을 함께 처리한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [생체 인증/자격 증명 계약](./biometrics-credential-contracts.md)

### 핵심 정의

`BiometricPrompt`는 지문/얼굴 인식 같은 생체 인증을 위한 시스템 표준 UI를 띄우는 API다. 단순 인증 결과를 받는 흐름뿐 아니라, **CryptoObject**(`Cipher`/`Signature`/`Mac` 등 암호 연산 객체를 감싸는 래퍼)를 함께 전달해 auth-per-use Keystore 키의 특정 연산을 인증 성공과 결합할 수 있다. Keystore 키가 항상 하드웨어에 저장된다고 가정하지 말고 `KeyInfo.securityLevel`로 확인한다.

### 메커니즘

앱이 CryptoObject 없이 `authenticate()`를 호출하면 인증 결과를 앱 로직의 gate로 사용할 수 있다. 이것이 곧 취약하거나 우회 가능하다는 뜻은 아니다. 반면 timeout 0으로 구성한 auth-per-use Keystore 키는 `CryptoObject`를 전달한 프롬프트로 해당 연산을 승인한다. 일정 시간 동안 재사용하는 time-based 키는 최근 기기 자격 증명 또는 허용된 인증 수단으로 잠금이 해제되며, CryptoObject 없는 프롬프트를 사용할 수 있다. 어떤 흐름을 쓸지는 보호 대상이 암호키 연산인지, 단순 앱 기능 접근인지에 따라 결정한다.

### 판단 기준

- 복호화·서명처럼 특정 auth-per-use 키 연산을 인증과 원자적으로 결합해야 하면 CryptoObject를 사용한다.
- 단순 앱 기능 접근 제어 또는 time-based 키 사용에는 CryptoObject 없는 인증이 올바를 수 있다. 인증 결과를 클라이언트의 유일한 서버 권한 검사로 재사용하지는 않는다.
- `DEVICE_CREDENTIAL` fallback이 필요한 time-based 키 흐름은 CryptoObject를 전달할 수 없는 구성도 있으므로 키의 `setUserAuthenticationParameters()`와 `setAllowedAuthenticators()` 조합을 함께 설계한다.
- 생체 정보가 변경되면(지문 추가/삭제 등) 키 무효화 여부(`setInvalidatedByBiometricEnrollment`)를 설계 시점에 결정해야 한다.

### 경계

- 이 노트는 인증 UI와 키 승인의 결합 메커니즘까지 다룬다. 프롬프트를 띄우기 전에 확인해야 하는 기기 지원 여부는 [BiometricManager.canAuthenticate는 실행 전에 확인해야 하는 사전 조건이다](./biometricmanager-canauthenticate-is-a-precondition-check.md)가 다룬다.
- Keystore 키 생성, 하드웨어 보안 모듈(StrongBox/TEE) 세부는 `05_security_privacy/secure-storage`가 다룬다.

### 관찰 가능한 신호

인증 실패/취소/오류는 `AuthenticationCallback`의 `onAuthenticationError`, `onAuthenticationFailed`로 구분되어 전달된다. 인증이 필요한 키를 정책 밖에서 사용하면 `UserNotAuthenticatedException`이 발생할 수 있으며, 생체 등록 변경·키 무효화는 별도의 예외 경로로 테스트한다.

### 공식 문서

- https://developer.android.com/identity/sign-in/biometric-auth
- https://developer.android.com/reference/androidx/biometric/BiometricPrompt.CryptoObject

검증일: 2026-08-06. 공식 BiometricPrompt/Keystore 문서에 따라 CryptoObject를 auth-per-use 키 연산용으로 한정하고 time-based 키와 단순 인증 흐름을 구분했다.
