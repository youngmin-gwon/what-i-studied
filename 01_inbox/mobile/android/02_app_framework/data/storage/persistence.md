---
title: persistence
tags: [android, android/data, android/persistence-contracts, android/storage]
aliases: ["영속 저장소 계약"]
date modified: 2026-08-03 18:09:08 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 영속 저장소 계약

영속 저장소는 앱 재시작 뒤에도 남아야 하는 데이터의 형태와 접근 방식을 정한다. DataStore 와 Room 은 대체재가 아니라 서로 다른 데이터 계약이다.

### 정본 노트

- [Android 저장소는 데이터 수명과 소유권으로 선택한다](persistence-lifetime-selection.md)
- [DataStore는 작은 설정과 현재 상태를 저장한다](datastore-key-value.md)
- [Room은 누적되고 조회되는 로컬 데이터를 저장한다](room-local-database.md)
- [SQLite와 Room의 경계는 엔진과 애플리케이션 API의 차이다](sqlite-vs-room.md)
- [Repository는 Room과 DataStore를 Flow로 연결한다](repository-flow-integration.md)
- [DataStore와 Room 마이그레이션은 저장소 계약의 시간 경계다](datastore-room-migrations.md)

상위 지도: [Android 저장소와 영속성](android-storage-and-persistence.md)
