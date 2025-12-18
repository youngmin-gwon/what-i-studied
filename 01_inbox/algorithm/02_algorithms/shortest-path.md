---
title: shortest-path-algorithms
tags: [algorithm, graph, shortest-path, dijkstra, bellman-ford, floyd-warshall]
aliases: [최단 경로, 다익스트라, 벨만-포드, 플로이드-와샬]
date modified: 2025-12-18 11:48:24 +09:00
date created: 2025-12-18 11:48:24 +09:00
---

## Shortest Path Algorithms: "가장 빠른 길 찾기"

**핵심**: 그래프의 지점(Node) 간을 연결하는 간선(Edge)의 가중치 합이 **최소가 되는 경로**를 찾는 알고리즘입니다.

### 💡 Why it matters (Context)

- **내비게이션**: 출발지에서 목적지까지 가장 빠른 도로 찾기
- **네트워크 라우팅**: 데이터 패킷을 가장 적은 시간 내에 목적지 서버로 전송
- **SNS**: 두 사람 사이의 최단 인맥 거리 측정
- **게임 AI**: 캐릭터가 장애물을 피해 목표물로 이동하는 최단 거리 계산

---

### 🏢 실무 사례

#### Shortest Path 활용
- **Google Maps / T-Map**: 실시간 교통 상황을 반영한 경로 탐색 (Dijkstra 변형)
- **Ride-sharing (Uber/Grab)**: 승객과 가장 가까운 기사 매칭 및 최적 운행 경로 산출
- **Internet Routing Protocol (OSPF)**: 대역폭과 혼잡도를 고려한 최적 데이터 전송 경로 선정
- **Logistics (FedEx/DHL)**: 허브 간 최적 운송망 구축을 통한 비용 절감
- **Blockchain**: P2P 네트워크 노드 간 메시지 전파 경로 최적화
- **Game Development**: NPC 의 A* Pathfinding (Dijkstra 의 발전된 형태)

---

## 🧭 알고리즘 선택 가이드

| 상황 | 추천 알고리즘 | 복잡도 | 특이사항 |
|:---|:---|:---|:---|
| **한 지점 → 모든 지점** (양수 가중치) | **Dijkstra** (다익스트라) | O(E log V) | 가장 범용적임 ⭐ |
| **한 지점 → 모든 지점** (음수 가중치 포함) | **Bellman-Ford** (벨만-포드) | O(VE) | 음수 사이클 탐지 가능 |
| **모든 지점 → 모든 지점** | **Floyd-Warshall** (플로이드-와샬) | O(V³) | 노드 수가 적을 때 유리 |
| **가중치 없는 그래프** | **BFS** | O(V+E) | 가장 빠름 |

---

## ⚡ Dijkstra's Algorithm (다익스트라)

**"매 순간 가장 가까운 노드부터 확정하기"**

그리디 방식을 사용하며, 현재까지 알고 있는 가장 짧은 경로를 가진 노드를 선택해 나갑니다.

### 🔧 구현 (우선순위 큐 활용)

```python
import heapq

def dijkstra(graph, start):
    # 1. 거리 테이블 초기화 (무한대)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # 2. 우선순위 큐 생성 (거리, 노드)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)
        
        # 3. 이미 처리된 적 있는 노드라면 무시
        if current_dist > distances[current_node]:
            continue
            
        # 4. 이웃 노드 확인 및 거리 업데이트
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            
            # 더 짧은 경로를 찾았다면 업데이트
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

# graph = {'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 5}, ...}
```

> [!IMPORTANT] **다익스트라의 조건**
> 간선의 가중치가 **음수**이면 사용할 수 없습니다. 가중치가 음수면 이미 방문한 노드의 최단 거리가 나중에 바뀔 수 있기 때문입니다.

---

## 📉 Bellman-Ford Algorithm (벨만-포드)

**"모든 간선을 V-1번 반복해서 확인하기"**

음수 가중치가 있어도 작동하며, **음수 사이클**(무한히 거리가 줄어드는 순환) 존재 여부를 판별할 수 있습니다.

### 🔧 구현

```python
def bellman_ford(graph, start, num_nodes):
    distances = [float('inf')] * num_nodes
    distances[start] = 0
    
    # 노드 수 - 1 번 반복
    for i in range(num_nodes):
        for u in graph:
            for v, weight in graph[u]:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    # V 번째 반복에도 값이 갱신되면 음수 사이클 존재
                    if i == num_nodes - 1:
                        return "Negative cycle detected"
                        
    return distances
```

---

## 🌐 Floyd-Warshall Algorithm (플로이드-와샬)

**"거쳐가는 노드를 기준으로 테이블 업데이트"**

거리가 갱신될 때마다 `D[i][j] = min(D[i][j], D[i][k] + D[k][j])` 공식을 사용합니다.

### 🔧 구현

```python
def floyd_warshall(matrix, n):
    # matrix는 인접 행렬
    dist = [row[:] for row in matrix]
    
    # k = 거쳐가는 노드
    for k in range(n):
        # i = 출발 노드
        for i in range(n):
            # j = 도착 노드
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    return dist
```

---

## 🎓 최단 경로 문제 해결 전략

### 1. **그래프 종류 파악**
- 가중치가 있는가? (없으면 BFS)
- 음수 가중치가 있는가? (있으면 Bellman-Ford)

### 2. **질문의 범위 확인**
- 한 곳에서 가나? (Dijkstra)
- 모든 노드끼리의 관계를 보나? (Floyd-Warshall)

### 3. **구현 효율성**
- 노드와 간선의 수에 따라 어떤 알고리즘이 시간 내에 통과할지 계산 루프를 미리 예상하세요.

---

## 🚨 흔한 실수

1. **인접 행렬 vs 인접 리스트 선택** ❌
   - 간선이 적은 그래프(Sparse Graph)에서 인접 행렬을 쓰면 메모리와 시간이 낭비됩니다 (Dijkstra 구현 시 특히 주의).

2. **우선순위 큐 갱신 누락**
   - 다익스트라에서 `current_dist > distances[current_node]` 체크를 생략하면 큐에 들어있는 낡은 정보들을 모두 처리하느라 속도가 매우 느려집니다.

3. **다익스트라에서 음수 가중치 처리 시도** ❌
   - 무한 루프에 빠지거나 잘못된 결과를 낼 수 있습니다.

---

---

## 📚 관련 문서
- [그래프 탐색](graph-traversal.md) - 가중치 없는 그래프에서의 BFS 최단 경로 탐색
- [힙과 우선순위 큐](../01_data-structures/heap-and-priority-queue.md) - 다익스트라 알고리즘의 성능 최적화 핵심
- [그리디 알고리즘](greedy.md) - 다익스트라가 국소 최적해를 찾는 방식의 이해
- [동적 계획법](dynamic-programming.md) - 플로이드-와샬 알고리즘의 점화식 설계 원리
- [최소 신장 트리](minimum-spanning-tree.md) - MST와 최단 경로 문제의 목적 차이 분석
