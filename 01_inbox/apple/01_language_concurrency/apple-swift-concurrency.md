---
title: apple-swift-concurrency
tags: [actor, apple, async-await, concurrency, internals, swift]
aliases: []
date modified: 2026-04-03 18:54:44 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Swift Concurrency Deep Dive

## Swift Concurrency Deep Dive

Swift 5.5부터 도입되어 **Swift 6에서 완전한 Data-Race Safety(엄격한 동시성 검사)**를 통해 완성된 비동기 프로그래밍 모델입니다. 컴파일러가 언어 차원에서 **안전하고(Safe)**, **구조적인(Structured)** 동시성을 보장합니다.

단순히 `async/await` 문법을 쓰는 것을 넘어, **Actor Isolation**과 **Sendable Check** 가 어떻게 데이터 경합(Data Race)을 **컴파일 타임 에러**로 막아주는지 알아봅니다.

### 💡 왜 이것을 알아야 하나요? (Why it matters)
- **콜백 지옥 탈출**: 중첩된 클로저(`completion handler`) 때문에 읽기 힘들었던 코드를, 동기 코드처럼 위에서 아래로 읽을 수 있게 해줍니다.
- **실수 방지**: "이거 메인 스레드에서 돌려야 하나?" 고민할 필요가 없습니다. `@MainActor` 를 붙이면 컴파일러가 알아서 체크해줍니다.
- **성능 (Thread Explosion 방지)**: 기존 GCD 는 블로킹 작업이 많으면 스레드를 수백 개씩 만들어 앱을 멈추게 했지만, Swift Concurrency 는 코어 개수만큼만 스레드를 유지하며 효율적으로 일합니다.

---

### 🔍 내부 동작 원리 (Internals)

#### 1. Cooperative Thread Pool (협력적 스레드 풀)

GCD 는 블로킹 작업 시 스레드를 계속 생성(Thread Explosion)하지만, Swift Concurrency 는 **CPU 코어 수에 맞춘 고정된 크기의 스레드 풀**을 유지합니다.

- **Continuation**: `await` 를 만나면 현재 작업의 상태(Continuation)를 힙에 저장하고 스레드를 다른 작업에 양보(Yield)합니다. 스레드는 멈추지 않고 다른 일을 하러 갑니다.
- **Context Switching 비용 감소**: OS 스레드 컨텍스트 스위칭(무거움) 대신, 런타임 레벨에서 가벼운 작업 전환이 일어납니다.

#### 2. Actor Isolation (액터 격리)

Actor 는 한 번에 하나의 작업(Task)만 자신의 가변 상태(Mutable State)에 접근하도록 보장하는 참조 타입입니다. **"스레드 안전한 클래스"**라고 생각하면 됩니다.

- **Mailbox**: Actor 내부에 메시지 큐(Mailbox)가 있어, 비동기 호출(`await`)들이 순차적으로 처리됩니다.
- **Reentrancy (재진입성)**: Actor 메서드 실행 중 `await` 로 실행을 중단하면, 그 사이 다른 작업이 Actor 에 진입할 수 있습니다. 이는 데드락을 방지하지만, 상태 불일치(State Inconsistency) 가능성을 엽니다.

```swift
actor UserCache {
    var users: [String: User] = [:]
    
    func getUser(id: String) async -> User? {
        if let cached = users[id] { return cached }
        
        // 주의: 여기서 await 하는 동안 다른 작업이 getUser를 호출할 수 있음! (Reentrancy)
        let user = await fetchRemote(id)
        
        users[id] = user
        return user
    }
}
```

---

### Structured Concurrency (구조적 동시성)

"작업의 수명이 스코프({})를 벗어나지 않는다"는 원칙입니다.

부모 작업이 취소되면 자식 작업도 자동으로 취소되고, 모든 자식이 끝날 때까지 부모는 리턴하지 않습니다.

```swift
func processImages(ids: [String]) async throws -> [UIImage] {
    // TaskGroup 사용
    // withThrowingTaskGroup은 에러 발생 시 형제 작업(Sibling Tasks)들을 자동 취소함.
    return try await withThrowingTaskGroup(of: UIImage.self) { group in
        for id in ids {
            group.addTask {
                return try await fetchImage(id) // 자식 태스크 생성
            }
        }
        
        var images: [UIImage] = []
        for try await image in group {
            images.append(image)
        }
        return images
    }
}
```

---

### 🛡️ 실무 패턴 및 주의사항

#### 1. @MainActor 와 UI 업데이트

UI 관련 클래스(UIView, UIViewController)는 이미 `@MainActor` 로 격리되어 있습니다. 비동기 작업 후 UI 를 고칠 때 `DispatchQueue.main.async` 대신 이렇게 씁니다.

```swift
class MyViewModel: ObservableObject {
    @Published var data: String = ""
    
    func loadData() async {
        let result = await api.fetch()
        await updateData(result) // MainActor 함수 호출
    }
    
    @MainActor
    func updateData(_ val: String) {
        self.data = val
    }
}
```

#### 2. Sendable 프로토콜

"이 데이터는 스레드를 건너뛰어도 안전한가?"를 컴파일러에게 확증(Guarantee)하는 프로토콜입니다. **Swift 6 모드에서는 Sendable하지 않은 타입을 동시성 도메인(Actor나 Task) 바깥으로 넘기는 동작이 경고가 아닌 컴파일 에러가 됩니다.**

- **Value Type** (Struct, Enum)은 멤버가 Sendable 이면 자동 준수.
- **Actor**는 내부 동기화가 있으므로 Sendable.
- **Class**는 `final` 이고 불변(immutable) 상태만 가져야 Sendable 가능. (아니면 `@unchecked Sendable` 로 수동 락(Lock) 관리를 보증해야 함)

```swift
// ❌ 컴파일 에러 (Swift 6): Class는 기본적으로 Sendable 아님
class MutableData { var x = 0 }

// ✅ Sendable 준수
final class ImmutableData: Sendable {
    let x: Int
    init(x: Int) { self.x = x }
}
```

#### 3. TaskLocal (Thread Local 의 대안)

Task 계층 구조를 따라 값을 전파하고 싶을 때 사용 (예: Request ID, Trace ID).

```swift
enum RequestContext {
    @TaskLocal static var requestID: String?
}

func handleRequest() async {
    await RequestContext.$requestID.withValue("req_123") {
        await process() // 내부에서 RequestContext.requestID 접근 가능
    }
}
```

---

### 🆕 Swift 6 Strict Concurrency (Complete Concurrency Checking)

Swift 6 에서는 Strict Concurrency 가 **기본 활성화**됩니다. 데이터 레이스를 **컴파일 타임**에 잡아내어 런타임 버그를 원천 차단합니다.

#### 1. Region-Based Isolation (SE-0414)

컴파일러가 값의 "격리 영역(Region)"을 추적하여, `Sendable` 하지 않은 값도 **안전하게 전송할 수 있는지** 자동으로 판단합니다.

```swift
// Swift 6 이전: 에러! MyClass 는 Sendable 아님
// Swift 6: 컴파일러가 "이 값은 더 이상 원래 도메인에서 사용되지 않음"을 증명 → OK
class MyClass { var value = 0 }

func example() async {
    let obj = MyClass()          // 여기서 생성
    await someActor.process(obj) // obj 가 여기로 "전송"됨
    // obj 를 여기서 다시 쓰지 않으므로 안전 → 컴파일 성공
}
```

이 분석 덕분에 `@Sendable` 보일러플레이트가 크게 줄어듭니다.

#### 2. `sending` 키워드 (SE-0430)

소유권 이전(Ownership Transfer)을 **명시적으로** 선언합니다.

```swift
// sending: "이 값의 소유권을 넘기겠다"
func processInBackground(sending data: MyClass) async {
    // 호출자는 이 함수 호출 이후 data 에 접근할 수 없음
    await actor.handle(data)
}

// 반환값에도 사용 가능
func createConfig() -> sending Config {
    Config() // 반환 후 이 함수 내에서는 더 이상 접근 불가
}
```

**`Sendable` vs `sending`**:
- `Sendable`: 타입 자체가 스레드 안전함을 **보장** (불변 또는 내부 동기화)
- `sending`: 특정 값의 **소유권을 이전**하여 안전하게 전달 (타입이 Sendable 이 아니어도 가능)

#### 3. `nonisolated` & `@MainActor` 분리 전략

```swift
@MainActor
class ViewController {
    var title: String = ""
    
    // 이 메서드는 메인 스레드 밖에서도 호출 가능
    nonisolated func computeHash() -> String {
        // self.title 접근 불가 (격리 위반)
        return "hash_value"
    }
}
```

**마이그레이션 팁**: Swift 5 → 6 전환 시 `Build Settings` > `Strict Concurrency Checking` 을 `Complete` 로 설정하여 경고를 먼저 확인하세요.

### 📚 외부 리소스
- **[Swift Concurrency Documentation](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)**: 공식 문서.
- **[WWDC 2021: Swift concurrency: Behind the scenes](https://developer.apple.com/videos/play/wwdc2021/10254/)**: 내부 스레딩 모델을 이해하려면 필수.

### ⚡️ Coroutines (Android) vs Swift Concurrency (iOS)

두 플랫폼 모두 "함수 실행을 일시 중단하고 나중에 재개"하는 개념을 공유하지만, 철학적 차이가 있습니다.

| 특징 | Kotlin Coroutines | Swift Concurrency |
| :--- | :--- | :--- |
| **핵심 키워드** | `suspend`, `launch`, `async` | `async`, `await`, `task` |
| **스레드 전환** | `withContext(Dispatchers.IO)` (명시적) | `actor` / `@MainActor` (격리 기반 자동 전환) |
| **데이터 경합** | 개발자가 주의 (MutableStateFlow 등 활용) | **컴파일 타임 차단** (Sendable, Actor Isolation) |
| **비동기 스트림** | `Flow` (Cold), `StateFlow` (Hot) | `AsyncSequence`, `AsyncStream` |
| **취소 전파** | Structured Concurrency (Job hierarchy) | Task hierarchy & Cooperative cancellation |

> [!TIP] **Android 개발자를 위한 Swift Concurrency**
> - `viewModelScope.launch` ≃ `Task { ... }` (MainActor 에서 실행 시)
> - `withContext(Dispatchers.IO)` ≃ `Task.detached { ... }` 또는 `nonisolated` 메서드 활용
> - `Flow.collect` ≃ `for await in sequence`
> 상세 비교는 [android-coroutines-flow](../../android/02_app_framework/android-coroutines-flow.md)를 참고하세요.

### 더 보기
- [apple-gcd-deep-dive](apple-gcd-deep-dive.md) - 기존 GCD 와의 차이점
- [apple-observation-framework](apple-observation-framework.md) - Actor 와 @Observable 의 결합
- [apple-combine-framework](../03_data_networking/apple-combine-framework.md) - 비동기 "스트림" 처리에는 AsyncSequence 가 유리함

