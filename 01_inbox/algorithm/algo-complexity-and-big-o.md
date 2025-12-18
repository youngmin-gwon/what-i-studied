---
title: algo-complexity-and-big-o
tags: [algorithm, big-o, complexity, optimization, performance]
aliases: [Big-O, 공간 복잡도, 시간 복잡도]
date modified: 2025-12-18 10:04:37 +09:00
date created: 2025-12-17 19:00:00 +09:00
---

## 복잡도 이론과 Big-O: 엔지니어의 자원 관리법

"이 코드는 O(n) 입니다"라는 말은 면접용 정답이 아닙니다.

**"데이터가 10 배 늘어날 때, 서버 비용은 몇 배 늘어나는가?"** 에 대한 경제학적 대답입니다.

### 💡 Why it matters (Context)

- **Scalability (확장성)**: 사용자가 100 명일 때 0.1 초 걸리던 API 가, 100 만 명이 되면 1000 초가 걸린다면? 그 서비스는 망합니다. 복잡도는 **서비스의 수명**을 예측하는 지표입니다.
- **DoS 공격 방어**: 해시 충돌을 유도해 O(1) 조회를 O(n) 으로 만들면 서버 CPU 가 100% 가 됩니다. 알고리즘을 모르면 보안 취약점이 됩니다. (ReDoS 등)
- **Latency Guarantee**: 실시간 시스템 (게임, 주식 거래) 에서는 O(1) 보다 **Worst Case 가 O(log n) 인 것**이 더 나을 수 있습니다. 예측 불가능한 튀는 값 (Spike) 이 없어야 하기 때문입니다.

---

### 🚦 Big-O 표기법의 실체

Big-O 는 **상한선 (Upper Bound)** 입니다. "아무리 느려도 이 정도는 보장한다"는 약속입니다.

#### 주요 복잡도 스펙트럼

| 표기             | 별명               | 실행 시간 (N=100) | 실행 시간 (N=1 만) | 예시                                            |
| :------------- | :--------------- | :------------ | :------------ | :-------------------------------------------- |
| **O(1)**       | Constant (상수)    | 1             | 1             | Hash Map 조회, Array 인덱스 접근                     |
| **O(log n)**   | Logarithmic (로그) | 7             | 14            | Binary Search, Balanced Tree (Red-Black, AVL) |
| **O(n)**       | Linear (선형)      | 100           | 10,000        | for loop, Linked List 탐색                      |
| **O(n log n)** | Lineariths       | 700           | 140,000       | Merge Sort, Quick Sort (Avg), Heap Sort       |
| **O(n^2)**     | Quadratic (제곱)   | 10,000        | 1 억 (위험)      | 2 중 for loop, Insertion Sort, Selection Sort  |
| **O(2^n)**     | Exponential (지수) | 우주 멸망         | 계산 불가         | 재귀 피보나치, 외판원 순회 (TSP)                         |

>[!TIP] **현실적인 한계**
> -   **O(n^2)**: N=10,000 을 넘어가면 타임아웃 (1 초) 위험이 큽니다.
> -   **O(n!)**: N=12 만 돼도 4 억 7 천만입니다. 순열 (Permutation) 문제는 N 이 작을 때만 가능합니다.

---

### ⚖️ Time vs Space Trade-off

"시간을 아끼려면 메모리를 써라. 메모리를 아끼려면 시간을 써라."

#### 1. Space-Time Trade-off
- **Hash Table**: 메모리를 많이 써서 (공간 O(n)), 검색을 빠르게 (시간 O(1)) 만듭니다.
- **Memoization (DP)**: 이미 계산한 값을 메모배열에 저장해 (공간 O(n)), 중복 계산을 없앰 (시간 O(2^n) -> O(n)).

#### 2. In-Place Algorithm

추가 메모리를 거의 안 쓰는 (O(1) Space) 알고리즘입니다.

- **Quick Sort**: 추가 배열 없이 swap 만으로 정렬합니다. 공간 효율적이라 캐시 히트율이 좋습니다.
- **Merge Sort**: 필연적으로 O(n) 의 보조 배열이 필요합니다. 메모리가 부족한 임베디드 환경에서는 Quick Sort 가 선호되는 이유입니다.

---

### 💾 Amortized Analysis (분할 상환 분석)

"가끔 비싼 비용을 치르지만, 평균내면 싸다."

**동적 배열 (Dynamic Array) 의 `append`**:
- 대부분은 O(1) 입니다 (빈 칸에 넣기만 하면 됨).
- 배열이 꽉 차면 **Capacity 를 2 배로 늘리고 복사 (Resize)** 합니다. 이때는 O(n) 이 걸립니다.
- 하지만 Resize 는 자주 일어나지 않으므로, 전체 N 번의 `append` 를 하면 총비용은 O(n) 입니다.
- 따라서 1 회 평균 비용은 **Amortized O(1)** 입니다.

>[!WARNING] **Latency Critical 시스템 주의**
>"평균 O(1)"은 믿으면 안 됩니다. Resize 가 터지는 순간 수 밀리초가 멈춥니다 (Jitter). 실시간 오디오 처리나 고빈도 거래 (HFT) 에서는 미리 용량을 확보 (`reserveCapacity`) 하거나 Linked List 를 써야 합니다.

---

### 🧪 Latency Numbers Every Programmer Should Know

알고리즘이 실제 하드웨어에서 얼마나 걸리는지 감을 잡아야 합니다. (Jeff Dean @ Google)

- **L1 Cache 참조**: 0.5 ns
- **Branch Mispredict**: 5 ns
- **L2 Cache 참조**: 7 ns
- **Mutex Lock/Unlock**: 25 ns
- **Main Memory 참조**: 100 ns (L1 보다 200 배 느림) -> [[algo-ds-linear|Linked List가 느린 이유]]
- **SSD Random Read**: 150,000 ns
- **Packet Roundtrip (CA->Netherlands)**: 150,000,000 ns (150ms)

👉 **결론**: 네트워크 호출 한 번 (150ms) 줄이는 게, Bubble Sort 를 Quick Sort 로 바꾸는 것 (수 ms 절약) 보다 훨씬 큰 성능 향상을 가져옵니다. **병목 (Bottleneck)**을 먼저 찾으세요.

#### 📚 연결 문서
- [[algo-ds-linear]] - 메모리 레이아웃과 캐시 효율성
- [[algo-ds-hash-and-map]] - O(1) 의 비밀과 해시 충돌
- [[kernel#2. NUMA (Non-Uniform Memory Access)]] - 메모리 접근 비용의 심화
