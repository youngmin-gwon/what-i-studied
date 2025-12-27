---
title: M3 Components - Actions (UX Evolution)
tags: [design-system, material-design, m3, buttons, fab, ux-design]
aliases: [M3 Actions, M3 Buttons vs M2]
date modified: 2025-12-27 23:10:00 +09:00
date created: 2025-12-27 22:56:00 +09:00
---

## ⚡ Actions (액션)

액션 컴포넌트는 사용자가 주요 기능이나 프로세스를 실행하도록 돕는 접점입니다. M3에서는 버튼의 크기, 형태, 색상 체계를 개편하여 **의사결정의 명확성**을 높였습니다.

---

## 🔘 Buttons: M2 vs M3

M3 버튼은 M2보다 더 크고(40dp height), 모서리가 완전히 둥글게(Full rounded) 바뀌었습니다.

![M2 vs M3 Buttons Comparison](file:///Users/youngmin/Documents/Obsidian/what-i-studied/01_inbox/visual%20design/design%20system/material-design-3/_assets/m3_buttons.png)
*<M2의 딱딱한 직사각형 형태에서 M3의 부드럽고 가독성 높은 형태로의 변화>*

### UX적 개선 사항:
1.  **위계의 세분화 (Hierarchical Clarity)**:
    - M2는 주로 Filled와 Outlined 두 가지만 사용했지만, M3는 **5가지 타입**을 제공합니다.
    - **Elevated / Filled / Filled Tonal / Outlined / Text** 순으로 중요도를 미세하게 조절할 수 있어, 화면 내에서 사용자가 무엇을 먼저 눌러야 할지 고민하는 시간을 줄여줍니다.
2.  **가독성 향상**: 버튼 높이가 높아지면서 텍스트 주변의 여백이 확보되어 시각적 편안함을 제공합니다.
3.  **상태 피드백**: Hover, Focus, Press 상태에서 색상 뿐만 아니라 **그림자의 깊이나 형태의 미세한 변화**를 통해 액션이 실행될 것임을 더 명확히 알립니다.

---

## 💎 FAB (Floating Action Button)

FAB는 화면에서 가장 중요한 단일 액션을 상징합니다. M3에서는 이 형태가 원형에서 **Rounded Square**로 드라마틱하게 변했습니다.

### 왜 사각형으로 바뀌었나?
- **시각적 구분**: 원형 아이콘들과 섞여 있을 때, 사각형에 가까운 형태가 '액션'임을 더 강하게 암시합니다.
- **적응성 (Adaptability)**: Large FAB 타입이 추가되어 태블릿이나 데스크탑 같은 큰 화면에서도 위계를 잃지 않습니다.
- **브랜드 정체성**: 사각형의 둥글기(Corner Radius)를 조절함으로써 브랜드 고유의 룩앤필을 반영하기 수월해졌습니다.

---

## 🔗 관련 문서
- [[index|Material Design 3 개요 (UX Deep Dive)]]
- [[components-containment-navigation|Containment & Navigation]]
