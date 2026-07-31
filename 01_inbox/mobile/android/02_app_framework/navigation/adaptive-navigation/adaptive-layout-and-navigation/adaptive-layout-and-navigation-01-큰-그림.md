# 큰 그림

상위 노트: [adaptive-layout-and-navigation](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-layout-and-navigation.md)

Adaptive app은 phone, tablet, foldable, ChromeOS, desktop window, connected display, car, TV, XR 등 다양한 form factor에서 앱 window 상태에 맞게 UI 구조를 조정하는 앱입니다.

공식 문서의 핵심 관점은 다음입니다.

- 기기 종류보다 **앱 window 크기**를 기준으로 판단합니다.
- multi-window, split screen, freeform window, fold/unfold로 window 크기는 앱 실행 중에도 바뀔 수 있습니다.
- 좁은 화면에서는 한 번에 적은 콘텐츠를 보여주고, 넓은 화면에서는 navigation rail, drawer, list-detail, supporting pane 같은 구조로 더 많은 콘텐츠를 함께 보여줍니다.
- layout은 단순히 늘리거나 줄이는 것이 아니라, 필요한 경우 component 배치와 정보 밀도를 바꿉니다.

관련 문서:

- [Get started with adaptive apps](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps)
- [Support different display sizes](https://developer.android.com/develop/adaptive-apps/guides/support-different-display-sizes)
- [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)

---
