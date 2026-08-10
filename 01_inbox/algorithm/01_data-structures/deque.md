---
title: deque
tags: [algorithm, data-structures, deque, queue]
aliases: [Deque, Double-Ended Queue, 덱]
date modified: 2026-08-10 00:00:00 +09:00
date created: 2026-08-10 00:00:00 +09:00
---

## Deque (Double-Ended Queue)

Deque는 **양쪽 끝** 에서 삽입/삭제가 모두 O(1)인 자료구조입니다.

### 일반 Queue와의 차이

- Queue: 뒤에서 넣고(enqueue) 앞에서 뺌(dequeue)
- Deque: **양쪽 모두** 가능 (앞/뒤 삽입, 앞/뒤 삭제)

---

## 구조

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

### 핵심 연산 (모두 O(1))

- `append_left(x)`: 왼쪽에 추가
- `append_right(x)`: 오른쪽에 추가
- `pop_left()`: 왼쪽에서 제거
- `pop_right()`: 오른쪽에서 제거

---

## 🔧 구현

### Python (collections.deque)

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

### Swift (직접 구현)

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

## 🎯 Deque 실전 패턴

### Pattern 1: Sliding Window (K개씩 묶어서 보기)

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

### Pattern 2: 회문 판별 (Palindrome Check)

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

## 🚨 흔한 실수

1. **Deque를 Array로 대체** ❌
   ```python
   arr.insert(0, x)  # O(n) - 느림!
   deque.appendleft(x)  # O(1) - 빠름!
   ```

2. **윈도우 범위 체크 누락**
   ```python
   # Sliding Window에서
   if i >= k - 1:  # ✅ 반드시 체크
       result.append(...)
   ```

---

## 📚 관련 문서

- [특수 큐](specialized-queues.md) - Deque, Monotonic Stack, Monotonic Queue 개요
- [Monotonic Queue](monotonic-queue.md) - Deque를 활용한 슬라이딩 윈도우 최댓값/최솟값
- [배열과 리스트](linear.md) - Stack, Queue 기초
