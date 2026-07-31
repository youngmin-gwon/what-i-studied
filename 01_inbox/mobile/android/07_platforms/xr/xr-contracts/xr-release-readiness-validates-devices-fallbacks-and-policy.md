---
title: "XR 출시 준비는 기능 시연이 아니라 기기, fallback, 정책 검증이다"
tags: ["android", "android/platforms"]
---

# XR 출시 준비는 기능 시연이 아니라 기기, fallback, 정책 검증이다

상위 문서: [Android XR 계약](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-contracts.md)

XR 앱이 한 번 실행되는 것과 출시 가능한 것은 다르다. 지원 기기, SDK 성숙도, runtime capability, 입력 fallback, 성능, 편안함, 권한, Play 배포 정책까지 반복 검증해야 출시 준비라고 볼 수 있다.

## 체크 기준

- 지원 폼 팩터를 XR headset, wired XR glasses, audio glasses, display glasses 중 어디까지로 둘지 명시한다.
- 필수 capability가 없거나 권한이 거부되었을 때 2D 또는 축소 기능 fallback이 남아야 한다.
- 실제 기기와 emulator에서 frame pacing, 발열, 배터리, 텍스트 가독성, 장시간 사용 편안함을 확인한다.
- alpha/beta 라이브러리는 API 변경 비용을 release risk로 기록한다.
- Play 배포, 스토어 등록, 기기 호환성 정책은 출시 직전 공식 문서 기준으로 재확인한다.

## 관련 문서

- [Jetpack XR SDK는 preview 성숙도를 전제로 채택해야 한다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/jetpack-xr-sdk-adoption-depends-on-preview-maturity.md)
- [XR 앱은 공간 capability를 실행 중에 확인해야 한다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-apps-must-check-spatial-capabilities-at-runtime.md)
- [XR 품질은 성능, 편안함, 안전을 기능 요구사항으로 포함한다](01_inbox/mobile/android/07_platforms/xr/xr-contracts/xr-quality-includes-performance-comfort-and-safety.md)
- [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)

공식 문서: [Develop with the Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk), [AndroidX releases](https://developer.android.com/jetpack/androidx/versions)

기준일: 2026-07-31. Android XR SDK는 Developer Preview 문서가 남아 있고, 일부 XR AndroidX 라이브러리는 alpha 또는 beta 단계이므로 출시 전 다시 확인한다.
