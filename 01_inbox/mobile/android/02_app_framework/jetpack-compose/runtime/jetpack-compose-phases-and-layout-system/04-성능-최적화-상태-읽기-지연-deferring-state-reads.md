# 성능 최적화: 상태 읽기 지연 (Deferring State Reads)

Compose는 상태(State)가 변경될 때 최소한의 페이즈만 거치도록 똑똑하게 동작할 수 있습니다. 상태 값 읽기를 늦추면 특정 단계를 완전히 스킵할 수 있습니다.

* **Composition 단계에서 상태 읽기 (비권장)**:
  상태 값을 단순하게 읽으면 값 변경 시 Recomposition(1단계)부터 시작하여 전체 파이프라인이 다시 실행됩니다.
* **Layout/Drawing 단계로 상태 읽기 지연 (권장)**:
  람다 형태(`{ state.value }`)로 상태 읽기를 감싸서 Modifier 매개변수로 넘겨주면, 값 변경 시 **Composition(1단계)을 건너뛰고 Layout(
  2단계) 또는 Drawing(3단계)만 바로 재수행**합니다.

```kotlin
// 1. 비효율적 방식: 오프셋이 바뀔 때마다 전체 Recomposition 발생
Box(Modifier.offset(x = offsetXState.value.dp))

// 2. 효율적 방식: 람다를 통해 상태 읽기를 레이아웃 배치 단계로 지연
Box(Modifier.offset { IntOffset(offsetXState.value.roundToInt(), 0) })
```

---
