---
title: navigation-contracts
tags: []
aliases: []
date modified: 2026-07-31 18:17:51 +09:00
date created: 2026-07-31 17:13:53 +09:00
---

## Android Navigation 진입 계약

Android navigation 은 세 층으로 나눠서 읽어야 한다. OS 는 Intent 와 Manifest 로 앱 컴포넌트를 찾고, Deep Link 는 외부 URI 를 앱 내부 목적지로 바꾸며, Navigation 3 는 앱 내부 back stack 상태를 관리한다.

### 판단 순서

1. [AndroidManifest는 OS가 발견할 컴포넌트와 진입점을 선언한다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/android-manifest-declares-os-visible-components-and-entry-points.md)
2. [Intent는 컴포넌트 실행을 설명하는 메시지다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-describes-component-action-request.md)
3. [intent-filter는 컴포넌트의 수신 계약이다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-filter-is-component-receiving-contract.md)
4. [Android 딥 링크는 외부 URI 계약이다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-is-external-uri-contract.md)
5. [Android App Link는 검증된 HTTPS 딥 링크다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/app-link-is-verified-https-deep-link.md)
6. [Navigation 3 deep link는 URI를 NavKey로 변환한다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-deep-link-converts-uri-to-navkey.md)
7. [NavKey와 back stack은 앱이 소유하는 navigation 상태다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navkey-and-back-stack-are-app-owned-navigation-state.md)
8. [Android task와 앱 back stack은 다른 스택이다](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/android-task-and-app-back-stack-are-different-stacks.md)
9. [Top-level destination은 adaptive navigation chrome의 단위다](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/top-level-destination-owns-adaptive-navigation-chrome.md)

### 하위 지도

- [Intent와 Manifest 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md)
- [Deep Link 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-contracts.md)
- [Navigation 3 계약](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-contracts.md)
- [Adaptive Navigation 계약](01_inbox/mobile/android/02_app_framework/navigation/adaptive-navigation/adaptive-navigation-contracts/adaptive-navigation-contracts.md)
