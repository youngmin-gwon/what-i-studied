---
title: apple-swift-concurrency
tags: [apple, swift, async, concurrency, actor]
aliases: []
date modified: 2025-12-16 17:01:32 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Swift Concurrency apple swift async concurrency actor

Swift 의 구조화된 동시성. 기본은 [[apple-runtime-and-swift]] 참고.

### async/await

비동기 함수를 동기 코드처럼 작성.

```swift
func fetchUser(id: Int) async throws -> User {
    let url = URL(string: "https://api.example.com/users/\(id)")!
    let (data, _) = try await URLSession.shared.data(from: url)
    return try JSONDecoder().decode(User.self, from: data)
}

// 호출
Task {
    do {
        let user = try await fetchUser(id: 1)
        print(user.name)
    } catch {
        print("Error: \(error)")
    }
}
```

### Task

비동기 작업 단위.

```swift
// 기본 Task
let task = Task {
    let result = await performWork()
    return result
}

let result = await task.value

// 취소
task.cancel()

// 취소 확인
Task {
    for i in 0..<1000 {
        if Task.isCancelled {
            print("Cancelled")
            return
        }
        await doWork(i)
    }
}
```

### TaskGroup

여러 작업 병렬 실행.

```swift
func fetchMultipleUsers(ids: [Int]) async throws -> [User] {
    try await withThrowingTaskGroup(of: User.self) { group in
        for id in ids {
            group.addTask {
                try await fetchUser(id: id)
            }
        }
        
        var users: [User] = []
        for try await user in group {
            users.append(user)
        }
        return users
    }
}
```

### Actor

데이터 격리로 경쟁 상태 방지.

```swift
actor Counter {
    private var value = 0
    
    func increment() {
        value += 1
    }
    
    func getValue() -> Int {
        return value
    }
}

let counter = Counter()

Task {
    await counter.increment()
    let value = await counter.getValue()
    print(value)
}
```

### MainActor

메인 스레드에서 실행 보장.

```swift
@MainActor
class ViewModel: ObservableObject {
    @Published var items: [Item] = []
    
    func loadItems() async {
        // 자동으로 메인 스레드에서 실행
        items = await fetchItems()
    }
}

// 함수 단위
@MainActor
func updateUI() {
    // UI 업데이트
}
```

### 더 보기

[[apple-gcd-deep-dive]], [[apple-combine-framework]], [[apple-runtime-and-swift]]
