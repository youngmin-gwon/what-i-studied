# `rememberCoroutineScope` (이벤트 기반 코루틴 실행)
* **목적**: Composable의 생명주기에 종속된 코루틴 스코프를 가져옵니다.
* **동작**: 코루틴 스코프를 기억(`remember`)하여, 비-composable 콜백(예: 버튼 클릭 이벤트 handler) 내부에서 안전하게 코루틴을 시작할 수 있게 해줍니다.
* **주요 사용처**: 버튼 클릭 시 스크롤 이동, Drawer 열기/닫기, 사용자 액션에 동반되는 가벼운 비동기 처리.

```kotlin
@Composable
fun ScrollToTopButton(lazyListState: LazyListState) {
    // Composable의 Lifecycle에 바인딩된 CoroutineScope 생성
    val scope = rememberCoroutineScope()

    Button(
        onClick = {
            // Composable 외부 콜백이므로 LaunchedEffect 대신 scope.launch 사용
            scope.launch {
                lazyListState.animateScrollToItem(index = 0)
            }
        }
    ) {
        Text("맨 위로 이동")
    }
}
```

#### 💡 수명 주기 안전을 위한 클릭 중복 방지: `dropUnlessResumed` / `dropUnlessStarted`
사용자가 버튼을 아주 빠르게 여러 번 탭하거나(Double-click), 화면 전환 애니메이션 중에 버튼을 다시 누르면 코루틴 작업이 중복 실행되거나 화면이 중복으로 열리는(Multiple Navigation) 문제가 발생할 수 있습니다. 

이를 방지하기 위해 Lifecycle 2.8+ 버전부터 제공되는 `dropUnlessResumed` 또는 `dropUnlessStarted`를 사용하여 콜백을 감싸는 것이 권장됩니다.

* **`dropUnlessResumed`**: 현재 화면의 Lifecycle이 최소 `RESUMED` 상태일 때만 내부 람다식을 실행하고, 그렇지 않을 때는 호출을 무시(Drop)합니다.
* **사용 방법**:
```kotlin
import androidx.lifecycle.compose.dropUnlessResumed

Button(
    onClick = dropUnlessResumed {
        // 화면이 완전히 활성화(Resumed) 상태인 경우에만 1회 실행 보장
        onNavigateToDetail() 
    }
) {
    Text("상세 화면으로 이동")
}
```

> [!IMPORTANT]
> **LaunchedEffect vs rememberCoroutineScope**
> * **`LaunchedEffect`**: 상태 변화나 생명주기 시작과 동시에 자동으로 실행되어야 하는 비동기 작업에 사용합니다.
> * **`rememberCoroutineScope`**: 사용자의 클릭이나 제스처 같은 특정 이벤트 발생 시점에 명시적으로 코루틴을 실행해야 할 때 사용합니다.
> * **중복 방지 연계**: `rememberCoroutineScope` 내부에서 실행되는 사용자 행동(이벤트) 콜백을 작성할 때는 `dropUnlessResumed`와 함께 사용하여 안전성을 보장하십시오.

---
