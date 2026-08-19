---
title: biometricprompt-couples-authentication-ui-with-key-authorization
tags: ["android", "android/system-services"]
aliases: ["BiometricPrompt는 인증 UI와 키 사용 승인을 함께 처리한다"]
date modified: 2026-08-06 14:59:18 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## BiometricPrompt는 인증 UI와 키 사용 승인을 함께 처리한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [생체 인증/자격 증명 계약](./biometrics-credential.md)

### 핵심 정의

`BiometricPrompt`는 지문/얼굴 인식 같은 생체 인증을 위한 시스템 표준 UI를 띄우는 API다. 단순 인증 결과를 받는 흐름뿐 아니라, **CryptoObject**(`Cipher`/`Signature`/`Mac` 등 암호 연산 객체를 감싸는 래퍼)를 함께 전달해 auth-per-use Keystore 키의 특정 연산을 인증 성공과 결합할 수 있다. Keystore 키가 항상 하드웨어에 저장된다고 가정하지 말고 `KeyInfo.securityLevel`로 확인한다.

### 메커니즘

앱이 CryptoObject 없이 `authenticate()`를 호출하면 인증 결과를 앱 로직의 gate로 사용할 수 있다. 이것이 곧 취약하거나 우회 가능하다는 뜻은 아니다. 반면 timeout 0으로 구성한 auth-per-use Keystore 키는 `CryptoObject`를 전달한 프롬프트로 해당 연산을 승인한다. 일정 시간 동안 재사용하는 time-based 키는 최근 기기 자격 증명 또는 허용된 인증 수단으로 잠금이 해제되며, CryptoObject 없는 프롬프트를 사용할 수 있다. 어떤 흐름을 쓸지는 보호 대상이 암호키 연산인지, 단순 앱 기능 접근인지에 따라 결정한다.

### auth-per-use 호출 흐름

```kotlin
val prompt = BiometricPrompt(activity, mainExecutor, callback)
val promptInfo = BiometricPrompt.PromptInfo.Builder()
    .setTitle("보호된 작업 승인")
    .setAllowedAuthenticators(BIOMETRIC_STRONG)
    .setNegativeButtonText("취소")
    .build()

// cipher는 timeout=0, user-auth-required Keystore 키로 init한 연산이다.
prompt.authenticate(promptInfo, BiometricPrompt.CryptoObject(cipher))
```

성공 콜백에서는 `result.cryptoObject?.cipher`만 사용한다. 인증 전 Cipher를 전역에 저장해 나중에 재사용하거나 UI 성공 boolean만으로 별도 암호 연산을 승인하지 않는다. 사용자 취소와 센서 장애·lockout은 서로 다른 오류 코드로 처리한다.

### 판단 기준

- **CryptoObject가 필수인 경우**: `setUserAuthenticationRequired(true)`와 함께 timeout을 0(auth-per-use)으로 설정한 Keystore 키를 사용할 때. 이 경우 `CryptoObject` 없이 프롬프트를 띄우면 키 연산 시 `UserNotAuthenticatedException`이 발생한다.
- **CryptoObject가 불필요한 경우**: timeout을 0보다 크게(time-based) 설정한 키를 사용하거나, 키 없이 단순 앱 화면 진입(기능 접근 제어)만 제한할 때. 이 때는 `CryptoObject` 없는 `authenticate()` 호출만으로 충분하다.
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

검증일: 2026-08-06. 공식 BiometricPrompt/Keystore 문서에 따라 CryptoObject를 auth-per-use 키 연산용으로 한정하고 실제 호출·실패 흐름을 보강했다.
