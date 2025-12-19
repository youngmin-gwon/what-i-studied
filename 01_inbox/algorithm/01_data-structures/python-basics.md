---
title: python-basics
tags: [algorithm, data-structures, python, cheatsheet]
aliases: [파이썬 기초 자료구조, 파이썬 문법 정리]
date modified: 2025-12-19 15:15:00 +09:00
date created: 2025-12-19 15:15:00 +09:00
---

## 🐍 Python 기초 자료구조 가이드

이 문서는 코딩테스트에 필요한 수준까지 Python 의 주요 자료구조를 정리한 가이드입니다. 이론적인 깊이보다는 **실전 문법과 시간 복잡도**에 집중합니다.

> [!TIP] **공부 팁**
> 여기의 내용은 억지로 외우려 하지 마시고, 문제를 풀 때마다 필요한 부분을 참고하며 익히는 것을 추천드립니다. 시간 복잡도가 잘 이해되지 않는다면 [복잡도와 Big-O](../00_fundamentals/complexity-and-big-o.md) 문서를 먼저 읽어보세요.

---

## 1. 배열 (List)

Python 에서 배열은 `list`를 사용합니다. 동적 배열로 구현되어 있어 크기가 자동으로 조절됩니다.

### 💻 주요 연산 코드
```python
# 리스트 선언
lst = [100, 200]

# 맨 뒤에 원소 삽입
lst.append(10)
lst.append(20)
lst.append(30)

# 원소 삭제
deleted_value = lst.pop(2) # 인덱스 2의 원소 삭제 및 반환
deleted_last = lst.pop()    # 맨 뒤의 원소 삭제

# 특정 위치의 원소 접근
print(lst[1])

# 특정 값의 존재 여부 확인
print(20 in lst)
```

### ⏱️ 시간 복잡도 요약
| 연산 | 코드 | 시간 복잡도 | 비고 |
| :--- | :--- | :--- | :--- |
| **맨 뒤 삽입** | `lst.append(x)` | $O(1)$ | |
| **특정 인덱스 삭제** | `lst.pop(i)` | $O(n)$ | 뒤의 원소들을 당겨야 함 |
| **맨 뒤 삭제** | `lst.pop()` | $O(1)$ | 리스트 끝만 건드림 |
| **인덱스 접근** | `lst[i]` | $O(1)$ | 임의 접근(Random Access) 가능 |
| **값 존재 확인** | `x in lst` | $O(n)$ | 전체 순회 필요 |
| **크기 확인** | `len(lst)` | $O(1)$ | |

---

## 2. 문자열 (String)

Python 의 문자열은 **불변(Immutable)** 자료형입니다. 한 번 생성하면 인덱스로 값을 바꿀 수 없습니다.

### 💻 주요 연산 코드
```python
s = "abcdef"

# 문자열 연결
s1, s2 = "Hello", "World"
s3 = s1 + s2

# 문자열 자르기 (Slicing)
print(s[2:5]) # 인덱스 2~4까지

# 특정 문자열 포함 여부 확인
print("abc" in "PPabcPPP")
```

### ⏱️ 시간 복잡도 요약
| 연산 | 코드 | 시간 복잡도 | 비고 |
| :--- | :--- | :--- | :--- |
| **연결** | `s1 + s2` | $O(len(s1) + len(s2))$ | 새로운 문자열 생성 |
| **인덱스 접근** | `s[i]` | $O(1)$ | |
| **슬라이싱** | `s[i:j]` | $O(k)$ | $k$ 는 추출된 길이 |
| **포함 여부 확인** | `substring in s` | $O(len(s))$ | |

---

## 3. 해시 테이블 (Dictionary)

Key 와 Value 를 쌍으로 저장하는 자료구조입니다.

### 💻 주요 연산 코드
```python
dt = {}
dt["apple"] = 500  # 할당
del dt["apple"]    # 삭제

print("banana" in dt) # 키 존재 확인
```

### ⏱️ 시간 복잡도 요약
| 연산 | 코드 | 시간 복잡도 | 비고 |
| :--- | :--- | :--- | :--- |
| **할당/조회/삭제** | `dt[key]` | $O(1)$* | 평균적인 경우 |
| **키 확인** | `key in dt` | $O(1)$* | |
| **크기 확인** | `len(dt)` | $O(1)$ | |

*\* 해시 충돌이 극단적으로 많은 경우 $O(n)$ 까지 떨어질 수 있으나, 일반적으론 $O(1)$ 로 간주합니다.*

---

## 4. 셋 (Set)

중복되지 않는 요소들의 모임입니다. 해시 테이블 기반으로 구현되어 조회가 매우 빠릅니다.

### 💻 주요 연산 코드
```python
s1 = {10, 20, 30}
s2 = {30, 40, 50}

s1.add(40)     # 추가
s1.remove(20)  # 삭제

# 집합 연산
union = s1 | s2        # 합집합
intersection = s1 & s2 # 교집합
difference = s1 - s2   # 차집합
```

### ⏱️ 시간 복잡도 요약
| 연산 | 코드 | 시간 복잡도 | 비고 |
| :--- | :--- | :--- | :--- |
| **추가/삭제/조회** | `s.add()`, `in` | $O(1)$ | |
| **합집합** | `s1 \| s2` | $O(len(s1) + len(s2))$ | |
| **교/차집합** | `s1 & s2`, `-` | $O(min(len(s1), len(s2)))$ | 효율적인 쪽 기준 |

---

## 5. 스택 (Stack)

후입선출(LIFO) 원칙을 따릅니다. Python 에서는 `collections.deque`를 사용하는 것이 효율적입니다.

### 💻 주요 연산 코드
```python
from collections import deque
st = deque()

st.append(10) # Push
st.pop()      # Pop
st[-1]        # Peek (맨 위 확인)

if not st:    # 비어있는지 확인
    print("Empty")
```

### ⏱️ 시간 복잡도 요약
| 연산 | 코드 | 시간 복잡도 |
| :--- | :--- | :--- |
| **Push** | `append()` | $O(1)$ |
| **Pop** | `pop()` | $O(1)$ |
| **Peek** | `st[-1]` | $O(1)$ |

---

## 6. 큐 (Queue)

선입선출(FIFO) 원칙을 따릅니다. 반드시 `collections.deque`의 `popleft()`를 사용해야 성능이 보장됩니다.

### 💻 주요 연산 코드
```python
from collections import deque
q = deque()

q.append(10)    # Enqueue
q.popleft()     # Dequeue

q[0]            # Front (맨 앞 확인)
```

### ⏱️ 시간 복잡도 요약
| 연산 | 코드 | 시간 복잡도 | 비고 |
| :--- | :--- | :--- | :--- |
| **Enqueue** | `append()` | $O(1)$ | |
| **Dequeue** | `popleft()` | $O(1)$ | `list.pop(0)`은 $O(n)$ 이므로 주의! |
| **값 존재 확인** | `x in q` | $O(n)$ | 전체 순회 |

---

## 7. 힙 (Heap / Priority Queue)

우선순위가 가장 높은 원소를 빠르게 꺼낼 수 있는 자료구조입니다.

### 💻 주요 연산 코드
`PriorityQueue` 클래스는 내부적으로 힙을 사용하며, 멀티스레드 환경을 지원하기 위해 다소의 오버헤드가 있습니다. 문제 풀이에서는 `heapq` 모듈을 더 자주 사용합니다.

```python
from queue import PriorityQueue
pq = PriorityQueue()

# 최소 힙 (Min Heap) 기본
pq.put(10)
val = pq.get() # 삭제 및 반환

# 최대 힙 (Max Heap) 트릭
pq.put((-value, value)) # 우선순위를 음수로
actual_val = pq.get()[1]
```

### ⏱️ 시간 복잡도 요약
| 연산 | 코드 | 시간 복잡도 |
| :--- | :--- | :--- |
| **삽입** | `pq.put()` | $O(\log n)$ |
| **삭제** | `pq.get()` | $O(\log n)$ |
| **조회 (최상단)** | `pq.queue[0]` | $O(1)$ |

---

## 📚 연결 문서
- [선형 자료구조](linear.md) - Array 와 Linked List 의 물리적 차이
- [해시 테이블](hash-and-map.md) - 해시 함수와 충돌 해결 원리
- [스택과 큐](stack-and-queue.md) - LIFO, FIFO 의 상세 개념
- [힙과 우선순위 큐](heap-and-priority-queue.md) - Heapify 와 완전 이진 트리의 구조
