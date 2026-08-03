---
title: testing-quality-contracts
tags: ["android", "android/testing-performance"]
aliases: []
date modified: 2026-08-03 18:15:09 +09:00
date created: 2026-07-31 17:32:53 +09:00
---

## 테스트 품질 계약

이 지도는 테스트를 종류가 아니라 피드백 비용, 실패 신호, 회귀 방지 역할로 나눈다.

### 정본 노트

- [테스트 레이어는 피드백 비용으로 선택한다](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/test-layer-is-chosen-by-feedback-cost-and-risk.md)
- [Unit, Integration, UI, E2E 테스트는 실패 신호가 다르다](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/unit-integration-ui-e2e-tests-have-different-failure-signals.md)
- [Compose UI 테스트는 testTag와 semantics를 분리한다](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/compose-ui-tests-should-use-stable-selectors-and-semantics.md)
- [Screenshot testing은 시각 회귀를 검출한다](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/screenshot-testing-detects-visual-regression-not-business-correctness.md)
- [회귀와 flaky 테스트는 릴리즈 게이트의 신뢰도를 낮춘다](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/regression-and-flaky-tests-are-release-gate-risks.md)

관련 지도: [디버깅 도구 계약](01_inbox/mobile/android/06_testing_performance/debugging/debugging-contracts/debugging-contracts.md), [Benchmark와 Baseline Profile 계약](01_inbox/mobile/android/06_testing_performance/performance/benchmark-baseline-contracts/benchmark-baseline-contracts.md)
