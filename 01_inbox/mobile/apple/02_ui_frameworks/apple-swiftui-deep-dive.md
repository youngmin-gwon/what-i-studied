---
title: apple-swiftui-deep-dive
tags: [apple, attributegraph, declarative, internals, swiftui, ui]
aliases: []
date modified: 2026-04-06 18:02:59 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## SwiftUI Deep Dive

"명령(Imperative)"에서 "선언(Declarative)"으로.

SwiftUI 는 단순히 새로운 UI 프레임워크가 아니라, **생각하는 방식(Mindset)의 전환**을 요구합니다.

화면을 "어떻게(How) 그릴지"가 아니라 "무엇(What)을 보여줄지" 정의하면, 나머지는 프레임워크가 알아서 합니다.

### 💡 왜 이것을 알아야 하나요? (Context)

- **Mindset Shift**: `view.backgroundColor = .red` 라고 쓰는 습관을 버려야 합니다. "State 가 Error 일 때 배경은 레드다"라고 선언해야 합니다.
- **성능 이슈 해결**: SwiftUI 뷰가 왜 자꾸 다시 그려지는지 모르겠다면, **Identity(정체성)**와 **Dependency(의존성)** 개념을 모르는 것입니다.
- **UIKit 통합**: iOS 17/18 시대에는 100% SwiftUI 앱이 충분히 가능해졌지만, 기존 UIKit 기반 라이브러리나 고도로 커스텀된 컨트롤(예: 카메라 프리뷰, 복잡한 텍스트 에디터)이 필요한 경우 `UIViewRepresentable` 을 통한 통합 능력은 여전히 중요합니다.

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

SwiftUI 는 뷰 계층을 렌더링하기 위해 내부적으로 **AttributeGraph**라는 C++ 기반의 종속성 그래프(Dependency Graph)를 유지합니다.

- `body` 를 호출할 때마다 새로운 뷰 트리를 생성하는 것처럼 보이지만, 실제로는 AG 의 노드 값을 갱신(Diffing)하는 것입니다.
- `@State`, `@Binding` 등은 AG 내의 노드에 대한 포인터 역할을 하며, 값이 변경되면 해당 노드를 구독하는 하위 노드만 무효화(Invalidate)됩니다.

#### 2. Identity (정체성)

시스템이 "이 뷰가 저번의 그 뷰인가?"를 판단하는 기준입니다.

- **Structural Identity (구조적 정체성)**: 뷰 계층 구조 내의 위치로 식별합니다. `if-else` 분기 처리가 중요한 이유입니다.
    - `AnyView` 사용 시 구조적 정체성이 파괴되어 성능이 저하될 수 있습니다. (최악의 패턴: `var body: some View { if condition { AnyView(…) } else { AnyView(…) } }`)
- **Explicit Identity (명시적 정체성)**: `.id(…)` 수식어를 통해 부여합니다. `ForEach` 에서 `id: \.self` 를 쓰는 것이 이에 해당합니다.

---

### 상태 관리 패턴 (State Management)

#### @Observable 매크로 (iOS 17+, Swift 5.9+) vs Legacy (@StateObject)

>[!WARNING] **Devil's Advocate : View 렌더링 최적화의 패러다임 시프트**
>기존 `@StateObject` 및 `@ObservedObject` 는 뷰모델 내의 어떤 속성 하나만 바뀌어도 전체 렌더링(Diffing)을 유발할 수 있어 성능 최적화가 까다로웠습니다.
>현재 현대적인 SwiftUI 코드는 **완전한 Observation 프레임워크(`@Observable` 매크로)**를 채택하고 있습니다. 이것은 프로퍼티 단위로 의존성을 추적하므로 `willSet/didSet` 낭비 없이 뷰 업데이트가 획기적으로 가벼워집니다.

과거에는 뷰모델을 다음과 같이 사용했습니다 (Legacy):

| Property Wrapper | 소유권 (Ownership) | 생명주기 | 용도 |
|------------------|-------------------|----------|------|
| **@StateObject** | View 가 소유함 | View 생성 시 최초 1 회 초기화. View 가 다시 그려져도 유지됨. | 데이터 소스 **생성** (`init()`) |
| **@ObservedObject** | 외부에서 주입됨 | View 가 다시 그려지면 초기화되지 않지만, 의존성은 가짐. | 데이터 소스 **전달받음** |

```swift
// ❌ 기존(Legacy) 코드 방식
class MyViewModel: ObservableObject { @Published var data = 0 }
struct ChildView: View { @ObservedObject var vm: MyViewModel; ... }

// ✅ 현대(Modern iOS 17+) 코드 방식
@Observable class MyViewModel { var data = 0 } // @Published 불필요

struct ParentView: View {
    @State private var viewModel = MyViewModel() // @StateObject 대신 @State 사용 가능
    var body: some View { ChildView(viewModel: viewModel) }
}
struct ChildView: View { 
    var viewModel: MyViewModel // @ObservedObject 불필요, 뷰가 프로퍼티 변경만 추적함
    var body: some View { Text("\(viewModel.data)") }
}
```

#### PreferenceKey (자식 -> 부모 데이터 전달)

UIKit 의 Delegate 패턴을 대체합니다. 자식 뷰의 크기나 스크롤 위치를 부모에게 알릴 때 사용합니다.

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

`GeometryReader` 는 부모 크기를 강제로 차지하는 부작용이 있습니다. `Layout` 프로토콜을 사용하면 자식 뷰들의 크기를 측정(`sizeThatFits`)하고 세밀하게 배치(`placeSubviews`)할 수 있습니다.

#### Transaction & Animation

`withAnimation` 은 내부적으로 `Transaction` 객체를 전파합니다. 이를 가로채거나 수정하여 애니메이션을 세밀하게 제어할 수 있습니다.

예를 들어, 상위 뷰의 애니메이션이 하위 뷰에 전파되는 것을 막을 때 유용합니다.

```swift
.transaction { transaction in
    transaction.animation = nil // 이 하위 뷰들은 애니메이션 끄기
}
```

---

### Debugging & Troubleshooting

#### `Self._printChanges()`

iOS 15 부터 제공되는 디버깅 헬퍼. 뷰의 `body` 가 왜 재호출되었는지 콘솔에 찍어줍니다.

```swift
var body: some View {
    let _ = Self._printChanges() // Console: "Executed... items changed."
    List(items) { ... }
}
```

#### Hang / Hitches 원인

- `body` 내부에서 무거운 계산 수행 (AG 업데이트 지연).
- `AnyView` 과다 사용으로 인한 Diffing 실패 및 전체 리드로우.
- 메인 스레드에서 무거운 데이터 로딩 (Swift Concurrency 로 해결).

---

### 🧭 Navigation (iOS 16+)

>[!CAUTION] **`NavigationView` 는 Deprecated**
>iOS 16 부터 `NavigationView` 가 더 이상 사용되지 않습니다. 반드시 `NavigationStack` 또는 `NavigationSplitView` 로 대체해야 합니다.

#### 1. `NavigationStack` (프로그래매틱 내비게이션)

```swift
@State private var path = NavigationPath()

var body: some View {
    NavigationStack(path: $path) {
        List(items) { item in
            NavigationLink(value: item) { // 값 기반 링크
                Text(item.name)
            }
        }
        .navigationDestination(for: Item.self) { item in
            DetailView(item: item) // 타입 기반 목적지 매핑
        }
    }
}

// 코드에서 직접 네비게이션
func navigateToDetail(_ item: Item) {
    path.append(item) // Push
}
func popToRoot() {
    path = NavigationPath() // 루트로 이동
}
```

#### 2. `NavigationSplitView` (다중 컬럼)

iPad/Mac 의 사이드바 - 디테일 패턴입니다.

```swift
NavigationSplitView {
    Sidebar()        // 사이드바
} content: {
    ContentList()    // 중간 패널 (iPad)
} detail: {
    DetailView()     // 상세 패널
}
```

---

### 🖼️ `#Preview` 매크로

기존 `PreviewProvider` 를 대체하는 더 간결한 미리보기 선언입니다.

```swift
// Before: 장황한 구조체
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

// After: 매크로 (Xcode 15+)
#Preview("기본 프리뷰") {
    ContentView()
}

#Preview("다크 모드") {
    ContentView()
        .preferredColorScheme(.dark)
}
```

---

### 💎 iOS 26: Liquid Glass Design System

iOS 26 은 visionOS 에서 시작된 **Liquid Glass** 디자인 언어를 시스템 전반에 통합했습니다. SwiftUI 는 이를 구현하기 위한 최적의 도구입니다.

#### 1. Material & Translucency

유리 질감(Glassmorphism)과 동적 투명도를 활용하여 레이어 간의 깊이감을 표현합니다.

```swift
struct GlassyCard: View {
    var body: some View {
        VStack {
            Text("Liquid Glass")
        }
        .padding()
        // iOS 26+ 신규 머티리얼 효과
        .background(.ultraThinMaterial, in: RoundedRectangle(cornerRadius: 24))
        .shadow(color: .black.opacity(0.1), radius: 10, x: 0, y: 5)
    }
}
```

#### 2. Pill-shaped UI (알약형 컴포넌트)

탭 바, 툴바, 플로팅 버튼 등 모든 주요 컨트롤이 부드러운 곡률의 알약 형태로 변화했습니다. `.clipShape(.capsule)` 와 `.containerBackground` 수식어의 중요성이 커졌습니다.

#### 3. Spatial Intelligence (공간 지능)

visionOS 와 공유되는 코드를 통해 2D 화면에서도 그림자와 조명 효과가 실시간으로 변하는 '공간적(Spatial)' 느낌을 줍니다.

---

### 더 보기

- [[apple-uikit-lifecycle]] - UIKit 과의 공존 (`UIViewRepresentable`)
- [[apple-observation-framework]] - `@Observable` 패러다임 시프트 상세
- [[apple-combine-framework]] - 비동기 스트림 처리 (레거시 `ObservableObject` 파이프라인 → `@Observable` 전환)
