---
title: apple-visionos-spatial
tags: [apple, spatial, visionos, realitykit, swiftui]
aliases: []
date modified: 2025-12-17 19:50:00 +09:00
date created: 2025-12-16 16:13:38 +09:00
---

## visionOS & Spatial Computing

**"공간 컴퓨팅(Spatial Computing)"**이라는 새로운 패러다임이 열렸습니다.
visionOS 앱은 더 이상 사각 화면에 갇혀 있지 않습니다. 사용자의 방(Room) 자체가 캔버스이며, 앱은 공중에 떠 있는 물체가 됩니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **미래 준비**: 지금 당장 앱을 출시하지 않더라도, Apple의 다음 10년이 "공간"에 있다는 점을 이해해야 합니다.
- **기존 기술의 확장**: visionOS는 완전히 새로운 것이 아니라, **SwiftUI + ARKit + RealityKit**의 융합체입니다. 기존 기술을 익혀두면 진입장벽이 낮아집니다.
- **UX의 변화**: "클릭" 대신 "응시(Eye) + 탭(Tap)"을 사용합니다. 버튼이 너무 작으면 눈으로 조준하기 힘듭니다.

---

### 🥽 공간을 구성하는 3요소

#### 1. Window (평면)
기존 iOS/macOS 앱과 가장 유사합니다. 공간상에 2D 평면 창을 띄웁니다.
- **SwiftUI**: 기존 코드를 거의 그대로 사용할 수 있습니다.
- **Glass Material**: 배경이 불투명하지 않고, 뒤가 비치는 유리 재질(Glassmorphism)이 기본입니다. 조명에 따라 그림자와 반사가 자동으로 적용됩니다.

#### 2. Volume (입체)
3D 물체를 담는 제한된 크기의 상자(Box)입니다.
- 사용자가 이 상자를 집어서 책상 위에 올려두거나 돌려볼 수 있습니다.
- **RealityKit**을 사용하여 3D 모델(.usdz)을 렌더링합니다.

#### 3. Space (공간)
사용자의 시야 전체를 제어합니다.
- **Shared Space (기본)**: 여러 앱이 공중에 둥둥 떠서 공존합니다.
- **Full Space (몰입)**: 내 앱만 남고 다른 앱은 숨겨집니다. 방(Passthrough)을 보여줄 수도 있고, 완전히 가상 환경(VR)으로 덮을 수도 있습니다.

---

### 👁️ 입력 시스템: 눈과 손 (Eyes & Hands)

#### 1. Eye Tracking (포커스)
마우스 커서 대신 **눈**을 사용합니다.
- 사용자가 버튼을 쳐다보면 살짝 강조(Highlight)됩니다. 이를 **Focus**라고 합니다.
- **Privacy**: 앱은 "사용자가 어디를 보고 있는지" 알 수 없습니다. 사용자가 손가락을 탭(Click)하는 순간에만 "여기를 클릭했다"는 좌표가 전달됩니다.

#### 2. Indirect Pinch (간접 탭)
허공에 손을 뻗어 터치하지 않아도 됩니다.
- 무릎 위에 손을 편안히 두고, 엄지와 집게 손가락을 맞대면(Tap) 클릭으로 인식됩니다.
- 화면을 보고 -> 손가락을 맞대면 -> 클릭입니다.

#### 3. Direct Touch (직접 터치)
가상 키보드나 가까이 있는 물체는 손가락 끝으로 직접 누를 수 있습니다.

---

### 🛠️ 개발 프레임워크

#### SwiftUI & RealityKit
- **SwiftUI**: 레이아웃, 버튼, 텍스트 등 2D 요소와 전반적인 앱 구조를 담당합니다.
- **RealityKit**: 3D 모델 렌더링, 물리 엔진, 파티클 효과, 조명 등을 담당합니다.
- **ARKit**: (Full Space에서만) 사용자의 손 관절 위치, 방의 바닥/벽 인식(Plane Detection) 등 현실 세계 데이터를 제공합니다.

### 📚 더 보기
- [[apple-platform-differences]] - 다른 플랫폼과의 차이점
- [[apple-rendering-and-media]] - RealityKit과 Metal 렌더링
