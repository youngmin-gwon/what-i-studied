---
title: "BiometricPrompt는 인증 UI와 키 사용 승인을 함께 처리한다"
tags: ["android", "android/system-services"]
---

# BiometricPrompt는 인증 UI와 키 사용 승인을 함께 처리한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [생체 인증/자격 증명 계약](01_inbox/mobile/android/04_system_services/device-capabilities/biometrics-credential-contracts/biometrics-credential-contracts.md)

## 핵심 정의

`BiometricPrompt`는 지문/얼굴 인식 같은 생체 인증을 위한 시스템 표준 UI를 띄우는 API다. 단순 신원 확인(`authenticate(PromptInfo)`)뿐 아니라, `CryptoObject`(Keystore에 저장된 `Cipher`/`Signature`/`Mac`)를 함께 전달하면 생체 인증 성공이 곧 해당 키 사용 승인으로 이어지는 흐름을 만들 수 있다.

## 메커니즘

앱이 CryptoObject 없이 `authenticate()`를 호출하면 "사용자가 맞다"는 확인만 결과로 받는다. 반면 Keystore에서 `setUserAuthenticationRequired(true)`로 생성한 키의 `Cipher`를 `CryptoObject`로 감싸 전달하면, 생체 인증이 성공해야만 해당 `Cipher`로 암복호화 작업을 실제로 수행할 수 있다. 인증 성공 전에 그 키를 사용하려 하면 시스템이 예외를 던진다. 이 결합 덕분에 "인증 UI만 통과하고 실제로는 키 없이 우회"하는 공격이 어려워진다.

## 판단 기준

- 로컬 데이터 암호화, 앱 잠금처럼 실제 민감 데이터 보호가 목적이면 CryptoObject를 반드시 함께 사용한다. UI 통과 여부만 확인하는 것은 우회에 취약하다.
- 단순히 "이 사람이 기기 소유자가 맞는지" 확인만 필요한 기능(앱 재실행 시 재인증 등)에는 CryptoObject 없는 단순 인증으로 충분하다.
- 생체 정보가 변경되면(지문 추가/삭제 등) 키 무효화 여부(`setInvalidatedByBiometricEnrollment`)를 설계 시점에 결정해야 한다.

## 경계

- 이 노트는 인증 UI와 키 승인의 결합 메커니즘까지 다룬다. 프롬프트를 띄우기 전에 확인해야 하는 기기 지원 여부는 [BiometricManager.canAuthenticate는 실행 전에 확인해야 하는 사전 조건이다](01_inbox/mobile/android/04_system_services/device-capabilities/biometrics-credential-contracts/biometricmanager-canauthenticate-is-a-precondition-check.md)가 다룬다.
- Keystore 키 생성, 하드웨어 보안 모듈(StrongBox/TEE) 세부는 `05_security_privacy/secure-storage`가 다룬다.

## 관찰 가능한 신호

인증 실패/취소/오류는 `AuthenticationCallback`의 `onAuthenticationError`, `onAuthenticationFailed`로 구분되어 전달된다. CryptoObject 없이 성공한 인증으로 보호된 키를 사용하려 하면 `IllegalStateException` 계열 예외가 발생하는지로 결합 여부를 검증할 수 있다.

## 공식 문서

- https://developer.android.com/identity/sign-in/biometric-auth
- https://developer.android.com/reference/androidx/biometric/BiometricPrompt.CryptoObject
