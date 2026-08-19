---
title: intent-filter-matches-action-category-data
tags: [android, android/navigation, android/manifest]
aliases: ["Intent filter는 action, category, data를 매칭한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Intent filter 는 action, category, data 를 매칭한다

상위 문서: [Intent & Manifest 계약](intent-manifest.md)

---

### 3대 매칭 규칙 (How)

안드로이드 OS가 암시적 인텐트를 수신했을 때 실행되는 매칭 파이프라인은 다음과 같다:

1. **Action 테스트**:
   - Intent Filter에 선언된 `<action>` 중 최소 하나와 Intent의 Action이 정확히 일치해야 함.
2. **Category 테스트**:
   - Intent 객체에 지정된 모든 `<category>`가 Intent Filter에 선언되어 있어야 통과 (Implicit Intent 통신 시 `CATEGORY_DEFAULT` 필수).
3. **Data 테스트 (Scheme, Host, Port, Path, MIME Type)**:
   - Scheme, Host, Path 및 MIME 타입 조건이 모두 부합해야 매칭 통과.

---

### 관련 상위 및 연관 노트

- 상위 계약: [Intent & Manifest 계약](intent-manifest.md)
- 연관 계약: [Intent filter는 컴포넌트의 수신 계약이다](intent-filter-is-component-receiving.md)
