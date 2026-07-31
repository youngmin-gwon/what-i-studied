# 🚀 Jetpack Compose (Declarative)

"선언형 UI: 상태(State)에 따라 UI 를 설명하라."

##### 1. The Three Phases

Compose 도 비슷해 보이지만 결정적인 차이가 있습니다.

1. **Composition (What to show)**:
    - Composable 함수를 실행해 UI 트리 구조를 만듭니다.
2. **Layout (Where to place)**:
    - **Measurable**을 측정하고 **Placeable**을 배치합니다.
    - **Single Pass Layout**: Compose 는 원칙적으로 자식을 **한 번만 측정**합니다. 두 번 측정하려 하면 런타임 에러를 뱉습니다. (`IntrinsicSize` 예외 제외)
3. **Drawing (How to render)**:
    - 픽셀을 그립니다.

##### 2. Internals: Gap Buffer & Slot Table (매우 중요)

Compose 는 뷰 객체를 힙에 만들지 않습니다(No View Object). 대신 **Slot Table**이라는 거대한 배열에 데이터를 저장합니다.

- **Gap Buffer**: 텍스트 에디터가 커서 위치에 빈 공간(Gap)을 두고 글자를 입력하듯, Compose 도 Slot Table 중간에 Gap 을 둡니다.
- **Recomposition**: UI 가 바뀌면, 바뀐 부분만 Slot Table 의 데이터를 덮어씁니다. 뷰를 `new` 하는 게 아닙니다. 이래서 Compose 가 빠릅니다.

##### 3. Modifiers (Chain of Responsibility)

XML 속성(`android:padding`, `android:background`) 대신 **Modifier 체인**을 씁니다.

- **Order Matters**: `padding().background()` 와 `background().padding()` 은 결과가 다릅니다. 순서대로 래퍼(Wrapper)가 씌워지는 구조이기 때문입니다.

---
