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

### 최적화 및 실전 패턴

10. [[03_patterns/optimization|최적화 전략]] ⭐
    - 어떤 알고리즘을 쓸 것인가? (N에 따른 선택)
    - Caching, Pruning, Heuristics

11. [[03_patterns/two-pointers|투 포인터 & 슬라이딩 윈도우]]
    - Fast & Slow Runner, Sliding Window
    - O(n^2)을 O(n)으로 최적화

12. [[03_patterns/prefix-sum|누적 합 (Prefix Sum)]]
    - 구간 합을 O(1)에 구하기
    - 2D Prefix Sum (Image Processing)

13. [[03_patterns/bit-manipulation|비트 연산 (Bit Manipulation)]]
    - 비트 마스킹을 이용한 공간/속도 최적화
    - 집합 표현, XOR 트릭

14. [[03_patterns/interval-patterns|구간 패턴 (Interval)]]
    - 구간 병합, 겹침 감지, 회의실 문제
    - 스케줄링 및 리소스 관리

15. [[03_patterns/binary-search-optimization|이진 탐색 최적화 (Parametric Search)]] ⭐
    - 최적화 문제를 결정 문제로 변환
    - 공유기 설치, 나무 자르기 등 고난도 패턴

---

### 🔢 04. Math (수학)
- [[04_math/gcd-lcm|GCD & LCM]]
  - 유클리드 호제법, 최소공배수
  - Juggling Algorithm
  - RSA 암호화, 배열 회전
- [[04_math/math-prime-number|Prime Numbers]] - 소수 판별, 에라토스테네스의 체
- [[04_math/math-modular-and-exponentiation|Modular & Exponentiation]] - 나머지 연산, 빠른 거듭제곱
- [[04_math/math-combinatorics|Combinatorics]] - 순열과 조합, 파스칼의 삼각형

---

## 📚 주제별 빠른 찾기

| 문제 유형 | 추천 자료구조/알고리즘 | 파일 링크 |
|:---|:---|:---|
| **"다음으로 큰/작은 값"** | Monotonic Stack | [[01_data-structures/specialized-queues]] |
| **"윈도우 최댓값/최솟값"** | Monotonic Queue | [[01_data-structures/specialized-queues]] |
| **"가장 큰 K개"** | Min Heap | [[01_data-structures/heap-and-priority-queue]] |
| **"실시간 중앙값"** | 2 Heaps | [[01_data-structures/heap-and-priority-queue]] |
| **"접두사 검색/자동완성"** | Trie | [[01_data-structures/string-advanced]] |
| **"패턴 매칭"** | KMP | [[01_data-structures/string-advanced]] |
| **"사이클 탐지"** | Union-Find / DFS | [[01_data-structures/disjoint-set]], [[02_algorithms/graph-traversal]] |
| **"최소 신장 트리"** | Kruskal + Union-Find | [[01_data-structures/disjoint-set]] |
| **"가장 빠른 길 (가중치X)"** | BFS | [[02_algorithms/graph-traversal]] |
| **"가장 빠른 길 (가중치O)"** | Dijkstra | [[02_algorithms/shortest-path]] |
| **"O(1) 조회"** | Hash Map | [[01_data-structures/hash-and-map]] |
| **"O(1) 구간 합"** | Prefix Sum | [[03_patterns/prefix-sum]] |

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
11. [[02_algorithms/dynamic-programming]]
12. [[02_algorithms/backtracking]]
13. [[03_patterns/bit-manipulation]]

---

## 🚧 앞으로 추가 예정

### 필수 알고리즘 (완료)
- [x] [[02_algorithms/graph-traversal|BFS / DFS (상세)]]
- [x] [[02_algorithms/dynamic-programming|Dynamic Programming (DP)]]
- [x] [[02_algorithms/backtracking|Backtracking]]
- [x] [[02_algorithms/greedy|Greedy Algorithm]]
- [x] [[02_algorithms/shortest-path|Graph Algorithms]]

### 심화 및 특수 주제 (선택)
- [ ] **Geometry** - CCW, Convex Hull
- [ ] **Advanced Trees** - Segment Tree, Fenwick Tree (BIT)
- [ ] **String Advanced 2** - Aho-Corasick, Suffix Array

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
- [x] BFS / DFS (상세)
- [x] Two Pointers
- [x] Dynamic Programming
- [x] Backtracking
- [x] Greedy
- [x] Graph Algorithms (Dijkstra 등)

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
**알고리즘 & 패턴**: 15/15 완료 (100%) 🎉

**다음 목표**: 심화 주제 (Segment Tree 등) 또는 실무 프로젝트 적용 사례 추가
