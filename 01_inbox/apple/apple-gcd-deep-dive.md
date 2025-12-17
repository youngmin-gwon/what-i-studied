---
title: apple-gcd-deep-dive
tags: [apple, gcd, dispatch, concurrency, internals, performance]
aliases: []
date modified: 2025-12-17 14:05:00 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## GCD (Grand Central Dispatch) Deep Dive

`libdispatch`의 내부 동작 원리와 실무 동시성 프로그래밍 패턴. 기본 개념은 [[apple-runtime-and-swift]] 참고.

### 📚 외부 리소스 및 참고 자료

#### 공식 문서 및 소스 코드
- [Dispatch - Apple Developer](https://developer.apple.com/documentation/dispatch)
- [swift-corelibs-libdispatch - GitHub](https://github.com/apple/swift-corelibs-libdispatch) - 오픈소스 구현체
- [Concurrency Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html)

#### 🎥 WWDC 세션
- [WWDC 2017: Modernizing Grand Central Dispatch Usage](https://developer.apple.com/videos/play/wwdc2017/706/)
- [WWDC 2016: Concurrent Programming With GCD in Swift 3](https://developer.apple.com/videos/play/wwdc2016/720/)
- [WWDC 2015: Building Responsive and Efficient Apps with GCD](https://developer.apple.com/videos/play/wwdc2015/718/)

---

### 🔍 내부 동작 원리 (Internals)

#### 1. Thread Pool & Work Stealing
GCD는 매번 스레드를 생성하지 않고, **시스템 관리 스레드 풀(Thread Pool)**을 사용합니다.
- **Thread Management**: 작업(Block)이 큐에 들어오면, 시스템은 가용한 스레드를 풀에서 가져와 할당합니다.
- **Work Stealing**: 유휴 상태의 스레드가 다른 바쁜 스레드의 큐에서 작업을 훔쳐와(Steal) 실행하여 로드 밸런싱을 수행합니다.
- **Thread Explosion**: 블로킹 작업이 너무 많아 스레드가 계속 생성되는 현상. 컨텍스트 스위칭 오버헤드로 성능이 급격히 저하되므로 주의해야 합니다. (최대 스레드 수 제한이 있지만, 도달하면 시스템이 멈춥니다).

#### 2. QoS (Quality of Service)와 우선순위 역전
QoS 등급은 커널 스케줄러에게 스레드 우선순위를 힌트로 제공합니다.
- **Propagation**: 동기 작업(`sync`)이나 `DispatchGroup.notify`의 경우, 호출자의 높은 QoS가 피호출자에게 전파될 수 있습니다.
- **Priority Inversion**: 낮은 QoS 작업이 자원(Lock 등)을 점유하고 있어서 높은 QoS 작업이 대기해야 하는 상황. GCD는 낮은 QoS 스레드의 우선순위를 일시적으로 높여(Priority Inheritance) 이를 해결하려 시도합니다.

---

### DispatchQueue 상세

#### 1. Main Queue vs Global Queue vs Custom Queue

```swift
// 1. Main Queue (Serial)
// UI 업데이트 전용. Run Loop와 통합되어 있습니다.
// 절대 Sync로 호출하면 안됨 (Deadlock 발생).
DispatchQueue.main.async {
    // UI Code
}

// 2. Global Queues (Concurrent)
// 시스템 전역 공유 큐. QoS별로 존재합니다.
DispatchQueue.global(qos: .userInitiated).async {
    // Heavy Calculation
}

// 3. Custom Serial Queue
// 순서가 보장되어야 하는 작업 (예: 데이터베이스 쓰기, 파일 로깅).
// label은 디버깅 시 Instruments에 표시되므로 역 DNS 포맷 권장.
let databaseQueue = DispatchQueue(label: "com.example.app.db")
databaseQueue.async {
    // Write
}

// 4. Custom Concurrent Queue
// 읽기 작업은 병렬로, 쓰기 작업은 배타적으로 할 때 유용 (Barrier).
let fastQueue = DispatchQueue(label: "com.example.app.fast", attributes: .concurrent)
```

---

### 🛡️ 고급 패턴과 동시성 제어 (Advanced Patterns)

#### 1. Reader-Writer Lock (with Barrier)
여러 스레드가 동시에 읽어도 되지만, 쓸 때는 혼자만 써야 하는 상황. `DispatchBarrier`를 사용합니다.

```swift
class ThreadSafeCache {
    private let cache = [String: Any]()
    private let queue = DispatchQueue(label: "com.example.cache", attributes: .concurrent)
    
    // Reader: 동시 접근 허용 (Concurrent)
    func object(forKey key: String) -> Any? {
        queue.sync { 
            return cache[key] 
        }
    }
    
    // Writer: 배타적 접근 (Barrier)
    // Barrier 플래그가 있으면, 이전 작업들이 다 끝날 때까지 대기하고,
    // 이 작업이 실행되는 동안엔 다른 작업이 실행되지 않습니다 (Serial 처럼 동작).
    func setObject(_ obj: Any, forKey key: String) {
        queue.async(flags: .barrier) { [weak self] in
            self?.cache[key] = obj
        }
    }
}
```

#### 2. DispatchGroup (작업 동기화)
여러 비동기 작업이 모두 끝난 시점을 알아야 할 때.

```swift
func fetchAllData(completion: @escaping () -> Void) {
    let group = DispatchGroup()
    
    // 작업 1
    group.enter()
    api.fetchUser { _ in api.fetchProfile { group.leave() } }
    
    // 작업 2
    group.enter()
    api.fetchFriends { group.leave() }
    
    // 모든 작업 완료 시 호출
    group.notify(queue: .main) {
        print("All data fetched")
        completion()
    }
}
```

#### 3. DispatchSemaphore (리소스 제한)
동시 실행 작업 수를 제한할 때 (예: 동시에 3개까지만 다운로드).

```swift
let semaphore = DispatchSemaphore(value: 3) // 허용량 3
let queue = DispatchQueue.global()

for i in 0..<10 {
    queue.async {
        semaphore.wait() // 카운트 감소 (0이면 대기)
        print("Downloading \(i)")
        sleep(2) // 작업 시뮬레이션
        print("Done \(i)")
        semaphore.signal() // 카운트 증가
    }
}
```

---

### Troubleshooting (문제 해결)

#### ❌ Deadlock (교착 상태)
가장 흔한 데드락 패턴: Serial Queue에서 자기 자신에게 `sync` 호출.

```swift
let queue = DispatchQueue(label: "my.queue")

queue.async {
    // 이미 queue 안에서 실행 중인데...
    queue.sync { 
        // queue가 끝나기를 기다림 -> 영원히 대기 (Deadlock)
        print("Never printed")
    }
}
```
**해결**: 같은 큐 내에서는 절대 `sync`를 부르지 않거나, `NSRecursiveLock` 등을 고려해야 합니다(하지만 GCD 큐는 재귀적이지 않음).

#### ❌ Thread Explosion (스레드 폭발)
```swift
// ❌ 나쁜 예: 수천 개의 블로킹 작업을 concurrent queue에 던짐
for _ in 0..<10000 {
    DispatchQueue.global().async {
        sleep(1) // 블로킹
    }
}
```
시스템이 10000개의 스레드를 만들려고 시도하며 시스템 전체가 느려짐.
**해결**: `DispatchSemaphore`로 동시 실행 수 제한을 두거나, Swift Concurrency (`TaskGroup`)를 사용해야 합니다.

---

### 더 보기
- [[apple-swift-concurrency]] - 모던 Swift 동시성 (권장)
- [[apple-operation-queue]] - GCD의 객체 지향 래퍼
- [[apple-performance-and-debug]] - 성능 최적화
