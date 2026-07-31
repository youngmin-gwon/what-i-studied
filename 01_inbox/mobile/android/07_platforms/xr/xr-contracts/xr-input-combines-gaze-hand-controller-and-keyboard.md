# XR 입력은 gaze, hand, controller, keyboard를 함께 설계한다

상위 문서: [Android XR 계약](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md)

XR 입력은 터치 이벤트를 공간으로 옮긴 것이 아니다. 사용자는 시선, 손, 컨트롤러, 음성, 키보드, 포인터를 상황에 따라 섞어 사용하므로 focus, selection, activation, text input을 여러 입력 경로에서 검증해야 한다.

## 실무 규칙

- 시선 또는 포인터가 머무는 hover/focus 상태를 명확히 만든다.
- 손이나 컨트롤러로 누르기 어려운 작은 target을 공간 안에 배치하지 않는다.
- text 입력은 가상 키보드, 물리 키보드, 음성 입력 가능성을 함께 고려한다.
- 같은 명령이 2D panel, orbiter, controller shortcut 중 어디에 있어야 하는지 역할을 나눈다.

## 관련 문서

- [키보드, 포인터, 스타일러스는 큰 화면의 기본 입력이다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/keyboard-pointer-and-stylus-are-primary-large-screen-inputs.md)
- [XR 품질은 성능, 편안함, 안전을 기능 요구사항으로 포함한다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-quality-includes-performance-comfort-and-safety.md)
