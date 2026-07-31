# Jetpack Compose Animation (애니메이션 시스템)

이 문서는 Jetpack Compose의 애니메이션 시스템을 상위 수준(High-level) API부터 하위 수준(Low-level) API까지 단계별 구조와 핵심 사용법, 그리고
다양한 애니메이션 스펙(AnimationSpec) 설정에 대해 다룹니다.

---

## 1. Jetpack Compose 애니메이션 API 레이어 구조

Jetpack Compose는 선언형 UI 패러다임에 맞춰 설계된 계층화된 애니메이션 API를 제공합니다. 개발자는 직관적인 레이아웃 레벨 애니메이션부터 세밀한 물리 기반 제어까지
필요한 수준의 추상화 단계를 선택할 수 있습니다.

```mermaid
graph TD
    classDef high fill: #FFEAEA, stroke: #D32F2F, stroke-width: 2px, color: #000000;
    classDef mid fill: #FFF3E0, stroke: #F57C00, stroke-width: 2px, color: #000000;
    classDef low fill: #E8F5E9, stroke: #388E3C, stroke-width: 2px, color: #000000;
    classDef spec fill: #E3F2FD, stroke: #1976D2, stroke-width: 2px, color: #000000;
    HighAPI[1. High-level APIs] --> LowAPI[2. Low-level APIs]
    LowAPI --> AnimSpecs[3. Animation Specs]

    subgraph HighLayer [1. 상위 수준 API: 레이아웃 및 컨텐츠 변경]
        HighAPI_1["AnimatedVisibility (진입/이탈 효과)"]
        HighAPI_2["AnimatedContent / Crossfade (컨텐츠 전환)"]
        HighAPI_3["Modifier.animateContentSize() (크기 변경 감지)"]
    end

    subgraph LowLayer [2. 하위 수준 API: 개별 속성 및 코루틴 제어]
        LowAPI_1["animate*AsState (단일 값 애니메이션)"]
        LowAPI_2["updateTransition (다중 속성 상태 전환)"]
        LowAPI_3["rememberInfiniteTransition (무한 루프)"]
        LowAPI_4["Animatable (코루틴 기반 직접 제어 및 물리 기반)"]
    end

    subgraph SpecLayer [3. 애니메이션 상세 스펙]
        Spec_1["spring (스프링 물리)"]
        Spec_2["tween (시간 기반 보간)"]
        Spec_3["keyframes (프레임 단위 제어)"]
        Spec_4["repeatable / infiniteRepeatable (반복 실행)"]
    end

    HighAPI_1 -.-> HighLayer
    HighAPI_2 -.-> HighLayer
    HighAPI_3 -.-> HighLayer
    LowAPI_1 -.-> LowLayer
    LowAPI_2 -.-> LowLayer
    LowAPI_3 -.-> LowLayer
    LowAPI_4 -.-> LowLayer
    Spec_1 -.-> SpecLayer
    Spec_2 -.-> SpecLayer
    Spec_3 -.-> SpecLayer
    Spec_4 -.-> SpecLayer
    class HighAPI, HighLayer high;
    class LowAPI, LowLayer mid;
    class AnimSpecs, SpecLayer spec;
```

---

## 2. 1단계: 상위 수준 애니메이션 API (High-level APIs)

컴포저블의 레이아웃이나 가시성, 화면 전환 등 고수준의 UI 변경을 처리하기에 적합하며, 선언적으로 간단히 선언해 사용할 수 있습니다.

### 2-1. AnimatedVisibility

컴포저블의 나타남(Enter)과 사라짐(Exit)을 단순한 조건식 변경으로 애니메이션화합니다.

* **기본 사용법**:
  ```kotlin
  var visible by remember { mutableStateOf(true) }

  AnimatedVisibility(
      visible = visible,
      enter = fadeIn() + expandVertically(),
      exit = fadeOut() + shrinkVertically()
  ) {
      Text("나타났다 사라지는 텍스트")
  }
  ```
* **커스텀 효과**: `enter` 및 `exit` 매개변수에 `fadeIn()`, `slideInHorizontally()`, `scaleIn()` 등의 다양한 전환 효과를
  `+` 연산자로 조합하여 적용할 수 있습니다.

### 2-2. AnimatedContent (Crossfade)

동적으로 변경되는 대상 상태에 따라 컨텐츠의 전환 애니메이션을 수행합니다.

* **AnimatedContent**: 상태가 변할 때 이전 컨텐츠와 새 컨텐츠 간의 세밀한 전환 효과(예: 위/아래 슬라이딩 전환)를 커스텀할 수 있습니다.
  ```kotlin
  AnimatedContent(
      targetState = currentTab,
      transitionSpec = {
          fadeIn(animationSpec = tween(150, delayMillis = 150)) togetherWith
          fadeOut(animationSpec = tween(150))
      }
  ) { targetTab ->
      when (targetTab) {
          Tab.Home -> HomeScreen()
          Tab.Profile -> ProfileScreen()
      }
  }
  ```
* **Crossfade**: 단순히 알파(투명도) 값을 기반으로 부드러운 전환을 적용하고 싶을 때 유용합니다.
  ```kotlin
  Crossfade(targetState = currentTab) { screen ->
      when (screen) {
          Tab.Home -> HomeScreen()
          Tab.Profile -> ProfileScreen()
      }
  }
  ```

### 2-3. Modifier.animateContentSize()

레이아웃의 크기가 변경될 때 자동으로 크기 변화 과정을 애니메이션화합니다.

```kotlin
var expanded by remember { mutableStateOf(false) }

Box(
    modifier = Modifier
        .background(Color.Blue)
        .animateContentSize() // 크기 변화 감지 후 애니메이션 적용
        .clickable { expanded = !expanded }
) {
    Text(
        text = if (expanded) "자세히 보기 콘텐츠..." else "간단 요약",
        modifier = Modifier.padding(16.dp)
    )
}
```

---

## 3. 2단계: 하위 수준 애니메이션 API (Low-level APIs)

특정 컴포저블의 단일 속성 값을 직접 부드럽게 보간하거나, 상태 머신을 기반으로 여러 요소의 복잡한 움직임을 정밀 제어할 때 사용합니다.

### 3-1. animate*AsState

가장 널리 쓰이는 하위 레벨 API로, 상태 변경 시 특정 단일 값(`Float`, `Color`, `Dp`, `Offset`, `IntSize` 등)을 부드럽게 변환시켜 줍니다.

```kotlin
var isRed by remember { mutableStateOf(false) }

// 상태 변경 시 자동으로 색상이 애니메이션화됨
val backgroundColor by animateColorAsState(
    targetValue = if (isRed) Color.Red else Color.Green,
    animationSpec = tween(durationMillis = 1000)
)

Box(
    modifier = Modifier
        .size(100.dp)
        .background(backgroundColor)
        .clickable { isRed = !isRed }
)
```

### 3-2. updateTransition

하나의 상태 변화(예: 탭 활성화, 접힘/펼침 상태 등)에 따라 **여러 애니메이션 값을 동기화**하여 일관된 전환 연출을 할 수 있도록 돕는 상태 기반 API입니다.

```kotlin
enum class BoxState { Collapsed, Expanded }

var boxState by remember { mutableStateOf(BoxState.Collapsed) }
val transition = updateTransition(targetState = boxState, label = "BoxTransition")

// 1. 크기 애니메이션 설정
val size by transition.animateDp(label = "Size") { state ->
    when (state) {
        BoxState.Collapsed -> 100.dp
        BoxState.Expanded -> 200.dp
    }
}

// 2. 색상 애니메이션 설정 (크기와 동기화됨)
val color by transition.animateColor(label = "Color") { state ->
    when (state) {
        BoxState.Collapsed -> Color.Blue
        BoxState.Expanded -> Color.Red
    }
}

Box(
    modifier = Modifier
        .size(size)
        .background(color)
        .clickable {
            boxState = if (boxState == BoxState.Collapsed) BoxState.Expanded else BoxState.Collapsed
        }
)
```

### 3-3. rememberInfiniteTransition

무한히 반복되는 애니메이션(예: 로딩 인디케이터의 회전, 심장 박동 효과, 그라데이션 쉬머 효과)을 만들 때 사용합니다.

```kotlin
val infiniteTransition = rememberInfiniteTransition(label = "InfinitePulse")

// 무한히 0.5f에서 1.0f 사이를 펄스 운동하는 애니메이션
val scale by infiniteTransition.animateFloat(
    initialValue = 0.5f,
    targetValue = 1.0f,
    animationSpec = infiniteRepeatable(
        animation = tween(1000),
        repeatMode = RepeatMode.Reverse
    ),
    label = "Scale"
)

Box(
    modifier = Modifier
        .size(100.dp)
        .graphicsLayer(scaleX = scale, scaleY = scale)
        .background(Color.Magenta)
)
```

### 3-4. Animatable

코루틴 범위를 통해 **애니메이션을 정밀하게 제어하거나 명령을 즉시 중단(SnapTo), 취소**해야 하는 가장 저수준의 애니메이션 상태 홀더입니다. 물리 기반 터치 스와이프
제스처 등에 적합합니다.

```kotlin
val colorAnim = remember { Animatable(Color.Gray) }

// 제스처 또는 특정 비동기 트리거 시 코루틴 내에서 실행
LaunchedEffect(isSuccess) {
    if (isSuccess) {
        // 부드럽게 Green으로 변환
        colorAnim.animateTo(Color.Green, animationSpec = spring())
    } else {
        // 즉시 Red로 값 스냅
        colorAnim.snapTo(Color.Red)
    }
}
```

---

## 4. 애니메이션 스펙 (AnimationSpec)

Jetpack Compose에서는 애니메이션의 보간 및 완화 함수(Easing), 가속도 물리 모델 등을 결정하기 위해 `AnimationSpec`을 구성합니다.

| API 종류                 | 역할 및 특징                                                                                                      |
|:-----------------------|:-------------------------------------------------------------------------------------------------------------|
| `spring()`             | **기본 스펙**: 물리 기반 스프링 모델입니다. 바운스 효과가 포함된 자연스러운 움직임을 생성합니다. 감쇠율(`dampingRatio`)과 강성(`stiffness`)으로 커스텀합니다.     |
| `tween()`              | **시간 기반 보간**: 지정된 시간(duration) 동안 수치가 변합니다. Easing 곡선(`LinearEasing`, `FastOutSlowInEasing` 등)을 커스텀할 수 있습니다. |
| `keyframes()`          | **프레임 단위 제어**: 특정 시간 지점마다 고정 값과 보간 방식을 직접 지정하여 엇박자 애니메이션이나 복합 연출을 설정할 수 있습니다.                                |
| `repeatable()`         | 특정 시간 기반 애니메이션(`tween` 등)을 지정된 횟수만큼 반복하도록 래핑합니다.                                                             |
| `infiniteRepeatable()` | 무한 반복 형태로 래핑하여 지속적으로 재생시킵니다.                                                                                 |
| `snap()`               | 대기 시간 없이 즉각적으로 목표 값으로 상태 값을 전환시킵니다.                                                                          |

> [!TIP]
> Jetpack Compose 애니메이션의 기본 동작 스펙은 `spring()`입니다. 사용자가 물리 법칙에 기반한 반응 속도를 가장 부드럽고 자연스럽게 인지하기 때문입니다.

---

## 5. 관련 문서

* **레이아웃 및 렌더링 시스템
  **: [[jetpack-compose-phases-and-layout-system]]

