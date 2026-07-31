# Window와 Resizability

상위 노트: [adaptive-layout-and-navigation](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-layout-and-navigation.md)

Adaptive layout의 기본 전제는 앱이 여러 window 크기에서 정상적으로 동작해야 한다는 것입니다.

공식 문서들이 반복해서 강조하는 내용:

- 특정 orientation에 고정하지 않습니다.
- 특정 aspect ratio에 강하게 의존하지 않습니다.
- resize 가능한 window를 정상 상태로 봅니다.
- multi-window mode에서 앱이 작아지거나 커지는 상황을 고려합니다.
- UI state는 configuration/window 변화에 견딜 수 있어야 합니다.

Android 16 / API 36 이상을 target하는 방향에서는 large screen에서 orientation, aspect ratio, resizability 제한에 기대는 설계가 점점 더 약해집니다. 따라서 처음부터 adaptive/resizable UI로 설계하는 편이 안전합니다.

관련 문서:

- [Support multi-window mode](https://developer.android.com/develop/adaptive-apps/guides/support-multi-window-mode)
- [App orientation, aspect ratio, and resizability](https://developer.android.com/develop/adaptive-apps/guides/app-orientation-aspect-ratio-resizability)

---
