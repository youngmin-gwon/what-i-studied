---
title: webview-contracts
tags: ["android", "android/app-framework"]
aliases: ["Android WebView 계약"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## Android WebView 계약

배경 지식: [웹 브라우저 보안](../../../../../../security/attacks/web-browser-security.md)

`WebView`(Chromium 엔진 기반으로 앱 레이아웃 내부에서 HTML/JS 웹 콘텐츠를 직접 렌더링하는 안드로이드 View 컴포넌트)는 네이티브 앱 화면 안에 웹 콘텐츠를 끼워 넣는 컴포넌트다. 편리하지만 앱의 신뢰 경계와 웹 콘텐츠의 신뢰 경계를 한 화면에 겹쳐 놓기 때문에, 다른 View 컴포넌트와 달리 브리지 설계, 콘텐츠 정책, 리소스 정리를 각각 별도의 계약으로 다뤄야 한다.

### 이 클러스터가 다루는 범위

- 앱 프로세스와 웹 콘텐츠 사이의 신뢰 경계가 어디에 있는지
- `addJavascriptInterface()` 로 자바 객체를 노출할 때의 위험과 안전 조건
- HTTPS/mixed content 정책과 Safe Browsing 이 어떤 콘텐츠를 걸러내는지
- `WebView` 가 `Activity` 와 다르게 명시적 `destroy()` 를 요구하는 이유

### 다루지 않는 범위

- Chrome Custom Tabs — 별도 프로세스의 브라우저가 렌더링을 담당하는 다른 신뢰 모델이며 `02_app_framework/navigation/` 의 Custom Tabs 노트에서 다룬다.
- `WebView` 컴포넌트 배포판(Chromium) 자체의 업데이트 메커니즘이나 System WebView 앱 관리.
- 하이브리드 앱 프레임워크(Cordova, Capacitor 등)의 자체 브리지 프로토콜 설계.

### 정본 노트

- [WebView는 신뢰된 앱 프로세스 안에서 신뢰되지 않은 웹 콘텐츠를 실행한다](./webview-runs-untrusted-web-content-inside-the-trusted-app-process.md)
- [addJavascriptInterface()는 @JavascriptInterface로 표시한 메서드만 웹 콘텐츠에 노출한다](./addjavascriptinterface-exposes-only-annotated-methods-to-web-content.md)
- [WebView는 HTTPS와 Safe Browsing으로 신뢰할 수 없는 콘텐츠를 걸러낸다](./webview-https-mixed-content-and-safe-browsing-policy.md)
- [WebView는 Activity와 달리 명시적 destroy() 호출이 필요하다](./webview-destroy-lifecycle-differs-from-activity.md)

### 읽는 순서

1. 신뢰 경계 노트로 왜 `WebView` 가 다른 View 와 다른 취급이 필요한지 이해한다.
2. `addJavascriptInterface()` 노트로 가장 위험한 통로가 어떻게 게이트되는지 확인한다.
3. HTTPS/Safe Browsing 노트로 콘텐츠 자체를 걸러내는 정책을 확인한다.
4. destroy 노트로 리소스 정리 계약을 확인한다.

관련 지도: [Android UI System](../android-ui-system.md), [Android UI System Contracts](../ui-system-contracts/ui-system-contracts.md)
