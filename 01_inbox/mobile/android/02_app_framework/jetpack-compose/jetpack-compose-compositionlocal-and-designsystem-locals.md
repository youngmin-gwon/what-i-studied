# Compose CompositionLocal과 이 프로젝트의 Local 값

이 문서는 Jetpack Compose의 `CompositionLocal` 개념과, 현재 design system에 있는 `LocalMyBenefit*` 값들이 어떤 역할을 하는지
정리합니다.

관련 공식 문서:

- [CompositionLocal in Jetpack Compose](https://developer.android.com/develop/ui/compose/compositionlocal)
- [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
- [Architecture layering in Compose](https://developer.android.com/develop/ui/compose/architecture)

---

## 1. CompositionLocal이란?

Compose에서 기본 데이터 흐름은 명시적인 parameter 전달입니다.

```kotlin
@Composable
fun Parent() {
    Child(color = Color.Red)
}

@Composable
fun Child(color: Color) {
    Text("Hello", color = color)
}
```

이 방식은 의존성이 명확합니다. 하지만 앱 전체에서 매우 자주 쓰이고, 중간 계층이 굳이 알 필요 없는 값은 매번 parameter로 넘기면 코드가 지저분해집니다.

대표 예시는 다음과 같습니다.

```text
theme color
typography
layout direction
Android Context
현재 adaptive layout 정보
현재 overlay inset 정보
```

`CompositionLocal`은 이런 값을 Compose tree 아래로 암묵적으로 전달하는 도구입니다.

```kotlin
CompositionLocalProvider(LocalValue provides value) {
    SomeScreen()
}
```

아래쪽 Composable은 가장 가까운 provider가 제공한 값을 읽습니다.

```kotlin
val value = LocalValue.current
```

Flutter 경험으로 보면 `InheritedWidget`, `Provider`, `Theme.of(context)`와 비슷한 역할입니다. 다만 Compose에서는
`BuildContext`를 넘기지 않고, `LocalSomething.current` 형태로 현재 Composition의 값을 읽습니다.

---

## 2. Local이라는 이름

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

## 3. 언제 CompositionLocal을 쓰나?

CompositionLocal은 아무 값이나 숨겨서 전달하는 도구가 아닙니다.

적합한 경우:

- 앱 또는 하위 tree 전체에 넓게 적용되는 값
- 중간 Composable이 굳이 몰라도 되는 환경값
- 화면 대부분이 공통으로 읽을 수 있는 design system 값
- preview/test 기본값을 둘 수 있는 값

부적합한 경우:

- 특정 화면의 `ViewModel`
- 버튼 클릭 callback
- form field 값
- 한두 Composable만 쓰는 임시 상태
- 명시적으로 parameter로 넘기는 편이 더 읽기 쉬운 값

이 프로젝트에서 `ViewModel`을 `Local`로 만들지 않는 이유도 여기에 있습니다. `ViewModel`은 화면 상태와 이벤트 처리의 구체적인 owner입니다. 이를
Local로 숨기면 어떤 UI가 어떤 상태에 의존하는지 추적하기 어려워집니다.

---

## 4. compositionLocalOf와 staticCompositionLocalOf

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

## 5. 이 프로젝트의 adaptive 값 흐름

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

## 6. 각 파일의 역할

### 6.1 `MyBenefitWindowAdaptivity.kt`

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

### 6.2 `MyBenefitWindowProfile.kt`

경로:

```text
core/designsystem/src/main/java/com/benefit/virtualmate/core/designsystem/adaptive/MyBenefitWindowProfile.kt
```

역할:

- width/height size class 조합을 앱에서 바로 쓰기 좋은 profile로 정리합니다.
- Android orientation 값이 아니라 현재 app window 모양을 표현합니다.
- feature나 shell이 매번 `width == Compact || height == Compact` 같은 조건을 반복하지 않게 합니다.

대표 값:

```text
CompactPortrait
- 폭이 좁고 높이는 충분한 일반 휴대폰 세로 화면

CompactLandscape
- 폭은 넓을 수 있지만 높이가 낮은 휴대폰 가로 화면 또는 얇은 freeform window

CompactConstrained
- 폭과 높이가 모두 좁은 split-screen/freeform window

Medium / Expanded / Large / ExtraLarge
- 높이가 충분하고 폭 구간에 따라 확장 가능한 window
```

---

### 6.3 `LocalMyBenefitWindowAdaptivity.kt`

경로:

```text
core/designsystem/src/main/java/com/benefit/virtualmate/core/designsystem/adaptive/LocalMyBenefitWindowAdaptivity.kt
```

역할:

- `MyBenefitWindowAdaptivity`를 Compose tree 전체에 전달합니다.
- 앱 전체 adaptive 상태를 읽는 최상위 Local입니다.

제공 위치:

```text
ProvideMyBenefitWindowAdaptivity
```

읽는 위치 예:

```text
MainShellAdaptivePolicy
DashboardAdaptiveLayoutPolicy
각 feature의 layout policy
```

이 값은 "현재 adaptive 환경을 화면별 정책이 어떻게 해석할지"가 필요할 때 읽습니다.

---

### 6.4 `MyBenefitLayoutMetrics.kt`

경로:

```text
core/designsystem/src/main/java/com/benefit/virtualmate/core/designsystem/adaptive/MyBenefitLayoutMetrics.kt
```

역할:

- window size에 따라 달라지는 화면 padding과 gap을 표현합니다.
- `MyBenefitSpacing` 같은 원시 token을 화면 의미 단위로 매핑합니다.
- metrics 선택은 raw `widthDp`가 아니라 `MyBenefitWindowProfile`을 기준으로 합니다.
- 그래서 휴대폰 가로 화면처럼 width는 넓지만 height가 낮은 window는 compact metrics를 사용합니다.

차이:

```text
MyBenefitSpacing
- 8.dp, 16.dp, 24.dp 같은 원시 spacing token

MyBenefitLayoutMetrics
- screenHorizontalPadding, contentGap, paneGap 같은 화면 의미 token
```

feature 화면은 가능하면 `16.dp`를 직접 쓰지 않고 `LocalMyBenefitLayoutMetrics.current`를 읽습니다.

---

### 6.5 `LocalMyBenefitLayoutMetrics.kt`

경로:

```text
core/designsystem/src/main/java/com/benefit/virtualmate/core/designsystem/adaptive/LocalMyBenefitLayoutMetrics.kt
```

역할:

- 현재 window size에 맞는 `MyBenefitLayoutMetrics`를 하위 화면에 전달합니다.
- UI 코드에서 가장 자주 쓰는 adaptive 값이라 `LocalMyBenefitWindowAdaptivity.current.layoutMetrics`와 별도로 제공합니다.

읽는 위치 예:

```kotlin
val layoutMetrics = LocalMyBenefitLayoutMetrics.current
```

사용 예:

```kotlin
Arrangement.spacedBy(layoutMetrics.contentGap)
Modifier.padding(layoutMetrics.contentGap)
```

---

### 6.6 `MyBenefitWindowPosture.kt`

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

### 6.7 `MyBenefitWindowFold.kt`

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

### 6.8 `LocalMyBenefitWindowPosture.kt`

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

### 6.9 `LocalMyBenefitWindowFold.kt`

경로:

```text
core/designsystem/src/main/java/com/benefit/virtualmate/core/designsystem/adaptive/LocalMyBenefitWindowFold.kt
```

역할:

- 현재 fold/hinge만 빠르게 읽을 수 있게 합니다.
- `LocalMyBenefitWindowAdaptivity.current.windowFold`와 같은 의미입니다.

일반 화면은 이 값을 직접 읽기보다 화면별 `AdaptiveLayoutPolicy`에서 읽는 편이 좋습니다.

---

### 6.10 `MyBenefitContentInsets.kt`

경로:

```text
core/designsystem/src/main/java/com/benefit/virtualmate/core/designsystem/layout/MyBenefitContentInsets.kt
```

역할:

- layout metrics가 아니라 runtime overlay inset을 표현합니다.
- floating toolbar처럼 실제 크기를 측정해야 알 수 있는 UI 여백을 하위 화면에 전달합니다.

중요한 차이:

```text
screen padding
- 화면 기본 여백
- MyBenefitLayoutMetrics가 담당

content inset
- floating toolbar, navigation chrome 때문에 scroll content가 추가로 피해야 하는 여백
- MyBenefitContentInsets가 담당
```

특히 compact main shell의 floating toolbar는 overlay입니다.

따라서 화면 전체를 위로 밀면 안 됩니다.

```text
잘못된 방식:
전체 화면 Modifier.padding(bottom = toolbarHeight)

의도한 방식:
LazyColumn contentPadding(bottom = toolbarHeight)
```

그래야 content는 floating bar 아래까지 뻗고, 마지막 item만 bar 뒤에 가려지지 않습니다.

---

## 7. 화면에서 사용하는 방식

일반 화면은 `MyBenefitAdaptiveScreen`을 사용합니다.

```kotlin
@Composable
fun SettingsScreen() {
    MyBenefitAdaptiveScreen {
        Text("Settings")
    }
}
```

화면이 tablet/foldable 전용 variant를 제공해야 한다면 feature 안에 policy를 둡니다.

```kotlin
internal object DashboardAdaptiveLayoutPolicy {
    fun resolve(windowAdaptivity: MyBenefitWindowAdaptivity): DashboardLayoutVariant =
        when {
            // dashboard 전용 tablet/foldable 화면이 설계되면 여기에서 명시한다.
            else -> DashboardLayoutVariant.Feed
        }
}
```

이때 core design system은 다음처럼 전역 정답을 강제하지 않습니다.

```kotlin
tablet이면 무조건 좌우 pane
foldable이면 무조건 위아래 또는 좌우 pane
```

대신 각 feature가 자기 화면 목적에 맞는 variant와 fallback을 결정합니다.

---

## 8. 언제 직접 Local을 읽어도 되나?

직접 읽어도 되는 경우:

- spacing/gap이 필요해서 `LocalMyBenefitLayoutMetrics`를 읽는 경우
- 화면별 `AdaptiveLayoutPolicy`가 posture에 따라 variant를 고르는 경우
- app shell처럼 navigation chrome을 직접 결정해야 하는 경우

가능하면 피해야 하는 경우:

- 단순히 화면 padding을 얻기 위해 모든 화면에서 직접 Local을 읽는 것
- feature 화면마다 tablet/foldable 분기를 직접 만드는 것
- `ViewModel`, repository, callback 같은 화면별 의존성을 Local로 숨기는 것

권장 순서:

```text
1. 일반 container가 필요하면 MyBenefitAdaptiveScreen을 사용한다.
2. 화면별 adaptive 차이가 필요하면 feature 안에 AdaptiveLayoutPolicy를 둔다.
3. 간격이 필요하면 LocalMyBenefitLayoutMetrics를 읽는다.
4. 정말 posture별 기능 차이가 필요할 때만 LocalMyBenefitWindowPosture를 읽는다.
5. AndroidX WindowManager 타입은 feature에서 직접 읽지 않는다.
```

---

## 9. 왜 이렇게 나눴나?

파일이 나뉜 이유는 값의 성격이 다르기 때문입니다.

| 파일                          | 성격                               | 예                                    |
|:----------------------------|:---------------------------------|:-------------------------------------|
| `MyBenefitWindowAdaptivity.kt`  | 현재 window 상태를 해석한 adaptive 환경 모델 | width class, height class, profile, posture |
| `MyBenefitWindowProfile.kt` | width/height 조합의 앱 내부 profile       | compact portrait, compact landscape  |
| `MyBenefitLayoutMetrics.kt` | window profile별 spacing/padding 수치 | screen padding, content gap          |
| `MyBenefitWindowPosture.kt` | window posture의 앱 내부 표현           | regular, tabletop, book              |
| `MyBenefitWindowFold.kt`   | fold/hinge의 물리 제약 정보              | orientation, separating, occluding    |
| `MyBenefitContentInsets.kt` | 런타임 overlay 여백                   | floating toolbar 높이                  |
| `Local*.kt`                 | 위 값들을 Compose tree 아래로 전달하는 통로   | `LocalMyBenefitWindowAdaptivity.current` |

이 구분을 유지하면 다음 장점이 있습니다.

- feature 모듈이 AndroidX WindowManager에 직접 묶이지 않습니다.
- core design system이 모든 화면의 layout 정답을 강제하지 않습니다.
- 화면별 adaptive 정책을 feature 안에서 테스트할 수 있습니다.
- preview/test에서 기본값으로 화면을 렌더링할 수 있습니다.
- floating toolbar 같은 runtime overlay와 screen spacing을 섞지 않습니다.

---

## 10. CompositionLocalProvider 및 유사한 스코프 제공 Composable 패턴

`CompositionLocalProvider`는 선언형 UI 트리 구조에서 매우 유용한 도구이지만, 그 특성과 유사한 Composable 제공 패턴들을 제대로 이해해야 의도치 않은 버그와 렌더링 누락을 피할 수 있습니다.

### 10-1. CompositionLocalProvider의 중첩과 값 덮어쓰기 (Overriding & Shadowing)
`CompositionLocalProvider`는 트리 아래로 내려가면서 값을 **오버라이드(Override)**할 수 있습니다. 즉, 하위 트리 내부에서 특정 지역만 다른 환경을 적용하고 싶을 때 유용합니다.

```kotlin
CompositionLocalProvider(LocalContentColor provides Color.Gray) {
    // 1. 여기서는 회색이 나옵니다.
    Text("Gray Text") 
    
    CompositionLocalProvider(LocalContentColor provides Color.Red) {
        // 2. 안쪽 provider가 상위 값을 덮어썼으므로 여기서는 빨간색이 나옵니다.
        Text("Red Text") 
    }
    
    // 3. 다시 바깥 스코프로 나왔으므로 다시 회색이 나옵니다.
    Text("Gray Text Again") 
}
```

### 10-2. 테마 래퍼 패턴 (Theme Composable Wrapper)
실무에서는 `CompositionLocalProvider`를 직접 노출하여 호출하기보다, 프로젝트의 기본 스타일과 속성을 한번에 주입하는 **Theme Composable Wrapper** 형태로 캡슐화하여 사용합니다.

```kotlin
@Composable
fun MyBenefitTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {
    val colors = if (darkTheme) DarkColors else LightColors
    val typography = MyBenefitTypography
    val spacing = MyBenefitSpacing
    
    // 여러 Local을 하나의 Provider 블록에서 한 번에 제공
    CompositionLocalProvider(
        LocalMyBenefitColors provides colors,
        LocalMyBenefitTypography provides typography,
        LocalMyBenefitSpacing provides spacing
    ) {
        content()
    }
}
```
이를 통해 개별 Composable은 다음과 같이 손쉽게 테마 정보에 접근하게 됩니다.
```kotlin
val currentColors = LocalMyBenefitColors.current
```

### 10-3. `Surface`와 `LocalContentColor` (유사한 자동 제공 메커니즘)
Material Design의 `Surface` 컴포저블은 `CompositionLocalProvider`를 내부적으로 활용하는 가장 대표적인 예시입니다. 
* **동작**: `Surface(color = Color.Black)` 처럼 배경색을 검정색으로 설정하면, `Surface`는 내부적으로 `LocalContentColor provides Color.White`를 실행하여 하위의 `Text` 컴포저블들이 별도의 색 지정 없이도 자동으로 흰색으로 그려지도록 유도합니다.

```kotlin
Surface(color = MaterialTheme.colorScheme.primary) {
    // primary 배경색에 대비되는 contentColor가 내부적으로 LocalContentColor에 설정되므로,
    // 아래 Text는 명시적인 color 설정 없이도 가독성 높은 색상으로 렌더링됩니다.
    Text("Automatically readable text") 
}
```

### 10-4. Subcomposition 경계에서의 Local 값 유실 주의
Compose 내부에서 기존 트리와 다른 독립적인 composition 단계를 밟는 컴포저블(`SubcomposeLayout` 기반의 `LazyColumn`, `BoxWithConstraints` 또는 다이얼로그나 팝업 등 Window가 새로 분리되는 컴포저블)의 경우, **CompositionLocal 값이 하위 트리로 정상적으로 전달되지 않고 기본 fallback 값으로 유실되는 경우**가 발생할 수 있습니다.

* **최신 Compose 버전**: 컴파일러와 런타임 수준에서 Subcomposition 경계를 가로질러 CompositionLocal 값을 자동으로 이어주도록 개선되었으나, 커스텀 `ComposeView`를 다이얼로그(Dialog)나 다른 Window 계층에 붙일 때는 반드시 부모 CompositionContext를 명시적으로 상속해 주거나 `CompositionLocalProvider`로 다시 감싸 주어야 합니다.

