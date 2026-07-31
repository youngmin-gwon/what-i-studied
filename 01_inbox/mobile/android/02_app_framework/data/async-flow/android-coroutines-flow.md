---
title: android-coroutines-flow
tags: []
aliases: []
date modified: 2026-04-05 17:43:01 +09:00
date created: 2026-04-04 00:13:51 +09:00
---

## [mobile-security](01_inbox/mobile/mobile-security.md) > [android-coroutines-flow](01_inbox/mobile/android/02_app_framework/data/async-flow/android-coroutines-flow.md)

### Coroutines & Flow: Asynchronous Mastery

Kotlin **Coroutines**와 **Flow**를 활용한 안드로이드의 비동기 프로그래밍 모델을 심층 분석합니다.

단순히 스레드를 바꾸는 도구를 넘어, 어떻게 하면 복잡한 비즈니스 로직을 동기 코드처럼 간결하게 유지하면서도 선언적으로 데이터 스트림을 관리할 수 있을지 이해하는 것이 목표입니다.

---

---

## 원자 노트

- [💡 Context: Kotlin Coroutines vs Swift Concurrency](01_inbox/mobile/android/02_app_framework/data/async-flow/android-coroutines-flow/01-context-kotlin-coroutines-vs-swift-concurrency.md)
- [구조적 동시성 (Structured Concurrency)](01_inbox/mobile/android/02_app_framework/data/async-flow/android-coroutines-flow/02-%EA%B5%AC%EC%A1%B0%EC%A0%81-%EB%8F%99%EC%8B%9C%EC%84%B1-structured-concurrency.md)
- [Dispatchers](01_inbox/mobile/android/02_app_framework/data/async-flow/android-coroutines-flow/03-dispatchers.md)
- [예외 처리](01_inbox/mobile/android/02_app_framework/data/async-flow/android-coroutines-flow/04-%EC%98%88%EC%99%B8-%EC%B2%98%EB%A6%AC.md)
- [병렬 실행](01_inbox/mobile/android/02_app_framework/data/async-flow/android-coroutines-flow/05-%EB%B3%91%EB%A0%AC-%EC%8B%A4%ED%96%89.md)
- [Flow](01_inbox/mobile/android/02_app_framework/data/async-flow/android-coroutines-flow/06-flow.md)
- [StateFlow vs SharedFlow](01_inbox/mobile/android/02_app_framework/data/async-flow/android-coroutines-flow/07-stateflow-vs-sharedflow.md)
- [stateIn / shareIn](01_inbox/mobile/android/02_app_framework/data/async-flow/android-coroutines-flow/08-statein-sharein.md)
- [UI 에서 Flow 수집](01_inbox/mobile/android/02_app_framework/data/async-flow/android-coroutines-flow/09-ui-%EC%97%90%EC%84%9C-flow-%EC%88%98%EC%A7%91.md)
- [callbackFlow](01_inbox/mobile/android/02_app_framework/data/async-flow/android-coroutines-flow/10-callbackflow.md)
- [테스팅](01_inbox/mobile/android/02_app_framework/data/async-flow/android-coroutines-flow/11-%ED%85%8C%EC%8A%A4%ED%8C%85.md)
- [🔗 연관 문서 및 심화 학습](01_inbox/mobile/android/02_app_framework/data/async-flow/android-coroutines-flow/12-%EC%97%B0%EA%B4%80-%EB%AC%B8%EC%84%9C-%EB%B0%8F-%EC%8B%AC%ED%99%94-%ED%95%99%EC%8A%B5.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
