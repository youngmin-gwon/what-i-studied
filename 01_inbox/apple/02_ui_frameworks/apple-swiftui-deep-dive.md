---
title: apple-swiftui-deep-dive
tags: [apple, swiftui, ui, declarative, internals, attributegraph]
aliases: []
date modified: 2025-12-17 19:20:00 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## SwiftUI Deep Dive

"명령(Imperative)"에서 "선언(Declarative)"으로.
SwiftUI는 단순히 새로운 UI 프레임워크가 아니라, **생각하는 방식(Mindset)의 전환**을 요구합니다.
화면을 "어떻게(How) 그릴지"가 아니라 "무엇(What)을 보여줄지" 정의하면, 나머지는 프레임워크가 알아서 합니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **Mindset Shift**: `view.backgroundColor = .red`라고 쓰는 습관을 버려야 합니다. "State가 Error일 때 배경은 레드다"라고 선언해야 합니다.
- **성능 이슈 해결**: SwiftUI 뷰가 왜 자꾸 다시 그려지는지 모르겠다면, **Identity(정체성)**와 **Dependency(의존성)** 개념을 모르는 것입니다.
- **UIKit 통합**: 100% SwiftUI 앱은 아직 어렵습니다. `UIViewRepresentable`을 통해 기존 UIKit 생태계를 끌어안는 법을 알아야 합니다.

---

### 📚 외부 리소스 및 참고 자료

#### 공식 문서 (Official Docs)
- [SwiftUI Documentation](https://developer.apple.com/documentation/swiftui)
- [SwiftUI View Lifecycle](https://developer.apple.com/documentation/swiftui/view-lifecycle)

#### 🎥 WWDC 세션
- [WWDC 2021: Demystify SwiftUI](https://developer.apple.com/videos/play/wwdc2021/10022/) - **Identity, Lifetime, Dependency** 핵심 설명 (필독)
- [WWDC 2023: Explore SwiftUI animation](https://developer.apple.com/videos/play/wwdc2023/10156/)

---

### 🔍 내부 동작 원리 (Internals)

#### 1. AttributeGraph (AG)
SwiftUI는 뷰 계층을 렌더링하기 위해 내부적으로 **AttributeGraph**라는 C++ 기반의 종속성 그래프(Dependency Graph)를 유지합니다.
- `body`를 호출할 때마다 새로운 뷰 트리를 생성하는 것처럼 보이지만, 실제로는 AG의 노드 값을 갱신(Diffing)하는 것입니다.
- `@State`, `@Binding` 등은 AG 내의 노드에 대한 포인터 역할을 하며, 값이 변경되면 해당 노드를 구독하는 하위 노드만 무효화(Invalidate)됩니다.

#### 2. Identity (정체성)
시스템이 "이 뷰가 저번의 그 뷰인가?"를 판단하는 기준입니다.
- **Structural Identity (구조적 정체성)**: 뷰 계층 구조 내의 위치로 식별합니다. `if-else` 분기 처리가 중요한 이유입니다.
    - `AnyView` 사용 시 구조적 정체성이 파괴되어 성능이 저하될 수 있습니다. (최악의 패턴: `var body: some View { if condition { AnyView(...) } else { AnyView(...) } }`)
- **Explicit Identity (명시적 정체성)**: `.id(...)` 수식어를 통해 부여합니다. `ForEach`에서 `id: \.self`를 쓰는 것이 이에 해당합니다.

---

### 상태 관리 패턴 (State Management)

#### @StateObject vs @ObservedObject
가장 흔한 실수 중 하나입니다.

| Property Wrapper | 소유권 (Ownership) | 생명주기 | 용도 |
|------------------|-------------------|----------|------|
| **@StateObject** | View가 소유함 | View 생성 시 최초 1회 초기화. View가 다시 그려져도 유지됨. | 데이터 소스 **생성** (`init()`) |
| **@ObservedObject** | 외부에서 주입됨 | View가 다시 그려지면 초기화되지 않지만, 의존성은 가짐. | 데이터 소스 **전달받음** |

```swift
struct ParentView: View {
    var body: some View {
        // ❌ 실수: 뷰가 렌더링 될 때마다 ViewModel이 새로 생성됨
        ChildView(viewModel: MyViewModel()) 
        
        // ✅ 올바른 사용: StateObject가 생명주기를 관리
        ChildWithStateObject()
    }
}
```

#### PreferenceKey (자식 -> 부모 데이터 전달)
UIKit의 Delegate 패턴을 대체합니다. 자식 뷰의 크기나 스크롤 위치를 부모에게 알릴 때 사용합니다.

```swift
struct HeightPreferenceKey: PreferenceKey {
    static var defaultValue: CGFloat = 0
    static func reduce(value: inout CGFloat, nextValue: () -> CGFloat) {
        value = max(value, nextValue()) // 여러 자식 중 가장 큰 값 선택
    }
}
```

---

### 🛡️ 고급 레이아웃 및 애니메이션

#### Layout Protocol (iOS 16+)
`GeometryReader`는 부모 크기를 강제로 차지하는 부작용이 있습니다. `Layout` 프로토콜을 사용하면 자식 뷰들의 크기를 측정(`sizeThatFits`)하고 세밀하게 배치(`placeSubviews`)할 수 있습니다.

#### Transaction & Animation
`withAnimation`은 내부적으로 `Transaction` 객체를 전파합니다. 이를 가로채거나 수정하여 애니메이션을 세밀하게 제어할 수 있습니다.
예를 들어, 상위 뷰의 애니메이션이 하위 뷰에 전파되는 것을 막을 때 유용합니다.

```swift
.transaction { transaction in
    transaction.animation = nil // 이 하위 뷰들은 애니메이션 끄기
}
```

---

### Debugging & Troubleshooting

#### `Self._printChanges()`
iOS 15부터 제공되는 디버깅 헬퍼. 뷰의 `body`가 왜 재호출되었는지 콘솔에 찍어줍니다.

```swift
var body: some View {
    let _ = Self._printChanges() // Console: "Executed... items changed."
    List(items) { ... }
}
```

#### Hang / Hitches 원인
- `body` 내부에서 무거운 계산 수행 (AG 업데이트 지연).
- `AnyView` 과다 사용으로 인한 Diffing 실패 및 전체 리드로우.
- 메인 스레드에서 무거운 데이터 로딩 (Swift Concurrency로 해결).

### 더 보기
- [[apple-uikit-lifecycle]] - UIKit과의 공존 (`UIViewRepresentable`)
- [[apple-combine-framework]] - ViewModel의 `ObservableObject` 파이프라인
