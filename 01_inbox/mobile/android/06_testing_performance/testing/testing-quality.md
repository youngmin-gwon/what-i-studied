---
title: testing-quality
tags: ["android", "android/testing-performance"]
aliases: ["testing-quality-contracts"]
date modified: 2026-08-04 18:00:00 +09:00
date created: 2026-07-31 17:32:53 +09:00
---

## 테스트 품질 계약

이 지도는 테스트를 단순한 종류 구분이 아니라 피드백 속도, 실행 비용, 실패 신호의 격리 범위, 회귀 방지 피라미드 계약으로 나눈다.

### 테스트 피라미드 & 피드백 속도 계약

```mermaid
flowchart TD
    E2E["E2E Test<br/>(Real Device / Full Flow / High Cost / Slow)"]
    UITest["UI Test / Screenshot Test<br/>(Compose Rule / Roborazzi / Medium Cost)"]
    Integration["Integration Test<br/>(Robolectric / Fake Repositories / Low Cost)"]
    UnitTest["Unit Test<br/>(JVM Local / Pure Coroutines & Logic / Instant Feedback)"]

    UnitTest --> Integration
    Integration --> UITest
    UITest --> E2E
```

## 정본 노트

- [테스트 레이어는 피드백 비용으로 선택한다](test-pyramid-strategy.md)
- [Unit, Integration, UI, E2E 테스트는 실패 신호가 다르다](test-levels-failure-signals.md)
- [Compose UI 테스트는 testTag와 semantics를 분리한다](compose-ui-tests-semantics.md)
- [Espresso 는 View 기반 UI 를 동기적으로 테스트하며 IdlingResource 로 비동기 작업 완료를 기다린다](espresso-idling-resources.md)
- [Screenshot testing은 시각 회귀를 검출한다](screenshot-testing-visual-regression.md)
- [회귀와 flaky 테스트는 릴리즈 게이트의 신뢰도를 낮춘다](flaky-tests-regression-gates.md)
- [Coroutine 과 Flow 테스트는 dispatcher 와 virtual time 을 통제해야 한다](coroutine-flow-testing.md)
- [CI는 Firebase Test Lab 같은 클라우드 디바이스 매트릭스에서 테스트를 실행하고 로컬 에뮬레이터 매트릭스와는 다른 계약을 가진다](firebase-test-lab-matrix.md)
- [파이프라인 sharding 은 테스트 개수가 아니라 과거 실행 시간 기준으로 분배해야 한다](test-pipeline-sharding.md)
- [TalkBack 수동 검증과 Accessibility Scanner 자동 검사는 서로 다른 결함군을 잡는다](accessibility-testing-scanner-talkback.md)
- [Test double는 행동의 소유권으로 Fake와 Mock을 구분해 선택한다](test-doubles-fake-vs-mock.md)

관련 지도: [Android 성능, 품질, 빌드 최적화 지도](../android-performance-testing-map.md), [디버깅 도구 계약](../debugging/debugging.md), [Benchmark와 Baseline Profile 계약](../benchmark/benchmark-baseline.md)
