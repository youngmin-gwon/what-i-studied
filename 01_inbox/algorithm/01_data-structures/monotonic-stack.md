---
title: monotonic-stack
tags: [algorithm, data-structures, stack, monotonic-stack]
aliases: [Monotonic Stack, 단조 스택, 단조 증가 스택]
date modified: 2026-08-10 00:00:00 +09:00
date created: 2026-08-10 00:00:00 +09:00
---

## Monotonic Stack (단조 스택)

**정의**: 스택 내부가 **항상 증가** 또는 **항상 감소** 순서를 유지하는 스택

**핵심 아이디어**: 새 원소가 들어올 때, 조건을 위반하는 원소들을 **미리 제거**

---

## 작동 방식 (Monotonic Increasing)

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

## 🎯 Monotonic Stack 실전 패턴

### Pattern 1: Next Greater Element (핵심!)

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

---

### Pattern 2: 히스토그램 최대 직사각형

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

---

### Pattern 3: Daily Temperatures

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

## 🧪 심화: Monotonic Stack의 변형

### 양방향 Next Greater (왼쪽/오른쪽)

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

## 🚨 흔한 실수

1. **Monotonic Stack에서 값 대신 인덱스 저장 안 함** ❌
   - 인덱스를 저장해야 거리/위치 계산 가능

2. **Monotonic 조건 헷갈림**
   - **Increasing**: 더 작은 값 제거 (작은 값은 답이 안 됨)
   - **Decreasing**: 더 큰 값 제거 (큰 값은 답이 안 됨)

3. **초기 스택 처리 누락**
   - 루프 종료 후 스택에 남은 원소 처리 필요 (Pattern 2 참조)

---

## 📚 관련 문서

- [특수 큐](specialized-queues.md) - Monotonic Stack, Monotonic Queue 개요
- [배열과 리스트](linear.md) - Stack 기초
- [복잡도 분석](../00_fundamentals/complexity-and-big-o.md) - 분할 상환 분석 (Amortized O(1))
