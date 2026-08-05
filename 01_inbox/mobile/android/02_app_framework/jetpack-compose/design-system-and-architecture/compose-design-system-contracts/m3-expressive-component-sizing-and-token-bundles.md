---
title: m3-expressive-component-sizing-and-token-bundles
tags: [android, compose/design-system, material3, m3-expressive, design-tokens]
aliases: ["Material 3 Expressive 컴포넌트 크기 스케일과 토큰 번들 계약"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-05 15:10:00 +09:00
---

## Material 3 Expressive 컴포넌트 크기 스케일과 토큰 번들 계약

Material 3 Expressive (M3 Expressive) 시스템에서 모든 UI 컴포넌트는 단일 고정 높이 대신 **5단계 크기 스케일 (ExtraSmall, Small, Medium, Large, ExtraLarge)**을 지원하며, 크기 변경 시 **[크기 + Shape + 타이포그래피 + 패딩]**이 하나의 묶음 번들(Bundled Tokens)로 함께 조율된다.

---

### 1. 개념 및 핵심 명제 (What)

- **`defaultMinSize` 접근성 하한선 규칙**:
  - 컴포넌트 내부에서 `.size(48.dp)`와 같이 크기를 고정(Hardcoding)하면 Large(56dp)나 ExtraLarge(64dp)로 확장되지 않는다.
  - 접근성(Accessibility) 최소 터치 영역(48dp)을 **`.defaultMinSize(minWidth = 48.dp, minHeight = minHeight)`**로 기본 지정하되, 외부 Modifier 에 의해 가변적 확장이 가능하도록 유연성을 보장해야 한다.
- **번들 토큰 (Bundled Design Tokens)**:
  - 크기가 Medium 에서 Large 로 변경되면 폰트도 `labelLarge`에서 `titleMedium`으로, 패딩도 `(24.dp, 12.dp)`에서 `(28.dp, 16.dp)`로 한꺼번에 자동 조정된다.

---

### 2. M3 Expressive 컴포넌트 5단계 규격표 (Size Scale Table)

| 크기 토큰 (`FeedbackButtonSize`) | 최소 높이 (`minHeight`) | 표준 디폴트 Shape | 타이포그래피 | 내측 패딩 (가로, 세로) |
| :--- | :--- | :--- | :--- | :--- |
| **ExtraSmall** | `32.dp` | `CircleShape` (Fully Rounded) | `labelSmall` | `(12.dp, 6.dp)` |
| **Small** | `40.dp` | `CircleShape` (Fully Rounded) | `labelMedium` | `(16.dp, 8.dp)` |
| **Medium (기본 디폴트)** | **`48.dp` (접근성 하한선)** | `CircleShape` (Fully Rounded) | `labelLarge` | `(24.dp, 12.dp)` |
| **Large** | `56.dp` | `CircleShape` (Fully Rounded) | `titleMedium` | `(28.dp, 16.dp)` |
| **ExtraLarge** | `64.dp` | `CircleShape` (Fully Rounded) | `titleLarge` | `(32.dp, 18.dp)` |

---

### 3. 관련 문서 및 참조

- 상위 문서: [Material 3 Expressive 디자인 시스템 및 컴포넌트 아키텍처](./m3-expressive-design-system-and-component-architecture.md)
- 관련 계약 문서:
  - [Material 3 Expressive Shape 스케일과 인터랙티브 Shape Morphing 계약](./m3-expressive-shape-scale-and-interactive-shape-morphing.md)
  - [Material 3 색상 역할은 고정된 색상이 아닌 의미적 의도를 표현한다](./material3-color-roles-express-semantic-intent-not-fixed-colors.md)

공식 가이드: [Material Design 3 - Buttons Specs](https://m3.material.io/components/buttons/specs)

검증일: 2026-08-05. M3 Expressive Component Sizing 및 defaultMinSize 사양 반영 완료.
