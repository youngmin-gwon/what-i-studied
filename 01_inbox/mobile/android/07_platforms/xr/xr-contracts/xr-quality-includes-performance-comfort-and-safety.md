---
title: "XR 품질은 성능, 편안함, 안전을 기능 요구사항으로 포함한다"
tags: ["android", "android/platforms"]
---

# XR 품질은 성능, 편안함, 안전을 기능 요구사항으로 포함한다

상위 문서: [Android XR 계약](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md)

XR에서 성능 문제는 단순히 프레임이 낮은 UI 문제가 아니다. 지연, 흔들림, 과도한 움직임, 잘못된 거리와 크기는 멀미, 피로, 조작 실패, 안전 문제로 이어질 수 있다.

## 실무 규칙

- rendering은 공식 품질 기준의 90Hz에서 프레임당 11.1ms 미만, 72Hz에서 13.8ms 미만을 측정하고 latency, 3D asset, animation 비용을 함께 본다.
- panel과 3D object의 거리, 크기, 대비는 오래 보아도 피로하지 않게 정한다.
- 갑작스러운 camera movement, 강제 이동, 사용자를 둘러싼 UI 과밀 배치를 피한다.
- passthrough, scene understanding, anchor 같은 기능은 권한과 사생활 기대를 함께 검토한다.
- release 전에 실제 XR 기기 또는 공식 emulator에서 입력, comfort, fallback을 검증한다.

## 테스트 경계

emulator는 space 전환, capability fallback, UI와 입력 흐름의 반복 검증에 적합하지만 착용감, 멀미, tracking 품질, 광학 가독성, 발열과 배터리는 검증하지 못한다. comfort와 장시간 성능은 지원하는 실제 기기에서 별도 통과시킨다.

## 관련 문서

- [성능 계약](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/performance-contracts.md)
- [Jetpack XR SDK는 preview 성숙도를 전제로 채택해야 한다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/jetpack-xr-sdk-adoption-depends-on-preview-maturity.md)

공식 문서: [Android XR app quality](https://developer.android.com/docs/quality-guidelines/android-xr), [Create virtual XR devices](https://developer.android.com/develop/xr/jetpack-xr-sdk/run/create-avds/xr-headsets-glasses)

검증일: 2026-08-03. 수치 기준과 지원 emulator 종류는 출시 직전에 재확인한다.
