---
title: Binder thread pool은 service concurrency와 deadlock 경계다
tags: [android, android/ipc, android/binder]
aliases: [Binder thread pool]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

상위 문서: [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)

Binder service는 들어오는 transaction을 Binder thread pool에서 처리한다. thread pool은 동시성을 제공하지만, blocking call이 쌓이면 service 전체 응답성이 떨어지고 caller와 callee가 서로 기다리는 deadlock 구조도 만들 수 있다.

Binder를 사용하는 API는 method 단위만 보지 말고 call graph 전체를 봐야 한다. 특히 service A가 service B를 동기 호출하고, 다시 B가 A를 호출하는 구조는 thread pool과 lock 순서에 따라 멈출 수 있다.

## 실무 규칙

- Binder callback 안에서 오래 걸리는 I/O나 lock 대기를 피한다.
- cross-service 동기 호출은 lock 보유 상태에서 실행하지 않는다.
- callback 재진입 가능성을 API 문서와 구현 양쪽에서 고려한다.
- ANR 분석은 UI thread뿐 아니라 Binder thread의 block stack도 같이 본다.

관련 노트: [ANR은 단일 timeout이 아니라 responsiveness contract 위반이다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/anr-is-responsiveness-contract-violation-not-single-timeout.md)
