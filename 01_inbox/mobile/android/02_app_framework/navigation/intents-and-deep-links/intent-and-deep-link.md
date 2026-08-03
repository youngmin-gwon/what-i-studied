---
title: intent-and-deep-link
tags: [android, android/intents, android/navigation]
aliases: ["Intent and Deep Link"]
date modified: 2026-08-03 18:11:51 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Intent 는 OS 메시지이고 Deep Link 는 외부 URI 를 앱 내부 상태로 바꾸는 계약이다

Intent 와 Deep Link 는 모두 앱 진입을 만들지만 책임이 다르다. Intent 는 OS 가 컴포넌트를 찾고 실행하는 메시지이고, Deep Link 는 외부 URI 를 앱 내부 navigation state 로 바꾸는 계약이다.

### 읽는 순서

- 컴포넌트가 OS 에 어떻게 노출되는지는 [Intent 와 Manifest 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md) 을 본다.
- 외부 URL 을 내부 목적지로 바꾸는 문제는 [Deep Link 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-contracts.md) 을 본다.
- 내부 back stack 과 route key 는 [Navigation 3 계약](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-contracts.md) 으로 넘긴다.
