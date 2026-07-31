# 7 `MyBenefitWindowFold.kt`

상위 노트: [[06-각-파일의-역할]]

경로:

```text
core/designsystem/src/main/java/com/benefit/virtualmate/core/designsystem/adaptive/MyBenefitWindowFold.kt
```

역할:

- fold/hinge bounds가 있는지 표현합니다.
- fold/hinge 방향이 가로인지 세로인지 표현합니다.
- fold/hinge가 logical display area를 나누는지 표현합니다.
- fold/hinge가 실제 픽셀을 가리거나 사용하기 어려운 영역을 만드는지 표현합니다.

예:

```text
tablet / desktop
- windowPosture = Regular
- windowFold = None

쫙 펼쳐진 foldable
- windowPosture = Regular
- windowFold.orientation = Vertical 또는 Horizontal
- windowFold.isSeparating = false
- windowFold.isOccluding = false

book posture
- windowPosture = Book
- windowFold.orientation = Vertical
- windowFold.isSeparating = true

tabletop posture
- windowPosture = Tabletop
- windowFold.orientation = Horizontal
- windowFold.isSeparating = true
```

이 값만으로 layout을 자동 분리하지 않습니다. 각 feature의 `AdaptiveLayoutPolicy`가 해당 화면에 실제로 이점이 있을 때만 사용합니다.

---
