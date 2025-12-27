---
title: components-search
tags: [accessibility, adaptive, design-system, m3, material-design, search, ux-design]
aliases: [Search Bar, Search View, M3 Search Patterns]
date modified: 2025-12-28 00:29:10 +09:00
date created: 2025-12-28 00:29:10 +09:00
---

## 🔍 Search (검색): 효율적인 탐색과 발견

M3 검색 컴포넌트는 사용자가 필요한 정보를 가장 빠르고 직관적으로 찾을 수 있도록 돕습니다. 상황에 따라 'Search Bar' 와 'Search View' 로 구분하여 사용합니다.

## 🔎 Search Bar (검색바)

화면에 상시 노출되어 즉각적인 검색을 유도하는 기본 컴포넌트입니다.

### 1. 설계 의도 및 UX 가치

- **Primary Entry**: 앱의 핵심 기능이 검색일 때 최상단에 고정 배치합니다.
- **Visual Prompt**: 플레이스홀더 텍스트(예: "메모 검색")를 통해 사용자에게 어떤 행동을 해야 할지 명확히 안내합니다.
- **Configuration**: 아이콘, 프로필 아바타, 트레일링 버튼 등을 포함하여 다기능적인 입구 역할을 수행할 수 있습니다.

### 2. 레이아웃 팁

- **Marginal Space**: 양옆에 충분한 여백(보통 16dp)을 두어 다른 UI 요소와 격리하고 주목도를 높입니다.
- **Elevation**: 배경 콘텐츠와 구분하기 위해 낮은 레벨의 그림자나 Tonal 대비를 사용할 수 있습니다.

---

## 🖼️ Search View (검색 뷰)

검색바를 탭했을 때 확장되는 전면 검색 인터페이스입니다.

### 1. 주요 특징

- **Focused State**: 검색에만 집중할 수 있도록 전체 화면(Mobile) 또는 모달 대화창(Tablet/Desktop) 형태로 노출됩니다.
- **Dynamic Suggestions**: 타이핑과 동시에 관련 키워드나 최근 검색어를 실시간으로 제안하여 입력 수고를 덜어줍니다.
- **Adaptive Behavior**: 화면 크기에 따라 지능적으로 변합니다. 작은 화면에서는 전체 화면을 차지하지만, 넓은 화면에서는 검색바와 연결된 플로팅 패널 형태로 나타납니다.

---

## ♿ Accessibility (A11y)

### 1. 터치 및 포커스

- **Touch Targets**: 검색바 전체와 내부의 개별 버튼(삭제, 필터 등)은 최소 **48dp** 의 터치 영역을 가져야 합니다.
- **Auto-focus**: 검색 뷰가 열릴 때 키보드가 자동으로 올라오고 텍스트 필드에 포커스가 가도록 설정하여 동작 단계를 줄입니다.

### 2. 스크린 리더

- **Content Description**: 검색바의 아이콘이나 텍스트 필드에 명확한 레이블(예: "검색 시작")을 부여합니다.
- **Announcements**: 검색 결과가 갱신될 때마다 결과 개수(예: "30 개의 결과가 있습니다")를 음성으로 안내하는 것이 좋습니다.

---

## 🔗 관련 문서

- [[../material3_walkthrough|Material Design 3 개요 (Expressive Deep Dive)]]
- [[components-actions|Actions: 버튼과 FAB]]
- [[components-containment-navigation|Containment & Navigation]]
- [[components-feedback|Feedback: 로딩과 진행률]]
