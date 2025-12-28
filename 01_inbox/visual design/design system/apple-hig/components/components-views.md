---
title: components-views
tags: [apple, collection-view, design-system, hig, ios, list, table-view, ux-design]
aliases: [Apple Views, List Styles, Table View, Collection View, Split View]
date modified: 2025-12-28 00:36:00 +09:00
date created: 2025-12-28 00:36:00 +09:00
---

## 🖼️ Views (뷰): 데이터의 구조화와 제시

Apple 의 뷰 컴포넌트는 정보를 시각화하고 사용자가 대규모 데이터를 효율적으로 탐색할 수 있는 틀을 제공합니다.

## 📋 Lists & Tables (리스트와 테이블)

가장 보편적인 데이터 제시 방식으로, 단일 열의 수직 스크롤 목록입니다.

### 1. List Styles (iOS 표준)

- **Plain**: 경계선 없이 평면적으로 나열. 알람 목록이나 연락처 등에 주로 사용.
- **Grouped**: 항목들을 논리적 그룹으로 묶어 표시. 설정(Settings) 앱의 전형적인 스타일.
- **Inset Grouped**: 그룹화된 리스트가 배경에서 살짝 떨어져 둥근 모서리를 가진 형태. 현대적인 iOS UI 의 표준입니다.

### 2. 셀(Cell) 구성 요소

- **Leading**: 아이콘이나 이미지 배치.
- **Content**: 주요 제목과 보조 설명 텍스트.
- **Trailing**: 체크마크, 화살표(Disclosure Indicator), 혹은 스위치나 버튼 배치.

---

## 🧱 Collection Views (컬렉션 뷰)

그리드(Grid) 형태나 커스텀한 레이아웃이 필요할 때 사용하는 유연한 뷰입니다.

### 1. UX Rationale

- 사진 앱이나 앱스토어처럼 이미지 중심의 콘텐츠를 탐색할 때 최적입니다.
- **Compositional Layout**: 섹션마다 다른 그리드 크기나 스크롤 방향을 조합하여 풍성한 시각적 경험을 제공합니다.

---

## 🪟 Split Views (스플릿 뷰)

대화면(iPad, Mac)에서 여러 계층의 정보를 동시에 보여주는 계층 관리 도구입니다.

### 1. 구조

- **Primary (Sidebar)**: 최상위 카테고리.
- **Supplementary**: 중간 목록 (이메일 리스트 등).
- **Secondary (Detail)**: 최종 콘텐츠 표시부.

### 2. 적응형 동작

- 화면이 좁아지면(iPhone 등) 자동으로 단일 계층 내비게이션으로 전환되는 지능형 구조를 가집니다.

---

## ♿ Accessibility (A11y)

- **Self-sizing Cells**: 사용자가 폰트 크기를 키우면 리스트의 높이도 자동으로 늘어나 텍스트가 잘리지 않게 해야 합니다.
- **Reordering Labels**: 리스트 항목의 순서를 바꿀 때, 현재 어떤 항목을 잡고 어디로 이동 중인지 VoiceOver 가 실시간으로 안내해야 합니다.

---

## 🔗 관련 문서

- [[../hig_walkthrough|Apple HIG 개요]]
- [[components-bars|Bars: 네비게이션과 사이드바]]
- [[components-feedback|Feedback: 알림과 메뉴]]
