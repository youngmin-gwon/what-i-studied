---
title: apple-history-and-evolution
tags: [apple, history]
aliases: []
date modified: 2025-12-16 16:15:28 +09:00
date created: 2025-12-16 16:11:27 +09:00
---

## History & Evolution apple history

애플 플랫폼이 어떻게 변해왔는지 큰 흐름을 요약했다. 용어는 [[apple-glossary]].

### 커널/보안
- 초기 OS X 는 Mach/BSD 기반 XNU 커널 도입 → iPhone OS 에서도 재사용.
- Code Signing/Entitlement 강화, SIP/SSV/AMFI 로 루트 조작 방지.
- kext 에서 DriverKit(유저 공간) 으로 전환 추세.

### 언어/런타임
- Objective-C 중심 → Swift 등장 (2014) → Swift Concurrency(2021) 로 안전성/성능 개선.
- Swift ABI 안정화로 XCFramework/배포가 쉬워졌다.

### UI
- UIKit(멀티터치) → Auto Layout/Size Class → SwiftUI(2019) 선언형 UI.
- iPadOS 멀티 윈도우/Stage Manager, macOS Catalyst/SwiftUI 로 코드 공유 증가.
- visionOS 는 공간 UI(윈도우/볼륨/풀 스페이스) 로 확장.

### 하드웨어/칩
- Intel 맥 → Apple Silicon(M1~) 전환, [[apple-glossary#Rosetta|Rosetta2]] 로 이행.
- Neural Engine, UWB, LiDAR, ProMotion, Always-on 디스플레이 등 센서/가속기 추가.

### 그래픽/미디어
- OpenGL → Metal 로 전환, ProRes/ProRAW 지원, Spatial Audio/ARKit/RealityKit 확장.

### 네트워크/클라우드
- ATS 기본화, QUIC/HTTP3 지원, iCloud/CloudKit 확장.
- APNs 개선, PushKit 제한 강화 (VoIP 남용 방지).

### 배포/정책
- App Store 심사 기준 강화, 개인정보 라벨/ATT 도입.
- TestFlight 확대, notarization 요구 (macOS) 확립.

### 플랫폼 별 이정표 (간단)
- iPhone OS 1: 멀티터치, 앱 스토어는 2 에서 도입.
- iOS 7: 플랫 디자인, AirDrop, 백그라운드 fetch.
- iOS 13: 다크 모드, SwiftUI, 멀티 윈도우 (Scene).
- iPadOS 분리: 멀티태스킹 강화, Stage Manager(16).
- watchOS: 컴플리케이션/헬스, 독립 앱 (6), SwiftUI 기본 (7).
- macOS: Gatekeeper/노타리제이션, Apple Silicon 지원 (Big Sur), SSV(11).
- visionOS 1: 공간 윈도우/볼륨, 패스스루, SwiftUI/RealityKit 우선.

### 링크

[[apple-architecture-stack]], [[apple-build-and-distribution]], [[apple-platform-differences]].
