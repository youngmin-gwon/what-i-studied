---
title: apple-combine-framework
tags: [apple, backpressure, combine, frp, internals, reactive]
aliases: []
date modified: 2026-04-06 18:04:54 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Combine Framework Deep Dive

>[!CAUTION] **Devil's Advocate : Combine 의 설 자리 축소 (점진적 Legacy 화)**
>Combine 은 RxSwift 를 대체하며 화려하게 등장했지만, 현재 Apple 의 행보는 **Swift Concurrency (`AsyncSequence`, `AsyncAlgorithms`)** 및 **Observation (`@Observable`)** 프레임워크로의 전환을 확고히 하고 있습니다.
> 1. SwiftUI 의 상태 관리는 `@Published` 에서 `@Observable` 로 이관되었습니다.
> 2. URLSession 이나 비동기 작업은 `.dataTaskPublisher` 대신 순수 `async/await` 를 선호합니다.
>복잡한 다중 이벤트 병합(`merge`, `zip`, `CombineLatest`)이 필수인 스트림 처리 외에는 가급적 순수 Swift Concurrency 를 사용하는 것이 장기적 관점에서 올바릅니다.

"시간에 따라 발생하는 값(Stream of Values)"을 처리하는 Apple 의 선언형 프레임워크입니다. 과거 **SwiftUI 의 데이터 흐름을 지탱하는 핵심 엔진**이었습니다.

### 💡 왜 이것을 알아야 하나요? (Context)

- **Async/Await 가 있는데 왜?**: (과거의 관점) `async/await` 는 단발성 데이터, Combine 은 "파이프라인" 데이터입니다. 하지만 현재는 `Apple Swift Async Algorithms` 라이브러리가 등장하면서 `debounce`, `combineLatest` 조차 `AsyncSequence` 체이닝으로 처리가 가능해졌습니다.
- **SwiftUI 필수**: 과거엔 `@Published` 가 Combine 기술이었습니다. iOS 17 이상에서는 `@Observable` 매크로를 통해 Combine 의존 없이 SwiftUI 뷰 바인딩이 가능합니다.

---

### 📚 외부 리소스 및 참고 자료

#### 공식 문서 (Official Docs)

- [Combine Documentation](https://developer.apple.com/documentation/combine)
- [Using Combine for Your App](https://developer.apple.com/documentation/combine/using-combine-for-your-app)

#### 🎥 WWDC 세션

- [WWDC 2019: Introducing Combine](https://developer.apple.com/videos/play/wwdc2019/722/)
- [WWDC 2019: Combine in Practice](https://developer.apple.com/videos/play/wwdc2019/721/)

#### 💻 심화 학습

- [Using Combine (Book)](https://heckj.github.io/swiftui-notes/) - 무료이자 최고의 가이드북
- [OpenCombine](https://github.com/OpenCombine/OpenCombine) - Combine 의 오픈소스 구현 (리눅스 호환용이지만 내부 이해에 도움됨)

---

### 🔍 내부 동작 원리 (Deep Dive)

Combine 은 **Publisher(생산자)**, **Subscriber(소비자)**, 그리고 **Subscription(구독 티켓)** 의 삼각관계로 돌아갑니다.

#### 1. Backpressure (배압 조절)

Combine 이 Rx 와 다른 가장 큰 차이점입니다.

Subcriber 가 "나 데이터 3 개만 더 줘"라고 요청(**Request Demand**)해야만 Publisher 가 데이터를 보냅니다.

- **Unlimited Demand**: Rx 처럼 무제한으로 데이터를 쏟아붓는 모드.
- **Custom Demand**: 소비 속도가 느리면 생산 속도를 늦출 수 있어, 메모리 폭발을 막습니다.

#### 2. AnyCancellable (Lifecycle)

Combine 파이프라인은 `Subscription` 객체가 유지되는 동안만 살아있습니다.

- `sink` 나 `assign` 이 반환하는 `AnyCancellable` 을 변수에 저장하지 않으면, 그 즉시 구독이 취소(`cancel()`)되어 아무 일도 일어나지 않습니다.
- 뷰 컨트롤러가 사라질 때 `store(in: &cancellables)` 에 담긴 구독들이 자동 해제되어 메모리 누수를 방지합니다.

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

- **Merge**: A 나 B 중 **아무거나** 오면 방출. (타입이 같아야 함)
- **Zip**: A 와 B 가 **둘 다 짝이 맞게** 도착해야 방출. (튜플로 묶임)
- **CombineLatest**: A 나 B 중 하나라도 오면, **가장 최근 값끼리** 묶어서 방출. (UI 갱신에 가장 많이 쓰임 - "아이디나 비번이 바뀔 때마다 버튼 활성 상태 체크")

#### 3. Custom Subscriber & Demand

직접 Subscriber 를 만들면 Backpressure 를 제어할 수 있습니다.

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

연산자 사이에 `.print("Step 1")` 을 끼워 넣으면, 데이터가 흘러갈 때마다(`receive value`, `receive completion`) 콘솔에 로그가 찍힙니다.

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

---

### 🔄 AsyncSequence/AsyncStream 으로의 마이그레이션

Combine 의 핵심 역할이었던 "비동기 데이터 스트림"을 **Swift Concurrency** 가 언어 레벨에서 대체하고 있습니다.

#### Combine → AsyncSequence 대응표

| Combine | AsyncSequence | 비고 |
|---------|---------------|------|
| `Publisher` | `AsyncSequence` | 프로토콜 |
| `sink { }` | `for await value in … { }` | 구독/소비 |
| `map`, `filter` | `.map { }`, `.filter { }` (그대로) | 내장 연산자 |
| `PassthroughSubject` | `AsyncStream` | 수동 이벤트 발행 |
| `CurrentValueSubject` | `AsyncStream` + 초기값 | 현재 값 보유 |
| `combineLatest`, `merge` | `AsyncAlgorithms` 패키지 | Apple 공식 |

#### 실전 예시: NotificationCenter 스트림

```swift
// Before: Combine
NotificationCenter.default.publisher(for: UIApplication.didBecomeActiveNotification)
    .sink { _ in print("Active") }
    .store(in: &cancellables)

// After: AsyncSequence (iOS 15+)
for await _ in NotificationCenter.default.notifications(named: UIApplication.didBecomeActiveNotification) {
    print("Active")
}
```

#### 실전 예시: 커스텀 이벤트 스트림

```swift
// Before: PassthroughSubject
let subject = PassthroughSubject<Location, Never>()
subject.send(newLocation)

// After: AsyncStream
let (stream, continuation) = AsyncStream.makeStream(of: Location.self)
continuation.yield(newLocation)       // 값 발행
continuation.finish()                  // 스트림 종료

// 소비
for await location in stream {
    updateMap(location)
}
```

>[!TIP] **언제 여전히 Combine 을 써야 하나?**
> 1. **`debounce`, `throttle`, `combineLatest` 등 복잡한 시간 기반 연산**: `swift-async-algorithms` 패키지가 일부를 지원하지만 아직 Combine 만큼 성숙하지 않습니다.
> 2. **에러 타입이 있는 스트림**: `AsyncThrowingStream` 은 에러 타입을 특정할 수 없지만(`any Error`), Combine 의 `Publisher<Output, MyError>` 는 가능합니다.
> 3. **iOS 14 이하 지원**: AsyncSequence 는 iOS 15+ 입니다.

### 더 보기

- [[apple-swift-concurrency]] - 비동기 작업의 또 다른 축 (단발성 작업)
- [[apple-observation-framework]] - Combine 의 ViewModel 역할을 대체하는 @Observable
- [[apple-uikit-lifecycle]] - MVVM 패턴과 Combine 의 결합
