# 1단계: 상위 수준 애니메이션 API (High-level APIs)

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
