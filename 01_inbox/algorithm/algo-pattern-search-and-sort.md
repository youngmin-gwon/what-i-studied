---
title: algo-pattern-search-and-sort
tags: [algorithm, binary-search, merge-sort, pattern, quick-sort, search, sort]
aliases: [병합 정렬, 이진 탐색, 정렬 알고리즘, 퀵 정렬]
date modified: 2025-12-18 10:06:00 +09:00
date created: 2025-12-17 19:40:00 +09:00
---

## Search & Sort: 정보 검색의 기술

데이터를 저장하는 이유는 나중에 **찾기 (Search)** 위해서입니다. 그리고 빠르게 찾으려면 **정렬 (Sort)**되어 있어야 합니다.

### 🔍 Binary Search (이진 탐색)

"업다운 게임"과 원리가 같습니다. 숫자가 정렬되어 있다면, 중간값 (Mid) 을 보고 범위를 절반씩 줄여나갈 수 있습니다.

- **복잡도**: **O(log n)**. 40 억 개의 데이터도 32 번 (`log2(40억)`) 비교면 찾습니다. 기적적인 속도입니다.
- **조건**: 데이터가 반드시 **정렬**되어 있어야 합니다.
- **Context**: 데이터베이스 인덱스 (B-Tree) 가 빠른 이유가 바로 이진 탐색 원리를 쓰기 때문입니다. `git bisect` 명령어도 커밋 히스토리를 이진 탐색하여 버그가 발생한 시점을 찾습니다.

```swift
// Mid 계산 시 (left + right) / 2는 오버플로우 위험이 있습니다 (C/Java 등).
// 안전한 방법: left + (right - left) / 2
```

---

### 🌪️ Sorting Algorithms

세상에 "가장 좋은" 정렬 알고리즘은 없습니다. 상황에 따라 다릅니다.

#### 1. Quick Sort (퀵 정렬)
- **전략**: Pivot 을 잡고 좌우로 나눕니다 (분할 정복).
- **특징**: 평균적으로 가장 빠릅니다. 메모리가 **연속적**이라 Cache Hit 율이 높고, 추가 메모리 (`Space O(log n)`) 를 거의 안 씁니다.
- **단점**: 최악의 경우 (이미 정렬된 경우 등) **O(n^2)**이 됩니다. 또한 **Unstable**합니다 (같은 값의 순서가 바뀔 수 있음).

#### 2. Merge Sort (병합 정렬)
- **전략**: 반으로 쪼개고 나중에 합칩니다.
- **특징**: 항상 **O(n log n)**을 보장합니다. **Stable**합니다.
- **단점**: 합치는 과정에서 **O(n) 메모리**가 추가로 필요합니다. Linked List 정렬에는 최고입니다 (메모리 추가 없이 포인터만 바꾸면 되므로).

#### 3. Timsort (현실의 승자)

Python, Java, Swift(`sort()`) 의 기본 정렬입니다.

- **전략**: **Insertion Sort**와 **Merge Sort**를 섞었습니다.
- **원리**: 현실 세계 데이터는 완전히 무작위가 아니라, 이미 부분적으로 정렬된 구간 (Run) 이 많습니다. 이 구간들은 Insertion Sort 가 엄청 빠릅니다. 이 특성을 이용해 평균 성능을 극대화합니다.

#### 📚 연결 문서
- [[algo-complexity-and-big-o]] - 정렬 복잡도 비교
- [[algo-ds-linear]] - Array 가 Quick Sort 에 유리한 이유
- [[algo-ds-tree-and-graph]] - 이진 탐색 트리와의 관계
