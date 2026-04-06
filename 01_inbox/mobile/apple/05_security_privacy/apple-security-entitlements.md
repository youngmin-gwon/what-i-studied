---
title: apple-security-entitlements
tags: [apple, apple/security, code-signing, entitlements]
aliases: []
date modified: 2026-04-06 18:13:54 +09:00
date created: 2026-04-05 17:07:50 +09:00
---

## [[mobile-security]] > [[apple-security-entitlements]]

### Code Signing & Entitlements

앱이 사용자의 리소스를 요청할 수 있는 권리가 있음을 증명하고, 전체 시스템의 무결성을 유지하는 핵심 메커니즘입니다.

---

#### 🛡️ Code Signing (코드 서명)

앱 바이너리에 대한 불변의 인장입니다.

- **통합성(Integrity)**: 바이너리가 수정되면 서명이 깨지고 OS 는 이를 거치게 됩니다.
- **출처 증명**: Apple 이나 개발자 본인임을 증명하여 악성코드 배포를 억제합니다.

---

#### 🎟️ Entitlements (권한)

앱의 주민등록증 뒤에 붙은 "특수 면허" 같은 것입니다.

- 하드웨어나 시스템 API(Push, iCloud, Apple Pay)를 쓰려면 Apple 이 발급한 `Provisioning Profile` 에 해당 권한이 명시되어 있어야 합니다.
- **Xcode 타겟 설정**: Capabilities 탭에서 활성화하지 않으면 런타임 에러가 발생합니다.

---

#### 🛠️ 하드웨어 기반 보안 (Secure Enclave)

Apple 기기에서 암호화 키는 **Secure Enclave** 내부에서만 생성 및 관리됩니다.

- 앱은 키 자체에 접근할 수 없으며, 시스템을 통해 서명이나 복호화 결과만 요청합니다.
- 이는 앱이 해킹되어 메모리가 유출되더라도 키 정보는 안전함을 보장합니다.

#### 연관 문서

- [[apple-security-sandbox]] - 격리 계층
- [[apple-security-app-attest]] - 앱 무결성 증명
- [[apple-keychain-biometrics]] - 키체인 및 생체 인증
