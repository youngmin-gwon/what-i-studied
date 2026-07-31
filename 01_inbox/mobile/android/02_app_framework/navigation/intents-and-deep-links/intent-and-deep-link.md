---
title: "Intent and Deep Link"
tags: [android, android/navigation, android/intents]
aliases: ["Intent and Deep Link"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Intent and Deep Link

Intent와 Deep Link는 모두 앱 진입을 만들지만 책임이 다르다. Intent는 OS가 컴포넌트를 찾고 실행하는 메시지이고, Deep Link는 외부 URI를 앱 내부 navigation state로 바꾸는 계약이다.

## 읽는 순서

- 컴포넌트가 OS에 어떻게 노출되는지는 [Intent 와 Manifest 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md)을 본다.
- 외부 URL을 내부 목적지로 바꾸는 문제는 [Deep Link 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-contracts.md)을 본다.
- 내부 back stack과 route key는 [Navigation 3 계약](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-contracts.md)으로 넘긴다.
