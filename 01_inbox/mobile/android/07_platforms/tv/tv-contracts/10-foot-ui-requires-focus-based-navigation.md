---
title: 10-foot-ui-requires-focus-based-navigation
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-03 18:16:09 +09:00
date created: 2026-08-03 17:27:04 +09:00
---

## 10-foot UI 는 포커스 기반 탐색을 요구한다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](01_inbox/mobile/android/07_platforms/android-platforms-and-form-factors.md)

관련 지도: [Android TV 계약](01_inbox/mobile/android/07_platforms/tv/tv-contracts/tv-contracts.md)

### 핵심 정의

"10-foot UI"는 시청자가 약 3 미터(10 피트) 거리에서 TV 화면을 보는 상황을 가정한 디자인 기준이다. 이 거리에서는 휴대폰 화면 대비 훨씬 큰 텍스트, 넓은 여백, 명확한 포커스 표시가 필요하며, 콘텐츠 탐색은 그리드/행(row) 기반 카드 목록을 방향키로 이동하는 패턴이 표준이다.

### 메커니즘

Jetpack 의 Leanback 라이브러리(View 기반, 현재는 유지보수 모드)와 최신 TV 용 Compose 컴포넌트는 모두 `BrowseSupportFragment` 또는 행 기반 컴포저블로 콘텐츠 카테고리를 가로 스크롤 행으로 배치하고, 각 카드에 포커스가 이동할 때 확대/강조 애니메이션을 기본 제공한다. 포커스가 이동하는 논리적 순서는 화면 배치와 반드시 일치해야 하며, 그렇지 않으면 사용자가 방향키를 눌러도 예상과 다른 요소로 포커스가 튄다.

### 판단 기준

- 텍스트 크기와 히트 영역을 휴대폰 기준 dp 값을 그대로 재사용하지 않는다. TV 는 시청 거리가 멀기 때문에 최소 텍스트 크기와 카드 크기 기준이 다르다.
- 콘텐츠 카탈로그형 앱은 처음부터 행 기반 브라우즈 패턴(Leanback 스타일)을 채택하는 것이 커스텀 그리드를 처음부터 설계하는 것보다 d-pad 탐색 일관성을 얻기 쉽다.
- 포커스 확대/강조 애니메이션이 없으면 사용자가 현재 선택된 항목을 인지하기 어렵다. 시각적 포커스 표시를 생략하지 않는다.

### 경계

- 이 노트는 레이아웃과 탐색 패턴을 다룬다. d-pad 입력 자체의 전달 메커니즘은 [Android TV는 d-pad/리모컨을 1차 입력으로 가정한다](01_inbox/mobile/android/07_platforms/tv/tv-contracts/android-tv-assumes-d-pad-remote-as-primary-input.md) 가 다룬다.
- 큰 화면 적응형 레이아웃(태블릿/폴더블)의 window size class 모델은 `07_platforms/large-screens` 가 다루며, TV 의 10-foot 기준과는 별개의 문제다.

### 관찰 가능한 신호

TV 에뮬레이터의 접근성 검사기나 레이아웃 인스펙터로 실제 포커스 이동 순서를 시각화해, 의도한 탐색 흐름과 실제 포커스 이동이 일치하는지 확인할 수 있다.

### 공식 문서

- https://developer.android.com/training/tv/start/layouts
- https://developer.android.com/training/tv/playback/browse
