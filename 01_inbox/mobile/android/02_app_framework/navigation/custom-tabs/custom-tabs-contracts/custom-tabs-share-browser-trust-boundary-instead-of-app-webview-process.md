---
title: custom-tabs-share-browser-trust-boundary-instead-of-app-webview-process
tags: [android, android/navigation, android/custom-tabs]
aliases: ["Custom Tabs는 WebView와 다른 신뢰 경계와 프로세스 모델을 가진다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## Custom Tabs 는 WebView 와 다른 신뢰 경계(Trust Boundary)와 프로세스 모델을 가진다

상위 문서: [Custom Tabs 계약](custom-tabs-contracts.md)

배경 지식: [웹 보안](../../../../../../security/web-security.md), [프로세스 생명주기](../../../../../../operating-systems/process-states-lifecycle.md)

---

### 개념과 필요성 (What & Why)

1. **개념 (What)**:
   - **Custom Tabs**(인앱 브라우저 기술)는 앱 내부 UI 레이아웃 안에서 웹 코드를 실행하는 `WebView`와 달리, 사용자의 기본 브라우저(예: Chrome) 프로세스를 구동하여 툴바 색상, 버튼, 바텀시트 높이 등 앱에 맞춤화된 브라우저 UI 창을 앱 상단에 띄우는 브라우저 연동 아키텍처다.
2. **필요성 (Why)**:
   - **보안 신뢰 경계(Trust Boundary) 격리**: `WebView`는 앱 프로세스 및 UID와 동일한 실행 공간에서 웹 랜더링 엔진을 작동시킨다. 만약 공격자가 웹 사이트에 자바스크립트 인젝션 공격을 감행하거나 `addJavascriptInterface()` 인터페이스를 악용하면 앱 프로세스의 메모리와 로컬 데이터가 노출될 수 있다. 반면 Custom Tabs는 브라우저 앱 프로세스에서 독립 작동하므로 웹 콘텐츠가 앱 프로세스 영역으로 침범할 수 없다.
   - **브라우저 인프라 재사용 (Cookie Jar, AutoFill, Passkey)**: 사용자 기존 브라우저의 저장된 로그인 세션, 자동완성, Safe Browsing, 보안 인증서를 그대로 공유받으므로, 인앱 웹 전환 시 재로그인 불필요 및 결제 UX가 극대화된다.

---

### 내부 동작 메커니즘 (How)

```mermaid
flowchart TB
    subgraph AppProc["호출한 앱 프로세스 (App PID)"]
        A1["Activity / Composable"] -->|"CustomTabsIntent.launchUrl()"| A2"Intent / [binder ipc"]
        W1["WebView (View)"] -.->|"같은 PID, 같은 UID 실행"| W2["웹 콘텐츠 실행 엔진"]
        W2 -.->|"addJavascriptInterface() 보안 취약 경로"| W1
    end
    subgraph BrowserProc["기본 브라우저 프로세스 (Chrome PID)"]
        B1["Custom Tabs Service"]
        B2["독립된 렌더링 엔진 (Blink/V8)"]
        B3["보안 쿠키 Jar, Safe Browsing, Passkey"]
        B1 --> B2
        B2 --> B3
    end
    A2 --> B1
    B2 -.->|"앱 메모리/코드 접근 물리적 차단"| A1
```

1. **`CustomTabsIntent` 및 IPC 통신**:
   - 앱이 `CustomTabsIntent.launchUrl()`을 호출하면 안드로이드 OS는 `ACTION_VIEW` Intent를 수신하고, Custom Tabs Protocol을 구현한 기본 브라우저 애플리케이션 서비스(`CustomTabsService`)로 IPC 연동을 수행한다.
2. **`CustomTabsServiceConnection`과 워밍업 (Pre-warming)**:
   - 앱이 `CustomTabsClient.bindCustomTabsService()`를 실행하면 브라우저 프로세스와 Binder 연결이 맺어진다.
   - `client.warmup(0L)`을 호출하면 브라우저 프로세스가 사전 초기화되며, `session.mayLaunchUrl()`을 호출하면 지정된 URL의 DNS 룩업 및 TLS 핸드셰이크, HTML 프리패치가 렌더링 시작 전에 완료되어 웹 페이지 로딩 속도가 비약적으로 향상된다.

---

### 구시대 레거시 vs 현대 표준 비교 (Legacy vs Modern)

| 구분 | 임베디드 WebView 방식 (Legacy) | 현대 Custom Tabs 방식 (Modern Standard) |
| :--- | :--- | :--- |
| **실행 프로세스** | 앱 프로세스 (동일 PID, 동일 UID) | 브라우저 전용 프로세스 (별도 PID, 브라우저 Sandbox) |
| **보안 위험성** | JS 브릿지 악용, RCE, 자바스크립트 인젝션, SSL 검증 무시 위험 | 브라우저 레벨 Sandbox 및 Safe Browsing 적용으로 원천 격리 |
| **세션/쿠키 공유** | 앱 전용 `CookieManager` 사용으로 사용자가 웹 서비스 재로그인 필요 | 기존 시스템 브라우저 쿠키 Jar 공유로 자동 로그인 유지 |
| **성능 최적화** | 페이지 로딩 시 매번 렌더링 엔진 처음부터 초기화 | `warmup()` 및 `mayLaunchUrl()` 사전 연결 및 DNS 프리패치 제공 |
| **UX 형태** | 앱 전체 화면을 가리거나 별도 Activity 전환 필요 | Partial Custom Tabs(바텀 시트) 형태로 앱과 웹의 부드러운 공존 |

---

### 핵심 구현 코드 예시

```kotlin
// 1. 브라우저 프로세스 사전 워밍업 (Pre-warm & Prefetch)
class BrowserWarmupManager(private val context: Context) {
    private var client: CustomTabsClient? = null
    private var session: CustomTabsSession? = null

    private val connection = object : CustomTabsServiceConnection() {
        override fun onCustomTabsServiceConnected(name: ComponentName, client: CustomTabsClient) {
            this@BrowserWarmupManager.client = client
            // 브라우저 프로세스 프로세스 준비
            client.warmup(0L)
            // 세션 생성 및 URL 프리패치
            session = client.newSession(CustomTabsCallback())
            session?.mayLaunchUrl(Uri.parse("https://example.com/terms"), null, null)
        }

        override fun onServiceDisconnected(name: ComponentName) {
            client = null
            session = null
        }
    }

    fun bind() {
        val packageName = CustomTabsClient.getPackageName(context, null)
        if (packageName != null) {
            CustomTabsClient.bindCustomTabsService(context, packageName, connection)
        }
    }

    // 2. Partial Custom Tabs (바텀 시트 스타일) 실행
    fun launchUrl(url: String) {
        val customTabsIntent = CustomTabsIntent.Builder(session)
            .setShowTitle(true)
            .setInitialActivityHeightPx(1200) // Chrome 107+ 바텀 시트 높이 설정
            .setToolbarCornerRadiusDp(16)
            .build()
        customTabsIntent.launchUrl(context, Uri.parse(url))
    }
}
```

---

### 관측 가능한 증거 및 검증 (Audit Evidence)

- **Process Isolation 확인**: `adb shell dumpsys activity processes | grep -i chrome` 명령을 통해 Custom Tabs 실행 시 앱 패키지 외에 브라우저 패키지의 별도 PID가 작동함을 확인한다.
- **Shared Session 확인**: 브라우저에서 로그인된 웹 사이트를 Custom Tabs로 launch 했을 때 추가 로그인 없이 즉시 세션이 유지됨을 확인한다.

---

### 관련 상위 및 연관 노트

- 상위 계약: [Custom Tabs 계약](custom-tabs-contracts.md)
- 연관 계약: [WebView 계약](../../../ui/system/webview-contracts/webview-contracts.md)
- 연관 계약: [Intent는 컴포넌트 실행을 설명하는 메시지다](../../intents-and-deep-links/intent-manifest-contracts/intent-describes-component-action-request.md)
