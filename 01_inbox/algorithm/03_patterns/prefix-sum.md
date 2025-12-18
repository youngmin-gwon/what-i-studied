---
title: prefix-sum
tags: [algorithm, array, pattern, prefix-sum]
aliases: [누적 합, 구간 합, Prefix Sum]
date modified: 2025-12-18 11:53:38 +09:00
date created: 2025-12-18 11:53:38 +09:00
---

## Prefix Sum: 구간 합을 O(1)에 구하기

미리 합계를 계산해두어, 임의의 구간 $[i, j]$의 합을 **상수 시간**에 구하는 기법입니다.

### 💡 Why it matters (Context)

- **잦은 구간 조회**: 데이터는 가만히 있는데 구간 합 질문이 수만 번 들어올 때 ($O(N)$으로 매번 구하면 시간 초과).
- **이미지 처리**: 특정 영역의 픽셀 합 구하기 (2D Prefix Sum).
- **변화율 계산**: 시간에 따른 데이터 누적치 분석.

---

### 🏢 실무 사례

#### Prefix Sum 활용
- **이미지 필터링 (Box Blur)**: 2D 구간 합을 빠르게 계산하여 흐림 효과 적용.
- **금융 데이터**: 특정 기간 내 주가 수익률 또는 거래량 합계 실시간 조회.
- **게임 엔진**: 특정 영역 내의 유닛 개수 또는 데미지 총합 계산.
- **GIS (지리정보시스템)**: 특정 구역의 인구 밀도나 강수량 누적치 합계.

---

## 🔧 기본 원리

배열 `A`가 있을 때, 누적 합 배열 `S`를 다음과 같이 정의합니다.
- `S[i] = A[0] + A[1] + ... + A[i-1]` (보통 구현 편의상 인덱스를 한 칸 밀어 사용)

그러면 구간 $[L, R]$의 합은?
$$\text{Sum}(L, R) = S[R+1] - S[L]$$

### 💻 구현 (1D)
```python
def get_prefix_sum(arr):
    n = len(arr)
    # n+1 크기로 만들면 인덱스 처리가 매우 편함
    s = [0] * (n + 1)
    for i in range(n):
        s[i+1] = s[i] + arr[i]
    return s

# 구간 [L, R] 합 구하기 (L, R은 0-indexed)
def query_sum(s, L, R):
    return s[R+1] - s[L]

# arr = [1, 2, 3, 4, 5]
# s   = [0, 1, 3, 6, 10, 15]
# [1, 3] 합 (2+3+4) = s[4] - s[1] = 10 - 1 = 9
```

---

## 🎨 2D Prefix Sum (Summed-Area Table)

이미지 처리 등에서 사용되는 2차원 누적 합입니다.

### 💻 구현 (2D)
```python
def get_2d_prefix_sum(matrix):
    rows, cols = len(matrix), len(matrix[0])
    s = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    for r in range(rows):
        for c in range(cols):
            s[r+1][c+1] = matrix[r][c] + s[r][c+1] + s[r+1][c] - s[r][c]
            
    return s

# (r1, c1)에서 (r2, c2)까지의 직사각형 합
def query_2d_sum(s, r1, c1, r2, c2):
    return s[r2+1][c2+1] - s[r1][c2+1] - s[r2+1][c1] + s[r1][c1]
```

---

## 🚨 흔한 실수 (Common Mistakes)

1. **인덱스 미스 (Off-by-one)** ❌
   - `S[i+1]`을 만드는 이유는 `S[R+1] - S[L]` 계산 시 `L=0`일 때의 예외 처리를 피하기 위함입니다. 이를 헷갈려 `S[R] - S[L-1]` 처럼 쓰다 인덱스 에러가 날 수 있습니다.
2. **데이터 업데이트 대응**
   - Prefix Sum은 데이터가 **정적(Static)**일 때 강력합니다. 중간에 데이터가 자꾸 바뀐다면 **Segment Tree**나 **Fenwick Tree**를 써야 합니다.
3. **오버플로우**
   - 합산 값이 매우 커질 수 있으므로 자료형 범위를 확인하세요.

---

## ⚔️ Prefix Sum vs Two Pointers

| 특징 | Prefix Sum | Two Pointers |
|:---|:---|:---|
| **메모리** | $O(N)$ 추가 공간 필요 | $O(1)$ 공간 |
| **데이터 변경** | 변경 시 재계산 필요 ($O(N)$) | 비교적 유연함 |
| **목적** | 임의 구간의 **합** 조회 | 특정 **조건**을 만족하는 구간 찾기 |

---

### 📚 연결 문서
- [[03_patterns/two-pointers|투 포인터]] - 가변 구간 탐색의 대안
- [[00_fundamentals/complexity-and-big-o|복잡도]] - $O(N)$ 조회와 $O(1)$ 조회의 차이
- [[01_data-structures/linear|배열]] - 연속 공간에서의 데이터 처리
