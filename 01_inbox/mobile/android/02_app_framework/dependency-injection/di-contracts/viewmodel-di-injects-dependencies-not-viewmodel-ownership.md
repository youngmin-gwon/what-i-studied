---
title: viewmodel-di-injects-dependencies-not-viewmodel-ownership
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## ViewModel DI 는 dependency 주입이지 ViewModel 소유권을 DI graph 로 옮기는 일이 아니다

ViewModel 은 화면 상태 owner 이며 lifecycle 은 ViewModelStoreOwner 가 관리한다. DI framework 는 ViewModel 이 필요로 하는 Repository, UseCase, dispatcher, saved state collaborator 를 제공할 수 있지만, ViewModel 생명주기 자체를 임의의 app graph singleton 으로 바꾸면 안 된다.

**Hilt**(**Dagger**(컴파일 타임에 의존성 그래프를 정적으로 검증하고 코드 생성을 수행하는 Java/Kotlin용 DI 엔진)를 안드로이드 컴포넌트 생명주기에 맞춰 의존성 그래프 생성을 자동화하는 구글의 공식 DI 라이브러리) 의 `@HiltViewModel` 이나 수동 `ViewModelProvider.Factory` 는 DI graph 와 ViewModel owner 사이의 연결 boundary 다. Compose 에서 ViewModel 을 얻을 때도 screen owner 와 navigation back stack owner 를 먼저 확인해야 한다.

관련 노트: [ViewModel](../../architecture/state-management/viewmodel/viewmodel.md), [Compose runtime/state](../../jetpack-compose/runtime/compose-runtime-and-state-model.md).

### 판단 기준

- ViewModel 에 대한 DI 는 의존성을 주입하는 역할일 뿐이며, ViewModel 의 실제 소유권과 생명주기 관리는 DI 컨테이너가 아니라 안드로이드 ViewModelProvider(ViewModelStore)가 담당한다.

### 경계

- ViewModel 내부에 `@Inject` 로 의존성을 선언하되, Activity 나 Fragment 에 주입할 때는 직접 주입받지 않고 `by viewModels()` 델리게이트나 프레임워크 지원 팩토리를 통해 생성해야 생명주기가 유지된다.
