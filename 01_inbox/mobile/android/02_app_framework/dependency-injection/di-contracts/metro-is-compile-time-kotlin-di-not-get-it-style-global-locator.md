---
title: metro-is-compile-time-kotlin-di-not-get-it-style-global-locator
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## Metro 는 get_it 식 전역 locator 가 아니라 compile-time Kotlin DI 로 이해한다

Flutter `get_it` 경험자는 DI 를 전역 registry 에서 객체를 꺼내는 방식으로 떠올리기 쉽다. **Metro**(Kotlin Multiplatform 환경 등에서 컴파일 타임 그래프 검증을 수행하는 정적 DI 프레임워크) 는 Kotlin compiler plugin 기반의 compile-time DI 이므로, 핵심은 어디서든 꺼내 쓰는 것이 아니라 graph 가 생성자를 호출하고 binding 을 검증하게 두는 것이다.

`@DependencyGraph`, `@Inject`, `@Provides`, scope annotation 은 "등록 목록"이라기보다 graph construction contract 다. Android 앱에서는 이 graph 를 Application 또는 feature entry 같은 명확한 owner 에 보관해야 한다.

참고 문서: [Metro](https://zacsweers.github.io/metro/latest/)

### 판단 기준

DI 노트는 객체를 어디서 만들고, 누가 소유하며, 어떤 lifetime 동안 재사용할지를 판단하는 기준으로 읽는다.

### 경계

framework 이름보다 graph boundary, scope, replacement seam, Android component lifetime 을 먼저 확인한다.
