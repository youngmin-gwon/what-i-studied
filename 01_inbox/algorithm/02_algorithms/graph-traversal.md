---
title: graph-traversal
tags: [algorithm, bfs, dfs, graph-traversal]
aliases: [BFS, DFS, 그래프 탐색, 깊이 우선 탐색, 너비 우선 탐색]
date modified: 2025-12-18 11:42:11 +09:00
date created: 2025-12-18 11:39:21 +09:00
---

## Graph Traversal: BFS & DFS

그래프를 탐색하는 두 가지 근본적인 방법입니다. **"모든 노드를 방문하되, 어떤 순서로?"** 가 핵심입니다.

### 💡 Why it matters (Context)

- **미로 찾기**: 출구까지의 경로는?
- **SNS 친구 찾기**: A 의 친구의 친구는?
- **웹 크롤링**: 링크를 따라가며 모든 페이지 방문
- **파일 시스템**: 폴더 구조 전체 탐색

---

### 🏢 실무 사례

#### BFS 활용
- **LinkedIn/Facebook 친구 추천**: "아는 사람일 수도" (2촌, 3촌 찾기)
- **Google Maps 경로 찾기**: 가중치 없는 경우 BFS로 최단 경로
- **Netflix 추천 알고리즘**: 사용자 관계 그래프 탐색
- **Git**: 커밋 히스토리 브랜치별 탐색
- **네트워크 패킷 라우팅**: 최소 홉(hop) 경로 찾기

#### DFS 활용
- **WebCrawler (검색엔진)**: 한 사이트를 깊게 파고들며 크롤링
- **파일 시스템 검색**: `find` 명령어 (디렉토리 깊이 우선)
- **IDE 코드 네비게이션**: "Find all references" (의존성 그래프)
- **컴파일러**: 순환 참조 탐지 (import cycle detection)
- **CI/CD Pipeline**: 작업 의존성 순서 결정 (Topological Sort)
- **Garbage Collector**: 참조되지 않는 객체 찾기

---

## 🌊 BFS (Breadth-First Search)

**"물결처럼 퍼져나가며 탐색"** - 가까운 것부터 차례대로

### 원리

```plaintext
시작점에서 거리 순서대로 탐색:
  거리 0: [시작점]
  거리 1: [시작점의 이웃들]
  거리 2: [거리 1 노드들의 이웃들]
  ...
```

**핵심 자료구조**: **Queue** (FIFO)

---

### 🔧 구현

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []
    
    while queue:
        node = queue.popleft()  # 맨 앞에서 꺼냄
        result.append(node)
        
        # 이웃 노드들을 큐에 추가
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result

# 그래프 (인접 리스트)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs(graph, 'A'))
# ['A', 'B', 'C', 'D', 'E', 'F']
```

**시간 복잡도**: O(V + E) - 모든 정점(V)과 간선(E) 한 번씩 방문

---

### 🎯 BFS 핵심 특징

>[!IMPORTANT] **최단 경로 보장**
> **가중치 없는 그래프**에서 BFS 는 **항상 최단 경로**를 찾습니다.
>
>왜? 거리 순서대로 탐색하기 때문에, 처음 도달한 경로가 곧 최단 경로입니다.

---

### 🎯 BFS 실전 패턴

#### Pattern 1: 최단 거리 찾기

```python
def shortest_path_bfs(graph, start, end):
    visited = set([start])
    queue = deque([(start, 0)])  # (노드, 거리)
    
    while queue:
        node, distance = queue.popleft()
        
        if node == end:
            return distance  # 최단 거리!
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return -1  # 도달 불가
```

#### Pattern 2: 레벨별 탐색 (트리)

```python
def level_order_traversal(root):
    """이진 트리 레벨별 순회"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)  # 현재 레벨 크기
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# [[1], [2, 3], [4, 5, 6]]
```

#### Pattern 3: 미로 탐색 (2D Grid)

```python
def shortest_path_in_maze(maze, start, end):
    """
    maze: 2D 배열 (0=길, 1=벽)
    start, end: (row, col) 튜플
    """
    rows, cols = len(maze), len(maze[0])
    visited = set([start])
    queue = deque([(start, 0)])  # ((row, col), distance)
    
    # 4방향 이동
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        (r, c), dist = queue.popleft()
        
        if (r, c) == end:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # 범위 체크, 벽 체크, 방문 체크
            if (0 <= nr < rows and 0 <= nc < cols and
                maze[nr][nc] == 0 and (nr, nc) not in visited):
                
                visited.add((nr, nc))
                queue.append(((nr, nc), dist + 1))
    
    return -1
```

#### Pattern 4: 섬의 개수 (BFS 버전)

```python
def num_islands_bfs(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0
    
    def bfs(r, c):
        queue = deque([(r, c)])
        visited.add((r, c))
        
        while queue:
            row, col = queue.popleft()
            
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = row + dr, col + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                    grid[nr][nc] == '1' and (nr, nc) not in visited):
                    
                    visited.add((nr, nc))
                    queue.append((nr, nc))
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r, c)
                count += 1
    
    return count
```

---

## 🌲 DFS (Depth-First Search)

**"한 우물만 파며 탐색"** - 끝까지 가본 후 돌아옴

### 원리

```plaintext
한 방향을 끝까지 탐색 후 백트래킹:
  A → B → D (막힘, 돌아감)
    → B → E → F (막힘, 돌아감)
  A → C → F (이미 방문, 돌아감)
```

**핵심 자료구조**: **Stack** 또는 **Recursion** (Call Stack)

---

### 🔧 구현

#### 1. 재귀 버전 (일반적)

```python
def dfs_recursive(graph, node, visited=None, result=None):
    if visited is None:
        visited = set()
    if result is None:
        result = []
    
    visited.add(node)
    result.append(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)
    
    return result

# ['A', 'B', 'D', 'E', 'F', 'C']
```

#### 2. 스택 버전 (반복문)

```python
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        node = stack.pop()  # 맨 뒤에서 꺼냄 (LIFO)
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # 이웃들을 스택에 추가 (역순으로 넣으면 원래 순서로 나옴)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result
```

---

### 🎯 DFS 실전 패턴

#### Pattern 1: 경로 존재 여부 (Path Exists)

```python
def has_path_dfs(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    
    if start == end:
        return True
    
    visited.add(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            if has_path_dfs(graph, neighbor, end, visited):
                return True
    
    return False
```

#### Pattern 2: 모든 경로 찾기

```python
def all_paths_dfs(graph, start, end, path=None):
    if path is None:
        path = []
    
    path = path + [start]  # 새 리스트 생성 (백트래킹용)
    
    if start == end:
        return [path]
    
    paths = []
    for neighbor in graph[start]:
        if neighbor not in path:  # 사이클 방지
            new_paths = all_paths_dfs(graph, neighbor, end, path)
            paths.extend(new_paths)
    
    return paths
```

#### Pattern 3: 사이클 탐지 (유향 그래프)

```python
def has_cycle_directed(graph):
    """유향 그래프 사이클 탐지 - DFS + 상태 추적"""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}
    
    def dfs(node):
        if color[node] == GRAY:  # 현재 경로에서 재방문 = 사이클!
            return True
        if color[node] == BLACK:  # 이미 처리 완료
            return False
        
        color[node] = GRAY  # 탐색 중
        
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        
        color[node] = BLACK  # 탐색 완료
        return False
    
    for node in graph:
        if color[node] == WHITE:
            if dfs(node):
                return True
    
    return False
```

#### Pattern 4: 위상 정렬 (Topological Sort)

```python
def topological_sort_dfs(graph):
    """DFS 기반 위상 정렬"""
    visited = set()
    stack = []
    
    def dfs(node):
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        
        stack.append(node)  # 후위 순서로 추가
    
    for node in graph:
        if node not in visited:
            dfs(node)
    
    return stack[::-1]  # 역순이 위상 순서
```

---

## ⚔️ BFS vs DFS 비교

| 특징 | BFS | DFS |
|:---|:---|:---|
| **자료구조** | Queue (FIFO) | Stack / Recursion |
| **탐색 방식** | 레벨 순서 (넓게) | 깊이 순서 (깊게) |
| **최단 경로** | ✅ 보장 (가중치 없는 그래프) | ❌ 보장 안 됨 |
| **메모리** | O(너비) - 많이 사용 | O(깊이) - 적게 사용 |
| **구현** | 반복문 (일반적) | 재귀 (일반적) |
| **완전 탐색** | 레벨별 순서 | 경로별 순서 |

---

### 🎯 언제 무엇을 쓸까?

>[!TIP] **BFS 추천**
> - **최단 경로** 필요
> - **레벨별 처리** (트리의 각 층)
> - **가까운 것부터** 찾기
> - 예: 미로 최단 경로, SNS 친구 촌수

>[!TIP] **DFS 추천**
> - **경로 존재 여부**만 필요
> - **모든 경로** 탐색
> - **사이클 탐지**
> - **위상 정렬**
> - **백트래킹** 문제
> - 예: 순열/조합, N-Queens, 미로 탈출 가능성

---

## 🧪 고급 응용

### 1. 이분 그래프 판별 (Bipartite Check)

```python
def is_bipartite_bfs(graph):
    """BFS로 이분 그래프 판별"""
    color = {}
    
    for start in graph:
        if start in color:
            continue
        
        queue = deque([start])
        color[start] = 0
        
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]  # 반대 색
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False  # 같은 색 = 이분 그래프 아님
        
    return True
```

### 2. 연결 컴포넌트 개수

```python
def count_connected_components(n, edges):
    """무방향 그래프의 연결 컴포넌트 개수"""
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    count = 0
    
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    for node in range(n):
        if node not in visited:
            dfs(node)
            count += 1
    
    return count
```

---

## 🚨 흔한 실수

1. **방문 체크 시점** ❌
   ```python
   # 잘못된 방법 - 큐에서 꺼낼 때 체크
   while queue:
       node = queue.popleft()
       if node in visited:  # ❌ 중복 방문!
           continue
   
   # 올바른 방법 - 큐에 넣을 때 체크
   if neighbor not in visited:
       visited.add(neighbor)  # ✅ 즉시 마킹
       queue.append(neighbor)
   ```

2. **DFS 재귀 깊이 제한**
   - Python: 기본 재귀 깊이 ~1000
   - 해결: `sys.setrecursionlimit(10**6)`

3. **그리드 탐색에서 범위 체크 누락**
   ```python
   # 반드시 범위 체크 먼저!
   if 0 <= nr < rows and 0 <= nc < cols:  # ✅
   ```

---

## 💾 언어별 구현 팁

```python
# Python - deque 필수
from collections import deque
queue = deque()  # O(1) append/popleft

# list는 느림
queue = []
queue.pop(0)  # O(n) ❌
```

```swift
// Swift - 직접 큐 구현 필요
struct Queue<T> {
    private var inbox: [T] = []
    private var outbox: [T] = []
    
    mutating func enqueue(_ element: T) {
        inbox.append(element)
    }
    
    mutating func dequeue() -> T? {
        if outbox.isEmpty {
            outbox = inbox.reversed()
            inbox.removeAll()
        }
        return outbox.popLast()
    }
}
```

---

---

## 📚 관련 문서
- [[01_data-structures/tree-and-graph|트리와 그래프]] - 인접 행렬과 인접 리스트 등 그래프 표현법
- [[01_data-structures/linear|선형 자료구조]] - 큐(BFS)와 스택(DFS) 자료구조의 이해
- [[01_data-structures/disjoint-set|서로소 집합]] - 연결 컴포넌트 찾기의 효율적 대안
- [[00_fundamentals/complexity-and-big-o|복잡도 분석]] - $O(V + E)$ 시간 복잡도의 의미와 공간 효율성
- [[02_algorithms/backtracking|백트래킹]] - DFS에 가지치기를 더한 최적화 탐색
