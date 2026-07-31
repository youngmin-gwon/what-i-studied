---
title: "ATMS는 activity, task, back stack 전이를 담당한다"
tags: [android, android/system-internals, android/boot-runtime, android/system-server]
aliases: ["ATMS는 activity, task, back stack 전이를 담당한다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# ATMS는 activity, task, back stack 전이를 담당한다

상위 문서: [system_server와 ActivityManager 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/system-server-contracts/system-server-contracts.md)

Android 10 이후 ActivityTaskManagerService는 activity, task, stack, window-facing transition 같은 UI 중심 실행 흐름을 AMS에서 분리해 담당한다. AMS가 process와 component 운영의 중심이라면 ATMS는 사용자가 보는 activity/task 전이의 중심이다.

## 실무 의미

- Activity launch, task 재사용, recents, multi-window, back stack 문제는 ATMS 책임과 맞닿아 있다.
- 프로세스 중요도와 task 전이는 연결되지만 같은 개념이 아니다.
- deep link나 notification launch 문제는 앱 navigation graph만 보지 말고 task/launchMode도 함께 봐야 한다.

## 관련 문서

- [Task와 새 창 실행은 back stack 재사용을 명시해야 한다](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/task-and-window-launch-must-declare-back-stack-reuse.md)
- [Android Navigation 진입 계약](01_inbox/mobile/android/02_app_framework/navigation/navigation-contracts/navigation-contracts.md)
