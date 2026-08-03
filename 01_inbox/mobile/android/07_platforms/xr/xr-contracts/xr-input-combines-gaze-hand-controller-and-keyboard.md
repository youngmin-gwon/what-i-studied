---
title: xr-input-combines-gaze-hand-controller-and-keyboard
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-03 18:15:26 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## XR 입력은 gaze, hand, controller, keyboard 를 함께 설계한다

상위 문서: [Android XR 계약](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md)

XR 입력은 터치 이벤트를 공간으로 옮긴 것이 아니다. Android XR 의 기본 자연 입력인 eye tracking 과 gesture 또는 raycast hand 를 먼저 보장하고, 컨트롤러, 키보드, 마우스 같은 주변 입력으로 확장한다. focus, selection, activation, text input 을 각 경로에서 검증해야 한다.

### 실무 규칙

- 시선 또는 포인터가 머무는 hover/focus 상태를 명확히 만든다.
- 손이나 컨트롤러로 누르기 어려운 작은 target 을 공간 안에 배치하지 않는다.
- text 입력은 가상 키보드, 물리 키보드, 음성 입력 가능성을 함께 고려한다.
- 같은 명령이 2D panel, orbiter, controller shortcut 중 어디에 있어야 하는지 역할을 나눈다.
- controller 가 없어도 핵심 과업을 완료할 수 있어야 하며 controller 는 선택적 강화 입력으로 둔다.

### 관련 문서

- [키보드, 포인터, 스타일러스는 큰 화면의 기본 입력이다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/keyboard-pointer-and-stylus-are-primary-large-screen-inputs.md)
- [XR 품질은 성능, 편안함, 안전을 기능 요구사항으로 포함한다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-quality-includes-performance-comfort-and-safety.md)

공식 문서: [Android XR app quality](https://developer.android.com/docs/quality-guidelines/android-xr)

검증일: 2026-08-03. headset 과 wired XR glasses 기준의 기본 입력 계약이며 audio/display glasses 지침은 preview 범위를 별도로 확인한다.
