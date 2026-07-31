# State Lifetime Callbacks (`RememberObserver` & `RetainObserver`)

상위 노트: [jetpack-compose-side-effects-and-lifecycle](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-side-effects-and-lifecycle.md)

공식 문서 [State Callbacks in Compose](https://developer.android.com/develop/ui/compose/state-callbacks)에 따르면, `remember`로 관리되는 커스텀 객체나 데이터 홀더가 Composition의 시작/종료 또는 Retain(화면 회전 후 유지) 생명주기를 직접 관찰해야 할 때 전용 Observer 인터페이스를 구현할 수 있습니다.

### 5-1. `RememberObserver`: Composition 수명주기 관찰

`remember` 블록 내부에서 기억되는 객체가 `RememberObserver`를 구현하면, Compose Runtime이 해당 객체의 트리 진입/탈출/포기를 감지하여 아래 콜백을 자동으로 호출합니다.

```kotlin
import androidx.compose.runtime.RememberObserver

class MyCustomStateHolder : RememberObserver {
    override fun onRemembered() {
        // Composition 트리에 진입했을 때 호출 (리소스 할당, 리스너 등록 등)
    }

    override fun onForgotten() {
        // Composition 트리에서 빠져나갈 때 호출 (리소스 해제, 센서/스트림 해제)
    }

    override fun onAbandoned() {
        // remember 객체가 생성되었지만 Composition에 정상 포함되지 못하고 버려졌을 때 호출 (메모리 누수 방지 Cleanup)
    }
}

@Composable
fun MyComponent() {
    // remember에 전달된 stateHolder는 RememberObserver 콜백을 받습니다.
    val stateHolder = remember { MyCustomStateHolder() }
}
```

* **`DisposableEffect`와의 차이점**: `DisposableEffect`는 Side Effect 계층에서 람다식 기반으로 정리를 수반하지만, `RememberObserver`는 커스텀 클래스 객체 자체가 생명주기 이벤트를 직접 다루고 캡슐화할 때 유용합니다.

---

### 5-2. `RetainObserver`: Configuration Change & Scope Retain 관찰

Navigation3나 ViewModel과 같이 화면 회전(Configuration Change) 후에도 상태가 유지(Retain)되는 Scope(예: `rememberRetained`)에서 객체가 살아있거나 완전히 소멸되는 시점을 감지할 때는 `RetainObserver`를 활용합니다.

```kotlin
// Navigation / Retain Scope에서 관리되는 커스텀 State Holder
class MyRetainedStateHolder : RetainObserver {
    override fun onRetained() {
        // Retain Scope에 진입하여 객체가 보관될 때 호출
    }

    override fun onForgotten() {
        // Navigation BackStack에서 완전히 제거되거나 Scope가 파괴될 때 최종 Cleanup 호출
    }
}
```

### 요약: 언제 어떤 Observer를 써야 하나?

| Observer | 주 관찰 대상 | 주요 콜백 | 사용 목적 |
|:---|:---|:---|:---|
| **`RememberObserver`** | Composable Composition | `onRemembered`, `onForgotten`, `onAbandoned` | Composable 트리 진입/이탈 시 커스텀 클래스 리소스 자동 정리 |
| **`RetainObserver`** | Navigation / Retained Scope | `onRetained`, `onForgotten` | 화면 회전 후에도 유지되는 커스텀 객체의 최종 소멸 시점 정리 |
