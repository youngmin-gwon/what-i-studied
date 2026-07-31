# Jetpack Compose UI에서의 UI Automator 조작 고도화
기본적으로 Macrobenchmark와 Baseline Profile 테스트 코드는 타겟 앱과 **완전히 분리된 격리 프로세스**에서 디바이스를 통제합니다. 
Compose UI 요소를 찾고 조작하려면 컴포저블에 `testTag`를 명시적으로 부여하여 UI Automator가 `resource-id`로 이를 찾아갈 수 있게 세팅해야 합니다.

* **앱 컴포저블 대상 지정**:
```kotlin
LazyColumn(
    modifier = Modifier
        .fillMaxSize()
        .testTag("exercise_list_view") // testTag 부여
) {
    // ...
}
```
