---
title: "데스크톱 윈도잉과 멀티태스킹 계약"
tags: ["android", "android/platforms"]
---

# 데스크톱 윈도잉과 멀티태스킹 계약

데스크톱 윈도잉은 Android 앱을 큰 화면에 띄우는 옵션이 아니라, 앱이 resizable window, precise pointer, keyboard, 여러 작업 인스턴스를 견디는지 묻는 실행 환경이다.

## 읽는 순서

1. 창 resize와 precise pointer가 UI 구조를 어떻게 바꾸는지 정한다.
2. visible, resumed, focused 상태를 분리해 자원과 재생의 lifecycle을 설계한다.
3. 여러 창이 필요한 제품만 task, instance, 데이터 소유권을 함께 설계한다.
4. caption bar와 system inset을 앱 콘텐츠의 안전 영역 경계로 처리한다.
5. 좁고 낮은 창부터 여러 instance까지 실제 생산성 과업으로 검증한다.

## 문제 경계

- 콘텐츠 구조만 깨지면 adaptive layout, 포커스나 자원 점유가 틀리면 lifecycle 문제다.
- 새 창이 잘못된 문서를 열면 layout이 아니라 task/back stack 재사용 문제다.
- 상단 컨트롤이 시스템 버튼과 겹치면 padding 상수가 아니라 caption bar inset과 bounding rect 문제다.

## 정본 노트
- [데스크톱 윈도잉에서는 앱 창이 자유롭게 변한다](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/desktop-windowing-makes-android-app-window-freeform.md)
- [Multi-window 생명주기는 단일 전체 화면 가정을 깨뜨린다](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/multi-window-lifecycle-breaks-single-fullscreen-assumption.md)
- [데스크톱 멀티 인스턴스는 작업 단위와 데이터 소유권을 먼저 정해야 한다](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/multi-instance-requires-task-and-data-ownership-boundaries.md)
- [Task와 새 창 실행은 back stack 재사용을 명시해야 한다](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/task-and-window-launch-must-declare-back-stack-reuse.md)
- [Caption bar와 window inset은 데스크톱 UI의 안전 영역이다](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/caption-bar-and-window-insets-define-desktop-safe-area.md)
- [데스크톱 윈도잉 준비도는 작은 화면 호환성이 아니라 생산성 검증이다](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/desktop-windowing-readiness-is-productivity-validation.md)

검증일: 2026-08-03. [Support desktop windowing](https://developer.android.com/develop/adaptive-apps/guides/support-desktop-windowing)
