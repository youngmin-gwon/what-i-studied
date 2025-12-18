---
title: dynamic-programming
tags: [algorithm, dp, dynamic-programming, memoization, optimization]
aliases: [DP, 동적 계획법, 다이나믹 프로그래밍, Memoization]
date modified: 2025-12-18 11:43:01 +09:00
date created: 2025-12-18 11:43:01 +09:00
---

## Dynamic Programming: "기억하며 최적화하기"

**핵심**: "같은 계산을 반복하지 말고 **기억(저장)**하자!"

동적 계획법은 **큰 문제를 작은 부분 문제로 나누고**, 그 결과를 **재사용**하여 효율적으로 푸는 기법입니다.

### 💡 Why it matters (Context)

- **피보나치 수열**: 재귀로 풀면 `O(2^n)` → DP로 `O(n)`
- **최단 경로**: 모든 가능한 경로 탐색 → DP로 최적 경로만
- **자원 할당**: 제한된 예산으로 최대 수익
- **문자열 편집**: 두 문자열을 같게 만드는 최소 연산

---

### 🏢 실무 사례

#### DP 활용
- **Google/Facebook 뉴스피드**: 최적 콘텐츠 조합 선택 (0/1 Knapsack)
- **Spotify 추천 알고리즘**: 사용자 취향 매칭 (LCS 변형)
- **Git Diff**: 두 파일 차이 최소화 (Edit Distance)
- **Stock Trading 알고리즘**: 주식 매매 최대 수익 (State Machine DP)
- **Image Compression (JPEG)**: 최적 양자화 테이블 (DP 최적화)
- **네트워크 라우팅**: 최소 비용 경로 (Bellman-Ford = DP)
- **비디오 스트리밍 (YouTube)**: 적응형 비트레이트 선택

---

## 🔑 DP의 핵심 2가지 조건

DP를 쓸 수 있으려면 다음 두 가지가 **반드시** 필요합니다:

### 1. **Optimal Substructure (최적 부분 구조)**

"큰 문제의 최적 해가 작은 문제의 최적 해로 구성됨"

```
피보나치 예:
F(5) = F(4) + F(3)
     = [F(3) + F(2)] + [F(2) + F(1)]
```

### 2. **Overlapping Subproblems (중복 부분 문제)**

"같은 작은 문제가 **여러 번** 등장함"

```
F(5) 계산 시:
  F(3)이 2번, F(2)가 3번 계산됨!
  → 저장해두면 재계산 불필요
```

---

## 🎯 DP의 2가지 접근법

### 1️⃣ Top-Down (Memoization) - 재귀 + 캐싱

"필요할 때 계산하고 저장"

```python
# 피보나치 - Top-Down
def fib_memo(n, memo={}):
    if n <= 1:
        return n
    
    # 이미 계산했으면 바로 리턴
    if n in memo:
        return memo[n]
    
    # 계산 후 저장
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# O(2^n) → O(n) 으로 개선!
```

**장점**:
- 직관적 (재귀 그대로)
- 필요한 것만 계산

**단점**:
- 재귀 스택 오버플로우 위험
- 함수 호출 오버헤드

---

### 2️⃣ Bottom-Up (Tabulation) - 반복문 + 테이블

"작은 것부터 차례대로 계산"

```python
# 피보나치 - Bottom-Up
def fib_tab(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    # 작은 것부터 채우기
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

**장점**:
- 스택 오버플로우 없음
- 보통 더 빠름 (함수 호출 X)

**단점**:
- 모든 부분 문제를 계산 (불필요한 것도)

---

## 🔥 필수 DP 패턴

### Pattern 1: 1D DP - Climbing Stairs

**문제**: N계단을 오르는데, 1칸 또는 2칸씩 올라갈 수 있다. 방법의 수는?

```python
def climb_stairs(n):
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1  # 1칸 가는 방법: 1가지
    dp[2] = 2  # 2칸 가는 방법: 2가지 (1+1, 2)
    
    for i in range(3, n + 1):
        # 현재 칸은 "1칸 전" 또는 "2칸 전"에서 올 수 있음
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# 공간 최적화 버전 - O(1) Space
def climb_stairs_opt(n):
    if n <= 2:
        return n
    
    prev2, prev1 = 1, 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1
```

**점화식**: `dp[i] = dp[i-1] + dp[i-2]`

---

### Pattern 2: 2D DP - Longest Common Subsequence (LCS)

**문제**: 두 문자열의 최장 공통 부분 수열

```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                # 같으면: 이전 LCS + 1
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # 다르면: 둘 중 더 긴 것
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# "ABCDE", "ACE" → 3 (ACE)
```

**DP 테이블 시각화**:
```plaintext
    ""  A  C  E
""   0  0  0  0
A    0  1  1  1
B    0  1  1  1
C    0  1  2  2
D    0  1  2  2
E    0  1  2  3  ← 답: 3
```

---

### Pattern 3: 0/1 Knapsack (배낭 문제)

**문제**: 용량 W인 가방에 (무게, 가치) 물건들을 넣어 최대 가치

```python
def knapsack(weights, values, capacity):
    n = len(weights)
    # dp[i][w] = 첫 i개 물건, 용량 w일 때 최대 가치
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # 현재 물건의 무게/가치
            weight, value = weights[i-1], values[i-1]
            
            if weight <= w:
                # 넣을 수 있으면: max(넣기, 안 넣기)
                dp[i][w] = max(
                    dp[i-1][w],              # 안 넣기
                    dp[i-1][w-weight] + value  # 넣기
                )
            else:
                # 못 넣으면: 이전 값 그대로
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

# 공간 최적화: O(W) Space
def knapsack_opt(weights, values, capacity):
    dp = [0] * (capacity + 1)
    
    for weight, value in zip(weights, values):
        # 뒤에서부터 (중복 사용 방지)
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)
    
    return dp[capacity]
```

---

### Pattern 4: Coin Change (동전 교환)

**문제**: 금액 N을 만들기 위한 최소 동전 개수

```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0원 만들기: 0개
    
    for coin in coins:
        for x in range(coin, amount + 1):
            # 현재 금액 x를 만들 때:
            # "coin을 하나 더 쓴다"
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# coins=[1,2,5], amount=11
# → 3 (5+5+1)
```

---

### Pattern 5: Longest Increasing Subsequence (LIS)

**문제**: 증가하는 부분 수열의 최대 길이

```python
# O(n^2) 방법
def lis_dp(nums):
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n  # 최소 길이는 자기 자신 1
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                # j까지의 LIS + 현재
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# [10, 9, 2, 5, 3, 7, 101, 18]
# → 4  ([2, 3, 7, 101] or [2, 3, 7, 18])
```

**O(n log n) 최적화** (이진 탐색):
```python
from bisect import bisect_left

def lis_optimized(nums):
    tails = []  # tails[i] = 길이 i+1인 LIS의 마지막 값 중 최소
    
    for num in nums:
        pos = bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    
    return len(tails)
```

---

### Pattern 6: Edit Distance (편집 거리)

**문제**: 문자열 A를 B로 바꾸는 최소 연산 수 (삽입/삭제/교체)

```python
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 초기화
    for i in range(m + 1):
        dp[i][0] = i  # word1[:i]를 ""로: i번 삭제
    for j in range(n + 1):
        dp[0][j] = j  # ""를 word2[:j]로: j번 삽입
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                # 같으면: 이전 상태 그대로
                dp[i][j] = dp[i-1][j-1]
            else:
                # 다르면: min(삽입, 삭제, 교체) + 1
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # 삭제
                    dp[i][j-1],    # 삽입
                    dp[i-1][j-1]   # 교체
                )
    
    return dp[m][n]

# "horse" → "ros"
# → 3 (replace h→r, remove o, remove e)
```

---

### Pattern 7: State Machine DP - Best Time to Buy/Sell Stock

**문제**: 주식을 최대 k번 거래할 때 최대 수익

```python
def max_profit_k_transactions(prices, k):
    if not prices or k == 0:
        return 0
    
    n = len(prices)
    # dp[i][j][0/1] = i일째, j번 거래 완료, 주식 보유(1)/미보유(0)
    
    # k가 너무 크면 무제한 거래와 같음
    if k >= n // 2:
        return max_profit_unlimited(prices)
    
    dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]
    
    for j in range(1, k + 1):
        dp[0][j][1] = -prices[0]  # 첫날 구매
    
    for i in range(1, n):
        for j in range(1, k + 1):
            # 오늘 미보유: max(어제도 미보유, 오늘 팔기)
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
            # 오늘 보유: max(어제도 보유, 오늘 사기)
            dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
    
    return dp[n-1][k][0]

def max_profit_unlimited(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit
```

---

## 🎓 DP 문제 해결 전략

### 1. **상태 정의** (State Definition)

"무엇을 저장할 것인가?"

```python
# 예: Knapsack
# dp[i][w] = "첫 i개 물건, 용량 w일 때 최대 가치"
```

### 2. **점화식** (Recurrence Relation)

"현재 상태는 이전 상태의 무엇으로 결정되는가?"

```python
# 예: LCS
# if s1[i] == s2[j]:
#     dp[i][j] = dp[i-1][j-1] + 1
# else:
#     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

### 3. **초기 조건** (Base Case)

"가장 작은 문제의 답은?"

```python
# 예: Fibonacci
# dp[0] = 0, dp[1] = 1
```

### 4. **계산 순서** (Fill Order)

"어떤 순서로 채울 것인가?"

```python
# Bottom-Up: 작은 것 → 큰 것
for i in range(1, n+1):
    ...
```

---

## 🚨 흔한 실수

1. **인덱스 범위 초과** ❌
   ```python
   # 항상 경계 체크!
   if i > 0 and j > 0:  # ✅
   ```

2. **초기값 설정 오류**
   ```python
   # 최솟값 찾기: float('inf')로 초기화
   dp = [float('inf')] * n  # ✅
   
   # 최댓값 찾기: 0 또는 -float('inf')
   dp = [0] * n  # ✅
   ```

3. **공간 최적화 시 순서 주의**
   ```python
   # 0/1 Knapsack 공간 최적화
   # 뒤에서부터! (중복 사용 방지)
   for w in range(capacity, weight - 1, -1):  # ✅
   ```

4. **상태 전이 누락**
   - 모든 가능한 전이 경로 고려했는지 체크

---

## 💡 DP vs Greedy vs Divide & Conquer

| 기법 | 특징 | 예시 |
|:---|:---|:---|
| **DP** | 모든 부분 문제 해결, 최적 보장 | Knapsack, LCS |
| **Greedy** | 매 순간 최선, 최적 **불보장** | Activity Selection |
| **Divide & Conquer** | 분할 → 정복 → 병합, 중복X | Merge Sort |

> [!WARNING] **Greedy는 언제 쓸 수 있나?**
> Greedy가 최적해를 보장하려면 **Greedy Choice Property**와 **Optimal Substructure**가 모두 필요합니다. 대부분은 DP가 안전합니다.

---

## 🧪 고급 DP 기법

### Digit DP
숫자 범위 내에서 조건 만족하는 개수

### Bitmask DP
집합 상태를 비트로 표현 (Traveling Salesman)

### Tree DP
트리 구조에서의 DP

---

---

## 📚 관련 문서
- [복잡도 분석](../00_fundamentals/complexity-and-big-o.md) - DP를 통한 기하급수적 시간 단축의 원리
- [최적화 전략](../03_patterns/optimization.md) - 그리디 vs DP 선택 기준과 성능 개선
- [그래프 탐색](graph-traversal.md) - 상태 공간 탐색과 최단 거리 문제 활용
- [선형 자료구조](../01_data-structures/linear.md) - 효율적인 DP 테이블(Array, Hash Map) 설계
- [백트래킹](backtracking.md) - 중복 계산을 허용하는 완전 탐색과의 비교
