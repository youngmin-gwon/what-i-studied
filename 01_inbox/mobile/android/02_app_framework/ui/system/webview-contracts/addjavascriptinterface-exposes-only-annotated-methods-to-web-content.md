---
title: addjavascriptinterface-exposes-only-annotated-methods-to-web-content
tags: ["android", "android/app-framework"]
aliases: ["addJavascriptInterface()는 @JavascriptInterface로 표시한 메서드만 웹 콘텐츠에 노출한다"]
date modified: 2026-08-04 18:00:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## addJavascriptInterface()는 @JavascriptInterface로 표시한 메서드만 웹 콘텐츠에 노출한다

`WebView.addJavascriptInterface(Object, String)` 는 자바/코틀린 객체를 JavaScript 전역 객체로 주입해, 페이지의 스크립트가 그 객체의 메서드를 직접 호출하게 만드는 API 다. [WebView는 신뢰된 앱 프로세스 안에서 신뢰되지 않은 웹 콘텐츠를 실행한다](./webview-runs-untrusted-web-content-inside-the-trusted-app-process.md) 에서 설명한 신뢰 경계를 실제로 뚫는 다리가 이 API 다 — 브리지 객체의 메서드는 앱 프로세스의 권한과 데이터 접근 범위로 실행된다.

### 메커니즘: 리플렉션 노출과 어노테이션 게이트

`targetSdkVersion` 17(`JELLY_BEAN_MR1`) 이상을 대상으로 하는 앱에서는 `@JavascriptInterface` 어노테이션이 붙은 public 메서드만 JavaScript 에서 호출 가능하다. 어노테이션이 없는 메서드는 리플렉션 대상에서 자동으로 제외된다.

```kotlin
class WebAppInterface(private val context: Context) {
    // 이 메서드만 JavaScript에서 호출 가능
    @JavascriptInterface
    fun showToast(message: String) {
        Toast.makeText(context, message, Toast.LENGTH_SHORT).show()
    }

    // 어노테이션이 없으면 targetSdk 17+ 에서 JavaScript가 호출할 수 없다
    fun readSecretFile(): String {
        return context.filesDir.resolve("secret.txt").readText()
    }
}

webView.settings.javaScriptEnabled = true
webView.addJavascriptInterface(WebAppInterface(this), "Android")
```

```javascript
// 페이지 쪽 JavaScript
Android.showToast("Hello from the page"); // 동작
Android.readSecretFile();                 // targetSdk 17+ 에서는 함수가 아예 보이지 않음
```

`targetSdkVersion` 이 17 미만이면 이 게이트가 적용되지 않아 어노테이션 없는 public 메서드까지 전부 리플렉션으로 호출 가능해진다. 이는 과거 버전 Android 에서 임의 자바 객체 주입이 원격 코드 실행으로 이어진 대표적인 취약점 패턴이었다(CVE-2012-6636 계열). `@JavascriptInterface` 강제는 이 문제에 대한 플랫폼 차원의 완화책이지, 브리지 설계 자체의 안전을 보장하지는 않는다.

### 안전한 사용 조건

- `targetSdkVersion` 17 이상을 유지해 어노테이션 게이트를 활성화한다.
- 브리지 인터페이스는 최소한의 메서드만 노출하고, 파일 시스템 경로·토큰·계정 정보를 그대로 반환하는 메서드를 만들지 않는다.
- `WebView` 가 로드할 origin 을 신뢰할 수 있는 도메인으로 제한한다(`shouldOverrideUrlLoading` 등으로 검증). 임의 URL 을 로드하는 `WebView` 에 브리지를 노출하면 그 도메인이 공격자에게 넘어가는 순간 전체 브리지가 공격 표면이 된다.
- 파라미터 값은 신뢰하지 않은 입력으로 취급해 검증한다 — JavaScript 쪽에서 임의 문자열/숫자를 넘길 수 있다.

### 관찰 가능한 신호

- `targetSdkVersion` 을 17 미만으로 낮추고 어노테이션 없는 메서드를 호출해 보면 정상 동작하지만, 17 이상에서는 페이지 콘솔에 `TypeError: Android.readSecretFile is not a function` 형태의 오류가 남는다 — 어노테이션 게이트가 실제로 메서드를 리플렉션 목록에서 제외한다는 관찰 증거다.
- 정적 분석 도구(lint, MobSDK 계열 보안 스캐너)는 `addJavascriptInterface()` 호출을 발견하면 노출된 클래스의 모든 public 메서드에 `@JavascriptInterface` 누락 여부를 함께 점검하도록 경고를 낸다.

공식 문서: [WebView.addJavascriptInterface() 레퍼런스](https://developer.android.com/reference/android/webkit/WebView#addJavascriptInterface(java.lang.Object,%20java.lang.String)), [WebView 보안 모범 사례](https://developer.android.com/develop/ui/views/layout/webapps/managing-webview)

검증일: 2026-08-04. `targetSdkVersion` `JELLY_BEAN_MR1`(17) 이상에서 `@JavascriptInterface` 어노테이션이 없는 메서드는 JavaScript 에서 호출할 수 없다는 동작을 공식 문서에서 확인했다.
