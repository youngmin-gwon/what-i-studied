# 폴더블 posture는 레이아웃 입력이지 별도 기기 분기가 아니다

상위 문서: [큰 화면 적응 계약](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md)

폴더블 지원은 폴더블 기기인지 확인하는 분기가 아니라 현재 창에 접힘, 힌지, 분리 영역이 있는지 해석하는 일이다. `FoldingFeature`의 state, orientation, occlusionType, isSeparating, bounds가 레이아웃 입력이 된다.

## 왜 중요한가

같은 폴더블도 펼침, 반쯤 접힘, tabletop, book posture, dual-screen spanning에 따라 화면의 안전한 영역과 조작 위치가 달라진다. 힌지를 무시하면 중요한 콘텐츠나 컨트롤이 물리적으로 가려지거나 조작하기 어려운 위치에 놓인다.

## 실무 규칙

- Jetpack WindowManager의 `WindowInfoTracker.windowLayoutInfo()` 흐름을 수명에 맞게 수집한다.
- `HALF_OPENED`와 `isSeparating`은 pane 분리나 컨트롤 위치 조정의 신호로 사용한다.
- 힌지의 정확한 각도를 기반으로 핵심 로직을 만들지 않는다. 공식 API는 각도를 안정적인 계약으로 제공하지 않는다.
- horizontal hinge는 tabletop, vertical hinge는 book posture 설계 가능성을 검토한다.
- `occlusionType`과 `bounds`로 힌지 영역에 콘텐츠를 둘지 피할지 결정한다.

## 관련 문서

- [창 크기 클래스는 기기 종류가 아니라 앱 창을 분류한다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/window-size-class-classifies-app-window-not-device-type.md)
- [적응형 앱 준비도는 창, posture, 입력 테스트로 판단한다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/adaptive-app-readiness-requires-window-posture-input-testing.md)

공식 문서: [Make your app fold aware](https://developer.android.com/develop/adaptive-apps/guides/foldables/make-your-app-fold-aware)

기준일: 2026-07-31. posture 지원 API와 WindowManager extension 요구사항은 Android 버전과 Jetpack WindowManager 버전에 따라 확인한다.
