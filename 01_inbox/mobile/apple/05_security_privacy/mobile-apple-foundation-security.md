---
title: mobile-apple-foundation-security
tags: [apple, apple/security, moc]
aliases: ["Apple 보안 정본 지도는 하드웨어 신뢰 근원에서 서명·샌드박스·사용자 동의까지의 계층으로 읽는다", "apple-security-privacy", "Apple Security Foundation"]
date modified: 2026-04-06 18:14:49 +09:00
date created: 2026-04-03 22:15:19 +09:00
---

## Apple 보안 정본 지도는 하드웨어 신뢰 근원에서 서명·샌드박스·사용자 동의까지의 계층으로 읽는다

Apple 플랫폼 보안은 하드웨어와 소프트웨어의 긴밀한 결합을 통해 **"기본 거부(Deny by Default)"** 철학을 실현하며, 사용자 프라이버시를 최우선으로 설계되었습니다.

---

### 🛡️ 핵심 아키텍처 (Core Architecture)

Apple 보안의 근간을 이루는 4 대 핵심 계층입니다.

1. [apple-sandbox-and-security](apple-sandbox-and-security.md): **App Sandbox, MAC, 그리고 런타임 진단** - 커널이 강제하는 격리와 그 위의 탈옥/디버거 탐지.
2. [apple-security-entitlements](apple-security-entitlements.md): **Code Signing & Entitlements** - 서명에 봉인되는 권한 명세.
3. [apple-security-app-attest](apple-security-app-attest.md): **App Attest & DeviceCheck** - 서버 측의 앱 무결성 및 기기 신뢰성 검증.
4. [apple-privacy-and-tcc-details](apple-privacy-and-tcc-details.md): **TCC & Privacy Manifests** - 런타임 사용자 동의와 심사 시점 선언.
5. [apple-keychain-biometrics](apple-keychain-biometrics.md): **Keychain & Secure Enclave** - 자격 증명의 하드웨어 보호.

---

### 🤖 차세대 보안 트렌드 (Modern Security)

2024-2025 년 기준 Apple 의 최신 보안 기술입니다.

- [apple-security-pq3](apple-security-pq3.md): **PQ3 Protocol** - iMessage 의 양자 내성 암호화.
- [apple-security-pcc](apple-security-pcc.md): **Private Cloud Compute** - Apple Intelligence 를 위한 클라우드 AI 프라이버시 모델.
- [apple-security-swift6-safety](apple-security-swift6-safety.md): **Swift 6 Security** - 컴파일 타임의 메모리 안전성 및 데이터 레이스 차단.

---

### 🌐 네트워크 및 저장소 (Network & Storage)

- [network-security-protocols](../../../security/protocols/network-security-protocols.md) - **ATS (App Transport Security)** 및 TLS 통신 보안.
- [mobile-apple-secure-storage](mobile-apple-secure-storage.md) - Keychain CRUD, Passkeys, LocalAuthentication 실무 구현.

### See Also
- [mobile-security](../../mobile-security.md) (Hub)
- [mobile-advanced-security-tips](../../cross-platform/mobile-advanced-security-tips.md) - 시니어용 RASP 및 안티 포렌식 팁
- [cross-platform-ai-privacy-comparison](../../cross-platform/cross-platform-ai-privacy-comparison.md) - AI 에이전트 프라이버시 모델 비교
