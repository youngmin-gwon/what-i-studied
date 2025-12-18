---
title: line-sweep
tags: [algorithm, pattern, geometry, sweep-line]
aliases: [평면 스위핑, 라인 스위핑, Sweep Line]
date modified: 2025-12-18 15:52:00 +09:00
date created: 2025-12-18 15:52:00 +09:00
---

## Line Sweep: 평면을 훑고 지나가는 최적화

**평면 스위핑(Line Sweep)**은 수직선이나 수평선을 평면 위에서 한쪽 끝에서 다른 쪽 끝으로 움직이며, 선이 만나는 **이벤트(Event)**들을 순차적으로 처리하는 기법입니다.

### 💡 Why it matters (Context)

- **$O(N^2)$ 타파**: 모든 쌍을 비교해야 할 것 같은 $O(N^2)$ 기하 문제를 $O(N \log N)$으로 해결합니다.
- **정렬과 효율**: 데이터를 한 방향으로 정렬하고, 현재 관련 있는 데이터만 관리(Active Set)하여 성능을 극대화합니다.

---

## 🎯 대표적인 적용 사례

### 1. 겹치는 사각형의 넓이
수직선이 왼쪽에서 오른쪽으로 이동하며:
- **사각형 시작**: 현재 스위핑 선에 걸친 y-구간 추가.
- **사각형 종료**: y-구간 제거.
- **이동 거리**: (현재 x - 이전 x) $\times$ (현재 y-구간의 총합).

### 2. 가장 가까운 두 점 (Closest Pair)
x축으로 이동하며, 현재 점 주변($d$ 거리 이내)의 점들만 후보로 두고 탐색 범위를 좁힙니다.

### 3. 선분 교차점 찾기 (Bentley-Ottmann)
대량의 선분들 중 교차하는 지점들을 $O((N+I) \log N)$에 찾습니다.

---

## 🔧 핵심 구성 요소
1. **Event Queue**: 정렬된 이벤트 지점들 (x 좌표 등).
2. **Status Structure**: 현재 스위핑 선이 가로지르는 객체들을 관리하는 자료구조 (보통 [[01_data-structures/tree-and-graph|BST]]나 [[01_data-structures/segment-tree|Segment Tree]]).

---

## 🚨 흔한 실수 (Common Mistakes)

1. **이벤트 정렬 오류**: x좌표가 같을 때 어떤 이벤트를 먼저 처리할지(시작 vs 끝)를 정하지 않으면 누락이 발생합니다.
2. **부적절한 자료구조 선택**: 선에 걸친 객체를 조회/삭제하는 데 시간이 오래 걸리면 스위핑의 장점이 사라집니다 ($O(\log N)$ 권장).

---

## 📚 관련 문서
- [[03_patterns/interval-patterns|구간 패턴]] - 1차원 스윕 라인의 기초
- [[01_data-structures/segment-tree|세그먼트 트리]] - 사각형 넓이 등 면적 계산의 파트너
- [[02_algorithms/search-and-sort|검색과 정렬]] - 이벤트 큐 관리를 위한 정렬
- [[05_geometry/geometry-fundamentals|기하 기초]] - 점과 선의 기본 관계
