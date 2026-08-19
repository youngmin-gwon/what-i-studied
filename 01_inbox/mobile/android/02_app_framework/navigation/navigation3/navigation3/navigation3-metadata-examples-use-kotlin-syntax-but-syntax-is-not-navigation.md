---
title: navigation3-metadata-examples-use-kotlin-syntax-but-syntax-is-not-navigation-contract
tags: [android, android/navigation, android/navigation3]
aliases: ["Navigation 3 metadata 예시는 Kotlin 문법을 쓰지만 문법 자체가 navigation 계약은 아니다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Navigation 3 metadata 예시는 Kotlin 문법을 쓰지만 문법 자체가 navigation 계약은 아니다

상위 문서: [Navigation 3 계약](navigation3.md)

---

### 개념과 본질적 의미 (What & Why)

1. **개념 (What)**:
   - Navigation 3 문서나 예제 코드에 작성된 `metadata = DialogSceneStrategy.dialog()` 같은 표기는 라이브러리가 사용하는 **Kotlin DSL 예시 문법**일 뿐이며, 내비게이션 아키텍처의 본질적 계약은 **"엔트리와 표시 정책(Display Policy)의 분리"**라는 아키텍처 개념 그 자체라는 고찰이다.
2. **필요성 (Why)**:
   - DSL 문법 형태에 집착하기보다 메타데이터 맵을 통해 렌더러와 라우터 간에 시각적 표현 규칙을 독립적으로 전달한다는 아키텍처 계약 본질을 이해해야 모듈화 및 커스텀 Strategy 수립이 가능해진다.

---

### 관련 상위 및 연관 노트

- 상위 계약: [Navigation 3 계약](navigation3.md)
- 연관 계약: [Metadata와 SceneStrategy는 표시 정책을 전달한다](metadata-and-scene-strategy-carry-display-policy.md)
