---
title: foldable-posture-is-layout-input-not-device-category
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-03 18:15:32 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## 폴더블 posture 는 레이아웃 입력이지 별도 기기 분기가 아니다

상위 문서: [큰 화면 적응 계약](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md)

폴더블 지원은 폴더블 기기인지 확인하는 분기가 아니라 현재 창에 접힘, 힌지, 분리 영역이 있는지 해석하는 일이다. `FoldingFeature` 의 state, orientation, occlusionType, isSeparating, bounds 가 레이아웃 입력이 된다.

### 왜 중요한가

같은 폴더블도 펼침, 반쯤 접힘, tabletop, book posture, dual-screen spanning 에 따라 화면의 안전한 영역과 조작 위치가 달라진다. 힌지를 무시하면 중요한 콘텐츠나 컨트롤이 물리적으로 가려지거나 조작하기 어려운 위치에 놓인다.

### 실무 규칙

- Jetpack WindowManager 의 `WindowInfoTracker.windowLayoutInfo()` 흐름을 수명에 맞게 수집한다.
- `HALF_OPENED` 와 `isSeparating` 은 pane 분리나 컨트롤 위치 조정의 신호로 사용한다.
- 힌지의 정확한 각도를 기반으로 핵심 로직을 만들지 않는다. 공식 API 는 각도를 안정적인 계약으로 제공하지 않는다.
- horizontal hinge 는 tabletop, vertical hinge 는 book posture 설계 가능성을 검토한다.
- `occlusionType` 과 `bounds` 로 힌지 영역에 콘텐츠를 둘지 피할지 결정한다.

### 버전 경계

현재 posture 는 `windowLayoutInfo()` 로 관찰한다. 기기가 tabletop posture 를 지원할 수 있는지 동기적으로 질의하는 `supportedPostures` 는 Android 15(API 35) 이상이면서 WindowManager Extensions 6 이상인 별도 조건이다. 지원 가능 여부와 현재 `HALF_OPENED` 상태를 같은 값으로 취급하지 않는다.

### 관련 문서

- [창 크기 클래스는 기기 종류가 아니라 앱 창을 분류한다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/window-size-class-classifies-app-window-not-device-type.md)
- [적응형 앱 준비도는 창, posture, 입력 테스트로 판단한다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/adaptive-app-readiness-requires-window-posture-input-testing.md)

공식 문서: [Make your app fold aware](https://developer.android.com/develop/adaptive-apps/guides/foldables/make-your-app-fold-aware)

검증일: 2026-08-03. posture 지원 API 와 WindowManager extension 요구사항은 [Make your app fold aware](https://developer.android.com/develop/adaptive-apps/guides/foldables/make-your-app-fold-aware) 에서 다시 확인한다.
