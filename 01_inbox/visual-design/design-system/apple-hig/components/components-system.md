---
title: components-system
tags: [apple, badges, design-system, hig, ios, live-activities, notifications, widgets]
aliases: [Apple System Integration, Notifications, Widgets, Live Activities, Badges]
date modified: 2025-12-28 00:43:00 +09:00
date created: 2025-12-28 00:43:00 +09:00
---

## 🌐 System Integration (시스템 통합): 앱 너머의 경험

Apple 시스템과의 깊은 통합을 통해 앱을 열지 않고도 중요한 정보를 전달하고 제어할 수 있는 컴포넌트들입니다.

## 🔔 Notifications (알림)

사용자에게 때맞춰 중요한 정보를 전달합니다.

### 1. 알림 스타일

- **Banner**: 화면 상단에 짧게 나타났다 사라지는 방식.
- **Alert**: 사용자의 명시적 확인이 필요한 중단적 방식.
- **Interruption Levels**: Passive(조용함), Active(소리/진동), Time Sensitive(즉시 확인 필요), Critical(긴급 상황)로 구분됩니다.

### 2. 설계 주의사항

- **간결함**: 요점만 명확히 전달하며, 마케팅 용도로 남용하는 것을 지양합니다.
- **Interaction**: 알림 하단에 커스텀 버튼을 추가하여 앱을 열지 않고도 빠른 동작(예: 답장, 수락)을 수행하게 할 수 있습니다.

---

## 🖼️ Widgets (위젯)

홈 화면이나 잠금 화면에서 즉각적으로 정보를 확인하게 해주는 미니 뷰입니다.

### 1. 설계 원칙

- **Glanceability**: 2~3초 내에 핵심 내용을 파악할 수 있어야 합니다.
- **Simplicity**: 앱의 모든 기능을 담으려 하지 말고, 가장 가치 있는 정보 하나에 집중합니다.
- **Interactivity**: iOS 17 이후 버튼이나 토글 등을 통해 위젯 내에서 직접적인 조작이 가능해졌습니다.

---

## ⚡ Live Activities (실시간 현황)

진행 중인 이벤트(배달 상태, 스포츠 경기 스코어 등)를 잠금 화면과 Dynamic Island 에서 실시간으로 보여줍니다.

### 1. Dynamic Island 표현

- **Compact**: 아일랜드 양옆에 정보를 짧게 표시.
- **Minimal**: 여러 개의 활동이 있을 때 작은 원형으로 표시.
- **Expanded**: 길게 눌렀을 때 나타나는 상세 제어 화면.

---

## 🔴 Badges (배지)

앱 아이콘이나 탭 바 위에 나타나는 작은 수치 표시기입니다.

- **용도**: 확인하지 않은 알림의 개수를 직관적으로 보여줍니다.
- **주의**: 수치가 너무 커지거나 의미 없는 알림으로 배지를 채우는 것은 사용자의 피로도를 높입니다.

---

## ♿ Accessibility (A11y)

- **VoiceOver Integration**: 알림이 오거나 위젯의 정보가 갱신될 때 스크린 리더가 이를 가로채서 읽어줄 수 있도록 접근성 모델을 설계해야 합니다.
- **Dynamic Type**: 위젯 내의 텍스트도 설정된 글자 크기에 맞춰 가독성을 유지해야 합니다.

---

## 🔗 관련 문서

- [[../hig_walkthrough|Apple HIG 개요]]
- [[components-feedback|Feedback: 알림과 햅틱]]
- [[components-bars|Bars: 탭 바 배지]]
