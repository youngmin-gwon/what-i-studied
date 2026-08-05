---
title: koin-trades-compile-time-graph-generation-for-runtime-dsl-convenience
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Koin 은 런타임 DSL 편의와 정적 graph 검증의 트레이드오프를 가진다

**Koin**(코드 생성 없이 런타임에 서비스 로케이터 방식으로 의존성을 주입하는 Kotlin 전용 DSL 기반 DI 프레임워크) 은 Kotlin DSL 로 binding 을 선언하고 런타임에 dependency 를 resolve 하는 방식에 가깝다. 설정이 가볍고 읽기 쉬운 장점이 있지만, **Dagger**(컴파일 타임에 의존성 그래프를 정적으로 검증하고 코드 생성을 수행하는 Java/Kotlin용 DI 엔진)/**Hilt**(Dagger를 안드로이드 컴포넌트 생명주기에 맞춰 의존성 그래프 생성을 자동화하는 구글의 공식 DI 라이브러리) 같은 정적 graph generation 과는 실패 시점과 검증 방식이 다르다.

따라서 Koin 을 선택할 때는 간단한 setup 만 보지 말고 startup cost, runtime resolution failure, module loading, test override, IDE/build integration 까지 같이 판단한다.

### 판단 기준

DI 노트는 객체를 어디서 만들고, 누가 소유하며, 어떤 lifetime 동안 재사용할지를 판단하는 기준으로 읽는다.

### 경계

framework 이름보다 graph boundary, scope, replacement seam, Android component lifetime 을 먼저 확인한다.
