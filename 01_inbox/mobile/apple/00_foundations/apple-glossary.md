---
title: apple-glossary
tags: []
aliases: []
date modified: 2026-04-06 17:51:13 +09:00
date created: 2026-04-03 22:15:19 +09:00
---

## [[mobile-security]] > [[apple-glossary]]

### Apple Developer Glossary: Key Terms & Concepts

Apple 생태계의 문서를 읽을 때 마주하게 되는 핵심 기술 용어들의 맥락(Context)을 설명합니다. 이 용어들을 명확히 이해하면 시스템 로그와 에러 메시지의 근본 원인을 파악하는 데 큰 도움이 됩니다.

---

#### 🏗️ Architecture & Kernel (기반 시스템)

- **Darwin**: macOS, iOS 등 모든 Apple OS 의 뿌리가 되는 오픈소스 유닉스 운영체제입니다.
- **XNU (X is Not Unix)**: Darwin 의 커널로, Mach 마이크로커널과 BSD 의 하이브리드 구조입니다. ([[apple-architecture-stack]])
- **Sandbox**: 앱을 격리하는 보안 울타리로, 자신의 컨테이너 외부 파일 접근을 차단합니다. ([[apple-sandbox-and-security]])
- **Daemon (데몬)**: 백그라운드에서 실행되는 시스템 서비스로, 이름 끝에 `d` 가 붙습니다. (예: `locationd`, `tccd`)

---

#### 📦 App Structure (앱 구조)

- **Bundle (번들)**: 코드, 리소스, 서명 등이 포함된 디렉토리 패키지(`.app`)입니다.
- **Info.plist**: 앱의 구성 정보와 권한 요청 문구 등이 포함된 설정 파일입니다.
- **Entitlement**: 앱이 수행할 수 있는 특정 권한(iCloud, Push 등)의 명세이며 코드 서명에 포함됩니다.

---

#### 🎨 UI & Execution (실행 및 화면)

- **Main Run Loop**: 터치 이벤트 처리와 UI 렌더링을 담당하는 메인 스레드의 무한 루프입니다.
- **GCD (Grand Central Dispatch)**: 시스템이 스레드를 자동으로 관리하며 작업을 분산 처리하는 기술입니다. ([[apple-gcd-deep-dive]])
- **dyld (Dynamic Link Editor)**: 앱 실행 시 필요한 라이브러리를 동적으로 연결하는 로더입니다. ([[apple-boot-flow-and-images]])

---

#### 🔐 Security & Privacy (보안 및 프라이버시)

- **Keychain**: 암호화된 시스템 데이터베이스로 비밀번호 등 민감 정보를 안전하게 저장합니다. ([[apple-keychain-biometrics]])
- **TCC (Transparency, Consent, and Control)**: 사용자의 개인 데이터 접근 권한을 관리하는 시스템입니다. ([[apple-privacy-and-tcc-details]])
- **Code Signing**: 앱의 무결성을 검증하고 개발자를 식별하기 위한 필수 서명 절차입니다.

---

#### 🛠️ Development Tools (개발 도구)

- **Instruments**: 성능 분석, 메모리 누수 진단 등을 수행하는 종합 프로파일링 도구입니다. ([[apple-instruments-profiling]])
- **TestFlight**: 정식 배포 전 베타 테스터에게 앱을 배포하고 피드백을 받는 공식 플랫폼입니다.

---

#### 🔗 관련 문서
- [[apple-foundations]] - Apple 플랫폼 공통 철학
- [[apple-architecture-stack]] - 시스템 계층 구조 및 커널 상세
- [[apple-history-and-evolution]] - 플랫폼의 변화 과정
- [[mobile-security]] - 모바일 보안 통합 가이드
