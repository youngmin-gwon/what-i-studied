---
title: apple-spatial-computing-visionos
tags: [apple, apple/26, visionos, spatial-computing, vision-pro, arkit]
aliases: [visionOS, Spatial Computing, Apple Vision Pro, ARKit]
date modified: 2026-04-04 00:33:00 +09:00
date created: 2026-04-04 00:33:00 +09:00
---

## Apple Spatial Computing: visionOS

visionOS는 Apple Vision Pro를 위한 전용 운영체제로, 2025년 버전 대점프(Version Jump)를 통해 **visionOS 26**으로 진화하였다. "모니터 너머의 캔버스"를 현실 공간으로 확장하며, 기존 iOS/iPadOS 생태계를 공간 컴퓨팅으로 완벽하게 흡수한다.

> [!NOTE] **Android 비교: Android XR vs visionOS**
> - **Android/Android XR**: Google, Samsung, Qualcomm의 협업 플랫폼. Gemini AI 기반의 멀티모달(Multimodal) 에이전트 경험과 개방적인 생태계가 강점이다.
> - **iOS/visionOS**: Apple의 전용 칩셋(R1, M2)을 활용한 12ms 이내의 극도로 낮은 지연 시간과 **Foveated Streaming**을 통한 초고지연성 경험이 강점이다. (visionOS 26+)
> 자세한 내용은 [android-xr-and-spatial-computing](../../android/07_platforms/android-xr-and-spatial-computing.md)를 참고하세요.

### 1. visionOS 26 신규 기능 (2026 Standard)

- **Foveated Streaming (visionOS 26.4)**: 사용자가 바라보는 지점만 고해상도로 렌더링하고 나머지는 낮추는 기술을 호스트 PC나 클라우드 스트리밍에서도 지원하여 무거운 시뮬레이션 앱 구동이 가능해졌다.
- **Shared Spatial Context**: 사용자의 물리적 공간(방의 구조 등)에 대한 음향/조명 메타데이터를 시스템이 기억하고 재활용하여 더 빠른 몰입형 환경 로딩을 지원한다.

### 2. 공간 컴퓨팅 앱 구조 (Spatial App Architecture)

visionOS 앱 개발은 기존 SwiftUI 지식을 기반으로 하지만, "공간(Volume/Window)"에 대한 개념이 추가된다.

#### Window, Volume, Space

| 요소 | 설명 | 비유 |
| :--- | :--- | :--- |
| **Window** | 2D 평면 콘텐츠 | 벽에 붙은 디지털 포스터 |
| **Volume** | 3D 경계가 있는 정육면체 공간 | 거실 테이블 위의 디지털 조각상 |
| **Space** | 전체 시야를 점유하는 몰입형 환경 | 공간 전체가 영화관이나 숲으로 변함 |

```swift
// SwiftUI for visionOS 예시
@main
struct SpatialApp: App {
    var body: some Scene {
        WindowGroup {
            MainView() // 2D 윈도우
        }
        
        WindowGroup(id: "model-viewer") {
            ModelView() // 3D 볼륨으로 확장 가능
        }
        .windowStyle(.volumetric)
    }
}
```

### 3. 입력 방식: 시선과 제스처 (Eyes & Hands)

가장 자연스러운 인터페이스인 **Look & Tap**을 사용한다.
- **Eye Tracking**: 시선은 곧 "포커스"이다.
- **Hand Gestures**: 검지와 엄지를 부딪치는 것(Tap)은 곧 "클릭"이다.

---

### 🏛️ 공간 컴퓨팅 시대의 앱 설계

사용자의 시야를 점유한다는 것은 강력한 힘인 동시에 배려가 필요한 작업이다.

> [!IMPORTANT] **Apple 개발자를 위한 제언 : 앱의 무게감(Mass)**
> visionOS에서 앱은 실제 사물처럼 "무게감"과 "공간감"을 가져야 한다. **Liquid Glass** 디자인 언어를 적극 활용하여 그림자와 반사 효과를 통해 앱이 실제 공간에 떠 있는 것처럼 느끼게 하는 것이 핵심이다. 단순한 2D 창 띄우기는 사용자에게 몰입을 방해하는 '불청객'이 될 수 있다.

### 더 보기
- [apple-app-intents](../04_system_services/apple-app-intents.md) - 공간 상의 기능 실행
- [apple-swiftui-deep-dive](../02_ui_frameworks/apple-swiftui-deep-dive.md) - Liquid Glass 디자인 구현
- [apple-intelligence-and-agentic-intents](../04_system_services/apple-intelligence-and-agentic-intents.md) - Siri 공간 명령 처리
