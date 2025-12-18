---
title: apple-operation-queue
tags: [apple, operation, queue, concurrency, nsoperation, dependencies]
aliases: []
date modified: 2025-12-17 18:00:00 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Operation & OperationQueue Deep Dive

GCD가 불(Fire)하고 잊는(Forget) 방식이라면, **Operation**은 작업을 **객체(Object)**로 만들어 관리하는 고수준 API입니다. 
복잡한 의존성(Dependency)이 있거나, 작업 취소(Cancellation) 기능이 필수적일 때 GCD보다 강력합니다.

### 💡 왜 아직도 이것을 알아야 하나요? (Why it matters)
- **복잡한 순서 제어**: "로그인이 끝나면 -> 프로필을 받고 -> 다 받으면 UI 갱신" 같은 흐름을 `addDependency`로 깔끔하게 표현할 수 있습니다.
- **취소 가능성(Cancellability)**: GCD 태스크는 취소가 번거롭지만, Operation은 `.cancel()`을 호출하고 내부에서 `isCancelled`를 체크하는 표준 패턴이 있습니다.
- **객체지향적 설계**: 재사용 가능한 작업 단위(클래스)로 캡슐화하기 좋습니다.

---

### 🔍 내부 동작 원리 (Internals)

#### 1. State Machine (상태 머신)
`Operation`은 내부적으로 **KVO(Key-Value Observing)** 기반의 상태 머신을 가집니다.
- `isReady`: 준비됨 (의존성이 모두 해결됨)
- `isExecuting`: 실행 중
- `isFinished`: 완료됨 (이 값을 `true`로 만들어야 큐에서 제거됨)
- `isCancelled`: 취소 요청됨

#### 2. Synchronous vs Asynchronous
- **Synchronous (기본값)**: `main()` 메서드가 리턴하면 작업이 끝난 것으로 간주합니다.
- **Asynchronous**: 네트워크 요청처럼 `main()`이 리턴되어도 작업이 끝난 게 아닐 때 사용합니다. 직접 KVO (`isExecuting`, `isFinished`)를 수동으로 조작해줘야 해서 구현이 까다롭습니다.

---

### 🛠️ 실무 구현 패턴

#### 1. 기본 구현 (BlockOperation)
간단한 작업은 서브클래싱 없이 블록으로 처리합니다.

```swift
let queue = OperationQueue()
let operation = BlockOperation {
    print("Task Start")
    // ...
}

operation.completionBlock = {
    print("Task Finished")
}

queue.addOperation(operation)
```

#### 2. Subclassing & Cancellation
취소 기능을 제대로 지원하려면 `main()` 실행 중간중간에 `isCancelled`를 체크해야 합니다.

```swift
class ImageFilterOperation: Operation {
    let inputImage: UIImage
    var outputImage: UIImage?
    
    init(image: UIImage) {
        self.inputImage = image
    }
    
    override func main() {
        // 1. 시작 전 취소 체크
        if isCancelled { return }
        
        // 2. 무거운 작업 수행 (가상)
        guard let cgImage = inputImage.cgImage else { return }
        
        // 3. 작업 중간 취소 체크
        if isCancelled { return }
        
        // 4. 필터 적용...
        Thread.sleep(forTimeInterval: 1.0) 
        
        if isCancelled { return }
        self.outputImage = self.inputImage // 결과 저장
    }
}
```

#### 3. 의존성 관리 (Dependencies)
Deadlock이 발생하지 않도록 주의해야 합니다(A->B, B->A).

```swift
let downloadOp = DownloadOperation(url: ...)
let filterOp = FilterOperation()
let uploadOp = UploadOperation()

// 다운로드 -> 필터 -> 업로드 순서 강제
filterOp.addDependency(downloadOp)
uploadOp.addDependency(filterOp)

// 데이터 전달 (Adapter 패턴)
filterOp.completionBlock = {
    if let data = downloadOp.resultData {
        filterOp.inputData = data // 보통은 Protocol이나 Adapter Operation을 씀
    }
}
```

#### 4. Asynchronous Operation (Advanced)
비동기 함수를 래핑할 때는 상태 관리가 필수입니다.

```swift
class AsyncOperation: Operation {
    // KVO 처리를 위한 보일러플레이트가 필요함 (생략)
    // state = .executing, .finished 등을 willChangeValue/didChangeValue로 알림
    
    override func start() {
        if isCancelled {
            state = .finished
            return
        }
        state = .executing
        
        // 비동기 작업 시작
        network.fetch { [weak self] in
            // 작업이 진짜 끝났을 때 state 변경
            self?.state = .finished
        }
    }
}
```

### 더 보기
- [apple-gcd-deep-dive](apple-gcd-deep-dive.md) - 더 가볍고 빠른 대안
- [apple-swift-concurrency](apple-swift-concurrency.md) - 최신 비동기 모델 (Task Group이 의존성 관리 대체 가능)
