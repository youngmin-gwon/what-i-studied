# AI 개인정보 보호 및 보안 (AI Privacy & Security)

에이전트가 앱의 기능을 자유롭게 호출하는 환경에서는 **데이터 유출(Data Leakage)**과 **권한 오남용** 방지가 핵심입니다.

##### 1) Gemini Nano (On-device AICore) 보안 모델

안드로이드는 **AICore**라는 전용 시스템 서비스를 통해 온디바이스 AI 연산을 수행합니다.

- **데이터 격리**: 개별 앱의 민감 데이터가 모델 학습에 사용되지 않으며, 모델 추론 시에만 메모리에 로드된 후 즉시 소멸됩니다.
- **Android Private Compute Core (PCC)**: AICore 는 네트워크 접근권이 없는 격리된 환경(PCC)에서 작동하며, 외부 통신이 필요한 경우에만 별도의 보안 게이트웨이를 거칩니다.
- **Android 15 기기 보호**: AI 에이전트가 민감한 데이터를 처리할 때, 사용자가 기기를 잠금 해제한 상태에서만 특정 도구(AppFunctions)를 실행할 수 있도록 보안 수준을 강화했습니다.

##### 2) 플랫폼별 보안 철학 비교

구글의 온디바이스 중심 보안과 애플의 클라우드 기반 보안(PCC)에 대한 상세 비교는 아래 문서를 참고하세요.

>[!TIP] **상세 비교 문서**
> - [cross-platform-ai-privacy-comparison](01_inbox/mobile/cross-platform/cross-platform-ai-privacy-comparison.md) - Gemini vs Apple PCC 심층 분석

##### 3) 에이전틱 보안 (Agentic Security) 실무
- **도구 호출 권한 위임**: 에이전트는 사용자가 명시적으로 허용한 범위 내에서만 도구에 접근할 수 있습니다.
- **심화 보안 팁**: [mobile-advanced-security-tips](01_inbox/mobile/cross-platform/mobile-advanced-security-tips.md) - 전문가용 RASP 및 API 보안 가이드

---
