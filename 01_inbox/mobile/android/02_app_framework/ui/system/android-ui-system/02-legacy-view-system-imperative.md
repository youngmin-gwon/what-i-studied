# 🏛️ Legacy View System (Imperative)

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
