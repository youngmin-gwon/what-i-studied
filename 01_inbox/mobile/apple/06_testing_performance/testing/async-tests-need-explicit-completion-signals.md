---
title: async-tests-need-explicit-completion-signals
tags: [apple, apple/testing, apple/testing/testing, async, concurrency, testing]
aliases: ["비동기 테스트는 완료 신호를 명시해야 하며 sleep 으로 기다리면 안 된다", "XCTestExpectation", "async test", "비동기 테스트"]
date modified: 2026-09-03 00:00:00 +09:00
date created: 2026-09-03 00:00:00 +09:00
---

## 비동기 테스트는 완료 신호를 명시해야 하며 sleep 으로 기다리면 안 된다

### 개념 (What)

동기 테스트는 함수가 반환하면 끝난다. 비동기 작업은 **함수가 반환한 뒤에도 계속 돌기 때문에**, 테스트 러너에게 "언제 끝났는지"를 알려줘야 한다.

방법은 세 가지이며, 어느 것을 쓰느냐는 **테스트 대상이 무엇을 노출하느냐**로 정해진다.

| 대상 | 방법 |
| :--- | :--- |
| `async` 함수 | **테스트 함수를 `async` 로** — 가장 단순 |
| 콜백 기반 API | `XCTestExpectation` 또는 `withCheckedContinuation` |
| `AsyncSequence` / 스트림 | `for await` 로 필요한 개수만 수집 |
| Combine `Publisher` | expectation + `sink` |

### 왜 필요한가 (Why)

```swift
// ❌ 가장 흔하고 가장 나쁜 패턴
func testLoad() {
    viewModel.load()
    Thread.sleep(forTimeInterval: 2)        // 느리고, 그래도 간헐적으로 실패한다
    XCTAssertEqual(viewModel.items.count, 3)
}
```

`sleep` 은 **두 방향으로 틀린다.** 빠른 기기에서는 불필요하게 느리고, 느린 CI 에서는 여전히 부족하다. 전형적인 [플레이키 테스트](flaky-tests-come-from-shared-state-and-timing.md)의 원인이다.

### 1. async 함수는 그냥 await 한다

```swift
// Swift Testing
@Test func loadsItems() async throws {
    let vm = ViewModel(api: StubAPI(items: [.sample, .sample, .sample]))
    await vm.load()
    #expect(vm.items.count == 3)
}

// XCTest
func testLoadsItems() async throws {
    let vm = ViewModel(api: StubAPI())
    await vm.load()
    XCTAssertEqual(vm.items.count, 3)
}
```

**대부분의 경우 이것으로 충분하다.** 프로덕션 코드를 async 로 만들면 테스트가 단순해진다.

### 2. 콜백 API 는 expectation 또는 continuation

```swift
// XCTest — expectation
func testLegacyCallback() async throws {
    let expectation = XCTestExpectation(description: "콜백 도착")
    var received: Data?

    legacyAPI.fetch { data, _ in
        received = data
        expectation.fulfill()
    }
    await fulfillment(of: [expectation], timeout: 2)   // async 버전
    XCTAssertNotNil(received)
}

// Swift Testing — continuation 으로 감싸는 편이 자연스럽다
@Test func legacyCallback() async throws {
    let data: Data = try await withCheckedThrowingContinuation { c in
        legacyAPI.fetch { data, error in
            if let error { c.resume(throwing: error) } else { c.resume(returning: data!) }
        }
    }
    #expect(!data.isEmpty)
}
```

> [!WARNING] `fulfill()` 은 정확히 한 번
> 두 번 호출하면 실패하고, 한 번도 안 하면 타임아웃이다. `expectedFulfillmentCount` 로 횟수를 명시하거나, `assertForOverFulfill = false` 로 완화할 수 있다.

### 3. 스트림은 필요한 개수만 수집한다

```swift
@Test func emitsThreeStates() async throws {
    var states: [State] = []
    for await state in viewModel.stateStream {
        states.append(state)
        if states.count == 3 { break }      // ★ break 하지 않으면 영원히 기다린다
    }
    #expect(states == [.loading, .loaded, .idle])
}
```

무한 스트림에서 `break` 를 빠뜨리면 타임아웃까지 매달린다. **몇 개를 기대하는지 명시**한다.

### 시간에 의존하는 코드는 시계를 주입한다

```swift
// ❌ 실제 시간을 기다린다 — 테스트가 5초 걸린다
func debounce() async {
    try? await Task.sleep(for: .seconds(5))
    performSearch()
}

// ✅ 시계를 주입해 테스트에서 즉시 진행시킨다
struct Debouncer<C: Clock> {
    let clock: C
    func run() async {
        try? await clock.sleep(for: .seconds(5))
        performSearch()
    }
}

@Test func debounces() async {
    let clock = TestClock()                 // 가상 시계
    let d = Debouncer(clock: clock)
    async let run: () = d.run()
    await clock.advance(by: .seconds(5))    // 즉시 5초 진행
    await run
    #expect(searchCalled)
}
```

**타이머·디바운스·재시도 백오프**를 테스트하려면 이 패턴이 사실상 필수다.

### MainActor 격리와 테스트

```swift
@MainActor
@Test func updatesUIState() async {
    let vm = ViewModel()            // @MainActor 격리된 타입
    await vm.load()
    #expect(vm.title == "완료")     // await 없이 접근 가능
}
```

[`@MainActor` 로 격리된 타입](../../01_language_concurrency/concurrency/mainactor-and-nonisolated.md)을 테스트하려면 테스트도 `@MainActor` 로 두는 것이 간결하다.

### 관찰 가능한 증거

```bash
# 느린 테스트 찾기 — sleep 이 숨어 있는 곳이 드러난다
xcrun xcresulttool get --path TestResults.xcresult --format json \
  | jq '.. | objects | select(.duration) | {name: .identifier._value, dur: .duration._value}' \
  | sort -k2 -rn | head -20
```

```bash
# 코드베이스에서 sleep 사용처 전수 확인
grep -rn "Thread.sleep\|sleep(" --include="*.swift" ./Tests
```

**CI 에서 테스트 실행 시간이 갑자기 늘었다면** 누군가 `sleep` 을 추가한 것이다.

### 연관 문서

- [Swift Testing 과 XCTest 는 공존하며 역할이 다르다](xctest-and-swift-testing-coexist.md)
- [플레이키 테스트는 공유 상태와 타이밍에서 나온다](flaky-tests-come-from-shared-state-and-timing.md)
- [await 는 스레드를 막지 않고 continuation 을 힙에 저장한다](../../01_language_concurrency/concurrency/await-suspension-stores-continuation.md)
- [구조적 동시성은 작업 수명을 스코프에 묶는다](../../01_language_concurrency/concurrency/structured-concurrency-task-tree.md)

공식 문서: [Testing asynchronous code](https://developer.apple.com/documentation/xctest/asynchronous_tests_and_expectations)
