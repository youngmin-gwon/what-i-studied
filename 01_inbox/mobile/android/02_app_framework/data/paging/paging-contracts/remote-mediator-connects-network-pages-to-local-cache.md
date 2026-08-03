---
title: RemoteMediator는 network page와 local cache를 연결한다
tags: [android, android/data, android/paging]
aliases: ["RemoteMediator는 network page와 local cache를 연결한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# RemoteMediator는 network page와 local cache를 연결한다

`RemoteMediator`는 network와 local database가 함께 있는 layered source에서 boundary 역할을 한다. UI는 local cache에서 읽고, mediator는 refresh/append/prepend 시점에 network page를 가져와 database를 갱신한다.

이 구조에서는 source of truth가 network response가 아니라 local database가 된다. offline, retry, sync indicator, invalidation 정책은 paging 자체보다 persistence와 synchronization contract로 같이 판단해야 한다.

## 판단 기준

- network result는 바로 UI에 밀어 넣지 말고 transaction으로 local cache에 반영한다.
- remote key는 item table과 별도로 저장해 refresh/append/prepend 위치를 복원한다.
- cache invalidation과 stale data 정책은 product 요구에 맞춰 명시한다.
- network error는 기존 cache 표시와 retry UI를 동시에 고려한다.

관련 노트: [영속 저장소 계약](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md), [Room은 누적되고 조회되는 로컬 데이터를 저장한다](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/room-stores-accumulated-queryable-local-data.md)
