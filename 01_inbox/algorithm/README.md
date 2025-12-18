---
title: Algorithm & Data Structures - Index
tags: [algorithm, data-structures, index]
aliases: [알고리즘 인덱스, 자료구조 인덱스]
date modified: 2025-12-18 11:33:14 +09:00
date created: 2025-12-18 11:33:14 +09:00
---

# 알고리즘 & 자료구조 학습 가이드

코딩테스트와 실무에 필요한 모든 알고리즘과 자료구조를 체계적으로 정리했습니다.

---

## 📖 학습 로드맵

### 🎯 Level 1: 기초 (Foundation)
이론과 기본 자료구조를 이해합니다.

1. [[00_fundamentals/complexity-and-big-o|복잡도와 Big-O]] ⭐ **필수**
   - 시간/공간 복잡도, Trade-off, Amortized Analysis
   - 모든 알고리즘의 성능을 평가하는 기준

2. [[01_data-structures/linear|선형 자료구조]]
   - Array, Linked List, Stack, Queue
   - Cache Locality, Sentinel Node, Runner Technique

---

### 🚀 Level 2: 핵심 (Core)
코딩테스트 80%를 커버하는 필수 자료구조입니다.

#### 자료구조 (Data Structures)

3. [[01_data-structures/hash-and-map|해시 테이블]]
   - Hash Map, Hash Collision 처리
   - O(1) 조회의 비밀

4. [[01_data-structures/tree-and-graph|트리와 그래프]]
   - Binary Search Tree, BFS/DFS
   - 그래프 탐색의 기초

5. [[01_data-structures/heap-and-priority-queue|힙과 우선순위 큐]] ⭐
   - Top-K, 실시간 중앙값
   - OS 스케줄러, 다익스트라 필수

---

### 🔥 Level 3: 고급 (Advanced)
난이도 높은 문제를 위한 특수 자료구조입니다.

6. [[01_data-structures/string-advanced|고급 문자열]]
   - Trie (자동완성, IP 라우팅)
   - KMP (패턴 매칭)

7. [[01_data-structures/disjoint-set|Union-Find]]
   - 사이클 탐지, MST (Kruskal)
   - 거의 O(1) 연결성 판별

8. [[01_data-structures/specialized-queues|특수 큐/스택]] ⭐
   - Deque, Monotonic Stack/Queue
   - Sliding Window Maximum, Next Greater Element

---

## 🧮 알고리즘 패턴 (Algorithmic Patterns)

### 검색과 정렬

9. [[02_algorithms/search-and-sort|검색과 정렬]]
   - Binary Search, Quick Sort, Merge Sort, Timsort

### 최적화 기법

10. [[03_patterns/optimization|최적화 패턴]]
    - Greedy, Dynamic Programming
    - Memoization vs Tabulation

11. [[03_patterns/two-pointers|투 포인터]]
    - Fast & Slow Runner, Sliding Window
    - 공간 복잡도 O(1) 최적화

---

## 🔢 수학 & 기타

12. [[04_math/gcd-lcm|GCD와 LCM]]
    - 유클리드 호제법, Juggling Algorithm
    - RSA 암호화, 배열 회전

---

## 📚 주제별 빠른 찾기

### 🎯 문제 유형별 자료구조 선택

| 문제 유형 | 추천 자료구조 | 파일 링크 |
|:---|:---|:---|
| **"다음으로 큰/작은 값"** | Monotonic Stack | [[01_data-structures/specialized-queues]] |
| **"윈도우 최댓값/최솟값"** | Monotonic Queue | [[01_data-structures/specialized-queues]] |
| **"가장 큰 K개"** | Min Heap | [[01_data-structures/heap-and-priority-queue]] |
| **"실시간 중앙값"** | 2 Heaps | [[01_data-structures/heap-and-priority-queue]] |
| **"접두사 검색/자동완성"** | Trie | [[01_data-structures/string-advanced]] |
| **"패턴 매칭"** | KMP | [[01_data-structures/string-advanced]] |
| **"사이클 탐지"** | Union-Find | [[01_data-structures/disjoint-set]] |
| **"최소 신장 트리"** | Kruskal + Union-Find | [[01_data-structures/disjoint-set]] |
| **"최단 경로"** | BFS | [[01_data-structures/tree-and-graph]] |
| **"O(1) 조회"** | Hash Map | [[01_data-structures/hash-and-map]] |

---

### 🔥 난이도별 학습 순서

#### 🟢 Easy (기초 다지기)
1. [[00_fundamentals/complexity-and-big-o]]
2. [[01_data-structures/linear]]
3. [[01_data-structures/hash-and-map]]
4. [[03_patterns/two-pointers]]

#### 🟡 Medium (실전 준비)
5. [[01_data-structures/tree-and-graph]]
6. [[02_algorithms/search-and-sort]]
7. [[01_data-structures/heap-and-priority-queue]]
8. [[01_data-structures/specialized-queues]]

#### 🔴 Hard (고득점 목표)
9. [[01_data-structures/string-advanced]]
10. [[01_data-structures/disjoint-set]]
11. [[03_patterns/optimization]]

---

## 🚧 앞으로 추가 예정

### 필수 알고리즘 (코딩테스트 고빈도)
- [ ] **BFS / DFS (상세)** - 미로 찾기, 섬 개수, 사이클 탐지
- [ ] **Dynamic Programming (DP)** - Fibonacci, 0/1 Knapsack, LCS
- [ ] **Backtracking** - N-Queens, Subset Sum, Permutation
- [ ] **Greedy Algorithm** - Activity Selection, Huffman Coding
- [ ] **Graph Algorithms** - Dijkstra, Bellman-Ford, Floyd-Warshall, Topological Sort

### 심화 알고리즘 (선택)
- [ ] **Divide and Conquer** - 상세 버전
- [ ] **Bit Manipulation** - XOR Tricks, Bit Masking
- [ ] **Geometry** - Convex Hull, Line Sweep
- [ ] **Advanced Trees** - Segment Tree, Fenwick Tree (BIT)

---

## 🎓 코딩테스트 체크리스트

### ✅ 자료구조 완성도
- [x] Array, Linked List, Stack, Queue
- [x] Hash Table
- [x] Binary Search Tree
- [x] Heap / Priority Queue
- [x] Trie
- [x] Union-Find
- [x] Deque, Monotonic Stack/Queue
- [ ] Segment Tree (선택)

### ✅ 알고리즘 완성도
- [x] Binary Search
- [x] Sorting (Quick, Merge, Heap)
- [ ] **BFS / DFS (상세)** (필수!)
- [x] Two Pointers
- [ ] **Dynamic Programming** (필수!)
- [ ] **Backtracking** (필수!)
- [ ] **Greedy** (필수!)
- [ ] **Graph Algorithms** (Dijkstra 등)

---

## 💡 학습 팁

> [!TIP] **효과적인 학습법**
> 1. **개념 → 구현 → 문제 풀이** 순서로 진행
> 2. 각 자료구조의 **시간/공간 복잡도**를 반드시 암기
> 3. **언제 쓰는가 (Context)**를 이해해야 응용 가능
> 4. 코드를 외우지 말고 **원리**를 이해

> [!IMPORTANT] **면접 준비**
> - 자료구조: "왜 이걸 쓰는가?"에 답할 수 있어야 함
> - 알고리즘: Trade-off 설명 (시간 vs 공간)
> - 실무 연결: "이 자료구조가 실제로 어디 쓰이나?"

---

## 📊 현재 진행도

**자료구조**: 8/10 완료 (80%) ✅
**알고리즘**: 4/8 완료 (50%) 🔄

**다음 목표**: Dynamic Programming, Backtracking, Greedy 추가
