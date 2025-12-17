---
title: apple-platform-differences
tags: [apple, platforms]
aliases: []
date modified: 2025-12-16 16:15:45 +09:00
date created: 2025-12-16 16:11:10 +09:00
---

## Platform Differences apple platforms

iOS/iPadOS/macOS/watchOS/visionOS 차이를 한 곳에 모았다. 용어는 [[apple-glossary]].

### iOS
- 손가락/제스처 중심, 단일 창 (하지만 Scene 기반 멀티 윈도우 가능).
- 강한 샌드박스, 백그라운드 제한, [[apple-glossary#TCC|TCC]] 필수.
- SpringBoard/Backboardd 가 홈/입력을 관리.

### iPadOS
- iOS 특성 + 멀티 윈도우/[[Stage Manager]]/외장 디스플레이/포인터 지원.
- 키보드/펜 입력이 중요, Drag&Drop 가 빈번.

### macOS
- 데스크탑: AppKit, 메뉴바, 다중 창, 파일 시스템 접근이 넓다.
- SIP/노타리제이션/샌드박스 (TCC) 로 점차 잠가가는 중.
- [[apple-glossary#Window Server|WindowServer]] 가 창을 합성.

### watchOS
- 짧은 세션, 작은 화면. 에너지/메모리 예산이 가장 작다.
- Notification/Complication/Workout/HealthKit/Background Refresh 가 핵심.
- iPhone 과 페어링된 데이터 흐름 (WCSession) 이 중요.

### visionOS
- 공간 윈도우/볼륨/풀 스페이스. 손/시선/음성 입력.
- 패스스루 렌더링, RealityKit/Metal 중심. SwiftUI 가 기본 UI 도구.

### 공통
- [[apple-glossary#SwiftUI|SwiftUI]] 로 UI 를 공유할 수 있고, [[apple-glossary#Swift|Swift]] 코드가 대부분 재사용 가능.
- APNs/CloudKit/Keychain/ATS 등 보안·네트워크 모델은 비슷하다.
- 샌드박스/서명/Entitlement/TCC 가 기본 규칙이다.

### 링크

[[apple-app-lifecycle-and-ui]], [[apple-rendering-and-media]], [[apple-build-and-distribution]], [[apple-history-and-evolution]].
