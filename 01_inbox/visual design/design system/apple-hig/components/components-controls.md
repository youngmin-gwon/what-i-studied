---
title: components-controls
tags: [apple, buttons, controls, design-system, hig, ios, pickers, sliders, ux-design]
aliases: [Apple Controls, Button Styles, Segmented Control, Picker, Switch]
date modified: 2025-12-28 00:38:00 +09:00
date created: 2025-12-28 00:38:00 +09:00
---

## 🎛️ Controls (제어): 의사 표현의 기본 단위

Apple 의 표준 제어 컴포넌트들은 사용자의 의도를 시스템에 전달하는 가장 작은 상호작용 단위입니다.

## 🔘 Buttons (버튼)

기능을 실행하거나 명령을 내리는 가장 보편적인 도구입니다.

### 1. Button Styles (iOS 표준 스타일)

- **Plain**: 가장 낮은 위계. 탭 바, 툴바 등 배경이 없는 환경에서 주로 사용.
- **Gray**: 중간 위계. 주변 콘텐츠와 구분되면서도 너무 튀지 않아야 할 때 적합.
- **Tinted**: 강조가 필요하지만 1 순위는 아닐 때. 시스템 강조색(System Blue 등)이 옅게 깔림.
- **Filled**: 최상위 위계(Primary). 프로세스를 완료하거나 가장 중요한 액션에 부여.

### 2. 설계 원칙

- **Verb-driven Title**: 버튼 이름은 항상 '동사'로 시작하여 무엇이 일어날지 예견하게 합니다 (예: '저장', '보내기').
- **44pt Target**: 실제 시각적 크기와 관계없이 터치 가능한 물리 영역은 반드시 **44 x 44 pt** 이상이어야 합니다.

---

## 🛞 Pickers & Date Pickers (피커)

여러 옵션 중 하나를 선택하거나 날짜를 입력할 때 사용합니다.

### 1. Picker Styles

- **Compact**: 탭했을 때 메뉴나 모달 형태로 나타나 공간을 절약합니다.
- **Inline**: 리스트나 텍스트 하단에 바로 노출되어 흐름을 이어가게 합니다.
- **Wheel**: 스크롤하며 선택하는 Apple 고유의 휠 스타일.

### 2. 사용 팁

- 항목이 10 개 이상이면 피커를, 5 개 미만이면 세그먼트 컨트롤이나 버튼 그룹을 고려하세요.

---

## 🎚️ Sliders & Steppers (슬라이더와 스테퍼)

연속적인 값이나 단계적 변화를 제어합니다.

### 1. Slider (슬라이더)

- **방향성**: 왼쪽(최소)에서 오른쪽(최대)으로 이동하는 것이 기본입니다.
- **시야 확보**: 슬라이더를 조작하는 손가락이 현재 수치를 가리지 않도록, 보조 텍스트를 상단이나 핸들 근처에 적절히 배치해야 합니다.

### 2. Stepper (스테퍼)

- 정밀한 1 단위 조절이 필요할 때 사용합니다 (예: 인원수 선택, 수량 조절).

---

## 🔘 Segmented Controls & Switches (세그먼트와 스위치)

상태를 전환하거나 상호 배타적인 옵션을 선택합니다.

### 1. Segmented Control

- 2~5 개의 옵션 사이를 전환할 때 사용합니다 (예: 지도 타입 전환 - 일반/위성).
- **제한**: 화면 너비의 한계로 인해 아이폰에서는 5 개 이하의 세그먼트 배치를 권장합니다.

### 2. Switch (스위치)

- On/Off 의 이진 상태를 토글할 때 사용합니다. 주로 설정 앱과 같은 리스트 형태에서 가장 강력한 위계를 가집니다.

---

## ♿ Accessibility (A11y)

- **Button Labels**: 아이콘 버튼의 경우, 시각적으로 이름이 없더라도 VoiceOver 를 위한 의미론적 레이블(예: "닫기 버튼")이 반드시 포함되어야 합니다.
- **Haptic Feedback**: 스위치를 켜거나 슬라이더가 특정 값에 도달할 때 미세한 햅틱 반응을 제공하여 조작의 확신을 줍니다.

---

## 🔗 관련 문서

- [[../hig_walkthrough|Apple HIG 개요]]
- [[../foundations/foundations-layout|Layout: 44pt 히트 타겟]]
- [[components-inputs|Inputs: 텍스트와 검색]]
