---
title: apple-boot-flow-and-images
tags: []
aliases: []
date modified: 2026-04-07 15:15:33 +09:00
date created: 2026-04-03 22:15:19 +09:00
---

## [[mobile-security]] > [[apple-boot-flow-and-images]]

### Boot Flow & System Images: Chain of Trust

전원 버튼을 누르는 순간부터 OS 가 로드되고 앱이 실행되기까지의 시스템 여정을 다룹니다. 이 과정은 단순히 부팅 속도뿐만 아니라, Apple 의 핵심 보안 철학인 **Secure Boot**와 앱 실행 무결성을 이해하는 근간이 됩니다.

---

#### 💡 Context: 왜 부팅 과정을 알아야 하는가?

- **Chain of Trust**: 기기가 켜질 때 각 단계가 다음 단계의 서명을 검증하여 위변조된 코드의 실행을 차단합니다.
- **Launch Performance**: **dyld Shared Cache** 매커니즘을 통해 시스템 프레임워크 로딩 시간을 단축하며, 이는 앱의 앱 실행 속도(Launch Time)와 직결됩니다.
- **Recovery & DFU**: 시스템 장애 시 복구 모드(Recovery)와 펌웨어 업데이트 모드(DFU)의 차이를 이해하고 하부 레벨에서의 대응이 가능해집니다.

---

#### 🚀 부팅 시퀀스: 신뢰의 사슬 (Secure Boot)

1. **Boot ROM (Hardware Root of Trust)**: 칩에 고정된 불변의 코드로, Apple Root CA 공개키를 통해 다음 단계인 iBoot 의 서명을 검증합니다.
2. **iBoot (Low-Level Bootloader)**: 하드웨어를 초기화하고 커널(XNU)의 무결성을 확인한 후 메모리에 로드합니다.
3. **Kernel (XNU) Start**: 커널이 시작되면서 하드웨어 드라이버를 로드하고 첫 번째 유저 프로세스인 `launchd` 를 실행합니다.
4. **Launchd (PID 1)**: 시스템 데몬들을 깨우며, 최종적으로 **SpringBoard**(홈 화면)나 **WindowServer**를 구동합니다.

---

#### 📦 시스템 이미지 및 데이터 격리

- **Signed System Volume (SSV)**: 시스템 볼륨은 읽기 전용(Read-Only)이며 Merkle Tree 기반의 해시 서명으로 보호되어 1 비트의 변조도 허용하지 않습니다.
- **dyld Shared Cache**: 자주 사용되는 시스템 프레임워크(UIKit, Foundation 등)를 하나의 거대한 파일로 묶어 부팅 시 메모리에 미리 로드함으로써 모든 앱의 실행 효율을 극대화합니다.

---

#### 🛠️ 장애 대응 및 업데이트 매커니즘

- **Recovery Mode**: `iBoot` 레벨에서 멈춘 상태로 OS 재설치가 가능합니다.
- **DFU Mode**: `Boot ROM` 레벨에서 멈춘 상태로 펌웨어 자체를 복구하며, 완전한 시스템 벽돌 상태에서 사용됩니다.
- **A/B Update**: 업데이트 시 새로운 파티션을 준비하고 부팅 순서를 교체하는 방식을 통해 업데이트 중 발생할 수 있는 데이터 손실 위험을 최소화합니다.

---

#### 📚 연관 문서 및 심화 학습
- [[apple-architecture-stack]] - Darwin 커널과 시스템 계층 구조
- [[apple-foundations]] - Apple 플랫폼 공통 설계 철학
- [[apple-sandbox-and-security]] - 앱 실행 이후의 보안 샌드박스 메커니즘
- [[apple-runtime-and-swift]] - 앱 실행의 내부 런타임 구조
- [[apple-performance-and-debug]] - 부팅 및 앱 실행 속도 분석 가이드
