---
title: android-appfunctions-and-ai-agents
tags: [android, android/16, android/baklava, ai, appfunctions, gemini]
aliases: [AppFunctions, Agentic Platforms, AI Agents, Baklava]
date modified: 2026-04-04 00:33:00 +09:00
date created: 2026-04-04 00:33:00 +09:00
---

## Android 16: AppFunctions & AI Agents

Android 16(Baklava)은 단순한 모바일 OS에서 **에이전틱 플랫폼(Agentic Platform)**으로 공식적인 진화를 선언했다. 이제 하이엔드 안드로이드 기기는 단순한 앱 런처가 아니라, 여러 앱에 흩어진 기능을 조율(Orchestrate)하여 사용자의 의도를 수행하는 지능형 에이전트의 역할을 수행한다.

> [!NOTE] **iOS 비교: Apple Intelligence vs Android AppFunctions**
> - **iOS**: `App Intents` 프레임워크를 통해 Siri가 앱 내부의 Action과 Entity를 제어한다. 강력한 생태계 통합과 개인정보 보호(Private Cloud Compute)가 강점이다. (iOS 26+)
> - **Android**: `AppFunctions` 프레임워크를 도입했다. 이는 모델 컨텍스트 프로토콜(MCP)과 유사한 구조로, 모든 AI 에이전트가 앱의 기능을 '도구(Tool)'로 발견하고 호출할 수 있도록 표준화된 인터페이스를 제공한다.
> 자세한 내용은 [apple-intelligence-and-agentic-intents](../../apple/04_system_services/apple-intelligence-and-agentic-intents.md)를 참고하세요.

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

에이전트가 앱의 기능을 자유롭게 호출하는 환경에서는 **데이터 유출(Data Leakage)**과 **권한 오남용** 방지가 핵심이다.

#### 1) Gemini Nano (On-device AICore) 보안 모델
안드로이드는 **AICore**라는 전 전용 시스템 서비스를 통해 온디바이스 AI 연산을 수행한다.
- **데이터 격리**: 개별 앱의 민감 데이터가 모델 학습에 사용되지 않으며, 모델 추론 시에만 메모리에 로드된 후 즉시 소멸된다.
- **Private Compute Core (PCC)**: AICore 는 네트워크 접근권이 없는 격리된 환경(PCC)에서 작동하며, 외부 통신이 필요한 경우에만 별도의 보안 게이트웨이를 거친다.

#### 2) 대결: Google Gemini Nano vs Apple Private Cloud Compute (PCC)

| 비교 항목 | Google Gemini Nano (On-device) | Apple Private Cloud Compute (PCC) |
| :--- | :--- | :--- |
| **핵심 철학** | "데이터를 기기 밖으로 내보내지 않는다." | "클라우드에서도 기기 수준의 보안을 유지한다." |
| **추론 위치** | **온디바이스 (NPU)** | **하드웨어 강화 클라우드 노드 (Apple Silicon)** |
| **데이터 상태** | 로컬 샌드박스 내부 유지 | **Stateless**: 연산 후 즉시 파기(No Storage) |
| **장점** | 오프라인 작동, 제로 레이턴시, 물리적 격리 | 복잡한 고성능 모델 구동 가능, 공개 감사 가능 |
| **단점** | 하드웨어 사양(RAM 등)에 따른 성능 제한 | 네트워크 연결 필수, 서버 인프라 신뢰 필요 |

#### 3) 에이전틱 보안 (Agentic Security)
AI 에이전트가 도구(`AppFunction`)를 호출할 때 발생할 수 있는 보안 위협과 대응책이다.
- **도구 호출 권한 위임**: 에이전트는 사용자가 명시적으로 허용한 범위 내에서만 도구에 접근할 수 있다. (예: "메시지 읽기" 권한이 없는 앱의 AppFunction 은 호출 불가)
- **프롬프트 인젝션 방어**: 외부에서 주입된 악성 프롬프트가 AppFunction 을 통해 시스템 명령을 실행하지 못하도록, 입력값에 대한 엄격한 타입 검증과 샌드박싱이 적용된다.

---

### 🏛️ 에이전틱 시대의 설계 철학

이제 사용자는 "앱을 켜서 작업을 수행"하는 방식보다 "에이전트에게 결과물을 요구"하는 방식을 선호하게 된다.

> [!TIP] **Devil's Advocate : 앱의 UI는 더 이상 유일한 진입점이 아니다**
> 미래의 안드로이드 개발자는 화려한 UI를 짜는 것보다, 에이전트가 내 앱의 기능을 얼마나 정확하고 빠르게 사용할 수 있게 만드는지(**Function-first mindset**)를 더 고민해야 한다. 앱의 가치가 화면 안(In-app)이 아닌 화면 밖(Cross-app)에서 결정되는 시대가 왔다.

### 더 보기
- [android-app-actions-assistant](android-app-actions-assistant.md) - Assistant 연동 기초
- [android-accessibility-compose](android-accessibility-compose.md) - UI 자동화를 위한 시맨틱 구조
- [android-desktop-windowing-and-multitasking](android-desktop-windowing-and-multitasking.md) - 멀티태스킹과 생산성
