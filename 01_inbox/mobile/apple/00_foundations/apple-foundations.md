---
title: apple-foundations
tags: [apple, apple/foundations, map, moc]
aliases: ["Apple Foundation Map", "Apple Foundations", "Apple 플랫폼 기초", "Apple 플랫폼의 기본값은 코드 서명·샌드박스·적극적 자원 회수이며 앱 설계는 그 위에서 시작한다"]
date modified: 2026-09-03 11:59:29 +09:00
date created: 2026-04-03 22:15:19 +09:00
---

## Apple 플랫폼의 기본값은 코드 서명·샌드박스·적극적 자원 회수이며 앱 설계는 그 위에서 시작한다

이 폴더는 개별 API 사용법이 아니라 **Apple 플랫폼 전체의 지도**를 제공하는 입구다. 먼저 세 가지 기본값을 잡고, 문제 유형별로 정본 영역이나 진단 런북으로 이동한다.

- **모든 코드는 서명된다.** 서명되지 않았거나 서명이 깨지면 실행 자체가 불가능하다.
- **모든 앱은 격리된다.** 컨테이너 밖의 것은 명시적 허가 없이는 보이지 않는다.
- **자원은 언제든 회수된다.** 앱은 정지되고 종료되는 것이 정상이며, 그것을 전제로 설계해야 한다.

### 읽는 순서

1. [apple-architecture-stack](apple-architecture-stack.md) 에서 커널부터 앱까지의 책임 계층을 구분한다.
2. [apple-system-internals-map](../01_system_internals/apple-system-internals-map.md) 에서 그 계층이 실제로 무엇을 소유하고 강제하는지 본다.
3. 지금 겪는 문제가 있으면 아래 **진단 런북**으로 바로 간다.
4. 전체 흐름을 익히려면 아래 **Worked Examples** 를 순서대로 읽는다.
5. 낯선 약어는 [apple-glossary](apple-glossary.md) 에서 뜻만 확인하고 연결된 정본으로 이동한다.

### 정본 영역

| 영역 | 다루는 범위 |
| :--- | :--- |
| [01_system_internals](../01_system_internals/apple-system-internals-map.md) | 부팅·IPC·커널·그래픽·저장소·네트워크의 플랫폼 내부 |
| [01_language_concurrency](../01_language_concurrency/apple-swift-concurrency.md) | Swift 런타임, ARC, 동시성 모델 |
| [02_ui_frameworks](../02_ui_frameworks/apple-swiftui-deep-dive.md) | SwiftUI, UIKit, 렌더링, 위젯, 접근성 |
| [03_data_networking](../03_data_networking/apple-networking-and-cloud.md) | 영속화, 네트워킹, 동기화 |
| [04_system_services](../04_system_services/apple-system-services.md) | 백그라운드, 알림, 위치, 인텐트 |
| [05_security_privacy](../05_security_privacy/mobile-apple-foundation-security.md) | 샌드박스, TCC, Keychain, 무결성 |
| [06_testing_performance](../06_testing_performance/apple-performance-and-debug.md) | 테스트, 프로파일링, 품질 지표 |
| [07_platforms](../07_platforms/apple-cross-platform-architecture.md) | iOS/iPadOS/macOS/watchOS/tvOS/visionOS |
| [08_packaging_deployment](../08_packaging_deployment/apple-packaging-deployment-map.md) | SPM, 서명, 배포, 심사 |

### 진단 런북 (증상에서 시작한다)

| 증상 | 런북 |
| :--- | :--- |
| 앱 시작이 느리거나 실행되지 않는다 | [01-app-launch-slow-or-fails](diagnostic-runbooks/01-app-launch-slow-or-fails.md) |
| 앱이 멈추거나 워치독으로 종료된다 | [02-watchdog-and-hang](diagnostic-runbooks/02-watchdog-and-hang.md) |
| 메모리 때문에 종료된다 | [03-jetsam-memory-termination](diagnostic-runbooks/03-jetsam-memory-termination.md) |
| 권한을 받았는데 API 가 실패한다 | [04-permission-granted-but-api-fails](diagnostic-runbooks/04-permission-granted-but-api-fails.md) |
| 백그라운드 작업이 실행되지 않는다 | [05-background-work-not-running](diagnostic-runbooks/05-background-work-not-running.md) |
| 푸시 알림이 오지 않는다 | [06-push-notification-missing](diagnostic-runbooks/06-push-notification-missing.md) |
| 스크롤이나 애니메이션이 끊긴다 | [07-scroll-hitches](diagnostic-runbooks/07-scroll-hitches.md) |
| 서명·프로비저닝·배포가 실패한다 | [08-signing-and-distribution-failure](diagnostic-runbooks/08-signing-and-distribution-failure.md) |

### Worked Examples (전체 경로를 끝까지 따라간다)

1. [아이콘 탭에서 첫 프레임까지](worked-examples/01-icon-tap-to-first-frame.md)
2. [사진 촬영에서 업로드까지](worked-examples/02-photo-capture-to-upload.md)
3. [유니버설 링크에서 올바른 화면 상태까지](worked-examples/03-universal-link-to-scene-restore.md)
4. [APNs 에서 알림 표시와 탭 처리까지](worked-examples/04-apns-to-notification-display-and-tap.md)
5. [종료 후 편집 상태 복원](worked-examples/05-termination-recovery-of-edit-state.md)
6. [세 개의 권한 게이트를 순서대로 통과시키기](worked-examples/06-permission-gates-in-sequence.md)
7. [SwiftUI 상태 변경에서 픽셀까지](worked-examples/07-swiftui-state-change-to-pixel.md)
8. [아카이브에서 TestFlight 배포와 업데이트까지](worked-examples/08-archive-to-testflight-to-update.md)

### 문제 분류

- **앱이 예고 없이 사라진다**: 원인이 네 가지(assertion 만료 / Jetsam / 워치독 / 사용자 강제 종료)다. [apple-ipc-and-process](../01_system_internals/ipc-and-process/apple-ipc-and-process.md) 의 진단 순서로 먼저 나눈다.
- **권한은 받았는데 실패한다**: entitlement · sandbox · TCC 세 게이트를 분리한다. [04 런북](diagnostic-runbooks/04-permission-granted-but-api-fails.md)
- **기기나 OS 버전에 따라 다르게 동작한다**: [apple-platform-differences](apple-platform-differences.md) 와 [apple-history-and-evolution](apple-history-and-evolution.md) 에서 버전 축과 플랫폼 축을 따로 확인한다.
- **성능이 특정 기기에서만 나쁘다**: 가변 주사율과 메모리 한도가 기기별로 다르다. [07 런북](diagnostic-runbooks/07-scroll-hitches.md), [03 런북](diagnostic-runbooks/03-jetsam-memory-termination.md)

### 경계

이 폴더에는 여러 영역을 잇는 **지도와 진단 기준**만 둔다. 특정 API 사용법, 구현 레시피, 서브시스템 내부 동작은 해당 정본 영역에 둔다.

### 관련 문서

- [apple-glossary](apple-glossary.md) - 용어의 짧은 정의와 정본 링크
- [apple-architecture-stack](apple-architecture-stack.md) - 시스템 계층 구조와 커널
- [apple-history-and-evolution](apple-history-and-evolution.md) - 플랫폼의 변화 과정
- [apple-platform-differences](apple-platform-differences.md) - 플랫폼 간 차이와 코드 공유
- [apple-runtime-and-swift](apple-runtime-and-swift.md) - 런타임과 dispatch
- [android-foundation-map](../../android/00_foundations/android-foundation-map.md) - 안드로이드 대응 지도
- [mobile-security](../../mobile-security.md) - 모바일 보안 통합 허브
- [apple-system-internals-map](../01_system_internals/apple-system-internals-map.md) - API 뒤에서 실제로 실행되는 6 개 플랫폼 계층
