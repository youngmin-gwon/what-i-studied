---
title: Material Design 3 (M3) & Expressive - UX Deep Dive
tags: [design-system, material-design, m3, material-you, ux-philosophy]
aliases: [M3 Deep Dive, Why Material 3, M2 vs M3]
date modified: 2025-12-27 23:05:00 +09:00
date created: 2025-12-27 22:55:00 +09:00
---

## 🎨 개요 (Overview)

**Material Design 3 (M3)**는 단순히 디자인의 '모양'을 바꾼 것이 아니라, 사용자와 기기 사이의 **정서적 연결**과 **사용성(Usability)**에 대한 근본적인 철학을 재정의한 시스템입니다. "Material You"는 디자인의 주도권을 시스템이 아닌 사용자에게 넘겨줌으로써, 기술이 인간에게 더 부드럽고 가깝게 다가오도록 합니다.

---

## 🚀 왜 M3로 진화했는가? (Evolution: M2 vs M3)

기존 Material Design 2 (M2)가 '일관성'과 '브랜드 정체성'에 집중했다면, M3는 **'개인화'**와 **'적응성'**을 최우선 가치로 둡니다.

| 특징 | Material Design 2 (M2) | Material Design 3 (M3) | UX 개선점 |
| :--- | :--- | :--- | :--- |
| **색상 (Color)** | 고정된 브랜드 컬러 중심 | **Dynamic Color (사용자 배경화면 기반)** | 정서적 소속감 및 자동 대비 조절 |
| **모양 (Shape)** | 정형화된 둥근 모서리 | **Variable/Expressive Shapes** | 시각적 위계 명확화 및 브랜드 표현 |
| **애니메이션** | 정해진 가속도(Easing) | **Physics-based Motion (Springs)** | 자연스러운 피드백, 인지 부하 감소 |
| **접근성** | 수동 설정 중심 | **System-level Adaptive Contrast** | 모든 사용자에게 최적화된 시인성 제공 |

---

## 🌈 핵심 철학 1: Personalization (Material You)

Material You의 핵심은 사용자가 디자인의 공동 제작자가 된다는 것입니다.

### Dynamic Color & Tonal Palettes
단순히 배경색이 바뀌는 것이 아닙니다. M3 알고리즘은 사용자의 배경화면에서 핵심 색상을 추출하고, 이를 5개의 톤 범위(Tonal Palettes)로 나눕니다.

![Dynamic Color Generation](file:///Users/youngmin/Documents/Obsidian/what-i-studied/01_inbox/visual%20design/design%20system/material-design-3/_assets/dynamic_color_gen.png)
*<사용자 배경에서 추출된 Source Color가 시스템 전체의 Tonal Palette로 확장되는 과정>*

**UX적 가치**:
- **정서적 연결**: 사용자가 직접 고른 사진이 UI 전체의 톤을 결정하면서 기기에 대한 애착이 높아집니다.
- **예측 가능한 접근성**: 동적 색상 시스템은 어떤 색상이 선택되더라도 텍스트와 배경 간의 최소 대비를 자동으로 보장합니다.

---

## ✨ 핵심 철학 2: Expressive System

"Material 3 Expressive"는 디자인이 사용자에게 말을 거는 방식입니다. 정형화된 딱딱한 인터페이스 대신, **살아있는 듯한 반응**을 목표로 합니다.

### 1. Motion Springs & Physics
기존 애니메이션이 정해진 시간 동안 움직였다면, M3의 모션은 **물리 법칙(Springs)**을 따릅니다.

![Expressive Motion & Shape Morph](file:///Users/youngmin/Documents/Obsidian/what-i-studied/01_inbox/visual%20design/design%20system/material-design-3/_assets/expressive_motion.png)
*<버튼이나 컴포넌트가 탄성 있게 변형되며 사용자에게 피드백을 주는 방식>*

**UX적 가치**:
- **인지 부하 감소**: 물리적인 움직임은 인간의 뇌가 예측하기 더 쉽습니다. 급격한 화면 전환보다 부드러운 연결(Continuity)을 통해 사용자는 현재 맥락을 잃지 않습니다.
- **발견 가능성(Discoverability)**: 연구에 따르면, 표현력이 풍부한 UI 요소는 정적인 요소보다 사용자의 시선을 4배 더 빠르게 유도하여 주요 기능을 쉽게 찾게 합니다.

---

## 📦 컴포넌트 라이브러리 (Components)

각 컴포넌트가 M2에서 M3로 진화하며 얻은 구체적인 UX 이점은 다음 문서에서 확인하세요.

- [[components-actions|M3 Actions: 버튼의 위계와 FAB의 변화]]
- [[components-containment-navigation|M3 Containment: 사용자를 움직이게 하는 네비게이션]]
- [[components-selection-inputs|M3 Selection: 더 직관적인 입력과 피드백]]

---

## 🔗 참고 링크 (References)
- [Material Design 공식 웹사이트](https://m3.material.io)
- [Design Google - Material 3 Expressive](https://design.google/library/material-3-expressive/)
