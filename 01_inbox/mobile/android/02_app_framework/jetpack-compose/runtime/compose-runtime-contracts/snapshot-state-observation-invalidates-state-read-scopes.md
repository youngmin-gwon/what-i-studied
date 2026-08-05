---
title: snapshot-state-observation-invalidates-state-read-scopes
tags: [android, compose/runtime, jetpack-compose]
aliases: [Snapshot system, State read observation]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## Snapshot State 관찰은 State를 읽은 scope를 invalidation 대상으로 만든다

### 1. 개념 정의 (What)
**Snapshot State 관찰 시스템**은 Compose Runtime의 상태 추적 엔진으로서, 다중 버전 동시성 제어(MVCC, Multi-Version Concurrency Control) 개념을 도입하여 코어 스냅샷 트랜잭션 내에서 발생하는 **상태 읽기(Read)** 및 **상태 쓰기(Write)**를 추적하고, 읽기가 이루어진 `RecomposeScope`를 자동으로 무효화(Invalidate) 대상 목록에 등록하는 메커니즘이다.

---

### 2. Snapshot 관찰 엔진의 필요성 (Why)
기존의 Observer 패턴(예: RxJava, LiveData 수동 observer 등록)에서는 개발자가 어떤 뷰에서 어떤 데이터 필드를 관찰해야 하는지 일일이 `.observe(this) { ... }` 코드를 작성해야 했다.

이 수동 방식은 다음 세 가지 문제가 존재했다:
1. **보일러플레이트 코드 증가**: 상태 변경마다 구속 코드를 수동 작성해야 함.
2. **리커넥트/메모리 누수**: Observer 해제가 누락되면 메모리 누수 발생.
3. **과도한 넓은 범위 무효화**: 뷰 전체가 갱신되어 세분화된 세부 단위 갱신 불가능.

Snapshot 관찰 엔진은 `@Composable` 함수 실행 중 `.value`를 읽는 동작을 코루틴/런타임 문맥에서 자동으로 인터셉트하여, 개발자의 개입 없이 완벽하고 정밀한 최소 단위 의존성 그래프를 동적으로 구축한다.

---

### 3. 내부 동작 메커니즘 (How)

```
[Composition Phase 시작]
         |
         v
[Snapshot.takeMutableSnapshot(readObserver) 생성]
         |
         v
[State.value 읽기 발생] -----> [readObserver(stateObj) 호출]
                                       |
                                       v
                     [현재 RecomposeScopeImpl 에 stateObj 바인딩]
         |
         v
[사용자의 State.value = newValue 쓰기 발생]
         |
         v
[Snapshot.sendApplyNotifications() 실행]
         |
         v
[바인딩되어 있던 RecomposeScopeImpl.invalidate() 발동]
```

1. **StateRecord 링크드 리스트**: 모든 `MutableState` 객체는 내부적으로 `StateRecord`의 단방향 체인을 유지하여 최신 스냅샷 버전별 값들을 보존한다.
2. **Read Observer 캡처**: Composition Phase가 시작될 때 런타임은 `Snapshot.takeMutableSnapshot()` 기반의 스냅샷을 활성화하고 Read Observer를 등록한다. Composable 바디 내에서 `state.value` 읽기가 실행되면 `StateRecord` 조회가 발생하며, 현 시점 실행 중인 `RecomposeScopeImpl`이 의존성 집합(Read Set)으로 저장된다.
3. **Write Tracking & Apply Notification**: `state.value = newValue` 쓰기가 발생하면 스냅샷에 변경 사항(Write Set)이 기록되며, 스냅샷이 적용(Apply)되는 시점에 해당 State 객체를 관찰 중이던 `RecomposeScopeImpl`들에 무효화 알림이 전송된다.

---

### 4. Read 위치에 따른 무효화 범위 제어 코드

```kotlin
@Composable
fun ReadLocationExample() {
    var count by remember { mutableStateOf(0) }

    // 1. Composition Phase Read: ReadLocationExample 스코프 자체가 count를 관찰함
    Text("Composition Read Count: $count")

    // 2. Layout/Draw Phase Read (람다 내부 읽기):
    // Box의 Composition 스코프는 count를 읽지 않음!
    // Modifier.offset 람다는 Layout Phase에서 실행되므로 Composition을 건너뛰고 Layout만 재실행됨
    Box(
        modifier = Modifier.offset {
            IntOffset(x = count * 2, y = 0) // Layout Phase Read!
        }
    )

    Button(onClick = { count++ }) {
        Text("Increment")
    }
}
```

- **Composition Phase Read**: 상태 읽기가 Composable 바디 직속에서 발생하면 Recomposition이 일어난다.
- **Layout/Draw Phase Read**: 상태 읽기를 `Modifier.offset { ... }`나 `Canvas { ... }` 람다 블록 내부로 미루면, Composition을 완전히 스킵하고 Layout/Draw 단계만 원자적으로 다시 계산하여 극강의 성능을 달성한다.

---

관련 노트: [Recomposition은 전체 UI redraw가 아니라 필요한 Composable scope 재실행이다](./recomposition-reruns-needed-composable-scopes-not-the-whole-ui.md), [Compose frame pipeline은 composition, layout, drawing으로 나뉜다](./compose-frame-pipeline-is-split-into-composition-layout-and-drawing.md)

출처: [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state), [Under the hood of Jetpack Compose Snapshots](https://medium.com/androiddevelopers/under-the-hood-of-jetpack-compose-snapshots-b8733a1e9447)

검증일: 2026-08-05. Compose Snapshot 시스템 구현체(`StateRecord`, `Snapshot.kt`) 원문을 대조하여 MVCC 트랜잭션 모델, Read Observer 인터셉트 및 파이프라인 단계별 Read 지점 분리 메커니즘 서술을 정밀 보강했다.
