---
title: string-advanced-2
tags: [aho-corasick, algorithm, data-structure, lcp, string, suffix-array]
aliases: [Aho-Corasick, Suffix Array, 아호-코라식, 접미사 배열]
date modified: 2025-12-18 15:49:36 +09:00
date created: 2025-12-18 15:45:00 +09:00
---

## String Advanced II: 대규모 문자열 검색과 분석

단일 패턴 매칭을 넘어, 수만 개의 키워드를 동시에 찾거나 문자열의 모든 부분 문자열을 분석하는 초고속 알고리즘들입니다.

### 💡 Why it matters (Context)

- **다중 패턴 매칭**: 금지어 필터링(수천 개의 단어)을 문서 하나에서 한 번에 수행.
- **문자열 분석**: 가장 긴 공통 부분 문자열(LCS), 반복되는 패턴 탐색 등을 효율적으로 처리.
- **인덱싱**: 검색 엔진의 핵심 엔진으로 사용되는 접미사 구조.

---

## 🕸️ 아호 - 코라식 (Aho-Corasick)

**"Trie + KMP"**: 여러 개의 패턴을 트라이(Trie)로 구축하고, KMP 의 실패 함수(Failure Function) 개념을 도입하여 한 번의 스캔으로 모든 패턴을 찾습니다.

### 🔧 핵심 개념
1. **Trie 구축**: 찾고자 하는 모든 단어를 트라이에 삽입.
2. **실패 링크 (Failure Link)**: 매칭 실패 시 이동할 '다음 최선의 노드'를 연결.
3. **출력 링크 (Output Link)**: 현재 노드에서 끝나는 패턴뿐만 아니라, 접미사가 패턴인 경우도 처리.

### 🏢 활용 사례
- **백신 소프트웨어**: 수만 개의 바이러스 시그니처를 실시간 검사.
- **웹 서버 방화벽**: 패킷 내의 위험 키워드 동시 탐색.

---

## 🗂️ 접미사 배열 (Suffix Array) & LCP

문자열의 모든 접미사를 사전순으로 정렬한 배열입니다.

### 1. Suffix Array (접미사 배열)
- 문자열 `banana` 의 모든 접미사: `banana`, `anana`, `nana`, `ana`, `na`, `a`
- 정렬 후: `a`, `ana`, `anana`, `banana`, `na`, `nana`
- **SA 인덱스**: `[5, 3, 1, 0, 4, 2]`

### 2. LCP Array (Longest Common Prefix)
- 정렬된 접미사 배열에서 **인접한 두 접미사 간의 공통 접두사 길이**를 저장합니다.
- 예: `ana` 와 `anana` 의 LCP 는 3 (`ana`).

### 🔧 위력
- **부분 문자열 검색**: $O(M \log N)$ (이진 탐색 활용).
- **서로 다른 부분 문자열 개수**: $\frac{N(N+1)}{2} - \sum LCP$.
- **가장 긴 반복되는 부분 문자열**: LCP 배열의 최댓값.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **메모리 초과 (Suffix Array)**
   - 접미사들을 직접 리스트로 만들면 $O(N^2)$ 공간이 필요합니다. 반드시 인덱스 배열(SA)만 사용하세요.
2. **아호 - 코라식의 메모리 관리**
   - 알파벳 소문자만 있다면 노드당 26 개의 포인터가 필요합니다. 패턴이 많으면 메모리가 급증하므로 `Map` 등을 사용해 공간을 절약해야 할 수 있습니다.

---

## 📚 관련 문서

- [고급 문자열 I](string-advanced-1.md) - Trie 와 KMP 기초
- [트리와 그래프](tree-and-graph.md) - 아호 - 코라식의 기반이 되는 Trie 구조
- [복잡도 분석](../00_fundamentals/complexity-and-big-o.md) - $O(N + M + K)$ 아호 - 코라식의 선형 시간 효율성
- [검색과 정렬](../02_algorithms/search-and-sort.md) - 접미사 배열에서의 이진 탐색 활용
