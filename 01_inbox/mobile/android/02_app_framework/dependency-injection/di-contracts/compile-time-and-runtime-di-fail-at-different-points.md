---
title: compile-time-and-runtime-di-fail-at-different-points
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 14:55:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Compile-time DI 와 runtime DI 는 실패 시점이 다르다

DI framework 비교의 핵심은 문법보다 graph 오류가 언제 드러나는가다. **Hilt**(**Dagger**(컴파일 타임에 의존성 그래프를 정적으로 검증하고 코드 생성을 수행하는 Java/Kotlin용 DI 엔진)를 안드로이드 컴포넌트 생명주기에 맞춰 의존성 그래프 생성을 자동화하는 구글의 공식 DI 라이브러리), Dagger, **Metro**(Kotlin Multiplatform 환경 등에서 컴파일 타임 그래프 검증을 수행하는 정적 DI 프레임워크) 같은 compile-time DI 는 누락 binding, cycle, 잘못된 graph wiring 을 build 단계에서 더 많이 드러내려 한다.

Koin classic DSL처럼 runtime resolution 성격이 강한 구성은 binding 오류가 해당 실행 경로에서 처음 드러날 수 있다. 다만 Koin도 `verify()`와 compiler plugin을 제공하므로 “Koin은 항상 runtime에만 검증된다”는 비교는 정확하지 않다.

관련 노트: [Hilt](./hilt-is-official-android-dagger-integration.md), [Metro](./metro-is-compile-time-kotlin-di-not-get-it-style-global-locator.md), [Koin](./koin-trades-compile-time-graph-generation-for-runtime-dsl-convenience.md).

### 실패 시점 비교

| 구성 | 주로 잡는 시점 | 누락 `UserApi`의 관찰 신호 |
| --- | --- | --- |
| Dagger / Hilt | generated graph compile | `[Dagger/MissingBinding]`과 dependency trace |
| Metro | Kotlin compiler plugin 실행 | graph에 공급할 수 없다는 compiler diagnostic |
| Koin classic DSL | `verify()` test 또는 최초 resolution | verification error나 `NoDefinitionFoundException` 계열 예외 |
| Koin compiler plugin | build | 생성자와 DSL binding 분석 diagnostic |

```kotlin
class UserRepository @Inject constructor(private val api: UserApi)
```

정적 graph도 provider body 안의 잘못된 URL, DB open 실패, 서버 응답 같은 동적 조건까지 증명하지는 못한다. 반대로 runtime container도 모든 entry path를 `verify()` 입력과 integration test로 실행하면 오류를 상당히 앞당길 수 있다. 비교 기준은 이분법보다 **검증되는 graph 범위와 남는 동적 조건**이다.

상위 문서: [DI 계약](./di-contracts.md)

공식 문서: [Dagger compile-time validation](https://dagger.dev/dev-guide/basic-usage), [Koin module verification](https://insert-koin.io/docs/reference/koin-test/verify/), [Metro dependency graphs](https://zacsweers.github.io/metro/latest/dependency-graphs/)
