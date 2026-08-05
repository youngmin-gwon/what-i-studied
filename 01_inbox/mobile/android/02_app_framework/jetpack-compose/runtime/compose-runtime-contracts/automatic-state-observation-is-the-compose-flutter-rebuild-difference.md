---
title: automatic-state-observation-is-the-compose-flutter-rebuild-difference
tags: [android, compose/runtime, jetpack-compose]
aliases: [A Compose State of Mind, Compose for Flutter developers]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 23:59:00 +09:00
---

## 자동 상태 관찰은 Compose 와 Flutter Rebuild 의 차이점이다

### 1. 개념 정의 (What)
**자동 상태 관찰(Automatic State Observation)**은 Compose Runtime이 코루틴/스냅샷 파이프라인 레벨에서 Composable 함수가 실행 중 어떤 State 객체의 `.value`를 읽었는지 실시간으로 추적·기록하여, 상태 변경 시 무효화 대상을 세분화하는 **자동화된 상태 추적 시스템**이다.

---

### 2. Flutter Rebuild 패러다임과의 비교 (Why)
Flutter 개발자가 Compose를 접할 때 가장 빈번하게 오해하는 부분은 UI 갱신 멘탈 모델의 차이다:
- **Flutter 모델**: `StatefulWidget` 내부에서 개발자가 직접 `setState(() { ... })`를 실행하거나, `Provider`/`Riverpod`의 `ref.watch()`를 통해 변경 범위를 수동/명시적으로 선언해야 한다. Dirty 플래그가 세팅되면 해당 Widget 전체의 `build()` 함수가 재실행된다.
- **Compose 모델**: 명시적인 `setState()`나 수동 리스너 등록 구문이 일절 존재하지 않는다. 런타임의 **Snapshot 엔진**이 Composable 함수 바디 내부의 정밀한 상태 읽기 지점을 100% 자동으로 인터셉트하여, 해당 스코프(`RecomposeScope`)만 선별 무효화한다.

이 차이점 덕분에 Compose는 개발자의 실수로 인한 전체 트리의 과도한 재구성을 근본적으로 차단한다.

---

### 3. 내부 동작 및 차이점 메커니즘 (How)

```
[Flutter Rebuild 파이프라인]
  개발자의 setState() 명시 호출 ---> 해당 Widget 트리 전체 build() 재실행 (Dirty 범위 수동 지정)

[Compose Automatic Read Observation 파이프라인]
  Composable 함수 실행중 state.value 읽기 감지 
  ---> Snapshot Read Observer 가 RecomposeScopeImpl 에 State 자동 의존성 바인딩 
  ---> state.value 변경 시 읽어간 최소 Scope 만 선별 Invalidate!
```

1. **의존성 자동 등록**: Composable 함수 실행 중 `State<T>.value`를 읽는 순간, 런타임의 스냅샷 관찰자가 호출 스택의 최상단에 있는 `RecomposeScope`를 읽기 집합(Read Set)에 포함시킨다.
2. **람다 및 읽기 위치 분리**: 람다 내부(예: `Button(onClick = { count++ })`)에서 수행되는 읽기/쓰기는 Composition 단계에서 실행되는 코드가 아니므로, 해당 `Button`을 둘러싼 Composable 스코프의 Read Set에 등록되지 않는다.

---

### 4. 코드 사례 및 Flutter 대비 성능 트래킹

```kotlin
@Composable
fun AutomaticObservationCounter() {
    var count by remember { mutableStateOf(0) }

    // Text 컴포넌트의 Scope가 count 상태 읽기를 감지 및 자동 등록함
    Text("Count: $count")

    // onClick 람다는 쓰기(Write) 동작이며, Composition 중 실행되지 않으므로 Button 스코프는 Invalidate 되지 않음!
    Button(onClick = { count++ }) {
        Text("Increment")
    }
}
```

- Android Studio의 **Layout Inspector**를 연결하면 recomposition count 열에서 실제로 어떤 Composable이 재구성되고 어떤 Composable이 Skip 되었는지 숫자로 직관적으로 확인할 수 있다.

---

관련 노트: [Snapshot State 관찰은 State를 읽은 scope를 invalidation 대상으로 만든다](./snapshot-state-observation-invalidates-state-read-scopes.md), [Compose state owner는 읽고 쓰는 범위의 가장 낮은 공통 owner다](./compose-state-owner-is-the-lowest-common-owner-that-needs-read-or-write.md)

출처: [Thinking in Compose](https://developer.android.com/develop/ui/compose/mental-model), [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)

검증일: 2026-08-05. Compose 공식 가이드 및 Flutter 아키텍처 문서 원문을 대조하여 자동 상태 관찰(Automatic State Observation)과 Flutter 수동 rebuild/ref.watch() 모델의 비교 서술을 정밀 보강했다.
