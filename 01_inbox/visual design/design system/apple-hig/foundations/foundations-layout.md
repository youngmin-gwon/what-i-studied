---
title: foundations-layout
tags: [apple, design-system, hig, ios, layout, safe-area, ux-design]
aliases: [Apple Layout Guidelines, Safe Area, Layout Margins]
date modified: 2025-12-28 00:33:10 +09:00
date created: 2025-12-28 00:33:10 +09:00
---

## 📐 Layout (레이아웃): 공간의 질서와 적응성

Apple 의 레이아웃 시스템은 다양한 스크린 크기와 환경에서도 일관된 사용자 경험을 제공하도록 설계되었습니다.

## 🛡️ Safe Area (안전 영역)

안전 영역은 시스템에 의해 가려지지 않고 콘텐츠가 온전히 표시될 수 있는 영역을 정의합니다.

### 1. 설계 이유
- **센서 하우징 (Notch/Dynamic Island)**: 상단의 카메라 구멍이나 노치에 콘텐츠가 가려지는 것을 방지합니다.
- **시스템 제스처**: 하단의 홈 인디케이터 영역과 상호작용이 겹치지 않도록 보호합니다.
- **곡률 (Corners)**: 기기의 둥근 모서리에 의해 텍스트나 핵심 UI 가 잘려 나가는 것을 막습니다.

### 2. 레이아웃 가이드라인
- **Full-screen Immersion**: 배경 이미지나 동영상은 전체 화면으로 채우되, 텍스트나 버튼 같은 인터랙티브 요소는 반드시 **Safe Area 인셋(Insets)** 내부에 배치해야 합니다.

---

## 📏 Margins & Padding (여백과 간격)

Apple 디자인에서 여백은 정보를 숨 쉬게 하고 가독성을 높이는 핵심 도구입니다.

### 1. Layout Margins (레이아웃 마진)
- 화면 양쪽 끝에 부여되는 기본 여백입니다. 일반적으로 iOS 에서는 최소 **16pt** 에서 **20pt** 사이의 여백을 권장하며, 이는 사용자가 기기를 잡았을 때 손가락이 콘텐츠를 가리지 않게 하는 물리적인 이유도 포함됩니다.
- **Readable Content Guide**: 텍스트 줄이 너무 길어지지 않도록, 대화면 기기(iPad 등)에서는 마진을 넓혀 가독성을 확보합니다.

### 2. Spacing (간격)
- 관련 있는 요소는 가깝게, 다른 그룹은 멀게 배치하여 시각적 그룹화를 명확히 합니다 (Gestalt 원칙 적용).

---

## 📱 Adaptive Layout (적응형 레이아웃)

하나의 코드/디자인으로 iPhone 부터 Mac 까지 대응하는 지능형 구조입니다.

### 1. Size Classes (사이즈 클래스)
- **Compact**: iPhone(세로 모드)과 같이 공간이 제한된 환경.
- **Regular**: iPad나 Mac, iPhone(가로 모드 일부)과 같이 넓은 공간이 확보된 환경.
- **UX 전략**: Compact 일 때는 탭 바(Tab Bar)를 선호하고, Regular 일 때는 사이드바(Sidebar)를 사용하여 더 넓은 네비게이션을 제공합니다.

### 2. Auto Layout
- 제약 조건(Constraints) 기반의 동적 계산을 통해 화면 크기, 기기 방향, 다이내믹 타입(글자 크기 변경)에 실시간으로 반응합니다.

---

## ♿ Accessibility (A11y)

- **Large Content Viewer**: 글자 크기를 아주 크게 설정한 사용자가 탭 바나 툴바를 길게 누를 때, 해당 항목의 큰 미리보기를 화면 중앙에 띄워주는 기능을 고려해야 합니다.
- **Orientation Independence**: 가로/세로 모드 중 하나만 지원하는 것보다, 두 환경 모두에서 최적화된 레이아웃을 제공하는 것이 접근성의 기본입니다.

---

## 🔗 관련 문서
- [[../hig_walkthrough|Apple HIG 개요]]
- [[foundations-color-typography|Color & Typography]]
- [[../components/components-bars|Bars & Navigation]]
