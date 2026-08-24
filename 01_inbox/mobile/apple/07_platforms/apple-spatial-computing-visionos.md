---
title: apple-spatial-computing-visionos
tags: [apple, apple/26, arkit, spatial-computing, vision-pro, visionos]
aliases: [Apple Vision Pro, ARKit, Spatial Computing, visionOS]
date modified: 2026-08-10 00:00:00 +09:00
date created: 2026-04-04 00:33:00 +09:00
---

## Apple Spatial Computing: visionOS

visionOS 는 Apple Vision Pro 를 위한 전용 운영체제로, 2025 년 버전 대점프(Version Jump)를 통해 **visionOS 26**으로 진화하였다. "모니터 너머의 캔버스"를 현실 공간으로 확장하며, 기존 iOS/iPadOS 생태계를 공간 컴퓨팅으로 완벽하게 흡수한다.

>[!NOTE] **Android 비교: Android XR vs visionOS**
> - **Android/Android XR**: Google, Samsung, Qualcomm 의 협업 플랫폼. Gemini AI 기반의 멀티모달(Multimodal) 에이전트 경험과 개방적인 생태계가 강점이다.
> - **iOS/visionOS**: Apple 의 전용 칩셋(R1, M2)을 활용한 12ms 이내의 극도로 낮은 지연 시간과 **Foveated Streaming**을 통한 초고지연성 경험이 강점이다. (visionOS 26+)
>자세한 내용은 [**android-xr-and-spatial-computing**](../../android/07_platforms/xr/xr.md) 를 참고하세요.

### 1. visionOS 26 신규 기능 (2026 Standard)

- **Foveated Streaming (visionOS 26.4)**: 사용자가 바라보는 지점만 고해상도로 렌더링하고 나머지는 낮추는 기술을 호스트 PC 나 클라우드 스트리밍에서도 지원하여 무거운 시뮬레이션 앱 구동이 가능해졌다.
- **Shared Spatial Context**: 사용자의 물리적 공간(방의 구조 등)에 대한 음향/조명 메타데이터를 시스템이 기억하고 재활용하여 더 빠른 몰입형 환경 로딩을 지원한다.

### 2. 공간 컴퓨팅 앱 구조 (Spatial App Architecture)

visionOS의 Window/Volume/Space 개념과 입력 방식(Eyes & Hands)은 [apple-visionos-system.md](apple-visionos-system.md)에서 자세히 다룹니다.

---

### 🏛️ 공간 컴퓨팅 시대의 앱 설계

사용자의 시야를 점유한다는 것은 강력한 힘인 동시에 배려가 필요한 작업이다.

>[!IMPORTANT] **Apple 개발자를 위한 제언 : 앱의 무게감(Mass)**
>visionOS 에서 앱은 실제 사물처럼 "무게감"과 "공간감"을 가져야 한다. **Liquid Glass** 디자인 언어를 적극 활용하여 그림자와 반사 효과를 통해 앱이 실제 공간에 떠 있는 것처럼 느끼게 하는 것이 핵심이다. 단순한 2D 창 띄우기는 사용자에게 몰입을 방해하는 '불청객'이 될 수 있다.

### 더 보기

- [apple-app-intents](../04_system_services/apple-app-intents.md) - 공간 상의 기능 실행
- [apple-swiftui-deep-dive](../02_ui_frameworks/apple-swiftui-deep-dive.md) - Liquid Glass 디자인 구현
- [apple-intelligence-and-agentic-intents](../04_system_services/apple-intelligence-and-agentic-intents.md) - Siri 공간 명령 처리
