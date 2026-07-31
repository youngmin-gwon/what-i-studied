# 적응형 레이아웃은 같은 화면을 늘리는 것이 아니라 구조를 바꾼다

상위 문서: [큰 화면 적응 계약](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-contracts.md)

Adaptive layout은 compact 화면을 큰 화면에 단순 확대하는 방식이 아니다. 창이 넓어지면 navigation chrome, content pane, 보조 도구, density, modal 위치 같은 화면 구조를 바꿔야 한다.

## 왜 중요한가

큰 화면에서 한 열 UI를 가운데 늘려 놓으면 정보량은 늘지 않고 이동 거리만 증가한다. 반대로 너무 이른 two-pane 전환은 작은 height, 분할 화면, 폴더블 posture에서 조작성을 해칠 수 있다.

## 실무 규칙

- list-detail, supporting pane, feed 같은 canonical layout을 먼저 검토한다.
- compact에서는 한 번에 하나의 주요 작업에 집중시키고, expanded 이상에서는 관련 정보를 함께 보여준다.
- button, dialog, text field는 전체 폭을 무조건 채우지 말고 기능적으로 적절한 최대 폭을 둔다.
- orientation lock이나 aspect ratio 제한으로 레이아웃 문제를 숨기지 않는다.

## 관련 문서

- [창 크기 클래스는 기기 종류가 아니라 앱 창을 분류한다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/window-size-class-classifies-app-window-not-device-type.md)
- [큰 화면 내비게이션은 목적지 중요도와 창 폭에 따라 chrome을 바꾼다](01_inbox/mobile/android/07_platforms/large-screens/large-screen-contracts/large-screen-navigation-changes-chrome-by-window-width.md)
- [Compose 상태와 Effect 계약](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md)

공식 문서: [Get started with adaptive apps](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps), [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)
