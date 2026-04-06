---
title: android-foundations
tags: [android, android/architecture, android/fundamentals, mobile/os]
aliases: []
date modified: 2026-04-06 18:29:18 +09:00
date created: 2025-12-16 15:22:14 +09:00
---

## [[mobile-security]] > [[android-foundations]]

### Android Foundations: Overview & Essential Concepts

안드로이드 운영체제가 어떻게 구동되고 앱이 실행되는지 전체적인 흐름을 파악하기 위한 가이드입니다. 복잡한 로우레벨 기술 용어는 [[android-glossary]] 에 별도로 정리되어 있습니다.

---

#### 💡 Why it matters (Context)

안드로이드는 단순한 앱 실행 환경이 아닌, 수십억 개의 기기에서 작동하는 복잡한 분산 시스템입니다.

- **Resource Constraints**: 배터리와 메모리가 제한된 환경에서 수십 개의 앱이 동시에 구동되어야 합니다.
- **Security by Design**: 모든 앱은 고유한 **UID**를 가지며, 자신의 샌드박스 안에서만 안전하게 동작합니다.
- **Inter-process Communication**: 서로 다른 앱과 시스템은 **Binder**라는 고속 통신 통로를 통해 데이터를 주고받습니다.

---

#### 🏗️ 핵심 구성 요소 (Core Components)

안드로이드 앱을 이루는 네 가지 핵심 구성 요소는 다음과 같습니다.

- **Activity**: 사용자 인터페이스(UI)를 담당하며, 앱의 생명주기(Lifecycle)에 따라 관리됩니다.
- **Service**: 화면 없이 백그라운드에서 오래 실행되는 작업을 처리합니다. (음악 재생, 위치 추적 등)
- **BroadcastReceiver**: 시스템이나 다른 앱에서 보내는 알림(부팅 완료, 배터리 부족 등)에 반응합니다.
- **ContentProvider**: 앱 간에 데이터를 안전하게 공유할 수 있는 표준화된 창구 역할을 합니다.

---

#### ⚙️ 실행 및 런타임 (Execution & Runtime)

- **Process Isolation**: 각 앱은 독립된 프로세스에서 실행되며, 고유한 보안 식별자(UID)를 부여받습니다.
- **Zygote**: 공통 라이브러리를 미리 로드하고 있는 부모 프로세스로, 새 앱이 필요할 때 빠르게 복사(fork)되어 실행 속도를 높입니다.
- **ART (Android Runtime)**: 기기에서 바이트 코드(DEX)를 네이티브 코드로 컴파일하여 실행하는 엔진입니다.

---

#### 📦 빌드 및 배포 (Build & Distribution)

- **APK/AAB**: 앱은 서명이 포함된 패키지 형태로 배포되며, Google Play Store 등의 마켓을 통해 설치됩니다.
- **Trunk Stable Project**: Android 16(Baklava)부터 도입된 개발 모델로, 더 빠르고 안정적인 빌드 및 OS 업데이트 주기를 지원합니다.
- **Mainline (APEX)**: 시스템의 일부 핵심 모듈을 OS 전체 업데이트 없이도 Google Play 를 통해 개별적으로 업데이트하는 기술입니다.

---

#### 📚 읽는 순서 제안 (Recommended Learning Path)

안드로이드의 깊은 내부 동작을 이해하려면 다음 순서대로 문서를 읽는 것을 권장합니다.

1. **아키텍처 기초**: [[android-architecture-stack]] → [[android-foundations]]
2. **시스템 인터널스**: [[android-boot-flow]] → [[android-zygote-and-runtime]] → [[android-binder-and-ipc]]
3. **프레임워크 심화**: [[android-activity-manager-and-system-services]] → [[android-os-development-guide]]
4. **보안 및 진단**: [[mobile-android-foundation-security]] → [[mobile-vulnerability-check]]
5. **성능 및 품질**: [[android-performance-and-debug]] → [[android-testing-and-quality]]

---

#### 🔗 관련 문서

- [[android-glossary]] - 안드로이드 주요 용어 사전
- [[android-evolution-history]] - 안드로이드 버전별 변화와 특징
