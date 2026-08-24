---
title: webview-lifecycle-cleanup
tags: ["android", "android/app-framework"]
aliases: ["WebView는 Activity와 달리 명시적 destroy() 호출이 필요하다"]
date modified: 2026-08-04 18:00:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## WebView는 Activity와 달리 명시적 destroy() 호출이 필요하다

`Activity` 는 `onDestroy()` 시점에 시스템이 window, view tree, 관련 리소스를 정리해 준다. `WebView` 는 다르다. Chromium 엔진 내부에 렌더러 프로세스, 네이티브 메모리, 진행 중인 네트워크 요청, JavaScript 컨텍스트가 얽혀 있어서 앱이 명시적으로 `destroy()` 를 호출하지 않으면 이 리소스가 정리되지 않고 메모리 누수로 남는다.

### 메커니즘

`WebView` 를 담고 있던 `Activity`/`Fragment` 가 소멸돼도 `WebView` 인스턴스가 다른 곳(정적 필드, 콜백 클로저)에서 참조되고 있으면 GC 대상이 되지 않는다. 여기에 `destroy()` 를 호출하지 않은 채로 두면 네이티브 렌더러 리소스까지 계속 붙잡고 있게 된다.

```kotlin
class WebActivity : AppCompatActivity() {
    private var webView: WebView? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        webView = WebView(this).also { setContentView(it) }
    }

    override fun onDestroy() {
        webView?.let { wv ->
            (wv.parent as? ViewGroup)?.removeView(wv) // 뷰 트리에서 먼저 제거
            wv.destroy()                               // 네이티브 리소스 해제
        }
        webView = null
        super.onDestroy()
    }
}
```

렌더러 프로세스가 크래시하거나 시스템이 메모리 회수를 위해 강제 종료하면 `WebViewClient.onRenderProcessGone()` 이 호출된다. 이 콜백에서 기존 `WebView` 를 재사용하면 안 되고, 뷰 트리에서 제거 후 `destroy()` 하고 새 인스턴스를 만들어야 한다 — 죽은 렌더러에 연결된 `WebView` 는 복구되지 않는다.

```kotlin
override fun onRenderProcessGone(view: WebView, detail: RenderProcessGoneDetail): Boolean {
    if (!detail.didCrash()) {
        // 시스템이 메모리 회수를 위해 렌더러를 죽인 경우: 앱 프로세스는 유지
        val container = webView?.parent as? ViewGroup
        webView?.let { container?.removeView(it); it.destroy() }
        webView = null
        return true // true를 반환하지 않으면 시스템이 앱 프로세스를 종료시킬 수 있다
    }
    return false // 렌더러 자체 크래시: 기본 처리(앱 크래시)에 맡김
}
```

### 판단 기준

- `Fragment` 안에서 `WebView` 를 쓸 때는 `onDestroyView()` 에서 뷰 트리 제거와 `destroy()` 를 함께 호출한다. `onDestroy()` 까지 기다리면 `Fragment` 재사용 시 이미 destroy 된 `WebView` 참조가 남을 수 있다.
- `WebView` 를 리스트/재사용 컨테이너(RecyclerView 등)에 넣는 설계는 피한다. `destroy()` 시점과 뷰 재활용 시점이 꼬이면 크래시나 누수로 이어지기 쉽다.
- `onRenderProcessGone()` 을 구현하지 않은 채 방치하면, 렌더러가 시스템에 의해 회수된 뒤에도 앱이 기본 동작(전체 프로세스 크래시)에 그대로 노출된다.

### 관찰 가능한 신호

- Android Studio Profiler 의 Memory Profiler 에서 `WebActivity` 를 반복적으로 열고 닫았을 때 `WebView` 관련 네이티브 메모리가 계속 증가하면 `destroy()` 누락을 의심할 수 있다.
- `adb shell dumpsys meminfo <package>` 출력의 `Native Heap` 항목이 `WebView` 화면 진입/이탈을 반복할 때마다 회수되지 않고 누적되는지 확인한다.
- `onRenderProcessGone()` 미구현 상태에서 시스템이 렌더러를 회수하면 앱 프로세스 전체가 종료되고, Logcat 에 `Yikes! Renderer crashed` 계열 시스템 메시지가 남는다.

공식 문서: [WebView 관리 — 렌더러 종료 처리와 정리](https://developer.android.com/develop/ui/views/layout/webapps/managing-webview)

검증일: 2026-08-04. `destroy()` 호출 전 뷰 트리 제거 순서, `onRenderProcessGone()` 반환값에 따른 동작 차이를 공식 문서에서 확인했다.
