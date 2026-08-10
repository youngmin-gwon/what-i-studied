---
title: dp-vs-greedy-vs-divide-and-conquer
tags: [algorithm, comparison, dp, greedy, divide-and-conquer, strategy, decision-making]
aliases: [DP와 그리디와 분할정복 비교, 알고리즘 선택 기준]
date modified: 2026-08-10 00:00:00 +09:00
date created: 2026-08-10 00:00:00 +09:00
---

## DP vs Greedy vs Divide & Conquer: 알고리즘 선택의 나침반

큰 문제를 푸는 세 가지 주요 전략을 비교합니다. 각 기법의 특성을 이해하고 문제 상황에 맞는 최적의 선택을 하세요.

---

## 📊 3가지 기법의 본질적 차이

| 기법 | 핵심 철학 | 하위 문제 관계 | 최적성 보장 | 주요 특징 |
|:---|:---|:---|:---|:---|
| **Dynamic Programming (DP)** | 모든 경우를 고려하고 기억하기 | **중복 있음** - 같은 부분 문제 반복 | ✅ 최적해 보장 | 메모이제이션/타블레이션으로 중복 제거 |
| **Greedy** | 매 순간 최선만 선택하기 | 무관 | ❌ 보장 안 함 | 국소 최적이 전역 최적일 때만 작동 |
| **Divide & Conquer (D&C)** | 분할-정복-병합 반복 | **중복 없음** - 독립적 하위 문제 | ✅ 최적해 보장 | 재귀로 문제를 반으로 계속 분할 |

---

## 💼 상황별 선택 가이드

### DP를 선택해야 할 때

**특징**:
- 같은 부분 문제가 **여러 번** 나타남
- **Overlapping Subproblems** 존재
- **Optimal Substructure** 만족

**예시**:
- Fibonacci: `F(5) = F(4) + F(3)`, `F(4) = F(3) + F(2)` → F(3) 중복
- 0/1 Knapsack: "물건을 넣을지 말지" 선택이 반복
- Longest Common Subsequence (LCS): 문자 비교 반복

**코드 패턴**:
```python
# Top-Down (Memoization)
memo = {}
def solve(n):
    if n in memo: return memo[n]
    result = ...
    memo[n] = result
    return result

# Bottom-Up (Tabulation)
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = ...
```

---

### Greedy를 선택해야 할 때

**조건**:
- **Greedy Choice Property**: 매 순간의 최선이 결국 전체 최선
- **Optimal Substructure**: 부분 문제의 최적해로 전체 최적해 구성

**예시**:
- Activity Selection (회의실 배정): 종료 시간이 빠른 회의부터 선택
- Fractional Knapsack: 단위 무게당 가치가 높은 순서로 넣기
- Huffman Coding: 빈도가 낮은 문자부터 트리에 합치기
- 거스름돈 (특정 조건 하): 큰 동전부터 사용

**장점**:
- 매우 빠름: O(n) 또는 O(n log n)
- 구현 간단
- 메모리 효율적

**주의**:
```
❌ 0/1 Knapsack에 Greedy는 오답
물건을 쪼갤 수 없을 때, 단순히 "가성비" 순서로 넣으면:
- 무게제한까지 가득 채우지 못할 수 있음
- 더 좋은 조합을 놓칠 수 있음
→ DP로 모든 경우를 고려해야 함
```

---

### Divide & Conquer를 선택해야 할 때

**특징**:
- 하위 문제들이 **겹치지 않음** (Merge Sort의 각 분할은 독립적)
- 각 하위 문제를 독립적으로 해결 후 병합
- **중복 저장이 필요 없음**

**예시**:
- Merge Sort: 배열 절반 → 각각 정렬 → 병합 (O(n log n))
- Quick Sort: 피벗 기준 분할 → 각각 정렬 (O(n log n) 평균)
- Binary Search: 범위 절반 → 한쪽만 탐색 (O(log n))
- Fast Exponentiation: 2^10 = (2^5)^2 (O(log n))

**장점**:
- 병렬화 용이 (MapReduce 같은 분산 처리에 최적)
- 캐시 친화적
- 메모리 효율적

**코드 패턴**:
```python
def divide_and_conquer(arr):
    if len(arr) <= 1:  # Base case
        return arr
    
    mid = len(arr) // 2
    left = divide_and_conquer(arr[:mid])      # Divide
    right = divide_and_conquer(arr[mid:])     # Divide
    
    return merge(left, right)  # Conquer & Combine
```

---

## 🔀 페어별 비교

### DP vs Greedy

| 측면 | DP | Greedy |
|:---|:---|:---|
| **결정** | 모든 가능성 탐색 | 매 순간 최선만 선택 |
| **속도** | 느림 (중첩 반복/재귀) | 매우 빠름 |
| **최적성** | 항상 보장 | 조건 만족할 때만 보장 |
| **메모리** | 많음 (테이블/메모) | 적음 |
| **예시** | Knapsack (0/1) | Knapsack (Fractional) |

**선택 기준**:
- "이전 선택이 다음에 영향을 줄까?" → YES면 DP
- "지금의 최선이 나중의 최악을 초래할까?" → YES면 DP, NO면 Greedy

---

### D&C vs DP

| 측면 | D&C | DP |
|:---|:---|:---|
| **하위 문제** | 겹치지 않음 | 자주 겹침 |
| **저장** | 저장하지 않음 | 메모이제이션 필수 |
| **방식** | Top-Down (재귀 자체가 탐색) | Top-Down (메모 + 재귀) / Bottom-Up (반복) |
| **복잡도** | O(n log n) - 정렬 기준 | O(n²) - 테이블 채우기 |
| **예시** | Merge Sort | Fibonacci |

**선택 기준**:
- 하위 문제들이 **독립적**인가? → D&C 선택
- 같은 하위 문제가 **반복**되는가? → DP 선택

---

### DP vs D&C vs Greedy 한눈에

| 특징 | DP | Greedy | D&C |
|:---|:---|:---|:---|
| **결정 방식** | 모든 부분 문제 해결, 최적 보장 | 매 순간 최선, 최적 **불보장** | 분할 → 정복 → 병합, 중복 X |
| **속도** | 느림 | **매우 빠름** | 중간 |
| **구현** | 복잡 (상태 정의 필요) | 간단 (정렬 + 반복) | 중간 (재귀 + 병합) |
| **대표 문제** | Knapsack, LCS, Coin Change | Activity Selection, Huffman | Merge Sort, Binary Search |

---

## 🎓 문제별 해결 전략

### 1단계: 최적성 보장 확인

```
Q: "최적해를 반드시 구해야 하나?"
├─ YES → DP 또는 D&C
└─ NO (근사해 가능) → Greedy 고려
```

### 2단계: 하위 문제 중복 확인

```
Q: "같은 부분 문제가 반복되나?"
├─ YES → DP (메모이제이션)
├─ NO → D&C (병합 정렬) 또는 Greedy
└─ 불명확 → 작은 예제로 테스트
```

### 3단계: 국소 최적성 검증

```
Q: "매 순간의 최선이 전체 최선일까?" (Greedy 검증)
├─ 수학적 증명 가능 → Greedy 사용
├─ 반례 발견 → DP로 변경
└─ 불명확 → DP가 안전
```

---

## 🚨 실수 방지 체크리스트

### DP 작성 시

- [ ] **상태 정의**: dp[i]의 의미가 명확한가?
- [ ] **점화식**: 모든 전이 경로를 포함했는가?
- [ ] **초기값**: Base case를 올바르게 설정했는가?
- [ ] **중복 계산**: 정말 같은 부분 문제가 반복되는가?

### Greedy 작성 시

- [ ] **정렬 기준**: 올바른 기준으로 정렬했는가?
- [ ] **반례 테스트**: 반례를 찾을 수 없나?
- [ ] **증명**: Greedy Choice Property를 만족하는가?
- [ ] **대안 고려**: DP로도 풀어볼 필요는 없나?

### D&C 작성 시

- [ ] **Base case**: 충분히 작은 크기로 설정했는가?
- [ ] **병합 로직**: 결합 과정이 O(n)을 넘지 않는가?
- [ ] **메모리**: 재귀 깊이와 추가 배열이 부담스럽지 않은가?

---

## 💡 실무 사례

### Google News Feed
- **문제**: 사용자 선호도를 고려하여 최대 engagement 콘텐츠 조합 선택
- **접근**: 0/1 Knapsack (DP)
- **이유**: 콘텐츠를 쪼갤 수 없음 + 최적 조합 필요

### YouTube 비디오 압축
- **문제**: 고속 푸리에 변환(FFT)으로 빈도 분석
- **접근**: Divide & Conquer (Fast Fourier Transform)
- **이유**: 신호를 절반으로 분할하며 반복

### Spotify 추천
- **문제**: 사용자 재생 기록 중 가장 유사한 곡 찾기
- **접근**: Longest Common Subsequence (DP)
- **이유**: 음악 선호 패턴의 공통 요소 추출

---

## 📚 관련 문서

- [동적 계획법 (DP)](dynamic-programming.md) - 상세 DP 기법과 패턴
- [메모이제이션 vs 타블레이션](../00_fundamentals/memoization.md) - DP의 두 가지 구현
- [그리디 알고리즘](greedy.md) - Greedy 패턴과 적용 조건
- [분할 정복](divide-and-conquer.md) - D&C의 대표 응용 사례
- [복잡도 분석](../00_fundamentals/complexity-and-big-o.md) - 시간/공간 복잡도 기준
