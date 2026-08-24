---
title: intent-filter-resolution
tags: [android, android/navigation, android/manifest]
aliases: ["Intent filter는 컴포넌트의 수신 계약이다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Intent filter 는 컴포넌트의 수신 계약이다

상위 문서: [Intent & Manifest 계약](intent-manifest.md)

---

### 개념과 필요성 (What & Why)

1. **개념 (What)**:
   - **`<intent-filter>`**는 컴포넌트가 수신하고 처리할 수 있는 암시적 인텐트의 유형(Action, Category, Data)을 `AndroidManifest.xml`에 명시하는 **수신 자격 선언 계약**이다.
2. **필요성 (Why)**:
   - OS Intent Resolver가 외부에서 날아오는 `ACTION_VIEW` 인텐트를 어떤 앱의 Activity로 전달할지 판정할 때 Intent Filter의 매칭 조건표를 기반으로 검증을 수행한다.

---

### 관련 상위 및 연관 노트

- 상위 계약: [Intent & Manifest 계약](intent-manifest.md)
- 연관 계약: [Intent filter는 action, category, data를 매칭한다](intent-filter-matching-rules.md)
