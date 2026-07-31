# Jetpack Compose 애니메이션 API 레이어 구조

Jetpack Compose는 선언형 UI 패러다임에 맞춰 설계된 계층화된 애니메이션 API를 제공합니다. 개발자는 직관적인 레이아웃 레벨 애니메이션부터 세밀한 물리 기반 제어까지
필요한 수준의 추상화 단계를 선택할 수 있습니다.

```mermaid
graph TD
    classDef high fill: #FFEAEA, stroke: #D32F2F, stroke-width: 2px, color: #000000;
    classDef mid fill: #FFF3E0, stroke: #F57C00, stroke-width: 2px, color: #000000;
    classDef low fill: #E8F5E9, stroke: #388E3C, stroke-width: 2px, color: #000000;
    classDef spec fill: #E3F2FD, stroke: #1976D2, stroke-width: 2px, color: #000000;
    HighAPI[1. High-level APIs] --> LowAPI[2. Low-level APIs]
    LowAPI --> AnimSpecs[3. Animation Specs]

    subgraph HighLayer [1. 상위 수준 API: 레이아웃 및 컨텐츠 변경]
        HighAPI_1["AnimatedVisibility (진입/이탈 효과)"]
        HighAPI_2["AnimatedContent / Crossfade (컨텐츠 전환)"]
        HighAPI_3["Modifier.animateContentSize() (크기 변경 감지)"]
    end

    subgraph LowLayer [2. 하위 수준 API: 개별 속성 및 코루틴 제어]
        LowAPI_1["animate*AsState (단일 값 애니메이션)"]
        LowAPI_2["updateTransition (다중 속성 상태 전환)"]
        LowAPI_3["rememberInfiniteTransition (무한 루프)"]
        LowAPI_4["Animatable (코루틴 기반 직접 제어 및 물리 기반)"]
    end

    subgraph SpecLayer [3. 애니메이션 상세 스펙]
        Spec_1["spring (스프링 물리)"]
        Spec_2["tween (시간 기반 보간)"]
        Spec_3["keyframes (프레임 단위 제어)"]
        Spec_4["repeatable / infiniteRepeatable (반복 실행)"]
    end

    HighAPI_1 -.-> HighLayer
    HighAPI_2 -.-> HighLayer
    HighAPI_3 -.-> HighLayer
    LowAPI_1 -.-> LowLayer
    LowAPI_2 -.-> LowLayer
    LowAPI_3 -.-> LowLayer
    LowAPI_4 -.-> LowLayer
    Spec_1 -.-> SpecLayer
    Spec_2 -.-> SpecLayer
    Spec_3 -.-> SpecLayer
    Spec_4 -.-> SpecLayer
    class HighAPI, HighLayer high;
    class LowAPI, LowLayer mid;
    class AnimSpecs, SpecLayer spec;
```

---
