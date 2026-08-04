---
title: navigation-contracts
tags: [android, android/navigation]
aliases: ["Android Navigation 진입 계약"]
date modified: 2026-08-03 18:11:52 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android Navigation 진입 계약

Android navigation 은 세 층으로 나눠서 읽어야 한다. OS 는 Intent 와 Manifest 로 앱 컴포넌트를 찾고, Deep Link 는 외부 URI 를 앱 내부 목적지로 바꾸며, Navigation 3 는 앱 내부 back stack 상태를 관리한다. Adaptive Navigation 은 같은 목적지를 window 조건에 맞는 chrome 과 pane 으로 표현한다.

### 판단 순서

- [AndroidManifest는 OS가 발견할 컴포넌트와 진입점을 선언한다](../intents-and-deep-links/intent-manifest-contracts/android-manifest-declares-os-visible-components-and-entry-points.md)
- [Intent는 컴포넌트 실행을 설명하는 메시지다](../intents-and-deep-links/intent-manifest-contracts/intent-describes-component-action-request.md)
- [Intent 입력은 명시적인 타입과 신뢰 경계가 필요하다](../intents-and-deep-links/intent-manifest-contracts/intent-inputs-need-explicit-type-and-trust-boundaries.md)
- [Android 딥 링크는 외부 URI 계약이다](../intents-and-deep-links/deep-link-contracts/deep-link-is-external-uri-contract.md)
- [외부 URI는 navigation 전에 검증한다](../intents-and-deep-links/deep-link-contracts/external-uri-must-be-validated-before-navigation.md)
- [Android App Link는 검증된 HTTPS 딥 링크다](../intents-and-deep-links/deep-link-contracts/app-link-is-verified-https-deep-link.md)
- [Navigation 3 deep link는 URI를 NavKey로 변환한다](../navigation3/navigation3-contracts/navigation3-deep-link-converts-uri-to-navkey.md)
- [Navigation 3 route key는 안정적인 직렬화 식별자다](../navigation3/navigation3-contracts/route-key-should-be-stable-and-serializable.md)
- [Navigation 3 back stack은 저장 가능한 state로 복원한다](../navigation3/navigation3-contracts/navigation3-back-stack-needs-saveable-restoration.md)
- [Adaptive navigation은 현재 window와 posture로 결정한다](../adaptive-navigation/adaptive-navigation-contracts/adaptive-navigation-is-driven-by-window-and-posture.md)

### 하위 지도

- [Intent와 Manifest 계약](../intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md)
- [Deep Link 계약](../intents-and-deep-links/deep-link-contracts/deep-link-contracts.md)
- [Navigation 3 계약](../navigation3/navigation3-contracts/navigation3-contracts.md)
- [Adaptive Navigation 계약](../adaptive-navigation/adaptive-navigation-contracts/adaptive-navigation-contracts.md)
