---
title: apple-gcd-deep-dive
tags: [apple, concurrency, gcd, internals, performance]
aliases: []
date modified: 2026-04-05 12:22:20 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## GCD (Grand Central Dispatch) Deep Dive

>[!CAUTION] **Devil's Advocate : 이제는 놓아주어야 할 레거시(Legacy)**
>GCD(libdispatch)는 오랫동안 훌륭한 도구였지만, 최근의 Swift 6 환경의 엄격한 동시성(Strict Concurrency) 패러다임 하에서 **비지니스 로직 작성 시엔 사용을 피해야 하는 레거시**입니다.
> 1. Thread Explosion 문제의 근본적 컨트롤 불가능.
> 2. 콜백 큐 점프 과정의 데이터 레이스를 방지하지 못함.
> 3. Swift 컴파일러의 Concurrency Check 기능을 우회함.
>이하 내용은 레거시(Objective-C 및 구형 Swift) 코드를 유지보수하기 위한 목적으로만 참고되어야 합니다. 신규 코드는 `Swift Concurrency (async/await, Actor)` 를 우선해야 합니다.

### 💡 왜 아직도 이것을 알아야 하나요? (Context)

- **Legacy Code**: 2021 년 이전에 작성된 거의 모든 iOS 앱은 GCD 를 사용합니다. 유지보수를 위해 피할 수 없습니다.
- **Low-Level Control**: "특정 스레드에 작업을 꽂아넣기", "정확히 0.3 초 뒤에 실행하기", "반복 작업 동기화" 등은 아직도 GCD 가 가장 직관적일 때가 있습니다.
- **Under the Hood**: Swift Concurrency(`Executor`)도 내부적으로 GCD 큐를 사용할 수 있습니다.

---

### 📚 외부 리소스 및 참고 자료

#### 공식 문서 및 소스 코드

- [Apple Open Source - libdispatch](https://github.com/apple/swift-corelibs-libdispatch) - GCD 는 오픈소스입니다! C 로 짜여진 내부 구현을 볼 수 있습니다.
- [Dispatch Documentation](https://developer.apple.com/documentation/dispatch)

#### 🎥 WWDC 세션

- [WWDC 2015: Building Responsive and Efficient Apps with GCD](https://developer.apple.com/videos/play/wwdc2015/718) - QoS 개념 도입
- [WWDC 2017: Modernizing Grand Central Dispatch Usage](https://developer.apple.com/videos/play/wwdc2017/706) - 스레드 폭발(Thread Explosion) 문제와 해결책

---

### 🔍 GCD Internals

#### 1. Work Stealing & Overcommit

- **ThreadPool**: GCD 는 시스템 전역 스레드 풀을 관리합니다.
- **Work Stealing**: 큐가 비어있는 스레드는 바쁜 스레드의 큐에서 작업을 훔쳐와 실행 효율을 높입니다.
- **Overcommit**: 메인 스레드나 일부 특수 상황에서는 시스템 부하와 상관없이 강제로 스레드를 생성(Overcommit)하여 데드락을 방지합니다.

#### 2. Thread Explosion (스레드 폭발)

GCD 의 가장 큰 단점입니다. `DispatchQueue.global().async` 를 100 번 호출하면서 내부에서 `sleep`(Block)을 걸면, GCD 는 100 개의 스레드를 생성해버립니다. 이는 컨텍스트 스위칭 오버헤드와 메모리 부족을 야기합니다.

👉 **해결책**: `DispatchSemaphore` 로 동시 실행 수를 제한하거나, Swift Concurrency 로 마이그레이션하세요.

---

### 🛠️ 고급 패턴 (Advanced Patterns)

#### 1. Barrier: Reader-Writer Lock 구현 (🚧 대안: `Actor`)

여러 스레드가 읽는 건 괜찮지만, 쓸 때는 혼자만 써야 할 때 사용합니다. 현대 Swift 에서는 동일한 역할을 보일러플레이트 없이 안전하게 수행하는 `actor` 로 대체합니다.

```swift
class ThreadSafeCache {
    private let queue = DispatchQueue(label: "com.cache", attributes: .concurrent)
    private var data: [String: Any] = [:]
    
    // Reader: 동시에 접근 가능 (.concurrent)
    func get(_ key: String) -> Any? {
        queue.sync { 
            return data[key] 
        }
    }
    
    // Writer: 혼자만 접근 가능 (.barrier)
    func set(_ key: String, value: Any) {
        queue.async(flags: .barrier) {
            self.data[key] = value
        }
    }
}
```

#### 2. DispatchGroup: 여러 작업 기다리기 (🚧 대안: `TaskGroup` 또는 `async let`)

과거에는 여러 비동기 호출이 끝나기를 기다릴 때 `DispatchGroup` 을 썼으나 완료 전에 `leave()` 를 빠뜨리는 등의 실수가 잦았습니다. 현재는 `TaskGroup` 배열 반환이나 구조적 동시성(Structured Concurrency)을 활용합니다.

```swift
let group = DispatchGroup()

// 작업 1
group.enter()
api.fetchUser { 
    print("User fetched")
    group.leave() 
}

// 작업 2
group.enter()
api.fetchIcon { 
    print("Icon fetched")
    group.leave() 
}

// 완료 통지
group.notify(queue: .main) {
    print("All tasks finished")
}
```

#### 3. DispatchSemaphore: 동시성(Concurrency) 수 제한 (🚧 대안: `withCheckedContinuation` / Custom Semaphore Actor)

네트워크 요청이 한 번에 3 개까지만 나가도록 제한하고 싶을 때 유용합니다. 하지만 `Semaphore` 는 대기하는 동안 스레드를 Block 하므로 스레드 폭발을 야기합니다. Swift Concurrency 에서는 세마포어 대신 동시성을 제어하는 액터 혹은 작업 풀 관리를 사용하는 편이 올바릅니다.

```swift
let sema = DispatchSemaphore(value: 3) // 티켓 3장

for url in urls {
    DispatchQueue.global().async {
        sema.wait() // 티켓 획득 (없으면 대기)
        download(url)
        sema.signal() // 티켓 반납
    }
}
```

---

### ⚠️ 주의사항 (Troubleshooting)

#### Sync on Main Thread (Deadlock)

메인 스레드에서 메인 큐로 `sync` 를 쏘면 앱이 즉시 멈춥니다.

메인 스레드는 작업을 기다리고(`sync`), 큐도 메인 스레드가 비길 기다리는 상황이 되기 때문입니다.

```swift
// ❌ 절대 금지
DispatchQueue.main.sync {
    // 이미 메인 스레드인데 또 메인 큐를 기다림 -> 데드락
}
```

### 더 보기

- [apple-swift-concurrency](apple-swift-concurrency.md) - GCD 의 현대적 대안
- [apple-operation-queue](apple-operation-queue.md) - GCD 기반의 객체지향 래퍼 (의존성 관리 가능)
