# 8 `LocalMyBenefitWindowPosture.kt`

상위 노트: [[06-각-파일의-역할]]

경로:

```text
core/designsystem/src/main/java/com/benefit/virtualmate/core/designsystem/adaptive/LocalMyBenefitWindowPosture.kt
```

역할:

- 현재 posture만 빠르게 읽을 수 있게 합니다.
- `LocalMyBenefitWindowAdaptivity.current.windowPosture`와 같은 의미입니다.

언제 읽나:

- 특정 화면이 posture에 따라 완전히 다른 interaction을 제공해야 할 때
- 예를 들어 camera preview, video player, 측정 화면처럼 hinge 위치가 직접 UI 구조에 영향을 줄 때

일반 화면은 직접 이 값을 읽기보다 화면별 `AdaptiveLayoutPolicy`를 먼저 두는 편이 좋습니다.

---
