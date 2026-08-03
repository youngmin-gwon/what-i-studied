---
title: binder-thread-pool-is-service-concurrency-and-deadlock-boundary
tags: [android, android/binder, android/ipc]
aliases: [Binder thread pool]
date modified: 2026-08-03 17:25:25 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Binder thread pool 은 service concurrency 와 deadlock 경계다

상위 문서: [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)

Binder service 는 들어오는 transaction 을 Binder thread pool 에서 처리한다. thread pool 은 동시성을 제공하지만, blocking call 이 쌓이면 service 전체 응답성이 떨어지고 caller 와 callee 가 서로 기다리는 deadlock 구조도 만들 수 있다.

Binder 를 사용하는 API 는 method 단위만 보지 말고 call graph 전체를 봐야 한다. 특히 service A 가 service B 를 동기 호출하고, 다시 B 가 A 를 호출하는 구조는 thread pool 과 lock 순서에 따라 멈출 수 있다.

### 실무 규칙

- Binder callback 안에서 오래 걸리는 I/O 나 lock 대기를 피한다.
- cross-service 동기 호출은 lock 보유 상태에서 실행하지 않는다.
- callback 재진입 가능성을 API 문서와 구현 양쪽에서 고려한다.
- ANR 분석은 UI thread 뿐 아니라 Binder thread 의 block stack 도 같이 본다.

관련 노트: [ANR은 단일 timeout이 아니라 responsiveness contract 위반이다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/anr-is-responsiveness-contract-violation-not-single-timeout.md)
