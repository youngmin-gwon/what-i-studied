---
title: M3 Components - Selection & Inputs (Accessibility & UX)
tags: [design-system, material-design, m3, input, selection, accessibility]
aliases: [M3 Selection, M3 Inputs Evolution]
date modified: 2025-12-27 23:15:00 +09:00
date created: 2025-12-27 22:58:00 +09:00
---

## 🔘 Selection (선택): 명확한 의사 표현

사용자가 옵션을 선택하거나 설정을 변경할 때, 시스템은 그 변화를 즉각적이고 명확하게 인지시켜야 합니다.

### 1. Switches: 포용적 디자인의 실천
M3 스위치는 M2보다 크기가 커졌으며, 핸들 내부에 **아이콘(체크/X 등)**을 포함할 수 있는 옵션이 생겼습니다.

**UX적 가치**:
- **접근성(Accessibility)**: 색상만으로 On/Off를 구분하기 힘든 저시력자나 색약 사용자를 위해 형태적 단서(아이콘)를 제공합니다.
- **터치 타겟 확장**: 더 커진 스위치는 모바일 환경에서 오터치를 줄여줍니다.

### 2. Chips: 맥락에 맞는 빠른 행동 유도
Chips는 단순히 태그가 아니라, 사용자의 다음 행동을 예측하여 제안하는 도구입니다. **Suggestion Chips**는 대화나 검색 맥락을 분석하여 사용자가 텍스트를 입력하는 수고를 덜어줍니다.

---

## ✍️ Inputs (입력): 시각적 노이즈 제거와 피드백

### 1. Text Fields: 가독성 중심의 진화
M3 텍스트 필드는 입력 영역과 라벨 사이의 관계를 더욱 명확히 합니다.
- **Error States**: 오류 발생 시 아이콘과 대비가 강한 붉은색을 사용하여 무엇이 잘못되었는지 즉각적으로 알립니다.
- **Support Text**: 입력 필드 하단에 실시간으로 글자 수나 형식을 안내하여 사용자의 실수를 미연에 방지합니다.

### 2. 가변 폰트(Variable Fonts)와 다이나믹 피드백
M3는 **Roboto Flex**와 같은 가변 폰트를 적극 활용합니다.
- **UX적 가치**: 사용자가 텍스트를 입력하는 동안 폰트의 두께나 너비가 미세하게 변하며 최적의 가독성을 유지합니다. 또한, 입력 중인 필드가 강조되는 방식이 더 부드러워져 '살아있는 시스템'과 대화하는 느낌을 줍니다.

---

## 🔗 관련 문서
- [[index|Material Design 3 개요 (UX Deep Dive)]]
- [[components-actions|Actions: 버튼과 FAB]]
- [[components-containment-navigation|Containment & Navigation]]
