---
title: components-actions
tags: [buttons, design-system, expressive, fab, m3, material-design, ux-design]
aliases: [Expressive Buttons, M3 Actions, Shape Morphing Feedback]
date modified: 2025-12-27 23:51:33 +09:00
date created: 2025-12-27 22:56:00 +09:00
---

## ⚡ Actions (액션): 반응성에서 표현으로

M3 의 액션은 단순히 기능을 실행하는 수단을 넘어, **사용자와 대화하는 피드백 루프**입니다. "Expressive" 업데이트의 핵심은 상태 변화를 시각적인 '이야기'로 전달하는 것입니다.

---

## 🔘 Expressive Buttons: Shape Morphing Feedback

M3 버튼의 가장 큰 특징은 **Shape Morphing(형태 변형)**입니다.

![m3_buttons](../../../../../_assets/material_3/m3_buttons.png)

*<단순한 색상 변화를 넘어, 형태의 곡률이 변하며 '눌림'을 인지시키는 방식>*

### UX 적 개선 사항

1. **상태 피드백의 극대화**: Hover 상태에서 버튼의 둥글기가 미세하게 변하거나, Press 상태에서 완전히 다른 형태로 모르핑(Morphing)되는 것은 사용자가 자신의 행동이 성공적으로 입력되었음을 본능적으로 이해하게 합니다.
2. **Segmented Buttons 의 활용**: 여러 옵션을 하나로 묶어 표현하는 세그먼트 버튼은 연관된 행동들 사이의 시각적 리듬을 조절하여 디자인의 '표현력'을 높입니다.
3. **IconButton 의 위계**: Filled, Filled Tonal, Outlined 등 아이콘 버튼에도 세분화된 위계를 적용하여 화면의 복잡도를 제어합니다.

---

## 💎 FAB (Floating Action Button): Contextual Expression

FAB 는 정적인 버튼이 아닙니다. M3 Expressive 에서는 상황에 따라 형태와 위계가 유연하게 변합니다.

### 왜 Rounded Square(사각형)인가?

- **형태적 대조 (Visual Contrast)**: 원형 아이콘과 리스트 사이에서 사각형의 둥글기(Corner Radius)를 가진 FAB 는 '가장 중요한 행동'임을 더 강하게 암시합니다.
- **Dynamic Expansion**: 탭 하거나 스크롤 할 때 FAB 가 확장(Extended FAB)되거나 축소되는 모션은 사용자가 현재 하고 있는 작업의 맥락에 맞춰 시스템이 반응하고 있음을 보여줍니다.

---

## 🔗 관련 문서

- [[../material3_walkthrough|Material Design 3 개요 (Expressive Deep Dive)]]
- [[components-containment-navigation|Containment & Navigation]]
- [[components-typography|Typography: 의미론적 가독성과 폰트 역할]]
- [[components-color-theme|Color & Theme: 지능적인 컬러 시스템과 HCT]]
