---
title: dagger-is-static-graph-engine-not-android-lifecycle-policy
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:28:45 +09:00
---

## Dagger 는 정적 graph 엔진이지 Android lifecycle 정책 자체가 아니다
배경 지식: [의존성 역전 원칙](../../../../../../02_references/oop/solid/DIP%28Dependency%20Inversion%20Principle%29.md), [독립 수명 모델](../../../00_foundations/learning-spine/05-independent-lifetimes-of-screen-process-task-and-state.md)

**Dagger**(컴파일 타임에 의존성 그래프를 정적으로 검증하고 코드 생성을 수행하는 Java/Kotlin용 DI 엔진) 는 compile time 에 dependency graph 를 생성하고 검증하는 정적 DI engine 이다. Android 에서 어떤 component 가 Activity, Fragment, ViewModel, Worker 와 어떻게 만나야 하는지는 별도의 integration policy 가 필요하다.

**Hilt**(Dagger를 안드로이드 컴포넌트 생명주기에 맞춰 의존성 그래프 생성을 자동화하는 구글의 공식 DI 라이브러리) 는 이 Android integration 을 표준화한다. 순수 Dagger 를 쓰는 경우에는 component owner, subcomponent/factory, injection timing, test replacement 를 프로젝트가 직접 설계해야 한다.

### 최소 예시

```kotlin
@Singleton
@Component(modules = [AppModule::class])
interface AppComponent {
    fun inject(application: App)

    @Component.Factory
    interface Factory {
        fun create(@BindsInstance application: Application): AppComponent
    }
}

class App : Application() {
    val appComponent by lazy {
        DaggerAppComponent.factory().create(this)
    }
}
```

Dagger는 `AppComponent`를 언제 만들고 어디에 저장할지 결정하지 않는다. 이 예시에서는 `Application`이 component instance를 소유한다. Activity별 subcomponent를 쓴다면 Activity 생성·종료와 맞춰 component reference도 직접 관리해야 한다.

### 실패와 관찰 신호

- 누락 binding, dependency cycle, duplicate binding은 generated component를 compile할 때 dependency trace로 드러난다.
- component를 Activity마다 다시 만들면 `@Singleton`도 Activity마다 다른 instance가 된다.
- app component가 Activity나 View를 잡는 설계는 compiler가 graph type을 검증해도 leak일 수 있다.

공식 문서: [Dagger basic usage](https://dagger.dev/dev-guide/basic-usage), [Dagger on Android](https://developer.android.com/training/dependency-injection/dagger-android)

상위 문서: [DI 계약](./di-contracts.md)
