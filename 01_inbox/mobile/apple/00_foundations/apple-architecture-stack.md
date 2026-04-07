---
title: apple-architecture-stack
tags: []
aliases: []
date modified: 2026-04-07 18:53:39 +09:00
date created: 2026-04-03 22:15:19 +09:00
---

## [[mobile-security]] > [[apple-architecture-stack]]

### Apple System Architecture & Kernel Internals

Apple 운영체제의 하부 구조인 **Darwin**과 **XNU 커널**의 아키텍처를 심층 분석합니다. 주요 기술 용어 정의는 [[apple-glossary]] 를 참고하시기 바랍니다.

#### 💡 Context: XNU (Hybrid Kernel)

XNU("X is Not Unix")는 **Mach 마이크로커널**의 유연성과 **BSD**의 실용성을 결합한 하이브리드 커널입니다.

- **Mach Layer**: 커널의 핵심으로 스레드 스케줄링, 가상 메모리 관리, 그리고 프로세스 간 통신인 **Mach Message**를 담당합니다.
- **BSD Layer**: Mach 위에서 POSIX 호환성을 제공하며, 파일 시스템(VFS), 네트워킹 스택, 그리고 유닉스 스타일의 프로세스/권한 모델을 관리합니다.
- **I/O Kit**: 객체 지향 기반의 디바이스 드라이버 프레임워크로, 하드웨어 제어와 효율적인 전원 관리를 수행합니다.

#### 🚀 시스템 부팅 및 앱 실행 시퀀스

1. **Secure Boot**: Boot ROM 에서 시작하여 iBoot 를 거쳐 커널의 서명을 검증하고 로드합니다. (Chain of Trust)
2. **Launchd (PID 1)**: 커널이 띄우는 첫 번째 유저 프로세스로, 모든 시스템 데몬과 앱의 조상입니다.
3. **App Launch (SpringBoard)**: 사용자가 앱을 탭하면 `launchd` 가 프로세스를 생성하고 동적 링커 `dyld` 가 필요한 라이브러리를 바인딩합니다.
4. **Shared Cache**: 모든 앱이 공통으로 사용하는 시스템 프레임워크를 공유 메모리에 매핑하여 실행 속도를 비약적으로 높입니다.

#### 🛡️ 보안 아키텍처 (Security Layers)

Apple 은 커널 레벨에서 다중 방어 체계를 구축하고 있습니다.

- **AMFI (Apple Mobile File Integrity)**: 실행되는 모든 바이너리의 코드 서명과 **Entitlements**(권한 명세)를 강제로 검사합니다.
- **Sandbox (Seatbelt)**: 앱이 접근할 수 있는 파일 시스템 경로와 네트워크 자원을 엄격히 격리합니다.
- **TCC (Transparency, Consent, and Control)**: 카메라, 마이크 등 민감한 데이터 접근 시 사용자의 명시적 허가를 `tccd` 데몬이 관리합니다.
- **Private Cloud Compute (PCC)**: 2024 년 이후 도입된 AI 프라이버시 계층으로, Apple Intelligence 의 원격 처리를 로컬 기기와 동일한 수준의 데이터 안전성을 보장하며 수행합니다.

#### 🧱 플랫폼별 아키텍처 특징 비교

| 특징            | macOS                         | iOS / iPadOS / visionOS           |
| :------------ | :---------------------------- | :-------------------------------- |
| **파일 시스템**    | 사용자 접근이 자유로운 편 (Finder)       | 철저한 샌드박스 및 컨테이너 격리                |
| **메모리(Swap)** | 디스크 스왑 사용 (Compressor + Swap) | **Swap 없음** (Compressor + Jetsam) |
| **앱 생명주기**    | 사용자 명시적 종료 전까지 유지             | 백그라운드 전환 시 적극적 Suspend/Terminate  |

#### 📚 연관 문서 및 심화 학습

- [[apple-foundations]] - Apple 플랫폼 공통 철학 및 기초
- [[apple-boot-flow-and-images]] - 전원 버튼부터 앱 실행까지의 상세 흐름
- [[apple-runtime-and-swift]] - Objective-C 및 Swift 런타임의 내부 구조
- [[apple-sandbox-and-security]] - 샌드박스 매커니즘과 보안 진단
- [[apple-interprocess-and-xpc]] - 프로세스 간 통신(XPC) 아키텍처
- [[apple-memory-management]] - Jetsam 과 메모리 최적화 전략
