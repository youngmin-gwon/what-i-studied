---
title: biometric-manager-preconditions
tags: ["android", "android/system-services"]
aliases: ["BiometricManager.canAuthenticate는 실행 전에 확인해야 하는 사전 조건이다"]
date modified: 2026-08-06 14:59:18 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## BiometricManager.canAuthenticate는 실행 전에 확인해야 하는 사전 조건이다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [생체 인증/자격 증명 계약](./biometrics-credential.md)

### 핵심 정의

`BiometricManager.canAuthenticate(authenticators)`는 시스템 인증 UI인 **BiometricPrompt**(지문·얼굴 등 생체 인증 대화상자)를 실제로 띄우기 전에, 기기가 요청한 인증 강도(`BIOMETRIC_STRONG`, `BIOMETRIC_WEAK`, `DEVICE_CREDENTIAL`)를 지원하는지, 사용자가 생체 정보를 등록했는지를 미리 확인하는 API다. 이 확인 없이 바로 `authenticate()`를 호출하면 하드웨어가 없거나 등록된 생체 정보가 없는 기기에서 예상치 못한 실패로 이어진다.

### 메커니즘

`canAuthenticate()`는 `BIOMETRIC_SUCCESS`, `BIOMETRIC_ERROR_NO_HARDWARE`, `BIOMETRIC_ERROR_HW_UNAVAILABLE`, `BIOMETRIC_ERROR_NONE_ENROLLED`, `BIOMETRIC_ERROR_SECURITY_UPDATE_REQUIRED` 등을 반환한다. 각 결과는 앱이 취해야 할 다른 대응을 요구한다. 예를 들어 `NONE_ENROLLED`는 하드웨어는 있지만 사용자가 지문/얼굴을 등록하지 않은 상태이므로, 설정 화면으로 유도하는 UX가 적절하다.

인증 강도 비트마스크(**Authenticators**: 요구되는 보안 수준으로 `BIOMETRIC_STRONG`은 암호화 키 해제용 강한 생체 인증, `BIOMETRIC_WEAK`는 미인증 시도가 쉬운 약한 생체 인증, `DEVICE_CREDENTIAL`은 기기 PIN/패턴/비밀번호) 조합에 따라 결과가 달라질 수 있다. `BIOMETRIC_STRONG`만 요청하면 얼굴 인식처럼 약한 등급으로 분류된 방식은 지원하지 않는다는 결과가 나올 수 있다.

### 최소 안전 호출 흐름

```kotlin
val authenticators = BIOMETRIC_STRONG or DEVICE_CREDENTIAL
when (BiometricManager.from(context).canAuthenticate(authenticators)) {
    BiometricManager.BIOMETRIC_SUCCESS -> showAuthenticateAction()
    BiometricManager.BIOMETRIC_ERROR_NONE_ENROLLED -> showEnrollmentHelp()
    BiometricManager.BIOMETRIC_ERROR_HW_UNAVAILABLE -> showRetryLater()
    BiometricManager.BIOMETRIC_ERROR_NO_HARDWARE,
    BiometricManager.BIOMETRIC_ERROR_SECURITY_UPDATE_REQUIRED,
    BiometricManager.BIOMETRIC_ERROR_UNSUPPORTED -> showNonBiometricFallback()
    else -> showNonBiometricFallback()
}
```

앱은 `USE_BIOMETRIC`을 선언하고, 사전 검사와 실제 `authenticate()` 사이에 상태가 바뀔 수 있으므로 프롬프트의 `onAuthenticationError()`도 처리한다. 성공 코드는 다음 호출의 성공 보장이 아니라 현재 capability snapshot이다.

### 판단 기준

- CryptoObject와 결합해 민감한 키를 보호하려면 `BIOMETRIC_STRONG`을 요구한다. `BIOMETRIC_WEAK`는 키 인증 승인 용도로 사용할 수 없는 경우가 있다.
- `NONE_ENROLLED` 결과에서는 프롬프트를 억지로 띄우지 말고, 생체 등록 설정 화면으로 안내하는 명시적 UX를 제공한다.
- 기기 PIN/패턴/비밀번호로도 승인할 수 있게 하려면 `DEVICE_CREDENTIAL`을 인증자 옵션에 포함할지 결정한다.

### 경계

- 이 노트는 실행 전 사전 조건 확인까지 다룬다. 인증 성공 후 키 사용 승인 메커니즘은 [BiometricPrompt는 인증 UI와 키 사용 승인을 함께 처리한다](biometric-prompt-key-auth.md)가 다룬다.
- 로그인 자격 증명 자체의 통합(비밀번호, 패스키)은 [CredentialManager는 비밀번호/패스키/연동 로그인을 하나의 API로 통합한다](credential-manager-unification.md)가 다룬다.

### 관찰 가능한 신호

`canAuthenticate()`의 반환 코드를 로그로 남겨 QA 단계에서 하드웨어 부재/미등록 상태를 구분해 재현할 수 있다. 에뮬레이터는 기본적으로 생체 하드웨어가 없어 `BIOMETRIC_ERROR_NO_HARDWARE`가 반환되므로, 실기기 테스트가 필요하다.

### 공식 문서

- https://developer.android.com/reference/androidx/biometric/BiometricManager

검증일: 2026-08-06. AndroidX BiometricManager의 결과 코드와 인증자 조합을 기준으로 호출 흐름을 보강했다.
