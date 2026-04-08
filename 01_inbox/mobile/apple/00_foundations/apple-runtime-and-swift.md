---
title: apple-runtime-and-swift
tags: []
aliases: []
date modified: 2026-04-08 13:58:50 +09:00
date created: 2026-04-03 22:15:19 +09:00
---

## [[mobile-security]] > [[apple-runtime-and-swift]]

### Runtime & Swift/ObjC Internals: Dynamic Architecture

Apple 플랫폼의 실행 환경을 구성하는 **Objective-C Runtime**과 **Swift Runtime**의 내부 동작 원리를 심층 분석합니다. 이 시스템의 근간이 되는 하이브리드 커널 구조는 [[apple-architecture-stack]] 을 참고하시기 바랍니다.

#### 🏗️ Architecture Level: How Compiled Code is Processed

컴파일된 코드가 실제 하드웨어(ARM64 CPU)에서 어떻게 인식되고 실행되는지, 언어별 컴파일 과정과 바이너리 구조를 분석합니다.

- **Compilation Pipeline (언어별 컴파일 경로)**:
    - **Objective-C**: `Clang` 프론트엔드가 C/Obj-C 코드를 분석하여 **LLVM IR**(Intermediate Representation)을 생성합니다. 이후 LLVM 백엔드가 이를 특정 아키텍처(arm64, x86_64)의 기계어로 변환합니다.
    - **Swift**: `Swift Compiler` 가 구문 분석 후 **SIL**(Swift Intermediate Language)이라는 고수준 중간 언어 단계를 거칩니다. SIL 단계에서 Swift 만의 최적화(ARC 최적화, 제네릭 특수화 등)를 수행한 뒤 LLVM IR 로 넘깁니다.
- **Mach-O Binary Structure (바이너리 수준의 구분)**:
    - 컴파일 결과물은 **Mach-O** 형식으로 저장됩니다.
    - **Objective-C Metadata**: `__DATA` 세그먼트의 `__objc_classlist`, `__objc_methname` 등의 섹션에 클래스 및 메서드 정보가 기록됩니다. 런타임(dyld)은 이 정보를 읽어 메서드 테이블을 구축합니다.
    - **Swift Metadata**: `__TEXT` 및 `__DATA` 세그먼트에 `__swift5_types`, `__swift5_protos` 등으로 기록됩니다. Swift 런타임은 이를 통해 리플렉션, 제네릭 타입 확인 등을 수행합니다.
- **CPU Execution & Runtime Intersection**:
    - CPU 는 Swift 나 Obj-C 를 직접 구분하지 않습니다. 오직 **ARM64 명령어**만 실행합니다.
    - **Dynamic Dispatch**는 결국 CPU 레벨에서 **간접 점프(Indirect Jump)** 명령어(`br x16` 등)로 처리됩니다.
    - `dyld`(Dynamic Linker)가 앱 실행 시 공유 라이브러리(`libobjc.A.dylib`, `libswiftCore.dylib`)를 로드하고, `_objc_init` 등의 초기화 함수를 호출하여 런타임 환경을 셋업해야 비로소 메시지 전달이나 타입 확인이 가능해집니다.
    - `dyld`(Dynamic Linker)가 앱 실행 시 공유 라이브러리(`libobjc.A.dylib`, `libswiftCore.dylib`)를 로드하고, `_objc_init` 등의 초기화 함수를 호출하여 런타임 환경을 셋업해야 비로소 메시지 전달이나 타입 확인이 가능해집니다.

---

#### 💡 초보자를 위한 Dispatch 이해하기 (Low-Level 개념)

"Dispatch" 란 한마디로 **"어떤 함수 코드를 실행할지 결정하고 그곳으로 점프하는 과정"** 입니다. 컴퓨터 입장에서 이해하기 쉽게 비유를 통해 설명합니다.

1. **Static Dispatch (정적 디스패치)**: **"직통 전화"**
   - **설명**: 컴파일러가 코드를 짤 때 이미 실행할 함수의 주소를 딱 정해버립니다.
   - **과정**: 저장된 메모리 주소(예: 0x123)로 곧장 뛰어갑니다.
   - **장점**: 중간에 물어볼 필요가 없어 가장 빠릅니다. (직행 열차)
   - **특징**: `struct`, `final class` 처럼 "나중에 바뀔 일이 없는" 코드에 쓰입니다.

2. **Dynamic Dispatch (동적 디스패치)**: **"안내 데스크 거치기"**
   - **설명**: 코드가 실행되는 도중(Runtime)에 "지금 이 객체의 상태를 보고 어떤 함수를 실행할지" 결정합니다.
   - **왜 필요한가?**: 상속 때문입니다. 부모 클래스의 `draw()` 인지, 자식 클래스가 재정의(Override)한 `draw()` 인지 실행해봐야 알기 때문입니다.
   - **방식 A (Table Dispatch)**: **"목록 확인하기"**
     - 각 클래스마다 함수 주소가 적힌 **메뉴판(V-Table)**이 있습니다.
     - "이 객체의 메뉴판 3 번째 줄에 적힌 곳으로 가라"고 CPU 에게 명령합니다.
   - **방식 B (Message Dispatch)**: **"직원에게 물어보기"** (Objective-C 방식)
     - 이름(문자열)을 들고 가서 "혹시 `sayHello` 라는 함수 어디 있나요?"라고 런타임 시스템에게 물어봅니다.
     - 런타임이 목록을 뒤져서 주소를 알려주면 그제야 점프합니다. 가장 유연하지만 매번 물어봐야 하므로 가장 느립니다.

---

#### 🧩 메모리 레벨에서 본 Dispatch 의 차이

CPU 가 함수를 실행하려면 **"어떤 메모리 주소로 가라"** 는 명령을 받아야 합니다.

- **Static Dispatch**:
  ```asm
  bl 0x1000  ; 컴파일러가 0x1000 이라는 주소를 아예 박아넣음. (속도: 빛의 속도)
  ```
- **Dynamic Dispatch (Table)**:
  ```asm
  ldr x16, [x0, #0x10]  ; 객체(x0)의 클래스 정보에서 주소값을 가져와(ldr) x16에 담음.
  br x16                ; x16에 담긴 주소로 점프. (중간에 한 단계를 거침)
  ```
- **Dynamic Dispatch (Message)**:
  ```asm
  bl _objc_msgSend      ; 런타임 매니저에게 주소 좀 찾아달라고 부탁하고 기다림. (가장 복잡)
  ```

---

#### 🔍 Method Dispatch (메서드 호출 매커니즘)

런타임에 어떤 코드를 실행할지 결정하는 과정으로, 성능과 유연성 사이의 균형을 결정합니다.

- **Static Dispatch (Direct)**: 컴파일 타임에 호출 주소가 확정됩니다. `struct`, `enum`, `final class`, `private` 메서드에 적용되며 가장 빠릅니다.
- **Table Dispatch (V-Table / Witness)**: 런타임에 함수 포인터 테이블을 참조합니다. Swift 의 클래스 상속과 프로토콜(PWT) 처리에 주로 사용됩니다.
- **Message Dispatch (objc_msgSend)**: Selector(문자열) 기반으로 메서드를 검색합니다. 가장 유연하며 **Method Swizzling**이나 KVO 의 기반이 됩니다.

#### 🧠 Objective-C Runtime Internals

- **isa Pointer**: 모든 객체의 첫 번째 필드로, 클래스 및 메타클래스 정보를 담고 있습니다. 64 비트 환경에서는 **Non-pointer isa** 기술을 통해 참조 카운트 등의 부가 정보를 함께 저장하여 최적화합니다.
- **Messaging Pipeline**: `objc_msgSend` 호출 시 `Cache Lookup` → `Method List Search` → `Dynamic Resolution` → `Forwarding` 순으로 진행됩니다. 대부분의 호출은 고도로 최적화된 메서드 캐시에서 즉시 반환됩니다.
- **Method Swizzling**: 런타임에 메서드 구현(IMP)을 교체하는 기술입니다. 메인 스레드 로깅이나 분석 SDK 에서 활용되나, 현대적인 Swift/SwiftUI 환경에서는 예기치 못한 부작용을 유발하는 안티패턴으로 간주되기도 합니다.

#### 🧬 Swift Runtime & Metadata

- **Type Metadata**: Swift 는 런타임에 제네릭과 동적 타입 확인을 위한 풍부한 메타데이터를 유지합니다. 이는 ABI 안정성의 핵심 요소입니다.
- **Existential Container**: 프로토콜 타입(`any` 키워드)을 처리하기 위한 특수 구조체로, 데이터 크기에 따라 인라인 버퍼 혹은 힙 할당을 수행합니다.
- **some vs any**: Swift 5.7+ 부터는 성능 최적화(Static Dispatch 유도)를 위해 컴파일 타임에 타입이 확정되는 `some`(Opaque Type) 사용이 적극 권장됩니다.

#### 🛡️ 보안 및 성능 최적화 포인트

- **WMO (Whole Module Optimization)**: 모듈 전체를 분석하여 `internal` 수준에서도 적극적인 정적 디스패치와 인라이닝 최적화를 수행합니다.
- **@objc 의 오버헤드**: Swift 코드에 `@objc` 를 남용하면 브리징 비용과 바이너리 크기 증가를 유발하므로 Selector 가 필수적인 경우에만 제한적으로 사용해야 합니다.
- **Dynamic Casting**: `as?` 또는 `as!` 는 런타임 메타데이터 순회를 동반하므로 빈번한 루프 내에서의 사용은 지양하는 것이 좋습니다.

#### 📚 연관 문서 및 심화 학습

- [[apple-memory-management]] - 객체 레이아웃과 ARC 메모리 관리
- [[apple-uikit-lifecycle]] - UIKit 프레임워크의 생명주기와 내부 동작
- [[apple-architecture-stack]] - Darwin 커널과 Mach/BSD 계층 구조
- [[apple-foundations]] - Apple 플랫폼 공통 설계 철학
- [[apple-performance-and-debug]] - 런타임 성능 프로파일링 가이드
- [[objective-c-vs-swift-interoperability]] - Swift 와 Objective-C 의 상호 운용 및 컴파일 심층 비교
- [[mobile-security]] - 통합 모바일 보안 가이드

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
