---
title: migrating-to-asyncsequence-changes-the-cancellation-model
tags: [apple, apple/data, apple/data/combine, asyncsequence, combine, migration]
aliases: ["AsyncSequence 는 Combine 의 스트림 역할을 대체하며 취소가 구독 해제 대신 Task 트리를 탄다", "AsyncSequence", "AsyncStream", "Combine 마이그레이션"]
date modified: 2026-09-03 00:00:00 +09:00
date created: 2026-09-03 00:00:00 +09:00
---

## AsyncSequence 는 Combine 의 스트림 역할을 대체하며 취소가 구독 해제 대신 Task 트리를 탄다

### 개념 (What)

Apple 은 Combine 이 하던 "시간에 따른 비동기 값 스트림" 역할을 **언어 기본 기능인 `AsyncSequence`** 로 옮기는 방향을 명확히 하고 있다. SwiftUI 의 `@Published` 가 `@Observable` 로 대체된 것과 같은 흐름이다.

두 모델의 결정적 차이는 **취소가 어디에 걸리는가**다.

| | Combine | AsyncSequence |
| :--- | :--- | :--- |
| 수명 관리 | `AnyCancellable` 을 [수동으로 보관](anycancellable-lifetime-gates-the-pipeline.md) | [Task 트리에 자동 귀속](../../01_language_concurrency/concurrency/structured-concurrency-task-tree.md) |
| 취소 시점 | `AnyCancellable` 해제 시 | 상위 Task 취소 시 자동 전파 |
| 구독 누락 버그 | **가능** (저장 안 하면 조용히 취소) | **구조적으로 어려움** |

### 왜 필요한가 (Why)

Combine 의 가장 흔한 버그가 [`AnyCancellable` 저장 누락](anycancellable-lifetime-gates-the-pipeline.md)이었다. `AsyncSequence` 는 `for await` 문 자체가 실행 흐름이므로, **저장을 깜빡해서 조용히 취소되는 경우가 원리적으로 없다.** 대신 [`.task` 가 뷰 수명에 자동으로 묶인다](../../02_ui_frameworks/swiftui/task-modifier-ties-async-to-view-lifetime.md).

### 대응표

| Combine | AsyncSequence | 비고 |
| :--- | :--- | :--- |
| `Publisher` | `AsyncSequence` | 프로토콜 |
| `sink { }` | `for await value in ... { }` | 구독/소비 |
| `map`, `filter` | `.map { }`, `.filter { }` | 그대로 존재 |
| `PassthroughSubject` | `AsyncStream` | 수동 이벤트 발행 |
| `CurrentValueSubject` | `AsyncStream` + 초기값 보관 | 현재 값 유지 |
| `combineLatest`, `merge`, `debounce` | `swift-async-algorithms` 패키지 | Apple 공식, 일부만 성숙 |
| `AnyCancellable.store(in:)` | (불필요) | Task 트리가 대신함 |

### 실전 변환 예시

**NotificationCenter 스트림**

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

**커스텀 이벤트 발행**

```swift
// Before: PassthroughSubject
let subject = PassthroughSubject<Location, Never>()
subject.send(newLocation)

// After: AsyncStream
let (stream, continuation) = AsyncStream.makeStream(of: Location.self)
continuation.yield(newLocation)      // 값 발행
continuation.finish()                // 스트림 종료

for await location in stream { updateMap(location) }
```

### switchToLatest 는 .task(id:) 로

Combine 에서 [`switchToLatest` 로 검색 취소를 구현](flatmap-family-implements-different-merge-strategies.md)하던 패턴은, SwiftUI 에서는 `.task(id:)` 로 더 짧게 표현된다.

```swift
// AsyncSequence + SwiftUI 조합 — 이전 검색 자동 취소
.task(id: query) {
    try? await Task.sleep(for: .milliseconds(500))   // 디바운스
    guard !Task.isCancelled else { return }
    results = try? await api.search(query)
}
```

`query` 가 바뀌면 이전 `.task` 가 자동 취소되고 새로 시작한다. `switchToLatest` 를 명시적으로 쓸 필요가 없다.

### 여전히 Combine 이 나은 경우

| 상황 | 이유 |
| :--- | :--- |
| **복잡한 시간 기반 연산 조합** | `debounce` + `combineLatest` + `removeDuplicates` 를 함께 쓰는 파이프라인은 `swift-async-algorithms` 가 아직 완전히 대체하지 못한다 |
| **에러 타입이 명확해야 함** | `Publisher<Output, MyError>` 는 에러 타입을 특정하지만, `AsyncThrowingStream` 은 `any Error` 로 지워진다 |
| **iOS 14 이하 지원** | `AsyncSequence` 는 iOS 15+ |
| **기존 대형 Combine 파이프라인** | 전면 재작성 비용이 이득보다 클 수 있음 |

**새 코드는 AsyncSequence, 위 조건에 해당하는 기존 코드는 유지**가 실무적인 기준이다. 전체를 한 번에 마이그레이션할 필요는 없다 — 두 모델은 같은 프로젝트에서 공존할 수 있다.

### 관찰 가능한 증거

```swift
// AsyncSequence 로 옮긴 뒤 취소가 실제로 전파되는지 확인
.task {
    defer { print("스트림 종료됨") }   // 취소 시에도 실행된다
    for await value in stream { process(value) }
}
```

**Instruments의 Swift Concurrency** 템플릿으로 Task 의 생성·취소가 예상대로 일어나는지 확인한다. Combine 쪽은 [Memory Graph](../../06_testing_performance/debugging/view-debugger-and-memory-graph-answer-different-questions.md)로 `AnyCancellable` 잔존 여부를 확인한다.

### 연관 문서

- [AnyCancellable 을 보관하지 않으면 구독이 즉시 해제된다](anycancellable-lifetime-gates-the-pipeline.md)
- [구조적 동시성은 작업 수명을 스코프에 묶고 취소를 트리로 전파한다](../../01_language_concurrency/concurrency/structured-concurrency-task-tree.md)
- [.task 는 비동기 작업의 수명을 뷰 수명에 묶고 사라질 때 자동 취소한다](../../02_ui_frameworks/swiftui/task-modifier-ties-async-to-view-lifetime.md)

공식 문서: [AsyncSequence](https://developer.apple.com/documentation/swift/asyncsequence) · [swift-async-algorithms](https://github.com/apple/swift-async-algorithms)
