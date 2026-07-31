# Kotlin `by` 키워드

상위 노트: [jetpack-compose-state-management-flutter-comparison](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison.md)

`by`는 Compose 전용 문법이 아니라 Kotlin의 **delegated property** 문법입니다.

Compose에서는 `MutableState<T>`를 더 자연스럽게 읽고 쓰기 위해 자주 사용합니다.

아래 두 코드는 의미가 같습니다.

```kotlin
val countState = remember { mutableStateOf(0) }

Text(text = "${countState.value}")
Button(onClick = { countState.value += 1 }) {
    Text("Increase")
}
```

```kotlin
var count by remember { mutableStateOf(0) }

Text(text = "$count")
Button(onClick = { count += 1 }) {
    Text("Increase")
}
```

`by`를 쓰려면 보통 다음 import가 필요합니다.

```kotlin
import androidx.compose.runtime.getValue
import androidx.compose.runtime.setValue
```

읽기 전용이면 `getValue`만 필요합니다.

```kotlin
val uiState by viewModel.uiState.collectAsStateWithLifecycle()
```

여기서 `by`는 `uiState.value`를 매번 쓰지 않게 해주는 Kotlin 문법입니다. 상태 관리 도구 자체가 아닙니다.

---
