---
title: apple-gcd-deep-dive
tags: [apple, gcd, concurrency, performance, internals]
aliases: []
date modified: 2025-12-17 17:50:00 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## GCD (Grand Central Dispatch) Deep Dive

Swift Concurrency가 나왔지만, **GCD(libdispatch)** 는 여전히 Apple 플랫폼 동시성의 **기반(Foundation)** 입니다.
레거시 코드를 이해하거나, Swift Concurrency가 제공하지 않는 **세밀한 제어** 가 필요할 때 GCD 지식은 필수입니다.

### 💡 왜 아직도 이것을 알아야 하나요? (Context)

- **Legacy Code**: 2021년 이전에 작성된 거의 모든 iOS 앱은 GCD를 사용합니다. 유지보수를 위해 피할 수 없습니다.
- **Low-Level Control**: "특정 스레드에 작업을 꽂아넣기", "정확히 0.3초 뒤에 실행하기", "반복 작업 동기화" 등은 아직도 GCD가 가장 직관적일 때가 있습니다.
- **Under the Hood**: Swift Concurrency(`Executor`)도 내부적으로 GCD 큐를 사용할 수 있습니다.

---

### 📚 외부 리소스 및 참고 자료

#### 공식 문서 및 소스 코드

- [Apple Open Source - libdispatch](https://github.com/apple/swift-corelibs-libdispatch) - GCD는 오픈소스입니다! C로 짜여진 내부 구현을 볼 수 있습니다.
- [Dispatch Documentation](https://developer.apple.com/documentation/dispatch)

#### 🎥 WWDC 세션

- [WWDC 2015: Building Responsive and Efficient Apps with GCD](https://developer.apple.com/videos/play/wwdc2015/718/) - QoS 개념 도입
- [WWDC 2017: Modernizing Grand Central Dispatch Usage](https://developer.apple.com/videos/play/wwdc2017/706/) - 스레드 폭발(Thread Explosion) 문제와 해결책

---

### 🔍 GCD Internals

#### 1. Work Stealing & Overcommit

- **ThreadPool**: GCD는 시스템 전역 스레드 풀을 관리합니다.
- **Work Stealing**: 큐가 비어있는 스레드는 바쁜 스레드의 큐에서 작업을 훔쳐와 실행 효율을 높입니다.
- **Overcommit**: 메인 스레드나 일부 특수 상황에서는 시스템 부하와 상관없이 강제로 스레드를 생성(Overcommit)하여 데드락을 방지합니다.

#### 2. Thread Explosion (스레드 폭발)

GCD의 가장 큰 단점입니다. `DispatchQueue.global().async`를 100번 호출하면서 내부에서 `sleep`(Block)을 걸면, GCD는 100개의 스레드를 생성해버립니다. 이는 컨텍스트 스위칭 오버헤드와 메모리 부족을 야기합니다.
👉 **해결책**: `DispatchSemaphore`로 동시 실행 수를 제한하거나, Swift Concurrency로 마이그레이션하세요.

---

### 🛠️ 고급 패턴 (Advanced Patterns)

#### 1. Barrier: Reader-Writer Lock 구현

여러 스레드가 읽는 건 괜찮지만, 쓸 때는 혼자만 써야 할 때 사용합니다.

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

#### 2. DispatchGroup: 여러 작업 기다리기

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

#### 3. DispatchSemaphore: 동시성(Concurrency) 수 제한

네트워크 요청이 한 번에 3개까지만 나가도록 제한하고 싶을 때 유용합니다.

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

메인 스레드에서 메인 큐로 `sync`를 쏘면 앱이 즉시 멈춥니다.
메인 스레드는 작업을 기다리고(`sync`), 큐도 메인 스레드가 비길 기다리는 상황이 되기 때문입니다.

```swift
// ❌ 절대 금지
DispatchQueue.main.sync {
    // 이미 메인 스레드인데 또 메인 큐를 기다림 -> 데드락
}
```

### 더 보기

- [[apple-swift-concurrency]] - GCD의 현대적 대안
- [[apple-operation-queue]] - GCD 기반의 객체지향 래퍼 (의존성 관리 가능)
