---
title: "데스크톱 윈도잉에서는 앱 창이 자유롭게 변한다"
tags: ["android", "android/platforms"]
---

# 데스크톱 윈도잉에서는 앱 창이 자유롭게 변한다

상위 문서: [데스크톱 윈도잉과 멀티태스킹 계약](01_inbox/mobile/android/07_platforms/large-screens/windowing-multitasking-contracts/windowing-multitasking-contracts.md)

Desktop windowing은 Android 태블릿이나 ChromeOS류 환경에서 앱이 고정 전체 화면이 아니라 resizable window로 실행되는 모드다. 사용자는 여러 앱을 나란히 두고 창 크기, 위치, 입력 방식을 계속 바꿀 수 있다.

## 실무 규칙

- 화면은 시작 시 크기가 아니라 현재 window bounds 변화에 반응해야 한다.
- orientation lock, aspect ratio 제한, `resizeableActivity=false`로 데스크톱 대응을 회피하지 않는다.
- Android 16(API 36)을 target하는 앱은 sw600dp 이상 큰 화면에서 방향, 종횡비, resizable 제한이 무시될 수 있으므로 adaptive layout을 기본 전제로 둔다.
- 카메라, 지도, 영상처럼 비율에 민감한 surface는 resize 중 preview와 capture 비율을 별도로 검증한다.
- precise pointer가 활성화된 환경에서는 touch-first UI보다 조밀한 정보 배치와 hover affordance를 검토한다.

## 관련 문서

- [창 크기 클래스는 기기 종류가 아니라 앱 창을 분류한다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/window-size-class-classifies-app-window-not-device-type.md)
- [키보드, 포인터, 스타일러스는 큰 화면의 기본 입력이다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/keyboard-pointer-and-stylus-are-primary-large-screen-inputs.md)

공식 문서: [Support desktop windowing](https://developer.android.com/develop/adaptive-apps/guides/support-desktop-windowing), [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)
