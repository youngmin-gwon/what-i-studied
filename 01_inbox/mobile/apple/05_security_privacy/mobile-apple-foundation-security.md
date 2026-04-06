---
title: mobile-apple-foundation-security
tags: [apple, apple/security, moc]
aliases: []
date modified: 2026-04-06 18:14:49 +09:00
date created: 2026-04-03 22:15:19 +09:00
---

## [[mobile-security]] > [[mobile-apple-foundation-security]]

### Apple Platform Foundation Security (MOC)

Apple 플랫폼 보안은 하드웨어와 소프트웨어의 긴밀한 결합을 통해 **"기본 거부(Deny by Default)"** 철학을 실현하며, 사용자 프라이버시를 최우선으로 설계되었습니다.

---

#### 🛡️ 핵심 아키텍처 (Core Architecture)

Apple 보안의 근간을 이루는 4 대 핵심 계층입니다.

1. [[apple-sandbox-and-security]]: **Apple Sandbox & Security Diagnosis** - 샌드박스 메커니즘과 앱 무결성 진단.
2. [[apple-security-sandbox]]: **App Sandbox & MAC Internals** - 리소스 접근 격리 및 커널 수준 제어의 상세 동작.
3. [[apple-security-entitlements]]: **Code Signing & Entitlements** - 앱 무결성 및 시스템 기능 권한 증명.
4. [[apple-security-app-attest]]: **App Attest & DeviceCheck** - 서버 측의 앱 무결성 및 기기 신뢰성 검증.
5. [[apple-security-tcc-compliance]]: **TCC & Legal Compliance** - 프라이버시 승인 시스템과 법적 준수 사항.

---

#### 🤖 차세대 보안 트렌드 (Modern Security)

2024-2025 년 기준 Apple 의 최신 보안 기술입니다.

- [[apple-security-pq3]]: **PQ3 Protocol** - iMessage 의 양자 내성 암호화.
- [[apple-security-pcc]]: **Private Cloud Compute** - Apple Intelligence 를 위한 클라우드 AI 프라이버시 모델.
- [[apple-security-swift6-safety]]: **Swift 6 Security** - 컴파일 타임의 메모리 안전성 및 데이터 레이스 차단.

---

#### 🌐 네트워크 및 저장소 (Network & Storage)

- [[network-security-protocols]] - **ATS (App Transport Security)** 및 TLS 통신 보안.
- [[mobile-apple-secure-storage]] - **Keychain & Secure Enclave**를 이용한 데이터 보호.

#### See Also
- [[mobile-security]] (Hub)
- [[mobile-advanced-security-tips]] - 시니어용 RASP 및 안티 포렌식 팁
- [[cross-platform-ai-privacy-comparison]] - AI 에이전트 프라이버시 모델 비교
