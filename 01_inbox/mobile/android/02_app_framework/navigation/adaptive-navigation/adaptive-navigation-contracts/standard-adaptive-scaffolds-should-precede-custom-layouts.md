# 표준 adaptive scaffold를 먼저 검토하고 custom layout은 명시적 이유가 있을 때 둔다

Material 3 Adaptive library는 navigation suite, list-detail, supporting pane 같은 표준 scaffold를 제공한다. 이들은 window size class와 posture에 맞춰 흔한 adaptive UI 문제를 이미 모델링한다.

Custom layout은 표준 scaffold가 표현하지 못하는 product-specific structure가 있을 때 선택한다. 표준 component와 같은 상태를 중복 소유하거나, window 변화마다 별도 route tree를 만들어야 한다면 custom layout의 비용을 다시 검토한다.

공식 문서: [Build adaptive navigation](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation), [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)
