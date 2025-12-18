---
title: memory-layout-and-cache
tags: [fundamentals, memory, cache, spatial-locality, temporal-locality, hardware]
aliases: [메모리 레이아웃, 캐시 지역성, 공간 지역성, 시간 지역성, Heap vs Stack]
date modified: 2025-12-18 11:57:00 +09:00
date created: 2025-12-18 11:57:00 +09:00
---

## Memory Layout & Cache Locality: 알고리즘이 "컴퓨터"에서 도는 법

Big-O 복잡도가 같더라도 어떤 알고리즘은 10배 더 빠를 수 있습니다. 그 비밀은 **컴퓨터 하드웨어(메모리 계층 구조)**와 알고리즘이 얼마나 조화로운가에 있습니다.

### 💡 Why it matters (Context)

- **이론 vs 실제**: $O(N)$ 알고리즘이라도 메모리를 마구잡이로 찌르면(Random Access) 메모리를 순차적으로 읽는 것보다 훨씬 느립니다.
- **Cache Hit**: CPU는 RAM보다 훨씬 빠릅니다. CPU 근처의 작은 저장소(Cache)에 데이터가 미리 와 있어야 성능이 폭발합니다.
- **데이터 구조의 선택**: 왜 Linked List보다 Array가 일반적으로 더 선호되는가?에 대한 하드웨어적 해답입니다.

---

### 🏢 실무 사례

#### Memory & Cache 활용
- **게임 엔진 최적화**: 수천 개의 오브젝트를 처리할 때 데이터 지향 설계(Data-Oriented Design)를 통해 캐시 효율 극대화.
- **데이터베이스 엔진**: B-Tree 인덱스 노드 크기를 디스크 페이지나 캐시 라인 크기(예: 64바이트)에 맞춰 최적화.
- **영상 인코딩/디코딩**: 픽셀 데이터를 처리할 때 메모리 접근 순서를 바꿔서 성능 향상.
- **고성능 서버(HFT)**: 메모리 할당을 최소화하고 CPU 캐시를 점유하기 위한 정교한 데이터 배치.

---

## 🏗️ 메모리 계층 구조 (Memory Hierarchy)

CPU에 가까울수록 빠르고 비싸며 용량이 적습니다.

1. **Registers**: 1 cycle (가장 빠름)
2. **L1 Cache**: ~4 cycles
3. **L2 Cache**: ~10 cycles
4. **L3 Cache**: ~40 cycles
5. **Main Memory (RAM)**: **~100-200 cycles** (엄청난 차이!)
6. **Disk (SSD/HDD)**: 수백만 cycle

> [!IMPORTANT] **핵심 목표**
> CPU가 데이터를 기다리느라 노는 시간(Stall)을 줄이는 것이 알고리즘 최적화의 숨은 목표입니다.

---

## 🎯 캐시 지역성 (Cache Locality)

캐시는 데이터를 1바이트씩 가져오지 않고 **Cache Line(보통 64바이트)** 단위로 뭉텅이로 가져옵니다.

### 1. 공간 지역성 (Spatial Locality)
"지금 읽은 데이터 근처의 데이터가 곧 쓰일 확률이 높다."
- **배열(Array)**: 연속된 메모리 공간에 있으므로 한 요소를 읽으면 다음 요소들도 캐시에 같이 들어옵니다. (Cache Hit!)
- **연결 리스트(Linked List)**: 요소들이 메모리 여기저기 흩어져 있어 매번 RAM을 찔러야 합니다. (Cache Miss!)

### 2. 시간 지역성 (Temporal Locality)
"한 번 읽은 데이터는 조만간 다시 쓰일 확률이 높다."
- 반복문에서 같은 변수를 여러 번 참조하는 경우.

---

## 🧠 Heap vs Stack

알고리즘 구현 시 데이터가 어디에 담기는지도 중요합니다.

| 특징 | Stack (스택) | Heap (힙) |
|:---|:---|:---|
| **할당 방식** | 자동 (정적) | 수동 (동적) |
| **속도** | **매우 빠름** (포인터 이동만 수행) | 느림 (공간 찾고 관리하는 비용) |
| **수명** | 함수 종료 시 자동 해제 | 개발자가 해제(`free`, `delete`) 또는 GC |
| **용도** | 지역 변수, 함수 호출 정보 | 거대한 배열, 객체, 수명이 긴 데이터 |

---

## 🚨 흔한 실수 (Common Mistakes)

1. **무분별한 객체 생성** ❌
   - 루프 내부에서 작은 객체를 계속 생성하면 힙 할당 비용과 GC(Garbage Collection) 부담이 커집니다.
2. **2차원 배열 접근 방향**
   - 행(Row) 방향이 아닌 열(Column) 방향으로 먼저 접근하면 공간 지역성을 완전히 깨뜨려 수십 배 느려질 수 있습니다.
   ```python
   # 좋은 예 (Row-major)
   for i in range(rows):
       for j in range(cols):
           sum += matrix[i][j]
   ```
3. **Linked List가 무조건 "삽입 빠르다"고 믿는 것**
   - 삽입 자체는 $O(1)$이지만, 삽입할 지점까지 찾아가는 과정이 캐시 효율 때문에 배열보다 월등히 느릴 수 있습니다.

---

## 🧪 최적화 팁

- **Data-Oriented Design**: 연산에 필요한 데이터들만 모아서 배열로 관리하세요 (Structure of Arrays).
- **Batching**: 큰 데이터를 처리할 때 캐시 한 번에 데이터가 들어오도록 쪼개서 처리하세요.

---

---

## 📚 관련 문서
- [복잡도와 Big-O](complexity-and-big-o.md) - 캐시 효율이 알고리즘 성능에 미치는 영향
- [선형 자료구조](../01_data-structures/linear.md) - 상반된 물리적 배치를 가지는 Array와 Linked List
- [트리와 그래프](../01_data-structures/tree-and-graph.md) - Pointer 기반 구조의 성능 한계
- [재귀와 호출 스택](recursion-and-stack.md) - 스택 메모리와 캐시 계층
