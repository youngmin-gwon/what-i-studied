---
title: android-ui-system
tags: [android, ui, view, compose, internal]
aliases: [View System, Jetpack Compose Internals, Measure Layout Draw]
date modified: 2025-12-18 06:20:00 +09:00
date created: 2025-12-16 16:19:14 +09:00
---

# UI System: Imperative vs Declarative

안드로이드 UI의 역사는 2010년의 `View.java`(2만 줄)에서 2020년의 `@Composable`로 완전히 바뀌었습니다.
단순히 문법이 바뀐 게 아닙니다. **"어떻게 그릴까(How)"**에서 **"무엇을 그릴까(What)"**로 패러다임이 이동했습니다.

## 💡 Why it matters (Context)

-   **Performance**: `ConstraintLayout`은 View 계층 깊이를 줄여 성능을 높였지만, 여전히 XML 파싱과 리플렉션 비용이 큽니다. Compose는 코드로 컴파일되므로 이 비용이 없습니다.
-   **State Sync**: View 시스템에서는 데이터가 바뀌면 `setText()`를 수동으로 호출해야 합니다. 실수하면 UI와 데이터가 틀어집니다. Compose는 **Single Source of Truth**를 강제합니다.
-   **Animations**: View 애니메이션은 "시작점과 끝점"을 정의하고 보간(Interpolation)하는 방식이지만, Compose는 "상태 A에서 상태 B로의 전환"으로 정의합니다. 훨씬 직관적입니다.

---

## 🏛️ Legacy View System (Imperative)

"명령형 UI: 위젯을 만들고, 속성을 `set` 하라."

### 1. The Big Three Passes
`ViewRootImpl`이 `performTraversals()`를 호출하면 세 단계가 실행됩니다.

1.  **Measure (크기 측정)**:
    -   부모가 자식에게 제약조건(`MeasureSpec`)을 줍니다. (예: "너 폭 100dp 넘지 마")
    -   자식은 자신의 크기를 결정해 `setMeasuredDimension()`을 부릅니다.
    -   **Top-down** 방식입니다.
2.  **Layout (위치 배치)**:
    -   부모가 자식의 위치(`left`, `top`, `right`, `bottom`)를 정해줍니다.
3.  **Draw (그리기)**:
    -   `Canvas` 객체에 실제로 그림을 그립니다.

### 2. The Problem
-   **Double Taxation**: `LinearLayout`에 `weight`를 쓰면 자식을 두 번 `measure` 해야 합니다. 뷰 계층이 깊어지면 측정 횟수가 지수적으로 늘어납니다 (Exponential layout cost).
-   **Inheritance Hell**: `Button`은 `TextView`를 상속받습니다. `TextView`는 `View`를 상속받습니다. 버튼 하나 만드는 데 수천 개의 불필요한 속성을 다 들고 다닙니다.

---

## 🚀 Jetpack Compose (Declarative)

"선언형 UI: 상태(State)에 따라 UI를 설명하라."

### 1. The Three Phases
Compose도 비슷해 보이지만 결정적인 차이가 있습니다.

1.  **Composition (What to show)**:
    -   Composable 함수를 실행해 UI 트리 구조를 만듭니다.
2.  **Layout (Where to place)**:
    -   **Measurable**을 측정하고 **Placeable**을 배치합니다.
    -   **Single Pass Layout**: Compose는 원칙적으로 자식을 **한 번만 측정**합니다. 두 번 측정하려 하면 런타임 에러를 뱉습니다. (`IntrinsicSize` 예외 제외)
3.  **Drawing (How to render)**:
    -   픽셀을 그립니다.

### 2. Internals: Gap Buffer & Slot Table (매우 중요)
Compose는 뷰 객체를 힙에 만들지 않습니다(No View Object). 대신 **Slot Table**이라는 거대한 배열에 데이터를 저장합니다.

-   **Gap Buffer**: 텍스트 에디터가 커서 위치에 빈 공간(Gap)을 두고 글자를 입력하듯, Compose도 Slot Table 중간에 Gap을 둡니다.
-   **Recomposition**: UI가 바뀌면, 바뀐 부분만 Slot Table의 데이터를 덮어씁니다. 뷰를 `new` 하는 게 아닙니다. 이래서 Compose가 빠릅니다.

### 3. Modifiers (Chain of Responsibility)
XML 속성(`android:padding`, `android:background`) 대신 **Modifier 체인**을 씁니다.
-   **Order Matters**: `padding().background()`와 `background().padding()`은 결과가 다릅니다. 순서대로 래퍼(Wrapper)가 씌워지는 구조이기 때문입니다.

---

## ⚔️ Comparison: RecyclerView vs LazyColumn

### RecyclerView (View)
-   **Recycling**: 뷰 객체(`ViewHolder`)를 버리지 않고 재활용합니다.
-   **Adapter**: 데이터와 뷰를 연결하는 **지루한 보일러플레이트**가 필요합니다.
-   **ViewType**: 뷰 종류가 많아지면 `getItemViewType()` 관리가 지옥이 됩니다.

### LazyColumn (Compose)
-   **No Recycling**: Compose는 뷰 객체가 없으므로 재활용할 필요가 없습니다. 그냥 필요한 컴포저블을 **새로 호출(Emit)**하면 됩니다. (Gap Buffer 덕분에 비용이 매우 쌉니다)
-   **Code**: `items(list) { item -> Text(item) }`. 끝입니다.

### 📚 연결 문서
- [[android-compose-internals]] - Compose 사용법 심화
- [[android-graphics-and-media]] - SurfaceFlinger로 그림이 넘어가는 과정
- [[android-activity-lifecycle]] - 생명주기에 따른 UI 상태 저장
