---
title: binary-search-optimization
tags: [algorithm, pattern, binary-search, parametric-search, optimization]
aliases: [결정 문제, 파라메트릭 서치, Binary Search on Answer, Parametric Search]
date modified: 2025-12-18 11:55:01 +09:00
date created: 2025-12-18 11:55:01 +09:00
---

## Binary Search on Answer: "최적화 문제를 결정 문제로"

가장 어려운 난이도의 이진 탐색 패턴입니다. 단순히 배열에서 숫자를 찾는 게 아니라, **"정답이 X일 때 가능한가?"**를 물어보며 정답의 범위를 좁혀나갑니다.

이를 **파라메트릭 서치(Parametric Search)**라고도 합니다.

### 💡 Why it matters (Context)

- **최대/최소의 최적화**: "나무를 최소한으로 자르면서 원하는 양을 얻는 최대 높이는?"
- **이진성 활용**: "X 에너지가 있을 때 목적지까지 갈 수 있는가?" (YES/NO)
- **범위 축소**: 정답의 범위가 $10^{18}$처럼 말도 안 되게 클 때 $O(\log N)$으로 해결.

---

### 🏢 실무 사례

#### 활용 분야
- **네트워크 디자인**: 특정 대역폭(Bandwidth)을 보장하면서 구축 비용을 최소화하는 지점 찾기.
- **물류 최적화**: 트럭의 최대 적재 용량을 결정할 때, 모든 짐을 실을 수 있는 최소 용량 찾기.
- **그래픽 엔진**: 특정 프레임 레이트(FPS)를 유지하기 위한 최적의 LOD(Level of Detail) 임계값 산출.
- **제조 공정**: 불량률을 특정 수준 이하로 유지하면서 생산 속도를 최대화하는 설정값 찾기.
- **금융 모델링**: 특정 리스크 수준을 넘지 않는 최대 투자 금액 산출.

---

## 🔑 패턴의 핵심 구조

"최댓값/최솟값을 구하라" → **"K라는 값이 조건을 만족하는가?" (True/False)**

### 🔧 구현 템플릿

```python
def solve(params):
    low = min_possible_answer
    high = max_possible_answer
    result = low
    
    while low <= high:
        mid = (low + high) // 2
        
        # 핵심: 결정 함수(Decision Function)
        if is_possible(mid):
            result = mid    # 일단 답으로 저장
            low = mid + 1   # 더 큰 값도 가능한지 확인 (최댓값 찾기라면)
        else:
            high = mid - 1
            
    return result

def is_possible(k):
    # k라는 정답이 주어졌을 때, 비즈니스 로직으로 가능한지 판별
    # 보통 이 함수가 O(N) 정도 소요됨
    pass
```

---

## 🔥 대표 예제: 공유기 설치 (Router)

**문제**: 집들의 좌표가 주어질 때, C개의 공유기를 설치해서 인접한 공유기 사이의 **거리를 최대화**하기.

```python
def can_install(dist, houses, C):
    count = 1  # 첫 번째 집에 설치
    last_loc = houses[0]
    
    for i in range(1, len(houses)):
        if houses[i] - last_loc >= dist:
            count += 1
            last_loc = houses[i]
    return count >= C

def maximum_distance(houses, C):
    houses.sort()
    low = 1
    high = houses[-1] - houses[0]
    res = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_install(mid, houses, C):
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return res
```

---

## 🚨 흔한 실수 (Common Mistakes)

1.  **이진 탐색 대상 선정 오류** ❌
    - 배열의 인덱스를 이진 탐색하는 것이 아니라, 우리가 구하고자 하는 **'값(정답)'의 범위**를 탐색해야 합니다.
2.  **`low`, `high` 초기값 설정**
    - 정답이 될 수 있는 최소/최대치를 너무 좁게 잡으면 답을 못 찾습니다. 넉넉하게 잡으세요. (단, 무한 루프 주의)
3.  **정렬 잊음**
    - 결정 함수(`is_possible`) 내에서 데이터를 처리할 때 정렬된 상태가 필요한 경우가 많습니다.
4.  **결정 함수의 시간 복잡도**
    - 전체 복잡도는 $O(\text{결정 함수 복잡도} \times \log(\text{정답 범위}))$입니다. 결정 함수가 너무 느리면 이진 탐색도 소용없습니다.

---

## ⚔️ 일반 Binary Search vs 이진 탐색 최적화

| 특징 | 일반 이진 탐색 | 이진 탐색 최적화 (Parametric) |
|:---|:---|:---|
| **찾는 것** | 배열의 특정 값 | 조건을 만족하는 최적의 정답 |
| **탐색 대상** | 인덱스 또는 요소 | 정답의 수치 범위 |
| **핵심 도구** | 값 비교 (`==`, `<`, `>`) | **결정 함수** (`is_possible`) |

---

### 📚 연결 문서
- [[02_algorithms/search-and-sort|검색과 정렬]] - 이진 탐색 기초
- [[03_patterns/optimization|최적화 전략]] - 최적화 문제를 푸는 다른 방법(Greedy, DP)
- [[00_fundamentals/complexity-and-big-o|복잡도]] - $O(N \log (\text{Range}))$의 위력
- [[02_algorithms/greedy|Greedy]] - 결정 함수 작성 시 그리디 기법이 자주 쓰임
