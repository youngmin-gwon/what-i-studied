---
title: Binder transaction lifetime은 call, copy, dispatch, reply로 나뉜다
tags: [android, android/ipc, android/binder]
aliases: [Binder transaction]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

상위 문서: [IPC and process contracts](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md)

동기 Binder 호출은 caller가 transaction을 보내고, Binder driver가 data와 object reference를 target process의 Binder buffer로 전달하고, target Binder thread가 `onTransact()`를 처리한 뒤 reply를 돌려주는 흐름이다.

이 흐름 때문에 Binder 비용은 “함수 호출 비용”이 아니다. thread scheduling, buffer copy, parcel marshaling, callee work, reply 대기 시간이 모두 caller 지연으로 관찰된다.

## 실무 규칙

- UI thread에서 느린 Binder 호출을 직접 실행하지 않는다.
- transaction payload는 작게 유지하고 대용량 데이터는 file descriptor나 shared buffer 경계로 넘긴다.
- remote exception과 service death를 정상 실패 경로로 모델링한다.
- trace에서는 caller block 시간과 callee 처리 시간을 분리해서 본다.

관련 노트: [IPC 디버깅은 service 등록, call path, thread state에서 시작한다](01_inbox/mobile/android/01_system_internals/ipc-and-process/ipc-process-contracts/ipc-debugging-starts-from-service-registration-call-path-and-thread-state.md)
