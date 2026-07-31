# 이 프로젝트의 adaptive 값 흐름

상위 노트: [[jetpack-compose-compositionlocal-and-designsystem-locals]]

현재 흐름은 다음과 같습니다.

```text
MyBenefitApp
 └─ ProvideMyBenefitWindowAdaptivity
     ├─ LocalMyBenefitWindowAdaptivity 제공
     ├─ LocalMyBenefitLayoutMetrics 제공
     ├─ LocalMyBenefitWindowPosture 제공
     └─ LocalMyBenefitWindowFold 제공
         ├─ AuthFlow
         └─ MainFlow
             └─ MainAdaptiveShell
                 ├─ CompactMainShell
                 │   └─ LocalMyBenefitContentInsets 제공
                 └─ ExpandedMainShell
                     └─ LocalMyBenefitContentInsets 제공
```

`ProvideMyBenefitWindowAdaptivity`는 app 모듈에 있습니다. 여기에서 제공하는 값이 실제 런타임 값입니다.

```text
app/src/main/java/com/benefit/virtualmate/member/ui/adaptive/MyBenefitWindowAdaptivityProvider.kt
```

여기에서 AndroidX/Material adaptive 타입을 읽습니다. 화면 크기, 회전, multi-window, fold/unfold 등으로 adaptive 정보가 바뀌면 provider가 다시 composition되면서 하위 tree에 새 값을 제공합니다.

```text
WindowSizeClass
Posture
hinge information
```

그리고 core design system의 앱 전용 모델로 변환합니다.

```text
MyBenefitWindowAdaptivity
MyBenefitWindowPosture
MyBenefitWindowFold
MyBenefitLayoutMetrics
```

이렇게 분리한 이유는 feature 모듈이 AndroidX WindowManager나 Material adaptive 타입을 직접 몰라도 되게 하기 위해서입니다.

---
