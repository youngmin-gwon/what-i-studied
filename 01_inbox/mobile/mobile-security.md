---
title: mobile-security
tags: [hub, mobile, moc, security]
aliases: []
date modified: 2026-04-06 18:22:49 +09:00
date created: 2026-04-05 14:48:40 +09:00
---

## [[mobile-security]]

### Mobile Security Knowledge Base Hub

2026 년 최신 모바일 플랫폼(Android & iOS)의 보안 아키텍처, 취약점 진단, 그리고 정보보안기사 실무 가이드 및 AI 에이전트 연동 전략을 모은 메인 인덱스입니다.

---

#### 📱 플랫폼별 보안 아키텍처 (Platform Security)

각 플랫폼의 핵심 보안 메커니즘인 샌드박싱, 권한 시스템, 커널 레벨 보안을 심층 분석합니다.

- **Android Ecosystem**:
	- [[android-foundations]] - 안드로이드 하이브리드 보안 모델 개요
	- [[android-security-sandbox]] - UID 기반 앱 샌드박싱 상세
	- [[android-security-permissions]] - 런타임 권한, AppOps 및 프라이버시 투명성
	- [[android-security-selinux]] - MAC 강제적 접근 통제 메커니즘
- **Apple Ecosystem**:
	- [[apple-foundations]] - 애플의 "기본 거부(Default Deny)" 보안 철학
	- [[mobile-apple-foundation-security]] - Apple 보안 아키텍처 (MOC)
	- [[apple-security-sandbox]] - App Sandbox & MAC 프로필
	- [[apple-security-entitlements]] - Code Signing & 하드웨어 기반 권한 증명
	- [[apple-security-app-attest]] - App Attest 를 통한 앱 무결성 검증
	- [[apple-security-tcc-compliance]] - TCC 프레임워크 및 프라이버시 컴플라이언스

---

#### 🔐 보안 저장소 및 데이터 보호 (Secure Storage)

민감한 데이터와 생체 인증을 안전하게 구현하는 하드웨어 기반 보안 기술입니다.

- [[android-storage-systems]] - Keystore, Scoped Storage & BiometricPrompt
- [[mobile-apple-secure-storage]] - Keychain, Secure Enclave, Passkeys & Data Protection

---

#### 🚀 최신 보안 트렌드 & AI (2024-2026 Trends)

양자 내성 암호화, 공급망 보안, 클라우드 AI 프라이버시 등 최신 기술 스택을 분석합니다.

- **Modern Threats & Trends**:
	- [[mobile-dev-security-checkpoints]] - **개발자를 위한 핵심 보안 체크포인트** (전체 단계 필수)
	- [[apple-security-pq3]] - iMessage 의 양자 내성 암호 프로토콜
	- [[apple-security-pcc]] - Apple Intelligence 를 위한 Private Cloud Compute
	- [[apple-security-swift6-safety]] - Swift 6 의 컴파일 타임 동시성 및 메모리 안전성
- **AI & Automation**:
	- [[android-appfunctions-and-ai-agents]] - AppFunctions 프레임워크와 에이전틱 보안
	- [[cross-platform-ai-privacy-comparison]] - Gemini Nano vs Apple PCC 프라이버시 모델 비교

---

#### 🛡️ 보안 엔지니어링 및 진단 (Engineering & Compliance)

보안 실무자와 개발자를 위한 취약점 점검표, 무결성 검증 및 법적 거버넌스 가이드입니다.

- [[android-security-play-integrity]] - **Play Integrity API** 실무 구현
- [[android-security-practices]] - **Frida/Drozer** 진단 대응 및 국내외 컴플라이언스
- [[mobile-vulnerability-check]] - OWASP Mobile Top 10 (2024 반영) 및 점검 가이드
- [[mobile-advanced-security-tips]] - RASP, Anti-RE, 메모리 보안 및 Zero Trust

---

#### 📚 기반 기술 및 사후 조치 (General & Incident Response)

모바일 보안의 토대가 되는 기반 지식과 사고 대응 기법입니다.

- [[cryptography-basics]] - 모바일 암호화의 기초
- [[network-security-protocols]] - 안전한 통신 인프라 (ATS/TLS)
- [[digital-forensics]] - 모바일 이미지 획득 및 분석 실무
- [[mobile-incident-response-2025]] - **최신 침해 사고 대응 가이드** (Zero-Click, AI-Phishing)

#### See Also

- [[mobile-security]] (This Hub)
- [[android-foundations]]
- [[apple-foundations]]
