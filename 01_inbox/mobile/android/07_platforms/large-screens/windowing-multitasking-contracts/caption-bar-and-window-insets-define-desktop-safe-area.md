---
title: "Caption bar와 window inset은 데스크톱 UI의 안전 영역이다"
tags: ["android", "android/platforms"]
---

# Caption bar와 window inset은 데스크톱 UI의 안전 영역이다

상위 문서: [데스크톱 윈도잉과 멀티태스킹 계약](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/windowing-multitasking-contracts.md)

Desktop windowing의 창 상단에는 시스템이 그리는 caption bar와 창 제어 영역이 있다. immersive mode에서도 이 영역은 사라진다고 가정할 수 없고, 앱 UI는 inset과 system gesture 영역을 기준으로 안전하게 배치되어야 한다.

## 실무 규칙

- caption bar가 보일 때 콘텐츠가 닫기, 최대화, 드래그 영역과 겹치지 않게 한다.
- custom header를 그릴 때도 시스템의 interactive caption element는 시스템이 소유한다는 점을 전제로 둔다.
- `WindowInsets.captionBar`와 caption bar visibility로 영역을 계산하고 높이를 하드코딩하지 않는다.
- Android 15(API 35)의 `WindowInsets.getBoundingRects()`로 닫기와 최대화 같은 시스템 요소의 점유 영역을 제외한다.
- 탭, 검색창처럼 상단 interactive UI를 둘 때 `setSystemGestureExclusionRects()`가 필요한지 별도로 판단한다.

## 관련 문서

- [데스크톱 윈도잉에서는 앱 창이 자유롭게 변한다](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/desktop-windowing-makes-android-app-window-freeform.md)
- [적응형 레이아웃은 같은 화면을 늘리는 것이 아니라 구조를 바꾼다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/adaptive-layout-changes-structure-not-scale.md)

공식 문서: [Support desktop windowing](https://developer.android.com/develop/adaptive-apps/guides/support-desktop-windowing)

검증일: 2026-08-03. immersive mode에서도 desktop header bar가 존재할 수 있고 시스템 interactive caption element는 계속 시스템이 그린다.
