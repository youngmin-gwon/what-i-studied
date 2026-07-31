# 상태 읽기 지연 (Defer State Reads)

상위 노트: [jetpack-compose-performance-guidelines](01_inbox/mobile/android/02_app_framework/jetpack-compose/performance/jetpack-compose-performance-guidelines.md)

Compose 최적화의 첫 번째 원칙은 **"상태 읽기(State Read)를 가능한 가장 늦은 렌더링 단계로 지연하는 것"**입니다.

### 1-1. 컴포즈의 3단계 파이프라인 복습
컴포즈는 상태가 변경되면 **1) Composition(구성) -> 2) Layout(배치) -> 3) Drawing(그리기)** 단계를 거칩니다.
* 일반적인 상태 읽기는 1단계(Composition)에서 발생하므로, 상태가 단 1픽셀만 변해도 관련 컴포저블 전체가 리컴포지션됩니다.
* 만약 상태 읽기를 2단계(Layout)나 3단계(Draw)로 지연시킬 수 있다면, 1단계 리컴포지션을 완전히 생략하고 픽셀 좌표 변경 또는 그리기만 빠르게 재수행할 수 있습니다.

### 1-2. 개선 예시 (람다 기반 Modifier 사용)
사용자가 화면을 스크롤할 때 스크롤 오프셋 상태값에 따라 컴포저블의 오프셋 위치를 이동시키는 시나리오입니다.

#### ❌ 나쁜 예 (매 프레임마다 Composition 발생)
```kotlin
val scrollState = rememberScrollState()

Box(
    Modifier.offset(
        // scrollState.value가 Composition 단계에서 바로 읽히기 때문에,
        // 스크롤이 움직일 때마다 Box 전체가 무수히 리컴포지션됩니다.
        x = 0.dp,
        y = scrollState.value.dp 
    )
)
```

#### 🐳 좋은 예 (State Read를 Layout/Draw 단계로 지연)
```kotlin
val scrollState = rememberScrollState()

Box(
    Modifier.offset {
        // 람다 {} 내부로 상태 읽기를 감싸면, Composition 단계에서는 람다 참조만 전달되고
        // 실제 스크롤 값은 2단계인 Layout(Measurement/Placement) 단계에서 비로소 읽힙니다.
        // 결과적으로 리컴포지션이 0회 발생합니다.
        IntOffset(x = 0, y = scrollState.value)
    }
)
```

> [!TIP]
> `Modifier.offset {}`, `Modifier.drawBehind {}`, `Modifier.graphicsLayer {}` 등 람다 인수를 받는 확장 Modifier들은 대부분 상태 읽기 지연을 지원하므로, 실시간 변화하는 상태를 화면에 반영할 때는 반드시 람다 형태의 함수형 API를 사용하십시오.

---
