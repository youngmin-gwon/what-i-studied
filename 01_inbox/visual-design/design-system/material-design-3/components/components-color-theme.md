---
title: components-color-theme
tags: [android, color-system, design-system, expressive, flutter, hct, m3, material-design, material-theme, ux-design]
aliases: [Color Roles, Color Scheme vs Theme, Compose ColorScheme, Dynamic Color, HCT Color Space, M3 Color System, ThemeData Mapping]
date modified: 2025-12-28 00:11:36 +09:00
date created: 2025-12-27 23:39:00 +09:00
---

## 🎨 M3 Color & Theme: 플랫폼을 초월한 지능적 색상 체계

Material Design 3 (M3) 의 컬러 시스템은 단순한 색상 가이드라인을 넘어, **HCT**라는 수학적 모델을 기반으로 다양한 플랫폼(Android, Flutter, Web 등) 에서 일관된 **접근성(Accessibility)** 과 **정서적 표현력(Expression)** 을 보장하는 자동화 시스템입니다.

---

## 💡 Color Scheme vs. Theme Color: 전략적 분리

디자인 시스템에서 이 두 개념을 엄격히 나누는 이유는 **'맥락에 따른 유연성'** 때문입니다.

### 1. Theme Color (테마 컬러/Seed Color)

- **개념**: 제품의 정체성을 정의하는 '원천(Source)' 입니다. 브랜드 컬러나 사용자가 직접 고른 색상, 혹은 배경화면에서 추출된 색상 등이 시드(Seed) 가 됩니다.
- **의도**: "이 앱의 무드는 무엇인가?" 에 대답합니다.

### 2. Color Scheme (컬러 스킴/Roles)

- **개념**: 시드 컬러를 입력받아 **HCT 알고리즘**이 생성한 **26 개 이상의 의미론적 역할(Roles)** 집합입니다.
- **나누는 이유 (UX 전략)**:
    - **플랫폼 독립성**: 안드로이드 시스템 UI 든, Flutter 앱이든 'Primary' 가 가지는 '가장 중요한 행동' 이라는 의미는 동일합니다. 개발자는 구체적인 HEX 값을 몰라도 '역할' 에만 집중하여 코딩할 수 있습니다.
    - **동적 적응 (Dynamic Color)**: 사용자가 배경화면을 바꾸면 시드 컬러가 변하지만, 각 요소의 위계는 유지됩니다. 시스템이 자동으로 '적절한 대비' 를 계산하여 재생성하므로 일관된 가독성을 보장합니다.

---

## 🏗️ Exhaustive Role Index: 26 개 이상의 의미론적 역할 (Roles)

M3 에서는 모든 색상을 **'어디에, 어떤 목적으로 쓰이는가'** 에 따라 정의합니다.

### 1. Accent Roles (강조 요소군)

사용자의 시선을 유도하고 정체성을 드러내는 핵심입니다.

| Role            | 사용 의도 및 권장 상황                                | 위계 (Prominence) |
| :-------------- | :------------------------------------------- | :-------------- |
| **Primary**     | 앱의 핵심 액션(FAB, 메인 버튼). 가장 높은 주목도.             | High            |
| **Secondary**   | 보조적인 액션(필터 칩, 보조 버튼, 하단 바 아이콘).              | Medium          |
| **Tertiary**    | 악센트가 필요한 개별 요소(알림 점, 입력 필드 커서, 대비되는 강조).     | Medium-Low      |
| **On-\***       | (On-Primary 등) 해당 배경색 위에 올라가는 텍스트/아이콘 전용 색상. | Contrast Link   |
| **\*Container** | 강조색의 옅은 배경 버전. 콘텐츠 그룹화나 덜 강조된 버튼에 사용.        | Low             |

### 2. Neutral Roles (배경/표면군) - *Expressive 업데이트 핵심*

M3 Expressive 에서는 Surface 가 더 세밀한 '표현력' 을 위해 5 단계 이상으로 분화되었습니다.

| Role | 사용 의도 및 권장 상황 | UX 가치 |
| :--- | :--- | :--- |
| **Surface** | 앱 전체의 가장 기본이 되는 평면적인 배경. | Default Canvas |
| **Surface Bright/Dim** | 대화면이나 멀티 레이어에서 공간의 명도를 조절하여 공간감을 부여. | Spatial Depth |
| **Surface Container** | 계층 구조(Hierarchy) 를 표현하는 5 단계 컨테이너 (Lowest ~ Highest). | Tonal Hierarchy |
| **Surface Variant** | 경계가 뚜렷하지 않은 보조적인 카드나 구분선 배경. | Subtle Contrast |
| **On Surface / Variant** | 배경 위의 본문 텍스트(On Surface) 및 보조 텍스트(Variant). | Legibility |

### 3. Utility & Fixed Roles (기능/고정군)

- **Error / On Error**: 시스템 오류 상황 알림용 고대비 레드.
- **Outline / Variant**: 요소의 경계를 나누는 선. Variant 는 더 낮은 대비로 보조적인 구분에 적합.
- **Fixed Roles**: 라이트/다크 모드에 관계없이 동일한 톤을 유지해야 하는 특수 상황(예: 미디어 플레이어 제어기) 에서 사용.

---

## ⚙️ HCT Color Space: 지각적 일관성의 수학적 증명

M3 의 엔진인 **HCT (Hue, Chroma, Tone)** 는 기존 RGB/HSL 의 구조적 한계를 해결합니다.

- **HSL 의 한계**: 숫자로 된 명도(L) 가 50% 라 하더라도 실제 눈으로 보면 노란색은 눈부시게 밝고 파란색은 어둡습니다. 이로 인해 자동 대비 계산 시 가독성 이슈가 빈번했습니다.
- **HCT 의 해결책**: **Tone** 축이 인간의 지각적 밝기와 1:1 로 대응됩니다.
- **접근성 자동화**: 알고리즘은 배경과 글자색의 Tone 차이를 항상 일정 수치(예: 40 이상) 로 유지하도록 강제합니다. 따라서 개발자가 어떤 Seed Color 를 넣어도 WCAG AA 등급 이상의 대비를 100% 보장합니다.

---

## �️ Platform Implementation Mapping Guide

플랫폼별로 프로퍼티 이름은 다르지만 M3 에서는 동일한 알고리즘을 공유합니다.

### 1. Flutter (`ThemeData` & `ColorScheme`)

Flutter 는 M2 에서 M3 로 넘어가며 `ColorScheme` 중심으로 모든 컬러를 통합했습니다.

| 기존 ThemeData 프로퍼티 | M3 ColorScheme 맵핑 | 권장 사용법 |
| :--- | :--- | :--- |
| `primaryColor` | `ColorScheme.primary` | 직접 하드코딩 피하고 `context.theme.colorScheme` 사용. |
| `backgroundColor` | `ColorScheme.surface` | 전체 배경은 이제 Surface 로 표현. |
| `cardColor` | `ColorScheme.surfaceContainerLow` | 카드는 배경보다 살짝 밝거나 어두운 컨테이너 톤. |
| `dividerColor` | `ColorScheme.outlineVariant` | 구분선은 더 부드러운 Outline Variant 활용. |

### 2. Android Jetpack Compose (`MaterialTheme.colorScheme`)

안드로이드는 시스템 레벨의 **Material You(Dynamic Color)** 와 가장 강력하게 결합됩니다.

- **Dynamic Color**: `dynamicLightColorScheme(context)` 함수를 통해 OS 배경화면에서 시드 컬러를 직접 추출합니다.
- **Tonal Palettes**: 안드로이드는 내부적으로 13 개의 톤(0~100) 으로 구성된 팰릿을 생성하여 각 역할에 분배합니다.
- **Theme Builder**: `Material Theme Builder` 를 통해 생성된 `Color.kt` 와 `Theme.kt` 를 사용하여 플랫폼 공식 표준을 준수하세요.

---

## 📐 배치 및 팔레트 활용 권장사항 (Design Strategy)

### 1. Tonal Hierarchy (톤의 위계)

- **원칙**: 배경(`Surface`) → 그룹화(`Surface Container Low`) → 카드 요소(`Surface Container High`) 순으로 톤을 배치하여 시각적 질서를 잡으세요.
- **Contrast Control**: 중요한 정보일수록 배경과의 Tone 차이를 크게 벌리고, 보조 정보는 Outline Variant 와 Surface Variant 로 처리하여 정보를 '필터링' 하세요.

### 2. Expressive Color Fidelity

- Expressive 테마에서는 시드 컬러의 채도를 억지로 낮추지 않고, 원본의 강렬함을 최대한 살리면서 접근성을 맞춥니다. 브랜드 개성이 강한 앱일수록 Expressive 스키마 사용을 권장합니다.

---

## ♿ Accessibility (A11y): HCT 기반의 대비 자동 보장

M3 컬러 시스템의 존재 이유 중 가장 큰 부분은 '누구에게나 잘 보이는 색상' 을 자동으로 만드는 것입니다.

### 1. Contrast by Design (설계에 의한 대비)

- **The 40-Tone Rule (40 톤 규칙)**: M3 알고리즘은 배경색과 그 위의 글자색(On-colors) 간의 **Tone** 차이를 항상 **40** 이상으로 설정합니다. HCT 의 Tone 은 지각적 밝기이므로, 이 차이만으로도 WCAG AA 기준인 4.5:1 대비가 수학적으로 보장됩니다.
- **Color Correction (색각 이상 대응)**: HCT 모델은 색맹이나 색약 사용자에게도 동일한 '지각적 밝기' 를 제공하므로, 특정 색상을 구별하지 못하더라도 **밝기 차이**를 통해 정보를 명확히 인지할 수 있게 합니다.

### 2. User Personalization (사용자 개인화)

- **Contrast Settings (적응형 대비)**: 사용자가 안드로이드 설정에서 '대비 강조' 를 활성화하면, Color Scheme 전체의 톤이 실시간으로 조절되어 시인성을 극대화합니다. 이는 개발자가 별도의 코드를 짤 필요 없이 M3 테마를 사용하는 것만으로 혜택을 얻습니다.

---

## 🔗 관련 문서

- [[../material3_walkthrough|Material Design 3 개요 (Expressive Deep Dive)]]
- [[components-typography|Typography: 의미론적 가독성과 스펙]]
- [[components-actions|Actions: 버튼과 FAB]]
- [[components-containment-navigation|Containment & Navigation]]
- [[components-selection-inputs|Selection & Inputs]]
