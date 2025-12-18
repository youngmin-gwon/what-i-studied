---
title: apple-foundations
tags: [apple, fundamentals, ios, ipados, macos, visionos, watchos]
aliases: []
date modified: 2025-12-17 17:00:00 +09:00
date created: 2025-12-16 16:07:21 +09:00
---

## Apple Platforms Foundations

iOS, macOS, visionOS 등 모든 Apple 플랫폼을 관통하는 **공통 철학**과 **시스템 기반 지식**입니다.
이 문서는 특정 API(UIKit, SwiftUI) 사용법보다는, **"Apple 생태계에서 앱이 돌아가는 근본 원리"**를 이해하는 데 초점을 맞춥니다.

### 💡 왜 이것을 알아야 하나요? (Why it matters)
- **버그의 원인**: "권한 오류", "샌드박스 위반", "메인 스레드 멈춤" 등의 문제는 대부분 이 기초 원리를 벗어났을 때 발생합니다.
- **크로스 플랫폼 설계**: iOS 앱을 macOS나 visionOS로 확장할 때, 무엇이 공통점이고 차이점인지 알면 코드 재사용률을 높일 수 있습니다.
- **성능 최적화**: 런타임이 어떻게 로딩되고 메모리가 어떻게 관리되는지 이해해야 "진짜 최적화"를 할 수 있습니다.

---

### 🍏 공통 디자인 철학 (Common Philosophy)

Apple 플랫폼은 **하드웨어와 소프트웨어의 통합**을 전제로 설계되었습니다.

1. **보안이 최우선 (Security First)**:
   - 모든 코드는 **서명(Code Signing)**되어야 실행됩니다.
   - 모든 앱은 **샌드박스(Sandbox)**라는 격리된 공간에서 돕니다. 옆집 앱의 데이터를 훔쳐볼 수 없습니다.
   - 사용자의 민감한 정보(위치, 사진 등)는 **TCC(투명성 및 동의)** 시스템을 통해 사용자가 매번 허락해야만 접근 가능합니다.

2. **반응성 (Responsiveness)**:
   - **메인 스레드(Main Thread)**는 오직 UI 렌더링만을 위해 존재해야 합니다.
   - 시스템은 배터리 수명을 위해 백그라운드 작업을 엄격하게 제한하거나 죽입니다(Jetsam).

3. **통합된 개발 환경**:
   - 언어: **Swift** (현대적, 안전함) 및 Objective-C (레거시, 런타임).
   - UI: **SwiftUI** (선언형, 멀티플랫폼) 및 UIKit/AppKit (네이티브).
   - 도구: Xcode 하나로 모든 플랫폼 개발 가능.

---

### 🏗️ 시스템 계층 구조 (Architecture Stack)

앱 개발자가 바라보는 시스템은 다음과 같이 층층이 쌓여 있습니다. 아래로 갈수록 기계와 가깝고 다루기 어렵지만 강력합니다.

| 계층 (Layer) | 주요 구성요소 | 역할 |
|---|---|---|
| **App & Extensions** | Your App, Widget, Share Extension | 여러분이 만드는 결과물. `.app` 번들 형태. |
| **User Experience** | SwiftUI, UIKit, AppKit | 화면을 그리고 이벤트를 받는 최상위 프레임워크. |
| **System Frameworks** | Foundation, AVFoundation, Core Data | 파일, 네트워크, 미디어 등 핵심 기능. |
| **System Services** | `launchd`, `SpringBoard`, `backboardd` | 앱을 실행하고 관리하는 시스템 데몬들. |
| **Kernel (Darwin)** | **XNU**, Mach, BSD, Drivers | 하드웨어 제어, 메모리 관리, 프로세스 스케줄링. |

👉 **Deep Dive**: 더 자세한 커널 구조는 [apple-architecture-stack](apple-architecture-stack.md)에서 다룹니다.

---

### 📦 앱의 실행 환경 (Execution Environment)

앱 아이콘을 누르면 무슨 일이 일어날까요?

1. **Entrypoint**: C언어의 `main` 함수에서 시작하여, Swift 런타임을 초기화하고 **Run Loop**를 돕니다.
2. **Bundle**: 앱은 단순한 파일이 아니라, 코드(실행 파일), 리소스(이미지), 설정(Info.plist)이 담긴 디렉토리 패키지입니다.
3. **Container**: 앱은 자신만의 디렉토리(`Documents`, `Library`, `tmp`)를 부여받습니다. 이 밖의 파일(예: 사용자 사진첩)에는 마음대로 접근할 수 없습니다.

---

### 🛤️ 학습 로드맵 (Roadmap)

이 폴더의 문서들은 다음 순서로 읽으면 좋습니다:

1. **기반 다지기**:
   - [apple-architecture-stack](apple-architecture-stack.md): XNU 커널과 Darwin의 이해
   - [apple-runtime-and-swift](apple-runtime-and-swift.md): Swift 언어가 돌아가는 원리
   - [apple-boot-flow-and-images](apple-boot-flow-and-images.md): 전원 버튼부터 앱 실행까지

2. **보안과 시스템**:
   - [apple-sandbox-and-security](../05_security_privacy/apple-sandbox-and-security.md): 왜 내 파일에 접근 못 할까?
   - [apple-interprocess-and-xpc](../04_system_services/apple-interprocess-and-xpc.md): 앱과 위젯은 어떻게 대화할까?

3. **플랫폼별 특징**:
   - [apple-platform-differences](apple-platform-differences.md): iOS vs macOS 차이점 정복

---

### 📚 더 보기
- 용어가 헷갈린다면? 👉 [apple-glossary](apple-glossary.md)
