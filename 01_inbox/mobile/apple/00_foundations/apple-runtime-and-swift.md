---
title: apple-runtime-and-swift
tags: []
aliases: []
date modified: 2026-04-05 17:44:31 +09:00
date created: 2026-04-03 22:15:19 +09:00
---

## [[mobile-security]] > [[apple-runtime-and-swift]]

### Runtime & Swift/ObjC Internals: Dynamic Architecture

Apple 플랫폼의 실행 환경을 구성하는 **Objective-C Runtime**과 **Swift Runtime**의 내부 동작 원리를 심층 분석합니다. 이 시스템의 근간이 되는 하이브리드 커널 구조는 [[apple-architecture-stack]] 을 참고하시기 바랍니다.

---

#### 🔍 Method Dispatch (메서드 호출 매커니즘)

런타임에 어떤 코드를 실행할지 결정하는 과정으로, 성능과 유연성 사이의 균형을 결정합니다.

- **Static Dispatch (Direct)**: 컴파일 타임에 호출 주소가 확정됩니다. `struct`, `enum`, `final class`, `private` 메서드에 적용되며 가장 빠릅니다.
- **Table Dispatch (V-Table / Witness)**: 런타임에 함수 포인터 테이블을 참조합니다. Swift 의 클래스 상속과 프로토콜(PWT) 처리에 주로 사용됩니다.
- **Message Dispatch (objc_msgSend)**: Selector(문자열) 기반으로 메서드를 검색합니다. 가장 유연하며 **Method Swizzling**이나 KVO 의 기반이 됩니다.

---

#### 🧠 Objective-C Runtime Internals

- **isa Pointer**: 모든 객체의 첫 번째 필드로, 클래스 및 메타클래스 정보를 담고 있습니다. 64 비트 환경에서는 **Non-pointer isa** 기술을 통해 참조 카운트 등의 부가 정보를 함께 저장하여 최적화합니다.
- **Messaging Pipeline**: `objc_msgSend` 호출 시 `Cache Lookup` → `Method List Search` → `Dynamic Resolution` → `Forwarding` 순으로 진행됩니다. 대부분의 호출은 고도로 최적화된 메서드 캐시에서 즉시 반환됩니다.
- **Method Swizzling**: 런타임에 메서드 구현(IMP)을 교체하는 기술입니다. 메인 스레드 로깅이나 분석 SDK 에서 활용되나, 현대적인 Swift/SwiftUI 환경에서는 예기치 못한 부작용을 유발하는 안티패턴으로 간주되기도 합니다.

---

#### 🧬 Swift Runtime & Metadata

- **Type Metadata**: Swift 는 런타임에 제네릭과 동적 타입 확인을 위한 풍부한 메타데이터를 유지합니다. 이는 ABI 안정성의 핵심 요소입니다.
- **Existential Container**: 프로토콜 타입(`any` 키워드)을 처리하기 위한 특수 구조체로, 데이터 크기에 따라 인라인 버퍼 혹은 힙 할당을 수행합니다.
- **some vs any**: Swift 5.7+ 부터는 성능 최적화(Static Dispatch 유도)를 위해 컴파일 타임에 타입이 확정되는 `some`(Opaque Type) 사용이 적극 권장됩니다.

---

#### 🛡️ 보안 및 성능 최적화 포인트

- **WMO (Whole Module Optimization)**: 모듈 전체를 분석하여 `internal` 수준에서도 적극적인 정적 디스패치와 인라이닝 최적화를 수행합니다.
- **@objc 의 오버헤드**: Swift 코드에 `@objc` 를 남용하면 브리징 비용과 바이너리 크기 증가를 유발하므로 Selector 가 필수적인 경우에만 제한적으로 사용해야 합니다.
- **Dynamic Casting**: `as?` 또는 `as!` 는 런타임 메타데이터 순회를 동반하므로 빈번한 루프 내에서의 사용은 지양하는 것이 좋습니다.

---

#### 📚 연관 문서 및 심화 학습
- [[apple-memory-management]] - 객체 레이아웃과 ARC 메모리 관리
- [[apple-uikit-lifecycle]] - UIKit 프레임워크의 생명주기와 내부 동작
- [[apple-architecture-stack]] - Darwin 커널과 Mach/BSD 계층 구조
- [[apple-foundations]] - Apple 플랫폼 공통 설계 철학
- [[apple-performance-monitoring]] - 런타임 성능 프로파일링 가이드
- [[mobile-security]] - 통합 모바일 보안 가이드
�에 인스턴스화된 타입 정보 (예: `Array<Int>` 와 `Array<String>` 은 다른 메타데이터를 가짐).

##### 2. Protocol Witness Table (PWT)

프로토콜을 통한 메서드 호출은 PWT 를 거칩니다.

```swift
func process(item: Runnable) { // Runnable 프로토콜 타입
    item.run() 
    // 컴파일러는 item의 PWT를 찾고, 
    // run() 함수 포인터 offset을 더해 실제 함수 주소를 호출함.
}
```

##### 3. Existential Container (`any` vs `some`)

프로토콜 타입 변수(Existential)는 크기가 제각각인 구현체를 담기 위해 컨테이너 구조를 가집니다.

- **작은 값**: **Inline Buffer** (3 pointers size)에 직접 저장.
- **큰 값**: 힙에 할당하고 포인터만 저장.
- **VWT (Value Witness Table)**: 할당/복사/해제 방법을 아는 테이블.
- **PWT**: 프로토콜 메서드 테이블 포인터.

>[!CAUTION] **Devil's Advocate : Swift 5.7+ 의 `any` 와 `some`**
>이전에는 무분별하게 프로토콜을 타입으로 지정했지만, 이는 런타임 오버헤드(Existential Container 생성 및 Heap 할당)를 유발합니다.
>현재는 Opaque Type 인 `some Protocol`(컴파일 타임 정적 디스패치)을 우선 사용하고, 다형성 배열 등 꼭 필요한 경우에만 명시적으로 `any Protocol` (런타임 오버헤드 감수)을 사용하도록 언어 차원(Swift 5.7+)에서 강제/권장하고 있습니다.
---

#### 🛡️ 실무 성능 및 최적화 포인트

##### 1. Static Dispatch 유도

- 성능이 중요한 루프 내부에서는 `final`, `private` 을 적극 사용하여 컴파일러가 Static Dispatch 및 Inlining 을 할 수 있게 돕습니다.
- `WMO (Whole Module Optimization)` 을 켜면 모듈 전체를 분석하여 `internal` 메서드도 자동으로 최적화할 수 있습니다.

##### 2. @objc 의 비용

- Swift 메서드에 `@objc` 를 붙이면 Thunk(변환 코드)가 생성되고, Objective-C 런타임에 메타데이터가 등록됩니다.
- 바이너리 크기가 증가하고, 호출 시 브리징 비용이 발생할 수 있습니다. 꼭 필요한 곳(Selector 등)에만 사용하세요.

##### 3. 다이나믹 캐스팅 (as?, as!)

- `as?` 는 런타임 메타데이터를 순회하며 타입 호환성을 검사하므로 비용이 발생합니다.
- 특히 `Any` 타입에서 구체 타입으로 캐스팅하는 것은 무겁습니다.

#### 더 보기

- [apple-memory-management](../01_language_concurrency/apple-memory-management.md) - 객체 레이아웃과 메모리 관리
- [apple-uikit-lifecycle](../02_ui_frameworks/apple-uikit-lifecycle.md) - Swizzling 이 자주 사용되는 UIKit 내부
