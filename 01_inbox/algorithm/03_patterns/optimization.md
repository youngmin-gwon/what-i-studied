---
title: optimization-strategies
tags: [algorithm, optimization, architecture, heuristic]
aliases: [최적화 전략, 알고리즘 선택, 휴리스틱, 최적화]
date modified: 2025-12-18 11:53:38 +09:00
date created: 2025-12-17 19:50:00 +09:00
---

## Optimization Strategies: "어떤 알고리즘을 쓸 것인가?"

단순히 특정 알고리즘 하나를 아는 것보다, 주어진 상황에서 **어떤 전략이 가장 효율적인지 판단**하는 능력이 중요합니다.

### 💡 Why it matters (Context)

- **정답 vs 효율**: 모든 경우를 따지면 100년이 걸리는 문제를 1초 만에 풀 수 있게 만듭니다.
- **자원 제약**: 메모리가 부족한 임베디드 환경과, 속도가 중요한 데이터 센터 환경의 전략은 다릅니다.

---

### 🏢 실무 사례

#### 최적화 전략 활용
- **웹 서버 수평 확장**: 캐시(DP 철학)와 로드 밸런싱을 통한 병목 해결.
- **검색 알고리즘 (Elasticsearch)**: 완벽한 검색 대신 근사치(Approximate Nearest Neighbor)를 통한 속도 확보.
- **비디오 인코딩**: 시간적 중복(이전 프레임 재사용 = DP)을 제거하여 용량 최적화.
- **컴파일러 최적화**: 코드 내의 중복 계산 제거 및 레지스터 활용 최적화.

---

## 🧭 알고리즘 선택 매트릭스

문제를 만났을 때 다음 질문들을 따라가 보세요.

### 1. 데이터의 크기 (N) 확인
- **$N \le 20$**: 모든 경우의 수 ([[02_algorithms/backtracking|Backtracking]]) 가능.
- **$N \le 10^5$**: $O(N \log N)$ 알고리즘 ([[02_algorithms/search-and-sort|정렬]], [[03_patterns/two-pointers|투 포인터]]) 필요.
- **$N \ge 10^7$**: $O(N)$ 또는 $O(\log N)$ ([[03_patterns/prefix-sum|누적 합]], [[02_algorithms/search-and-sort|이진 탐색]]) 필수.

### 2. 문제 유형에 따른 접근

| 상황 | 추천 전략 | 이유 |
|:---|:---|:---|
| **중복 계산이 발생함** | **Dynamic Programming** | 이미 푼 문제는 답을 재사용 |
| **매 순간 최선의 선택이 정답** | **Greedy** | 빠르고 직관적이나 증명 필요 |
| **모든 경로를 가봐야 함** | **Backtracking** | 가지치기(Pruning)로 탐색 공간 축소 |
| **연속된 구간을 다룸** | **Sliding Window** | 2중 루프 방지 |
| **잦은 구간 합 질문** | **Prefix Sum** | $O(1)$ 조회 성능 |

---

## 🛠️ 실무 최적화의 3원칙

### 1. **Caching (DP / Memoization)**
"공간을 써서 시간을 산다." 한 번 계산한 복잡한 값이나 데이터베이스 쿼리는 저장해두고 재사용합니다.

### 2. **Pruning (Better Search)**
"쓸데없는 일은 하지 않는다." 조건에 맞지 않는 탐색 경로는 아예 발을 들이지 않습니다.

### 3. **Heuristics (Close enough is good)**
"완벽한 정답보다 빠른 근사치." 실무에서는 0.0001초 차이가 중요하지 않은 경우, 완벽한 최단 경로 대신 적당히 빠른 경로를 선택합니다 (예: A* 알고리즘).

---

## 🚨 최적화 시 흔한 실수 (Premature Optimization)

> "성급한 최적화는 만악의 근원이다." - 도널드 커누스(Donald Knuth)

1. **병목 지점 오판**: 90%의 시간을 잡아먹는 곳은 따로 있는데, 1%만 차지하는 코드를 고치느라 고생하는 경우. (반드시 **프로파일링** 하세요!)
2. **코드 가독성 저하**: 고작 몇 밀리초를 아끼려고 코드를 알아볼 수 없게 꼬아버리는 경우.
3. **메모리 오버헤드 무시**: 시간을 아끼려고 무작정 캐싱을 하다가 메모리 부족(OOM)으로 시스템이 죽는 경우.

---

### 📚 연결 문서
- [[02_algorithms/dynamic-programming|Dynamic Programming]] - 최적화의 왕
- [[03_patterns/two-pointers|Two Pointers]] - $O(N^2)$ 타파
- [[00_fundamentals/complexity-and-big-o|복잡도 분석]] - 최적화 대상을 찾는 눈
- [[README]] - 전체 학습 로드맵
