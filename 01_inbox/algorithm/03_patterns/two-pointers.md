---
title: two-pointers
tags: [algorithm, array, pattern, sliding-window, two-pointers]
aliases: [슬라이딩 윈도우, 투 포인터, Two Pointers, Sliding Window]
date modified: 2025-12-18 11:53:38 +09:00
date created: 2025-12-17 20:00:00 +09:00
---

## Two Pointers & Sliding Window: O(n²)을 O(n)으로

배열에서 "구간"이나 "쌍 (Pair)"을 구할 때, 단순하게 2중 루프를 돌리면 $O(n^2)$이 걸립니다. 하지만 포인터 두 개를 영리하게 움직이면 **$O(n)$**으로 최적화할 수 있습니다.

### 💡 Why it matters (Context)

- **데이터 스트리밍**: 실시간으로 흘러들어오는 데이터의 최근 1시간 평균 구하기.
- **메모리 최적화**: 정렬된 거대 데이터에서 특정 조건을 만족하는 쌍 찾기.
- **가변 길이 구간**: 합이 S 이상인 가장 짧은 연속 부분 배열 찾기.

---

### 🏢 실무 사례

#### Sliding Window 활용
- **네트워크 (TCP)**: 패킷 흐름 제어 (Sliding Window Protocol).
- **영상 알고리즘**: 프레임 내 윈도우 이동을 통한 객체 탐지.
- **로그 분석**: 대량의 로그 중 특정 패턴이 나타나는 연속 구간 탐색.
- **스트리밍 대시보드**: "최근 5분간의 에러율" 실시간 계산.

#### Two Pointers 활용
- **데이터 정제**: 정렬된 로그에서 중복 항목 제거.
- **압축 알고리즘**: 유사한 데이터 구간을 찾아 압축 최적화.
- **검색 엔진**: 두 문자의 거리 차이가 최소인 문서 위치 찾기.

---

## 👈👉 Two Pointers (양쪽에서 조이기)

주로 **정렬된 배열**에서 두 노드를 양 끝이나 같은 방향에서 출발시켜 조건을 만족하는 쌍을 찾습니다.

### 🔧 구현: Two Sum (Sorted)
```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # 합을 키워야 함
        else:
            right -= 1 # 합을 줄여야 함
    return []
```

---

## 🪟 Sliding Window (창문 밀기)

연속된 구간(Subarray)을 처리할 때, 창문을 오른쪽으로 밀어가며 **새로 들어오는 값**과 **나가는 값**만 갱신합니다.

### 1. 고정 길이 윈도우 (Fixed Size)
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

### 2. 가변 길이 윈도우 (Variable Size)
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
   - 양방향 투 포인터(`left`, `right`) 전략은 대부분 **정렬된 배열**에서만 유효합니다. 정렬되지 않았다면 정렬부터 하거나 [[01_data-structures/hash-and-map|Hash Map]]을 고려하세요.
2. **인덱스 범위 에러 (Off-by-one)**
   - `while left < right` 인지 `left <= right` 인지 상황에 따라 정확히 결정해야 합니다. (쌍을 찾을 땐 보통 `<`)
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

---

## 📚 관련 문서
- [[00_fundamentals/complexity-and-big-o|복잡도 분석]] - 2중 루프($O(N^2)$)를 선형 시간($O(N)$)으로 단축하는 원리
- [[01_data-structures/linear|배열과 리스트]] - 연속 공간 포인터 이동을 통한 효율적 데이터 접근
- [[03_patterns/prefix-sum|누적 합]] - 고정 구간 합 조회를 위한 또 다른 최적화 도구
- [[01_data-structures/specialized-queues|특수 큐]] - 슬라이딩 윈도우에서의 최댓값/최솟값 추적 최적화
- [[02_algorithms/search-and-sort|검색과 정렬]] - 정렬된 상태를 요구하는 투 포인터 전략의 기초
