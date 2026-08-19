---
title: di
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-06 15:22:00 +09:00
date created: 2026-08-03 16:59:23 +09:00
---

## DI 계약은 전역 객체 접근이 아니라 조립 경계다

DI를 읽을 때는 프레임워크 문법보다 세 질문을 먼저 고정한다. **누가 객체를 만드는가**, **어느 component instance가 재사용과 폐기를 소유하는가**, **잘못된 연결은 빌드와 실행 중 언제 드러나는가**다. 

과거 19개의 개별 노트로 분산되어 있던 원칙들을 다음 핵심 문서들로 통합하였다:

1. [DI 바인딩과 생성 계약](./di-binding-creation.md)
   - 의존성 생성, Constructor Injection, Binds/Provides, Qualifier, Assisted Injection, 그리고 컴파일 에러 검증에 대한 원칙.

2. [DI 소유권과 스코프 계약](./di-ownership-scope.md)
   - Scope, Android Context 주입, [viewmodel](../../viewmodel.md) 및 Worker 소유권 경계, Entry Point, 멀티 모듈 및 Dynamic Feature DI 적용 규칙.

3. [DI 도구 및 엔진 비교](./di-tool-comparison.md)
   - Dagger, Hilt, Koin, Metro 비교 및 Compile-time vs Runtime DI, DSL의 의미.

4. [Metro DI 아키텍처와 멀티모듈 바인딩 계약](./metro-di.md)
   - Kotlin 컴파일러 플러그인 기반 정적 DI, 범용 멀티모듈 Aggregation 구조, ViewModel 멀티바인딩(`metrox-viewmodel`), 패턴 A/B 배선 의사결정 트리.

상위 문서: [Android 의존성 주입 지도](../android-dependency-injection-map.md)

