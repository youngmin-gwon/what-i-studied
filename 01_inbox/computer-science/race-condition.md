---
title: race-condition
tags: [computer-science, concurrency, thread-safety, synchronization, bug]
aliases: [Race Condition, 경쟁 상태, Data Race, Lost Update]
date modified: 2026-08-10 00:00:00 +09:00
date created: 2026-08-10 00:00:00 +09:00
---

## Race Condition (경쟁 상태)

**Race Condition (경쟁 상태)**은 멀티스레드 환경에서 두 개 이상의 스레드가 공유 자원에 동시에 접근하여 조작할 때, 실행 순서(Timing/Interleaving)에 따라 연산의 최종 결과가 달라지는 비결정론적 오류 상태입니다.

---

### 초보자를 위한 쉽게 이해하는 비유

**Race Condition (경쟁 상태)**: **"공용 노트에 두 사람이 동시에 글 쓰기"**

A와 B가 서로 상대방의 글을 확인하지 않고 동시에 숫자를 읽고 `+1`을 적다 보면, 한 사람의 작업 기록이 지워지는(Lost Update) 데이터 오염 버그가 생깁니다.

---

## Race Condition의 정의 및 특징

### 무엇이 Race Condition인가?

```
여러 스레드 → 공유 자원 (동시 접근) → 타이밍 의존 → 비결정론적 결과
```

### 발생 조건

Race Condition이 발생하려면:

1. **여러 스레드**: 2개 이상의 스레드/프로세스 존재
2. **공유 자원**: 메모리, 변수, 파일 등의 공유 자원 접근
3. **동기화 부재**: Mutex/Lock 없이 직접 접근
4. **동시 실행**: 같은 시점에 실행되는 경우

---

## Race Condition vs Data Race

| 비교 항목 | Race Condition | Data Race |
|---------|----------------|----------|
| **정의 수준** | 비즈니스 로직 수준 | 언어/메모리 모델 수준 |
| **범위** | 넓음 (타이밍 문제 전체) | 좁음 (메모리 접근만) |
| **발생 원인** | 동기화 로직 오류, 타이밍 의존 | 동기화 메커니즘 부재 |
| **예시** | 계좌 이체 금액 오류 | 같은 메모리 위치에서 R/W 충돌 |
| **해결 방법** | Mutex, 불변성, 원자적 연산 | 올바른 동기화 사용 |

---

## Race Condition 발생의 메커니즘: Lost Update Bug

```
스레드 A와 스레드 B가 count = 0 을 +1씩 증가시키는 경우
```

### 올바른 순서 (Synchronization 적용)

```
Thread A: Read count (0) → Write count (1) → [완료]
Thread B: Read count (1) → Write count (2) → [완료]
최종 결과: count = 2 ✅
```

### Race Condition 발생 (동기화 없음)

```
Thread A: Read count (0)
Thread B: Read count (0)         ← 두 스레드 모두 0을 읽음
Thread A: Write count (0+1=1)
Thread B: Write count (0+1=1)    ← 중복 쓰기!
최종 결과: count = 1 ❌ (2여야 함)
```

이 현상을 **Lost Update Bug** 또는 **Write-After-Write Conflict**라고 합니다.

---

## Race Condition의 실제 예시

### 1. 은행 계좌 송금 (Lost Update)

```kotlin
// ❌ Race Condition 발생
var balance = 1000

fun withdraw(amount: Int) {
    val current = balance    // 읽기
    balance = current - amount // 쓰기 (원자적 아님)
}

// Thread A와 B가 동시에 100씩 출금
// A: Read(1000) → B: Read(1000) → A: Write(900) → B: Write(900)
// 결과: balance = 900 (1800이어야 함)
```

### 2. 카운팅 오류

```kotlin
// ❌ Race Condition
var counter = 0

fun increment() {
    counter++  // 읽기-수정-쓰기 3단계 (원자적 아님)
}

// 100개 스레드가 각각 1씩 증가 → 결과는 100보다 훨씬 작을 수 있음
```

---

## Race Condition의 영향 범위

### 메모리 수준 (하위 레벨)

```
메모리 주소에 대한 읽기/쓰기 경쟁
→ 불일치한 상태, 부분 업데이트
```

### 비즈니스 로직 수준 (상위 레벨)

```
거래 금액 계산, 재고 관리, 사용자 데이터 동기화
→ 금전 손실, 데이터 불일치
```

---

## Race Condition 해결 전략

### 1. Mutex / Lock 적용 (동기화)

```kotlin
// ✅ Synchronized 블록
val lock = ReentrantLock()
var counter = 0

fun incrementSafe() {
    lock.withLock {
        counter++  // 한 번에 한 스레드만 실행
    }
}
```

### 2. Immutability (불변성)

```kotlin
// ✅ 불변 객체는 Race Condition 불가능
data class Account(
    val balance: Int  // final, 변경 불가
)

fun withdraw(account: Account, amount: Int): Account {
    return account.copy(balance = account.balance - amount)
}
```

### 3. Atomic 연산

```kotlin
// ✅ 원자적 연산 (Lock 없음)
import java.util.concurrent.atomic.AtomicInteger

val counter = AtomicInteger(0)

fun incrementAtomic() {
    counter.incrementAndGet()  // CAS(Compare-And-Swap) 기반
}
```

### 4. Thread-safe 컬렉션

```kotlin
// ✅ Thread-safe 컬렉션 사용
val list = Collections.synchronizedList(mutableListOf<Int>())
val map = ConcurrentHashMap<String, Int>()

list.add(1)  // 내부적으로 동기화됨
map["key"] = 1
```

### 5. Actor 모델 (메시지 패싱)

```kotlin
// ✅ 공유 상태 제거
actor<Int> {
    var counter = 0
    for (msg in channel) {
        when (msg) {
            is Increment -> counter++
            is Get -> sendReply(counter)
        }
    }
}
```

---

## Race Condition 디버깅 팁

### 재현의 어려움

```
Race Condition은 타이밍에 따라 발생/미발생
→ 수작업 테스트로 재현하기 어려움
```

### 디버깅 방법

1. **Stress Testing**: 많은 스레드로 반복 실행
```bash
for i in {1..1000}; do run_test; done
```

2. **ThreadSanitizer/Helgrind** 사용 (C/C++)
```bash
valgrind --tool=helgrind ./program
```

3. **Java Flight Recorder** (Java)
```bash
jcmd <pid> JFR.start
```

4. **로깅 추가** (조심스럽게)
```
로깅 자체가 타이밍을 바꿀 수 있음 (Heisenbug)
```

---

## Race Condition의 예방 체크리스트

| 항목 | 체크 사항 |
|------|---------|
| **공유 상태** | 여러 스레드가 접근하는 상태가 있는가? |
| **쓰기 작업** | 공유 상태에 대한 쓰기가 있는가? |
| **동기화** | Mutex/Lock이 적용되었는가? |
| **원자성** | 다중 단계 작업이 원자적인가? |
| **테스트** | Stress test를 실행했는가? |

---

## 연결 문서 (Related Documents)

- [Mutex/Lock](mutex-lock.md) - 상호 배제를 통한 Race Condition 해결
- [Deadlock](deadlock.md) - 잘못된 Lock 사용으로 인한 교착 상태
- [Immutability](immutability.md) - 불변성을 통한 근본적 해결
- [Pure Function](pure-function.md) - 상태 변이를 최소화하는 설계
- [Structured Concurrency](structured-concurrency.md) - 안전한 동시성 제어
