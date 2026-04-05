---
title: android-ui-system
tags: []
aliases: []
date modified: 2026-04-05 17:43:18 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [[mobile-security]] > [[android-ui-system]]

### Android UI System: From View to Compose

전통적인 **View-based 명령형 UI 시스템**부터 현대적인 **Jetpack Compose 선언형 UI 프레임워크**까지, 안드로이드의 화면 렌더링 메커니즘을 심층적으로 분석합니다.

단순히 UI 를 그리는 것을 넘어, 어떻게 하면 효율적으로 리소스를 관리하고 고성능의 애니메이션을 구현할 수 있을지 이해하는 것이 목표입니다.

---

#### 💡 Context: UI 패러다임의 변화

안드로이드 UI 개발은 최근 몇 년간 큰 변화를 겪었습니다. 기존 XML 기반의 명령형(Imperative) 방식에서 Kotlin 코드로 UI 를 정의하는 선언형(Declarative) 방식으로의 전환은 개발 생산성과 유지보수성을 획기적으로 개선했습니다.

---

- **Performance**: `ConstraintLayout` 은 View 계층 깊이를 줄여 성능을 높였지만, 여전히 XML 파싱과 리플렉션 비용이 큽니다. Compose 는 코드로 컴파일되므로 이 비용이 없습니다.
- **State Sync**: View 시스템에서는 데이터가 바뀌면 `setText()` 를 수동으로 호출해야 합니다. 실수하면 UI 와 데이터가 틀어집니다. Compose 는 **Single Source of Truth**를 강제합니다.
- **Animations**: View 애니메이션은 "시작점과 끝점"을 정의하고 보간(Interpolation)하는 방식이지만, Compose 는 "상태 A 에서 상태 B 로의 전환"으로 정의합니다. 훨씬 직관적입니다.

---

#### 🏛️ Legacy View System (Imperative)

>[!CAUTION] **Devil's Advocate : XML 과 DataBinding 의 종말**
>안드로이드 진영은 수년간 XML 레이아웃과 `DataBinding`/`ViewBinding` 을 통해 MVVM 을 구현해왔으나, 이는 상태 불일치 버그의 온상이었습니다.
>현재는 **신규 프로젝트에서 XML View 체계를 기초로 구축하는 것은 명백한 기술 부채(Tech Debt)**로 간주됩니다. DataBinding 역시 레거시 유지보수를 제외하고는 Compose 로 100% 대체되어야 합니다.

"명령형 UI: 위젯을 만들고, 속성을 `set` 하라." (Legacy)

##### 1. The Big Three Passes

`ViewRootImpl` 이 `performTraversals()` 를 호출하면 세 단계가 실행됩니다.

1. **Measure (크기 측정)**:
    - 부모가 자식에게 제약조건(`MeasureSpec`)을 줍니다. (예: "너 폭 100dp 넘지 마")
    - 자식은 자신의 크기를 결정해 `setMeasuredDimension()` 을 부릅니다.
    - **Top-down** 방식입니다.
2. **Layout (위치 배치)**:
    - 부모가 자식의 위치(`left`, `top`, `right`, `bottom`)를 정해줍니다.
3. **Draw (그리기)**:
    - `Canvas` 객체에 실제로 그림을 그립니다.

##### 2. The Problem
- **Double Taxation**: `LinearLayout` 에 `weight` 를 쓰면 자식을 두 번 `measure` 해야 합니다. 뷰 계층이 깊어지면 측정 횟수가 지수적으로 늘어납니다 (Exponential layout cost).
- **Inheritance Hell**: `Button` 은 `TextView` 를 상속받습니다. `TextView` 는 `View` 를 상속받습니다. 버튼 하나 만드는 데 수천 개의 불필요한 속성을 다 들고 다닙니다.

---

#### 🚀 Jetpack Compose (Declarative)

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

#### ⚔️ Comparison: RecyclerView vs LazyColumn

##### RecyclerView (View)
- **Recycling**: 뷰 객체(`ViewHolder`)를 버리지 않고 재활용합니다.
- **Adapter**: 데이터와 뷰를 연결하는 **지루한 보일러플레이트**가 필요합니다.
- **ViewType**: 뷰 종류가 많아지면 `getItemViewType()` 관리가 지옥이 됩니다.

##### LazyColumn (Compose)
- **No Recycling**: Compose 는 뷰 객체가 없으므로 재활용할 필요가 없습니다. 그냥 필요한 컴포저블을 **새로 호출(Emit)**하면 됩니다. (Gap Buffer 덕분에 비용이 매우 쌉니다)
- **Code**: `items(list) { item -> Text(item) }`. 끝입니다.

---

#### 🎨 2026 현대적 UI 표준 (Android 15-16+)

##### 1. Edge-to-Edge (전체 화면 인터페이스)

Android 15 부터는 모든 앱에 **Edge-to-Edge**가 기본으로 강제된다. 시스템 바(상태바, 네비게이션 바) 뒤 영역까지 앱이 그려지며, `WindowInsets` 를 통한 패딩 처리가 필수적이다.

```kotlin
// Compose에서의 인셋 처리
Scaffold(
    modifier = Modifier.consumeWindowInsets(WindowInsets.safeDrawing),
    contentWindowInsets = WindowInsets.safeDrawing
) { innerPadding ->
    Box(Modifier.padding(innerPadding)) { ... }
}
```

##### 2. Predictive Back (예측형 뒤로 가기)

Android 14 에서 도입되어 16 에서 표준화된 기능으로, 사용자가 뒤로 가기 제스처를 할 때 이전 화면을 미리 보여주는 애니메이션을 제공한다. 이를 위해 앱은 `OnBackInvokedCallback` 을 올바르게 등록해야 한다.

---

##### 📚 연결 문서
- [android-compose-internals](android-compose-internals.md) - Compose 사용법 심화
- [android-graphics-and-media](../01_system_internals/android-graphics-and-media.md) - SurfaceFlinger 로 그림이 넘어가는 과정
- [android-activity-lifecycle](android-activity-lifecycle.md) - 생명주기에 따른 UI 상태 저장
