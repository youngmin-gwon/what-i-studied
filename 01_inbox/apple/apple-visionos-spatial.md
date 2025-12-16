---
title: apple-visionos-spatial
tags: [apple, spatial, visionos]
aliases: []
date modified: 2025-12-16 16:15:50 +09:00
date created: 2025-12-16 16:13:38 +09:00
---

## visionOS & Spatial Computing apple visionos spatial

visionOS 에서 앱을 만들 때 알아야 할 기초를 쉽게 적었다. 용어는 [[apple-glossary]].

### 공간 UI 개념
- 창 (Window): 평면 UI. SwiftUI 로 작성, 공간 안에 배치된다.
- 볼륨 (Volume): 3D 콘텐츠를 담은 박스. RealityKit/SceneKit 으로 만든다.
- 풀 스페이스: 사용자 시야 전체를 차지하는 경험 (몰입). 패스스루/가상 환경을 선택.

### 입력
- 시선: 사용자가 보는 곳을 포커스로 삼는다.
- 손 제스처: 집기/탭/핀치. 기본 제스처를 사용하면 시스템이 자연스러운 입력을 제공.
- 음성: 마이크로 Siri/Dictation. 키보드 입력도 가능하지만 주 입력은 아니다.

### 렌더링
- 패스스루: 카메라를 통해 본 현실을 렌더링. 안전/프라이버시 때문에 앱은 원본 영상을 직접 받지 않는다.
- RealityKit/Metal: 3D/AR 콘텐츠. 라이트/머티리얼/피직스를 설정.
- 공간 오디오: 사용자의 머리/귀 위치에 맞춰 소리를 배치.

### UI 빌딩
- SwiftUI 가 기본. ImmersiveSpace/WindowGroup/VolumeGroup 을 선언해 공간 배치를 지정.
- Focus/Hit Testing 은 시선과 손 제스처를 통해 자동 처리. 너무 작은 터치 타깃은 피한다.
- 텍스트/컨트롤은 시스템 스타일을 사용해 가독성/거리/투명도를 자동 조정한다.

### 접근성
- VoiceOver, 손 제스처 보조, 자막/오디오 설명, 색상 대비 등 기존 접근성 기능이 확장된다.
- 시선 추적 민감도/프라이버시 설정을 존중한다.

### 성능/제약
- 3D/패스스루 합성으로 GPU 예산이 크다. 드로우콜/폴리곤/텍스처 최적화 필수.
- 저해상도 프리패스 (Perceptual foveation) 로 렌더링 비용을 줄인다.
- 백그라운드 실행 시간은 제한적. Live Activity/알림/단순 위젯은 평면 창으로.

### 보안/프라이버시
- 카메라/마이크/센서 데이터는 시스템이 관리하며, 앱은 필요 최소한만 받는다.
- 공간 맵/메시 데이터 접근은 제한적이며, 사용자 동의가 필요.

### 디버깅
- 시뮬레이터에서 3D 공간 배치 미리 보기, 실제 기기에서 패스스루/입력 확인.
- Reality Composer Pro 로 자산을 만들어 프리뷰.
- Instruments(금속, 타임 프로파일러), GPU Frame Capture 로 성능 점검.

### 링크

[[apple-platform-differences]], [[apple-rendering-and-media]], [[apple-performance-and-debug]], [[apple-accessibility-and-internationalization]].
