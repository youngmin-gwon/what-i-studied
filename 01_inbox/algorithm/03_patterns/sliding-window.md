---
title: sliding-window
tags: [algorithm, array, pattern, sliding-window, optimization]
aliases: [슬라이딩 윈도우, Sliding Window]
date modified: 2026-08-10 00:00:00 +09:00
date created: 2026-08-10 00:00:00 +09:00
---

## Sliding Window (창문 밀기)

연속된 구간(Subarray)을 처리할 때, 창문을 오른쪽으로 밀어가며 **새로 들어오는 값**과 **나가는 값**만 갱신합니다.

### 💡 Why it matters (Context)

- **데이터 스트리밍**: 실시간으로 흘러들어오는 데이터의 최근 1시간 평균 구하기.
- **효율성**: 2중 루프의 $O(n^2)$을 $O(n)$으로 최적화.
- **가변 길이 구간**: 합이 S 이상인 가장 짧은 연속 부분 배열 찾기.

---

### 🏢 실무 사례

- **네트워크 (TCP)**: 패킷 흐름 제어 (Sliding Window Protocol).
- **영상 알고리즘**: 프레임 내 윈도우 이동을 통한 객체 탐지.
- **로그 분석**: 대량의 로그 중 특정 패턴이 나타나는 연속 구간 탐색.
- **스트리밍 대시보드**: "최근 5분간의 에러율" 실시간 계산.

---

## 1. 고정 길이 윈도우 (Fixed Size)

```python
def fixed_sliding_window(arr, k):
    # 첫 k개 합 구하기
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    for i in range(k, len(arr)):
        # 나가는 놈(arr[i-k]) 빼고, 들어오는 놈(arr[i]) 더하기
        current_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, current_sum)
    return max_sum
```

---

## 2. 가변 길이 윈도우 (Variable Size)

"합이 S 이상인 가장 짧은 구간의 길이 구하기"

```python
def min_subarray_len(target, nums):
    left = 0
    current_sum = 0
    min_len = float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        # 조건을 만족하는 동안 왼쪽 포인터를 당김
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
            
    return min_len if min_len != float('inf') else 0
```

---

## 🚨 흔한 실수 (Common Mistakes)

1. **정렬 여부 확인 망각** ❌
   - 슬라이딩 윈도우는 배열 정렬 여부와 무관하게 동작합니다.
   
2. **인덱스 범위 에러 (Off-by-one)**
   - 가변 길이 윈도우에서 `left` 포인터 위치 및 구간 길이 계산 주의.
   
3. **윈도우 갱신 순서**
   - 가변 길이 윈도우에서 `left`를 옮기기 전/후에 값을 뺄 때 인덱스 주의.
   
4. **무한 루프**
   - `left`나 `right`가 특정 조건에서 멈추어 루프가 끝나지 않는 경우.

---

## ⚔️ Two Pointers vs Sliding Window

| 특징 | Two Pointers | Sliding Window |
|:---|:---|:---|
| **배열 상태** | 보통 정렬됨 | 정렬 안 되어도 무관 |
| **관심 영역** | 두 지점의 **값** (쌍) | 두 지점 사이의 **구간** |
| **포인터 방향** | 양 끝에서 안으로 (보통) | 같은 방향으로 (Slide) |

---

## 📚 관련 문서

- [Two Pointers](two-pointers.md) - 양 끝에서 조이는 투 포인터 전략
- [복잡도 분석](../00_fundamentals/complexity-and-big-o.md) - 2중 루프($O(N^2)$)를 선형 시간($O(N)$)으로 단축하는 원리
- [배열과 리스트](../01_data-structures/linear.md) - 연속 공간 포인터 이동을 통한 효율적 데이터 접근
- [누적 합](prefix-sum.md) - 고정 구간 합 조회를 위한 또 다른 최적화 도구
- [특수 큐](../01_data-structures/specialized-queues.md) - 슬라이딩 윈도우에서의 최댓값/최솟값 추적 최적화
- [검색과 정렬](../02_algorithms/search-and-sort.md) - 정렬된 상태를 요구하는 투 포인터 전략의 기초
