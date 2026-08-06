---
title: navigation3-transition-and-back-policy-must-share-stack-state
tags: [android, android/navigation, android/navigation3]
aliases: ["Navigation 3 transition과 back policy는 같은 stack 상태를 공유해야 한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Navigation 3 transition 과 back policy 는 같은 stack 상태를 공유해야 한다

상위 문서: [Navigation 3 계약](navigation3-contracts.md)

---

### 개념과 필요성 (What & Why)

1. **개념 (What)**:
   - Navigation 3 화면 전환 모션 애니메이션(Transition)과 뒤로 가기 및 Predictive Back 제스처 정책(Back Policy)은 반드시 **동일한 `NavBackStack` 진실의 단일 원천([single source of truth](../../../single-source-of-truth.md)) 상태**를 공유하여 작동해야 한다는 원칙이다.
2. **필요성 (Why)**:
   - 백스택 상태와 애니메이션 진행 상태가 별개의 boolean 변수나 흩어진 커스텀 상태로 이원화되면, Predictive Back 제스처 도중 사용자가 취소했을 때 이전 화면 UI와 백스택 불일치가 발생하는 버그가 유발된다.

---

### 관련 상위 및 연관 노트

- 상위 계약: [Navigation 3 계약](navigation3-contracts.md)
- 연관 계약: [NavKey와 back stack은 앱이 소유하는 navigation 상태다](navkey-and-back-stack-are-app-owned-navigation-state.md)
