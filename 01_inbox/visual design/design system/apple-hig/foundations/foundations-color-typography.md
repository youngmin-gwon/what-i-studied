---
title: foundations-color-typography
tags: [apple, color, design-system, dynamic-type, hig, sf-symbols, typography, ux-design]
aliases: [Apple Color Palette, SF Symbols, San Francisco Font, Semantic Colors]
date modified: 2025-12-28 00:33:20 +09:00
date created: 2025-12-28 00:33:20 +09:00
---

## 🎨 Color & Typography (색상과 타이포그래피): Apple 의 시각 언어

Apple 시스템의 정체성은 정교하게 설계된 서체와 환경에 반응하는 지능적인 컬러 시스템에 있습니다.

## 🌈 Color System (색상 시스템)

Apple 의 컬러는 단순히 예쁜 색을 고르는 것이 아니라, **의미(Semantics)** 를 전달하는 도구입니다.

### 1. Semantic Colors (의미론적 컬러)
- **의도**: 개발자가 구체적인 HEX 값을 지정하는 대신, `SystemBackground`, `Label`, `Link` 와 같은 역할을 부여합니다.
- **적응성**: 시스템 컬러를 사용하면 **Dark Mode(다크 모드)** 전환 시 배경색은 검정으로, 글자색은 흰색으로 자동 반전됩니다. 또한 대비(Contrast) 설정 변화에도 유연하게 대응합니다.

### 2. Vibrant Effects (Vibrancy & Blurring)
- Apple UI 의 상징인 투명도와 블러 효과입니다. 레이어 사이의 깊이감을 만들고, 배경 이미지가 투영되면서도 그 위의 콘텐츠 판독성을 잃지 않게 합니다 (Materials 적용).

### 3. Color Contrast & Accessibility
- 최소 대비 **4.5:1** (WCAG AA) 을 기본으로 지향하며, 색상만으로 정보를 전달하지 말아야 한다는 원칭을 철저히 지킵니다 (예: 에러 시 색상 + 경고 아이콘 병행).

---

## 🔡 Typography (타이포그래피)

Apple 은 독자적인 가변 폰트인 **San Francisco (SF)** 시리즈를 통해 전 사양 판독성을 완성합니다.

### 1. San Francisco (SF) 시리즈
- **SF Pro**: iOS, iPadOS, macOS, visionOS 의 표준 서체.
- **SF Compact**: watchOS 전용 서체 (작은 화면에서 가독성을 높이기 위해 둥근 형태가 강조됨).
- **SF Mono**: 코드나 터미널 등 고정폭이 필요한 환경.

### 2. Dynamic Type (다이내믹 타입)
- 사용자가 설정 앱에서 텍스트 크기를 조절하면, 앱의 모든 텍스트가 이에 맞춰 유동적으로 변하는 기능입니다.
- **기술 사양**: `Large (Default)` 를 기준으로, 시스템 폰트 스타일(`Title`, `Body`, `Caption` 등) 을 사용하면 접근성이 자동으로 보장됩니다.

---

##  símbolos SF Symbols (SF 심볼)

텍스트와 완벽하게 조화되는 시스템 아이콘 라이브러리입니다.

### 1. 특징
- **폰트와의 조화**: 아이콘이 폰트의 굵기(Weight)와 크기(Size)에 맞춰 정렬됩니다. Bold 텍스트 옆에는 Bold 심볼을 배치하여 시각적 무게감을 맞출 수 있습니다.
- **Variable Color**: 단일 아이콘 내에서 여러 레이어의 불투명도나 색상을 조절하여 상태 변화를 풍부하게 표현합니다.
- **Accessibility**: 각 심볼은 VoiceOver 에 의해 의미론적으로 읽힐 수 있는 준비가 되어 있습니다.

---

## ♿ Accessibility (A11y)

- **Minimum Tap Target**: 모든 버튼과 터치 가능한 텍스트 영역은 최소 **44 x 44 pt** 이상이어야 합니다 (Apple 의 물리적 터치 기준).
- **Legibility Over Aesthetics**: 아무리 아름다운 색상 조합이라도 텍스트 판독성을 해친다면 HIG 위반입니다. 시스템 가이드라인이 제공하는 `SecondaryLabel` 등은 이 판독성 로직이 이미 검증된 컬러입니다.

---

## 🔗 관련 문서
- [[../hig_walkthrough|Apple HIG 개요]]
- [[foundations-layout|Layout: 공간과 환경]]
- [[../components/components-controls|Controls: 버튼과 입력]]
