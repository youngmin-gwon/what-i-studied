---
title: "XR 품질은 성능, 편안함, 안전을 기능 요구사항으로 포함한다"
tags: ["android", "android/platforms"]
---

# XR 품질은 성능, 편안함, 안전을 기능 요구사항으로 포함한다

상위 문서: [Android XR 계약](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md)

XR에서 성능 문제는 단순히 프레임이 낮은 UI 문제가 아니다. 지연, 흔들림, 과도한 움직임, 잘못된 거리와 크기는 멀미, 피로, 조작 실패, 안전 문제로 이어질 수 있다.

## 실무 규칙

- frame pacing, latency, 3D asset 크기, animation 비용을 일반 Android UI보다 엄격하게 본다.
- panel과 3D object의 거리, 크기, 대비는 오래 보아도 피로하지 않게 정한다.
- 갑작스러운 camera movement, 강제 이동, 사용자를 둘러싼 UI 과밀 배치를 피한다.
- passthrough, scene understanding, anchor 같은 기능은 권한과 사생활 기대를 함께 검토한다.
- release 전에 실제 XR 기기 또는 공식 emulator에서 입력, comfort, fallback을 검증한다.

## 관련 문서

- [성능 계약](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/performance-contracts.md)
- [Jetpack XR SDK는 preview 성숙도를 전제로 채택해야 한다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/jetpack-xr-sdk-adoption-depends-on-preview-maturity.md)
