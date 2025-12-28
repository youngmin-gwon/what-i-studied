---
title: components-spatial
tags: [apple, design-system, hig, immersive, spatial-computing, vision-pro, visionos, xr]
aliases: [visionOS Guidelines, Spatial UI, Windows and Volumes, Ornaments, Eye-Hand Interaction]
date modified: 2025-12-28 00:48:00 +09:00
date created: 2025-12-28 00:48:00 +09:00
---

## 🥽 Spatial Computing (공간 컴퓨팅): visionOS 의 설계 원칙

Apple Vision Pro 를 필두로 한 visionOS 는 화면의 제약을 벗어나, 앱이 실세계 공간(Infinite Canvas)에 공존하도록 설계되었습니다.

## 🖼️ Windows, Volumes, and Ornaments

### 1. Windows (윈도우)

- **형태**: 공간에 떠 있는 2D 평면 레이어입니다.
- **특징**: 사용자가 자유롭게 이동하고 크기를 조절할 수 있습니다. 시스템은 창의 거리에 따라 가독성을 유지하도록 지능적으로 스케일을 조정합니다.

### 2. Volumes (볼륨)

- **형태**: 3D 콘텐츠를 담는 경계 없는 상자입니다.
- **특징**: 사용자가 주위를 돌아다니며 모든 각도에서 객체(예: 3D 가구 모델)를 관찰할 수 있습니다.

### 3. Ornaments (오너먼트)

- **형태**: 윈도우나 볼륨 옆에 부착되어 떠 있는 보조 도구 모음.
- **디자인**: 윈도우 콘텐츠를 가리지 않으면서, 탭 바 나 툴바 같은 기능을 본체 가까이 제공합니다.

---

## 👁️ Interaction: Eye and Hand (시선과 손)

visionOS 는 별도의 컨트롤러 없이 가장 자연스러운 인체 동작을 인터페이스로 사용합니다.

### 1. Look and Tap (보고 누르기)

- **Eye Tracking**: 사용자가 특정 요소를 바라보는 것만으로 '호버(Hover)' 상태가 됩니다. 요소가 살짝 빛나거나 커지며 반응합니다.
- **Gesture**: 시선을 고정한 채로 검지와 엄지를 가볍게 맞대는(Pinch) 동작으로 선택을 확정합니다.

### 2. Hand Placements

- **Indirect Manipulation**: 손을 무릎 위에 편하게 둔 상태에서도 조작이 가능해야 합니다.
- **Direct Manipulation**: 가상 키보드 타이핑처럼 공중의 객체를 직접 손가락으로 건드리는 상호작용도 지원합니다.

---

## 🌌 Immersion (몰입감)

앱이 공간을 얼마나 차지하느냐에 따라 몰입 단계를 조절합니다.

- **Shared Space (공유 공간)**: 여러 앱이 실세계 배경(Passthrough) 위에 함께 떠 있는 기본 모드.
- **Full Space (전체 공간)**: 특정 앱이 시야를 완전히 장악하거나, 실세계 배경 주위에 복잡한 3D 월드를 구축하는 모드.

---

## 🧊 Visual Depth & Materials (공간의 질감)

- **Glass Material**: visionOS 의 기본 배경은 주변의 빛과 색을 투영하는 투명한 '유리' 재질입니다. 이는 앱이 사용자의 실제 방 안에 자연스럽게 스며들게 합니다.
- **Dynamic Lighting**: 창이나 객체의 그림자가 실제 바닥이나 가구 위에 드리워져 현실감을 더합니다.

---

## ♿ Accessibility (A11y)

- **Pointer Control**: 시선 추적이 어려운 사용자를 위해 머리 위치나 손목 움직임으로 포인터를 제어하는 대안을 제공합니다.
- **Dwell Control**: 손동작이 어려운 경우, 특정 요소를 일정 시간 바라보는 것만으로 클릭이 발생하게 설계할 수 있습니다.

---

## 🔗 관련 문서

- [[../hig_walkthrough|Apple HIG 개요]]
- [[../foundations/foundations-layout|Layout: 공간의 레이아웃]]
- [[../foundations/foundations-color-typography|Materials: Liquid Glass 와 물성]]
