---
title: mobile-dev-security-checkpoints
tags: [checklist, development, mobile, security]
aliases: []
date modified: 2026-04-06 18:22:06 +09:00
date created: 2026-04-05 20:00:00 +09:00
---

## [[mobile-security]] > [[mobile-dev-security-checkpoints]]

### Mobile App Security: Critical Developer Checkpoints

본 문서는 모바일 앱 개발 과정에서 설계 및 구현 단계에서 **반드시 고려해야 할 핵심 보안 취약점**과 그에 따른 방어 전략을 정리한 실무 가이드입니다.

---

#### 🛠️ 1. 설계 단계 (Design Phase)

앱 아키텍처 수립 시 고려해야 할 "Security by Design" 원칙입니다.

- **최소 권한의 원칙 (Principle of Least Privilege)**:
    - 앱이 동작하는 데 반드시 필요한 권한만 요청하세요.
    - Android 14/15 의 **부분 사진 허용(Partial Photo Access)** 과 같은 세분화된 권한 모델을 적극 활용하세요.
- **신뢰 경계 설정 (Trust Boundaries)**:
    - 기기 외부(API, Deeplink, SD Card)에서 들어오는 모든 데이터는 **신뢰할 수 없음(Untrusted)** 으로 간주하고 검증 로직을 타야 합니다.
- **공급망 보안 (Supply Chain Security)**:
    - 외부 라이브러리/SDK 선정 시 보안 취약점 이력을 확인하세요.
    - **SBOM(Software Bill of Materials)** 을 생성하여 종속성 전반의 보안 상태를 관리하세요.

---

#### 💻 2. 구현 단계 (Implementation Phase)

코드 작성 시 흔히 발생하는 취약점과 방지 기법입니다.

##### **A. 데이터 보호 (Data Protection)**
- **민감 정보 하드코딩 금지**: API Keys, Secret Tokens 를 소스코드나 `strings.xml` 에 평문으로 남기지 마세요. (Local Build Secrets 활용)
- **로컬 저장소 암호화**: Shared Preferences 나 SQLite DB 는 반드시 **EncryptedSharedPreferences** 또는 **SQLCipher**를 사용하여 암호화하세요.
- **백업 제외 설정**: `allowBackup="false"` 를 설정하거나, 백업이 필요한 경우 민감 데이터를 명시적으로 제외하세요.

##### **B. 통신 보안 (Network Security)**
- **HTTPS 강제화**: 모든 통신은 TLS 1.3 이상을 사용하세요.
- **인증서 핀닝 (Certificate Pinning)**: 중간자 공격(MITM)을 방지하기 위해 신뢰할 수 있는 서버의 공개키 해시를 앱 내에 고정하세요.
- **PQC (Post-Quantum Cryptography)**: 장기적인 보안이 필요한 데이터라면 Apple 의 PQ3 프로토콜과 같은 양자 내성 암호 적용을 고려하세요.

##### **C. 컴포넌트 보안 (Component Security)**
- **Intent Hijacking 방지**: 외부 앱에서 호출할 필요가 없는 Component 는 `exported="false"` 로 설정하세요.
- **Deeplink 검증**: 커스텀 URL 스킴을 통해 전달되는 파라미터는 인젝션 공격의 통로가 될 수 있으므로 엄격하게 필터링하세요.

---

#### 🚀 3. 배포 및 운영 단계 (Deployment Phase)

상용 배포 전 최종적으로 확인해야 할 사항입니다.

- **무결성 검증 (Integrity Check)**:
    - **Android**: Play Integrity API 를 사용하여 앱이 정식 스토어에서 받은 무결한 상태인지 확인하세요.
    - **iOS**: App Attest 를 통해 디바이스와 앱의 무결성을 증명하세요.
- **난독화 및 최적화 (Obfuscation)**:
    - **R8/ProGuard**를 적용하여 리버스 엔지니어링 시 비즈니스 로직 노출을 최소화하세요.
- **루팅/탈옥 탐지**: 금융 등 민감한 앱의 경우 변조된 환경에서의 실행을 차단하는 RASP 로직을 포함하세요.

---

#### 🚨 최신 공격 이슈 대응 (Incident Awareness)
- **Zero-Click Exploits**: 미디어 파서(Image, Video) 취약점을 통한 공격이 많으므로, 가급적 시스템 제공 API 를 사용하고 보안 패치를 최우선으로 적용하세요.
- **AI-Powered Phishing**: LLM 기반의 정교한 텍스트를 통한 사회 공학적 공격에 대비하여, 앱 내에서 사용자에게 "민감 정보 입력 주의" 알림을 강화하세요.

---

#### 📚 관련 리소스

- [[mobile-vulnerability-check]] - OWASP 기반 종합 체크리스트
- [[mobile-advanced-security-tips]] - RASP 및 Zero Trust 구현 팁
- [[android-security-permissions]] - 안드로이드 권한 정책 상세
