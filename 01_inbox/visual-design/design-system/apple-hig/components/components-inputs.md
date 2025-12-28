---
title: components-inputs
tags: [apple, design-system, hig, inputs, ios, search, text-field, ux-design]
aliases: [Apple Inputs, Text Field, Search Bar, Text View]
date modified: 2025-12-28 00:40:00 +09:00
date created: 2025-12-28 00:40:00 +09:00
---

## ✍️ Inputs (입력): 명확한 정보 수집

사용자가 텍스트를 입력하거나 방대한 데이터에서 정보를 걸러내는 도구들입니다.

## 📝 Text Fields & Text Views (텍스트 입력)

한 줄 또는 여러 줄의 텍스트를 입력받을 때 사용합니다.

### 1. Text Field (한 줄 입력)

- **Placeholder**: 필드가 비어 있을 때 목적을 안내합니다 (예: "이메일 주소").
- **Clear Button**: 입력한 내용을 한 번에 지울 수 있는 리셋 버튼을 우측 끝에 배치하는 것이 관정됩니다.
- **Security**: 암호 입력 시 `Secure Text Field` 를 사용하여 입력값이 점(`•`)으로 처리되게 합니다.

### 2. Text View (여러 줄 입력)

- 장문의 글을 작성할 때 사용하며, 스크롤 기능을 내장합니다.

### 3. 입력 최적화 (UX 팁)

- **Keyboard Matching**: 이메일이면 `@`가 포함된 자판을, 숫자면 숫자 키패드를 자동으로 띄워 입력 단계를 최적화합니다.

---

## 🔍 Search Bar (검색바)

검색은 앱 내 콘텐츠로 향하는 가장 빠른 통로입니다.

### 1. 구성 요소

- **Search Field**: 돋보기 아이콘과 플레이스홀더를 포함한 영역.
- **Cancel Button**: 검색 상태를 종료하고 이전 환경으로 돌아가는 버튼.

### 2. 배치 및 동작

- **Large Title 과의 조화**: 스크롤 시 검색바가 제목 뒤로 숨거나 나타나는 지능적인 모션을 제공하여 공간을 효율적으로 사용합니다.
- **Scope Bar**: 결과 내에서 필터링이 필요할 때 검색바 하단에 추가 범주를 제공할 수 있습니다.

---

## 🔘 Selection Patterns (선택 패턴)

항목을 선택하는 Apple 스타일의 방식입니다.

### 1. Checkmarks in Lists (리스트 체크마크)

- iOS 에서는 별도의 체크박스 오브젝트보다, 리스트 항목의 우측(Trailing)에 체크 아이콘이 나타나는 방식을 선호합니다 (다중 선택 시 유용).

### 2. Edit Menus (편집 메뉴)

- 텍스트나 객체를 길게 누를 때 나타나는 '복사', '붙여넣기' 풍선 도움말입니다. 시스템 표준을 사용하여 사용자가 학습 없이도 조작하게 합니다.

---

## ♿ Accessibility (A11y)

- **Instructional Context**: 텍스트 필드가 포커스 되었을 때, 어떤 정보를 입력해야 하는지 VoiceOver 가 충분히 설명할 수 있도록 힌트(Hint)를 제공합니다.
- **Dynamic Type**: 텍스트 필드의 글자 크기가 커져도 내부 레이아웃이 깨지지 않고 유동적으로 늘어나야 합니다.

---

## 🔗 관련 문서

- [[../hig_walkthrough|Apple HIG 개요]]
- [[components-controls|Controls: 버튼과 피커]]
- [[components-views|Views: 리스트와 테이블]]
