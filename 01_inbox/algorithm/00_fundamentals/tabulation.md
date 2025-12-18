---
title: tabulation
tags: [algorithm, dp, fundamentals, tabulation, optimization, iteration]
aliases: [타블레이션, 도표 채우기, 바텀업]
date modified: 2025-12-18 19:17:00 +09:00
date created: 2025-12-18 19:17:00 +09:00
---

## 타블레이션 (Tabulation) 이란?

타블레이션은 **작은 하위 문제부터 시작하여 차례대로 테이블(Table)을 채워나가며 최종적인 답을 구하는 최적화 기법**이다. **[동적 계획법 (DP)](../02_algorithms/dynamic-programming.md)** 의 **Bottom-Up** 방식에서 핵심적으로 사용된다.

### 💡 Why it matters (Context)

- **안정성**: 재귀를 사용하지 않으므로 스택 오버플로우(Stack Overflow) 걱정이 없다.
- **성능**: 함수 호출 오버헤드가 없어 일반적으로 **[메모이제이션 (Memoization)](memoization.md)** 보다 속도가 빠르다.
- **예측 가능성**: 모든 부분 문제를 순서대로 해결하므로 실행 시간을 정확히 예측하기 쉽다.

### 직관적인 비유
- **벽돌 쌓기**: 1 층부터 한 장 한 장 벽돌을 쌓아 100 층 빌딩을 올리는 것과 같다. 기초부터 탄탄히 쌓아 올라가야 최종 목표인 100 층에 도달할 수 있다.

---

## 타블레이션의 작동 원리

1. **테이블 설계**: 문제의 상태를 저장할 1 차원 또는 2 차원 배열(Table)을 준비한다.
2. **초기값 설정**: 가장 작은 문제(Base Case)의 답을 테이블에 미리 채워넣는다. (예: `dp[0] = 0`, `dp[1] = 1`)
3. **반복문 수행**: 루프를 돌며 점화식에 따라 테이블의 다음 칸을 채워나간다.
4. **결과 반환**: 테이블의 마지막 칸(또는 목표 인덱스)에 저장된 값이 최종 정답이 된다.

---

## 💻 코드 예시: 피보나치 수열 (Python)

반복문을 사용하여 `0` 번 인덱스부터 `n` 번 인덱스까지 차례대로 값을 채운다.

```python
def fib_tab(n):
    # 1. 기저 사례 처리
    if n <= 1: return n
    
    # 2. 테이블(배열) 준비
    fib_table = [0] * (n + 1)
    
    # 3. 초기값 설정 (Base Case)
    fib_table[1] = 1
    
    # 4. 차례대로 테이블 채우기 (Bottom-Up)
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i-1] + fib_table[i-2]
    
    # 5. 최종 결과 반환
    return fib_table[n]
```

---

## ⚖️ 타블레이션 vs 메모이제이션

두 기법은 모두 중복 계산을 피하기 위해 결과를 저장하지만, 접근 방향이 정반대이다.

| 특징 | 타블레이션 (Tabulation) | 메모이제이션 (Memoization) |
| :--- | :--- | :--- |
| **방향** | Bottom-Up (작은 것 → 큰 것) | Top-Down (큰 것 → 작은 것) |
| **기법** | 반복문 (Iteration) | 재귀 (Recursion) |
| **장점** | 스택 안전, 오버헤드 적음 | 필요한 부분만 계산 (Sparse DP 에 유리) |
| **단점** | 불필요한 부분 문제까지 모두 계산 | 스택 오버플로우 위험, 호출 비용 발생 |

---

## 📚 관련 문서
- [동적 계획법 (DP)](../02_algorithms/dynamic-programming.md): 타블레이션이 구현되는 대표적인 알고리즘 패러다임.
- [메모이제이션 (Memoization)](memoization.md): 타블레이션과 대비되는 최적화 기법.
- [재귀와 호출 스택](recursion-and-stack.md): 타블레이션이 재귀의 한계를 극복하는 방식.
