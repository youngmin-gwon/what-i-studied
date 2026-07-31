# 창 크기 클래스는 기기 종류가 아니라 앱 창을 분류한다

상위 문서: [큰 화면 적응 계약](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md)

Window size class는 태블릿인지, 폴더블인지, ChromeOS인지 판별하는 값이 아니다. 앱에 실제로 주어진 window bounds를 compact, medium, expanded, large, extra-large 같은 크기 구간으로 해석하는 기준이다.

## 왜 중요한가

같은 기기에서도 분할 화면, 자유 크기 조절, 접힘/펼침, 외부 디스플레이 연결에 따라 앱 창은 계속 바뀐다. `isTablet` 같은 분기는 큰 화면에서 가장 먼저 깨지는 추상화다.

## 실무 규칙

- 레이아웃 전환은 물리 기기명이 아니라 현재 앱 창 크기와 비율을 기준으로 결정한다.
- 대부분의 화면은 width class를 중심으로 설계하되, 낮은 height에서는 two-pane이 부적절할 수 있다.
- Compose에서는 Material 3 Adaptive의 `currentWindowAdaptiveInfo()` 같은 API를 우선 고려한다.
- Views 기반 화면은 현재 window metrics를 기준으로 계산하고 deprecated `Display` 크기 API에 기대지 않는다.

## 관련 문서

- [적응형 레이아웃은 같은 화면을 늘리는 것이 아니라 구조를 바꾼다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/adaptive-layout-changes-structure-not-scale.md)
- [Android Navigation 진입 계약](01_inbox/mobile/android/02_app_framework/navigation/navigation-contracts/navigation-contracts.md)

공식 문서: [Use window size classes](https://developer.android.com/develop/ui/views/layout/use-window-size-classes), [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)

기준일: 2026-07-31. Window size class breakpoint와 권장 API는 Jetpack/Material 3 Adaptive 업데이트에 따라 확인한다.
