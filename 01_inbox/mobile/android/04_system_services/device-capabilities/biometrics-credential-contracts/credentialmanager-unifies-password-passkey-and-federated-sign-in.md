---
title: credentialmanager-unifies-password-passkey-and-federated-sign-in
tags: ["android", "android/system-services"]
aliases: ["CredentialManager는 비밀번호/패스키/연동 로그인을 하나의 API로 통합한다"]
date modified: 2026-08-04 15:30:00 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## CredentialManager는 비밀번호/패스키/연동 로그인을 하나의 API로 통합한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [생체 인증/자격 증명 계약](./biometrics-credential-contracts.md)

### 핵심 정의

`CredentialManager`(Jetpack Credentials)는 저장된 비밀번호, 패스키(FIDO2/WebAuthn 기반 생체 인증 로그인), Google 계정 같은 연동 로그인(federated sign-in)을 앱이 각각 다른 API로 따로 다루지 않고 하나의 요청/응답 흐름으로 통합한 API다. 사용자는 하나의 시스템 로그인 시트에서 어떤 방식으로 로그인할지 선택한다.

### 메커니즘

앱은 `CredentialManager.getCredential()`을 호출하면서 지원하려는 자격 증명 옵션들(`GetPasswordOption`, `GetPublicKeyCredentialOption`(패스키), `GetGoogleIdOption` 등)을 함께 전달한다. 시스템은 기기에 저장된 자격 증명(비밀번호 관리자, 패스키 등)을 조회해 사용자에게 선택 UI로 보여주고, 선택된 방식에 따라 인증을 수행한 뒤 앱에 결과를 반환한다. 패스키는 기기의 생체 인증(BiometricPrompt와 유사한 흐름)으로 개인 키 사용을 승인하는 방식으로 동작하며, 서버는 공개 키 기반 서명을 검증한다.

### 판단 기준

- 신규 로그인 플로우를 설계할 때 비밀번호 전용 흐름 대신 패스키를 1차 옵션으로 제공하는 것을 우선 검토한다. 패스키는 피싱에 강하고 사용자 마찰이 적다.
- 기존 비밀번호 로그인 사용자를 위한 하위 호환 경로(비밀번호 옵션)를 CredentialManager 흐름에서 제거하지 않고 함께 등록한다.
- 서버 측에서 패스키(WebAuthn) 등록/검증을 지원하지 않는다면 클라이언트에서 패스키 옵션을 노출해도 실제로 사용할 수 없다는 점을 백엔드 로드맵과 맞춰 확인한다.

### 경계

- 이 노트는 로그인 자격 증명 통합 API까지 다룬다. 생체 인증 자체의 UI/키 결합 메커니즘은 [BiometricPrompt는 인증 UI와 키 사용 승인을 함께 처리한다](./biometricprompt-couples-authentication-ui-with-key-authorization.md)가 다룬다.
- 서버 측 WebAuthn 검증 로직이나 OAuth/OIDC 프로토콜 세부는 이 지도의 범위 밖이다.

### 관찰 가능한 신호

`getCredential()` 실패는 `GetCredentialException`의 하위 타입(사용자 취소, 자격 증명 없음, 지원되지 않는 옵션 등)으로 구분된다. 시스템 로그인 시트가 뜨지 않으면 요청한 옵션 조합과 기기에 실제로 등록된 자격 증명 유형을 먼저 대조한다.

### 공식 문서

- https://developer.android.com/identity/sign-in/credential-manager
- https://developer.android.com/identity/sign-in/passkeys
