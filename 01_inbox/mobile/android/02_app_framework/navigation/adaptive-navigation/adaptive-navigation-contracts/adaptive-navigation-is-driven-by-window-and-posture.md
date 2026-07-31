# Adaptive navigation은 device type이 아니라 현재 window와 posture로 결정한다

Adaptive navigation은 phone/tablet 같은 device label보다 현재 app window의 크기, posture, resizability, multi-window 상태를 기준으로 판단한다. 같은 device라도 window가 줄어들면 compact navigation이 필요할 수 있다.

Android 16/API 36 이후 large screen 환경에서는 orientation, aspect ratio, resizability 제한에 기대는 설계가 더 약해진다. navigation chrome과 content layout은 runtime window 변화에 대응해야 한다.

공식 문서: [Get started with adaptive apps](https://developer.android.com/develop/adaptive-apps/guides/get-started-with-adaptive-apps), [Adaptive do's and don'ts](https://developer.android.com/develop/adaptive-apps/guides/adaptive-dos-and-donts)
