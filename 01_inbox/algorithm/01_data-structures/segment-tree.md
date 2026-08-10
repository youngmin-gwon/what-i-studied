---
title: segment-tree
tags: [data-structure, tree, segment-tree, range-query, optimization]
aliases: [세그먼트 트리, 구간 트리, 구간 합 트리, Segment Tree]
date modified: 2026-08-10 00:00:00 +09:00
date created: 2025-12-18 12:15:00 +09:00
---

## Segment Tree & Fenwick Tree: 구간의 정보를 O(log N)에 지배하기

**세그먼트 트리(Segment Tree)**와 **펜윅 트리(Fenwick Tree, BIT)**는 배열의 특정 구간 $[L, R]$에 대한 질문(합, 최댓값, 최솟값 등)에 응답하고, 데이터가 변경될 때 트리를 업데이트하는 작업을 모두 **$O(\log N)$** 시간 복잡도로 수행하는 심화 자료구조입니다.

### 💡 Why it matters (Context)

- **동적 데이터**: 배열의 값이 자꾸 바뀌는데, 구간 합 질문이 수만 번 들어올 때 사용합니다. (배열이 고정이라면 [Prefix Sum](../03_patterns/prefix-sum.md)이 더 빠릅니다)
- **효율성**: 단순 $O(N)$ 조회를 $O(\log N)$으로 줄여, 대규모 시뮬레이션이나 실시간 시스템을 가능하게 합니다.

---

### 🏢 실무 사례

#### Segment Tree 활용

- **주식 거래 시스템**: 특정 시간 범위의 주가 최대/최소/합계를 실시간 업데이트하며 조회.
- **로그 분석 서버**: 특정 시간대(Interval)의 트래픽 급증 구간을 $O(\log N)$에 탐색.
- **게임 엔진**: 특정 영역 내 유닛들의 체력 합계 계산 또는 충돌 범위 관리.
- **광고 플랫폼**: 시간대별 예산 집행 현황을 업데이트하며 남은 예산 구간 조회.
- **데이터베이스 인덱스**: 범위 검색(Range Search)을 지원하는 고급 인덱싱 구조.

---

## 🏗️ 트리 구조와 메모리

- **루트 노드**: 전체 구간 $[0, n-1]$의 정보.
- **리프 노드**: 배열의 개별 요리 정보.
- **중간 노드**: 자식 노드들의 정보를 합친 구간 정보 ($[L, mid]$, $[mid+1, R]$).
- **메모리**: 보통 $4 \times N$ 크기의 리스트를 사용합니다.

---

## 🛠️ 핵심 구현 (구간 합 예시)

```python
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self._build(data, 1, 0, self.n - 1)

    def _build(self, data, node, start, end):
        # 1. 리프 노드에 도달함
        if start == end:
            self.tree[node] = data[start]
            return
        
        # 2. 자식들로 쪼갬
        mid = (start + end) // 2
        self._build(data, 2 * node, start, mid)
        self._build(data, 2 * node + 1, mid + 1, end)
        
        # 3. 올라올 때 합침 (Conquer)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node, start, end, left, right):
        # 1. 구간이 아예 안 겹침
        if left > end or right < start:
            return 0
        
        # 2. 쿼리 범위가 노드 범위를 완전히 포함함
        if left <= start and end <= right:
            return self.tree[node]
        
        # 3. 걸쳐 있음 -> 양쪽 다 탐색
        mid = (start + end) // 2
        lsum = self.query(2 * node, start, mid, left, right)
        rsum = self.query(2 * node + 1, mid + 1, end, left, right)
        return lsum + rsum

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
            
        # 자식 값이 바뀌었으니 부모도 갱신
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
```

---

## 🚨 흔한 실수 (Common Mistakes)

1. **배열 크기 오판** ❌
   - 트리 배열의 크기가 $2^k$ 꼴로 딱 떨어지지 않는 경우, 안전하게 $4 \times N$을 할당해야 합니다. (혹은 $2^{\lceil \log_2 N \rceil + 1}$)
2. **인덱스 처리 (1-based vs 0-based)**
   - 트리의 노드 번호는 보통 계산 편의상 1번(루트)부터 시작합니다. 배열 인덱스(0-based)와 헷갈리지 않도록 주의하세요.
3. **업데이트 누락**
   - 리프 노드만 바꾸고 부모 노드들을 다시 합치지 않으면 $O(1)$ 조회가 아닌 오답 조회가 됩니다.
4. **Prefix Sum과의 혼동** ❌
   - 데이터가 변하지 않는 정적 배열이라면 Prefix Sum이 메모리 공간($O(N)$)과 속도 면에서 훨씬 유리합니다. 데이터 변화가 있을 때만 세그먼트 트리를 꺼내세요.

---

## ⚡ 펜윅 트리 (Fenwick Tree / Binary Indexed Tree)

세그먼트 트리보다 구현이 훨씬 간결하고 메모리 사용량이 적은 자료구조입니다. 주로 **누적 합(Prefix Sum)의 동적 업데이트**가 필요할 때 사용됩니다.

펜윅 트리의 원리, 구현 방법, 그리고 세그먼트 트리와의 자세한 비교는 별도 문서로 분리되어 있습니다.

- **[Fenwick Tree (Binary Indexed Tree)](fenwick-tree.md)** - 펜윅 트리의 원리, 간결한 구현, 세그먼트 트리와의 비교

---

## ⚡ 심화: 느리게 갱신되는 세그먼트 트리 (Lazy Propagation)

범위$[L, R]$ 전체에 특정 값을 더해야 할 때, 모든 리프를 일일이 업데이트($O(N \log N)$)하는 대신, "나중에 자식 갈 때 해주자"고 메모해두는 방식입니다. 이를 통해 **구간 업데이트도 $O(\log N)$** 만에 끝낼 수 있습니다.

---

### 📚 연결 문서

- [누적 합](../03_patterns/prefix-sum.md) - 정적 데이터의 구간 합 최강자
- [복잡도](../00_fundamentals/complexity-and-big-o.md) - $O(N)$ 조회를 $O(\log N)$으로 줄이는 위력
- [분할 정복](../02_algorithms/divide-and-conquer.md) - 트리를 쪼개고 합치는 근본 패러다임
- [트리](tree-and-graph.md) - 세그먼트 트리의 물리적 구조
