---
title: apple-visionos-spatial
tags: [apple, realitykit, spatial, swiftui, visionos]
aliases: []
date modified: 2026-08-10 00:00:00 +09:00
date created: 2025-12-16 16:13:38 +09:00
---

## visionOS & Spatial Computing

**"공간 컴퓨팅(Spatial Computing)"** 이라는 새로운 패러다임이 열렸습니다.

visionOS 앱은 더 이상 사각 화면에 갇혀 있지 않습니다. 사용자의 방(Room) 자체가 캔버스이며, 앱은 공중에 떠 있는 물체가 됩니다.

### 💡 왜 이것을 알아야 하나요? (Context)

- **미래 준비**: 지금 당장 앱을 출시하지 않더라도, Apple 의 다음 10 년이 "공간"에 있다는 점을 이해해야 합니다.
- **기존 기술의 확장**: visionOS 는 완전히 새로운 것이 아니라, **SwiftUI + ARKit + RealityKit**의 융합체입니다. 기존 기술을 익혀두면 진입장벽이 낮아집니다.
- **UX 의 변화**: "클릭" 대신 "응시(Eye) + 탭(Tap)"을 사용합니다. 버튼이 너무 작으면 눈으로 조준하기 힘듭니다.

---

### 🥽 공간을 구성하는 3 요소 & 입력 시스템

visionOS의 기본 개념인 Window/Volume/Space와 입력 모델에 대한 자세한 설명은 [apple-visionos-system.md](../07_platforms/apple-visionos-system.md) 를 참고하세요.

---

### 🛠️ 개발 프레임워크

#### SwiftUI & RealityKit

- **SwiftUI**: 레이아웃, 버튼, 텍스트 등 2D 요소와 전반적인 앱 구조를 담당합니다.
- **RealityKit**: 3D 모델 렌더링, 물리 엔진, 파티클 효과, 조명 등을 담당합니다.
- **ARKit**: (Full Space 에서만) 사용자의 손 관절 위치, 방의 바닥/벽 인식(Plane Detection) 등 현실 세계 데이터를 제공합니다.

### 📚 더 보기

- [apple-visionos-system](../07_platforms/apple-visionos-system.md) - 기본 개념 (Window/Volume/Space, 입력모델)
- [apple-platform-differences](../00_foundations/apple-platform-differences.md) - 다른 플랫폼과의 차이점
- [apple-rendering-and-media](apple-rendering-and-media.md) - RealityKit 과 Metal 렌더링
