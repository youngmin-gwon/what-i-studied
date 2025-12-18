---
title: algo-ds-linear
tags: [algorithm, array, cache, data-structures, linked-list, queue, stack]
aliases: [배열, 스택, 연결 리스트, 큐]
date modified: 2025-12-18 10:05:54 +09:00
date created: 2025-12-17 19:10:00 +09:00
---

## 선형 자료구조: 메모리 배치의 미학

Array 와 Linked List 의 차이를 "중간 삽입이 O(1) 이냐 O(n) 이냐"로만 설명한다면 하수입니다.

진짜 차이는 **CPU 가 메모리를 어떻게 읽느냐 (Cache Locality)**에 있습니다.

### ⚔️ Array vs Linked List: 하드웨어의 관점

이론적인 Big-O 만 보면 Linked List 가 삽입/삭제에서 우월해 보입니다. 하지만 실무에서는 Array(`ArrayList`, `std::vector`) 가 90% 이상 쓰입니다. 왜일까요?

#### 1. Memory Layout (메모리 배치)

- **Array**: 모든 요소가 물리적으로 **연속된 메모리 (Contiguous Memory)**에 있습니다.
    - `[0x100, 0x104, 0x108, 0x10C …]`
- **Linked List**: 요소들이 힙 메모리 여기저기에 흩어져 있고, 포인터로 연결됩니다.
    - `[0x500] -> [0x920] -> [0x120] …`

#### 2. Cache Locality (캐시 지역성)

CPU 는 메모리에서 데이터를 읽을 때, 한 번에 한 바이트 (Byte) 만 읽지 않습니다. **캐시 라인 (Cache Line, 보통 64 Bytes)** 단위로 덩어리째 읽어옵니다.

- **Array 순회**: `arr[0]` 을 읽을 때 `arr[1]…arr[15]` 까지 캐시에 같이 딸려옵니다. 다음 데이터 접근 시 L1 Cache Hit 가 터집니다. (매우 빠름, ~0.5ns)
- **Linked List 순회**: `node1` 을 읽어도 `node2` 는 전혀 다른 주소에 있습니다. 매번 Cache Miss 가 발생하고 Main Memory 를 뒤져야 합니다. (느림, ~100ns)

>[!IMPORTANT] **결론**
>데이터 개수가 아주 많고 삽입/삭제가 빈번한 특수 상황이 아니라면, **Array 가 기본값 (Default)**입니다. 포인터 자체의 메모리 오버헤드 (64bit 머신에서 8 바이트) 도 무시할 수 없습니다.

---

### 📚 Stack & Queue

#### 1. Stack (LIFO: Last In First Out)
- **구현**: 보통 `Array` 의 끝 (`append`/`pop`) 을 사용합니다.
- **Context (Call Stack)**: 함수 호출이 스택 구조인 이유는, 실행이 끝나면 **"가장 최근에 중단된 지점"**으로 돌아가야 하기 때문입니다. 재귀 함수가 깊어지면 `Stack Overflow` 가 나는 그 스택입니다.

#### 2. Queue (FIFO: First In First Out)
- **구현**: `Array` 로 구현하면 앞쪽 (`[0]`) 을 뺄 때 나머지 요소를 다 당겨야 해서 O(n) 이 됩니다.
- **Circular Buffer (Ring Buffer)**: 시작 (`head`) 과 끝 (`tail`) 포인터를 두고, 배열을 둥글게 맙니다. 이러면 삽입/삭제 모두 O(1) 이며, 메모리 재할당도 필요 없습니다. 네트워크 패킷 버퍼나 키보드 입력 버퍼가 이렇게 생겼습니다.

---

### 🛠️ 실전 응용 (Real-World Use Cases)

#### Sentinel Node (보초병 노드)

Linked List 구현 시 `head` 나 `tail` 이 `null` 인지 매번 검사 (if 문) 하는 것은 귀찮고 버그가 생기기 쉽습니다.

- **Dummy Node**: 비어있는 `dummyHead` 와 `dummyTail` 을 미리 만들어두면, 노드가 0 개일 때나 1 개일 때나 **로직이 똑같아집니다.** (코드가 깔끔해짐)

#### Runner Technique (Two Pointers)

Linked List 에는 `size` 프로퍼티가 없는 경우가 많습니다. 중간 지점을 찾으려면?

- **Fast & Slow Runner**: `Fast` 는 2 칸씩, `Slow` 는 1 칸씩 갑니다. `Fast` 가 끝에 도착하면 `Slow` 는 정확히 중간에 있습니다. 이를 이용해 사이클 (Cycle) 존재 여부도 판별할 수 있습니다.

#### 📚 연결 문서
- [[algo-complexity-and-big-o]] - 시간 복잡도 기초
- [[kernel#2. NUMA (Non-Uniform Memory Access)]] - 메모리 접근 속도 차이
- [[apple-memory-management]] - 포인터와 메모리 관리
