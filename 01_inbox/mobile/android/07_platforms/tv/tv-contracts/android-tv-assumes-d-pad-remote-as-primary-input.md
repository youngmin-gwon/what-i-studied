---
title: "Android TV는 d-pad/리모컨을 1차 입력으로 가정한다"
tags: ["android", "android/platforms"]
---

# Android TV는 d-pad/리모컨을 1차 입력으로 가정한다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](01_inbox/mobile/android/07_platforms/android-platforms-and-form-factors.md)
관련 지도: [Android TV 계약](01_inbox/mobile/android/07_platforms/tv/tv-contracts/tv-contracts.md)

## 핵심 정의

Android TV 기기는 터치스크린이 없는 것을 기본 전제로 한다. 사용자는 리모컨의 방향키(d-pad)와 확인/뒤로 버튼으로만 화면을 조작하며, 일부 기기에 마우스나 터치패드형 리모컨이 있어도 이는 보조 입력이다. 앱은 모든 클릭 가능한 요소를 d-pad만으로 도달 가능하게 설계해야 한다.

## 메커니즘

d-pad 입력은 `KeyEvent`(`KEYCODE_DPAD_UP/DOWN/LEFT/RIGHT/CENTER`)로 전달된다. View 시스템은 방향키 입력에 따라 포커스를 다음 뷰로 옮기는 기본 알고리즘(뷰의 기하학적 위치 기반)을 갖고 있지만, 복잡한 레이아웃에서는 의도한 대로 포커스가 이동하지 않을 수 있다. 이 경우 `android:nextFocusUp`/`Down`/`Left`/`Right` 같은 속성이나 Compose의 `FocusRequester`로 명시적 포커스 순서를 지정해야 한다.

## 판단 기준

- 화면의 모든 상호작용 가능한 요소가 d-pad만으로 도달 가능한지 방향키만으로 앱을 조작하는 테스트를 반드시 거친다.
- 제스처(스와이프, 핀치 줌) 기반 UI를 TV로 그대로 이식하지 않는다. 대응하는 d-pad 조작(좌우 이동, 확인 버튼)으로 재설계해야 한다.
- 터치 기반 시각적 피드백(리플 효과 등)보다 포커스 상태(테두리 강조, 스케일 변화)가 더 중요한 시각 신호다. 포커스가 어디 있는지 항상 명확히 보여야 한다.

## 경계

- 이 노트는 입력 모델까지 다룬다. 화면 레이아웃과 포커스 탐색 패턴 자체는 [10-foot UI는 포커스 기반 탐색을 요구한다](01_inbox/mobile/android/07_platforms/tv/tv-contracts/10-foot-ui-requires-focus-based-navigation.md)가 다룬다.
- 리모컨 이외의 물리 입력 장치(게임패드 등)에 대한 일반 모델은 `04_system_services/device-capabilities/input-accessibility-contracts`가 다룬다.

## 관찰 가능한 신호

Android TV 에뮬레이터 또는 실기기에서 리모컨(또는 방향키만 사용하는 하드웨어 키보드)만으로 앱을 조작해보면, 포커스가 갇히거나 도달 불가능한 요소를 즉시 발견할 수 있다.

## 공식 문서

- https://developer.android.com/training/tv/start/start
- https://developer.android.com/training/tv/start/navigation
