---
title: apple-visionos-system
tags: [apple, apple/platforms, apple/platforms/visionos, arkit, immersive, privacy, realitykit, spatial, vision-pro, visionos]
aliases: ["visionOS 는 시선 데이터를 앱에 넘기지 않고 Space 종류가 렌더링 권한을 결정한다", "Apple Vision Pro", "Spatial Computing", "visionOS System Internals", "visionOS 시스템"]
date modified: 2026-09-03 00:00:00 +09:00
date created: 2025-12-18 00:00:00 +09:00
---

## visionOS 는 시선 데이터를 앱에 넘기지 않고 Space 종류가 렌더링 권한을 결정한다

visionOS 의 두 가지 근본 제약이 앱 설계를 지배한다. 첫째, **시선(Eye)은 시스템만 안다** — 사용자가 어디를 보는지는 단 1 프레임도 앱에 전달되지 않는다. 둘째, **앱이 어느 Space 에 있느냐가 쓸 수 있는 렌더링 API 와 센서 데이터를 결정한다** — Shared Space 에서는 RealityKit 만, Full Space 에서는 Metal 직접 렌더링과 손 골격 데이터까지 열린다. 이 두 제약을 모르면 구현 불가능한 기능을 설계하게 된다.

> [!NOTE] **Android 비교: Android XR vs visionOS**
> - **Android XR**: Google, Samsung, Qualcomm 의 협업 플랫폼. Gemini AI 기반의 멀티모달(Multimodal) 에이전트 경험과 개방적인 생태계가 강점이다.
> - **visionOS**: Apple 의 전용 칩셋(R1, M2)을 활용한 낮은 지연 시간과 **Foveated Streaming** 이 강점이다.
> 자세한 내용은 [android-xr-and-spatial-computing](../../android/07_platforms/xr/xr.md) 를 참고한다.

### 💡 왜 이것을 알아야 하나요? (Context)

- **Eye Tracking Privacy**: "사용자가 어디를 보고 있는지 데이터를 달라"는 요청은 불가능하다. 이 제약을 이해해야 UI 를 설계할 수 있다.
- **Shared Space vs Full Space**: 내 앱이 거실에 다른 앱들과 같이 떠 있을지(Shared), 아니면 사용자의 방 전체를 장악할지(Full) 결정해야 한다. 이 둘은 렌더링 파이프라인이 다르다.
- **Volumes**: 2D 윈도우가 아니라, 3D 객체(예: 농구공)를 띄우려면 Window 대신 Volume 을 써야 한다.

---

### 👁️ Privacy & Input Model

가장 중요한 차이점이다. 시스템은 **사용자가 무엇을 보는지 앱이 모르게** 한다.

1. **Hover Effect (System Level)**: 사용자가 버튼을 쳐다보면 버튼이 밝아진다. 이건 시스템이 처리하며, 앱은 아직 모른다.
2. **Tap (Pinch)**: 사용자가 손가락을 꼬집는 순간, 그제서야 앱은 "이 버튼이 눌렸다"는 이벤트를 받는다.
3. **Implication**: "사용자가 광고를 3 초 동안 쳐다봤으니 과금" 같은 로직은 구현 불가능하다.
4. **설계 귀결**: 눈으로 조준하는 입력이므로 터치 타깃이 iOS 기준보다 커야 한다. 작은 버튼은 시선 조준 자체가 어렵다.

---

### 🌌 Spaces & Rendering

#### 1. Shared Space (기본값)

여러 앱이 동시에 떠 있는 상태다.

- **RealityKit**: 시스템이 제공하는 렌더러를 써야 한다. 그래야 다른 앱과 조명(Lighting), 그림자(Shadow)를 공유하며 자연스럽게 어우러진다.
- **ARKit 제약**: 손 골격 데이터는 받을 수 없다. 보안상 차단된다.

#### 2. Full Space (Immersive Space)

내 앱만 존재하는 상태다.

- **Compositor Services**: Metal 을 직접 써서 렌더링할 수 있다. (Custom Rendering)
- **ARKit Hand Tracking**: 이때는 사용자의 손 골격(Skeletal Data) 정보를 받을 수 있다.
- **Plane Detection**: 방의 바닥/벽 인식 등 현실 세계 데이터도 Full Space 에서만 열린다.

---

### 🛠️ 개발 프레임워크의 역할 분담

visionOS 는 완전히 새로운 것이 아니라 **SwiftUI + RealityKit + ARKit** 의 융합체다.

- **SwiftUI**: 레이아웃, 버튼, 텍스트 등 2D 요소와 전반적인 앱 구조를 담당한다.
- **RealityKit**: 3D 모델 렌더링, 물리 엔진, 파티클 효과, 조명을 담당한다.
- **ARKit**: (Full Space 에서만) 손 관절 위치, 평면 인식 등 현실 세계 데이터를 제공한다.

UIKit 은 사실상 레거시 브릿지에 불과하며, **SwiftUI 및 RealityKit 사용**이 현대의 표준이다.

- **WindowGroup**: 2D 평면 윈도우. 깊이(Depth)를 줄 수 있지만 기본은 판판하다.
- **Volumetric Window**: 3D 부피를 가진 큐브 형태. 사용자가 걸어 다니며 360 도로 볼 수 있다.
- **Ornaments**: 윈도우 밖으로 튀어나온 툴바/탭바. 시선을 따라다니지 않고 윈도우에 붙어 있다.

---

### 🆕 visionOS 26 (2026 Standard)

2025 년 버전 대점프(Version Jump)를 통해 **visionOS 26** 으로 통합되었다.

- **Foveated Streaming**: 사용자가 바라보는 지점만 고해상도로 렌더링하고 나머지는 낮추는 기술을 호스트 PC 나 클라우드 스트리밍에서도 지원하여 무거운 시뮬레이션 앱 구동이 가능해졌다.
- **Shared Spatial Context**: 사용자의 물리적 공간(방의 구조 등)에 대한 음향/조명 메타데이터를 시스템이 기억하고 재활용하여 더 빠른 몰입형 환경 로딩을 지원한다.

> [!IMPORTANT] **앱의 무게감(Mass)**
> visionOS 에서 앱은 실제 사물처럼 "무게감"과 "공간감"을 가져야 한다. **Liquid Glass** 디자인 언어를 활용해 그림자와 반사로 앱이 실제 공간에 떠 있는 것처럼 느끼게 하는 것이 핵심이다. 단순한 2D 창 띄우기는 몰입을 방해한다.

### 더 보기

**visionOS 심화**
- [apple-visionos-design-patterns](visionos/apple-visionos-design-patterns.md) - 공간 설계 패턴
- [apple-visionos-immersion-guide](visionos/apple-visionos-immersion-guide.md) - 몰입형 앱 개발 가이드

**관련 기술**
- [apple-rendering-and-media](../02_ui_frameworks/apple-rendering-and-media.md) - Metal 렌더링 파이프라인
- [apple-swiftui-deep-dive](../02_ui_frameworks/apple-swiftui-deep-dive.md) - Liquid Glass 디자인 구현
- [apple-app-intents](../04_system_services/apple-app-intents.md) - 공간 상의 기능 실행
- [apple-intelligence-and-agentic-intents](../04_system_services/apple-intelligence-and-agentic-intents.md) - Siri 공간 명령 처리
- [apple-ipados-multitasking](../04_system_services/apple-ipados-multitasking.md) - 멀티 윈도우 관리 (비슷한 개념)
- [apple-platform-differences](../00_foundations/apple-platform-differences.md) - 다른 플랫폼과의 차이점
