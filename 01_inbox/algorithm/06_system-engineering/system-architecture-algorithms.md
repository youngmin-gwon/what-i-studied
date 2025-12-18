---
title: system-architecture-algorithms
tags: [algorithm, system-engineering, redis, database, git, engineering]
aliases: [시스템 아키텍처 알고리즘, 실무 알고리즘, Engineering Algorithms]
date modified: 2025-12-18 15:58:00 +09:00
date created: 2025-12-18 15:58:00 +09:00
---

## System Architecture Algorithms: 실무 시스템의 심장

알고리즘은 코딩테스트용만이 아닙니다. 우리가 매일 쓰는 Database, Cache, Git의 내부에는 거대한 엔지니어링 최적화가 숨어 있습니다.

### 💡 Why it matters (Context)

- **대규모 데이터**: 초당 수만 건의 요청을 처리하기 위한 선택.
- **Trade-off**: 읽기 성능을 위해 쓰기를 희생할 것인가? 메모리와 속도 중 무엇이 중요한가?

---

## 🚀 Redis: 초고속 캐시의 비밀

### 1. Skip List (스키드 리스트)
- Redis의 `Sorted Set` 내부 자료구조.
- 연결 리스트에 '층(Level)'을 두어 이진 탐색 수준($O(\log N)$)의 성능을 냄. 구현이 균형 트리보다 간결함.

### 2. Hash Slot
- Redis Cluster에서 데이터를 분산 저장하는 메커니즘. 일관된 해싱(Consistent Hashing)의 변형.

---

## 🗄️ Database: 데이터 저장의 철학

### 1. B+ Tree (Read-Intensive)
- 대부분의 RDBMS(MySQL, PostgreSQL) 인덱스.
- 모든 데이터는 리프 노드에만 저장하여 스캔 성능 극대화. 디스크 I/O 최적화.

### 2. LSM Tree (Log-Structured Merge Tree)
- NoSQL(Cassandra, RocksDB)이나 대량 로그 저장에 사용.
- 메모리에 먼저 쓰고(Append-only), 나중에 백그라운드에서 병합하여 **쓰기 성능**을 극대화.

---

## 🌳 Git: 버전 관리의 마법

### 1. DAG (Directed Acyclic Graph)
- Git의 커밋 히스토리는 방향성 있는 비순환 그래프입니다.
- 충돌 해결(Merge) 시 공통 조상(LCA)을 찾는 알고리즘이 핵심.

### 2. Delta Encoding
- 파일의 전체 내용을 매번 저장하는 대신, 변경된 차이점만 저장하여 용량 최적화.

---

## 🚨 엔지니어링 관점의 주의사항

1. **상수 시간($O(1)$)의 함정**
   - 알고리즘적으로는 $O(1)$이어도, 실제 캐시 미스나 네트워크 지연이 발생하면 $O(N)$보다 느릴 수 있습니다.
2. **복잡도 vs 유지보수성**
   - 수 밀리초를 아끼기 위해 극도로 복잡한 자작 자료구조를 쓰는 것보다, 검증된 라이브러리 자료구조를 쓰는 것이 실무에서는 더 유리할 때가 많습니다.

---

## 📚 관련 문서
- [해시와 맵](../01_data-structures/hash-and-map.md) - 시스템 분산 저장의 기초
- [트리와 그래프](../01_data-structures/tree-and-graph.md) - B+ Tree, DAG의 원형
- [메모리와 캐시](../00_fundamentals/memory-layout-and-cache.md) - 하드웨어 최적화의 근본
- [복잡도 분석](../00_fundamentals/complexity-and-big-o.md) - 시스템 설계의 성능 척도
