---
title: recursion-and-stack
tags: [call-stack, fundamentals, recursion, stack, tail-recursion]
aliases: [Base Case, 재귀, 재귀의 기초, 호출 스택]
date modified: 2025-12-18 18:17:53 +09:00
date created: 2025-12-18 11:58:00 +09:00
---

## Recursion & Call Stack: 자신을 부르는 논리

**재귀(Recursion)** 는 자신을 정의할 때 자신을 다시 참조하는 방법입니다. 문제를 풀 때 필요한 **가장 강력한 기초 도구** 중 하나로, 복잡한 문제를 단순한 하위 문제로 쪼개 해결하는 논리적 프레임워크를 제공합니다.

> [!NOTE] **기초 다지기**
> 재귀는 처음엔 낯설 수 있지만, 이후의 챕터에서 문제를 풀며 반복적으로 등장하므로 이번에 완벽히 이해하지 못해도 괜찮습니다. 하지만 그 **구조** 와 **구현 방식** 을 익히는 것은 매우 중요합니다.

### 💡 Why it matters (Context)

- **분할 정복**: 퀵 정렬, 병합 정렬 등은 모두 재귀로 작동합니다.
- **비선형 구조 탐색**: 트리(Tree)나 그래프(Graph)의 깊이 우선 탐색(DFS)은 재귀가 가장 자연스럽습니다.
- **코드 가독성**: 반복문보다 훨씬 직관적으로 문제를 표현할 수 있습니다.

---

### 🏢 실무 사례

#### Recursion 활용

- **HTML/XML 파싱**: 계층적인 DOM 구조를 탐색할 때.
- **파일 시스템 탐색**: 폴더 안의 폴더를 계속 뒤지는 기능 (Finder, 탐색기).
- **JSON 라이브러리**: 중첩된 객체 구조를 직렬화/역직렬화할 때.
- **UI 프레임워크**: 컴포넌트 트리 렌더링 (React 등).

---

## 🔑 재귀의 2 가지 필수 조건

이 중 하나라도 없으면 재귀는 끝나지 않고 무한 루프에 빠집니다.

1. **Base Case (기단 상태)**: 재귀를 멈추는 조건. (가장 단순한 상황)
2. **Recursive Step (재귀 단계)**: 문제를 더 작은 단위로 쪼개서 자신을 호출하는 과정.

```python
def factorial(n):
    # 1. Base Case
    if n <= 1:
        return 1
    # 2. Recursive Step (더 작은 n-1로 호출)
    return n * factorial(n - 1)
```

---

## 🧩 재귀 기반의 주요 알고리즘

현업과 코딩테스트에서 재귀는 다음과 같은 핵심 알고리즘들의 뼈대가 됩니다.

- **조합(Combination) / 순열(Permutation)**: 모든 경우의 수를 탐색해야 할 때.
- **분할 정복(Divide & Conquer)**: 병합 정렬(Merge Sort), 퀵 정렬(Quick Sort).
- **탐색(Search)**: 이분 탐색(Binary Search), 깊이 우선 탐색(DFS).
- **동적 계획법(DP)**: 하향식(Top-down) 접근 시 메모이제이션과 함께 사용.

---

## 🥞 호출 스택 (Call Stack)

함수가 호출될 때마다 컴퓨터 메모리의 **Stack** 영역에는 함수의 매개변수, 지역 변수, 돌아갈 주소가 차곡차곡 쌓입니다.

### Stack Overflow

재귀가 너무 깊어지면 메모리의 Stack 영역이 꽉 차서 프로그램이 죽어버리는 현상입니다.

- **Python**: 기본 재귀 한도가 약 1,000 회로 설정되어 있어 주의가 필요합니다.

---

## ⚡ 꼬리 재귀 (Tail Recursion)

재귀의 "스택 소모"라는 단점을 해결하기 위한 최적화 기법입니다.

- **조건**: 함수의 마지막 연산이 `자신을 호출` 하는 것뿐이어야 합니다. (호출 후 추가 연산이 없어야 함)
- **효과**: 컴파일러가 이를 알아차리고 스택을 새로 쌓는 대신 **루프(Iteration)** 로 변환하여 실행합니다.

```python
# 일반 재귀 (factorial * n 이라는 연산이 남아있음)
def normal_fact(n):
    if n == 1: return 1
    return n * normal_fact(n - 1)

# 꼬리 재귀 (함수 결과가 바로 다음 호출의 결과임)
def tail_fact(n, acc=1):
    if n == 1: return acc
    return tail_fact(n - 1, n * acc)
```

>[!NOTE] **언어별 지원**
>Swift, Kotlin, Haskell 등은 지원하지만, **Java, Python 등은 기본적으로 이를 지원하지 않습니다.**

---

## 🚨 흔한 실수 (Common Mistakes)

1. **Base Case 누락** ❌
   - 영원히 멈추지 않는 함수를 만들게 됩니다.
2. **반복문으로 충분한 경우에도 재귀 사용** ❌
   - 단순한 루프는 재귀보다 메모리와 속도 면에서 항상 유리합니다. (스택 쌓는 비용이 없으므로)
3. **상태 공유의 오류**
   - 전역 변수를 재귀에서 잘못 사용하면 각 호출 단계에서 값이 꼬일 수 있습니다. 가급적 인자로 넘기세요.

---

## ⚔️ Recursion vs Iteration (반복문)

| 특징      | Recursion (재귀)   | Iteration (반복) |
| :------ | :--------------- | :------------- |
| **코드**  | 간결하고 직관적임        | 비교적 복잡할 수 있음   |
| **메모리** | 스택 메모리 사용 (많음)   | 상수 메모리 사용 (적음) |
| **속도**  | 함수 호출 오버헤드 있음    | 매우 빠름          |
| **언제?** | 계층 구조, 복잡한 분할 정복 | 단순 반복 처리       |

---

## 📚 관련 문서

- [메모리 계층 구조](../../../02_references/computer-science/memory-layout-and-cache.md) - 스택 메모리의 물리적 위치
- [메모이제이션](memoization.md) - 재귀의 중복 계산을 해결하는 최적화 기법
- [분할 정복](../02_algorithms/divide-and-conquer.md) - 재귀를 활용한 문제 해결 패러다임
- [백트래킹](../02_algorithms/backtracking.md) - 상태 공간 트리와 DFS 탐색
- [문제 해결 프로세스](problem-solving-process.md) - 재귀적 사고 설계법
