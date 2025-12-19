---
title: tree-and-graph
tags: [algorithm, bfs, data-structures, dfs, graph, heap, tree]
aliases: [그래프, 깊이 우선 탐색, 너비 우선 탐색, 이진 탐색 트리, 트리, 힙]
date modified: 2025-12-18 16:26:53 +09:00
date created: 2025-12-17 19:30:00 +09:00
---

## Tree & Graph: 관계를 표현하는 구조

세상은 선형적 (Linear) 이지 않습니다. 계층적 (Hierarchy) 이거나 그물망 (Network) 처럼 연결되어 있습니다.

이를 표현하기 위한 자료구조가 트리와 그래프입니다.

### 🌳 Tree (계층 구조)

트리는 **"순환 (Cycle) 이 없는 그래프"**입니다.

- **Context**: 파일 시스템 폴더 구조, HTML DOM 트리, 회사 조직도, 그리고 **iOS 의 View Hierarchy**.
- **Recursive**: 트리는 본질적으로 재귀적입니다. "자식 뷰의 자식 뷰"를 찾는 로직은 재귀 함수 하나로 끝납니다.

#### Binary Search Tree (BST)
- **Rule**: `Left Child < Parent < Right Child`.
- **Power**: 이 규칙 덕분에 검색 공간을 매번 절반으로 줄일 수 있습니다. (**O(log n)**). 100 만 개의 데이터도 20 번 (`log2(1,000,000)`) 비교면 찾습니다.
- **Balance**: 한쪽으로 치우치면 (Skewed) O(n) 이 됩니다. 그래서 현실에서는 스스로 균형을 잡는 **Red-Black Tree**나 **AVL Tree**를 씁니다. (DB 인덱스, map 내부 구현)

---

### 🕸️ Graph (네트워크 구조)

트리보다 더 일반적인, "Node 와 Edge 의 집합"입니다. 순환 (Cycle) 이 있을 수 있습니다.

#### 탐색의 두 가지 방법 (BFS vs DFS)

| 구분 | BFS (Breadth-First Search) | DFS (Depth-First Search) |
| :--- | :--- | :--- |
| **방식** | 넓게 퍼짐 (물결 파동처럼) | 한 우물만 팜 (미로 찾기처럼) |
| **자료구조** | **Queue** (줄 세우기) | **Stack** / **Recursion** |
| **강점** | **최단 거리** (Shortest Path) 보장 | 구현이 간단 (재귀 사용) |
| **활용 예** | 내비게이션 경로, 페이스북 친구 촌수 | 미로 찾기, 사이클 탐지 |

>[!TIP] **Context**
>"최단 경로를 찾아라" 문제가 나오면 무조건 **BFS**입니다. DFS 는 해를 찾을 수는 있지만, 그게 최단이라는 보장은 없습니다.

---

### ⛰️ Heap (Priority Queue)

힙은 정렬된 트리가 아니라, **"부모가 자식보다 크다 (Max Heap)"**라는 규칙만 지키는 느슨한 트리입니다.

- **목적**: 가장 큰 값 (혹은 작은 값) **하나**를 빠르게 (`O(1)`) 꺼내기 위함입니다.
- **삽입/삭제**: `O(log n)`. 트리의 높이만큼만 재정렬 (Heapify) 하면 됩니다.
- **Context (OS Scheduler)**: 운영체제는 수천 개의 프로세스 중 **우선순위가 가장 높은 놈**을 다음에 실행해야 합니다. 이때 전체를 정렬 (`O(n log n)`) 하는 건 낭비입니다. 힙을 쓰면 `O(log n)` 만에 다음 타자를 뽑을 수 있습니다.

#### 📚 연결 문서

- [Big-O](../00_fundamentals/complexity-and-big-o.md) - O(log n) 의 위대함
- [linear](linear.md) - BFS 에 쓰이는 Queue 구현
- [그래프 탐색](../02_algorithms/graph-traversal.md) - BFS/DFS 의 상세 구현과 활용
- [최단 경로](../02_algorithms/shortest-path.md) - 다익스트라와 플로이드-와샬
- [최소 신장 트리](../02_algorithms/minimum-spanning-tree.md) - 크루스칼과 프림 알고리즘
- [kernel: 프로세스 스케줄링](../../../02_references/operating-systems/kernel.md) - 힙 자료구조가 쓰이는 곳
