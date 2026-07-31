# 1 `MyBenefitWindowAdaptivity.kt`

상위 노트: [[06-각-파일의-역할]]

경로:

```text
core/designsystem/src/main/java/com/benefit/virtualmate/core/designsystem/adaptive/MyBenefitWindowAdaptivity.kt
```

역할:

- 현재 app window 상태를 앱 내부 모델로 표현합니다.
- width size class, height size class, window profile, posture, window fold, layout metrics를 한곳에 묶습니다.
- 화면별 layout variant를 직접 결정하지 않습니다.

주요 값:

```kotlin
data class MyBenefitWindowAdaptivity(
    val widthSizeClass: MyBenefitWindowWidthSizeClass,
    val heightSizeClass: MyBenefitWindowHeightSizeClass,
    val windowProfile: MyBenefitWindowProfile,
    val windowPosture: MyBenefitWindowPosture,
    val windowFold: MyBenefitWindowFold,
    val layoutMetrics: MyBenefitLayoutMetrics,
)
```

`windowProfile`은 기기 orientation이 아닙니다. 현재 app window의 width/height size class 조합을 UI가 쓰기 좋게 정규화한 값입니다.
예를 들어 휴대폰 가로 화면은 width만 보면 `Expanded`일 수 있지만, height가 `Compact`이면
`CompactLandscape`로 분류합니다.

중요한 원칙:

```text
MyBenefitWindowAdaptivity
- 현재 window의 사실 정보

MainShellAdaptivePolicy
- main shell이 compact/expanded 중 무엇인지 결정

각 feature의 AdaptiveLayoutPolicy
- 해당 화면이 phone/tablet/foldable 정보를 어떤 화면 variant로 해석할지 결정
```

즉, tablet이나 foldable이라고 해서 core design system이 자동으로 좌우 pane을 만들지 않습니다. 화면마다 목적이 다르므로
layout variant는 feature가 fallback을 포함해 직접 결정합니다.

---
