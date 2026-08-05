---
title: compile-time-and-runtime-di-fail-at-different-points
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Compile-time DI 와 runtime DI 는 실패 시점이 다르다

DI framework 비교의 핵심은 문법보다 graph 오류가 언제 드러나는가다. **Hilt**(**Dagger**(컴파일 타임에 의존성 그래프를 정적으로 검증하고 코드 생성을 수행하는 Java/Kotlin용 DI 엔진)를 안드로이드 컴포넌트 생명주기에 맞춰 의존성 그래프 생성을 자동화하는 구글의 공식 DI 라이브러리), Dagger, **Metro**(Kotlin Multiplatform 환경 등에서 컴파일 타임 그래프 검증을 수행하는 정적 DI 프레임워크) 같은 compile-time DI 는 누락 binding, cycle, 잘못된 graph wiring 을 build 단계에서 더 많이 드러내려 한다.

**Koin**(코드 생성 없이 런타임에 서비스 로케이터 방식으로 의존성을 주입하는 Kotlin 전용 DSL 기반 DI 프레임워크) 이나 `get_it` 처럼 runtime resolution 성격이 강한 도구는 설정과 실험이 빠를 수 있지만, binding 오류가 실행 경로에서 드러날 수 있다. 작은 앱에서는 편의가 이길 수 있고, 큰 앱이나 multi-module graph 에서는 검증 시점이 architecture 비용을 크게 바꾼다.

관련 노트: [Hilt](./hilt-is-official-android-dagger-integration.md), [Metro](./metro-is-compile-time-kotlin-di-not-get-it-style-global-locator.md), [Koin](./koin-trades-compile-time-graph-generation-for-runtime-dsl-convenience.md).

### 판단 기준

DI 노트는 객체를 어디서 만들고, 누가 소유하며, 어떤 lifetime 동안 재사용할지를 판단하는 기준으로 읽는다.

### 경계

framework 이름보다 graph boundary, scope, replacement seam, Android component lifetime 을 먼저 확인한다.
