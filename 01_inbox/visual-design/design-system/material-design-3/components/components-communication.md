---
title: components-communication
tags: [accessibility, communication, design-system, dialogs, m3, material-design, sheets, ux-design]
aliases: [Bottom Sheets, Dialogs, Snackbars, Tooltips, M3 Overlay Patterns]
date modified: 2025-12-28 00:29:20 +09:00
date created: 2025-12-28 00:29:20 +09:00
---

## 💬 Communication (커뮤니케이션): 시스템과의 대화

사용자에게 중요한 정보를 전달하거나 결정을 요청할 때 사용하는 오버레이 컴포넌트들입니다.

## 📢 Dialogs (다이얼로그)

사용자의 작업을 일시 중지시키고 중요한 인터랙션을 요구하는 모달 창입니다.

### 1. Basic vs Full-screen

- **Basic Dialog**: 짧은 메시지나 확인 동작에 사용 (예: 삭제 확인).
- **Full-screen Dialog**: 일정 생성, 복잡한 설정 등 많은 입력이 필요한 복합 작업에 사용.

### 2. 설계 주의사항

- **Minimalism**: 하나의 다이얼로그는 하나의 목적만 가져야 합니다. 결정 사항이 너무 많으면 별도의 화면으로 이동시키는 것이 좋습니다.
- **Scrim**: 배경을 어둡게 처리하여 사용자의 시선을 다이얼로그에 고정시킵니다.

---

## 📑 Bottom Sheets (바텀 시트)

화면 하단에서 올라오는 유연한 표면입니다.

### 1. Modal vs Standard

- **Modal Bottom Sheet**: 다이얼로그처럼 배경을 차단하고 사용자 응답을 기다립니다.
- **Standard Bottom Sheet**: 메인 콘텐츠와 병행하여 사용 가능하며, 보조적인 정보(예: 음악 플레이어 컨트롤)를 상시 노출할 때 유리합니다.

### 2. Interaction

- **Drag Handle**: 시트 상단에 핸들을 배치하여 스와이프를 통한 조절(확장/축소)이 가능함을 시각적으로 제안합니다.

---

## 💡 Overlays: Tooltips, Snackbars, Badges

### 1. Rich Tooltips

- M3 Expressive 에서는 단순히 텍스트만 보여주는 것이 아니라, 버튼이나 링크를 포함하여 **작은 정보 카드**처럼 작동할 수 있습니다.

### 2. Snackbars

- 작업 결과를 비방해적으로 알립니다 (예: "메시지가 전송되었습니다").
- **Dynamic Color**: 시스템 테마에 맞춰 배경색이 지능적으로 변하여 시각적 통일감을 줍니다.

### 3. Badges

- 아이콘이나 텍스트 위에 작은 수치를 표시하여 알림 상태를 알립니다. M3 에서는 4자리 이상의 큰 숫자보다는 `99+` 같은 압축된 표현을 권장합니다.

---

## ♿ Accessibility (A11y)

- **Dismissability**: 모든 오버레이는 '닫기' 버튼이나 외부 영역 탭, 뒤로 가기 버튼 등을 통해 쉽게 닫을 수 있어야 합니다.
- **Focus Trap**: 모달 다이얼로그가 열려 있을 때는 초점이 다이얼로그 내부에만 머물도록 고립시켜야 합니다.

---

## 🔗 관련 문서

- [[../material3_walkthrough|Material Design 3 개요 (Expressive Deep Dive)]]
- [[components-actions|Actions: 버튼과 FAB]]
- [[components-feedback|Feedback: 로딩과 진행률]]
- [[components-color-theme|Color & Theme: 지능적인 컬러 시스템과 HCT]]
