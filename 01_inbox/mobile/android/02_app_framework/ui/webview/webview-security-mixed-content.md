---
title: webview-security-mixed-content
tags: ["android", "android/app-framework"]
aliases: ["WebView는 HTTPS와 Safe Browsing으로 신뢰할 수 없는 콘텐츠를 걸러낸다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## WebView는 HTTPS와 Safe Browsing으로 신뢰할 수 없는 콘텐츠를 걸러낸다

배경 지식: [HTTP 프로토콜](../../../../../computer-science/networking/http-protocol.md), [SSL/TLS](../../../../../linux/security/ssl-tls.md)

[WebView는 신뢰된 앱 프로세스 안에서 신뢰되지 않은 웹 콘텐츠를 실행한다](webview-process-isolation.md) 에서 설명한 신뢰 경계 문제를 완화하는 두 번째 축은 브리지 설계가 아니라 어떤 콘텐츠를 애초에 로드하고 실행할지 걸러내는 정책이다. `WebView` 는 이를 mixed content 정책과 Safe Browsing 두 메커니즘으로 제공한다.

### Mixed content(HTTPS 암호화 페이지 내부에서 비암호화 HTTP 리소스를 로드할 때 발생하는 보안 상태) 정책

HTTPS 페이지 안에 HTTP 리소스(이미지, 스크립트, iframe)가 섞여 로드되면 그 HTTP 리소스는 중간자 공격으로 변조될 수 있다. `WebSettings.setMixedContentMode()` 로 이 동작을 제어한다.

```kotlin
webView.settings.mixedContentMode = WebSettings.MIXED_CONTENT_NEVER_ALLOW
```

- `MIXED_CONTENT_NEVER_ALLOW`: HTTPS 페이지에서 HTTP 리소스 로드를 완전히 차단한다. 새 앱의 기본 권장값이다.
- `MIXED_CONTENT_COMPATIBILITY_MODE`: 브라우저와 유사하게 일부 mixed content 를 허용한다.
- `MIXED_CONTENT_ALWAYS_ALLOW`: HTTP/HTTPS 리소스를 구분하지 않고 모두 허용한다 — 보안상 권장하지 않는다.

`targetSdkVersion` 21(`Lollipop`) 이상 앱은 기본값이 `MIXED_CONTENT_NEVER_ALLOW` 다. HTTPS 로 로드한 페이지 안에서 HTTP 리소스가 깨져 보이는 것은 버그가 아니라 이 정책이 정상 동작한 결과일 수 있다.

### Safe Browsing 연동

`WebView` 는 Google Safe Browsing 위협 데이터베이스와 연동해 알려진 악성/피싱 사이트로의 이동을 차단한다. Android 8.0(API 26)+ 에서는 개별 `WebView` 단위로, 그 이전 버전 호환은 AndroidX `WebViewCompat`/`WebSettingsCompat` 로 제어한다.

```kotlin
// 개별 WebView에서 Safe Browsing 활성화(기본값은 켜짐)
WebSettingsCompat.setSafeBrowsingEnabled(webView.settings, true)

// Safe Browsing 초기화(API 26.1+ 권장 패턴)
if (WebViewFeature.isFeatureSupported(WebViewFeature.START_SAFE_BROWSING)) {
    WebViewCompat.startSafeBrowsing(this) { success ->
        if (!success) Log.e("WebView", "Safe Browsing 초기화 실패")
    }
}

class SafeBrowsingWebViewClient : WebViewClientCompat() {
    override fun onSafeBrowsingHit(
        view: WebView,
        request: WebResourceRequest,
        threatType: Int,
        callback: SafeBrowsingResponseCompat
    ) {
        if (WebViewFeature.isFeatureSupported(WebViewFeature.SAFE_BROWSING_RESPONSE_BACK_TO_SAFETY)) {
            callback.backToSafety(true) // 안전한 페이지로 되돌림
        }
    }
}
```

앱 전체에서 Safe Browsing 을 끄려면 매니페스트에 명시적으로 opt-out 해야 한다 — 이 값을 빼면 기본값은 활성화다.

```xml
<application>
    <meta-data
        android:name="android.webkit.WebView.EnableSafeBrowsing"
        android:value="false" />
</application>
```

### 판단 기준

- 임의 외부 URL 을 로드하는 `WebView` 는 `MIXED_CONTENT_NEVER_ALLOW` 와 Safe Browsing 활성화를 기본값으로 유지한다.
- 앱이 완전히 통제하는 자체 도메인의 정적 콘텐츠만 로드한다면 Safe Browsing opt-out 을 검토할 수 있지만, 이 경우에도 `addJavascriptInterface()` 브리지를 열었다면 [addJavascriptInterface()는 @JavascriptInterface로 표시한 메서드만 웹 콘텐츠에 노출한다](javascript-interface-security.md) 의 origin 제한이 여전히 필요하다.

### 관찰 가능한 신호

- Safe Browsing 이 위협을 차단하면 `onSafeBrowsingHit()` 콜백이 호출되고, 콜백을 구현하지 않으면 기본 인터스티셜 경고 화면이 사용자에게 표시된다.
- `MIXED_CONTENT_NEVER_ALLOW` 상태에서 HTTP 리소스 로드가 차단되면 Logcat 에 `Mixed Content: The page at 'https://...' was loaded over HTTPS, but requested an insecure resource` 형태의 콘솔 경고가 남는다.

공식 문서: [WebView 관리 — Safe Browsing과 mixed content](https://developer.android.com/develop/ui/views/layout/webapps/managing-webview)

검증일: 2026-08-04. `setMixedContentMode()` 값 3 종, Safe Browsing 기본 활성화와 매니페스트 opt-out 메타데이터, `onSafeBrowsingHit()` 콜백 동작을 공식 문서에서 확인했다.
