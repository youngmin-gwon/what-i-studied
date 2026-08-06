---
title: entry-points-bridge-framework-owned-objects-to-the-graph
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Entry point 는 framework-owned 객체와 DI graph 를 잇는 예외 경계다

Android 에는 앱 코드가 생성자를 호출하지 않는 객체가 많다. Hilt가 직접 지원하지 않는 `ContentProvider`나 일부 framework callback 주변 코드는 DI graph 안에서 자연스럽게 생성되지 않을 수 있다. 반면 `BroadcastReceiver`는 `@AndroidEntryPoint`를 지원하며 `SingletonComponent`의 binding을 주입받으므로 entry point가 필수라는 설명은 틀리다.

**Entry Point**(`@EntryPoint` — 안드로이드 OS가 생성하는 프레임워크 객체에서 Hilt DI 그래프에 접근하기 위한 비상 인터페이스 경계) 는 이런 framework-owned 객체가 graph 의 dependency 를 꺼내야 할 때 쓰는 명시적 bridge 다. 하지만 entry point 를 아무 곳에서나 service locator 처럼 쓰면 DI 의 장점이 사라지므로, framework 가 소유한 경계에서만 제한적으로 사용한다.

관련 노트: [Hilt integration](./hilt-is-official-android-dagger-integration.md), [Worker injection](./worker-injection-crosses-workmanager-factory-boundary.md).

### 최소 예시

```kotlin
@EntryPoint
@InstallIn(SingletonComponent::class)
interface ProviderDependencies {
    fun startupRecorder(): StartupRecorder
}

class AppContentProvider : ContentProvider() {
    override fun onCreate(): Boolean {
        val app = requireNotNull(context).applicationContext
        EntryPointAccessors.fromApplication(app, ProviderDependencies::class.java)
            .startupRecorder()
            .recordProviderStart()
        return true
    }
}
```

accessor에 넘기는 holder와 `@InstallIn` component가 일치해야 한다. interface에는 경계가 실제로 필요한 최소 provision만 노출하고 container 전체나 범용 `get()`은 노출하지 않는다.

### 실패와 관찰 신호

- 잘못된 component accessor를 쓰면 runtime cast/access 오류가 나거나 기대한 scope의 binding을 볼 수 없다.
- entry point method의 return binding이 component에 없으면 generated graph build가 실패한다.
- Repository/ViewModel에서 `EntryPointAccessors` import가 발견되면 service locator로 번진 신호다.

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Hilt entry points](https://dagger.dev/hilt/entry-points.html), [Hilt supported Android classes](https://developer.android.com/training/dependency-injection/hilt-android#inject-android-classes)
