---
title: oneway-binder-removes-caller-waiting-not-server-backpressure
tags: [android, android/binder, android/ipc]
aliases: [oneway Binder]
date modified: 2026-08-03 17:25:31 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## oneway Binder 는 caller 대기를 없애지만 server backpressure 를 없애지 않는다

상위 문서: [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)

`oneway` AIDL 호출은 caller 가 reply 를 기다리지 않는 비동기 transaction 으로 바뀐다. 하지만 이것은 server 의 queue, Binder thread pool, 처리 비용, 순서 제약을 사라지게 하지 않는다.

따라서 `oneway` 는 latency hiding 도구이지 무제한 이벤트 버스가 아니다. 호출 빈도가 높거나 payload 가 큰 경계에서는 queue 적체, memory pressure, server thread 고갈을 별도로 설계해야 한다.

### 실무 규칙

- `oneway` 는 결과가 필요 없고 caller 가 실패를 즉시 복구할 수 있는 이벤트에만 쓴다.
- 상태 변경 명령은 idempotency 와 재동기화 경로를 둔다.
- progress, ack, error reporting 이 필요하면 별도 callback 이나 관찰 API 를 설계한다.
- "caller 가 안 기다림"과 "system 에 비용이 없음"을 혼동하지 않는다.

관련 노트: [Binder thread pool은 service concurrency와 deadlock 경계다](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/binder-thread-pool-is-service-concurrency-and-deadlock-boundary.md)
