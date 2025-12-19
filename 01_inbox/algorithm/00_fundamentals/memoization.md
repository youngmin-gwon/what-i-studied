---
title: memoization
tags: [algorithm, dp, fundamentals, memoization, optimization, recursion]
aliases: [기억하며 풀기, 메모이제이션, 캐싱]
date modified: 2025-12-19 18:08:41 +09:00
date created: 2025-12-18 19:07:00 +09:00
---

## 메모이제이션 (Memoization) 이란?

메모이제이션은 **한 번 계산한 결과를 메모리에 저장해두었다가, 같은 계산이 필요할 때 다시 계산하지 않고 저장된 값을 꺼내 쓰는 최적화 기법**이다.

### 💡 Why it matters (Context)

- **시간 복잡도 단축**: 기하급수적으로 늘어나는 중복 계산을 선형 시간으로 줄일 수 있다. (예: $O(2^n) \to O(n)$)
- **Top-Down DP 의 핵심**: 재귀 알고리즘의 비효율성을 해결하는 가장 강력한 도구이다.

### 직관적인 비유
- **수학 문제 풀기**: 7 x 8 이 얼마인지 물었을 때, 매번 7 을 8 번 더하는 대신 "56"이라는 답을 머릿속에 **기억(Memo)** 해두는 것과 같다. 다음에 7 x 8 이 나오면 즉시 대답할 수 있다.

---

## 메모이제이션의 작동 원리

1. **상태 정의**: 문제의 입력값(입력 파라미터)을 확인한다.
2. **저장소 준비**: 입력값에 따른 결과를 저장할 테이블(배열, 리스트, 해시 맵 등)을 만든다.
3. **로직 흐름**:
   - 함수 호출 시, 먼저 저장소에 해당 입력값의 결과가 있는지 확인한다.
   - **있다면**: 저장된 값을 즉시 반환한다. (**Cache Hit**)
   - **없다면**: 원래의 로직대로 계산을 수행하고, 결과를 저장소에 기록한 뒤 반환한다. (**Cache Miss**)

---

## 💻 코드 예시: 피보나치 수열 (Python)

### 1. 일반 재귀 (Memoization 미적용)

중복 호출이 기하급수적으로 발생하여 `n` 이 커지면 매우 느려진다 ($O(2^n)$).

```python
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```

### 2. 메모이제이션 적용

한 번 구한 값은 `memo` 딕셔너리에 저장된다 ($O(n)$).

```python
def fib_memo(n, memo={}):
    # 1. 기저 사례
    if n <= 1: return n
    
    # 2. 이미 계산한 적이 있는지 확인 (Cache Hit)
    if n in memo:
        return memo[n]
    
    # 3. 계산 후 저장 (Cache Miss)
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
```

---

## ⚖️ 메모이제이션 vs 타블레이션 (Tabulation)

메모이제이션은 주로 **[동적 계획법 (DP)](../02_algorithms/dynamic-programming.md)** 의 Top-Down 방식에서 사용된다.

| 특징     | 메모이제이션 (Memoization) | 타블레이션 (Tabulation)                       |
| :----- | :------------------- | :--------------------------------------- |
| **방향** | Top-Down (위에서 아래로)   | **[Bottom-Up (아래에서 위로)](tabulation.md)** |
| **구현** | 재귀 (Recursion)       | 반복문 (Loop)                               |
| **특징** | 필요한 부분 문제만 계산 가능     | 모든 부분 문제를 순서대로 계산                        |
| **위험** | 스택 오버플로우 가능성         | 상대적으로 안전하고 빠름                            |

---

## 📚 관련 문서

- [동적 계획법 (DP)](../02_algorithms/dynamic-programming.md): 메모이제이션을 활용한 최적화의 대표 사례.
- [타블레이션 (Tabulation)](tabulation.md): 메모이제이션과 대비되는 최적화 기법.
- [재귀와 호출 스택](recursion-and-stack.md): 메모이제이션이 해결하고자 하는 재귀의 한계.
