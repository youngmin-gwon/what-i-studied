# 💡 Context: 에이전틱 시대의 앱 설계

이제 운영체제는 단순한 앱 실행기가 아니라 지능형 비서로 진화하고 있습니다. AppFunctions 는 앱의 기능을 표준화된 인터페이스로 개방하여 AI 엔진(Gemini 등)이 직접 제어할 수 있게 합니다.

>[!IMPORTANT] **Android 15 Edge-to-edge 레이아웃**
>Android 15 부터는 앱이 기본적으로 전체 화면(Edge-to-edge)을 점유합니다. 에이전트가 호출하는 AI 오버레이나 플로팅 UI 가 앱의 중요한 인터랙션 요소와 겹치지 않도록 **WindowInsets** 처리가 더욱 중요해졌습니다.

>[!NOTE] **상호 참조**
>Apple Intelligence 의 App Intents 및 에이전트 연동 방식은 [apple-intelligence-and-agentic-intents](01_inbox/mobile/apple/04_system_services/apple-intelligence-and-agentic-intents.md) 를 참고하세요.

---
