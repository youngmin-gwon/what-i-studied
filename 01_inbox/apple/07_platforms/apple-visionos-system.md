---
title: apple-visionos-system
tags: [apple, visionos, spatial, immersive, privacy, mrr]
aliases: []
date modified: 2025-12-18 00:00:00 +09:00
date created: 2025-12-18 00:00:00 +09:00
---

## visionOS System Internals

Spatial Computing은 화면의 크기 제한을 없앴지만, 새로운 책임(Privacy, Multi-tasking in 3D)을 부여했습니다.
아이폰 앱을 그대로 실행할 수 있다고 해서 방심하면 안 됩니다. visionOS는 **시선(Eye)**이 곧 마우스 커서인 세상입니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **Eye Tracking Privacy**: "사용자가 어디를 보고 있는지 데이터를 달라"는 요청은 불가능합니다. Apple은 시선 데이터를 1프레임도 앱에 넘겨주지 않습니다. 이 제약을 이해해야 UI를 설계할 수 있습니다.
- **Shared Space vs Full Space**: 내 앱이 거실에 다른 앱들과 같이 떠 있을지(Shared), 아니면 사용자의 방 전체를 장악할지(Full) 결정해야 합니다. 이 둘은 렌더링 파이프라인이 다릅니다.
- **Volumes**: 2D 윈도우가 아니라, 3D 객체(예: 농구공)를 띄우려면 Window 대신 Volume을 써야 합니다.

---

### 👁️ Privacy & Input Model

가장 중요한 차이점입니다. 시스템은 **사용자가 무엇을 보는지 앱이 모르게** 합니다.

1. **Hover Effect (System Level)**: 사용자가 버튼을 쳐다보면 버튼이 밝아집니다. 이건 **iOS(System)**가 처리합니다. 앱은 아직 모릅니다.
2. **Tap (Pinch)**: 사용자가 손가락을 꼬집는 순간, 그제서야 앱은 "이 버튼이 눌렸다"는 이벤트를 받습니다.
3. **Implication**: "사용자가 광고를 3초 동안 쳐다봤으니 과금" 같은 로직은 구현 불가능합니다.

---

### 🌌 Spaces & Rendering

#### 1. Shared Space (기본값)
여러 앱이 동시에 떠 있는 상태입니다. (마이너리티 리포트처럼)
- **RealityKit**: 시스템이 제공하는 렌더러를 써야 합니다. 그래야 다른 앱과 조명(Lighting), 그림자(Shadow)를 공유하며 자연스럽게 어우러집니다.

#### 2. Full Space (Immersive Space)
내 앱만 존재하는 상태입니다. (VR 게임처럼)
- **Compositor Services**: Metal을 직접 써서 렌더링할 수 있습니다. (Custom Rendering)
- **ARKit Hand Tracking**: 이때는 사용자의 손 골격(Skeletal Data) 정보를 받을 수 있습니다. (Shared Space에서는 보안상 불가)

---

### 📦 SwiftUI & Architecture

visionOS 앱의 90%는 SwiftUI로 만듭니다.

- **WindowGroup**: 2D 평면 윈도우. 깊이(Depth)를 줄 수 있지만 기본은 판판합니다.
- **Volumetric Window**: 3D 부피를 가진 큐브 형태. 사용자가 걸어 다니며 360도로 볼 수 있습니다.
- **Ornaments**: 윈도우 밖으로 튀어나온 툴바/탭바. 시선을 따라다니지 않고 윈도우에 붙어 있습니다. (Floating UI)

### 더 보기
- [[apple-rendering-and-media]] - Metal 렌더링 파이프라인
- [[apple-ipados-multitasking]] - 멀티 윈도우 관리 (비슷한 개념)
