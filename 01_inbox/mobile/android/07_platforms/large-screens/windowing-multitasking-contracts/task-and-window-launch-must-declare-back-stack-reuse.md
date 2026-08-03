---
title: task-and-window-launch-must-declare-back-stack-reuse
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-03 18:15:13 +09:00
date created: 2026-07-31 18:08:32 +09:00
---

## Task 와 새 창 실행은 back stack 재사용을 명시해야 한다

상위 문서: [데스크톱 윈도잉과 멀티태스킹 계약](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/windowing-multitasking-contracts.md)

데스크톱과 multi-window 에서 `Intent` 실행은 단순 화면 이동이 아니라 어느 task, 어느 window, 어느 기존 activity 를 재사용할지 결정하는 상태 전이다. 알림, deep link, 공유, drag-out, New Window 동작이 모두 같은 back stack 으로 합쳐지면 사용자는 다른 문서나 다른 작업으로 튕긴 것처럼 느낀다.

### 실무 규칙

- `launchMode`, `taskAffinity`, `Intent` flags, `onNewIntent()` 처리를 작업 단위별로 문서화한다.
- 이미 열린 문서를 재사용할지, 새 window 로 열지, 기존 task 위에 쌓을지 명시한다.
- deep link 와 notification click 이 multi-instance 환경에서 어느 창을 선택하는지 테스트한다.
- 새 task 를 만드는 코드는 뒤로 가기, recents, window title, saved state 까지 함께 검증한다.
- 중복 창 생성, 잘못된 문서 표시, 예측 불가능한 back 동작은 desktop 지원에서 출시 차단 버그로 본다.

### 관련 문서

- [Intent는 Android 컴포넌트 실행을 요청하는 데이터 객체다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-describes-component-action-request.md)
- [Deep link는 외부 URI를 앱 내부 목적지로 연결하는 진입 계약이다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-is-external-uri-contract.md)
- [데스크톱 멀티 인스턴스는 작업 단위와 데이터 소유권을 먼저 정해야 한다](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/multi-instance-requires-task-and-data-ownership-boundaries.md)

공식 문서: [Support desktop windowing](https://developer.android.com/develop/adaptive-apps/guides/support-desktop-windowing), [Tasks and the back stack](https://developer.android.com/guide/components/activities/tasks-and-back-stack)
