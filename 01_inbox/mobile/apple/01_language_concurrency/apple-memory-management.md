---
title: apple-memory-management
tags: []
aliases: []
date modified: 2026-04-06 17:51:17 +09:00
date created: 2026-04-03 22:15:19 +09:00
---

## [[mobile-security]] > [[apple-memory-management]]

### Memory Management: ARC & Internals

iOS 앱의 성능과 안정성을 결정짓는 핵심, **ARC(Automatic Reference Counting)**의 깊은 구조와 동작 원리를 분석합니다.

---

iOS 앱의 성능과 안정성을 결정짓는 핵심, **ARC(Automatic Reference Counting)**의 깊은 곳을 탐험합니다.

단순히 `weak self` 를 쓰는 것을 넘어, **Side Table**이 어떻게 약한 참조를 관리하고 **Autoreleasepool**이 언제 필요한지 이해합니다.

#### 💡 왜 이것을 알아야 하나요? (Why it matters)
- **앱이 자꾸 죽나요? (OOM)**: 이미지가 많은 피드를 스크롤하다 앱이 튕긴다면, 순환 참조(Retain Cycle)나 메모리 피크(Peak) 관리 실패일 확률이 높습니다.
- **성능 저하**: 불필요한 객체 복사나 해제 지연은 프레임 드랍의 원인이 됩니다.
- **면접 단골 질문**: "ARC 와 가비지 컬렉션의 차이", "weak 와 unowned 의 내부 동작 차이"는 시니어 레벨로 가는 관문입니다.

---

#### 🔍 ARC 내부 동작 원리 (ARC Internals)

##### 1. Object Memory Layout & RefCounts

Swift 객체는 힙에 할당될 때, 메타데이터와 함께 두 개의 숨겨진 Reference Count 필드를 가집니다 (최적화에 따라 다름).

- **Strong Reference Count**: 객체를 유지하는 강한 참조 수.
- **Unowned Reference Count**: unowned 참조 수.
- *Weak Reference Count?* → 객체 내부에 없고 **Side Table**에 있을 수 있습니다.

##### 2. Side Table (사이드 테이블) 메커니즘

강한 참조 카운트나 약한 참조 카운트를 위해 객체 헤더 공간이 부족하거나, **Weak Reference**가 생성될 때 "Side Table"이라는 별도의 메모리 블록이 할당됩니다.

- **Why?** Weak 참조는 객체가 힙에서 할당 해제(Deallocated)된 후에도 nil 임을 확인하기 위해 주소를 추적해야 합니다 (Zombie Object 방지).
- **Process**:
    1. 객체에 첫 Weak 참조가 생기면 Side Table 을 할당합니다.
    2. 객체 헤더는 Side Table 을 가리키는 포인터로 대체됩니다(Bitmasking trick 사용).
    3. Weak 참조들은 객체가 아닌 Side Table 을 가리킵니다.
    4. 객체가 해제되어도 Side Table 은 Weak 참조 카운트가 0 이 될 때까지 살아남습니다.

##### 3. Tagged Pointers

작은 데이터(예: 작은 숫자, 날짜, 일부 짧은 문자열)는 힙에 할당하지 않고 포인터 자체에 데이터를 저장합니다.

- 64 비트 포인터 중 일부 비트를 Tag 로 사용하고 나머지를 데이터로 사용.
- `retain`/`release` 연산이 필요 없어 매우 빠릅니다.

---

#### 순환 참조 심화 및 해결 (Retain Cycles)

##### 클로저 캡처 (Deep Dive)

클로저는 참조 타입이므로 힙에 존재하며, 캡처된 변수들을 강하게 참조합니다.

```swift
class ViewController: UIViewController {
    var name = "ViewController"
    var onCompletion: (() -> Void)?
    
    func setupHandler() {
        // ❌ [강한 참조 순환]
        // self -> onCompletion -> Closure -> self
        self.onCompletion = {
            print(self.name) 
        }
        
        // ✅ [Weak Self]
        // Closure -> self (Weak)
        // self가 해제되면 closure 내부의 self는 nil이 됨.
        self.onCompletion = { [weak self] in
            guard let self = self else { return } // Strongify
            print(self.name)
        }
        
        // ✅ [Unowned Self]
        // self가 클로저보다 오래 산다는 것이 "100% 확실할 때만" 사용.
        // 아니면 크래시 발생.
        self.onCompletion = { [unowned self] in
            print(self.name)
        }
    }
}
```

---

#### 🛡️ 실무 메모리 최적화 (Memory Optimization)

##### 1. Autoreleasepool 활용

대량의 임시 객체가 루프 안에서 생성될 때 메모리 피크(Peak)를 낮춥니다.

```swift
func processLargeImages() {
    // ❌ 메모리가 계속 증가하다가 루프 종료 후 한꺼번에 해제됨
    for filename in filenames {
        let image = UIImage(contentsOfFile: filename)
        let processed = filter(image)
        save(processed)
    }

    // ✅ 루프 돌 때마다 즉시 해제하여 메모리 평탄화
    for filename in filenames {
        autoreleasepool {
            let image = UIImage(contentsOfFile: filename)
            let processed = filter(image)
            save(processed)
        }
    }
}
```

##### 2. COW (Copy-On-Write) 커스텀 구현

Swift 의 `Array`, `Dictionary` 처럼 값을 수정할 때만 복사하는 동작을 커스텀 타입에 적용하기.

```swift
struct MyData {
    private var dataWrapper: DataWrapper
    
    init() { dataWrapper = DataWrapper() }
    
    var value: Int {
        get { return dataWrapper.value }
        set {
            // 참조 카운트가 1보다 크면(공유 중이면) 복사본 생성
            if !isKnownUniquelyReferenced(&dataWrapper) {
                dataWrapper = dataWrapper.copy()
            }
            dataWrapper.value = newValue
        }
    }
}

private class DataWrapper {
    var value: Int = 0
    func copy() -> DataWrapper { 
        let new = DataWrapper()
        new.value = self.value
        return new
    }
}
```

---

#### 🐞 메모리 누수 디버깅 (Profiling)

##### 1. Xcode Memory Graph Debugger

**사용법**:

1. 앱 실행 중 하단 디버그 바의 "연결된 3 개의 사각형 아이콘" 클릭.
2. 실행이 일시 정지되고 힙 메모리 스냅샷을 뜹니다.
3. 좌측 네비게이터에서 노란색 경고(⚠️)가 뜨는 항목 확인. 보라색(🟣)은 누수 가능성 높음.
4. 객체를 클릭하여 참조 그래프(Reference Chain)를 확인. 굵은 선이 Strong Reference. **순환 참조 고리**를 찾으세요.

##### 2. Instruments - Allocations & Leaks

**Allocations**: 객체의 생존 주기를 시각적으로 확인.

- "Mark Generation" 기능을 사용해 화면 진입/이탈 시 **Persistent Bytes**가 증가하는지 확인합니다(Dirty Memory 증가 추적).

**Leaks**: 자동으로 누수 탐지.

- 하지만 순환 참조(Retain Cycle)는 레퍼런스 카운트가 0 이 아니므로 Leaks 악기(Instrument)가 못 잡는 경우가 많습니다. Memory Graph 가 더 유용할 때가 많습니다.

##### 3. 코드로 누수 탐지 (Deinit Logger)

디버깅용으로 특정 객체가 제대로 해제되는지 로그를 심을 때 유용합니다.

```swift
class LeakDetector {
    static func track(_ object: AnyObject, file: String = #file, line: Int = #line) {
        let address = Unmanaged.passUnretained(object).toOpaque()
        let className = String(describing: type(of: object))
        print("🟢 Init: \(className) (\(address)) at \(file):\(line)")
        
        // Associated Object로 DeinitTracker 연결
        objc_setAssociatedObject(object, &AssociatedKeys.tracker, DeinitTracker {
            print("🔴 Deinit: \(className) (\(address))")
        }, .OBJC_ASSOCIATION_RETAIN)
    }
}

private enum AssociatedKeys { static var tracker = "tracker" }

private class DeinitTracker {
    let callback: () -> Void
    init(_ callback: @escaping () -> Void) { self.callback = callback }
    deinit { callback() }
}
```

#### 📚 외부 리소스 및 참고 자료

- **[WWDC 2021: ARC in Swift](https://developer.apple.com/videos/play/wwdc2021/10216)**: Side Table 과 ARC 최적화의 바이블.
- **[Swift Runtime Source](https://github.com/apple/swift/tree/main/stdlib/public/runtime)**: 실제 C++ 구현체 확인.

#### 🔗 연관 문서 및 심화 학습
- [[apple-uikit-lifecycle]] - 앱 생명주기에 따른 메모리 관리 및 뷰 컨트롤러 해제 시점
- [[apple-performance-monitoring]] - Instruments 를 활용한 메모리 누수 및 리테인 사이클 추적
- [[apple-swift-concurrency]] - 비동기 작업에서의 강한 참조 순환 방지 및 Actor 의 메모리 안전성
- [[apple-memory-management-check]] - 핵심 개념 자가 진단 및 면접 대비 질문
