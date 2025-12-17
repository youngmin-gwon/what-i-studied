---
title: algo-pattern-optimization
tags: [algorithm, pattern, dynamic-programming, greedy, optimization]
aliases: [동적 계획법, 그리디, 최적화 알고리즘]
date modified: 2025-12-18 04:50:00 +09:00
date created: 2025-12-17 19:50:00 +09:00
---

# Optimization: 컴퓨터를 효율적으로 부려먹기

같은 문제를 풀어도 누군가는 1시간(Exponential)이 걸리고, 누군가는 1초(Linear/Polynomial)가 걸립니다.
그 차이는 "중복된 일을 하느냐, 안 하느냐"에 있습니다.

## 💾 Dynamic Programming (DP, 동적 계획법)

이름이 어렵지만, 핵심은 딱 하나입니다: **"기억해두기 (Memoization)"**.
한 번 푼 문제는 답을 적어두고, 다음에 또 나오면 계산하지 말고 답만 베끼는 것입니다.

### 피보나치 수열 예시
-   **순수 재귀 (Naive)**: `f(5)`를 구하기 위해 `f(3)`을 두 번이나 다시 계산합니다. -> **O(2^n)** (지수 시간, 폭발함)
-   **DP (Memoization)**: `f(3)`을 한 번 계산하고 배열에 저장합니다. -> **O(n)** (선형 시간, 빠름)

> [!TIP] **Engineering Context**
> DP는 알고리즘 문제에만 나오는 게 아닙니다. **웹 브라우저 캐시, CDN, 데이터베이스 쿼리 캐시** 모두 "한 번 한 일은 저장해둔다"는 DP의 철학을 따릅니다.

---

## 🍪 Greedy (탐욕 알고리즘)

**"미래는 모르겠고, 당장 눈앞의 이득(Local Optimum)만 쫓는다."**

-   **장점**: 계산이 매우매우 빠릅니다. 모든 경우의 수를 안 따져도 되니까요.
-   **단점**: 그 결과가 전체적으로 최선(Global Optimum)이라는 보장이 없습니다.

### 언제 통하나? (Matroid)
거스름돈 문제(10, 50, 100, 500원)처럼 큰 단위가 작은 단위의 배수일 때 등, 특수한 수학적 조건에서만 "항상 최적해"를 보장합니다.
하지만 최적해가 보장되지 않더라도, **"대충 괜찮은 답(Approximation)"**을 빠르게 구해야 할 때(예: AI 길찾기, 휴리스틱) 유용합니다.

-   **다익스트라(Dijkstra)**: 대표적인 그리디 알고리즘입니다. "현재 갈 수 있는 가장 가까운 노드"를 계속 선택해서 확정 짓습니다.

### 📚 연결 문서
- [[algo-complexity-and-big-o]] - O(2^n)과 O(n)의 엄청난 차이
- [[algo-ds-hash-and-map]] - Memoization을 위한 저장소
- [[algo-ds-tree-and-graph]] - 다익스트라 최단 경로
