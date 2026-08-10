---
title: fenwick-tree
tags: [data-structure, tree, fenwick-tree, binary-indexed-tree, range-query, optimization]
aliases: [펜윅 트리, 이진 인덱스 트리, Binary Indexed Tree, BIT, Fenwick Tree]
date modified: 2026-08-10 00:00:00 +09:00
date created: 2026-08-10 00:00:00 +09:00
---

## Fenwick Tree (Binary Indexed Tree)

세그먼트 트리보다 구현이 훨씬 간결하고 메모리 사용량이 적은($O(N)$) 자료구조입니다. 주로 **누적 합(Prefix Sum)의 동적 업데이트**가 필요할 때 사용됩니다.

### 💡 핵심 원리: "비트의 끝자리 1을 활용"

`i & -i` 연산을 통해 가장 낮은 자리의 비트(LSB)를 구하고, 이를 이용해 트리를 탐색합니다.

---

## 🔧 구현 (구간 합)

```python
class FenwickTree:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, i, delta):
        # i번째 값을 delta만큼 증가시킴
        while i < len(self.tree):
            self.tree[i] += delta
            i += (i & -i)

    def query(self, i):
        # 1부터 i까지의 합 구하기
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= (i & -i)
        return s

# 구간 [L, R] 합: query(R) - query(L-1)
```

---

## ⚔️ Segment Tree와의 비교

| 특징 | Segment Tree | Fenwick Tree |
|:---|:---|:---|
| **메모리** | $4N$ | $N$ |
| **구현 난이도** | 높음 (재귀/복잡) | 매우 낮음 (간결) |
| **유연성** | 최댓값, 최솟값 등 자유로움 | 주로 누적 합(구간 합)에 특화 |
| **속도** | 약간 더 무거움 | 매우 빠름 |

---

## 📚 관련 문서

- [Segment Tree](segment-tree.md) - 구간 쿼리를 위한 보다 유연한 자료구조
- [누적 합](../03_patterns/prefix-sum.md) - 정적 데이터의 구간 합 최강자
- [복잡도](../00_fundamentals/complexity-and-big-o.md) - $O(N)$ 조회를 $O(\log N)$으로 줄이는 위력
