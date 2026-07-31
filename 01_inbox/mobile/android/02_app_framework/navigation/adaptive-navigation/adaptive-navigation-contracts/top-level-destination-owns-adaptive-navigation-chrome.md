# Top-level destination은 adaptive navigation chrome의 단위다

Top-level destination은 bottom bar, navigation rail, drawer 같은 app chrome에 노출되는 가장 큰 이동 단위다. Adaptive UI에서는 chrome 모양이 window 조건에 따라 바뀌어도 선택된 destination의 의미는 그대로 유지되어야 한다.

Compact window에서는 navigation bar가 자연스럽고, expanded window에서는 rail이나 drawer가 더 적합할 수 있다. 하지만 chrome 전환이 각 destination의 back stack을 초기화하거나 route 의미를 바꾸면 안 된다.

따라서 adaptive chrome은 현재 window와 posture에 반응하는 표시 정책이고, destination과 stack state는 앱 navigation state로 별도 관리한다.

공식 문서: [Build adaptive navigation](https://developer.android.com/develop/adaptive-apps/guides/build-adaptive-navigation)
