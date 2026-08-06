---
title: race-condition-and-deadlock
tags: [computer-science, concurrency, thread-safety, synchronization]
aliases: [Race Condition, Deadlock, Mutex, Lock, 경쟁 상태, 데드락, 뮤텍스, Coffman Conditions]
date modified: 2026-08-06 16:25:00 +09:00
date created: 2026-08-06 16:25:00 +09:00
---

## 핵심 개념 정의

동시성(Concurrency) 및 멀티스레드 프로그래밍 환경에서 **Race Condition (경쟁 상태)**, **Mutex/Lock (상호 배제)**, **Deadlock (데드락/교착 상태)** 은 스레드 안전성(Thread Safety)을 위협하거나 동기화를 위해 반드시 이해해야 하는 핵심 개념들이다.

```
[Race Condition]
Thread A: Read count (0) ───────> Add 1 ───────> Write count (1)  (Lost Update 발생!)
Thread B: Read count (0) ── Add 1 ── Write count (1)

[Mutex Solution]
Thread A: Acquire Lock ──> Read/Modify/Write ──> Release Lock
Thread B:                  (Wait for Lock...)  ──> Acquire Lock ──> Read/Modify/Write

[Deadlock]
Thread A (Holds Lock 1) ────(Wants Lock 2)────> [Lock 2 held by Thread B]
Thread B (Holds Lock 2) ────(Wants Lock 1)────> [Lock 1 held by Thread A]
(서로 락 해제를 기다리며 무한 대기)
```

---

## 1. Race Condition (경쟁 상태)

### 정의
두 개 이상의 프로세스나 스레드가 공유 자원(Shared Resource)에 동시에 접근하여 읽고 쓰는 작업을 수행할 때, **실행 순서(Timing / Interleaving)에 따라 연산의 최종 결과가 달라지는 비결정론적(Non-deterministic) 오류 상태**이다.

### Data Race 와의 차이점
- **Data Race (데이터 경쟁)**: 동기화(Synchronization) 없이 둘 이상의 스레드가 동일한 메모리 위치에 동시에 접근하고, 그 중 적어도 하나가 쓰기(Write) 연산인 경우를 의미하는 C++/Java 언어 스펙상의 명확한 하위 개념이다.
- **Race Condition**: 비즈니스 로직 수준의 제약 조건이나 실행 순서상의 경쟁으로 인한 더 넓은 범위의 결함을 의미한다. (Data Race 가 없더라도 Race Condition 이 발생할 수 있다).

---

## 2. Mutex / Lock (상호 배제)

### 정의
**Mutex (Mutual Exclusion, 상호 배제)** 및 **Lock** 은 임계 영역(Critical Section)에 동시에 단 하나의 스레드만 진입할 수 있도록 제어하는 동기화 메커니즘이다.

### 특징
- **소유권 (Ownership)**: Mutex 는 락을 획득(Acquire/Lock)한 스레드만이 그 락을 해제(Release/Unlock)할 수 있는 소유권 개념을 가진다. (바이너리 세마포어와의 핵심 차이).
- **상태**: Lock 상태(진입 불가능)와 Unlock 상태(진입 가능) 2가지 상태만을 가진다.

---

## 3. Deadlock (데드락 / 교착 상태)

### 정의
두 개 이상의 프로세스나 스레드가 서로가 소유한 자원(락)을 얻기 위해 기다리며 **모든 관련 작업의 진행이 영구적으로 멈추어 버리는 상태**이다.

---

## Deadlock 발생의 4가지 필요충분 조건 (Coffman Conditions)

데드락은 다음 **4가지 코프만(Coffman) 조건이 동시에 모두 성립**할 때만 발생한다:

1. **상호 배제 (Mutual Exclusion)**:
   - 한 번에 한 프로세스/스레드만 자원을 사용할 수 있음 (공유 불가능한 자원).
2. **점유와 대기 (Hold and Wait)**:
   - 자원을 이미 보유(Hold)한 프로세스가 다른 자원을 추가로 요구하며 대기(Wait)함.
3. **비선점 (No Preemption)**:
   - 다른 프로세스가 보유한 자원을 강제로 빼앗을(Preempt) 수 없으며, 해당 프로세스가 스스로 해제할 때까지 기다려야 함.
4. **순환 대기 (Circular Wait)**:
   - 대기 프로세스들이 순환 링 형태로 자원을 요구함 ($P_0$은 $P_1$의 자원을, $P_1$은 $P_2$의 자원을, $P_n$은 $P_0$의 자원을 대기).

---

## 개념 간 차이점 종합 비교

| 구분 | Race Condition (경쟁 상태) | Deadlock (교착 상태) |
| :--- | :--- | :--- |
| **발생 원인** | 동기화 부족으로 실행 순서가 무작위 변경됨 | 과도하거나 잘못된 순서의 락 점유 대기 |
| **프로그램 상태** | 스레드들이 계속 실행되며 **잘못된 데이터 생성** | 스레드들이 차단(Blocked)되어 **아무것도 진행 안 됨** |
| **증상** | 비결정론적 데이터 오염, 묵묵히 버그 발생 | 시스템 멈춤 (Hang/Freeze), 무한 대기 |
| **주요 해결책** | Mutex/Lock 적용, [Immutability](immutability.md), Atomic 연산 | Lock 획득 순서 정렬, 타임아웃, Lock 범위 최소화 |

---

## 방지 및 해결 전략 (Prevention & Mitigation Strategies)

### 1. Immutability (불변성) 활용
[Immutability](immutability.md) 객체는 상태가 변경되지 않고 읽기 전용이므로, Lock 이나 Mutex 없이도 Race Condition 및 Data Race 를 100% 근본적으로 예방한다.

### 2. Lock Ordering (락 순서 정렬) - Circular Wait 파괴
시스템 내의 모든 자원/락에 고유한 순서(Hierarchy ID)를 부여하고, 반드시 정해진 동일한 순서대로만 락을 획득하도록 규정하여 Circular Wait 조건을 완벽히 해제한다.
```
// Always Acquire Lock A before Lock B
synchronized(lockA) {
    synchronized(lockB) {
        // Critical Section
    }
}
```

### 3. Lock-free / Atomic 연산 사용
Hardware Atomic Instruction (e.g., CAS - Compare-And-Swap) 기반의 `AtomicInteger`, `AtomicReference` 등을 사용하여 Mutex Lock 없이도 안전하게 카운팅 및 상태 변경을 수행한다.

### 4. Timeout 및 Lock 획득 시도 (Hold and Wait / No Preemption 파괴)
`tryLock(timeout)` 기법을 사용하여 일정 시간 내에 락을 획득하지 못하면 이미 소유한 락을 스스로 해제하고 재시도하거나 에러를 반환한다.

### 5. 은행원 알고리즘 (Banker's Algorithm) 및 교착 상태 감시
- **데드락 회피 (Avoidance)**: 자원 할당 전 시스템이 안전 상태(Safe State)를 유지할 수 있는지 미리 계산하여 할당 여부를 결정 (은행원 알고리즘).
- **데드락 감지 및 복구 (Detection & Recovery)**: 자원 할당 그래프(Resource Allocation Graph)를 주기적으로 분석하여 교착 상태 발생 시 스레드를 강제 종료하거나 락을 선점(Preempt) 복구.

---

## 관련 노트
- [Structured Concurrency](structured-concurrency.md)
- [Immutability](immutability.md)
- [Context](context.md)
- [Pure Function](pure-function.md)
