---
title: components-feedback
tags: [alerts, apple, context-menus, design-system, feedback, hig, ios, sheets, ux-design]
aliases: [Apple Feedback, Alert, Action Sheet, Context Menu, Activity Indicator]
date modified: 2025-12-28 00:36:10 +09:00
date created: 2025-12-28 00:36:10 +09:00
---

## 📢 Feedback (피드백): 소통과 제어

사용자에게 상태를 알리고, 흐름을 잠시 멈춰 결정을 요구하거나 보조 기능을 제공하는 오버레이 컴포넌트들입니다.

## 🚨 Alerts (알림)

중대한 정보를 전달하거나 중단이 필요한 결정을 요구하는 모달 형태의 창입니다.

### 1. 사용 원칙

- **절제**: 사용자의 흐름을 완전히 막으므로 꼭 필요한 경우(데이터 삭제, 구매 확인 등)에만 제한적으로 사용합니다.
- **버튼 배치**: 일반적으로 부정적/취소 액션은 왼쪽, 긍정적/확인 액션은 오른쪽에 배치합니다. 파괴적인 액션(삭제 등)은 빨간색 컬러를 부여합니다.

---

## 📑 Action Sheets & Panes (액션 시트)

현재 맥락과 관련된 두 개 이상의 선택지를 제공합니다.

### 1. UX Rationale

- 주로 하단에서 위로 슬라이드되며 나타납니다 (Mobile).
- **Secondary Choices**: 특정 버튼을 눌렀을 때 파생되는 여러 동작을 나열하기에 적합합니다.

---

## 🖱️ Context Menus (컨텍스트 메뉴)

특정 요소(메시지, 사진, 파일 등)를 길게 누를 때 나타나는 보조 명령 모음입니다.

### 1. 핵심 특징

- **Preview**: 메뉴와 함께 해당 요소의 미리보기를 함께 띄워 맥락을 유지합니다.
- **Hierarchy**: 가장 자주 쓰는 기능을 상단에 배치하고, 하단에 그룹화된 보조 기능을 둡니다.

---

## ⏳ Indicators: Activity & Progress

작업 진행 상태를 시각화합니다.

### 1. Activity Indicator (활동 인디케이터)

- 시간 소요를 알 수 없는 불확정적인 상황(로딩 중)에 회전하는 휠 형태로 표시됩니다.

### 2. Progress Bar (프로그레스 바)

- 작업의 완료 시점을 알 수 있는 확정적인 상황(파일 다운로드 등)에 선형으로 진행률을 보여줍니다.

---

## ♿ Accessibility (A11y)

- **Haptic Feedback**: 알람이 뜨거나 성공/실패 시 시스템 표준 햅틱 엔진을 사용하여 사용자에게 물리적 확신을 줍니다.
- **Focus Management**: 알람이나 모달이 열리면 포커스가 해당 오버레이 내부에 갇히도록 하여 시각 장애 사용자가 엉뚱한 배경 요소를 건드리지 않게 보호합니다.

---

## 🔗 관련 문서

- [[../hig_walkthrough|Apple HIG 개요]]
- [[components-views|Views: 리스트와 테이블]]
- [[components-controls|Controls: 버튼과 전환]]
