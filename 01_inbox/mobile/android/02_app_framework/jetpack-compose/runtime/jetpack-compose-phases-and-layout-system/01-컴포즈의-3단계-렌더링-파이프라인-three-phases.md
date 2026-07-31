# 컴포즈의 3단계 렌더링 파이프라인 (Three Phases)

Jetpack Compose는 매 프레임을 렌더링할 때 다음 3단계를 순차적으로 실행하여 화면을 갱신합니다.

```mermaid
graph LR
    classDef step fill: #E3F2FD, stroke: #1976D2, stroke-width: 2px, color: #000000;
    Comp["1. Composition<br/>(무엇을 보여줄 것인가)"] --> Lay["2. Layout<br/>(어디에 보여줄 것인가)"]
    Lay --> Draw["3. Drawing<br/>(어떻게 보여줄 것인가)"]
    class Comp, Lay, Draw step;
```

1. **Composition (구성)**: UI를 설명하는 컴포저블 함수들을 실행하여 메모리에 UI 트리(Slot Table)를 생성하거나 업데이트합니다.
2. **Layout (배치)**: UI 트리 안의 요소를 측정하고 화면 상의 배치 좌표를 설정합니다. 이 단계는 다시 **자식 측정(Measure)** 과 **위치 결정(
   Place)** 의 세부 단계로 나뉩니다.
3. **Drawing (그리기)**: 각 요소가 화면의 Canvas 영역에 실제로 픽셀을 그립니다.

---
