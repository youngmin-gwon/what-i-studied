---
title: webview-runs-untrusted-web-content-inside-the-trusted-app-process
tags: ["android", "android/app-framework"]
aliases: ["WebView는 신뢰된 앱 프로세스 안에서 신뢰되지 않은 웹 콘텐츠를 실행한다"]
date modified: 2026-08-04 18:00:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## WebView는 신뢰된 앱 프로세스 안에서 신뢰되지 않은 웹 콘텐츠를 실행한다

`WebView` 는 Chromium 기반 렌더링 엔진으로 HTML/JavaScript 를 화면에 그린다. 문제는 그 콘텐츠의 출처다. 앱 자체는 서명, 권한, UID 로 신뢰되지만 `WebView` 가 로드하는 URL 은 공격자가 통제하는 서버일 수 있고, 리다이렉트나 mixed content 로 콘텐츠가 중간에 뒤바뀔 수도 있다. 즉 `WebView` 는 신뢰 경계가 다른 두 세계 — 신뢰된 네이티브 앱 프로세스와 신뢰할 수 없는 웹 콘텐츠 — 를 하나의 화면 안에 붙여 넣는 컴포넌트다.

일반 브라우저 탭은 웹사이트가 OS 권한이나 다른 탭의 데이터에 접근하지 못하도록 격리된 sandbox 안에서 실행된다. `WebView` 안의 콘텐츠는 이 격리가 훨씬 약하다. 앱이 명시적으로 다리를 놓지 않는 한 페이지는 기본적으로 앱의 파일이나 권한에 접근할 수 없지만, 앱이 `addJavascriptInterface()`, `postMessage`, custom scheme handler 같은 통로를 열면 그 통로를 통해 앱의 UID 로 실행되는 코드를 웹 콘텐츠가 간접적으로 호출하게 된다. 이 통로의 안전성은 `WebView` 자체가 아니라 앱이 설계한 브리지 코드에 달려 있다.

### 렌더러 프로세스 격리와 신뢰 경계는 별개다

Android 8.0(API 26) 이상에서 `WebView` 는 렌더링을 별도 프로세스(renderer process)에서 수행할 수 있다. 이 프로세스가 크래시하거나 시스템에 의해 강제 종료돼도 앱 프로세스 자체는 죽지 않고 `WebViewClient.onRenderProcessGone()` 콜백으로 통지받는다.

```kotlin
class MyWebViewClient : WebViewClient() {
    override fun onRenderProcessGone(
        view: WebView,
        detail: RenderProcessGoneDetail
    ): Boolean {
        if (!detail.didCrash()) {
            // 시스템이 메모리 회수를 위해 렌더러만 강제 종료한 경우
            Log.w("WebView", "renderer reclaimed by system, recreating WebView")
        } else {
            Log.e("WebView", "renderer process crashed")
        }
        return true // 앱 프로세스는 계속 실행
    }
}
```

렌더러가 별도 프로세스라는 사실은 안정성(크래시 격리) 문제이지 신뢰 경계 문제가 아니다. 앱이 자바 객체를 JavaScript 에 노출하면 그 객체는 여전히 앱 프로세스의 UID, 파일 접근 권한, 앱 데이터로 실행된다 — 렌더러 프로세스가 분리돼 있어도 브리지를 통한 호출은 앱 프로세스 안에서 처리된다.

### 관찰 가능한 신호

- `adb shell dumpsys activity processes | grep -i webview` 로 앱 프로세스와 별도의 `:sandboxed_process`/renderer 프로세스가 떠 있는지 확인할 수 있다.
- `onRenderProcessGone()` 이 `didCrash() == true` 로 호출되는데 앱이 이를 처리하지 않으면 시스템이 앱 프로세스 전체를 종료시킬 수 있다(문서상 처리하지 않으면 OS 가 앱을 crash 시킨다).
- Logcat 에 `chromium` 태그로 렌더러 크래시 스택이 남는 경우가 있는데, 이는 앱 코드 크래시가 아니라 웹 콘텐츠 렌더링 크래시로 원인 조사 경로가 다르다.

이 노트는 경계 자체를 다룬다. 브리지가 실제로 위험해지는 지점은 [addJavascriptInterface()는 @JavascriptInterface로 표시한 메서드만 웹 콘텐츠에 노출한다](./addjavascriptinterface-exposes-only-annotated-methods-to-web-content.md) 에서, HTTPS/Safe Browsing 정책은 [WebView는 HTTPS와 Safe Browsing으로 신뢰할 수 없는 콘텐츠를 걸러낸다](./webview-https-mixed-content-and-safe-browsing-policy.md) 에서 다룬다.

공식 문서: [WebView 관리](https://developer.android.com/develop/ui/views/layout/webapps/managing-webview)

검증일: 2026-08-04. Android 8.0(API 26)+ 렌더러 프로세스 분리와 `onRenderProcessGone()` 콜백 동작을 공식 문서에서 확인했다.
