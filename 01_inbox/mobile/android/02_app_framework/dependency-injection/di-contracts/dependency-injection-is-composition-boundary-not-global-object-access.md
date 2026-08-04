---
title: dependency-injection-is-composition-boundary-not-global-object-access
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-03 18:09:24 +09:00
date created: 2026-08-03 16:28:45 +09:00
---

## DI 는 전역 객체 접근이 아니라 조립 경계다

Dependency Injection 의 핵심은 필요한 객체를 소비자가 직접 만들거나 전역 registry 에서 꺼내지 않고, 바깥 조립 경계에서 연결해 넣는 것이다. 이렇게 해야 객체 생성 정책, 테스트 대체, lifetime 이 사용 코드와 분리된다.

Android 에서는 이 조립 경계가 `Application`, feature entry, screen owner, Worker factory 처럼 OS/framework lifetime 과 만나는 지점에 놓인다. DI framework 선택보다 먼저 정해야 하는 것은 어떤 객체가 어떤 owner 아래에서 만들어지고 재사용되는가다.

관련 노트: [app architecture](../../architecture/android-app-architecture.md), [Context boundaries](../../architecture/context-and-modularity/android-context-boundaries.md).

### 판단 기준

- DI 는 객체 조립(Composition)을 외부로 위임하기 위한 경계다. 서비스 로케이터 패턴처럼 임의의 위치에서 전역적으로 객체를 가져오는 용도로 DI 컨테이너를 직접 참조해서는 안 된다.

### 경계

- DI 컨테이너(그래프) 접근은 앱의 최상위 Entry Point 나 프레임워크가 인스턴스화를 통제하는 곳(UI 레이어 등)으로만 제한하고, 일반 클래스 내부에서는 의존성을 주입받기만 해야 한다.
