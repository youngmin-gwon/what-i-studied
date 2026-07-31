# Jetpack Compose 부작용 및 수명 주기 관리 (Side Effects & Lifecycle)

이 문서는 Jetpack Compose에서 안전하게 비동기 작업을 처리하고, 외부 시스템과 상태를 동기화하며, 컴포저블의 생명주기(Lifecycle)에 맞추어 부작용(Side Effect)을 제어하는 핵심 API와 설계 패턴을 설명합니다.

상태나 작업이 어떤 owner 수명에 묶여야 하는지부터 판단해야 한다면 [[jetpack-compose-state-lifetime-api-selection]]를 먼저 봅니다. 이 문서는 각 effect API의 동작과 사용법에 더 집중합니다.

---

---

## 원자 노트

- [[01-부작용-side-effect-이란|부작용(Side Effect)이란?]]
- [[02-핵심-effect-api-올바른-사용법|핵심 Effect API & 올바른 사용법]]
- [[03-고급-effect-상태-최적화-api|고급 Effect & 상태 최적화 API]]
- [[04-실무-안티패턴과-모범-사례-anti-patterns-best-practices|실무 안티패턴과 모범 사례 (Anti-Patterns & Best Practices)]]
- [[05-state-lifetime-callbacks-rememberobserver-retainobserver|State Lifetime Callbacks (`RememberObserver` & `RetainObserver`)]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
