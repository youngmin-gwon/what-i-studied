---
title: apple-combine-framework
tags: [apple, combine, reactive, frp, internals, backpressure]
aliases: []
date modified: 2025-12-17 20:30:00 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Combine Framework Deep Dive

"시간에 따라 발생하는 값(Stream of Values)"을 처리하는 Apple의 선언형 프레임워크입니다.
RxSwift, ReactiveSwift를 시스템 레벨로 흡수했으며, **SwiftUI의 데이터 흐름을 지탱하는 엔진**입니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **Async/Await가 있는데 왜?**: `async/await`는 "함수(Function)"입니다. 한 번 호출하면 끝납니다. 반면 Combine은 "파이프라인"입니다. 검색창에 글자를 칠 때마다 `debounce`로 거르고, 중복을 제거(`removeDuplicates`)해서 네트워크를 쏘는 로직은 `async/await`만으로는 구현이 매우 복잡합니다.
- **SwiftUI 필수**: `ObservableObject`, `@Published`는 Combine 기술입니다. SwiftUI와 데이터를 바인딩하려면 Combine을 알아야 합니다.
- **Debugging**: "왜 내 데이터가 UI에 안 뜨지?"라는 문제는 대부분 Combine 스트림이 중간에 끊겼거나(AnyCancellable 해제), 에러로 종료되었기 때문입니다.

---

### 📚 외부 리소스 및 참고 자료

#### 공식 문서 (Official Docs)
- [Combine Documentation](../../../../https:/developer.apple.com/documentation/combine.md)
- [Using Combine for Your App](../../../../https:/developer.apple.com/documentation/combine/using-combine-for-your-app.md)

#### 🎥 WWDC 세션
- [WWDC 2019: Introducing Combine](../../../../https:/developer.apple.com/videos/play/wwdc2019/722/.md)
- [WWDC 2019: Combine in Practice](../../../../https:/developer.apple.com/videos/play/wwdc2019/721/.md)

#### 💻 심화 학습
- [Using Combine (Book)](../../../../https:/heckj.github.io/swiftui-notes/.md) - 무료이자 최고의 가이드북
- [OpenCombine](../../../../https:/github.com/OpenCombine/OpenCombine.md) - Combine의 오픈소스 구현 (리눅스 호환용이지만 내부 이해에 도움됨)

---

### 🔍 내부 동작 원리 (Deep Dive)

Combine은 **Publisher(생산자)**, **Subscriber(소비자)**, 그리고 **Subscription(구독 티켓)**의 삼각관계로 돌아갑니다.

#### 1. Backpressure (배압 조절)
Combine이 Rx와 다른 가장 큰 차이점입니다.
Subcriber가 "나 데이터 3개만 더 줘"라고 요청(**Request Demand**)해야만 Publisher가 데이터를 보냅니다.
- **Unlimited Demand**: Rx처럼 무제한으로 데이터를 쏟아붓는 모드.
- **Custom Demand**: 소비 속도가 느리면 생산 속도를 늦출 수 있어, 메모리 폭발을 막습니다.

#### 2. AnyCancellable (Lifecycle)
Combine 파이프라인은 `Subscription` 객체가 유지되는 동안만 살아있습니다.
- `sink`나 `assign`이 반환하는 `AnyCancellable`을 변수에 저장하지 않으면, 그 즉시 구독이 취소(`cancel()`)되어 아무 일도 일어나지 않습니다.
- 뷰 컨트롤러가 사라질 때 `store(in: &cancellables)`에 담긴 구독들이 자동 해제되어 메모리 누수를 방지합니다.

---

### 🛠️ 고급 연산자 및 패턴

#### 1. FlatMap & SwitchToLatest (검색 최적화)
사용자가 검색어를 빠르게 바꿀 때, 이전 검색 요청을 취소하고 최신 것만 살려야 합니다.

```swift
@Published var query: String = ""

// ...

$query
    .debounce(for: 0.5, scheduler: RunLoop.main) // 0.5초 멈출 때만
    .removeDuplicates() // 같은 검색어 무시
    .map { text -> AnyPublisher<[Result], Error> in
        return api.search(text) // 네트워크 요청이 담긴 Publisher 리턴
    }
    .switchToLatest() // ⭐️ 핵심: 새 요청이 오면 이전 요청(Inner Publisher)을 구독 취소
    .sink { ... }
    .store(in: &cancellables)
```

#### 2. Merge vs Zip vs CombineLatest
- **Merge**: A나 B 중 **아무거나** 오면 방출. (타입이 같아야 함)
- **Zip**: A와 B가 **둘 다 짝이 맞게** 도착해야 방출. (튜플로 묶임)
- **CombineLatest**: A나 B 중 하나라도 오면, **가장 최근 값끼리** 묶어서 방출. (UI 갱신에 가장 많이 쓰임 - "아이디나 비번이 바뀔 때마다 버튼 활성 상태 체크")

#### 3. Custom Subscriber & Demand
직접 Subscriber를 만들면 Backpressure를 제어할 수 있습니다.

```swift
class MySubscriber: Subscriber {
    typealias Input = Int
    typealias Failure = Never
    
    func receive(subscription: Subscription) {
        subscription.request(.max(3)) // "일단 3개만 줘"
    }
    
    func receive(_ input: Int) -> Subscribers.Demand {
        print("Received: \(input)")
        return .none // "더 이상은 필요 없어" (혹은 .max(1)로 하나씩 추가 요청)
    }
    
    func receive(completion: Subscribers.Completion<Never>) {
        print("Done")
    }
}
```

### 🐞 디버깅 (Debugging Patterns)

Combine 체인은 블랙박스 같아서 디버깅이 어렵습니다. 

#### 1. `print()`
연산자 사이에 `.print("Step 1")`을 끼워 넣으면, 데이터가 흘러갈 때마다(`receive value`, `receive completion`) 콘솔에 로그가 찍힙니다.

#### 2. `handleEvents`
스트림에 영향을 주지 않고 사이드 이펙트(로깅, 인디케이터 제어)를 발생시킵니다.

```swift
.handleEvents(
    receiveSubscription: { _ in print("구독 시작") },
    receiveOutput: { _ in print("데이터 도착") },
    receiveCompletion: { _ in print("완료") },
    receiveCancel: { print("취소됨") }
)
```

### 더 보기
- [apple-swift-concurrency](../01_language_concurrency/apple-swift-concurrency.md) - 비동기 작업의 또 다른 축 (단발성 작업)
- [apple-uikit-lifecycle](../02_ui_frameworks/apple-uikit-lifecycle.md) - MVVM 패턴과 Combine의 결합
