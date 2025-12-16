---
title: apple-rendering-and-media
tags: [apple, graphics, media, metal]
aliases: []
date modified: 2025-12-16 16:15:46 +09:00
date created: 2025-12-16 16:09:09 +09:00
---

## Rendering & Media apple graphics metal media

화면/소리/카메라가 어떻게 처리되는지 쉽게 정리했다. 용어는 [[apple-glossary]].

### 그래픽 파이프라인
- 앱 (View/SwiftUI) 이 레이아웃을 만들고, Core Animation 이 레이어 트리를 관리한다.
- Metal/OpenGL(이전) 로 GPU 명령을 만들어 WindowServer(iOS 는 백보드/스프링보드 경유) 가 합성한다.
- ProMotion/Adaptive sync 로 디스플레이 주사율을 조정한다.

### SwiftUI vs UIKit/AppKit
- SwiftUI 는 선언형, diff 기반 업데이트. UIKit/AppKit 은 명령형 뷰 트리.
- 둘 다 Core Animation 레이어로 내려가므로 성능 도구는 비슷하게 쓴다.

### 입력과 렌더링 타이밍
- Run Loop 가 터치/제스처를 모아 한 프레임에 처리한다.
- Core Animation 이 vsync 에 맞춰 레이어를 커밋하고, GPU 가 렌더링한다.

### 카메라
- AVFoundation 의 AVCaptureSession/Device/Input/Output 구조.
- 권한은 Info.plist 의 NSCameraUsageDescription + TCC 팝업.
- 사진/비디오/라이브 포토/심도/ProRes/RAW 등 포맷 지원은 기기별로 다르다.

### 오디오
- AVAudioSession 으로 오디오 카테고리 (Playback/Record/PlayAndRecord/Ambient 등) 를 설정한다.
- AudioSession 이 중단 (전화/시리/다른 앱) 되면 알림을 받고 복구해야 한다.
- AudioUnit/AudioEngine 으로 저지연 오디오 처리. AirPlay/Handoff 지원은 세션 설정에 따라 달라진다.

### 비디오/DRM
- AVPlayer/AVQueuePlayer 로 재생. HLS 가 기본 스트리밍 포맷.
- FairPlay Streaming(FPS) 이 DRM 을 담당한다.

### 3D/AR/Spatial
- SceneKit/RealityKit/ARKit 로 3D·AR·Vision Pro 앱을 만든다.
- visionOS 는 공간 컴퓨팅 (창/볼륨/풀 스페이스) 렌더링을 RealityKit/Metal 로 한다.

### 디버깅/프로파일링
- Instruments: Core Animation, Game Performance, Metal System Trace, Time Profiler.
- `sudo log stream --process WindowServer`(macOS) 로 합성 문제 확인, iOS 는 sysdiagnose.
- GPU Frame Capture/Xcode Metal Debugger 로 셰이더/리소스 상태를 본다.

### 링크

[[apple-app-lifecycle-and-ui]], [[apple-performance-and-debug]], [[apple-platform-differences]], [[apple-visionos-spatial]].
