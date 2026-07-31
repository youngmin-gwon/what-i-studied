# Local이라는 이름

상위 노트: [[jetpack-compose-compositionlocal-and-designsystem-locals]]

공식 문서에서도 `CompositionLocal` 값은 보통 `Local` prefix를 붙입니다.

```kotlin
LocalContext
LocalDensity
LocalLayoutDirection
LocalContentColor
```

이 프로젝트도 같은 관례를 따릅니다.

```kotlin
LocalMyBenefitWindowAdaptivity
LocalMyBenefitLayoutMetrics
LocalMyBenefitWindowPosture
LocalMyBenefitWindowFold
LocalMyBenefitContentInsets
```

`Local`은 "전역 singleton"이라는 뜻이 아닙니다. 더 정확히는 "현재 Compose tree 위치에서 가장 가까운 provider가 준 값"입니다.

같은 앱 안에서도 tree 위치가 다르면 값이 다를 수 있습니다.

```text
App root
 └─ Provider A
     ├─ Screen 1 -> A 값 읽음
     └─ Provider B
         └─ Screen 2 -> B 값 읽음
```

### 2.1 Local과 Fallback의 차이

`LocalMyBenefitWindowAdaptivity`는 fallback 값 자체가 아닙니다. 이것은 Compose tree에서 window adaptivity를 읽기 위한
`CompositionLocal` key입니다.

정확한 관계는 다음과 같습니다.

```kotlin
private val fallbackMyBenefitWindowAdaptivity = MyBenefitWindowAdaptivity(...)

val LocalMyBenefitWindowAdaptivity = staticCompositionLocalOf {
    fallbackMyBenefitWindowAdaptivity
}
```

역할을 나누면 다음과 같습니다.

```text
LocalMyBenefitWindowAdaptivity
- 하위 Composable이 현재 window adaptivity를 읽는 통로

fallbackMyBenefitWindowAdaptivity
- provider가 없을 때 preview/test가 깨지지 않도록 쓰는 기본값

ProvideMyBenefitWindowAdaptivity
- 실제 앱 런타임에서 현재 window 상태를 계산해 Local에 넣는 provider
```

따라서 공개 API 이름은 `Local~`을 유지합니다. 소비자는 fallback을 읽는 것이 아니라 "현재 Composition에 제공된 값"을 읽습니다.
fallback은 provider가 없을 때만 쓰는 내부 구현 detail입니다.

---
