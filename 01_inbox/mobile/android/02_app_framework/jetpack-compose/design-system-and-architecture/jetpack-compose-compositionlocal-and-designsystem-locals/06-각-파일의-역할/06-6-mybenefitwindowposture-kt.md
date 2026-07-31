# 6 `MyBenefitWindowPosture.kt`

상위 노트: [[06-각-파일의-역할]]

경로:

```text
core/designsystem/src/main/java/com/benefit/virtualmate/core/designsystem/adaptive/MyBenefitWindowPosture.kt
```

역할:

- tabletop/book 같은 window posture를 앱 내부 용어로 표현합니다.
- feature 모듈이 `FoldingFeature`, `Posture`, `WindowManager` 타입을 직접 몰라도 되게 합니다.
- fold/hinge가 화면을 나누는지, 가리는지, bounds만 있는지는 `MyBenefitWindowFold`가 표현합니다.
- tablet, desktop, ChromeOS window처럼 넓은 화면은 posture가 아니라 width/height size class로 표현합니다.

예:

```text
Regular
- tabletop/book이 아닌 일반 window
- tablet, desktop window도 posture 관점에서는 Regular

Tabletop
- 반쯤 열린 가로 fold/hinge가 위/아래 영역을 나누는 상태

Book
- 반쯤 열린 세로 fold/hinge가 좌/우 영역을 나누는 상태
```

이 값은 "기기 모델명"이 아닙니다. 같은 Galaxy Fold라도 펼침, 회전, multi-window 상태에 따라 값이 바뀔 수 있습니다.

---
