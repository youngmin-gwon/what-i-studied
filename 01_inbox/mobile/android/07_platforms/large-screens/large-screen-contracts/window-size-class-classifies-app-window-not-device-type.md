---
title: "창 크기 클래스는 기기 종류가 아니라 앱 창을 분류한다"
tags: ["android", "android/platforms"]
---

# 창 크기 클래스는 기기 종류가 아니라 앱 창을 분류한다

상위 문서: [큰 화면 적응 계약](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md)

Window size class는 태블릿인지, 폴더블인지, ChromeOS인지 판별하는 값이 아니다. 앱에 실제로 주어진 window bounds를 compact, medium, expanded, large, extra-large 같은 크기 구간으로 해석하는 기준이다.

## 왜 중요한가

같은 기기에서도 분할 화면, 자유 크기 조절, 접힘/펼침, 외부 디스플레이 연결에 따라 앱 창은 계속 바뀐다. `isTablet` 같은 분기는 큰 화면에서 가장 먼저 깨지는 추상화다.

## 실무 규칙

- 레이아웃 전환은 물리 기기명이 아니라 현재 앱 창 크기와 비율을 기준으로 결정한다.
- 대부분의 화면은 width class를 중심으로 설계하되, 낮은 height에서는 two-pane이 부적절할 수 있다.
- Compose에서는 Material 3 Adaptive의 `currentWindowAdaptiveInfo()`를 우선 고려한다. large와 extra-large width 구간을 사용할 때는 현재 API의 `supportLargeAndXLargeWidth = true` 조건을 함께 확인한다.
- Views 기반 화면은 현재 window metrics를 기준으로 계산하고 deprecated `Display` 크기 API에 기대지 않는다.

## 기준과 경계

- width는 compact `<600dp`, medium `600..<840dp`, expanded `840..<1200dp`, large `1200..<1600dp`, extra-large `>=1600dp`다.
- height는 별도로 compact `<480dp`, medium `480..<900dp`, expanded `>=900dp`로 분류한다.
- breakpoint는 고수준 레이아웃 결정의 출발점이지 모든 컴포넌트의 고정 분기표가 아니다. 실제 콘텐츠 제약과 posture를 추가로 적용한다.

## 관련 문서

- [적응형 레이아웃은 같은 화면을 늘리는 것이 아니라 구조를 바꾼다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/adaptive-layout-changes-structure-not-scale.md)
- [Android Navigation 진입 계약](01_inbox/mobile/android/02_app_framework/navigation/navigation-contracts/navigation-contracts.md)

공식 문서: [Use window size classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes), [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)

검증일: 2026-08-03. breakpoint와 `currentWindowAdaptiveInfo()` 옵션은 Material 3 Adaptive 업데이트에 따라 다시 확인한다.
