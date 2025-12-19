---
title: linear
tags: [algorithm, array, cache, data-structures, linked-list]
aliases: [배열, 연결 리스트, Array, Linked List]
date modified: 2025-12-18 13:05:00 +09:00
date created: 2025-12-17 19:10:00 +09:00
---

## 선형 자료구조: 메모리 배치의 미학

선형 자료구조는 데이터를 일렬로 나열하는 가장 기초적인 방식입니다. Array와 Linked List의 차이를 단순히 "삽입 속도"로만 이해한다면 하드웨어의 위력을 놓치는 것입니다.

### ⚔️ Array vs Linked List: 하드웨어의 관점

이론적인 Big-O만 보면 Linked List가 삽입/삭제에서 $O(1)$로 우월해 보이지만, 실제 성능은 **Array**가 압도적인 경우가 많습니다.

#### 1. Memory Layout (메모리 배치)
- **Array**: 물리적으로 **연속된 메모리 (Contiguous Memory)** 공간을 차지합니다.
- **Linked List**: 요소들이 힙(Heap) 여기저기에 흩어져 있고 포인터로 연결됩니다.

#### 2. Cache Locality (캐시 지역성)
CPU는 데이터를 읽을 때 주변 데이터까지 뭉텅이(Cache Line)로 가져옵니다.
- **Array**: `arr[0]`을 읽을 때 `arr[1]...arr[15]`가 캐시에 같이 들어옵니다. (L1 Cache Hit)
- **Linked List**: 다음 노드가 어디 있을지 몰라 매번 메인 메모리를 뒤져야 합니다. (Cache Miss)

> [!IMPORTANT] **Engineering Default**
> 데이터 개수가 아주 많고 중간 삽입이 빈번한 특수 케이스가 아니라면, **Array가 기본값**입니다.

---

### 🛠️ 실전 테크닉

#### 1. Sentinel Node (보초병 노드)
Linked List 구현 시 `head`나 `tail`이 `null`인지 매번 검사하는 if 문을 없애기 위해 사용합니다. 비어있는 Dummy Node를 하나 두면 삽입/삭제 로직이 훨씬 간결해집니다.

#### 2. Runner Technique (Two Pointers)
연결 리스트에서 중간 지점을 찾거나 사이클(Cycle) 존재 여부를 판별할 때 씁니다. 한 명(Fast)은 2칸씩, 한 명(Slow)은 1칸씩 이동합니다.

---

### 🚨 흔한 실수 (Common Mistakes)

1. **인덱스 범위 초과 (Out of Bounds)** ❌
   - `for i in range(len(arr))` 대신 `len(arr) + 1`을 참조하거나 음수 인덱스에 대한 예외 처리를 잊는 경우.
2. **Linked List의 메모리 누수**
   - C++/Swift처럼 직접 관리하는 언어에서 이전 노드의 참조를 끊지 않아 메모리가 해제되지 않는 경우.
3. **Array 중간 삽입을 O(1)로 착각** ❌
   - `list.insert(0, x)`는 최악의 경우 O(N)입니다. 성능이 중요하다면 [Stack/Queue](stack-and-queue.md)나 `Deque`를 고려하세요.
4. **포인터 소실**
   - 연결 리스트 노드 삭제 시 `prev.next = current.next`를 하기 전 `current`를 먼저 지워버려 연결이 끊기는 실수.

---

### 📚 연결 문서

- [메모리 레이아웃](../00_fundamentals/memory-layout-and-cache.md) - 캐시 지역성과 하드웨어 기초
- [스택과 큐](stack-and-queue.md) - 선형 구조를 활용한 ADT
- [덱(Deque)](specialized-queues.md) - 양방향 삽입/삭제 최적화
- [복잡도](../00_fundamentals/complexity-and-big-o.md) - 선형 탐색의 비용
