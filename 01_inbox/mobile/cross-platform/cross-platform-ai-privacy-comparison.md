# [[mobile-security]] > [[cross-platform-ai-privacy-comparison]]

## AI Privacy: Gemini Nano vs Apple Private Cloud Compute (PCC)

에이전틱 플랫폼(Agentic Platform) 시대의 핵심은 **"어떻게 사용자의 민감한 데이터를 보호하며 지능형 AI 기능을 제공할 것인가"**입니다. 본 문서는 구글과 애플의 서로 다른, 그러나 상호 보완적인 프라이버시 보호 아키텍처를 비교 분석합니다.

---

### 🛡️ Context: AI 보안의 새로운 패러다임

기존의 데이터 보호가 저장된 데이터(Data at Rest)와 전송 중인 데이터(Data in Transit)에 집중했다면, 차세대 AI 보안은 **추론 과정의 데이터(Data in Use)**와 **모델 가상화의 무결성**을 포함하는 전방위적 신뢰 모델을 요구합니다.

---

### 🏛️ 핵심 보안 기술 비교

| 비교 항목 | Google Gemini Nano (On-device) | Apple Private Cloud Compute (PCC) |
| :--- | :--- | :--- |
| **보안 철학** | "데이터를 기기 내부 격리 구역에 유지한다." | "클라우드에서도 온디바이스 급의 보안을 보장한다." |
| **추론 환경** | **온디바이스 (NPU / AICore)** | **보안 강화 클라우드 노드 (Apple Silicon)** |
| **데이터 영속성** | 로컬 샌드박스 내부에서만 유지 | **Stateless**: 연산 직후 메모리에서 즉시 파기 |
| **신뢰 검증** | Android Private Compute Core (PCC) | **Verifiable Transparency** (SW 빌드 공개 감사) |
| **주요 장점** | 완전한 오프라인 작동, 물리적 유출 차단 | 고성능 대규모 모델 구동, 엔드투엔드 암호화 |

---

### 🔍 플랫폼별 상세 아키텍처

#### 1. Google: Android Private Compute Core (Android PCC)
안드로이드는 OS 레벨에서 네트워크 접근권이 차단된 특수 격리 샌드박스인 **Android PCC**를 제공합니다.
- **AICore Isolation**: Gemini Nano와 같은 모델이 개별 앱의 민감 데이터를 처리할 때 외부 전송을 물리적으로 차단합니다.
- **Ephemeral Context**: 에이전트가 `AppFunctions`를 호출할 때 생성되는 모든 추론 컨텍스트는 작업 완료 즉시 메모리에서 소멸됩니다. ([[android-appfunctions-and-ai-agents]])

#### 2. Apple: Private Cloud Compute (Apple PCC)
애플은 고성능 연산이 필요한 경우 자체 설계한 보안 서버 노드인 **Apple PCC**로 작업을 위임합니다.
- **Diskless Computing**: PCC 서버는 영구 저장 장치가 없으며(Diskless), 모든 데이터는 휘발성 메모리(RAM)에서만 처리됩니다.
- **Cryptographic Attestation**: 서버 소프트웨어의 무결성이 암호학적으로 증명되지 않으면 기기에서 데이터를 전송하지 않는 강력한 투명성을 제공합니다. ([[apple-intelligence-and-agentic-intents]])

---

### 🛡️ 에이전틱 보안 (Agentic Security) 공통 원칙

두 플랫폼 모두 에이전트가 앱의 기능을 '도구'로서 호출할 때 다음의 샌드박스 원칙을 준수합니다.

1.  **Least Privilege Access**: 에이전트는 사용자가 요청한 특정 작업을 수행하는 데 필요한 최소한의 데이터(Entity)만 수집합니다.
2.  **Explicit Consent Only**: 사용자가 명시적으로 허용한 기능(`AppFunction`, `AppIntent`)만 에이전트의 검색 및 호출 대상이 됩니다.
3.  **Prompt Injection Defense**: 외부에서 주입된 악성 프롬프트가 시스템 도구를 탈취하여 송금이나 데이터 유출을 시도하지 못하도록 입력값 검증과 실행 격리를 수행합니다.

---

### 📚 연관 분석 가이드
- [[android-apple-2026-comparison]] - 2026년 차세대 플랫폼 통합 비교
- [[mobile-advanced-security-tips]] - 전문가를 위한 보안 심화 구현 팁
- [[cross-platform-mobile-vulnerability-check]] - 플랫폼 공통 취약점 점검 리스트
- [[mobile-security]] - 통합 모바일 보안 가이드
