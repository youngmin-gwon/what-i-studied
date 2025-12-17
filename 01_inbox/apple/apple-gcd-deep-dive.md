---
title: apple-gcd-deep-dive
tags: [apple, gcd, dispatch, concurrency]
aliases: []
date modified: 2025-12-16 17:01:32 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## GCD Deep Dive apple gcd dispatch concurrency

Grand Central Dispatch 심화. 기본은 [[apple-runtime-and-swift]] 참고.

### DispatchQueue

```swift
// 메인 큐
DispatchQueue.main.async {
    // UI 업데이트
}

// 글로벌 큐
DispatchQueue.global(qos: .userInitiated).async {
    // 백그라운드 작업
}

// 커스텀 큐
let queue = DispatchQueue(label: "com.example.myqueue")
queue.async {
    // 작업
}
```

### QoS (Quality of Service)

```swift
// .userInteractive: UI 업데이트 (최고 우선순위)
// .userInitiated: 사용자가 시작한 작업
// .default: 기본
// .utility: 진행 표시가 있는 긴 작업
// .background: 백그라운드 (최저 우선순위)
```

### DispatchGroup

```swift
let group = DispatchGroup()

group.enter()
fetchData1 { data in
    print("Data 1")
    group.leave()
}

group.enter()
fetchData2 { data in
    print("Data 2")
    group.leave()
}

group.notify(queue: .main) {
    print("All done")
}
```

### 더 보기

[[apple-swift-concurrency]], [[apple-operation-queue]], [[apple-performance-and-debug]]
