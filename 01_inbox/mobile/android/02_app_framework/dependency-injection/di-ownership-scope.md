---
title: di-ownership-scope
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 15:22:00 +09:00
date created: 2026-08-06 15:22:00 +09:00
---

## DI Ownership and Scope Contracts

### Scope는 owner lifetime에 맞춘 재사용 계약이다
`@Scope` 메커니즘은 "어떤 graph/component instance 안에서 재사용되는가"를 정의한다. Application scope, Activity scope, [viewmodel](../architecture/state-management/viewmodel.md) scope 는 서로 다른 owner lifetime 을 가진다. 짧은 lifetime 객체를 긴 graph 에 넣으면 leak 이 생긴다.

### Android Context는 graph lifetime과 맞아야 한다
Activity 나 Fragment Context 를 app-wide graph 에 넣으면 화면이 사라진 뒤에도 UI owner 가 붙잡힐 수 있으므로, Context의 주입은 component lifetime과 맞아야 한다.

### ViewModel DI는 dependency 주입이지 ViewModel 소유권을 옮기는 일이 아니다
ViewModel 은 화면 상태 owner 이며 lifecycle 은 ViewModelStoreOwner 가 관리한다. DI framework는 필요한 collaborator 를 제공할 뿐, 생명주기 자체를 app graph singleton 으로 바꾸면 안 된다.

### Worker 주입은 WorkManager factory boundary를 지난다
Worker는 WorkManager가 생성하므로, WorkerFactory나 Hilt의 `@HiltWorker` 같은 생성 boundary 를 통과해야 한다.

### Entry point는 framework-owned 객체와 DI graph를 잇는 예외 경계다
앱 코드가 생성자를 호출하지 않는 프레임워크 객체(ex. ContentProvider)는 `@EntryPoint`를 통해 제한적으로 graph 의 dependency 를 꺼내야 한다.

### 멀티 모듈 DI는 module dependency 방향을 따른다
base/app module 은 feature 가 요구하는 contract 를 알 수 있어야 하고, feature 는 자신이 소유한 implementation을 노출해야 한다. 

### Dynamic feature DI는 base-owned contract와 install boundary를 분리해야 한다
base graph가 provision contract를 제공하고, 설치된 feature가 그 contract에 의존하는 별도 component를 만들어야 한다.

### DI 테스트는 graph boundary에서 binding을 교체한다
DI 테스트 시 내부 구현을 건드리지 않고 module replacement나 factory injection을 통해 fake나 test dispatcher를 graph boundary에서 바꿀 수 있다.
