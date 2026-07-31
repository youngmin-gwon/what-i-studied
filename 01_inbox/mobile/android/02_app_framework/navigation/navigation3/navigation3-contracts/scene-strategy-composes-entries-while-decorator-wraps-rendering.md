# SceneStrategy는 entry를 조합하고 SceneDecorator는 렌더링을 감싼다

Navigation 3에서 SceneStrategy는 back stack의 어떤 entry들을 어떤 scene으로 보여줄지 결정하는 확장 지점이다. Adaptive layout이나 multi-pane 표시처럼 여러 entry를 함께 읽는 정책은 strategy 쪽 책임이다.

SceneDecorator나 entry decorator는 이미 선택된 entry/scene의 rendering 주변에 saveable state, ViewModel store, transition 같은 횡단 관심사를 더하는 지점이다. 표시할 entry를 고르는 정책과 렌더링을 감싸는 정책을 섞지 않는다.

관련 노트: [Metadata and SceneStrategy](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/metadata-and-scene-strategy-carry-display-policy.md), [Scene and adaptive scaffold](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/navigation3-scenes-and-adaptive-scaffolds-solve-different-layout-problems.md).
