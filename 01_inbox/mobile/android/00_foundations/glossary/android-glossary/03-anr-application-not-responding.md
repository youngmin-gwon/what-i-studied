---
title: "ANR"
tags: ["android", "android/glossary"]
aliases: ["Application Not Responding"]
---

# ANR

정의: ANR은 앱이나 system component가 정해진 responsiveness contract를 지키지 못했을 때 system_server가 기록하고 사용자에게 드러낼 수 있는 failure signal이다.

혼동 방지: ANR은 단일 timeout 숫자가 아니라 input dispatch, broadcast, service, content provider 같은 호출 경계별 응답성 계약 위반이다. 원인은 main thread block일 수도 있고 binder wait, lock contention, I/O 지연일 수도 있다.

정본 링크:
- [ANR responsiveness contract](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/anr-is-responsiveness-contract-violation-not-single-timeout.md)
- [Logcat, crash, ANR debugging](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/logcat-crash-anr-and-debugger-answer-different-questions.md)
