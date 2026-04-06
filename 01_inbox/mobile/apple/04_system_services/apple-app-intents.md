---
title: apple-app-intents
tags: [app-intents, apple, intelligence, shortcuts, siri, spotlight, widgets]
aliases: []
date modified: 2026-04-06 18:07:45 +09:00
date created: 2026-04-03 23:58:00 +09:00
---

## App Intents & Shortcuts Deep Dive

"시리야, 오늘 운동 기록 보여줘."

이 한마디가 작동하려면 **App Intents** 프레임워크가 필요합니다.

App Intents 는 단순히 Siri 용 API 가 아닙니다. **Spotlight, Shortcuts 앱, Action Button, Interactive Widgets, 그리고 Apple Intelligence** 까지 — 앱을 시스템 곳곳에 노출시키는 **유일한 관문**입니다.

### 💡 왜 이것을 알아야 하나요? (Context)

- **Apple Intelligence (iOS 18+)**: Apple 의 온디바이스 AI 가 사용자의 의도를 파악하고 앱의 기능을 자동으로 호출합니다. 이때 사용하는 것이 App Intents 입니다. 구현하지 않으면 AI 에게 "보이지 않는" 앱이 됩니다.
- **Interactive Widgets (iOS 17+)**: 위젯에서 버튼을 누르면 앱을 열지 않고도 동작이 수행됩니다. 이것도 AppIntent 기반입니다.
- **레거시 교체**: 과거의 `SiriKit Intent Definition (.intentdefinition)` 파일 기반 방식을 **완전히 대체**합니다. 새 프로젝트에서는 .intentdefinition 파일을 만들 일이 없습니다.

---

### 📐 핵심 아키텍처

#### 1. `AppIntent` 프로토콜 (동작 정의)

"이 앱이 할 수 있는 일"을 선언합니다.

```swift
import AppIntents

struct StartWorkoutIntent: AppIntent {
    // Siri/Spotlight 에 보여질 제목
    static var title: LocalizedStringResource = "운동 시작"
    static var description: IntentDescription = "선택한 운동 타입으로 운동을 시작합니다."
    
    // 파라미터 (사용자 입력)
    @Parameter(title: "운동 종류")
    var workoutType: WorkoutType
    
    // 실행 로직
    func perform() async throws -> some IntentResult & ProvidesDialog {
        let session = WorkoutManager.shared.start(type: workoutType)
        return .result(dialog: "\(workoutType.name) 운동을 시작합니다! 💪")
    }
}
```

#### 2. `AppEntity` 프로토콜 (데이터 노출)

앱의 데이터 모델을 시스템에 노출합니다. Siri 가 "어떤 운동?"이라고 물을 때 목록을 보여주는 데 사용됩니다.

```swift
struct WorkoutType: AppEntity {
    static var typeDisplayRepresentation = TypeDisplayRepresentation(name: "운동 종류")
    static var defaultQuery = WorkoutTypeQuery()
    
    var id: String
    var name: String
    
    var displayRepresentation: DisplayRepresentation {
        DisplayRepresentation(title: "\(name)")
    }
}

// 시스템이 엔티티를 검색할 때 사용하는 쿼리
struct WorkoutTypeQuery: EntityQuery {
    func entities(for ids: [String]) async throws -> [WorkoutType] {
        WorkoutStore.shared.workouts(for: ids)
    }
    
    func suggestedEntities() async throws -> [WorkoutType] {
        WorkoutStore.shared.allWorkouts()
    }
}
```

#### 3. `AppShortcutsProvider` (시스템 등록)

Shortcuts 앱과 Siri 에 자동으로 등록됩니다. 사용자가 별도 설정 없이 바로 쓸 수 있습니다.

```swift
struct MyAppShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: StartWorkoutIntent(),
            phrases: [
                "운동 시작해 \(.applicationName)",
                "\(.applicationName)에서 \(\.$workoutType) 시작"
            ],
            shortTitle: "운동 시작",
            systemImageName: "figure.run"
        )
    }
}
```

---

### 🧩 시스템 연동 포인트

| 연동 대상 | 역할 | 필요한 것 |
|-----------|------|-----------|
| **Siri** | 음성 명령으로 앱 기능 실행 | `AppShortcutsProvider` + phrases |
| **Spotlight** | 앱 내 콘텐츠를 검색 결과에 노출 | `AppEntity` + `IndexedEntity` |
| **Shortcuts 앱** | 사용자가 자동화 워크플로우 구성 | `AppIntent` 등록 |
| **Interactive Widgets** | 위젯에서 버튼 터치로 동작 실행 | `AppIntent` + `Button(intent:)` |
| **Action Button** | iPhone 15 Pro 물리 버튼 | `AppShortcutsProvider` 에 등록 |
| **Apple Intelligence** | AI 가 맥락에 맞는 기능 자동 제안 | `AppEntity` + `AppIntent` |

---

### 📱 Interactive Widgets 과의 관계 (iOS 17+)

위젯에서 직접 동작을 수행할 수 있습니다. `AppIntent` 를 버튼의 액션으로 연결합니다.

```swift
struct ToggleTodoIntent: AppIntent {
    static var title: LocalizedStringResource = "할 일 완료 토글"
    
    @Parameter(title: "Todo ID")
    var todoId: String
    
    func perform() async throws -> some IntentResult {
        TodoStore.shared.toggle(id: todoId)
        return .result()
    }
}

// 위젯 뷰에서 사용
struct TodoWidgetView: View {
    let todo: TodoEntry
    
    var body: some View {
        Button(intent: ToggleTodoIntent(todoId: todo.id)) {
            Label(todo.title, systemImage: todo.isDone ? "checkmark.circle.fill" : "circle")
        }
    }
}
```

>[!TIP] **`AppIntentTimelineProvider` (iOS 17+)**
>기존 `TimelineProvider` 대신 `AppIntentTimelineProvider` 를 사용하면, 위젯 설정(Configuration)도 App Intents 기반으로 통합할 수 있습니다.

---

### 🤖 Apple Intelligence 연동 (iOS 18+)

Apple Intelligence 가 사용자의 의도를 파악하여 앱의 기능을 자동으로 제안하거나 실행합니다.

- **SiriKit + App Intents**: 기존 SiriKit 도메인(메시지, 결제 등)이 App Intents 와 통합되고 있습니다.
- **Foundation Models**: 온디바이스 LLM 이 앱의 `AppEntity` 데이터를 이해하고, 자연어 요청을 적절한 `AppIntent` 로 라우팅합니다.

### 🤖 Android 비교: App Intents vs App Actions

Apple 의 App Intents 와 유사한 기능을 Android 에서는 **App Actions** 와 **AppFunctions** 가 담당합니다.

| 특징 | Apple App Intents | Android App Actions |
| :--- | :--- | :--- |
| **핵심 기술** | Swift 기반의 `AppIntent` 프로토콜 | `shortcuts.xml` 및 `capability` 선언 |
| **시스템 통합** | Siri, Shortcuts, Spotlight, Action Button | Google Assistant, Android Shortcuts |
| **데이터 노출** | `AppEntity` 프로토콜 | `shortcuts.xml` 의 `parameter` 매핑 |
| **AI 연동** | Apple Intelligence (iOS 18+) | AppFunctions (Android 16+), Gemini 연동 |

>[!TIP] **Android 개발자를 위한 App Intents**
> - `AppIntent.perform()` ≃ `shortcuts.xml` 에 정의된 Intent Fulfillment 처리 logic
> - `AppShortcut` ≃ Android 의 **Static Shortcut** (`shortcuts.xml`)
> - `AppEntity` ≃ 시스템이 검색할 수 있는 앱 내 데이터 (Search Indexing)
>상세 비교는 [android-app-actions-assistant](../../android/02_app_framework/android-app-actions-assistant.md) 를 참고하세요.

### 더 보기
- [apple-widgets-live-activities](../02_ui_frameworks/apple-widgets-live-activities.md) - WidgetKit 기본 아키텍처 및 타임라인
- [apple-system-services](apple-system-services.md) - 시스템 데몬과의 IPC 원리
- [apple-swift-concurrency](../01_language_concurrency/apple-swift-concurrency.md) - `perform()` 의 `async throws` 이해
