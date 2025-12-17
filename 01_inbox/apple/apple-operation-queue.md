---
title: apple-operation-queue
tags: [apple, operation, queue, concurrency]
aliases: []
date modified: 2025-12-16 17:01:32 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Operation Queue apple operation queue concurrency

NSOperation 과 의존성 관리. 기본은 [[apple-gcd-deep-dive]] 참고.

### Operation

```swift
class DownloadOperation: Operation {
    let url: URL
    
    init(url: URL) {
        self.url = url
    }
    
    override func main() {
        if isCancelled { return }
        
        // 작업 수행
        downloadFile(from: url)
    }
}

let queue = OperationQueue()
let operation = DownloadOperation(url: url)
queue.addOperation(operation)
```

### 의존성

```swift
let download = DownloadOperation(url: url)
let process = ProcessOperation()
let upload = UploadOperation()

process.addDependency(download)
upload.addDependency(process)

queue.addOperations([download, process, upload], waitUntilFinished: false)
```

### 더 보기

[[apple-gcd-deep-dive]], [[apple-swift-concurrency]]
