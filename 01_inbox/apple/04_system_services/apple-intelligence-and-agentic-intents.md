---
title: apple-intelligence-and-agentic-intents
tags: [apple, apple-intelligence, siri, app-intents, ios/26]
aliases: [Apple Intelligence, Siri Campos, App Entities, iOS 26]
date modified: 2026-04-04 00:33:00 +09:00
date created: 2026-04-04 00:33:00 +09:00
---

## iOS 26: Apple Intelligence & Agentic Intents

iOS 26(버전 대점프)의 출시와 함께, 애플의 생태계는 개인화된 지능형 에이전트 환경으로 완전히 전환되었다. Apple Intelligence는 단순한 AI 비서가 아니라, 시스템 수준에서 앱의 모든 데이터(Entity)와 기능(Action)을 이해하고 실행하는 강력한 엔진이다.

> [!NOTE] **Android 비교: AppFunctions vs Apple Intelligence**
> - **Android**: `AppFunctions` (Android 16+)를 통해 모델 컨텍스트 프로토콜(MCP)과 유사한 구조로 앱의 기능을 도구화한다.
> - **iOS**: `App Intents` 프레임워크를 고도화하여 Siri가 앱 내부의 상세 액션을 수행한다. **Private Cloud Compute (PCC)**를 통한 보안과 온디바이스 연산의 결합이 특징이다. (iOS 26+)
> 자세한 내용은 [android-appfunctions-and-ai-agents](../../android/02_app_framework/android-appfunctions-and-ai-agents.md)를 참고하세요.

### 1. Liquid Glass 디자인 언어 (iOS 26+)

iOS 26의 가장 큰 시각적 변화는 **visionOS 3.0**에서 계승된 **Liquid Glass** 디자인이다.
- **Translucency**: 유리 질감과 깊이감(Depth)을 강조하여 멀티태스킹 시 가독성을 높인다.
- **Pill-shaped Bars**: 애플 워치와 비전 프로에서 검증된 알약 형태의 탭 바와 툴바가 iOS 전체의 표준이 되었다.

### 2. Siri Campos (LLM & Agentic Siri)

기존 Siri는 정해진 규칙에 따라 동작했지만, iOS 26의 **Siri Campos**는 초거대언어모델(LLM) 기반으로 사용자의 의도를 분석하고 `App Intents`를 조합하여 실행한다.

#### App Entity 와 App Intent 정의

```swift
import AppIntents

struct PhotoEntity: AppEntity {
    static var typeDisplayRepresentation: TypeDisplayRepresentation = "Photo"
    var id: String
    var dateCreated: Date
    // 시스템이 이 데이터의 의미를 이해하도록 메타데이터 제공
}

struct ApplyFilterIntent: AppIntent {
    static var title: LocalizedStringResource = "필터 적용"

    @Parameter(title: "필터 이름") var filterName: String
    @Parameter(title: "대상 사진") var target: PhotoEntity

    func perform() async throws -> some IntentResult {
        // 실제 사진 편집 로직 수행
        return .result()
    }
}
```

### 3. Private Cloud Compute (PCC) & Security

온디바이스 칩셋(Apple Silicon)만으로 처리하기 힘든 복잡한 요청은 애플의 전용 클라우드 **PCC**에서 익명화되어 처리된다. 이는 데이터가 서버에 저장되지 않고 처리 즉시 파기됨을 기술적으로 보장한다.

---

### 🏛️ 에이전틱 시대의 사용자 경험

사용자는 이제 "앱 간의 경계"를 느끼지 않고 시리에게 통합된 명령을 내린다. (예: "지난주에 찍은 제주도 사진들 중에서 제일 예쁜 거 하나 골라서 이번 주 금요일 미팅 일정에 첨부해 줘.")

> [!IMPORTANT] **Apple 개발자를 위한 제언 : App Intent 는 이제 선택이 아닌 필수다**
> iOS 26 환경에서 `App Intents`와 `App Entities`를 지원하지 않는 앱은 시스템 지능 시스템으로부터 고립된다. 앱의 UI보다 시스템이 내 앱의 데이터를 얼마나 잘 이해하는지(**Semantic Data Modeling**)가 앱의 점유율을 결정하게 될 것이다.

### 더 보기
- [apple-app-intents](apple-app-intents.md) - 기본 App Intents 구조
- [apple-swiftui-deep-dive](../02_ui_frameworks/apple-swiftui-deep-dive.md) - Liquid Glass 디자인 구현
- [apple-sandbox-and-security](../05_security_privacy/apple-sandbox-and-security.md) - PCC 및 보안 구조
