---
title: custom-tabs-contracts
tags: [android, android/navigation]
aliases: ["Custom Tabs 계약"]
date modified: 2026-08-04 18:00:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## Custom Tabs 계약

Custom Tabs 는 앱 내부에서 신뢰 경계가 다른 웹 콘텐츠를 보여주는 세 번째 선택지다. 완전한 외부 브라우저 전환도 아니고, 앱 프로세스 안에서 실행되는 `WebView` 도 아니다. 이 클러스터는 그 경계가 왜 그렇게 나뉘는지 다룬다.

### 정본 노트

- [Custom Tabs는 WebView와 다른 신뢰 경계와 프로세스 모델을 가진다](./custom-tabs-share-browser-trust-boundary-instead-of-app-webview-process.md)

### 읽는 기준

앱 안에서 외부 링크를 열어야 하는데 `WebView` 를 써야 할지 Custom Tabs 를 써야 할지 판단하려면 이 노트에서 두 모델의 프로세스·신뢰 차이를 먼저 확인한다. `WebView` 자체의 위험(예: `addJavascriptInterface`, mixed content)은 [WebView 계약](../../../ui/system/webview-contracts/webview-contracts.md)에서 다룬다.

상위 지도: [Android Navigation 진입 계약](../../navigation-contracts/navigation-contracts.md)
