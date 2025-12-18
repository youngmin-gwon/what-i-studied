---
title: divide-and-conquer
tags: [algorithm, paradigm, divide-and-conquer, recursion]
aliases: [분할 정복, Divide and Conquer, D&C]
date modified: 2025-12-18 12:05:00 +09:00
date created: 2025-12-18 12:05:00 +09:00
---

## Divide and Conquer: 거대한 문제를 쪼개어 정복하라

**분할 정복(Divide and Conquer)**은 문제를 그대로 해결하기 어려울 때, 문제를 **작은 하위 문제(Subproblems)**로 나누어 각각을 해결한 후 다시 합치는 알고리즘 패러다임입니다.

### 💡 Why it matters (Context)

- **효율의 극대화**: $O(N^2)$의 문제를 $O(N \log N)$으로 줄이는 기적 같은 효율을 보여줍니다. (예: 정렬)
- **병렬화 친화적**: 쪼개진 하위 문제들은 서로 독립적인 경우가 많아 분산 처리(Multi-threading)에 매우 유리합니다.
- **논리적 분해**: 복잡한 아키텍처를 설계할 때 컴포넌트를 분할하여 관리하는 철학의 근간이 됩니다.

---

### 🏢 실무 사례

#### Divide & Conquer 활용
- **빅데이터 처리**: MapReduce 프레임워크 (데이터를 분산(Map)하고 합침(Reduce)).
- **그래픽스 알고리즘**: Z-buffer, 영상 렌더링 시 화면을 쪼개어 처리.
- **수치 해석**: 빠른 푸리에 변환(FFT), 행렬 곱셈 알고리즘(Strassen).
- **데이터베이스**: 거대한 인덱스를 쪼개어 관리하는 Partitioning 기법.
- **컴파일러**: 소스 코드를 구문 트리(AST)로 분해하여 최적화.

---

## 🏗️ 작동 원리 (3-Step)

1. **분할 (Divide)**: 원래 문제를 더 작은 크기의 동일한 유형의 하위 문제로 나눕니다.
2. **정복 (Conquer)**: 하위 문제를 재귀적으로 해결합니다. (충분히 작으면 그냥 해결)
3. **결합 (Combine)**: 하위 문제의 정답을 합쳐 원래 문제의 정답을 만듭니다.

---

## 🔥 대표적인 사례

### 1. Merge Sort (병합 정렬)
- **Divide**: 배열을 절반으로 나눕니다.
- **Conquer**: 각 절반을 재귀적으로 정렬합니다.
- **Combine**: 정렬된 두 배열을 하나로 합칩니다.
- **효과**: $O(N^2) \rightarrow O(N \log N)$

### 2. Quick Sort (퀵 정렬)
- **Divide**: 피벗(Pivot)을 기준으로 작은 값과 큰 값으로 나눕니다. (Partition)
- **Conquer**: 각 구획을 재귀적으로 정렬합니다.
- **Combine**: (별도의 결합 과정 없음, 이미 정렬됨)

### 3. Binary Search (이진 탐색)
- **Divide**: 탐색 범위를 절반으로 나눕니다.
- **Conquer**: 찾는 값이 있는 절반만 다시 탐색합니다. (한쪽은 버림)

### 4. Fast Exponentiation (빠른 거듭제곱)
- **Divide**: $A^{10} \rightarrow A^5 \times A^5$ 형식으로 지수를 반으로 줄입니다.
- **효과**: $O(N) \rightarrow O(\log N)$

---

## ⚖️ D&C vs Dynamic Programming

| 특징 | Divide & Conquer | Dynamic Programming |
|:---|:---|:---|
| **중복 여부** | 하위 문제가 겹치지 않음 | 하위 문제가 **자주 겹침** |
| **저장** | 결과를 별도로 저장하지 않음 | 결과를 저장(Memoization) |
| **방향** | 주로 Top-Down (재귀) | Top-Down 및 Bottom-Up |
| **예시** | Merge Sort | Fibonacci, Knapsack |

---

## 🚨 흔한 실수 (Common Mistakes)

1. **지나친 재귀 깊이** ❌
   - 문제를 너무 작게 쪼개거나 Base Case가 부적절하면 Stack Overflow가 발생할 수 있습니다.
2. **결합(Combine) 과정의 비효율**
   - 쪼개는 것은 잘했는데, 합치는 과정이 $O(N)$을 넘어가면 분할 정복의 이점이 사라집니다.
3. **메모리 오버헤드**
   - 병합 정렬처럼 하위 문제 결과를 담기 위해 추가 배열을 계속 생성하면 메모리 사용량이 폭증할 수 있습니다. (In-place 알고리즘 고려 필요)

---

## 🧪 최적화 팁: "Base Case를 크게 잡기"

재귀 호출은 함수 호출 오버헤드가 있습니다. 배열 크기가 10~20 이하로 작아지면 분할 정복 대신 **삽입 정렬(Insertion Sort)** 같은 단순한 알고리즘을 수행하는 것이 실제 속도(Timsort의 철학)에 더 유리할 수 있습니다.

---

---

## 📚 관련 문서
- [[02_algorithms/search-and-sort|검색과 정렬]] - 병합 정렬과 퀵 정렬 등 D&C의 대표 응용 사례
- [[00_fundamentals/recursion-and-stack|재귀와 스택]] - 분할 정복의 논리적/물리적 실행 기반
- [[02_algorithms/dynamic-programming|동적 계획법]] - 하위 문제의 중복 여부에 따른 D&C와의 비교
- [[04_math/math-modular-and-exponentiation|수학적 기초]] - 빠른 거듭제곱 알고리즘 ($O(\log N)$)
- [[00_fundamentals/complexity-and-big-o|복잡도 분석]] - 마스터 정리(Master Theorem)를 통한 D&C 시간 복잡도 이해
