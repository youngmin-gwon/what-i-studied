---
title: Metro는 get_it식 전역 locator가 아니라 compile-time Kotlin DI로 이해한다
tags: ["android", "android/app-framework"]
---

# Metro는 get_it식 전역 locator가 아니라 compile-time Kotlin DI로 이해한다

Flutter `get_it` 경험자는 DI를 전역 registry에서 객체를 꺼내는 방식으로 떠올리기 쉽다. Metro는 Kotlin compiler plugin 기반의 compile-time DI이므로, 핵심은 어디서든 꺼내 쓰는 것이 아니라 graph가 생성자를 호출하고 binding을 검증하게 두는 것이다.

`@DependencyGraph`, `@Inject`, `@Provides`, scope annotation은 "등록 목록"이라기보다 graph construction contract다. Android 앱에서는 이 graph를 Application 또는 feature entry 같은 명확한 owner에 보관해야 한다.

참고 문서: [Metro](https://zacsweers.github.io/metro/latest/)

## 판단 기준

DI 노트는 객체를 어디서 만들고, 누가 소유하며, 어떤 lifetime 동안 재사용할지를 판단하는 기준으로 읽는다.

## 경계

framework 이름보다 graph boundary, scope, replacement seam, Android component lifetime을 먼저 확인한다.
