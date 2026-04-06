---
title: apple-security-pcc
tags: [ai, apple, apple/security, cloud, pcc]
aliases: []
date modified: 2026-04-06 18:14:08 +09:00
date created: 2026-04-05 17:08:24 +09:00
---

## [[mobile-security]] > [[apple-security-pcc]]

### PCC: Private Cloud Compute

**Apple Intelligence**는 개인 기기 내에서 처리 가능한 작업은 기기에서 수행하고, 복잡한 작업은 클라우드로 위임합니다. 이때 서버에서의 사용자 데이터 프라이버시를 극한으로 보호하기 위한 기술이 **Private Cloud Compute (PCC)**입니다.

---

#### 🛡️ 설계 원칙: "Stateless Cloud"

1. **상태 유지 불가 (Stateless)**: 서버는 작업을 완료한 즉시 사용자 데이터를 삭제해야 하며, 장기 보관이 불가능합니다.
2. **데이터 접근 차단**: Apple 운영자나 외부 관리자가 사용자 데이터에 접근할 수 없도록 하드웨어 수준에서 차단합니다.
3. **신뢰할 수 있는 하드웨어**: 전용 Apple Silicon 기반 서버를 사용하며, 기존의 가상화된 클라우드 환경보다 높은 물리적 보안을 제공합니다.

---

#### ⚙️ 동작 메커니즘

- **검증 가능한 투명성 (Verifiable Transparency)**: 독립적인 보안 연구자가 PCC 서버의 소프트웨어가 선언된 대로 동작하는지, 사용자 데이터가 노출되지 않는지 공개적으로 검증할 수 있도록 설계되었습니다.
- **TLS 암호화**: 기기와 PCC 서버 간의 통신은 강력하게 암호화되어 있으며, Apple 조차 중간에서 이를 가로챌 수 없습니다.
- **개인정보 식별 불가**: 서버는 작업을 처리하지만, 대상이 누구인지 식별할 수 있는 정보를 수집하지 않습니다.

---

#### 🚀 개발자 및 사용자에게 갖는 의미

- **AI 와 프라이버시의 결합**: 클라우드 AI 의 강력한 성능과 기기 내 AI 의 강력한 프라이버시를 동시에 누릴 수 있는 유일한 모델입니다.

#### 연관 문서

- [[cryptography-basics]] - 암호학 기초
- [[mobile-security]] - 모바일 보안 허브
- [[cross-platform-ai-privacy-comparison]] - Gemini Nano vs Apple PCC 프라이버시 모델 심층 분석
