---
title: apple-swift-concurrency
tags: [apple, swift, concurrency, async-await, actor, internals]
aliases: []
date modified: 2025-12-17 17:40:00 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Swift Concurrency Deep Dive

Swift 5.5부터 도입된, 언어 차원에서 보장하는 **안전하고(Safe)**, **구조적인(Structured)** 비동기 프로그래밍 모델입니다.
단순히 `async/await` 문법을 쓰는 것을 넘어, **Actor Isolation**과 **Sendable Check** 가 어떻게 데이터 경합(Data Race)을 컴파일 타임에 막아주는지 알아봅니다.

### 💡 왜 이것을 알아야 하나요? (Why it matters)
- **콜백 지옥 탈출**: 중첩된 클로저(`completion handler`) 때문에 읽기 힘들었던 코드를, 동기 코드처럼 위에서 아래로 읽을 수 있게 해줍니다.
- **실수 방지**: "이거 메인 스레드에서 돌려야 하나?" 고민할 필요가 없습니다. `@MainActor`를 붙이면 컴파일러가 알아서 체크해줍니다.
- **성능 (Thread Explosion 방지)**: 기존 GCD는 블로킹 작업이 많으면 스레드를 수백 개씩 만들어 앱을 멈추게 했지만, Swift Concurrency는 코어 개수만큼만 스레드를 유지하며 효율적으로 일합니다.

---

### 🔍 내부 동작 원리 (Internals)

#### 1. Cooperative Thread Pool (협력적 스레드 풀)
GCD는 블로킹 작업 시 스레드를 계속 생성(Thread Explosion)하지만, Swift Concurrency는 **CPU 코어 수에 맞춘 고정된 크기의 스레드 풀**을 유지합니다.
- **Continuation**: `await`를 만나면 현재 작업의 상태(Continuation)를 힙에 저장하고 스레드를 다른 작업에 양보(Yield)합니다. 스레드는 멈추지 않고 다른 일을 하러 갑니다.
- **Context Switching 비용 감소**: OS 스레드 컨텍스트 스위칭(무거움) 대신, 런타임 레벨에서 가벼운 작업 전환이 일어납니다.

#### 2. Actor Isolation (액터 격리)
Actor는 한 번에 하나의 작업(Task)만 자신의 가변 상태(Mutable State)에 접근하도록 보장하는 참조 타입입니다. **"스레드 안전한 클래스"**라고 생각하면 됩니다.
- **Mailbox**: Actor 내부에 메시지 큐(Mailbox)가 있어, 비동기 호출(`await`)들이 순차적으로 처리됩니다.
- **Reentrancy (재진입성)**: Actor 메서드 실행 중 `await`로 실행을 중단하면, 그 사이 다른 작업이 Actor에 진입할 수 있습니다. 이는 데드락을 방지하지만, 상태 불일치(State Inconsistency) 가능성을 엽니다.

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

#### 1. @MainActor와 UI 업데이트
UI 관련 클래스(UIView, UIViewController)는 이미 `@MainActor`로 격리되어 있습니다. 비동기 작업 후 UI를 고칠 때 `DispatchQueue.main.async` 대신 이렇게 씁니다.

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
"이 데이터는 스레드를 건너뛰어도 안전한가?"를 컴파일러에게 알려줍니다.
- **Value Type** (Struct, Enum)은 멤버가 Sendable이면 자동 준수.
- **Actor**는 내부 동기화가 있으므로 Sendable.
- **Class**는 `final`이고 불변(immutable) 상태만 가져야 Sendable 가능. (아니면 `@unchecked Sendable`로 수동 보증해야 함)

```swift
// ❌ 컴파일 경고: Class는 기본적으로 Sendable 아님
class MutableData { var x = 0 }

// ✅ Sendable 준수
final class ImmutableData: Sendable {
    let x: Int
    init(x: Int) { self.x = x }
}
```

#### 3. TaskLocal (Thread Local의 대안)
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

### 📚 외부 리소스
- **[Swift Concurrency Documentation](../../../../https:/docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/.md)**: 공식 문서.
- **[WWDC 2021: Swift concurrency: Behind the scenes](../../../../https:/developer.apple.com/videos/play/wwdc2021/10254/.md)**: 내부 스레딩 모델을 이해하려면 필수.

### 더 보기
- [apple-gcd-deep-dive](apple-gcd-deep-dive.md) - 기존 GCD와의 차이점
- [apple-combine-framework](../03_data_networking/apple-combine-framework.md) - 비동기 "스트림" 처리에는 Combine/AsyncSequence가 유리함
