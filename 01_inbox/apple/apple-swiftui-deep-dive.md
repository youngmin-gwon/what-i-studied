---
title: apple-swiftui-deep-dive
tags: [apple, swiftui, ui, declarative]
aliases: []
date modified: 2025-12-16 17:01:32 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## SwiftUI Deep Dive apple swiftui ui declarative

SwiftUI 의 내부 동작과 고급 패턴. 기본은 [[apple-foundations]] 와 [[apple-app-lifecycle-and-ui]] 참고.

### SwiftUI 철학

선언적 UI 프레임워크. 상태가 변경되면 UI 가 자동으로 업데이트된다.

```swift
struct ContentView: View {
    @State private var count = 0
    
    var body: some View {
        VStack {
            Text("Count: \(count)")
            Button("Increment") {
                count += 1
            }
        }
    }
}
```

### View 생명주기

#### body 재평가

`body` 는 상태가 변경될 때마다 재평가된다.

```swift
struct ProfileView: View {
    @State private var name = "John"
    
    var body: some View {
        let _ = print("Body evaluated") // 상태 변경 시마다 출력
        
        VStack {
            Text("Hello, \(name)")
            TextField("Name", text: $name)
        }
    }
}
```

**최적화:**
```swift
// ❌ 나쁜 예: body 에서 무거운 계산
var body: some View {
    let expensiveResult = performExpensiveCalculation() // 매번 실행!
    return Text(expensiveResult)
}

// ✅ 좋은 예: 계산된 프로퍼티 사용
private var expensiveResult: String {
    performExpensiveCalculation()
}

var body: some View {
    Text(expensiveResult)
}
```

#### onAppear / onDisappear

```swift
struct DetailView: View {
    @StateObject private var viewModel = DetailViewModel()
    
    var body: some View {
        Text("Detail")
            .onAppear {
                viewModel.loadData()
            }
            .onDisappear {
                viewModel.cleanup()
            }
    }
}
```

### 상태 관리

#### @State

View 내부 상태. 값 타입 (struct, enum, primitive).

```swift
struct CounterView: View {
    @State private var count = 0
    @State private var isOn = false
    
    var body: some View {
        VStack {
            Text("\(count)")
            Toggle("Switch", isOn: $isOn)
            Button("Increment") {
                count += 1
            }
        }
    }
}
```

#### @Binding

부모로부터 전달받은 상태의 양방향 바인딩.

```swift
struct ParentView: View {
    @State private var text = ""
    
    var body: some View {
        VStack {
            Text("Parent: \(text)")
            ChildView(text: $text) // Binding 전달
        }
    }
}

struct ChildView: View {
    @Binding var text: String
    
    var body: some View {
        TextField("Enter text", text: $text)
    }
}
```

#### @ObservedObject vs @StateObject

**@StateObject**: View 가 소유. View 재생성 시에도 유지.

```swift
struct ContentView: View {
    @StateObject private var viewModel = ContentViewModel()
    
    var body: some View {
        Text(viewModel.data)
    }
}
```

**@ObservedObject**: 외부에서 전달받음. View 재생성 시 새 인스턴스 가능.

```swift
struct DetailView: View {
    @ObservedObject var viewModel: DetailViewModel
    
    var body: some View {
        Text(viewModel.data)
    }
}
```

**차이점:**
```swift
struct ParentView: View {
    @State private var toggle = false
    
    var body: some View {
        VStack {
            Toggle("Recreate", isOn: $toggle)
            
            // ❌ @ObservedObject: toggle 변경 시 새 인스턴스 생성
            ChildWithObserved()
            
            // ✅ @StateObject: toggle 변경해도 같은 인스턴스 유지
            ChildWithState()
        }
    }
}
```

#### @EnvironmentObject

View 계층 전체에 주입.

```swift
class UserSettings: ObservableObject {
    @Published var username = ""
    @Published var isDarkMode = false
}

@main
struct MyApp: App {
    @StateObject private var settings = UserSettings()
    
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(settings)
        }
    }
}

struct ContentView: View {
    @EnvironmentObject var settings: UserSettings
    
    var body: some View {
        Text("Hello, \(settings.username)")
    }
}

struct DeepChildView: View {
    @EnvironmentObject var settings: UserSettings // 자동으로 전달됨
    
    var body: some View {
        Toggle("Dark Mode", isOn: $settings.isDarkMode)
    }
}
```

### ObservableObject 패턴

```swift
class ViewModel: ObservableObject {
    @Published var items: [Item] = []
    @Published var isLoading = false
    @Published var errorMessage: String?
    
    func loadItems() async {
        isLoading = true
        defer { isLoading = false }
        
        do {
            items = try await fetchItems()
        } catch {
            errorMessage = error.localizedDescription
        }
    }
}

struct ListView: View {
    @StateObject private var viewModel = ViewModel()
    
    var body: some View {
        List(viewModel.items) { item in
            Text(item.name)
        }
        .overlay {
            if viewModel.isLoading {
                ProgressView()
            }
        }
        .alert("Error", isPresented: .constant(viewModel.errorMessage != nil)) {
            Button("OK") {
                viewModel.errorMessage = nil
            }
        }
        .task {
            await viewModel.loadItems()
        }
    }
}
```

### 레이아웃 시스템

#### Stack (VStack, HStack, ZStack)

```swift
VStack(alignment: .leading, spacing: 16) {
    Text("Title")
    Text("Subtitle")
}

HStack(alignment: .top, spacing: 8) {
    Image(systemName: "star")
    Text("Rating")
}

ZStack(alignment: .topLeading) {
    Rectangle()
        .fill(Color.blue)
    Text("Overlay")
        .padding()
}
```

#### Spacer와 Divider

```swift
HStack {
    Text("Left")
    Spacer() // 가능한 모든 공간 차지
    Text("Right")
}

VStack {
    Text("Top")
    Divider() // 구분선
    Text("Bottom")
}
```

#### GeometryReader

부모 크기에 따라 동적으로 레이아웃.

```swift
struct AdaptiveView: View {
    var body: some View {
        GeometryReader { geometry in
            VStack {
                Rectangle()
                    .fill(Color.blue)
                    .frame(width: geometry.size.width * 0.8,
                           height: geometry.size.height * 0.5)
                
                Text("Width: \(geometry.size.width)")
            }
        }
    }
}
```

**주의사항:**
```swift
// ❌ GeometryReader 는 가능한 모든 공간 차지
VStack {
    GeometryReader { geo in
        Text("Takes all space")
    }
    Text("Pushed down")
}

// ✅ frame 으로 제한
VStack {
    GeometryReader { geo in
        Text("Limited")
    }
    .frame(height: 100)
    
    Text("Proper position")
}
```

#### Layout Protocol (iOS 16+)

커스텀 레이아웃 컨테이너.

```swift
struct EqualWidthLayout: Layout {
    func sizeThatFits(proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) -> CGSize {
        let maxWidth = subviews.map { $0.sizeThatFits(.unspecified).width }.max() ?? 0
        let totalHeight = subviews.map { $0.sizeThatFits(.unspecified).height }.reduce(0, +)
        return CGSize(width: maxWidth, height: totalHeight)
    }
    
    func placeSubviews(in bounds: CGRect, proposal: ProposedViewSize, subviews: Subviews, cache: inout ()) {
        var y = bounds.minY
        for subview in subviews {
            let size = subview.sizeThatFits(.unspecified)
            subview.place(at: CGPoint(x: bounds.minX, y: y), proposal: .init(width: bounds.width, height: size.height))
            y += size.height
        }
    }
}

// 사용
EqualWidthLayout {
    Text("Short")
    Text("Much longer text")
    Text("Medium")
}
```

### ViewModifier

재사용 가능한 스타일.

```swift
struct CardModifier: ViewModifier {
    func body(content: Content) -> some View {
        content
            .padding()
            .background(Color.white)
            .cornerRadius(10)
            .shadow(radius: 5)
    }
}

extension View {
    func cardStyle() -> some View {
        modifier(CardModifier())
    }
}

// 사용
Text("Hello")
    .cardStyle()
```

#### 조건부 Modifier

```swift
extension View {
    @ViewBuilder
    func `if`<Transform: View>(_ condition: Bool, transform: (Self) -> Transform) -> some View {
        if condition {
            transform(self)
        } else {
            self
        }
    }
}

// 사용
Text("Hello")
    .if(isHighlighted) { view in
        view.foregroundColor(.red)
    }
```

### PreferenceKey

자식에서 부모로 데이터 전달.

```swift
struct HeightPreferenceKey: PreferenceKey {
    static var defaultValue: CGFloat = 0
    
    static func reduce(value: inout CGFloat, nextValue: () -> CGFloat) {
        value = max(value, nextValue())
    }
}

struct ParentView: View {
    @State private var childHeight: CGFloat = 0
    
    var body: some View {
        VStack {
            Text("Child height: \(childHeight)")
            
            ChildView()
                .onPreferenceChange(HeightPreferenceKey.self) { value in
                    childHeight = value
                }
        }
    }
}

struct ChildView: View {
    var body: some View {
        Text("I'm the child")
            .padding(50)
            .background(GeometryReader { geo in
                Color.clear.preference(key: HeightPreferenceKey.self, value: geo.size.height)
            })
    }
}
```

### 애니메이션

#### 암시적 애니메이션

```swift
struct AnimatedView: View {
    @State private var scale: CGFloat = 1.0
    
    var body: some View {
        Circle()
            .scaleEffect(scale)
            .animation(.spring(response: 0.3), value: scale)
            .onTapGesture {
                scale = scale == 1.0 ? 1.5 : 1.0
            }
    }
}
```

#### 명시적 애니메이션

```swift
struct ExplicitAnimationView: View {
    @State private var offset: CGFloat = 0
    
    var body: some View {
        Circle()
            .offset(x: offset)
            .onTapGesture {
                withAnimation(.easeInOut(duration: 1.0)) {
                    offset = offset == 0 ? 100 : 0
                }
            }
    }
}
```

#### 트랜지션

```swift
struct TransitionView: View {
    @State private var showDetail = false
    
    var body: some View {
        VStack {
            Button("Toggle") {
                showDetail.toggle()
            }
            
            if showDetail {
                DetailView()
                    .transition(.asymmetric(
                        insertion: .move(edge: .trailing),
                        removal: .move(edge: .leading)
                    ))
            }
        }
        .animation(.default, value: showDetail)
    }
}
```

#### 커스텀 트랜지션

```swift
extension AnyTransition {
    static var pivot: AnyTransition {
        .modifier(
            active: PivotModifier(angle: -90),
            identity: PivotModifier(angle: 0)
        )
    }
}

struct PivotModifier: ViewModifier {
    let angle: Double
    
    func body(content: Content) -> some View {
        content
            .rotationEffect(.degrees(angle), anchor: .topLeading)
            .clipped()
    }
}
```

### 제스처

```swift
struct GestureView: View {
    @State private var offset = CGSize.zero
    @State private var scale: CGFloat = 1.0
    
    var body: some View {
        Circle()
            .fill(Color.blue)
            .frame(width: 100, height: 100)
            .scaleEffect(scale)
            .offset(offset)
            .gesture(
                DragGesture()
                    .onChanged { value in
                        offset = value.translation
                    }
                    .onEnded { _ in
                        withAnimation {
                            offset = .zero
                        }
                    }
            )
            .gesture(
                MagnificationGesture()
                    .onChanged { value in
                        scale = value
                    }
                    .onEnded { _ in
                        withAnimation {
                            scale = 1.0
                        }
                    }
            )
    }
}
```

#### 제스처 조합

```swift
// 동시 제스처
let combined = DragGesture()
    .simultaneously(with: MagnificationGesture())

// 순차 제스처
let sequential = LongPressGesture()
    .sequenced(before: DragGesture())
```

### 성능 최적화

#### LazyStack

```swift
// ❌ 모든 뷰를 즉시 생성
ScrollView {
    VStack {
        ForEach(0..<1000) { i in
            ExpensiveView(index: i)
        }
    }
}

// ✅ 화면에 보이는 것만 생성
ScrollView {
    LazyVStack {
        ForEach(0..<1000) { i in
            ExpensiveView(index: i)
        }
    }
}
```

#### Equatable

```swift
struct ItemView: View, Equatable {
    let item: Item
    
    var body: some View {
        Text(item.name)
    }
    
    static func == (lhs: ItemView, rhs: ItemView) -> Bool {
        lhs.item.id == rhs.item.id
    }
}

// 사용
ForEach(items) { item in
    ItemView(item: item)
        .equatable() // 동일한 item 이면 재평가 안 함
}
```

### 고급 패턴

#### 커스텀 Binding

```swift
struct CustomBindingView: View {
    @State private var celsius: Double = 0
    
    private var fahrenheit: Binding<Double> {
        Binding(
            get: { celsius * 9/5 + 32 },
            set: { celsius = ($0 - 32) * 5/9 }
        )
    }
    
    var body: some View {
        VStack {
            TextField("Celsius", value: $celsius, format: .number)
            TextField("Fahrenheit", value: fahrenheit, format: .number)
        }
    }
}
```

#### 커스텀 Environment Value

```swift
private struct ThemeKey: EnvironmentKey {
    static let defaultValue: Theme = .light
}

extension EnvironmentValues {
    var theme: Theme {
        get { self[ThemeKey.self] }
        set { self[ThemeKey.self] = newValue }
    }
}

extension View {
    func theme(_ theme: Theme) -> some View {
        environment(\.theme, theme)
    }
}

// 사용
struct ContentView: View {
    @Environment(\.theme) var theme
    
    var body: some View {
        Text("Hello")
            .foregroundColor(theme.textColor)
    }
}
```

#### ViewBuilder 활용

```swift
struct ConditionalContent<TrueContent: View, FalseContent: View>: View {
    let condition: Bool
    let trueContent: TrueContent
    let falseContent: FalseContent
    
    init(
        _ condition: Bool,
        @ViewBuilder then trueContent: () -> TrueContent,
        @ViewBuilder else falseContent: () -> FalseContent
    ) {
        self.condition = condition
        self.trueContent = trueContent()
        self.falseContent = falseContent()
    }
    
    var body: some View {
        if condition {
            trueContent
        } else {
            falseContent
        }
    }
}
```

#### 복잡한 애니메이션 체인

```swift
struct ComplexAnimationView: View {
    @State private var isAnimating = false
    
    var body: some View {
        Circle()
            .fill(Color.blue)
            .frame(width: 100, height: 100)
            .scaleEffect(isAnimating ? 1.5 : 1.0)
            .opacity(isAnimating ? 0.5 : 1.0)
            .rotationEffect(.degrees(isAnimating ? 360 : 0))
            .animation(
                Animation
                    .spring(response: 0.5, dampingFraction: 0.6)
                    .repeatForever(autoreverses: true),
                value: isAnimating
            )
            .onAppear {
                isAnimating = true
            }
    }
}
```

#### Matched Geometry Effect

```swift
struct MatchedGeometryView: View {
    @Namespace private var animation
    @State private var isExpanded = false
    
    var body: some View {
        VStack {
            if !isExpanded {
                Circle()
                    .fill(Color.blue)
                    .frame(width: 100, height: 100)
                    .matchedGeometryEffect(id: "circle", in: animation)
            } else {
                Circle()
                    .fill(Color.blue)
                    .frame(width: 300, height: 300)
                    .matchedGeometryEffect(id: "circle", in: animation)
            }
            
            Button("Toggle") {
                withAnimation {
                    isExpanded.toggle()
                }
            }
        }
    }
}
```

### 디버깅 팁

```swift
// View 계층 확인
struct DebugView: View {
    var body: some View {
        Text("Hello")
            .background(Color.red)
            .border(Color.blue, width: 2)
            ._printChanges() // 재평가 이유 출력 (iOS 15+)
    }
}

// 성능 측정
struct PerformanceView: View {
    var body: some View {
        let _ = Self._printChanges()
        
        Text("Hello")
            .task {
                let start = Date()
                await loadData()
                print("Loaded in \(Date().timeIntervalSince(start))s")
            }
    }
}
```

### 더 보기

[[apple-combine-framework]], [[apple-uikit-lifecycle]], [[apple-swift-concurrency]], [[apple-app-lifecycle-and-ui]], [[apple-performance-and-debug]]
