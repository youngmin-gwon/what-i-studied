---
title: Compose 계층은 상위 컴포넌트가 맞지 않을 때 낮은 계층을 허용한다
tags: [android, jetpack-compose, compose/design-system]
aliases: [Compose layering]
date modified: 2026-07-31 23:59:30 +09:00
date created: 2026-07-31 23:59:30 +09:00
---

# Compose 계층은 상위 컴포넌트가 맞지 않을 때 낮은 계층을 허용한다

Compose는 Runtime, UI, Foundation, Material 같은 계층을 조합하는 구조다. 상위 계층은 더 낮은 계층의 API를 조합해 기본 동작, 접근성, styling, interaction을 제공한다.

상위 Material component가 요구에 맞지 않으면 Foundation이나 UI 계층으로 내려가 직접 조합할 수 있다. 이때 제어권은 커지지만 accessibility, interaction state, token 적용, bug fix 추적 책임도 같이 커진다.

따라서 낮은 계층 사용은 “더 순수한 Compose”가 아니라 trade-off다. 컴포넌트 포킹이나 재구현은 upstream 개선을 자동으로 받지 못하는 비용을 남긴다.

관련 노트: [Compose 모듈 경계는 의존성 범위와 교체 비용을 드러낸다](01_inbox/mobile/android/02_app_framework/jetpack-compose/design-system-and-architecture/compose-design-system-contracts/compose-module-boundaries-expose-dependency-scope-and-replacement-cost.md), [Semantics Tree는 UI 의미를 접근성 서비스와 테스트에 드러낸다](01_inbox/mobile/android/02_app_framework/jetpack-compose/layout-and-ui/compose-ui-contracts/semantics-tree-makes-ui-meaning-visible-to-accessibility-and-tests.md)

출처: [Compose architectural layering](https://developer.android.com/develop/ui/compose/layering)
