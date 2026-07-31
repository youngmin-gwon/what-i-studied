# compositionLocalOf와 staticCompositionLocalOf

상위 노트: [jetpack-compose-compositionlocal-and-designsystem-locals](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/jetpack-compose-compositionlocal-and-designsystem-locals.md)

Compose에는 두 가지 생성 API가 있습니다.

| API                        | 특징                                                | 사용 기준                              |
|:---------------------------|:--------------------------------------------------|:-----------------------------------|
| `compositionLocalOf`       | 값을 읽은 위치를 추적하고, 값이 바뀌면 읽은 곳 중심으로 recomposition    | 값이 자주 바뀌거나 세밀한 invalidation이 필요할 때 |
| `staticCompositionLocalOf` | 읽은 위치를 추적하지 않고 provider content 단위로 recomposition | theme, metrics처럼 자주 바뀌지 않는 값       |

현재 adaptive 관련 값은 대부분 window 변화가 있을 때만 바뀝니다. 화면 회전, resize, fold/unfold 같은 이벤트에서는 subtree 전체가 다시
계산되어도 괜찮습니다.

그래서 다음 값들은 `staticCompositionLocalOf`를 사용합니다.

```kotlin
LocalMyBenefitWindowAdaptivity
LocalMyBenefitLayoutMetrics
LocalMyBenefitWindowPosture
LocalMyBenefitWindowFold
```

각 Local은 provider가 없을 때 사용할 fallback 값을 내부에 가지고 있습니다. 이 fallback은 실제 앱 런타임 값을 대신하는 정책이 아니라,
preview/test 또는 provider 누락 상황에서 화면이 즉시 깨지지 않도록 하는 기본값입니다.

반면 `LocalMyBenefitContentInsets`는 `compositionLocalOf`를 사용합니다.

```kotlin
LocalMyBenefitContentInsets
```

이 값은 compact main shell의 floating toolbar 높이처럼 렌더링 후 측정되는 값과 연결됩니다. toolbar 크기 측정 후 scrollable
content padding이 바뀔 수 있으므로 일반 `compositionLocalOf`가 더 자연스럽습니다.

---
