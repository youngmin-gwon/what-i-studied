# Jetpack Compose 부작용 및 수명 주기 관리 (Side Effects & Lifecycle)

이 문서는 Jetpack Compose에서 안전하게 비동기 작업을 처리하고, 외부 시스템과 상태를 동기화하며, 컴포저블의 생명주기(Lifecycle)에 맞추어 부작용(Side Effect)을 제어하는 핵심 API와 설계 패턴을 설명합니다.

상태나 작업이 어떤 owner 수명에 묶여야 하는지부터 판단해야 한다면 [jetpack-compose-state-lifetime-api-selection](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection.md)를 먼저 봅니다. 이 문서는 각 effect API의 동작과 사용법에 더 집중합니다.

---

---

## 원자 노트

- [부작용(Side Effect)이란?](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-side-effects-and-lifecycle/01-%EB%B6%80%EC%9E%91%EC%9A%A9-side-effect-%EC%9D%B4%EB%9E%80.md)
- [핵심 Effect API & 올바른 사용법](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-side-effects-and-lifecycle/02-%ED%95%B5%EC%8B%AC-effect-api-%EC%98%AC%EB%B0%94%EB%A5%B8-%EC%82%AC%EC%9A%A9%EB%B2%95.md)
- [고급 Effect & 상태 최적화 API](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-side-effects-and-lifecycle/03-%EA%B3%A0%EA%B8%89-effect-%EC%83%81%ED%83%9C-%EC%B5%9C%EC%A0%81%ED%99%94-api.md)
- [실무 안티패턴과 모범 사례 (Anti-Patterns & Best Practices)](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-side-effects-and-lifecycle/04-%EC%8B%A4%EB%AC%B4-%EC%95%88%ED%8B%B0%ED%8C%A8%ED%84%B4%EA%B3%BC-%EB%AA%A8%EB%B2%94-%EC%82%AC%EB%A1%80-anti-patterns-best-practices.md)
- [State Lifetime Callbacks (`RememberObserver` & `RetainObserver`)](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-side-effects-and-lifecycle/05-state-lifetime-callbacks-rememberobserver-retainobserver.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
