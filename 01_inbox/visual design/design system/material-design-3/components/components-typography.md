---
title: M3 Typography - Roles & Intents (Expressive Update)
tags: [design-system, material-design, m3, typography, material-theme, expressive, ux-design]
aliases: [M3 Type Scale, Typography Roles, MaterialTheme Fonts, Emphasized Typography]
date modified: 2025-12-27 23:40:00 +09:00
date created: 2025-12-27 23:28:00 +09:00
---

## 🔤 M3 Typography: 의미론적 가독성

Material Design 3의 타이포그래피는 단순한 크기 조정을 넘어, **정보의 중요도와 맥락**을 사용자에게 전달하는 semantic(의미론적) 도구입니다. 특히 "Expressive" 업데이트로 추가된 **Emphasized(강조)** 스타일은 더 동적이고 위계가 뚜렷한 UI를 가능하게 합니다.

---

## 🏗️ Typography Roles (타입 스케일)

모든 스타일은 **Large**, **Medium**, **Small**의 세 가지 크기 변형을 가집니다.

### 1. Display (디스플레이)
화면에서 가장 크고 눈에 띄는 텍스트입니다.
- **Baseline**: `displayLarge`, `displayMedium`, `displaySmall`
- **Emphasized**: `emphasizedDisplayLarge`, `emphasizedDisplayMedium`, `emphasizedDisplaySmall`
- **의도**: 시선을 강력하게 끌어당기거나, 짧고 중요한 숫자를 표현합니다. Emphasized 버전은 더 굵고 대담하여 정서적 임팩트가 필요한 순간에 사용됩니다.
- **권장 상황**: 대시보드 지표, 랜딩 페이지 슬로건.

### 2. Headline (헤드라인)
섹션의 시작을 알리는 고대비 텍스트입니다.
- **Baseline**: `headlineLarge`, `headlineMedium`, `headlineSmall`
- **Emphasized**: `emphasizedHeadlineLarge`, `emphasizedHeadlineMedium`, `emphasizedHeadlineSmall`
- **의도**:Passages(본문 덩어리)를 논리적으로 구분하는 '이정표'입니다. Emphasized는 잡지(Editorial)와 같은 드라마틱한 섹션 전환에 적합합니다.
- **권장 상황**: 새로운 섹션 제목, 카테고리 헤더.

### 3. Title (타이틀)
중간 정도의 강조를 가진 텍스트로, 레이아웃의 구역을 나눕니다.
- **Baseline**: `titleLarge`, `titleMedium`, `titleSmall`
- **Emphasized**: `emphasizedTitleLarge`, `emphasizedTitleMedium`, `emphasizedTitleSmall`
- **의도**: 리스트 아이템이나 다이얼로그의 이름 등 모듈화된 정보의 제목입니다. Emphasized는 선택된 항목이나 특히 주의가 필요한 요소에 쓰입니다.
- **권장 상황**: 리스트 아이템 제목, 다이얼로그 타이틀.

### 4. Body (바디)
텍스트의 핵심 내용을 담는 '본문' 스타일입니다.
- **대상**: `bodyLarge`, `bodyMedium`, `bodySmall` (Body는 가독성을 위해 Emphasized를 지양하고 굵기 변형만 사용)
- **의도**: 가독성(Legibility) 최우선. 장문의 글을 읽을 때 피로도를 낮춥니다.
- **권장 상황**: 게시글 본문, 설명 텍스트.

### 5. Label (레이블)
컴포넌트 내부에 쓰이는 utilitarian(실용적인) 텍스트입니다.
- **Baseline**: `labelLarge`, `labelMedium`, `labelSmall`
- **Emphasized**: `emphasizedLabelLarge`, `emphasizedLabelMedium`, `emphasizedLabelSmall`
- **의도**: 버튼 텍스트나 캡션처럼 특정 기능을 설명합니다. Emphasized는 활성화된 버튼이나 강조하고 싶은 캡션에 적합합니다.
- **권장 상황**: 버튼 내 텍스트, 그림 아래 캡션, 태그/칩 메타데이터.

---

## 🚀 Expressive: Emphasized 스타일의 가치

M3 Expressive에서 **Emphasized** 역할이 중요한 이유는 다음과 같습니다:

1. **시각적 드라마 (Visual Drama)**: 정적인 UI에서 벗어나, 중요한 정보에 더 강한 물리적 굵기를 부여하여 감성적인 호소력을 높입니다.
2. **상태 전환 표현**: 사용자가 항목을 선택하거나 Hover할 때, 단순히 색상만 바꾸는 것이 아니라 폰트를 `emphasized` 스케일로 전환하여 '확실한 선택'을 피드백합니다.
3. **가변 폰트(Variable Fonts)와의 시너지**: `MaterialTheme`의 스타일을 기반으로 하되, 애니메이션과 함께 굵기가 부드럽게 변하는 '표현적' 순간을 만듭니다.

---

## 💡 프로그래밍 가이드 (Contextual Usage)

1.  **시선을 끌어야 하는가?** → **Display**
2.  **새로운 주제를 시작하는가?** → **Headline**
3.  **정보의 덩어리에 이름을 붙이는가?** → **Title**
4.  **읽어야 하는 정보인가?** → **Body**
5.  **기능을 설명하거나 버튼인가?** → **Label**
6.  **위의 상황에서 더 강한 강조나 '표현'이 필요한가?** → **Emphasized** 버전 선택

---

## 🔗 관련 문서
- [[../material3_walkthrough|Material Design 3 개요 (Expressive Deep Dive)]]
- [[components-actions|Actions: 버튼과 FAB]]
- [[components-selection-inputs|Selection & Inputs]]
