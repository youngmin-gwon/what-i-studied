---
title: apple-memory-management
tags: [apple, memory, arc, performance]
aliases: []
date modified: 2025-12-16 17:01:32 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Memory Management apple memory arc performance

ARC 와 메모리 최적화. 기본은 [[apple-runtime-and-swift]] 참고.

### ARC (Automatic Reference Counting)

컴파일 타임에 retain/release 코드를 자동 삽입.

```swift
class Person {
    let name: String
    
    init(name: String) {
        self.name = name
        print("\(name) is being initialized")
    }
    
    deinit {
        print("\(name) is being deinitialized")
    }
}

var person1: Person? = Person(name: "John") // retain count: 1
var person2 = person1 // retain count: 2
person1 = nil // retain count: 1
person2 = nil // retain count: 0, deinit 호출
```

### Strong, Weak, Unowned

#### Strong (기본)

강한 참조. retain count 증가.

```swift
class Owner {
    var pet: Pet?
}

class Pet {
    var owner: Owner? // Strong reference
}

let owner = Owner()
let pet = Pet()
owner.pet = pet
pet.owner = owner // 순환 참조!
```

#### Weak

약한 참조. retain count 증가 안 함. 참조 대상이 해제되면 자동으로 nil.

```swift
class Pet {
    weak var owner: Owner? // Weak reference
}

let owner = Owner()
let pet = Pet()
owner.pet = pet
pet.owner = owner // 순환 참조 해결

// owner 가 해제되면 pet.owner 는 자동으로 nil
```

#### Unowned

약한 참조이지만 항상 값이 있다고 가정. 참조 대상이 해제되면 크래시.

```swift
class CreditCard {
    unowned let customer: Customer // 항상 customer 존재
    
    init(customer: Customer) {
        self.customer = customer
    }
}

class Customer {
    var card: CreditCard?
    
    init() {
        self.card = CreditCard(customer: self)
    }
}
```

### 순환 참조 패턴

#### 클로저 캡처

```swift
class ViewController: UIViewController {
    var name = "ViewController"
    
    func setupHandler() {
        // ❌ 순환 참조
        someAsyncOperation {
            print(self.name) // self 강하게 캡처
        }
        
        // ✅ weak self
        someAsyncOperation { [weak self] in
            guard let self = self else { return }
            print(self.name)
        }
        
        // ✅ unowned self (self 가 항상 존재한다고 확신할 때)
        someAsyncOperation { [unowned self] in
            print(self.name)
        }
    }
}
```

#### Delegate 패턴

```swift
protocol DataSourceDelegate: AnyObject {
    func dataDidUpdate()
}

class DataSource {
    weak var delegate: DataSourceDelegate? // weak 필수!
}

class ViewController: UIViewController, DataSourceDelegate {
    let dataSource = DataSource()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        dataSource.delegate = self
    }
    
    func dataDidUpdate() {
        // 처리
    }
}
```

### Autoreleasepool

임시 객체의 메모리를 즉시 해제.

```swift
func processLargeData() {
    for i in 0..<1000000 {
        autoreleasepool {
            let data = createTemporaryData(index: i)
            process(data)
            // data 는 여기서 즉시 해제됨
        }
    }
}
```

**사용 시기:**
- 루프에서 많은 임시 객체 생성
- 백그라운드 스레드에서 Cocoa API 사용
- 메모리 압박 상황

### Memory Footprint 최적화

#### 값 타입 vs 참조 타입

```swift
// ✅ 값 타입 (struct): 스택에 할당, 빠름
struct Point {
    var x: Double
    var y: Double
}

// ❌ 참조 타입 (class): 힙에 할당, 느림
class PointClass {
    var x: Double
    var y: Double
    
    init(x: Double, y: Double) {
        self.x = x
        self.y = y
    }
}
```

#### Copy-on-Write

Swift 컬렉션은 COW 최적화.

```swift
var array1 = [1, 2, 3] // 메모리 할당
var array2 = array1 // 복사 안 함, 같은 메모리 공유

array2.append(4) // 이제 복사 발생
```

**커스텀 COW:**
```swift
struct MyArray {
    private var storage: Storage
    
    private final class Storage {
        var elements: [Int]
        
        init(elements: [Int]) {
            self.elements = elements
        }
    }
    
    init(elements: [Int]) {
        storage = Storage(elements: elements)
    }
    
    mutating func append(_ element: Int) {
        if !isKnownUniquelyReferenced(&storage) {
            storage = Storage(elements: storage.elements)
        }
        storage.elements.append(element)
    }
}
```

### 메모리 누수 감지

#### Instruments - Leaks

```bash
# Xcode → Product → Profile → Leaks
```

**주요 패턴:**
1. 순환 참조
2. Notification Observer 미제거
3. Timer 미해제
4. Delegate 강한 참조

#### 코드로 확인

```swift
class LeakDetector {
    static func track(_ object: AnyObject, file: String = #file, line: Int = #line) {
        let address = String(format: "%p", unsafeBitCast(object, to: Int.self))
        print("[\(file):\(line)] Allocated: \(address)")
        
        // deinit 시 로그
        objc_setAssociatedObject(object, &AssociatedKeys.deinitKey, DeinitLogger {
            print("[\(file):\(line)] Deallocated: \(address)")
        }, .OBJC_ASSOCIATION_RETAIN)
    }
}

private enum AssociatedKeys {
    static var deinitKey = "deinitKey"
}

private class DeinitLogger {
    let closure: () -> Void
    
    init(_ closure: @escaping () -> Void) {
        self.closure = closure
    }
    
    deinit {
        closure()
    }
}

// 사용
let person = Person(name: "John")
LeakDetector.track(person)
```

### 메모리 경고 처리

```swift
class ViewController: UIViewController {
    var imageCache: [String: UIImage] = [:]
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        
        // 캐시 정리
        imageCache.removeAll()
        
        // 재생성 가능한 데이터 제거
        clearTemporaryData()
    }
}

// App Delegate
class AppDelegate: UIResponder, UIApplicationDelegate {
    func applicationDidReceiveMemoryWarning(_ application: UIApplication) {
        // 전역 캐시 정리
        URLCache.shared.removeAllCachedResponses()
    }
}
```

### 성능 측정

#### Memory Graph Debugger

```bash
# Xcode → Debug → View Memory Graph
```

**확인 사항:**
- 순환 참조
- 예상치 못한 객체 유지
- 메모리 사용량

#### Allocations Instrument

```swift
// 메모리 할당 추적
class MemoryTracker {
    static func measure(label: String, block: () -> Void) {
        let before = mach_task_basic_info.memoryUsage
        block()
        let after = mach_task_basic_info.memoryUsage
        print("\(label): \(after - before) bytes")
    }
}

extension mach_task_basic_info {
    static var memoryUsage: UInt64 {
        var info = mach_task_basic_info()
        var count = mach_msg_type_number_t(MemoryLayout<mach_task_basic_info>.size) / 4
        
        let result = withUnsafeMutablePointer(to: &info) {
            $0.withMemoryRebound(to: integer_t.self, capacity: 1) {
                task_info(mach_task_self_, task_flavor_t(MACH_TASK_BASIC_INFO), $0, &count)
            }
        }
        
        return result == KERN_SUCCESS ? info.resident_size : 0
    }
}
```

### 더 보기

[[apple-runtime-and-swift]], [[apple-swift-concurrency]], [[apple-performance-and-debug]], [[apple-instruments-profiling]]
