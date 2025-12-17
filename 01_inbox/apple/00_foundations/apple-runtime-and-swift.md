---
title: apple-runtime-and-swift
tags: [apple, objc, runtime, swift, internals, dispatch, isa]
aliases: []
date modified: 2025-12-17 16:00:00 +09:00
date created: 2025-12-16 16:08:12 +09:00
---

## Runtime & Swift/ObjC Internals

Apple 플랫폼의 근간이 되는 Objective-C Runtime과 Swift Runtime의 내부 동작 원리 상세 분석.

### 📚 외부 리소스 및 참고 자료

#### 공식 문서 및 소스 코드

- [Objective-C Runtime Source - GitHub](https://github.com/apple-oss-distributions/objc4) - `objc_msgSend` 등의 실제 구현 확인 가능.
- [Swift Runtime Source - GitHub](https://github.com/apple/swift/tree/main/stdlib/public/runtime)
- [Objective-C Runtime Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Introduction/Introduction.html)

#### 📖 기술 아티클 & Reverse Engineering

- [Understanding Swift Method Dispatch](https://www.rightpoint.com/rplabs/switch-method-dispatch-table)
- [Friday Q&A: objc_msgSend Tour](https://www.mikeash.com/pyblog/friday-qa-2012-11-16-lets-build-objc_msgsend.html)
- [The Swift ABI](https://github.com/apple/swift/blob/main/docs/ABI/TypeMetadata.rst)

---

### 🔍 Method Dispatch (메서드 디스패치)

메서드 호출 시 **어떤 코드를 실행할지 결정하는 과정**입니다. Swift는 3가지 방식을 모두 사용합니다.

#### 1. Static Dispatch (Direct Dispatch)
- **동작**: 컴파일 타임에 호출할 함수 주소가 확정됩니다. (`call 0x123456`)
- **사용처**: `struct`, `enum`의 메서드, `final class`, `extension`에 정의된 메서드 (단, `@objc` 제외), `private`.
- **특징**: 가장 빠르며 인라인 최적화 가능.

#### 2. Table Dispatch (Witness Table / V-Table)
- **동작**: 런타임에 **함수 포인터 테이블(Table)**을 참조하여 주소를 찾습니다.
- **사용처**: Swift `class`의 메서드 (초기 선언부), 프로토콜 요구사항.
- **구조**:
    - **V-Table (Virtual Table)**: 클래스 상속 계층 지원.
    - **PWT (Protocol Witness Table)**: 프로토콜 채택 시 생성. 각 타입마다 해당 프로토콜 요구사항을 어디서 구현했는지 매핑.

#### 3. Message Dispatch (`objc_msgSend`)
- **동작**: 런타임에 문자열(Selector)로 메서드를 검색합니다. 실패 시 전달(Forwarding) 가능.
- **사용처**: Objective-C 클래스, `dynamic` 키워드가 붙은 Swift 메서드.
- **특징**: 가장 느리지만 가장 유연함 (KVO, Swizzling 가능).

| 타입 | 초기 선언 (Initial Declaration) | Extension |
|------|--------------------------------|-----------|
| **Value Type** | Static | Static |
| **Protocol** | Table (Witness) | Static |
| **Class** | Table (V-Table) | Static |
| **NSObject** | Table (V-Table) | Message |

---

### 🧠 Objective-C Runtime Internals

#### 1. `isa` Pointer & Class Structure
모든 ObjC 객체(그리고 Swift 클래스 인스턴스)의 첫 번째 필드는 `isa` 포인터입니다.
- **Non-pointer isa**: 64비트 아키텍처에서 포인터의 남는 비트에 Reference Count, Weakly Referenced 여부 등을 함께 저장하는 최적화 기법. (`1`비트만 실제 클래스 주소 판별에 사용하고 나머지는 플래그로 씀)
- **Metaclass**: `isa`가 가리키는 `Class` 객체의 `isa`는 `Metaclass`를 가리킵니다. 클래스 메서드(`+func`)는 메타클래스에 저장됩니다.

#### 2. `objc_msgSend` Anatomy
```c
id objc_msgSend(id self, SEL op, ...)
```
이 함수는 어셈블리로 작성되어 있으며, 극도로 최적화되어 있습니다:
1. `self`가 `nil`인지 체크 (nil이면 0 리턴하고 종료).
2. `self->isa`를 통해 클래스 객체 로드.
3. **Cache Lookup**: 클래스의 메서드 캐시 해시테이블에서 Selector 검색 **(가장 중요, 여기서 대부분 리턴)**.
4. **Method List Search**: 캐시 미스 시, 클래스(및 슈퍼클래스)의 `rw` 영역 메서드 리스트 선형 검색.
5. **Dynamic Method Resolution**: 못 찾으면 `resolveInstanceMethod:` 호출.
6. **Forwarding**: 그래도 없으면 `forwardInvocation:` 호출 (크래시 전 마지막 기회).

#### 3. Method Swizzling
런타임에 메서드 구현(IMP)을 바꿔치기하는 기술. 주로 로깅, 분석 SDK, 디버깅 툴이 사용함.

```swift
extension UIViewController {
    // +load는 앱 시작 시 런타임에 의해 호출됨 (Swift에서는 initialize 등으로 대체 권장되나 여전히 쓰임)
    static func swizzleViewDidLoad() {
        let original = class_getInstanceMethod(UIViewController.self, #selector(viewDidLoad))
        let swizzled = class_getInstanceMethod(UIViewController.self, #selector(myViewDidLoad))
        method_exchangeImplementations(original!, swizzled!)
    }
    
    @objc func myViewDidLoad() {
        print("Logged ViewDidLoad: \(self)")
        self.myViewDidLoad() // 재귀 호출 아님! 원본 viewDidLoad가 호출됨 (Swizzled)
    }
}
```

---

### 🧬 Swift Runtime & Metadata

#### 1. Type Metadata
Swift는 런타임에 제네릭과 동적 타입 확인을 위해 풍부한 메타데이터를 유지합니다.
- **Nominal Type Descriptor**: 타입의 이름, 필드 이름 등 정적 정보.
- **Type Metadata Records**: 런타임에 인스턴스화된 타입 정보 (예: `Array<Int>`와 `Array<String>`은 다른 메타데이터를 가짐).

#### 2. Protocol Witness Table (PWT)
프로토콜을 통한 메서드 호출은 PWT를 거칩니다.
```swift
func process(item: Runnable) { // Runnable 프로토콜 타입
    item.run() 
    // 컴파일러는 item의 PWT를 찾고, 
    // run() 함수 포인터 offset을 더해 실제 함수 주소를 호출함.
}
```

#### 3. Existential Container
프로토콜 타입 변수(Existential)는 크기가 제각각인 구현체를 담기 위해 컨테이너 구조를 가집니다.
- **작은 값**: **Inline Buffer** (3 pointers size)에 직접 저장.
- **큰 값**: 힙에 할당하고 포인터만 저장.
- **VWT (Value Witness Table)**: 할당/복사/해제 방법을 아는 테이블 포인터.
- **PWT**: 프로토콜 메서드 테이블 포인터.

---

### 🛡️ 실무 성능 및 최적화 포인트

#### 1. Static Dispatch 유도
- 성능이 중요한 루프 내부에서는 `final`, `private`을 적극 사용하여 컴파일러가 Static Dispatch 및 Inlining을 할 수 있게 돕습니다.
- `WMO (Whole Module Optimization)`을 켜면 모듈 전체를 분석하여 `internal` 메서드도 자동으로 최적화할 수 있습니다.

#### 2. @objc의 비용
- Swift 메서드에 `@objc`를 붙이면 Thunk(변환 코드)가 생성되고, Objective-C 런타임에 메타데이터가 등록됩니다.
- 바이너리 크기가 증가하고, 호출 시 브리징 비용이 발생할 수 있습니다. 꼭 필요한 곳(Selector 등)에만 사용하세요.

#### 3. 다이나믹 캐스팅 (as?, as!)
- `as?`는 런타임 메타데이터를 순회하며 타입 호환성을 검사하므로 비용이 발생합니다.
- 특히 `Any` 타입에서 구체 타입으로 캐스팅하는 것은 무겁습니다.

### 더 보기
- [[apple-memory-management]] - 객체 레이아웃과 메모리 관리
- [[apple-uikit-lifecycle]] - Swizzling이 자주 사용되는 UIKit 내부
