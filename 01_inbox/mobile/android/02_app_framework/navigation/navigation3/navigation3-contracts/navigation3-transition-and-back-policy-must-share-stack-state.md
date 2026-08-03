---
title: Navigation 3 transition과 predictive back은 같은 stack state를 기준으로 해야 한다
tags: [android, android/navigation, android/navigation3]
aliases: ["Navigation 3 transition과 predictive back은 같은 stack state를 기준으로 해야 한다"]
date modified: 2026-08-03 16:37:09 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Navigation 3 transition과 predictive back은 같은 stack state를 기준으로 해야 한다

Navigation animation 은 실제 navigation state 와 분리된 장식이 아니다. `NavDisplay` transition, pop transition, predictive back 중간 상태는 모두 같은 back stack 변경을 기준으로 움직여야 한다.

사용자가 back gesture 를 취소하거나 완료할 때 app back stack, visible entry, transition state 가 서로 다르면 화면은 되돌아왔지만 state 는 pop 된 상태 같은 불일치가 생긴다. 시스템 back 과 앱 내부 back action 은 하나의 stack mutation policy 로 모은다.

### 판단 기준

- system back, toolbar back, gesture back 은 같은 pop 정책을 호출한다.
- transition 은 state mutation 의 결과를 표현하고 별도 navigation state 를 만들지 않는다.
- predictive back 취소 시 stack 과 visible entry 가 그대로 유지되는지 확인한다.
- dialog, overlay, multi-pane scene 은 어떤 entry 가 pop 되는지 명시한다.

관련 노트: [NavKey와 back stack은 앱이 소유하는 navigation 상태다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navkey-and-back-stack-are-app-owned-navigation-state.md), [SceneStrategy는 entry를 조합하고 SceneDecorator는 렌더링을 감싼다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/scene-strategy-composes-entries-while-decorator-wraps-rendering.md)
