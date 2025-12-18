---
title: search-and-sort
tags: [algorithm, binary-search, merge-sort, pattern, quick-sort, search, sort]
aliases: [병합 정렬, 이진 탐색, 정렬 알고리즘, 퀵 정렬]
date modified: 2025-12-18 11:42:13 +09:00
date created: 2025-12-17 19:40:00 +09:00
---

## Search & Sort: 정보 검색의 기술

데이터를 저장하는 이유는 나중에 **찾기 (Search)** 위해서입니다. 그리고 빠르게 찾으려면 **정렬 (Sort)**되어 있어야 합니다.

### 🔍 Binary Search (이진 탐색)

"업다운 게임"과 원리가 같습니다. 숫자가 정렬되어 있다면, 중간값 (Mid) 을 보고 범위를 절반씩 줄여나갈 수 있습니다.

- **복잡도**: **O(log n)**. 40 억 개의 데이터도 32 번 (`log2(40억)`) 비교면 찾습니다. 기적적인 속도입니다.
- **조건**: 데이터가 반드시 **정렬**되어 있어야 합니다.

#### 🔧 구현 (iterative)
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # 오버플로우 방지
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

### 🌪️ Sorting Algorithms

세상에 "가장 좋은" 정렬 알고리즘은 없습니다. 상황에 따라 다릅니다.

#### 1. Quick Sort (퀵 정렬)
- **전략**: Pivot 을 잡고 좌우로 나눕니다 (분할 정복).
- **특징**: 평균적으로 가장 빠릅니다. 메모리가 **연속적**이라 Cache Hit 율이 높고, 추가 메모리를 거의 안 씁니다.
- **구현**:
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

#### 2. Merge Sort (병합 정렬)
- **전략**: 반으로 쪼개고 나중에 합칩니다.
- **특징**: 항상 **O(n log n)**을 보장합니다. **Stable**합니다 (순서 보존).
- **구현**:
```python
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result
```

#### 3. Timsort (현실의 승자)
Python, Java, Swift(`sort()`) 의 기본 정렬입니다. **Insertion Sort**와 **Merge Sort**를 섞어 현실 데이터에서 최강의 성능을 냅니다.

---

### 🚨 흔한 실수 (Common Mistakes)

1. **이진 탐색 시 정렬 누락** ❌
   - 가장 빈번한 실수입니다. 이진 탐색 전에는 반드시 데이터가 정렬되어 있는지 확인하세요.
2. **무한 루프 (Binary Search)**
   - `left = mid` 또는 `right = mid`로 설정할 경우, `left`와 `right`가 인접했을 때 루프를 빠져나오지 못할 수 있습니다. `mid + 1`, `mid - 1`을 사용하거나 탈출 조건을 명확히 하세요.
3. **Mid 계산 오버플로우**
   - 앞서 언급한 대로 `(left + right) // 2`는 범위를 벗어날 수 있습니다. `left + (right - left) // 2` 습관을 들이세요.
4. **Stable vs Unstable 정렬의 오용**
   - 데이터에 여러 기준이 있을 때(예: 성적순 정렬 후 이름순 정렬), Unstable한 Quick Sort를 쓰면 이전의 정렬 결과가 망가질 수 있습니다.

---

### 🏢 실무 사례
- **Database Indexing**: B-Tree 내부에서 이진 탐색을 기반으로 데이터 조회
- **Git Bisect**: 버그가 발생한 커밋을 찾기 위해 히스토리를 이진 탐색
- **E-commerce Search**: 가격순, 인기순 정렬 시 내부적으로 Timsort 또는 Quick Sort 변형 사용
- **Excel/Spreadsheet**: 대량의 레코드 정렬

---

### 📚 연결 문서
- [[00_fundamentals/complexity-and-big-o|정렬 복잡도 비교]]
- [[01_data-structures/linear|Array 가 Quick Sort 에 유리한 이유]]
- [[01_data-structures/tree-and-graph|이진 탐색 트리와의 관계]]
