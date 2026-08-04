---
title: jetpack-navigation-3-guide
tags: [android, android/navigation, android/navigation3]
aliases: ["Jetpack Navigation 3 Guide"]
date modified: 2026-08-03 18:12:06 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Jetpack Navigation 3 Guide 는 NavKey 기반 렌더링 모델을 설명한다

Jetpack Navigation 3 문서는 앱이 `NavKey` back stack 을 직접 소유하고 `NavDisplay` 가 이를 Compose 화면으로 렌더링하는 모델을 정리한다. 기존 XML graph 중심 Navigation 과 섞지 않고 typed key, entry provider, scene strategy, saveable restoration 을 기준으로 읽는다.

### 정본 지도

- [Navigation 3 계약](./navigation3-contracts/navigation3-contracts.md)
- [NavKey와 back stack은 앱이 소유하는 navigation 상태다](./navigation3-contracts/navkey-and-back-stack-are-app-owned-navigation-state.md)
- [NavDisplay와 entry provider는 렌더링과 route registry를 분리한다](./navigation3-contracts/navdisplay-and-entry-provider-separate-rendering-from-route-registry.md)
- [Navigation 3 deep link는 URI를 NavKey로 변환한다](./navigation3-contracts/navigation3-deep-link-converts-uri-to-navkey.md)
