---
title: M3 Components - Containment & Navigation
tags: [design-system, material-design, m3, cards, navigation, ux-design]
aliases: [M3 Containment, M3 Navigation Evolution]
date modified: 2025-12-27 23:12:00 +09:00
date created: 2025-12-27 22:57:00 +09:00
---

## 📦 Containment (수용)

콘텐츠를 논리적으로 묶어 사용자가 정보의 구조를 한눈에 파악하게 하는 '그릇' 역할을 합니다.

### 1. Cards: 명확한 상태 구분
M3 카드는 M2보다 그림자(Elevation)의 사용을 줄이고, 색상과 외곽선을 통해 상태를 구분합니다. 이는 화면을 덜 복잡하게 보이게 하여 **시각적 노이즈를 줄이는 효과**가 있습니다.

---

## 🧭 Navigation: 사용자를 위한 길안내

M3의 네비게이션은 사용자가 '자신이 어디에 있는지'를 직관적으로 알 수 있게 하는 데 집중합니다.

### 1. Navigation Bar (Pill Indicator)
가장 큰 변화 중 하나는 선택된 메뉴를 표시하는 **Pill 형태의 활성 인디케이터**입니다.

![M3 Navigation Pill Indicator](file:///Users/youngmin/Documents/Obsidian/what-i-studied/01_inbox/visual%20design/design%20system/material-design-3/_assets/nav_pill.png)
*<배경색이 채워진 캡슐 형태를 통해 현재 위치를 즉각적으로 인지할 수 있음>*

**UX적 개선 사항**:
- **가독성(Legibility)**: M2의 단순 아이콘 색상 변화보다 훨씬 명확한 시각적 피드백을 제공합니다.
- **접근성(Accessibility)**: 색각 이상이 있는 사용자도 명암 대비와 형태의 변화를 통해 활성 상태를 더 쉽게 구분할 수 있습니다.

### 2. Adaptive Navigation Layout
기기의 화면 크기에 따라 네비게이션 형태가 유연하게 변합니다.
- **Mobile**: 하단 Navigation Bar.
- **Tablet/Foldable**: 측면 Navigation Rail (공간 효율성 극대화).
- **Desktop**: Navigation Drawer (더 깊은 서비스 계층 구조 표현).

---

## 🔗 관련 문서
- [[index|Material Design 3 개요 (UX Deep Dive)]]
- [[components-actions|Actions: 버튼과 FAB]]
- [[components-selection-inputs|Selection & Inputs]]
