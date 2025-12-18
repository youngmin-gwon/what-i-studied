---
title: README
tags: [algorithm, data-structures, index]
aliases: [알고리즘 인덱스, 자료구조 인덱스]
date modified: 2025-12-18 13:04:34 +09:00
date created: 2025-12-18 11:33:14 +09:00
---

## 알고리즘 & 자료구조 학습 가이드

코딩테스트와 실무에 필요한 모든 알고리즘과 자료구조를 체계적으로 정리했습니다.

---

### 📖 학습 로드맵

#### 🎯 Level 1: 기초 (Foundation)

이론과 하드웨어, 사고 체계까지 아우르는 단단한 기초를 다집니다.

1. [[00_fundamentals/complexity-and-big-o|복잡도와 Big-O]] ⭐
   - 알고리즘 성능 평가의 절대 기준.

2. [[00_fundamentals/memory-layout-and-cache|메모리 레이아웃과 캐시]]
   - 하드웨어 구조가 실제 성능에 미치는 영향.

3. [[00_fundamentals/recursion-and-stack|재귀와 호출 스택]]
   - 문제를 쪼개는 논리와 실행 구조의 이해.

4. [[00_fundamentals/problem-solving-process|문제 해결 프로세스]] ⭐
   - 문제를 분석하고 설계하는 4 단계 프레임워크.

5. [[00_fundamentals/floating-point-guide|실수와 정밀도]]
   - 수치 오차를 방지하는 실전 지침.

4. [[01_data-structures/linear|선형 자료구조]]
   - Array, Linked List의 물리적 배치와 하드웨어 효율성.

---

#### 🚀 Level 2: 핵심 (Core)

코딩테스트 80% 를 커버하는 필수 자료구조입니다.

##### 자료구조 (Data Structures)

1. [[01_data-structures/stack-and-queue|스택과 큐 (Stack & Queue)]] ⭐
   - 데이터 순서 제어의 기초 (LIFO, FIFO)
   - 구현 방식에 따른 성능 차이 ($O(1)$ vs $O(N)$)

2. [[01_data-structures/hash-and-map|해시 테이블]]
   - Hash Map, Hash Collision 처리
   - O(1) 조회의 비밀

3. [[01_data-structures/tree-and-graph|트리와 그래프]]
   - Binary Search Tree, BFS/DFS
   - 그래프 탐색의 기초

4. [[01_data-structures/heap-and-priority-queue|힙과 우선순위 큐]] ⭐
   - Top-K, 실시간 중앙값
   - OS 스케줄러, 다익스트라 필수

---

#### 🔥 Level 3: 고급 (Advanced)

난이도 높은 문제를 위한 특수 자료구조입니다.

1. [[01_data-structures/string-advanced|고급 문자열]]
   - Trie (자동완성, IP 라우팅)
   - KMP (패턴 매칭)

2. [[01_data-structures/disjoint-set|Union-Find]]
   - 사이클 탐지, MST (Kruskal)
   - 거의 O(1) 연결성 판별

3. [[01_data-structures/segment-tree|세그먼트 트리]] ⭐
   - 구간 합, 최소/최대 $O(\log N)$ 업데이트 및 조회
   - 동적 데이터의 구간 쿼리 끝판왕

4. [[01_data-structures/specialized-queues|특수 큐/스택]]
   - Deque, Monotonic Stack/Queue
   - Sliding Window Maximum, Next Greater Element

---

### 🧮 알고리즘 패턴 (Algorithmic Patterns)

#### 검색과 정렬 & 정복

1. [[02_algorithms/search-and-sort|검색과 정렬]]
   - Binary Search, Quick Sort, Merge Sort, Timsort

2. [[02_algorithms/divide-and-conquer|분할 정복 (Divide & Conquer)]]
    - 문제를 쪼개어 해결하는 근본 패러다임
    - 병렬 처리 및 대규모 데이터 처리의 기초

#### 최적화 및 실전 패턴

1. [[03_patterns/optimization|최적화 전략]] ⭐
    - 어떤 알고리즘을 쓸 것인가? (N 에 따른 선택)
    - Caching, Pruning, Heuristics

2. [[03_patterns/two-pointers|투 포인터 & 슬라이딩 윈도우]]
    - Fast & Slow Runner, Sliding Window
    - O(n^2)을 O(n)으로 최적화

3. [[03_patterns/prefix-sum|누적 합 (Prefix Sum)]]
    - 구간 합을 O(1)에 구하기
    - 2D Prefix Sum (Image Processing)

4. [[03_patterns/bit-manipulation|비트 연산 (Bit Manipulation)]]
    - 비트 마스킹을 이용한 공간/속도 최적화
    - 집합 표현, XOR 트릭

5. [[03_patterns/interval-patterns|구간 패턴 (Interval)]]
    - 구간 병합, 겹침 감지, 회의실 문제
    - 스케줄링 및 리소스 관리

6. [[03_patterns/binary-search-optimization|이진 탐색 최적화 (Parametric Search)]] ⭐
    - 최적화 문제를 결정 문제로 변환
    - 공유기 설치, 나무 자르기 등 고난도 패턴

---

#### 🔢 04. Math (수학)
- [[04_math/gcd-lcm|GCD & LCM]]
  - 유클리드 호제법, 최소공배수
  - Juggling Algorithm
  - RSA 암호화, 배열 회전
- [[04_math/math-prime-number|Prime Numbers]] - 소수 판별, 에라토스테네스의 체
- [[04_math/math-modular-and-exponentiation|Modular & Exponentiation]] - 나머지 연산, 빠른 거듭제곱
- [[04_math/math-combinatorics|Combinatorics]] - 순열과 조합, 파스칼의 삼각형

---

### 📚 주제별 빠른 찾기

| 문제 유형 | 추천 자료구조/알고리즘 | 파일 링크 |
|:---|:---|:---|
| **"다음으로 큰/작은 값"** | Monotonic Stack | [[01_data-structures/specialized-queues]] |
| **"윈도우 최댓값/최솟값"** | Monotonic Queue | [[01_data-structures/specialized-queues]] |
| **"가장 큰 K 개"** | Min Heap | [[01_data-structures/heap-and-priority-queue]] |
| **"실시간 중앙값"** | 2 Heaps | [[01_data-structures/heap-and-priority-queue]] |
| **"접두사 검색/자동완성"** | Trie | [[01_data-structures/string-advanced]] |
| **"패턴 매칭"** | KMP | [[01_data-structures/string-advanced]] |
| **"사이클 탐지"** | Union-Find / DFS | [[01_data-structures/disjoint-set]], [[02_algorithms/graph-traversal]] |
| **"최소 신장 트리"** | Kruskal + Union-Find | [[01_data-structures/disjoint-set]] |
| **"가장 빠른 길 (가중치 X)"** | BFS | [[02_algorithms/graph-traversal]] |
| **"가장 빠른 길 (가중치 O)"** | Dijkstra | [[02_algorithms/shortest-path]] |
| **"O(1) 조회"** | Hash Map | [[01_data-structures/hash-and-map]] |
| **"O(1) 구간 합"** | Prefix Sum | [[03_patterns/prefix-sum]] |

---

#### 🔥 난이도별 학습 순서

##### 🟢 Easy (기초 다지기)
1. [[00_fundamentals/complexity-and-big-o]]
2. [[01_data-structures/linear]]
3. [[01_data-structures/hash-and-map]]
4. [[03_patterns/two-pointers]]

##### 🟡 Medium (실전 준비)
1. [[01_data-structures/tree-and-graph]]
2. [[02_algorithms/search-and-sort]]
3. [[01_data-structures/heap-and-priority-queue]]
4. [[01_data-structures/specialized-queues]]

##### 🔴 Hard (고득점 목표)
1. [[01_data-structures/string-advanced]]
2. [[01_data-structures/disjoint-set]]
3. [[02_algorithms/dynamic-programming]]
4. [[02_algorithms/backtracking]]
5. [[03_patterns/bit-manipulation]]

---

### 🚧 앞으로 추가 예정

#### 필수 알고리즘 (완료)
- [x] [[02_algorithms/graph-traversal|BFS / DFS (상세)]]
- [x] [[02_algorithms/dynamic-programming|Dynamic Programming (DP)]]
- [x] [[02_algorithms/backtracking|Backtracking]]
- [x] [[02_algorithms/greedy|Greedy Algorithm]]
- [x] [[02_algorithms/shortest-path|Shortest Path]]
- [x] [[02_algorithms/minimum-spanning-tree|Minimum Spanning Tree (MST)]]

#### 심화 및 특수 주제 (선택)
- [ ] **Geometry** - CCW, Convex Hull
- [ ] **String Advanced 2** - Aho-Corasick, Suffix Array
- [x] [[01_data-structures/segment-tree|Segment Tree / Fenwick Tree]]

---

### 🎓 코딩테스트 체크리스트

#### ✅ 자료구조 완성도
- [x] Array, Linked List, Stack, Queue
- [x] Hash Table
- [x] Binary Search Tree
- [x] Heap / Priority Queue
- [x] Trie
- [x] Union-Find
- [x] Deque, Monotonic Stack/Queue
- [ ] Segment Tree (선택)

#### ✅ 알고리즘 완성도
- [x] Binary Search
- [x] Sorting (Quick, Merge, Heap)
- [x] BFS / DFS (상세)
- [x] Two Pointers / Sliding Window
- [x] Dynamic Programming
- [x] Backtracking
- [x] Greedy
- [x] Graph Algorithms (Dijkstra, MST 등)
- [x] Divide and Conquer

---

### 💡 학습 팁

>[!TIP] **효과적인 학습법**
> 1. **개념 → 구현 → 문제 풀이** 순서로 진행
> 2. 각 자료구조의 **시간/공간 복잡도**를 반드시 암기
> 3. **언제 쓰는가 (Context)**를 이해해야 응용 가능
> 4. 코드를 외우지 말고 **원리**를 이해

>[!IMPORTANT] **면접 준비**
> - 자료구조: "왜 이걸 쓰는가?"에 답할 수 있어야 함
> - 알고리즘: Trade-off 설명 (시간 vs 공간)
> - 실무 연결: "이 자료구조가 실제로 어디 쓰이나?"

---

### 📊 전체 진행도

- **기초 (Fundamentals)**: 5/5 완료 (100%) ✅
- **자료구조 (Data Structures)**: 9/9 완료 (100%) 🎉
- **알고리즘 & 패턴 (Algorithms)**: 17/17 완료 (100%) 🎉

**다음 목표**: 실제 코딩 테스트 기출 유형 분석 및 실무 시스템 결합 사례 심화
