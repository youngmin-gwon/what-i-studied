# CompositionLocalProvider 및 유사한 스코프 제공 Composable 패턴

상위 노트: [[jetpack-compose-compositionlocal-and-designsystem-locals]]

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
