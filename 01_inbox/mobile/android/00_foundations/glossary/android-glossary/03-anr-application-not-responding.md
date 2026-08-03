---
title: 03-anr-application-not-responding
tags: ["android", "android/glossary"]
aliases: ["Application Not Responding"]
date modified: 2026-08-03 17:21:47 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

## ANR 은 앱이 메인 스레드에서 응답하지 못할 때 발생하는 상태다

정의: ANR 은 앱이나 system component 가 정해진 responsiveness contract 를 지키지 못했을 때 system_server 가 기록하고 사용자에게 드러낼 수 있는 failure signal 이다.

혼동 방지: ANR 은 단일 timeout 숫자가 아니라 input dispatch, broadcast, service, content provider 같은 호출 경계별 응답성 계약 위반이다. 원인은 main thread block 일 수도 있고 binder wait, lock contention, I/O 지연일 수도 있다.

정본 링크:

- [ANR responsiveness contract](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/anr-is-responsiveness-contract-violation-not-single-timeout.md)
- [Logcat, crash, ANR debugging](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/logcat-crash-anr-and-debugger-answer-different-questions.md)
