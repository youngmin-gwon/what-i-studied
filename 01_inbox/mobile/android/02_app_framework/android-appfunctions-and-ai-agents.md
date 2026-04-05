# [[mobile-security]] > [[android-appfunctions-and-ai-agents]]

## AI Agents: AppFunctions Platform

Android 15/16(Baklava)에서 도입된 **AppFunctions** 프레임워크와 이를 통한 **에이전틱 플랫폼(Agentic Platform)**으로의 진화를 분석합니다. 

앱 내부의 기능을 시스템 AI 에이전트가 발견하고 호출할 수 있는 '도구(Tool)'로 노출하여, 사용자의 복합적인 의도를 여러 앱이 협력하여 수행하는 차세대 연동 아키텍처를 이해하는 것이 목표입니다.

---

### 💡 Context: 에이전틱 시대의 앱 설계

이제 운영체제는 단순한 앱 실행기가 아니라 지능형 비서로 진화하고 있습니다. AppFunctions는 앱의 기능을 표준화된 인터페이스로 개방하여 AI 엔진(Gemini 등)이 직접 제어할 수 있게 합니다.

> [!IMPORTANT] **Android 15 Edge-to-edge 레이아웃**
> Android 15부터는 앱이 기본적으로 전체 화면(Edge-to-edge)을 점유합니다. 에이전트가 호출하는 AI 오버레이나 플로팅 UI가 앱의 중요한 인터랙션 요소와 겹치지 않도록 **WindowInsets** 처리가 더욱 중요해졌습니다.

> [!NOTE] **상호 참조**
> Apple Intelligence의 App Intents 및 에이전트 연동 방식은 [[apple-intelligence-and-agentic-intents]]를 참고하세요.

---

### 1. AppFunctions 프레임워크

앱 개발자가 자신의 앱에 포함된 특정 기능을 시스템 AI 에이전트에게 **도구(Tool)**로 노출하는 신규 API이다.

#### AppFunction 정의 (Jetpack Library)

```kotlin
@AppFunction(name = "create_note")
suspend fun createNote(
    @AppFunctionParam(name = "title") title: String,
    @AppFunctionParam(name = "content") content: String
): CreateNoteResult {
    // 에이전트의 자연어 요청을 받아 실제 앱 로직 수행
    val noteId = repository.addNote(title, content)
    return CreateNoteResult(id = noteId, status = "Success")
}
```

### 2. 에이전틱 오케스트레이션 (Agentic Orchestration)

안드로이드의 에이전트(주로 Gemini Nano)는 사용자의 자연어 명령을 분석하여 필요한 AppFunctions의 조합을 결정한다.

**예시 시나리오:**
1. **사용자 요청:** "우리 팀원들에게 오늘 오후 5시에 강남역 근처 카페에서 미팅한다고 메시지 보내줘."
2. **에이전트 판단:**
    *   `CalendarApp / find_free_slot` 호출하여 일정 확인.
    *   `MapApp / search_poi` (강남역 카페) 호출하여 위치 정보 획득.
    *   `MessengerApp / send_group_message` 호출하여 최종 발송.

### 3. AI 개인정보 보호 및 보안 (AI Privacy & Security)

에이전트가 앱의 기능을 자유롭게 호출하는 환경에서는 **데이터 유출(Data Leakage)**과 **권한 오남용** 방지가 핵심입니다.

#### 1) Gemini Nano (On-device AICore) 보안 모델
안드로이드는 **AICore**라는 전용 시스템 서비스를 통해 온디바이스 AI 연산을 수행합니다.
- **데이터 격리**: 개별 앱의 민감 데이터가 모델 학습에 사용되지 않으며, 모델 추론 시에만 메모리에 로드된 후 즉시 소멸됩니다.
- **Android Private Compute Core (PCC)**: AICore 는 네트워크 접근권이 없는 격리된 환경(PCC)에서 작동하며, 외부 통신이 필요한 경우에만 별도의 보안 게이트웨이를 거칩니다.
- **Android 15 기기 보호**: AI 에이전트가 민감한 데이터를 처리할 때, 사용자가 기기를 잠금 해제한 상태에서만 특정 도구(AppFunctions)를 실행할 수 있도록 보안 수준을 강화했습니다.

#### 2) 플랫폼별 보안 철학 비교
구글의 온디바이스 중심 보안과 애플의 클라우드 기반 보안(PCC)에 대한 상세 비교는 아래 문서를 참고하세요.
> [!TIP] **상세 비교 문서**
> - [[cross-platform-ai-privacy-comparison]] - Gemini vs Apple PCC 심층 분석

#### 3) 에이전틱 보안 (Agentic Security) 실무
- **도구 호출 권한 위임**: 에이전트는 사용자가 명시적으로 허용한 범위 내에서만 도구에 접근할 수 있습니다.
- **심화 보안 팁**: [[mobile-advanced-security-tips]] - 전문가용 RASP 및 API 보안 가이드

---

### 🏛️ 에이전틱 시대의 설계 철학

이제 사용자는 "앱을 켜서 작업을 수행"하는 방식보다 "에이전트에게 결과물을 요구"하는 방식을 선호하게 된다.

> [!TIP] **Devil's Advocate : 앱의 UI는 더 이상 유일한 진입점이 아니다**
> 미래의 안드로이드 개발자는 화려한 UI를 짜는 것보다, 에이전트가 내 앱의 기능을 얼마나 정확하고 빠르게 사용할 수 있게 만드는지(**Function-first mindset**)를 더 고민해야 한다. 앱의 가치가 화면 안(In-app)이 아닌 화면 밖(Cross-app)에서 결정되는 시대가 왔다.

### See Also

- [[android-app-actions-assistant]] - Assistant 연동 기초
- [[android-accessibility-compose]] - UI 자동화를 위한 시맨틱 구조
- [[android-desktop-windowing-and-multitasking]] - 멀티태스킹과 생산성
