---
title: greedy-algorithm
tags: [algorithm, greedy, optimization, heuristic]
aliases: [그리디, 탐욕법, Greedy Choice, 최적해]
date modified: 2025-12-18 11:48:24 +09:00
date created: 2025-12-18 11:48:24 +09:00
---

## Greedy Algorithm: "지금 이 순간 최선을 다하기"

**핵심**: 미래를 생각하지 않고 **매 결정의 순간마다 가장 좋아 보이는 선택**을 하는 알고리즘입니다.

그리디 알고리즘은 **국소적인 최적해(Local Optimum)**를 계속 선택하다 보면 결국 **전역적인 최적해(Global Optimum)**에 도달할 것이라는 믿음을 전제로 합니다.

### 💡 Why it matters (Context)

- **거스름돈**: 동전 개수 최소화하여 돈 거슬러 주기
- **회의실 배정**: 겹치지 않게 최대한 많은 회의 예약하기
- **파일 압축**: 빈도가 높은 문자에 짧은 코드 할당 (허프만 코딩)
- **최소 비용 연결**: 모든 도시를 최소 비용으로 연결 (Kruskal/Prim)

---

### 🏢 실무 사례

#### Greedy 활용
- **네트워크 라우팅 (OSPF)**: 패킷을 보낼 때 다음 노드 중 가장 빠른 경로 선택
- **데이터 압축 (ZIP/JPEG)**: 허프만 코딩(Huffman Coding)을 통한 무손실 압축
- **머신러닝 (Decision Tree)**: 각 분기점에서 정보 이득(Information Gain)이 가장 높은 특성 선택
- **Amazon/Coupang 배송 경로**: 특정 구역 내에서 가장 가까운 포인트부터 배송 (근사 최적해)
- **Task Scheduling**: 클라우드 서버에서 들어오는 요청을 특정 기준(가장 짧은 작업 등)으로 우선순위 할당
- **Financial Trading**: 지정가 주문 체결 시 즉각적인 수익이 발생하는 가격 우선 체결

---

## 🔑 그리디의 성립 조건

그리디로 풀었을 때 항상 최적해를 얻으려면 다음 두 조건이 만족되어야 합니다.

### 1. **Greedy Choice Property (탐욕적 선택 조건)**
"앞의 선택이 뒤의 선택에 영향을 주지 않으면서, 매 순간의 최적 선택이 결국 전체의 최적해가 됨"

### 2. **Optimal Substructure (최적 부분 구조)**
"큰 문제의 최적해는 작은 부분 문제들의 최적해들로 구성됨" (DP와 공통점)

> [!CAUTION] **주의: 그리디는 만능이 아닙니다!**
> 위 조건이 만족되지 않는 문제(예: 0/1 배낭 문제)에 그리디를 적용하면 **오답**을 낼 수 있습니다. 이 경우 보통 **Dynamic Programming**으로 해결해야 합니다.

---

## 🔥 필수 Greedy 패턴

### Pattern 1: Coin Change (거스름돈) - 특정 조건 하

**문제**: 500원, 100원, 50원, 10원 동전이 무한히 있을 때 최소 개수로 거슬러 주기

```python
def greedy_coin_change(amount, coins):
    # 동전이 큰 순서대로 정렬되어 있어야 함 (Greedy Choice)
    coins.sort(reverse=True)
    count = 0
    details = {}
    
    for coin in coins:
        num = amount // coin
        count += num
        amount %= coin
        details[coin] = num
        
    return count, details

# 1260원 → (5, {500: 2, 100: 2, 50: 1, 10: 1})
```

**조건**: 큰 동전이 항상 작은 동전들의 배수여야 함. (만약 400원 동전이 추가되면 그리디로 풀 수 없음 → DP 사용)

---

### Pattern 2: Activity Selection (회의실 배정)

**문제**: 회의 시간이 겹치지 않게 하면서 하나의 회의실을 가장 많이 사용할 수 있는 회의 수 찾기

```python
def activity_selection(meetings):
    # 1. 종료 시간(End Time) 기준으로 오름차순 정렬 ⭐ 핵심
    meetings.sort(key=lambda x: x[1])
    
    count = 0
    last_end_time = 0
    selected_meetings = []
    
    for start, end in meetings:
        # 2. 다음 회의 시작 시간이 이전 회의 종료 시간보다 크거나 같으면
        if start >= last_end_time:
            selected_meetings.append((start, end))
            last_end_time = end
            count += 1
            
    return count, selected_meetings

# [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
# → 4번 [(1, 4), (5, 7), (8, 11), (12, 14)]
```

**인사이트**: 종료 시간이 빠를수록 다음에 선택할 수 있는 시간의 폭이 넓어집니다.

---

### Pattern 3: Fractional Knapsack (부분 배낭 문제)

**문제**: 물건을 **쪼갤 수 있을 때**, 무게 제한 안에서 가치 최대화

```python
def fractional_knapsack(items, capacity):
    # 1. 단위 무게당 가치(value/weight) 기준으로 정렬 ⭐ 핵심
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    
    total_value = 0
    for weight, value in items:
        if capacity >= weight:
            # 다 넣을 수 있으면
            capacity -= weight
            total_value += value
        else:
            # 쪼개서 넣기
            fraction = capacity / weight
            total_value += value * fraction
            break
            
    return total_value

# items: [(weight, value)]
# [(10, 60), (20, 100), (30, 120)], capacity: 50
# 10kg(60) + 20kg(100) + 나머지 20kg(80) = 240
```

---

### Pattern 4: Huffman Coding (허프만 코딩)

**문제**: 자주 나타나는 문자에는 짧은 비트를, 드물게 나타나는 문자에는 긴 비트를 할당하여 데이터 압축

```python
import heapq

def build_huffman_tree(frequencies):
    # 1. 모든 문자를 우선순위 큐(Min Heap)에 삽입
    heap = [[weight, [char, ""]] for char, weight in frequencies.items()]
    heapq.heapify(heap)
    
    # 2. 가장 작은 빈도 두 개를 합쳐서 부모 노드 생성 반복
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        
        # 합쳐진 노드: [빈도합, [왼쪽자식, 오른쪽자식]]
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

# frequencies = {'a': 45, 'b': 13, 'c': 12, 'd': 16, 'e': 9, 'f': 5}
```

---

## ⚖️ Greedy vs Dynamic Programming

| 특징 | Greedy | Dynamic Programming |
|:---|:---|:---|
| **결정 방식** | 매 순간 가장 좋은 하나를 선택 | 모든 가능성을 고려하여 최적을 선택 |
| **속도** | 매우 빠름 (O(n) 또는 O(n log n)) | 느림 (O(n²) 등 중첩 반복문) |
| **최적성** | 보장되지 않을 때가 많음 | 항상 전역 최적해 보장 |
| **정렬** | 보통 정렬이 수반됨 | 메모이제이션/테이블 활용 |

---

## 🎓 Greedy 문제 해결 전략

### 1. **관찰과 직관**
"어떤 기준으로 정렬하거나 선택했을 때 가장 유리할까?" (예: 종료 시간, 가격 대비 무게 등)

### 2. **그리디가 반례 없이 작동하는지 확인**
"지금 나의 최선이 나중에 발목을 잡지 않는가?"

### 3. **정렬 또는 우선순위 큐 사용**
그리디는 대부분 데이터를 특정 순서로 처리할 때 강력합니다.

---

## 🧪 고급 기법

### Prim's & Kruskal's Algorithm
최소 신장 트리(MST)를 찾는 그리디의 대표격입니다. [Union-Find](../01_data-structures/disjoint-set.md)를 활용하여 효율적으로 구현합니다.

### Dijkstra's Algorithm
가중치 그래프에서 최단 경로를 찾는 알고리즘 역시 그리디 접근 방식입니다. (현재 도달한 노드 중 가장 짧은 거리 선택)

---

## 🚨 흔한 실수

1. **정렬 기준 선정 오류** ❌
   - 회의실 배정에서 "시작 시간"이나 "짧은 회의 시간" 기준으로 정렬하면 오답이 나옵니다.
   - 반드시 **"종료 시간"**이 기준이어야 합니다.

2. **그리디를 쓰지 말아야 할 때 사용** ❌
   - 0/1 Knapsack 문제를 "가성비" 그리디로 풀려고 시도함.
   - 가성비로만 채우면 가득 차지 않고 남는 공간에 더 비싼 걸 넣을 수 있는 기회를 놓침.

3. **우선순위 큐 미활용**
   - 데이터가 동적으로 추가되면서 매번 최솟값/최댓값을 찾아야 한다면 단순 정렬보다 [Heap](../01_data-structures/heap-and-priority-queue.md)이 훨씬 빠릅니다.

---

## 📚 관련 문서

- [동적 계획법](dynamic-programming.md) - 그리디가 해결하지 못하는 전역 최적해 문제의 해법
- [힙과 우선순위 큐](../01_data-structures/heap-and-priority-queue.md) - 매 순간 최적의 요소를 찾기 위한 효율적 도구
- [서로소 집합](../01_data-structures/disjoint-set.md) - 크루스칼(Kruskal) 알고리즘의 핵심 구현체
- [검색과 정렬](search-and-sort.md) - 그리디 적용 전 데이터 정렬의 중요성
- [최적화 전략](../03_patterns/optimization.md) - 다양한 문제 상황에 따른 그리디 vs DP 선택 기준
