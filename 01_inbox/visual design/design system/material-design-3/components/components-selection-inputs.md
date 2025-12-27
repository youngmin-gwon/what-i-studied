---
title: components-selection-inputs
tags: [accessibility, design-system, expressive, input, m3, material-design, selection, typography]
aliases: [Emphasized Typography, M3 Inputs Evolution, M3 Selection]
date modified: 2025-12-27 23:31:52 +09:00
date created: 2025-12-27 22:58:00 +09:00
---

## 🔘 Selection (선택): 표현적인 의사 결정

M3 의 선택 컴포넌트는 사용자가 '시스템을 제어하고 있다'는 감각을 시각적 피드백을 통해 강화합니다.

### 1. Switches: 포용적 디자인과 아이콘

M3 스위치는 단순히 크기가 커진 것이 아니라, **내러티브(Narrative) 아이콘**을 포함할 수 있습니다.

- **UX 적 가치**: 핸들 내에 체크(`v`)나 엑스(`x`) 아이콘을 배치하여, 색상뿐만 아니라 형태적 단서만으로도 현재 상태를 0.1 초 만에 파악하게 합니다. 이는 시인성을 4 배 이상 높이는 효과가 있습니다.

### 2. Emphasized Chips

- **Expressive Chips**: 상황에 맞는 **Suggestion Chips**는 디자인이 '살아있음'을 느끼게 합니다. 사용자가 입력할 내용을 미리 예측하여 제안하는 과정에서의 모션은 시스템에 대한 신뢰감을 형성합니다.

---

## 🎚️ Sliders (슬라이더): 정밀함과 탐색의 조화

M3 Expressive 슬라이더는 단순한 수치 조절 도구를 넘어, 풍부한 애니메이션과 지능적인 구성을 통해 시각적 피드백을 극대화합니다.

### 1. Slider Variants (슬라이더 유형)
- **Standard Slider (표준)**: 단일 값을 선택할 때 사용. 텍스트 필드보다 빠르고 직관적인 입력이 가능합니다.
- **Centered Slider (중앙 집중형)**: 양의 값과 음의 값을 동시에 가질 때 사용. 제로 포인트(0) 를 중심으로 균형 잡힌 조절이 가능합니다.
- **Range Slider (범위 선택형)**: 두 개의 핸들을 사용하여 특정 범위를 결정합니다 (예: 가격 범위).

### 2. Expressive Motion & States
- **Handle Feedback**: 핸들을 탭 하거나 드래그할 때 크기가 줄어들며 현재 수치(Value) 가 팝업으로 노출됩니다. 이는 손가락에 수치가 가려지는 문제를 해결하는 UX 적 배려입니다.
- **Dynamic Track**: 선택된 범위가 넓어질수록 트랙의 두께나 형태가 미세하게 반응하여 엔진의 '동력' 을 시각화합니다.

### 3. 설계 및 배치 팁
- **정밀도 vs 속도**: 슬라이더는 '정확한 숫자' 보다는 '탐색적 탐색' 에 적합합니다. 정확한 수치가 중요하다면 텍스트 입력 필드와 병행 배치하는 것이 좋습니다.
- **Stops (스톱)**: 특정 단계로만 이동해야 하는 경우(Discrete) 시각적인 점(Stops) 을 노출하여 사용자가 가용 옵션을 명확히 알게 하세요.

### 4. ♿ Accessibility (A11y)
- **Touch Target**: 슬라이더 핸들은 최소 **48dp** 의 터치 영역을 가져야 합니다.
- **Contrast**: 비활성화된 트랙과 배경 간의 대비를 최소 **3:1** 이상 유지하여 저시력 사용자도 범위를 인지할 수 있게 합니다.

---

## ✍️ Inputs (입력): 타이포그래피의 진화

입력 영역은 사용자가 가장 스트레스를 많이 받는 공간 중 하나입니다. M3 Expressive 는 이를 완화하기 위해 **강조된 타이포그래피**와 **다이나믹 피드백**을 도입했습니다.

### 1. Emphasized Typography in Text Fields

- **시각적 위계**: 입력 중인 텍스트는 **Roboto Flex** 가변 폰트의 축을 활용하여 굵기(Weight)와 자간이 지능적으로 조절됩니다. 이는 긴 문장을 입력할 때도 가독성을 잃지 않게 돕습니다.
- **Label Animation**: 필드를 탭 할 때 라벨이 상단으로 이동하며 작아지는 모션은 단순한 이동이 아닌, '입력 공간 확보'라는 논리적인 메시지를 전달합니다.

### 2. 다이나믹 피드백과 가변 폰트 (Variable Fonts)

- **실시간 반응**: 사용자가 타이핑하는 동안 폰트의 두께나 너비가 아주 미세하게 반응하여, 마치 종이 위에 글을 쓰는 듯한 자연스러운 피드백을 줍니다. 이는 입력 오류를 줄이고 사용자가 입력 과정 자체를 즐기게 만드는 정서적 이점이 있습니다.

---

---

## ♿ Accessibility (A11y): 데이터 입력의 정확성과 명확성

입력 도구는 복잡한 상호작용이 수반되므로, 사용자가 현재 무엇을 입력하고 있고 어떤 상태인지를 즉각 알 수 있어야 합니다.

### 1. Labeling & Instruction (레이블과 인스트럭션)
- **Always Visible Labels (영구 레이블)**: 입력창이 활성화되더라도 레이블(Label) 은 사라지지 않고 상단으로 부유(Floating) 해야 합니다. 이는 인지 장애가 있는 사용자가 "내가 무엇을 쓰고 있었지?" 하는 혼란을 겪지 않게 돕습니다.
- **Helper Text (보조 텍스트)**: 스크린 리더는 입력창에 포커스가 갈 때 해당 `helperText` 를 함께 읽어주어 입력 형식을 안내합니다.

### 2. Error & Validation (에러와 유효성)
- **Error Accessibility (에러 접근성)**: 에러 발생 시 단순히 빨간색으로 색을 바꾸는 것에 그치지 않고, 에러 아이콘을 병행하고 명확한 텍스트 메시지를 하단에 노출해야 합니다.
- **Immediate Feedback (즉각적 피드백)**: 입력 직후 유효성 검사 결과를 알려주어 사용자가 수고스럽게 전체 폼을 제출하고 다시 돌아오는 경험을 최소화합니다.

### 3. Selection Elements (선택 요소)
- **Touch Target (터치 타겟)**: Checkbox, Switch, Radio Button 은 시각적 크기보다 훨씬 넓은 터치 타겟(최소 48dp) 을 가져야 하며, 보통 옆의 텍스트 레이블을 클릭해도 선택되도록 설계합니다.

---

## 🔗 관련 문서

- [[../material3_walkthrough|Material Design 3 개요 (Expressive Deep Dive)]]
- [[components-actions|Actions: 버튼과 FAB]]
- [[components-containment-navigation|Containment & Navigation]]
- [[components-typography|Typography: 의미론적 가독성과 폰트 역할]]
- [[components-color-theme|Color & Theme: 지능적인 컬러 시스템과 HCT]]
