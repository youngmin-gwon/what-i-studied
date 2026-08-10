---
title: monotonic-queue
tags: [algorithm, data-structures, queue, monotonic-queue, sliding-window]
aliases: [Monotonic Queue, 단조 큐]
date modified: 2026-08-10 00:00:00 +09:00
date created: 2026-08-10 00:00:00 +09:00
---

## Monotonic Queue (단조 큐)

**목적**: Sliding Window에서 **최댓값/최솟값을 O(1)로 유지**

---

## 핵심 패턴: Sliding Window Maximum (최고난이도!)

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

---

## 핵심 인사이트

- Deque 맨 앞 = 현재 윈도우의 최댓값 인덱스
- 새 값이 들어올 때 그보다 작은 값들은 **절대 답이 될 수 없음** → 제거
- 시간 복잡도: O(n) (각 원소는 최대 1번 삽입, 1번 삭제)

---

## 🚨 흔한 실수

1. **윈도우 범위 체크 누락**
   ```python
   if i >= k - 1:  # ✅ 반드시 체크
       result.append(nums[dq[0]])
   ```

2. **윈도우 벗어난 인덱스 제거 순서**
   - 새로운 값 처리 전에 먼저 윈도우 범위를 벗어난 인덱스를 제거해야 합니다.

3. **Monotonic 조건 혼동**
   - Sliding Window Maximum은 **Decreasing** 순서를 유지합니다.
   - 최솟값을 구할 땐 **Increasing** 순서를 유지합니다.

---

## 📚 관련 문서

- [특수 큐](specialized-queues.md) - Monotonic Stack, Monotonic Queue 개요
- [Deque](deque.md) - Deque 구조 및 기본 연산
- [Monotonic Stack](monotonic-stack.md) - Monotonic Stack의 패턴
- [Sliding Window](../03_patterns/sliding-window.md) - 슬라이딩 윈도우 기법
- [복잡도 분석](../00_fundamentals/complexity-and-big-o.md) - 분할 상환 분석 (Amortized O(1))
