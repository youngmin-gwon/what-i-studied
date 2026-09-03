---
title: apple-glossary
tags: [apple, apple/foundations]
aliases: ["Apple Glossary", "Apple 용어 사전"]
date modified: 2026-09-03 11:59:30 +09:00
date created: 2026-04-03 22:15:19 +09:00
---

## Apple Glossary 는 용어의 짧은 정의와 정본 링크만 담는다

Apple 생태계의 문서를 읽을 때 마주하게 되는 핵심 기술 용어들의 맥락(Context)을 설명합니다. 이 용어들을 명확히 이해하면 시스템 로그와 에러 메시지의 근본 원인을 파악하는 데 큰 도움이 됩니다.

---

### 🏗️ Architecture & Kernel (기반 시스템)

- **Darwin**: macOS, iOS 등 모든 Apple OS 의 뿌리가 되는 오픈소스 유닉스 운영체제입니다.
- **XNU (X is Not Unix)**: Darwin 의 커널로, Mach 마이크로커널과 BSD 의 하이브리드 구조입니다. ([apple-architecture-stack](apple-architecture-stack.md))
- **Sandbox**: 앱을 격리하는 보안 울타리로, 자신의 컨테이너 외부 파일 접근을 차단합니다. ([apple-sandbox-and-security](../05_security_privacy/apple-sandbox-and-security.md))
- **Daemon (데몬)**: 백그라운드에서 실행되는 시스템 서비스로, 이름 끝에 `d` 가 붙습니다. (예: `locationd`, `tccd`)

---

### 📦 App Structure (앱 구조)

- **Bundle (번들)**: 코드, 리소스, 서명 등이 포함된 디렉토리 패키지(`.app`)입니다.
- **Info.plist**: 앱의 구성 정보와 권한 요청 문구 등이 포함된 설정 파일입니다.
- **Entitlement**: 앱이 수행할 수 있는 특정 권한(iCloud, Push 등)의 명세이며 코드 서명에 포함됩니다.

---

### 🎨 UI & Execution (실행 및 화면)

- **Main Run Loop**: 터치 이벤트 처리와 UI 렌더링을 담당하는 메인 스레드의 무한 루프입니다.
- **GCD (Grand Central Dispatch)**: 시스템이 스레드를 자동으로 관리하며 작업을 분산 처리하는 기술입니다. ([apple-gcd-deep-dive](../01_language_concurrency/apple-gcd-deep-dive.md))
- **dyld (Dynamic Link Editor)**: 앱 실행 시 필요한 라이브러리를 동적으로 연결하는 로더입니다. ([apple-boot-flow-and-images](apple-boot-flow-and-images.md))

---

### 🔐 Security & Privacy (보안 및 프라이버시)

- **Keychain**: 암호화된 시스템 데이터베이스로 비밀번호 등 민감 정보를 안전하게 저장합니다. ([apple-keychain-biometrics](../05_security_privacy/apple-keychain-biometrics.md))
- **TCC (Transparency, Consent, and Control)**: 사용자의 개인 데이터 접근 권한을 관리하는 시스템입니다. ([apple-privacy-and-tcc-details](../05_security_privacy/apple-privacy-and-tcc-details.md))
- **Code Signing**: 앱의 무결성을 검증하고 개발자를 식별하기 위한 필수 서명 절차입니다.

---

### 🛠️ Development Tools (개발 도구)

- **Instruments**: 성능 분석, 메모리 누수 진단 등을 수행하는 종합 프로파일링 도구입니다. ([apple-instruments-profiling](../06_testing_performance/apple-instruments-profiling.md))
- **TestFlight**: 정식 배포 전 베타 테스터에게 앱을 배포하고 피드백을 받는 공식 플랫폼입니다.

---

---

### ⚙️ 프로세스와 IPC

- **Mach port**: 커널이 소유한 메시지 큐이자 능력(capability). 가진 것 자체가 권한이다. ([mach-port-is-a-capability](../01_system_internals/ipc-and-process/mach-port-is-a-capability.md))
- **XPC**: Mach 메시지 위에 올린 프로세스 간 통신 추상. launchd 가 중개한다. ([xpc-connection-lifetime](../01_system_internals/ipc-and-process/xpc-connection-lifetime.md))
- **launchd**: PID 1. 모든 프로세스의 조상이며 선언에 따라 데몬을 온디맨드로 띄운다. ([launchd-is-pid-1](../01_system_internals/boot-and-runtime/launchd-is-pid-1.md))
- **RunningBoard**: 프로세스가 계속 실행되어도 되는지를 assertion 으로 판정하는 데몬. ([runningboard-assertions](../01_system_internals/ipc-and-process/runningboard-assertions.md))
- **Jetsam**: 메모리 압력 시 우선순위 밴드로 프로세스를 종료하는 커널 메커니즘. ([jetsam-memory-pressure-bands](../01_system_internals/ipc-and-process/jetsam-memory-pressure-bands.md))
- **SpringBoard / backboardd**: 홈 화면 셸 / 이벤트 라우팅·화면 합성 데몬. ([springboard-frontboard-lifecycle](../01_system_internals/ipc-and-process/springboard-frontboard-lifecycle.md))
- **Watchdog**: 생명주기 전이가 제한 시간을 넘으면 앱을 강제 종료하는 감시자. `0x8badf00d` ([watchdog-termination-codes](../01_system_internals/ipc-and-process/watchdog-termination-codes.md))

---

### 🧱 커널과 서명

- **AMFI**: Apple Mobile File Integrity. exec 시점에 코드 서명과 entitlement 를 검증하는 커널 정책 모듈. ([amfi-code-signature-enforcement](../01_system_internals/kernel-and-driver/amfi-code-signature-enforcement.md))
- **TrustedBSD MAC**: sandbox 판정이 실제로 일어나는 커널 훅 프레임워크. ([trustedbsd-mac-and-sandbox-enforcement](../01_system_internals/kernel-and-driver/trustedbsd-mac-and-sandbox-enforcement.md))
- **IOKit / DriverKit**: 커널 내 C++ 드라이버 프레임워크 / 사용자 공간 드라이버. ([iokit-driver-families](../01_system_internals/kernel-and-driver/iokit-driver-families.md))
- **Memory Compressor**: iOS 에서 디스크 스왑을 대체하는 RAM 내 압축기. ([memory-compressor-and-swap](../01_system_internals/kernel-and-driver/memory-compressor-and-swap.md))
- **chained fixups**: lazy binding 을 대체해 심볼 해석을 실행 전에 확정하는 방식. ([dyld-fixups-and-launch-closures](../01_system_internals/boot-and-runtime/dyld-fixups-and-launch-closures.md))

---

### 🎨 그래픽과 저장소

- **Render Server**: 앱이 커밋한 레이어 트리를 실제로 합성하는 별도 프로세스. ([render-server-composition](../01_system_internals/graphics-and-media/render-server-composition.md))
- **Hitch**: 프레임이 예정 시각보다 늦게 표시된 것. 평균 FPS 와 다르다. ([hitches-measure-user-visible-jank](../01_system_internals/graphics-and-media/hitches-measure-user-visible-jank.md))
- **IOSurface**: 프로세스와 GPU 가 함께 보는 이미지 버퍼. `CVPixelBuffer` 의 뒷단. ([iosurface-shared-gpu-memory](../01_system_internals/graphics-and-media/iosurface-shared-gpu-memory.md))
- **mediaserverd**: 오디오 라우팅과 하드웨어 코덱을 소유하는 시스템 데몬. ([mediaserverd-audio-arbitration](../01_system_internals/graphics-and-media/mediaserverd-audio-arbitration.md))
- **APFS 클론 / 스냅샷**: 블록을 공유하다 쓰는 순간에만 복제하는 복사 / 시점 고정. ([apfs-copy-on-write-clones](../01_system_internals/storage/apfs-copy-on-write-clones.md))
- **SSV**: Signed System Volume. 시스템 볼륨을 해시 트리로 봉인. ([signed-system-volume-seal](../01_system_internals/boot-and-runtime/signed-system-volume-seal.md))
- **Data Protection Class**: 파일 키를 기기 잠금 상태에 묶는 보호 등급. ([data-protection-classes](../01_system_internals/storage/data-protection-classes.md))

---

### 🌐 네트워크

- **ATS**: App Transport Security. TLS 최소 요구를 시스템이 강제. ([ats-transport-security-defaults](../01_system_internals/connectivity/ats-transport-security-defaults.md))
- **isConstrained / isExpensive**: 저데이터 모드 / 셀룰러·핫스팟 경로 신호. ([constrained-and-expensive-paths](../01_system_internals/connectivity/constrained-and-expensive-paths.md))
- **APNs**: Apple Push Notification service. HTTP/2 기반 푸시 전송. ([apple-push-notifications-apns](../04_system_services/apple-push-notifications-apns.md))

### 🔗 관련 문서

- [apple-foundations](apple-foundations.md) - Apple 플랫폼 공통 철학
- [apple-architecture-stack](apple-architecture-stack.md) - 시스템 계층 구조 및 커널 상세
- [apple-history-and-evolution](apple-history-and-evolution.md) - 플랫폼의 변화 과정
- [mobile-security](../../mobile-security.md) - 모바일 보안 통합 가이드
