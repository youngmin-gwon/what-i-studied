---
title: components-macos
tags: [apple, design-system, desktop, hig, macos, menu-bar, window]
aliases: [macOS Specific Patterns, Menu Bar, Windowing, Desktop Layout]
date modified: 2025-12-28 00:45:00 +09:00
date created: 2025-12-28 00:45:00 +09:00
---

## 🖥️ macOS Specific Patterns (데스크탑 패턴)

macOS 는 정밀한 포인팅 기기(마우스/트랙패드)와 넓은 화면을 기반으로 하는 생산성 중심의 환경입니다.

## 🖱️ Menu Bar (메뉴 바)

화면 최상단에 고정된 전역 명령 센터입니다.

### 1. 메뉴 구성

- **Apple Menu**: 시스템 전역 설정.
- **App Menu**: 현재 활성화된 앱의 이름으로 표시되며, 설정/종료를 담당.
- **Standard Menus**: 파일, 편집, 보기, 윈도우, 도움말 등 익숙한 범주를 유지.

### 2. 가용성 (Availability)

- 활성화되지 않은 명령은 숨기는 대신 **비활성화(Dimmed)** 처리하여 사용자가 해당 기능의 존재를 인지할 수 있게 돕습니다.

---

## 🪟 Windows (윈도우)

앱 콘텐츠를 담는 최상위 컨테이너입니다.

- **Toolbar**: 윈도우 상단에 핵심 동작을 배치하며, 사이드바와 유기적으로 결합됩니다.
- **Panels**: 보조적인 도구 모음으로, 메인 윈도우 위에 떠 있거나 자석처럼 붙을 수 있습니다.

---

## ⚙️ Settings (설정)

macOS 의 설정은 전통적으로 탭 바가 상단에 위치한 가로형 대화창 스타일을 선호해 왔으나, 최근에는 iOS/iPadOS 와 유사한 사이드바 기반의 리스트 스타일로 통합되고 있습니다.

---

## ♿ Accessibility (A11y)

- **Keyboard Shortcuts**: 모든 메뉴 명령에는 키보드 단축키를 부여하여 생산성과 접근성을 동시에 높여야 합니다.
- **Hover Effects**: 마우스 커서가 올라갔을 때의 변화를 통해 인터랙티브 요소를 명확히 구분합니다.

---

## 🔗 관련 문서

- [[../hig_walkthrough|Apple HIG 개요]]
- [[components-bars|Bars: 사이드바와 내비게이션]]
- [[components-views|Views: 테이블과 컬렉션]]
