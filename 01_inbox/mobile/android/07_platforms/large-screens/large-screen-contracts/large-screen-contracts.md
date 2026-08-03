---
title: "큰 화면 적응 계약"
tags: ["android", "android/platforms"]
---

# 큰 화면 적응 계약

큰 화면 지원은 태블릿용 별도 화면을 만드는 일이 아니라 현재 앱 창, posture, 입력 장치에 맞춰 UI 구조를 바꾸는 계약이다.

## 읽는 순서

1. window size class로 현재 앱 창을 분류한다. 이 값으로 태블릿 같은 기기 종류를 추론하지 않는다.
2. canonical layout과 navigation chrome으로 정보 구조를 적응시킨다.
3. `FoldingFeature`는 창 크기와 별개의 posture/layout 입력으로 합성한다.
4. keyboard, pointer, stylus와 drag and drop을 핵심 과업별로 검증한다.
5. PiP와 desktop windowing은 별도의 lifecycle/windowing 계약으로 검증한다.

## 경계

- size class는 사용 가능한 창 영역, posture는 창 안의 물리적 분리나 가림을 설명한다.
- adaptive structure는 pane과 navigation 배치를 정하지만 task, back stack, caption bar를 소유하지 않는다.
- 품질 등급은 특정 태블릿 한 대의 스크린샷이 아니라 창 크기, 입력, posture, 멀티태스킹 테스트 결과로 판정한다.

## 정본 노트
- [창 크기 클래스는 기기 종류가 아니라 앱 창을 분류한다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/window-size-class-classifies-app-window-not-device-type.md)
- [적응형 레이아웃은 같은 화면을 늘리는 것이 아니라 구조를 바꾼다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/adaptive-layout-changes-structure-not-scale.md)
- [큰 화면 내비게이션은 목적지 중요도와 창 폭에 따라 chrome을 바꾼다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-navigation-changes-chrome-by-window-width.md)
- [폴더블 posture는 레이아웃 입력이지 별도 기기 분기가 아니다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/foldable-posture-is-layout-input-not-device-category.md)
- [PiP는 백그라운드 UI가 아니라 연속 시청을 위한 멀티윈도우 모드다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/picture-in-picture-is-continuity-mode-not-background-ui.md)
- [드래그 앤 드롭은 창 사이 데이터 이동 계약이다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/drag-and-drop-is-cross-window-data-contract.md)
- [키보드, 포인터, 스타일러스는 큰 화면의 기본 입력이다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/keyboard-pointer-and-stylus-are-primary-large-screen-inputs.md)
- [적응형 앱 준비도는 창, posture, 입력 테스트로 판단한다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/adaptive-app-readiness-requires-window-posture-input-testing.md)

검증일: 2026-08-03. [Use window size classes](https://developer.android.com/develop/adaptive-apps/guides/use-window-size-classes), [Adaptive app quality](https://developer.android.com/docs/quality-guidelines/adaptive-app-quality)
