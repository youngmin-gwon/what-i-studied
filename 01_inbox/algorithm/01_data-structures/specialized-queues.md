---
title: algo-ds-specialized-queues
tags: [algorithm, data-structures, deque, monotonic-queue, monotonic-stack, sliding-window]
aliases: [Deque, Monotonic Stack, Monotonic Queue, 덱, 단조 스택, 단조 큐]
date modified: 2025-12-18 11:28:51 +09:00
date created: 2025-12-18 11:28:51 +09:00
---

## Deque & Monotonic Structures: 특수 용도 큐/스택

일반 Stack/Queue로는 해결하기 어려운 문제를 위한 **특수화된 자료구조** 입니다.

### 🔄 Deque (Double-Ended Queue)

Deque는 **양쪽 끝**에서 삽입/삭제가 모두 O(1)인 자료구조입니다.

**일반 Queue와의 차이**:
- Queue: 뒤에서 넣고(enqueue) 앞에서 뺌(dequeue)
- Deque: **양쪽 모두** 가능 (앞/뒤 삽입, 앞/뒤 삭제)

#### 구조

```plaintext
    [front]  ←→  [back]
      ↓           ↓
    +---+---+---+---+
    | 3 | 7 | 2 | 9 |
    +---+---+---+---+
      ↑           ↑
  append_left  append_right
  pop_left     pop_right
```

**핵심 연산** (모두 O(1)):
- `append_left(x)`: 왼쪽에 추가
- `append_right(x)`: 오른쪽에 추가
- `pop_left()`: 왼쪽에서 제거
- `pop_right()`: 오른쪽에서 제거

---

### 🔧 구현

#### Python (collections.deque)

```python
from collections import deque

dq = deque([1, 2, 3])

# 양쪽 추가
dq.appendleft(0)   # [0, 1, 2, 3]
dq.append(4)       # [0, 1, 2, 3, 4]

# 양쪽 제거
dq.popleft()       # 0 제거 → [1, 2, 3, 4]
dq.pop()           # 4 제거 → [1, 2, 3]

# 인덱스 접근도 가능 (하지만 O(n))
dq[0]  # 1
```

#### Swift (직접 구현)

```swift
struct Deque<T> {
    private var array: [T] = []
    private var head = 0
    
    mutating func appendLeft(_ element: T) {
        if head > 0 {
            head -= 1
            array[head] = element
        } else {
            array.insert(element, at: 0)
        }
    }
    
    mutating func append(_ element: T) {
        array.append(element)
    }
    
    mutating func popLeft() -> T? {
        guard head < array.count else { return nil }
        let element = array[head]
        head += 1
        
        // 주기적으로 메모리 정리
        if head > array.count / 2 {
            array.removeFirst(head)
            head = 0
        }
        
        return element
    }
    
    mutating func popRight() -> T? {
        return array.popLast()
    }
}
```

---

### 🎯 Deque 실전 패턴

#### Pattern 1: Sliding Window (K개씩 묶어서 보기)

"배열에서 K개씩 윈도우를 이동하며 처리"

```python
def process_sliding_window(arr, k):
    """K개씩 묶어서 처리"""
    dq = deque()
    result = []
    
    for i, num in enumerate(arr):
        # 윈도우에 추가
        dq.append(num)
        
        # 윈도우 크기가 K가 되면
        if i >= k - 1:
            # 윈도우 내 처리 (예: 합계)
            result.append(sum(dq))
            
            # 가장 오래된 요소 제거
            dq.popleft()
    
    return result

# [1, 2, 3, 4, 5], k=3
# → [6, 9, 12]  ([1,2,3], [2,3,4], [3,4,5]의 합)
```

#### Pattern 2: 회문 판별 (Palindrome Check)

```python
def is_palindrome(s):
    dq = deque(s.lower())
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    
    return True

# "racecar" → True
# "hello" → False
```

---

### 📈 Monotonic Stack (단조 스택)

**정의**: 스택 내부가 **항상 증가** 또는 **항상 감소** 순서를 유지하는 스택

**핵심 아이디어**: 새 원소가 들어올 때, 조건을 위반하는 원소들을 **미리 제거**

#### 작동 방식 (Monotonic Increasing)

```python
# 입력: [3, 1, 4, 2]
stack = []

for num in [3, 1, 4, 2]:
    # 스택이 증가 순서 유지하도록
    while stack and stack[-1] > num:
        stack.pop()  # 조건 위반 제거
    stack.append(num)

# 과정:
# 3 추가 → [3]
# 1 추가: 3 제거 → [1]
# 4 추가 → [1, 4]
# 2 추가: 4 제거 → [1, 2]
```

---

### 🎯 Monotonic Stack 실전 패턴

#### Pattern 1: Next Greater Element (핵심!)

"각 원소의 오른쪽에서 처음으로 나타나는 더 큰 값 찾기"

```python
def next_greater_element(nums):
    result = [-1] * len(nums)
    stack = []  # (인덱스, 값) 저장
    
    for i, num in enumerate(nums):
        # 현재 값보다 작은 애들의 답 = 현재 값
        while stack and stack[-1][1] < num:
            idx, _ = stack.pop()
            result[idx] = num
        
        stack.append((i, num))
    
    return result

# [2, 1, 2, 4, 3]
# → [4, 2, 4, -1, -1]
#    ↑  ↑  ↑
#    2의 다음 큰 값은 4
#    1의 다음 큰 값은 2
#    2의 다음 큰 값은 4
```

**시간 복잡도**: O(n) (각 원소는 최대 1번 push, 1번 pop)

**응용**:
- 주식 가격 변동 분석
- 히스토그램 최대 넓이
- 괄호 매칭

#### Pattern 2: 히스토그램 최대 직사각형

```python
def largest_rectangle_area(heights):
    stack = []  # (인덱스) 저장 - Monotonic Increasing
    max_area = 0
    
    for i, h in enumerate(heights):
        # 현재 높이보다 높은 막대 처리
        while stack and heights[stack[-1]] > h:
            height_idx = stack.pop()
            height = heights[height_idx]
            # 왼쪽 경계 = 스택의 다음 원소, 오른쪽 경계 = 현재
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        stack.append(i)
    
    # 남은 막대 처리
    while stack:
        height_idx = stack.pop()
        height = heights[height_idx]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)
    
    return max_area

# [2, 1, 5, 6, 2, 3]
# → 10 (높이 5, 6의 넓이 = 2 × 5)
```

#### Pattern 3: Daily Temperatures

"오늘보다 더운 날이 며칠 후에 오는지"

```python
def daily_temperatures(temps):
    result = [0] * len(temps)
    stack = []  # Monotonic Decreasing (온도 감소)
    
    for i, temp in enumerate(temps):
        # 현재 온도보다 낮은 날들의 답 계산
        while stack and temps[stack[-1]] < temp:
            prev_idx = stack.pop()
            result[prev_idx] = i - prev_idx  # 날짜 차이
        
        stack.append(i)
    
    return result

# [73, 74, 75, 71, 69, 72, 76, 73]
# → [1, 1, 4, 2, 1, 1, 0, 0]
#    ↑  ↑
#   73 다음 더운 날은 1일 후(74)
#   74 다음 더운 날은 1일 후(75)
```

---

### 📊 Monotonic Queue (단조 큐)

**목적**: Sliding Window에서 **최댓값/최솟값을 O(1)로 유지**

#### Pattern: Sliding Window Maximum (최고난이도!)

"크기 K 윈도우를 이동하며 각 윈도우의 최댓값 찾기"

```python
def max_sliding_window(nums, k):
    from collections import deque
    
    dq = deque()  # 인덱스 저장 (값은 감소 순서 유지)
    result = []
    
    for i, num in enumerate(nums):
        # 1. 윈도우 벗어난 인덱스 제거
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # 2. 현재 값보다 작은 값들 제거 (Monotonic Decreasing)
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        # 3. 현재 인덱스 추가
        dq.append(i)
        
        # 4. 윈도우가 완성되면 최댓값 (맨 앞) 기록
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# [1, 3, -1, -3, 5, 3, 6, 7], k=3
# → [3, 3, 5, 5, 6, 7]
```

**핵심 인사이트**:
- Deque 맨 앞 = 현재 윈도우의 최댓값 인덱스
- 새 값이 들어올 때 그보다 작은 값들은 **절대 답이 될 수 없음** → 제거
- 시간 복잡도: O(n) (각 원소는 최대 1번 삽입, 1번 삭제)

---

### 🧪 심화: Monotonic Stack의 변형

#### 양방향 Next Greater (왼쪽/오른쪽)

```python
def next_and_prev_greater(nums):
    n = len(nums)
    next_greater = [-1] * n
    prev_greater = [-1] * n
    
    # 오른쪽 스캔
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            next_greater[stack.pop()] = i
        stack.append(i)
    
    # 왼쪽 스캔
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and nums[stack[-1]] < nums[i]:
            prev_greater[stack.pop()] = i
        stack.append(i)
    
    return next_greater, prev_greater
```

---

### ⚡ 언어별 팁

```python
# Python - collections.deque가 최고
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)  # O(1)
dq.popleft()      # O(1)
```

```swift
// Swift - 직접 구현 필요
// Array의 insert(at: 0)는 O(n)이므로 주의
// head 인덱스를 사용한 최적화 필요
```

---

### 🚨 흔한 실수

1. **Deque를 Array로 대체** ❌
   ```python
   arr.insert(0, x)  # O(n) - 느림!
   deque.appendleft(x)  # O(1) - 빠름!
   ```

2. **Monotonic Stack에서 값 대신 인덱스 저장 안 함** ❌
   - 인덱스를 저장해야 거리/위치 계산 가능

3. **윈도우 범위 체크 누락**
   ```python
   # Sliding Window에서
   if i >= k - 1:  # ✅ 반드시 체크
       result.append(...)
   ```

4. **Monotonic 조건 헷갈림**
   - **Increasing**: 더 작은 값 제거 (작은 값은 답이 안 됨)
   - **Decreasing**: 더 큰 값 제거 (큰 값은 답이 안 됨)

---

### 🎓 핵심 정리

| 자료구조 | 핵심 용도 | 시간 복잡도 | 대표 문제 |
|:---|:---|:---|:---|
| **Deque** | 양방향 삽입/삭제 | O(1) | Sliding Window, Palindrome |
| **Monotonic Stack** | Next Greater/Smaller | O(n) | 히스토그램, 온도 변화 |
| **Monotonic Queue** | Sliding Max/Min | O(n) | Sliding Window Maximum |

> [!TIP] **언제 쓰나?**
> - **"다음으로 큰/작은 값"** → Monotonic Stack
> - **"윈도우 최댓값/최솟값"** → Monotonic Queue
> - **"양쪽에서 처리"** → Deque

---

#### 📚 연결 문서
- [[algo-ds-linear]] - Stack, Queue 기초
- [[algo-pattern-two-pointers]] - Sliding Window 기법
- [[algo-complexity-and-big-o]] - 분할 상환 분석 (Amortized O(1))
