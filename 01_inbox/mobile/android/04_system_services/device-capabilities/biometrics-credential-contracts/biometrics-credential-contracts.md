---
title: biometrics-credential-contracts
tags: ["android", "android/system-services"]
aliases: ["생체 인증/자격 증명 계약"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## 생체 인증/자격 증명 계약

이 지도는 생체 인증 표준 UI를 제공하고 키 해제를 담당하는 **BiometricPrompt**, 프롬프트 표시 전 기기의 하드웨어 상태를 확인하는 사전 검증 API인 **BiometricManager**, 그리고 비밀번호·패스키·SSO 로그인을 통합 시트로 다루는 **CredentialManager**라는 세 핵심 계약을 분리한다. 실제 물리 키 저장 및 암호화 알고리즘 자체는 다루지 않는다.

### 읽는 순서

1. [BiometricPrompt는 인증 UI와 키 사용 승인을 함께 처리한다](./biometricprompt-couples-authentication-ui-with-key-authorization.md)에서 인증과 crypto 객체의 관계를 본다.
2. [BiometricManager.canAuthenticate는 실행 전에 확인해야 하는 사전 조건이다](./biometricmanager-canauthenticate-is-a-precondition-check.md)에서 프롬프트를 띄우기 전 실패를 막는 법을 본다.
3. [CredentialManager는 비밀번호/패스키/연동 로그인을 하나의 API로 통합한다](./credentialmanager-unifies-password-passkey-and-federated-sign-in.md)에서 로그인 흐름 통합 모델을 본다.

### 문제 분류

| 증상 | 먼저 확인할 경계 |
| --- | --- |
| 생체 인증 버튼이 있는데 프롬프트가 안 뜸 | `canAuthenticate()` 사전 확인을 건너뛰었는지, 등록된 생체 정보가 있는지 |
| 인증은 성공했는데 암호화 작업이 실패 | crypto 객체 바인딩과 키 무효화(생체 정보 변경) 여부 |
| 로그인 UI에 패스키 옵션이 안 보임 | CredentialManager 통합 여부, 서버 측 패스키 지원 |

### 책임 경계

- 생체 인증은 "사용자가 맞다는 것을 확인"하는 계층이고, 실제 암호화 키 보호는 `05_security_privacy/secure-storage`(Keystore)가 담당한다. BiometricPrompt는 이 둘을 연결하는 다리다.
- CredentialManager는 여러 로그인 수단을 통합하는 UX 계층이며, 서버 측 인증 로직 자체를 대체하지 않는다.

### 노트 목록

- [BiometricPrompt는 인증 UI와 키 사용 승인을 함께 처리한다](./biometricprompt-couples-authentication-ui-with-key-authorization.md)
- [BiometricManager.canAuthenticate는 실행 전에 확인해야 하는 사전 조건이다](./biometricmanager-canauthenticate-is-a-precondition-check.md)
- [CredentialManager는 비밀번호/패스키/연동 로그인을 하나의 API로 통합한다](./credentialmanager-unifies-password-passkey-and-federated-sign-in.md)

검증일: 2026-08-03. [BiometricPrompt 문서](https://developer.android.com/identity/sign-in/biometric-auth)와 [CredentialManager 문서](https://developer.android.com/identity/sign-in/credential-manager)를 기준으로 확인했다.
