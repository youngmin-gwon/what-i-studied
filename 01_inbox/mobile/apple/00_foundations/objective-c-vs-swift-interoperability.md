---
title: objective-c-vs-swift-interoperability
tags: [apple, interoperability, objective-c, runtime, swift]
aliases: []
date modified: 2026-04-07 18:59:07 +09:00
date created: 2026-04-07 19:10:00 +09:00
---

## [[apple-runtime-and-swift]] > Objective-C vs Swift: Interoperability & Compilation

Apple 플랫폼의 두 주요 언어인 Objective-C 와 Swift 가 어떻게 공존하며, 바이너리 수준에서 어떻게 상호 호환성을 구현하는지 심층 비교 분석합니다.

### 1. 📂 설계 철학 및 패러다임 비교

| 특징 | Objective-C | Swift |
| :--- | :--- | :--- |
| **기반** | C 언어의 확장이자 Smalltalk 스타일 메시징 | 현대적, 안전 지향, 모듈 중심 |
| **타입 시스템** | 동적 (Dynamic) | 정적 (Static) / 강한 타입 체크 |
| **호출 메커니즘** | **Message Dispatch** (Runtime 중심) | **Static/Table Dispatch** (Compiler 중심) |
| **메모리 관리** | ARC (Automatic Reference Counting) | ARC (Objective-C 보다 더 엄격한 소유권 모델) |

### 2. ⚙️ Compilation Process & Binary Level

두 언어는 모두 **LLVM**을 백엔드로 사용하지만, 프론트엔드 처리 과정에서 큰 차이를 보입니다.

#### 🏗️ Objective-C (Clang Pipeline)

1. **Preprocessor**: 매크로(`#define`) 및 헤더(`#import`) 처리.
2. **Clang Frontend**: 코드를 구문 분석하여 AST(Abstract Syntax Tree)를 생성.
3. **LLVM IR Generation**: LLVM 중간 표현으로 변환. 이때 dynamic dispatch 를 위한 `objc_msgSend` 호출이 삽입됨.
4. **Mach-O Binary**: 클래스 데이터가 `__objc_` 섹션에 저장됨.

#### 🏗️ Swift (Swift Compiler Pipeline)

1. **Swift Frontend**: 소스 코드 분석.
2. **SIL (Swift Intermediate Language) Generation**: **Swift 전용** 고수준 중간 언어. 여기서 제네릭 특수화(Specialization), 참조 카운팅 최적화, 정격 검사가 수행됨.
3. **LLVM IR Generation**: SIL 을 LLVM IR 로 변환.
4. **Mach-O Binary**: Swift 메타데이터와 정적 디스패치 주소가 생성됨.

### 3. 🌉 Interoperability Mechanisms (상호 운용)

Apple 은 앱 개발자가 두 언어를 한 프로젝트에서 섞어 쓸 수 있도록 강력한 브리징 기술을 제공합니다.

#### 🔹 Swift -> Objective-C (Swift 에서 ObjC 사용)

- **Bridging Header**: `#import "MyObjcFile.h"` 가 포함된 헤더 파일을 통해 Swift 컴파일러에게 ObjC 클래스를 노출합니다.
- **Clang Importer**: Swift 컴파일러 내부의 이 모듈은 ObjC 헤더를 Swift 인터페이스로 자동 변환합니다. (예: `initWithString:` -> `init(string:)`)

#### 🔹 Objective-C -> Swift (ObjC 에서 Swift 사용)

- **Generated Header**: Swift 컴파일러는 프로젝트 이름에 맞춘 `-Swift.h` 파일을 자동 생성합니다.
- **@objc & NSObject**: Swift 클래스가 ObjC 에서 인식되려면 `NSObject` 를 상속하거나 클래스/메서드에 `@objc` 속성을 붙여야 합니다. 이는 ObjC 런타임이 이해할 수 있는 메타데이터를 추가로 생성함을 의미합니다.

### 4. 🧩 Runtime Interoperability (바이너리 수준의 동작)

- **Thunks (변환 코드)**: Swift 의 메서드가 ObjC 런타임(메시징)을 통해 호출될 때, 컴파일러는 **Thunk**라는 작은 중계 코드를 생성합니다. 이 Thunk 는 ObjC 의 `id` 타입을 Swift 의 구체 타입으로 변환하거나 그 반대의 작업을 수행하여 두 세계를 연결합니다.
- **V-Table vs Message Dispatch**:
    - Swift 전용 클래스는 **V-Table**을 사용해 정적/함수 포인터 방식으로 호출됩니다.
    - `NSObject` 상속 클래스에서 `dynamic` 키워드를 사용하면 Swift 메서드도 ObjC 의 `objc_msgSend` 를 통해 호출되도록 강제할 수 있습니다. (KVO 및 Method Swizzling 지원을 위해 필요)

### 5. 🚀 성능 및 바이너리 영향

- **Bridging Cost**: Swift 와 ObjC 사이를 오갈 때(예: `String` <-> `NSString`), 값 타입과 참조 타입 사이의 변환 비용(Bridging cost)이 발생할 수 있습니다.
- **Binary Size**: `@objc` 를 남발하면 ObjC 런타임에 등록하기 위한 추가적인 메타데이터와 Thunk 코드로 인해 바이너리 크기가 증가합니다.

### 📚 연관 문서

- [[apple-runtime-and-swift]] - 런타임 내부 동작 원리
- [[apple-foundations]] - Apple 플랫폼 공통 설계 철학
