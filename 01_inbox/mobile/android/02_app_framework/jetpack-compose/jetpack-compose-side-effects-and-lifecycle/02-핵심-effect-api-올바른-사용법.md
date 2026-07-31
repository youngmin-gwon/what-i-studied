# 핵심 Effect API & 올바른 사용법

상위 노트: [[jetpack-compose-side-effects-and-lifecycle]]

### 2-1. `LaunchedEffect` (코루틴 기반 비동기 작업)

* **목적**: Composable의 수명 주기에 맞춰 코루틴을 실행합니다.
* **동작**: Composition이 시작될 때 코루틴 블록을 실행하고, 지정된 `key`가 변경되면 기존 코루틴을 취소하고 새로운 코루틴을 실행합니다. 컴포저블이 화면에서 사라지면 코루틴도 자동으로 취소됩니다.
* **주요 사용처**: 화면 진입 시 일회성 데이터 로드, 특정 상태 변경에 따른 스낵바 표시, 화면 네비게이션 이벤트 처리.

```kotlin
@Composable
fun UserProfileScreen(userId: String, snackbarHostState: SnackbarHostState) {
    // userId가 변경될 때마다 기존 로딩 작업을 취소하고 새로운 사용 정보를 로드합니다.
    LaunchedEffect(userId) {
        try {
            val user = repository.getUserProfile(userId)
            // 성공 처리
        } catch (e: Exception) {
            snackbarHostState.showSnackbar("사용자 정보를 가져오는데 실패했습니다.")
        }
    }
}
```

> [!WARNING]
> `LaunchedEffect(Unit)` 또는 `LaunchedEffect(true)`와 같이 고정 상수를 키로 사용하면 Composition 시작 시 단 한 번만 실행됩니다. 하지만 이는 파라미터 변경에 유연하게 대처하지 못하므로, Effect 내부에서 사용하는 모든 동적 변수는 가급적 키로 명시하는 것이 권장됩니다.

---

### 2-2. `rememberCoroutineScope` (이벤트 기반 코루틴 실행)
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

### 2-3. `DisposableEffect` (정리 작업이 필요한 효과)
* **목적**: 컴포저블이 화면에 나타나고 사라질 때(Composition 진입 및 소멸) 자원 등록 및 해제 쌍을 안전하게 관리합니다.
* **동작**: 블록이 실행된 후, 마지막 줄에 반드시 `onDispose` 블록을 정의하여 정리 작업을 작성해야 합니다. `key`가 변경되면 기존 작업을 해제(`onDispose`)하고 새로 다시 등록합니다.
* **주요 사용처**: 리스너(Listener) 등록 및 해제, SDK 초기화 및 정리, 센서 모니터링 시작 및 중단.

```kotlin
@Composable
fun SensorMonitor(sensorManager: SensorManager) {
    DisposableEffect(sensorManager) {
        val listener = SensorEventListener { /* 센서 데이터 처리 */ }
        sensorManager.registerListener(listener, ...)

        // 컴포저블이 화면에서 제거되거나 sensorManager가 바뀔 때 실행
        onDispose {
            sensorManager.unregisterListener(listener)
        }
    }
}
```

---

### 2-4. `SideEffect` (외부 비-Compose 상태와의 동기화)
* **목적**: Compose 재구성이 성공적으로 완료될 때마다 실행할 작업을 정의합니다.
* **동작**: Compose 상태가 성공적으로 스크린에 반영된 직후에 호출되며, 재구성이 취소되면 실행되지 않습니다.
* **주요 사용처**: 외부 모니터링 도구(Google Analytics 등)에 화면 상태 기록, Compose 관리 밖의 블루투스/네이티브 인스턴스에 현재 상태 반영.

```kotlin
@Composable
fun MyScreen(userStatus: String) {
    // Compose 상태를 Compose 관리 영역 밖의 외부 시스템에 공유할 때 사용
    SideEffect {
        NativeAnalyticsTracker.logUserStatus(userStatus)
    }
    
    Text("User: $userStatus")
}
```

---
