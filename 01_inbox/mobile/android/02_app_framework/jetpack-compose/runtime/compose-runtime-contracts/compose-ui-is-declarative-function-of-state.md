---
title: compose-ui-is-declarative-function-of-state
tags: [android, compose/runtime, jetpack-compose]
aliases: [Thinking in Compose, UI = f(state)]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Compose UI는 상태의 선언적 함수다

### 1. 개념 정의 (What)
Jetpack Compose에서 UI는 명령형 View 객체의 집합을 수동으로 탐색하여 속성을 변경하는 대상이 아니라, **현재 앱 상태(State)를 입력으로 받아 트리를 계산하고 기술하는 선언적 함수($UI = f(State)$)**다. `@Composable` 함수는 데이터를 수신하여 UI 구조(Composition)를 생성하며, 상태가 변경되면 Compose Runtime이 수신된 새 상태를 기반으로 영향을 받는 함수를 다시 호출(Recomposition)하여 UI 설명을 갱신한다.

---

### 2. 선언적 모델의 도입 배경 및 필연성 (Why)
기존 Android View System(Imperative UI Model)에서는 XML 기반 뷰 트리를 자바/코틀린 코드에서 `findViewById()`, `ViewBinding`, 또는 `DataBinding`으로 찾아 개별 setter(`textView.setText()`, `view.setVisibility()`)를 호출했다. 

이 방식은 다음과 같은 치명적 한계를 안고 있었다:
- **상태 불일치(State-UI Desynchronization)**: 데이터 모델의 값과 화면에 표시된 뷰 상태가 동기화되지 않아 예외적인 UI 버그(예: 비동기 데이터 로딩 후 숨겨져야 할 로딩 프로그레스바가 여전히 표시됨)가 자주 발생한다.
- **높은 상태 복잡도**: 뷰 자체가 내부 상태(예: `EditText` 입력 텍스트, `CheckBox` 체크 여부)를 직접 유지하여 비즈니스 로직과 UI 상태 간의 "단일 진실 출처(Single Source of Truth, SSOT)" 관리가 불가능하다.

Compose의 선언적 모델은 화면 전체를 매번 처음부터 다시 묘사하는 정형화된 수학적 함수 구조를 제공함으로써, 개발자가 UI 요소의 변경 절차(How)를 작성하는 대신 **현재 상태에 대응하는 UI의 모습(What)**만 선언하도록 강제한다.

---

### 3. 내부 동작 메커니즘 (How)

```
+-------------------+      State Read       +----------------------+
| State (Snapshot)  | --------------------> | Composable Function  |
+-------------------+                       +----------------------+
          |                                            |
          | State Changed                              | Emits Node Structure
          v                                            v
+-------------------+   Recomposes Scope   +----------------------+
| RecomposeScope    | --------------------> | Slot Table Update    |
+-------------------+                       +----------------------+
```

1. **상태 관찰 및 캡처**: Composable 함수가 실행되는 동안 `State<T>` 객체의 `.value`를 읽으면, Compose Runtime의 Snapshot 엔진이 해당 읽기 동작을 감지하고 현재 실행 중인 `RecomposeScope`에 이 State를 의존성으로 등록한다.
2. **트리 변경 갱신 (Recomposition)**: State 값이 변경되면 런타임은 해당 State를 읽은 `RecomposeScope`만 무효화(Invalidate)하고 재실행한다.
3. **Slot Table 및 Layout Node 반영**: Composable 재실행 결과는 화면을 통째로 다시 그리는 것이 아니라, 메모리 상의 **Slot Table**을 차분(Diffing) 분석하여 변경이 발생한 `LayoutNode`만 선택적으로 갱신하고 Canvas에 렌더링한다.

---

### 4. View System vs Jetpack Compose 비교

```kotlin
// [기존 View System]: 명령형 (Imperative)
// UI 객체를 직접 찾아가 상태 변경 메서드를 실행해야 함
class LegacyCounterActivity : AppCompatActivity() {
    private var count = 0
    private lateinit var binding: ActivityCounterBinding

    private fun updateCount() {
        count++
        binding.textViewCount.text = "Count: $count" // 수동 변경
    }
}

// [Jetpack Compose]: 선언형 (Declarative)
// 상태(count)를 입력받아 UI 구조를 선언. count가 변경되면 Compose가 자동 갱신.
@Composable
fun CounterScreen(count: Int, onIncrement: () -> Unit) {
    Column {
        Text(text = "Count: $count") // count 상태의 선언적 표현
        Button(onClick = onIncrement) {
            Text("Increment")
        }
    }
}
```

---

관련 노트: [Recomposition은 전체 UI redraw가 아니라 필요한 Composable scope 재실행이다](./recomposition-reruns-needed-composable-scopes-not-the-whole-ui.md), [Compose 상태와 Effect 계약](../../state-and-lifecycle/compose-state-and-effect-contracts/compose-state-and-effect-contracts.md)

출처: [Thinking in Compose](https://developer.android.com/develop/ui/compose/mental-model)

검증일: 2026-08-05. Compose 공식 가이드의 "Thinking in Compose" 문서 원문을 대조하여 선언적 UI 패러다임, Imperative View 모델과의 구조적 비교, Slot Table Diffing 및 Recomposition 메커니즘 서술을 정밀 보강했다.
