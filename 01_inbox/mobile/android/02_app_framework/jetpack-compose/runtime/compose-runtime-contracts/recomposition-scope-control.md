---
title: [recomposition](../recomposition.md)-reruns-needed-composable-scopes-not-the-whole-ui
tags: [android, compose/runtime, jetpack-compose]
aliases: [Recomposition, RecomposeScope]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Recomposition은 전체 UI redraw가 아니라 필요한 Composable scope 재실행이다

### 1. 개념 정의 (What)
**Recomposition**이란 Snapshot State의 값이 변경되었을 때 Compose Runtime이 전체 UI 트리를 재구축하거나 화면 전체를 다시 그리지 않고, 해당 상태를 직접 읽은 최소 단위의 `@Composable` 스코프(`RecomposeScope`)만을 선별하여 재실행하는 메커니즘이다.

---

### 2. 스코프 단위 Recomposition의 필요성 (Why)
복잡한 앱 화면은 수백 개 이상의 Composable 함수로 구성된다. 만약 상태 하나가 바뀔 때마다 루트(Root) Composable부터 하위 전체를 매번 재실행한다면, CPU 자원 낭비와 프레임 드롭(Jank), 극심한 발열 및 배터리 소모가 발생한다. 

Compose Runtime은 **최소 스코프 단위 재실행**과 **Skippable(건너뛰기)** 조작을 결합하여 60fps/120fps의 부드러운 화면 갱신 성능을 보장한다.

---

### 3. 내부 동작 메커니즘 (How)

```
[State.value 변경 발생]
         |
         v
[Snapshot System 이 의존성 맵 탐색]
         |
         v
[영향받는 RecomposeScopeImpl 찾아 Invalidate]
         |
         v
[해당 Composable 바디만 재실행 (하위 함수 파라미터 비교)]
         |
    +----+----+
    |         |
 [동일함]    [변경됨]
    |         |
    v         v
 [Skip]     [재실행]
```

1. **RecomposeScope 경계 생성**: Compose Compiler는 비-inline 상의 `@Composable` 함수 경계마다 바이트코드를 변환하여 `composer.startRestartGroup()`과 `composer.endRestartGroup()`을 삽입한다. 이로 인해 `RecomposeScopeImpl` 객체가 생성된다.
2. **State Read 감지 및 바인딩**: 함수 내부에서 `State.value`를 읽는 순간, 런타임의 `Snapshot` 관찰기가 읽기를 수집하여 "해당 State 객체 -> 현재 `RecomposeScopeImpl`" 의존성 매핑을 기록한다.
3. **Invalidation 요청**: State 쓰기가 일어난 후 스냅샷이 적용(Apply)되면, 매핑된 `RecomposeScopeImpl`의 `invalidate()`가 호출되어 재구성 대기열(Invalidated Scopes Queue)에 등록된다.
4. **Skip 제어**: 다음 프레임에서 해당 스코프만 재실행되며, 하위 Composable 호출 시 파라미터의 값이 이전 값과 동등(`equals() == true`)하고 파라미터 타입이 안정적(Stable)이라면 하위 함수 실행을 즉시 **Skip(건너뛰기)**한다.

---

### 4. 코드 사례: 스코프 분리와 State Read 지점

```kotlin
@Composable
fun ParentScreen() {
    var count by remember { mutableStateOf(0) }

    Log.d("Recomposition", "ParentScreen 실행") // count 변경 시 재실행되지 않음!

    Column {
        HeaderComponent() // count와 무관하므로 Recomposition 시 Skip됨
        
        // CountText 함수 내부에서 count.value를 읽으므로 CountText 스코프만 Invalidate됨
        CountText(count = count)

        Button(onClick = { count++ }) {
            Text("Increment")
        }
    }
}

@Composable
fun CountText(count: Int) {
    Log.d("Recomposition", "CountText 실행") // count 변경 시 이 스코프만 실행됨
    Text(text = "Current Count: $count")
}

@Composable
fun HeaderComponent() {
    Log.d("Recomposition", "HeaderComponent 실행")
    Text(text = "App Header")
}
```

- `ParentScreen` 내부에서 직접 `count`를 읽지 않고 `CountText(count)`로 넘기면, `count` 변경 시 `CountText` 스코프만 무효화된다.
- Android Studio Layout Inspector의 **Recomposition Counts** 도구를 활성화하면 특정 Composable의 Recompose 횟수와 Skipped 횟수를 정밀하게 모니터링할 수 있다.

---

관련 노트: [Snapshot State 관찰은 State를 읽은 scope를 invalidation 대상으로 만든다](./snapshot-state-observation-invalidates-state-read-scopes.md), [@Composable 컴파일 결과는 restart와 skip 제어를 가능하게 한다](./composable-compiler-restart-skip.md)

출처: [Recomposition in Jetpack Compose](https://developer.android.com/develop/ui/compose/mental-model#recomposition)

검증일: 2026-08-05. Compose 공식 가이드의 "Recomposition" 단락을 대조하여 RecomposeScope 생성, Invalidation Queue, Skippable 판정 조건 및 스코프 국소화 서술을 정밀 보강했다.
