---
title: specialized-queues
tags: [algorithm, data-structures, deque, monotonic-queue, monotonic-stack, sliding-window]
aliases: [Deque, Monotonic Queue, Monotonic Stack, 단조 스택, 단조 큐, 덱]
date modified: 2026-08-10 00:00:00 +09:00
date created: 2025-12-18 11:28:51 +09:00
---

## Deque & Monotonic Structures: 특수 용도 큐/스택

일반 Stack/Queue로는 해결하기 어려운 문제를 위한 **특수화된 자료구조** 입니다.

---

## 📚 관련 문서

각 자료구조의 자세한 설명, 구현 방법, 실전 패턴은 다음 문서들을 참조하세요:

- **[Deque (Double-Ended Queue)](deque.md)** - 양쪽 끝에서 O(1) 삽입/삭제, 슬라이딩 윈도우 기본 구조
- **[Monotonic Stack](monotonic-stack.md)** - 다음 큰/작은 값 찾기, 히스토그램, 괄호 매칭
- **[Monotonic Queue](monotonic-queue.md)** - 슬라이딩 윈도우에서 최댓값/최솟값을 O(1)로 유지

---

### 🎓 핵심 정리

| 자료구조 | 핵심 용도 | 시간 복잡도 | 대표 문제 |
|:---|:---|:---|:---|
| **Deque** | 양방향 삽입/삭제 | O(1) | Sliding Window, Palindrome |
| **Monotonic Stack** | Next Greater/Smaller | O(n) | 히스토그램, 온도 변화 |
| **Monotonic Queue** | Sliding Max/Min | O(n) | Sliding Window Maximum |

>[!TIP] **언제 쓰나?**
> - **"다음으로 큰/작은 값"** → Monotonic Stack
> - **"윈도우 최댓값/최솟값"** → Monotonic Queue
> - **"양쪽에서 처리"** → Deque

---

## 📚 연결 문서

- [배열과 리스트](linear.md) - Stack, Queue 기초
- [두 포인터](../03_patterns/two-pointers.md) - Sliding Window 기법
- [복잡도](../00_fundamentals/complexity-and-big-o.md) - 분할 상환 분석 (Amortized O(1))
