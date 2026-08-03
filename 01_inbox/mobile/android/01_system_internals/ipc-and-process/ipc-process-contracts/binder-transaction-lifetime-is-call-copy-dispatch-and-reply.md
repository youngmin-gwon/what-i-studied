---
title: binder-transaction-lifetime-is-call-copy-dispatch-and-reply
tags: [android, android/binder, android/ipc]
aliases: [Binder transaction]
date modified: 2026-08-03 17:25:29 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Binder transaction lifetime 은 call, copy, dispatch, reply 로 나뉜다

상위 문서: [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)

동기 Binder 호출은 caller 가 transaction 을 보내고, Binder driver 가 data 와 object reference 를 target process 의 Binder buffer 로 전달하고, target Binder thread 가 `onTransact()` 를 처리한 뒤 reply 를 돌려주는 흐름이다.

이 흐름 때문에 Binder 비용은 "함수 호출 비용"이 아니다. thread scheduling, buffer copy, parcel marshaling, callee work, reply 대기 시간이 모두 caller 지연으로 관찰된다.

### 실무 규칙

- UI thread 에서 느린 Binder 호출을 직접 실행하지 않는다.
- transaction payload 는 작게 유지하고 대용량 데이터는 file descriptor 나 shared buffer 경계로 넘긴다.
- remote exception 과 service death 를 정상 실패 경로로 모델링한다.
- trace 에서는 caller block 시간과 callee 처리 시간을 분리해서 본다.

관련 노트: [IPC 디버깅은 service 등록, call path, thread state에서 시작한다](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-debugging-starts-from-service-registration-call-path-and-thread-state.md)
