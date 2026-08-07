---
title: apple-observation-framework
tags: [apple, macro, observable, observation, state-management, swiftui]
aliases: []
date modified: 2026-04-06 17:58:11 +09:00
date created: 2026-04-03 23:58:00 +09:00
---

## Observation Framework Deep Dive

iOS 17 에서 도입된 `@Observable` 매크로는 단순한 API 변경이 아닙니다.

SwiftUI 의 **상태 관리 패러다임 자체를 바꾼** 혁명적 변화입니다.

기존의 `ObservableObject` + `@Published` + `@StateObject`/`@ObservedObject` 조합은 **객체 단위**로 변경을 추적했습니다. 프로퍼티 하나만 바뀌어도 해당 객체를 구독하는 **모든 뷰**가 다시 평가되었습니다.

`@Observable` 은 **프로퍼티 단위**로 추적합니다. 뷰의 `body` 에서 실제로 읽은 프로퍼티만 변경될 때 해당 뷰만 다시 평가됩니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **성능 혁신**: 대규모 앱에서 불필요한 뷰 재평가가 80% 이상 줄어들 수 있습니다. "왜 내 리스트가 버벅이지?"의 근본 원인이 사라집니다.
- **코드 단순화**: `@Published`, `@StateObject`, `@ObservedObject` 삼총사가 사라집니다. 그냥 `@State` 와 `@Environment` 만 있으면 됩니다.
- **Combine 탈출**: ViewModel → View 데이터 흐름에 Combine (`objectWillChange.send()`) 이 더 이상 필요 없습니다.

---

### 🔄 Before vs After

#### Before (iOS 16 이하 — ObservableObject)

```swift
// ViewModel
class UserViewModel: ObservableObject {
    @Published var name: String = ""
    @Published var email: String = ""
    @Published var avatarURL: URL?
}

// View
struct ProfileView: View {
    @StateObject var viewModel = UserViewModel()  // 객체 소유
    
    var body: some View {
        Text(viewModel.name) // name만 읽지만, email이 바뀌어도 body 재호출됨!
    }
}
```

#### After (iOS 17+ — Observation)

```swift
// ViewModel
@Observable
class UserViewModel {
    var name: String = ""       // @Published 필요 없음
    var email: String = ""
    var avatarURL: URL?
}

// View
struct ProfileView: View {
    @State var viewModel = UserViewModel()  // @StateObject 대신 @State
    
    var body: some View {
        Text(viewModel.name) // name만 읽으므로, email이 바뀌어도 body 재호출 안 됨!
    }
}
```

---

### ⚙️ 내부 동작 원리 (Under the Hood)

#### 1. 매크로 확장 (Macro Expansion)

`@Observable` 매크로가 컴파일 시점에 다음을 자동 생성합니다:

```swift
// 이것이 @Observable이 실제로 하는 일 (개념적 확장)
class UserViewModel {
    // 추적 엔진
    private let _$observationRegistrar = ObservationRegistrar()
    
    // 원본 저장소
    private var _name: String = ""
    
    // Computed Property로 래핑 (읽기/쓰기 가로채기)
    var name: String {
        get {
            _$observationRegistrar.access(self, keyPath: \.name)  // 👈 "누가 날 읽었는지" 기록
            return _name
        }
        set {
            _$observationRegistrar.withMutation(self, keyPath: \.name) {  // 👈 "내가 바뀔 거야" 알림
                _name = newValue
            }
        }
    }
}
```

#### 2. `withObservationTracking` (추적 메커니즘)

SwiftUI 의 뷰 시스템이 내부적으로 이 함수를 사용합니다:

```swift
withObservationTracking {
    // 이 클로저 안에서 읽힌 @Observable 프로퍼티들이 자동으로 추적됩니다
    let _ = viewModel.name  // name 이 추적 대상에 등록됨
    // viewModel.email 은 읽지 않았으므로 추적 안 됨
} onChange: {
    // 추적된 프로퍼티 중 하나라도 바뀌면 호출됨
    // SwiftUI 는 여기서 해당 뷰의 body 를 다시 평가함
}
```

이것이 **프로퍼티 수준 추적**의 핵심 원리입니다.

---

### 📋 SwiftUI 프로퍼티 래퍼 마이그레이션

| 레거시 (iOS 16-) | 현대 (iOS 17+) | 용도 |
|-------------------|----------------|------|
| `ObservableObject` 프로토콜 | `@Observable` 매크로 | ViewModel 정의 |
| `@Published` | (필요 없음 — 모든 `var` 가 자동 추적) | 프로퍼티 변경 알림 |
| `@StateObject` | `@State` | 뷰가 소유하는 객체 |
| `@ObservedObject` | 일반 프로퍼티 (래퍼 필요 없음) | 외부에서 주입받은 객체 |
| `@EnvironmentObject` | `@Environment` | 환경을 통한 주입 |

#### 주입 패턴 변경

```swift
// Before
@EnvironmentObject var settings: SettingsViewModel
// 주입: .environmentObject(settings)

// After
@Environment(SettingsViewModel.self) var settings
// 주입: .environment(settings)
```

---

### 🚫 추적에서 제외하기

계산 비용이 높거나 자주 바뀌는 프로퍼티 중 뷰 갱신이 불필요한 것은 제외할 수 있습니다.

```swift
@Observable
class SensorData {
    var location: CLLocation?            // 추적됨
    
    @ObservationIgnored
    var rawAccelerometerBuffer: [Double] = []  // 추적 안 됨 (뷰 갱신 불필요)
}
```

---

### 🔗 AsyncSequence 와의 조합

`@Observable` 객체의 프로퍼티 변경을 비동기 스트림으로 관찰할 수 있습니다.

```swift
// 프로퍼티 변경을 AsyncStream 으로 변환
func observeNameChanges(viewModel: UserViewModel) async {
    for await _ in AsyncStream<Void> { continuation in
        withObservationTracking {
            _ = viewModel.name
        } onChange: {
            continuation.yield()
        }
    } {
        print("이름이 바뀌었습니다: \(viewModel.name)")
    }
}
```

---

### ⚠️ 주의사항

1. **클래스 전용**: `@Observable` 은 `class` 에만 적용할 수 있습니다. `struct` 에는 사용할 수 없습니다 (struct 는 이미 값 타입이라 SwiftUI 가 자동 추적합니다).
2. **iOS 17+ 전용**: iOS 16 이하를 지원해야 한다면 여전히 `ObservableObject` 를 사용해야 합니다. `#available` 로 분기하는 것은 권장되지 않습니다.
3. **Collection 주의**: `@Observable` 객체 안의 배열(`[Item]`)은 배열 자체의 변경(추가/삭제)만 추적합니다. 배열 **내부 요소**의 프로퍼티 변경도 추적하려면 `Item` 도 `@Observable` 이어야 합니다.

>[!WARNING] **Devil's Advocate : 점진적 마이그레이션이 핵심**
>`@Observable` 이 우월하다고 해서 기존 `ObservableObject` 를 한꺼번에 바꾸면 안 됩니다.
> 1. iOS 17 미만을 지원해야 하는 앱에서는 **기존 패턴을 유지**하세요.
> 2. 새 ViewModel 부터 `@Observable` 을 적용하고, 기존 것은 자연스러운 리팩토링 시점에 전환하세요.
> 3. `ObservableObject` 와 `@Observable` 은 같은 앱 내에서 공존할 수 있습니다.

### 더 보기
- [apple-swiftui-deep-dive](../02_ui_frameworks/apple-swiftui-deep-dive.md) - SwiftUI 의 상태 관리 전체 그림
- [apple-combine-framework](../03_data_networking/apple-combine-framework.md) - Combine 이 Observation 에 의해 대체되는 흐름
- [apple-swift-concurrency](apple-swift-concurrency.md) - Actor 와 @Observable 의 결합
