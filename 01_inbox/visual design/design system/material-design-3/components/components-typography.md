---
title: components-typography
tags: [design-system, expressive, m3, material-design, material-theme, typography, ux-design]
aliases: [Emphasized Typography, M3 Type Scale, MaterialTheme Fonts, Typography Roles, Typography Specs]
date modified: 2025-12-27 23:40:32 +09:00
date created: 2025-12-27 23:28:00 +09:00
---

## 🔤 M3 Typography: 의미론적 가독성

Material Design 3 의 타이포그래피는 단순한 크기 조정을 넘어, **정보의 중요도와 맥락**을 사용자에게 전달하는 semantic(의미론적) 도구입니다. 특히 "Expressive" 업데이트로 추가된 **Emphasized(강조)** 스타일은 더 동적이고 위계가 뚜렷한 UI 를 가능하게 합니다.

---

## 🏗️ Typography Roles & Technical Specs

모든 텍스트 스타일은 가독성과 리듬을 위해 정밀하게 설계되었습니다. (단위: `sp` / 안드로이드 기준)

| Category | Role | Font Size | Line Height | Letter Spacing | Initial Weight |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Display** | Large | 57sp | 64sp | -0.25sp | Regular |
| | Medium | 45sp | 52sp | 0sp | Regular |
| | Small | 36sp | 44sp | 0sp | Regular |
| **Headline**| Large | 32sp | 40sp | 0sp | Regular |
| | Medium | 28sp | 36sp | 0sp | Regular |
| | Small | 24sp | 32sp | 0sp | Regular |
| **Title** | Large | 22sp | 28sp | 0sp | Regular |
| | Medium | 16sp | 24sp | 0.15sp | Medium |
| | Small | 14sp | 20sp | 0.1sp | Medium |
| **Body** | Large | 16sp | 24sp | 0.5sp | Regular |
| | Medium | 14sp | 20sp | 0.25sp | Regular |
| | Small | 12sp | 16sp | 0.4sp | Regular |
| **Label** | Large | 14sp | 20sp | 0.1sp | Medium |
| | Medium | 12sp | 16sp | 0.5sp | Medium |
| | Small | 11sp | 16sp | 0.5sp | Medium |

---

## 🎨 Role 별 제작 의도 및 사용 사례

### 1. Display (디스플레이)

- **제작 의도**: 대화면 기기에서 시선을 강력하게 끌어당기거나, 짧고 중요한 숫자를 표현하기 위함입니다.
- **Emphasized**: 더 굵고 대담한 버전으로 정서적 임팩트가 필요한 순간에 사용됩니다.
- **권장 상황**: 메인 대시보드 지표, 랜딩 페이지의 핵심 메시지.

### 2. Headline (헤드라인)

- **제작 의도**: 본문 덩어리를 논리적으로 구분하는 '이정표' 역할을 합니다.
- **Emphasized**: '잡지(Editorial)' 스타일의 대담한 섹션 전환에 적합합니다.
- **권장 상황**: 섹션 제목, 카테고리 헤더.

### 3. Title (타이틀)

- **제작 의도**: 모듈화된 정보(리스트 아이템, 다이얼로그 등)의 이름을 정의하기 위함입니다.
- **Emphasized**: 선택된 상태나 사용자의 주의가 즉각적으로 필요한 요소에 사용합니다.
- **권장 상황**: 리스트 아이템의 제목, 팝업창의 타이틀.

### 4. Body (바디)

- **제작 의도**: 장문의 글을 읽을 때 피로도를 낮추는 가독성(Legibility) 위주로 설계되었습니다.
- **권장 상황**: 게시글 본문, 설명 텍스트. (Body 는 강조를 위해 스타일을 바꾸기보다 굵기만 조절하는 것을 권장합니다.)

### 5. Label (레이블)

- **제작 의도**: 버튼의 글자나 캡션처럼 특정 기능을 보조하거나 설명하는 실용적인 텍스트입니다.
- **Emphasized**: 활성화된 버튼이나 강조가 필요한 메타데이터에 적합합니다.
- **권장 상황**: 버튼 텍스트, 캡션, 태그 내부 글자.

---

## 📈 Dynamic Scaling & Adaptive Typography

M3 Typography 는 환경에 따라 지능적으로 반응합니다.

### 1. Line Height Scaling (행간 비례)

- **원칙**: 텍스트의 크기가 커질수록 행간은 상대적으로 좁아져야 정보의 응집력이 유지됩니다. 반대로 본문(`Body`)은 충분한 행간(약 1.4~1.5 배)을 두어 눈의 피로를 줄입니다.

### 2. Letter Spacing (자간 조정)

- **원칙**: 큰 텍스트(`Display`, `Headline`)는 자간을 좁혀서(Negative Spacing) 시각적 흩어짐을 방지하고, 작은 텍스트(`Label`, `BodySmall`)는 자간을 넓혀서 글자 간 간섭을 줄입니다.

### 3. Adaptive Width (가변 너비)

- **Expressive Update**: 사용자의 접근성 설정이나 기기의 가로 너비에 따라 폰트의 `Width`(너비) 축이 미세하게 조절되어, 화면을 가득 채우거나 정보를 더 빽빽하게 담을 수 있도록 돕습니다.

---

## 🔗 관련 문서

- [[../material3_walkthrough|Material Design 3 개요 (Expressive Deep Dive)]]
- [[components-actions|Actions: 버튼과 FAB]]
- [[components-selection-inputs|Selection & Inputs]]
- [[components-color-theme|Color & Theme: 지능적인 컬러 시스템과 HCT]]
