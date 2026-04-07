---
title: apple-foundations
tags: []
aliases: []
date modified: 2026-04-07 15:21:20 +09:00
date created: 2026-04-03 22:15:19 +09:00
---

## [[mobile-security]] > [[apple-foundations]]

### Apple Platforms Foundations: Core Philosophies

iOS, macOS, visionOS 등 모든 Apple 플랫폼을 관통하는 **공통 철학**과 **시스템 기반 지식**을 다룹니다. 특정 프레임워크(UIKit, SwiftUI)의 사용법보다는, 앱이 Apple 생태계에서 안전하고 효율적으로 구동되는 근본 원리에 초점을 맞춥니다.

---

#### 💡 Why it matters (Context)

Apple 플랫폼은 하드웨어와 소프트웨어의 긴밀한 통합을 통해 사용자 경험을 극대화합니다. 엔지니어로서 이 기초를 이해하는 것은 다음과 같은 이유로 중요합니다.

- **Security by Default**: 모든 앱은 **Code Signing**(서명)이 필수이며, 격리된 **Sandbox** 환경에서 실행됩니다.
- **System Responsiveness**: 배터리 효율과 사용자 반응성을 위해 시스템은 백그라운드 작업을 엄격히 제한하며, 필요시 프로세스를 즉시 종료(Jetsam)합니다.
- **Unified Versioning**: 2025 년 대규모 업데이트를 통해 모든 Apple OS 버전이 출시 연도에 맞춰 **iOS 26** 등으로 통합되었습니다. 이제 모든 플랫폼이 동일한 메인 버전 번호를 공유합니다.

---

#### 🏗️ 시스템 아키텍처 계층 (Architecture Stack)

Apple 의 시스템은 커널부터 앱 레이어까지 견고하게 쌓여 있습니다.

- **App & Extensions**: `.app` 번들 형태의 결과물과 위젯 등 확장 프로그램.
- **Cocoa / Cocoa Touch**: SwiftUI, UIKit 등 화면을 구성하고 이벤트를 처리하는 최상위 프레임워크.
- **Media / Core Services**: Foundation, AVFoundation, Core Data 등 핵심 기능 Layer.
- **Core OS / Kernel**: **XNU**(Mach + BSD) 커널 기반의 하드웨어 제어 및 리소스 스케줄링.

---

#### 📦 앱의 실행 환경 (Execution Environment)

- **Entrypoint**: `@main` 어트리뷰트가 붙은 진입점을 통해 Swift 런타임이 초기화되고 **Run Loop**가 시작됩니다.
- **App Bundle**: 코드, 리소스, `Info.plist` 가 포함된 패키지 구조입니다.
- **Resource Sandbox**: 앱은 자신만의 고유한 디렉토리 컨테이너를 가집니다. 사진첩이나 연락처 등 공용 자원 접근에는 사용자의 명시적 동의(TCC)가 필요합니다.

---

#### 📚 추천 학습 경로 (Learning Path)

Apple 시스템의 심층적인 이해를 위해 다음 순서로 학습하는 것을 권장합니다.

1. **플랫폼 기초**: [[apple-architecture-stack]] → [[apple-foundations]]
2. **런타임 및 부팅**: [[apple-runtime-and-swift]] → [[apple-boot-flow-and-images]]
3. **보안 및 통신**: [[apple-sandbox-and-security]] → [[apple-interprocess-and-xpc]]
4. **실전 대응**: [[apple-platform-differences]] → [[apple-performance-and-debug]]

---

#### 🔗 관련 문서
- [[apple-glossary]] - Apple 기술 용어 사전
- [[apple-history-and-evolution]] - 플랫폼의 역사와 주요 변화
- [[mobile-security]] - 모바일 보안 통합 허브
