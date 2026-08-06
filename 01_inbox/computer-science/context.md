---
title: context
tags: [computer-science, software-architecture, operating-systems]
aliases: [Context, 컨텍스트, Context Switch, Execution Context, CoroutineContext, Android Context]
date modified: 2026-08-06 16:25:00 +09:00
date created: 2026-08-06 16:25:00 +09:00
---

## Context (컨텍스트) 란 무엇인가

컴퓨터 과학과 소프트웨어 아키텍처에서 **Context (컨텍스트/맥락)** 란 **"어떤 연산, 프로세스, 작업 또는 객체가 특정 시점에 올바르게 실행되기 위해 필요한 실행 상태(Execution State) 및 주변 환경 정보의 묶음(Environment Bundle)"** 을 의미한다.

컨텍스트는 독립적으로 의미를 갖기 어려운 개별 연산에 "현재 어디서, 어떤 자원과 식별자를 가지고, 어떤 생명주기와 권한 속에서 실행 중인가"라는 맥락을 제공한다.

```
[System Environment / Runtime]
       │
       ▼
┌────────────── Context (Environment Bundle) ──────────────┐
│  - Execution State (PC, Registers, Stack Pointer)         │
│  - System Resources (File Descriptors, DB Handle, Memory) │
│  - Environment & Identity (User Auth, Locale, Scope ID)  │
└──────────────────────────────────────────────────────────┘
       │
       ▼
[Task / Execution Unit] (연산 수행)
```

---

## 컴퓨터 과학 영역별 Context 의 구체적 정의

### 1. 운영체제 (OS): Process & Thread Context
운영체제에서 컨텍스트는 프로세스나 스레드가 CPU를 점유하여 실행되다가 스케줄링에 의해 인터럽트될 때, 나중에 **동일한 상태로 복원하여 재개(Resume)** 할 수 있도록 저장하는 CPU 레지스터 및 상태 정보 구조체이다.
- **포함 정보**: Program Counter (PC), CPU General Registers, Stack Pointer (SP), Memory Management Unit (MMU) Page Table Pointer 등.
- **Context Switch (문맥 교환)**: CPU가 한 프로세스/스레드에서 다른 프로세스/스레드로 제어권을 넘길 때 이전 Context를 PCB/TCB에 저장하고 새로운 Context를 로드하는 작업.

### 2. 코루틴/동시성 프로그래밍: CoroutineContext
Kotlin Coroutines 등 현대 비동기 프로그래밍 모델에서 `CoroutineContext`는 비동기 작업(코루틴)의 실행 환경을 구성하는 요소들의 집합(Indexed Set)이다.
- **포함 요소**:
  - `Job`: 코루틴의 생명주기와 제어(취소, 상태 감시). [Structured Concurrency](structured-concurrency.md) 계층 구조 형성.
  - `CoroutineDispatcher`: 작업이 실행될 스레드 풀 지정 (e.g., `Dispatchers.IO`, `Dispatchers.Main`).
  - `CoroutineExceptionHandler`: Uncaught Exception 처리기.
  - `CoroutineName`: 디버깅용 코루틴 이름.

### 3. 애플리케이션 프레임워크: Android Context
안드로이드 OS에서 `android.content.Context`는 애플리케이션의 현재 상태 및 시스템 환경에 대한 글로벌 정보 접근 인터페이스(Abstract Class)이다.
- **제공 기능**: 리소스 접근 (`getString()`, `getDrawable()`), 데이터베이스/파일 접근 (`openFileInput()`), 시스템 서비스 획득 (`getSystemService()`), 컴포넌트 시작 (`startActivity()`).
- **종류**: `ApplicationContext` (앱 전역 생명주기), `ActivityContext` (UI 및 화면 생명주기), `ServiceContext` 등.

---

## Context 가 남용되는 이유와 문제점 (Anti-Patterns)

`Context` 개념은 시스템 자원에 대한 편리한 접근 통로를 제공하지만, 설계 관점에서 쉽게 **God Object (신 객체)** 및 오남용 패턴으로 변질되기 쉽다.

### 1. God Object (신 객체) 화
Context 가 모든 상태와 서비스를 담는 통로 역할을 하다 보니, 개발자가 의존성을 명확히 나눈 객체를 설계하는 대신 Context 통째로 클래스에 전달하는 만능 열쇠(Master Key)처럼 사용하는 경향이 생긴다.

### 2. 암묵적 의존성 (Implicit Dependency) 과 테스트 격리 저해
클래스가 동작하기 위해 실제 필요한 최소 의존성(예: `UserRepository`, `NotificationSender`) 대신 전체 `Context`를 넘겨받으면:
- 해당 클래스가 내부에서 Context 의 어느 기능을 사용하는지 인터페이스만 보고 파악할 수 없다.
- 단위 테스트(Unit Test) 작성 시 Context 전체를 Mocking 해야 하므로 테스트가 극도로 복잡해진다. [Pure Function](pure-function.md) 원칙 위반.

### 3. 생명주기 불일치에 따른 메모리 누수 (Memory Leak)
특히 Android 환경에서 짧은 생명주기를 가진 `Activity Context`의 참조를 장기 실행 비동기 작업, 싱글톤 객체 또는 백그라운드 스레드에 보관하면, 화면이 파괴되어도 메모리에서 해제되지 않는 심각한 메모리 누수가 발생한다.

---

## Context 를 올바르게 구조화하고 다루는 원칙

```
[Bad: 만능 Context 직접 참조]
Service Class ───(Context 전체 의존)───> [God Context] ───> System API, Resources, DB...

[Good: 캡슐화 및 최소 권한 인터페이스 제공]
Service Class ───(필요한 인터페이스만 주입)───> Interface (e.g., ResourceProvider, StringResolver)
```

### 1. 명시적 의존성 주입 (Explicit Dependency Injection)
단순 자원 획득을 위해 Context 전체를 전달하지 말고, 해당 객체가 **실제로 필요한 구체적 의존성(Narrow Interface 또는 데이터 객체)** 을 DI (Dependency Injection) 로 직접 전달한다.
- Bad: `fun processOrder(context: Context, orderId: String)`
- Good: `fun processOrder(paymentGateway: PaymentGateway, stringResolver: StringResolver, orderId: String)`

### 2. 인터페이스 분리 원칙 (Interface Segregation Principle, ISP) 적용
Context 가 가진 수많은 책임 중 특정 레이어에 필요한 최소한의 인터페이스로 추상화하여 분리한다. (예: UI 리소스 읽기 전용 인터페이스 `ResourceProvider`, 로거 인터페이스 `LoggerContext`).

### 3. Scope 와 생명주기(Lifetime) 의 명확한 구분
Context 의 생명주기가 그것을 소비하는 객체의 생명주기보다 긴지/짧은지 엄격히 관리한다.
- 긴 생명주기 객체가 짧은 생명주기 Context 를 참조해야 할 경우, WeakReference 를 사용하거나 생명주기 수명 종료 시점에 참조를 해제해야 한다.
- 코루틴 환경에서는 Parent-Child 생명주기가 올바르게 연결되도록 [Structured Concurrency](structured-concurrency.md) 범주 내에서 `CoroutineContext`를 상속 및 전달한다.

---

## 관련 노트
- [Structured Concurrency](structured-concurrency.md)
- [Pure Function](pure-function.md)
- [Immutability](immutability.md)
