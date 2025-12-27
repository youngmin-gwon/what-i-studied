---
title: components-color-theme
tags: [color-system, design-system, expressive, hct, m3, material-design, material-theme, ux-design]
aliases: [Color Roles, Color Scheme vs Theme, Dynamic Color, HCT Color Space, M3 Color System]
date modified: 2025-12-27 23:42:43 +09:00
date created: 2025-12-27 23:39:00 +09:00
---

## 🎨 M3 Color System: 지능적인 색상 체계

Material Design 3 (M3)의 컬러 시스템은 단순히 '색을 고르는 것'이 아닙니다. **HCT**라는 새로운 컬러 공간을 통해 개인화와 접근성을 동시에 달성하는 **지능적 알고리즘**의 결과물입니다.

---

## 💡 Color Scheme vs Theme Color

디자인 시스템에서 이 두 개념을 나누는 이유는 **'동적 대응력'** 때문입니다.

### 1. Theme Color (테마 컬러)

- **정의**: 브랜드나 제품을 상징하는 고정된 핵심 색상(Seed Color).
- **역할**: "이 앱은 파란색이다"라는 정체성을 부여합니다.

### 2. Color Scheme (컬러 스킴)

- **정의**: 핵심 색상을 기반으로 알고리즘에 의해 생성된 **26 개 이상의 색상 역할군(Roles)** 의 집합.
- **UX 적 가치**: 사용자가 배경화면을 바꾸면(Dynamic Color), Seed Color 가 변하고 그에 따라 전체 Color Scheme 이 자동으로 재계산됩니다. 개발자는 구체적인 '색상값'이 아니라 '역할(Role)'을 선언함으로써 어떤 환경에서도 일관된 대비와 가독성을 보장할 수 있습니다.

---

## 🏗️ 6 대 핵심 Color Roles & 사용 의도

M3 는 모든 색상을 '역할' 단위로 정의합니다. 각 역할은 `Color`, `On-(글자색)`, `Container`, `On-Container` 의 set 를 가집니다.

### 1. Primary (주요색)

- **사용처**: Floating Action Button (FAB), 가장 중요한 버튼, 활성 상태의 강조.
- **의도**: 화면에서 사용자의 시선이 가장 먼저 머물러야 하는 핵심 요소.

### 2. Secondary (보조색)

- **사용처**: 필터 칩, 덜 강조된 버튼, 보조적인 UI 컴포넌트.
- **의도**: 주요 기능을 방해하지 않으면서도 전체적인 톤을 조절하고 풍부한 표현을 돕습니다.

### 3. Tertiary (강조색)

- **사용처**: 알림 배지, 입력 필드의 강조, Primary/Secondary 와 대비되는 악센트.
- **의도**: 고정된 톤에서 벗어나 의외성을 주거나, 특정 개별 요소를 도드라지게 할 때 사용합니다.

### 4. Error (오류색)

- **사용처**: 텍스트 필드의 에러 메시지, 경고 아이콘.
- **의도**: 문제 발생을 즉각적으로 알리며, 시스템의 다른 색상들과 명확히 구분되는 고대비 레드 계열로 설계되었습니다.

### 5. Surface (기반색)

- **사용처**: 배경, 카드, 다이얼로그, 시트.
- **의도**: 콘텐츠가 담기는 그릇입니다. M3 는 이전의 그림자(Elevation) 중심에서 **톤(Tonal Elevation)** 중심의 Surface 로 진화했습니다.

### 6. Outline (외곽선)

- **사용처**: 카드 경계선, 버튼 테두리, 구분선.
- **의도**: 요소 간의 경계를 명확히 하여 시각적 위계를 정리합니다.

---

## ⚙️ HCT Color Space: 지각적 일관성

M3 의 핵심 기술인 **HCT (Hue, Chroma, Tone)**는 기존 RGB 나 HSL 의 한계를 해결합니다.

- **문제점 (HSL)**: 노란색(L:50%)과 파란색(L:50%)은 숫자는 같아도 인간의 눈에는 노란색이 훨씬 밝게 보입니다. 이는 접근성(Contrast) 계산 시 오류를 범하게 만듭니다.
- **해결책 (HCT)**: **Tone** 축이 인간이 느끼는 실제 '밝기'와 완벽하게 일치합니다. 따라서 알고리즘이 "Tone 40 위에 Tone 90 글자를 써라"고 결정하면, 어떤 색(Hue)이 선택되더라도 4.5:1 이상의 대비를 100% 보장합니다.

---

## 🚀 Material 3 Expressive 업데이트: 컬러의 진화

Expressive 업데이트에서는 컬러가 더욱 대담해졌습니다.

### 1. Color Fidelity (색상 충실도)

- 사용자가 선택한 색상을 인위적으로 보정하지 않고, 원본의 느낌을 최대한 살리면서도 접근성을 맞추는 알고리즘이 강화되었습니다.

### 2. Adaptive Contrast (적응형 대비)

- 단순히 다크/라이트 모드를 넘어, 사용자가 시스템 설정에서 대비를 높이면 Color Scheme 전체의 톤이 실시간으로 조절되어 시인성을 극대화합니다.

### 3. Extended Surface Roles

- 대화면과 XR 환경에 맞춰 `Surface Bright`, `Surface Dim` 등 더 세밀한 배경 역할군이 추가되어 공간감을 풍부하게 표현합니다.

---

## 🔗 관련 문서

- [[../material3_walkthrough|Material Design 3 개요 (Expressive Deep Dive)]]
- [[components-typography|Typography: 의미론적 가독성과 스펙]]
- [[components-actions|Actions: 버튼과 FAB]]
