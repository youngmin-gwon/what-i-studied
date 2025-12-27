---
title: components-bars
tags: [apple, design-system, hig, ios, navigation, tab-bar, toolbar, ux-design]
aliases: [Navigation Bar, Tab Bar, Toolbar, Sidebar, Status Bar]
date modified: 2025-12-28 00:35:00 +09:00
date created: 2025-12-28 00:35:00 +09:00
---

## 🏗️ Bars (바): 구조와 탐색의 명확성

Apple 의 바(Bars) 컴포넌트는 사용자가 앱 내에서 길을 잃지 않게 하고, 현재 맥락에서 가장 필요한 도구를 적재적소에 배치하는 역할을 합니다.

## 🧭 Navigation Bar (내비게이션 바)

화면 상단에 위치하며, 현재 위치를 알리고 계층 구조를 탐색하게 돕습니다.

### 1. 주요 기능
- **계층적 탐색**: 이전 화면으로 돌아가는 'Back' 버튼을 제공합니다.
- **제목(Titles)**: 현재 화면의 이름을 명확히 표시합니다. iOS 11 이후부터는 스크롤 시 작아지는 **Large Title** 형식을 지원하여 콘텐츠의 시작을 강조합니다.
- **액션**: '편집', '추가' 와 같은 보조 동작을 우측(Trailing) 에 배치합니다.

### 2. 설계 원칙
- **Translucency (반투명)**: 콘텐츠가 바 아래로 흐를 때 살짝 비치게 하여 화면의 깊이감과 공간감을 유지합니다.

---

## 📑 Tab Bar (탭 바)

앱의 최상위 메뉴를 구분하며, 일반적으로 화면 하단에 위치합니다.

### 1. UX Rationale
- **Flat Hierarchy**: 앱의 주요 기능(보통 3~5개)을 평면적으로 나열하여 사용자가 한 번의 탭으로 핵심 영역 사이를 빠르게 전환할 수 있게 합니다.
- **Visual Feedback**: 현재 선택된 탭을 활성 컬러(System Blue 등)로 강조하여 위치 정보를 제공합니다.

### 2. 설계 팁
- **Badge**: 읽지 않은 메시지나 알림이 있을 때 작은 수치 배지를 사용하여 사용자의 주의를 끕니다.

---

## 🛠️ Toolbar (툴바)

현재 화면의 콘텐츠와 직접적으로 관련된 동작을 제공하며, 보통 화면 하단에 위치합니다.

### 1. Tab Bar 와의 차이
- **Tab Bar** 는 '이동(Navigation)'이 목적이지만, **Toolbar** 는 '행동(Action)'이 목적입니다 (예: 메일 삭제, 답장, 보관).

### 2. 배치 전략
- 상황에 따라 유동적으로 나타나거나 사라질 수 있으며, 키보드가 올라올 때는 키보드 상단에 부착(Input Accessory View)되기도 합니다.

---

## 🖥️ Sidebar (사이드바)

iPadOS 와 macOS 에서 대화면의 이점을 활용하여 복잡한 앱 구조를 한눈에 조망하게 합니다.

- **장점**: 대량의 폴더나 카테고리를 관리하기에 최적이며, 드래그 앤 드롭을 통한 콘텐츠 이동을 직관적으로 지원합니다.

---

## ♿ Accessibility (A11y)

- **Minimum Text Size**: 바 내부의 텍스트가 다이내믹 타입에 반응하더라도, 최소한의 가독성을 해치지 않는 범위 내에서 조정되어야 합니다.
- **Standard Glyphs**: 시스템에서 제공하는 표준 아이콘(SF Symbols)을 사용하여 사용자가 기능을 학습하지 않고도 바로 이해할 수 있게 합니다.

---

## 🔗 관련 문서
- [[../hig_walkthrough|Apple HIG 개요]]
- [[../foundations/foundations-layout|Layout: 공간의 질서]]
- [[components-controls|Controls: 버튼과 입력]]
