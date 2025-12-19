---
title: stack-and-queue
tags: [algorithm, data-structure, fifo, lifo, linear, queue, stack]
aliases: [FIFO, LIFO, Queue, Stack, 스택, 큐]
date modified: 2025-12-19 18:50:40 +09:00
date created: 2025-12-18 12:04:02 +09:00
---

## Stack & Queue: 데이터의 순서를 제어하는 기초

**스택(Stack)** 과 **큐(Queue)** 는 데이터를 저장하고 꺼내는 **순서**에 대한 약속입니다. 가장 단순하지만 가장 강력한 도구입니다.

### 💡 Why it matters (Context)

- **순서 기록**: 수행한 작업의 이력을 기록하거나(Undo/Redo), 들어온 순서대로 요청을 처리할 때 필수적입니다.
- **제어 흐름**: 복잡한 비선형 구조(그래프)를 탐색할 때 다음에 어디로 갈지를 결정하는 핵심 저장소입니다.
- **버퍼**: 데이터 전송 속도 차이를 극복하기 위해 잠시 대기시키는 장소입니다.

---

### 🏢 실무 사례

#### Stack (LIFO) 활용

- **브라우저 방문 기록**: '뒤로 가기' 버튼을 누를 때 가장 최근 페이지로 이동.
- **텍스트 에디터 Undo/Redo**: 입력한 순서의 역순으로 복원.
- **컴파일러/인터프리터**: 괄호 `()`, `{}`, `[]` 짝 맞추기 및 계산기 수식 파싱.
- **함수 호출(Call Stack)**: 프로그램 실행 시 복귀 주소 관리.

#### Queue (FIFO) 활용

- **프린터 출력 대기열**: 먼저 인쇄 버튼을 누른 문서부터 순서대로 출력.
- **메시지 브로커 (Kafka, RabbitMQ)**: 서비스 간 비동기 요청을 순서대로 처리.
- **OS 스케줄링**: Ready Queue 에 대기 중인 프로세스를 순서대로 할당.
- **네트워크 패킷 버퍼**: 도착한 패킷을 버퍼에 담아두고 순차적으로 처리.

---

## 🥞 Stack (스택, LIFO)

"Last In, First Out" - 나중에 들어온 놈이 먼저 나간다.

| 연산 | 설명 | 복잡도 |
|:---|:---|:---|
| **Push** | 상단에 데이터 추가 | $O(1)$ |
| **Pop** | 상단 데이터 제거 및 반환 | $O(1)$ |
| **Peek** | 상단 데이터 확인 (제거 X) | $O(1)$ |

### 🔧 구현 (Python)
```python
stack = []
stack.append(1) # Push
stack.pop()      # Pop
stack[-1]       # Peek
```

---

## 🏃 Queue (큐, FIFO)

"First In, First Out" - 먼저 들어온 놈이 먼저 나간다.

| 연산 | 설명 | 복잡도 |
|:---|:---|:---|
| **Enqueue** | 뒤(Rear)에 데이터 추가 | $O(1)$ |
| **Dequeue** | 앞(Front)에서 데이터 제거 | $O(1)$ |

### 🔧 구현 (Python - deque 권장)
```python
from collections import deque
queue = deque()
queue.append(1)    # Enqueue
queue.popleft()    # Dequeue
```

>[!CAUTION] **리스트(`list.pop(0)`)는 쓰지 마세요!**
>파이썬 리스트의 첫 번째 요소를 빼면 나머지 모든 요소를 앞으로 한 칸씩 당겨야 하므로 $O(N)$ 이 걸립니다. 반드시 `collections.deque` 를 사용하세요.

---

## 🎨 순환 큐 (Circular Queue)

고정된 크기의 배열을 효율적으로 사용하기 위해 마지막 인덱스 다음에 다시 처음 인덱스로 연결되는 구조입니다. 메모리 재할당 없이 큐를 무한히 회전시키며 쓸 수 있습니다.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **Stack Underflow/Overflow** ❌
   - 비어있는 스택에서 `pop` 을 하거나, 고정 크기 스택이 꽉 찼는데 `push` 를 시도하는 경우.
2. **큐의 Dequeue 성능 저하** ❌
   - 배열의 앞부분을 제거하고 전체를 Shift 하는 $O(N)$ 연산을 수행하는 실수. (언어별 전용 자료구조나 포인터 활용 필수)
3. **용도 혼동**
   - 최근 기록이 중요한데 큐를 쓰거나, 줄 세우기가 필요한데 스택을 쓰는 설계 오류.

---

## 🐍 실전 Python 활용 (Applied Python)

Python 에서는 별도의 Stack/Queue 클래스 대신 `list` 나 `collections.deque` 를 활용합니다. 특히 큐의 경우 성능 차이가 극명하므로 주의가 필요합니다.

### 1. 스택 (Stack)

그냥 기본 `list` 를 사용해도 무방합니다. (LIFO)

#### 💻 활용법
```python
stk = []
stk.append(1) # Push
stk.pop()      # Pop
stk[-1]        # Peek
```

### 2. 큐 (Queue)

반드시 `collections.deque` 를 사용해야 합니다. (FIFO)

#### 💻 활용법

```python
from collections import deque
q = deque()

q.append(1)    # Enqueue
q.popleft()    # Dequeue (O(1))
```

>[!CAUTION] **`list.pop(0)` 은 금지!**
>리스트에서 첫 번째 원소를 제거하면 뒤의 모든 원소를 한 칸씩 당겨야 하므로 **$O(N)$**이 소요됩니다. 큐 구현 시에는 무조건 `deque` 의 **`popleft()`**를 사용하세요.

---

### 📚 연결 문서

- [재귀와 스택](../00_fundamentals/recursion-and-stack.md) - 논리적/물리적 실행 스택의 이해
- [특수 큐/스택](specialized-queues.md) - Deque, Monotonic Stack, Monotonic Queue
- [그래프 탐색](../02_algorithms/graph-traversal.md) - BFS(Queue 사용) vs DFS(Stack 사용)
- [선형 자료구조](linear.md) - Array 와 Linked List 를 이용한 구현 원리
