---
title: custom-tabs-contracts
tags: [android, android/navigation, android/custom-tabs]
aliases: ["Custom Tabs 계약", "Custom Tabs Contracts"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Custom Tabs 계약 (Custom Tabs Contracts)

안드로이드 앱 내부에서 웹 콘텐츠를 노출할 때 **Custom Tabs**(인앱 브라우저 기술)를 활용하기 위한 핵심 보안, 프로세스, 라이프사이클 계약 모음이다.

---

### 개념과 아키텍처 원칙 (What & Why)

1. **프로세스 및 신뢰 경계(Trust Boundary) 분리**:
   - **`WebView`**는 앱 프로세스 내부에서 웹 코드를 실행하여 보안상 취약점(`addJavascriptInterface` 악용, 자바스크립트 인젝션, 별도 쿠키 관리)을 노출한다.
   - **`CustomTabsIntent`**는 사용자가 지정한 브라우저(Chrome 등) 프로세스에 웹 렌더링을 위임함으로써, 앱 프로세스와 웹 콘텐츠 간의 물리적 신뢰 경계를 완전히 분리한다.
2. **세션 및 성능 최적화 계약**:
   - 브라우저 쿠키(Cookie Jar) 및 로그인 상태(SSO)를 공유하여 사용자가 다시 로그인할 필요가 없다.
   - `CustomTabsClient.warmup()` 및 `CustomTabsSession.mayLaunchUrl()`을 이용한 사전 워밍업 및 렌더링 프리패치를 지원한다.
   - Chrome 107+부터 지원되는 **Partial Custom Tabs**(바텀 시트 형태 인앱 브라우저)로 앱 경험 연속성을 극대화한다.

---

### 하위 세부 계약 항목

- [Custom Tabs는 WebView와 다른 신뢰 경계와 프로세스 모델을 가진다](custom-tabs-share-browser-trust-boundary-instead-of-app-webview-process.md)

---

### 연관 지도 및 상위 문서

- 상위 가이드: [Android Navigation 진입 계약](../../navigation-contracts/navigation-contracts.md)
- 연관 계약: [WebView 계약](../../../ui/system/webview-contracts/webview-contracts.md)
- 보안 참조: [웹 보안](../../../../../../security/web-security.md)
