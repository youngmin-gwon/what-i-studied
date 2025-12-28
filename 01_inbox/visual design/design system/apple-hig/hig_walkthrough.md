---
title: Apple HIG Walkthrough
tags: [apple, design-system, hig, ios, macos, ux-design]
aliases: [HIG Overview, Apple Design Principles]
date modified: 2025-12-28 00:33:00 +09:00
date created: 2025-12-28 00:33:00 +09:00
---

# 🍎 Apple Human Interface Guidelines (HIG)

Apple 의 HIG 는 전 세계 수십억 명의 사용자가 직관적으로 시스템을 이해하고 조작할 수 있도록 설계된 **사용자 경험의 표준**입니다. 이 문서는 Apple 플랫폼(iOS, iPadOS, macOS, watchOS, visionOS) 전반에 적용되는 핵심 원칙과 디자인 사양을 깊게 탐구합니다.

---

## 💎 Apple Design Principles (핵심 원칙)

Apple 의 디자인은 단순한 심미성을 넘어, 다음과 같은 철학적 뿌리를 가집니다.

### 1. Aesthetic Integrity (심미적 무결성)
- 제품의 형태와 기능이 얼마나 조화로운가를 측정합니다.
- **예시**: 작업에 집중해야 하는 데이터 도구는 배경으로 물러나고, 몰입이 필요한 게임이나 미디어 앱은 화려하고 역동적인 인터페이스를 가집니다.

### 2. Consistency (일관성)
- 시스템이 제공하는 표준 컴포넌트, 잘 알려진 아이콘 스타일, 친숙한 상호작용 방식을 사용하여 사용자가 새로운 앱을 배울 필요가 없게 합니다.

### 3. Direct Manipulation (직접 조작)
- 화면의 가상 객체를 실제 물건처럼 다루는 감각을 제공합니다.
- **동작**: 기기를 기울여 반응을 보거나, 제스처를 통해 객체를 이동/회전시키는 행위 등이 포함됩니다.

### 4. Feedback (피드백)
- 모든 사용자 행동에는 시각적, 청각적, 또는 햅틱(Haptic) 반응이 즉각적으로 뒤따라야 합니다. 사용자는 시스템이 자신의 명령을 수행 중임을 확신해야 합니다.

### 5. Metaphors (은유)
- 실제 세상에서의 물리적 경험을 UI 에 투영합니다.
- **예시**: 페이지를 넘기는 듯한 스와이프, 제어 센터의 스위치 조절 등.

### 6. User Control (사용자 제어권)
- 시스템이 아닌 사용자가 항상 주도권을 가집니다. 시스템은 위험을 경고하거나 제안할 수 있지만, 최종 결정은 사용자의 몫이어야 합니다.

---

## 🗺️ Documentation Index (문서 인덱스)

이 가이드는 Apple HIG 의 방대한 사양을 다음과 같은 체계로 분류하여 설명합니다.

### 🛠️ Foundations (기초 사양)
- [[foundations/foundations-layout|Layout]]: 안전 영역(Safe Area), 레이아웃 가이드 및 적응형 구조.
- [[foundations/foundations-color-typography|Color & Typography]]: 시스템 컬러, 다이내믹 타입, SF Symbols, 그리고 **Liquid Glass(리퀴드 글래스)** 물성 사양.

### 🧱 Components (UI 컴포넌트)
- [[components/components-bars|Bars & Navigation]]: 내비게이션 바, 탭 바, 사이드바.
- [[components/components-controls|Controls]]: 버튼, 피커, 슬라이더, 스위치.
- [[components/components-inputs|Inputs]]: 텍스트 필드, 검색바, 선택 패턴.
- [[components/components-views|Views & Containment]]: 리스트, 테이블, 컬렉션, 스플릿 뷰.
- [[components/components-feedback|Feedback & Overlays]]: 알림(Alerts), 시트, 팝오버, 햅틱 피드백.
- [[components/components-system|System Integration]]: 위젯, 실시간 현황(Live Activities), 알림 시스템.
- [[components/components-macos|macOS Specifics]]: 메뉴 바, 윈도우 스타일, 데스크탑 최적화.
- [[components/components-spatial|Spatial Computing (visionOS)]]: 윈도우, 볼륨, 오너먼트 및 시선/손 조작 체계.

---

## ♿ Accessibility (접근성)
Apple 은 접근성을 '태초부터 배제되지 않는 경험'으로 정의합니다. 모든 문서는 다음 사양을 기본적으로 포함합니다.
- **Dynamic Type**: 가변 글꼴 크기 지원.
- **VoiceOver**: 스크린 리더를 위한 의미론적 레이블링.
- **Reduce Motion**: 운동 능력이나 시각적 자극에 민감한 사용자를 위한 모션 최적화.

---

## 🔗 관련 링크
- [Official Apple HIG](https://developer.apple.com/design/human-interface-guidelines)
- [[../material-design-3/material3_walkthrough|Material Design 3 와의 비교 분석]]
