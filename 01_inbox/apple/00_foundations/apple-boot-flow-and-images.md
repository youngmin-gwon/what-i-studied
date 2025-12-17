---
title: apple-boot-flow-and-images
tags: [apple, boot, images, launch, security]
aliases: []
date modified: 2025-12-17 17:05:00 +09:00
date created: 2025-12-16 16:09:51 +09:00
---

## Boot Flow & System Images

전원 버튼을 눌렀을 때부터 사과 로고가 뜨고, 잠금 화면이 나오고, 내 앱이 실행되기까지의 여정입니다.
단순히 OS의 부팅 과정을 넘어서, **앱이 얼마나 빨리 켜지는지(Launch Time)**와 **왜 위변조된 앱이 실행되지 않는지(Security)**를 이해하는 열쇠입니다.

### 💡 왜 이것을 알아야 하나요? (Why it matters)
- **앱 실행 속도(Launch Time)**: 부팅 과정에서 로드되는 **dyld Shared Cache**는 앱 실행 속도에 결정적인 영향을 미칩니다. 이 원리를 알면 "앱이 왜 느리게 켜지는지" 분석할 수 있습니다.
- **"앱을 확인할 수 없음" 에러**: 개발 중이나 배포 시 "손상된 앱"이라며 실행되지 않는 이유는 **Secure Boot Chain**과 코드 서명 검증 과정에 있습니다.
- **시스템 복구**: 기기가 먹통이 되었을 때 DFU 모드나 Recovery 모드가 무엇을 하는 건지 이해할 수 있습니다.

---

### 🚀 부팅 시퀀스: 신뢰의 사슬 (Chain of Trust)

Apple 기기는 전원이 들어오는 순간부터 OS가 켜질 때까지, 단계마다 "이전 단계가 다음 단계의 신원을 보증"하는 방식으로 보안을 유지합니다. 이를 **Secure Boot Chain**이라고 합니다.

1.  **Boot ROM (Hardware Root of Trust)**
    - 칩 제조 시 불변으로 박혀 나오는 코드입니다. 절대 위변조될 수 없으므로 모든 신뢰의 시작점입니다.
    - Apple Root CA 공개키를 가지고 있어, 다음 단계(iBoot)의 서명을 검증합니다.

2.  **Low-Level Bootloader (LLB) & iBoot**
    - 초기 하드웨어를 깨우고, 커널을 로드할 준비를 합니다.
    - **Relevance**: 여기서 OS 버전 탈옥 등을 방지하는 서명 확인이 일어납니다.

3.  **Kernel (XNU) Start**
    - 커널이 메모리에 올라오고(`Slide` 적용), 하드웨어 드라이버를 로드합니다.

4.  **launchd (PID 1)**
    - 커널이 실행하는 첫 번째 사용자 프로세스입니다.
    - 시스템의 모든 데몬(백그라운드 서비스)을 깨웁니다.

5.  **User Space (SpringBoard / WindowServer)**
    - 화면을 그리는 UI 서버가 켜지고, 잠금 화면이 나타납니다.

---

### 📦 이미지와 시스템 볼륨 (System Images)

Apple OS는 사용자가 시스템 파일을 실수로라도 건드리지 못하게 철저히 격리합니다.

#### 1. Signed System Volume (SSV) - macOS
macOS Big Sur부터 도입된 강력한 보안 기능입니다.
- 시스템 볼륨은 **Read-Only**일 뿐만 아니라, **모든 파일의 해시값(Merkle Tree)이 캡슐화되어 서명**되어 있습니다.
- 파일 하나라도 1비트만 바뀌어도 서명이 깨져서 부팅조차 거부됩니다. (악성코드가 시스템 파일 감염 불가)

#### 2. dyld Shared Cache (성능의 핵심)
앱이 `UIKit`, `Foundation` 같은 프레임워크를 쓸 때마다 디스크에서 파일을 읽어오면 엄청 느리겠죠?
- 부팅 시점에 OS는 자주 쓰이는 시스템 프레임워크들을 **거대한 하나의 파일(Shared Cache)**로 묶어 메모리에 미리 올려둡니다.
- 모든 앱은 이 메모리 영역을 공유합니다. 따라서 앱 실행 시 시스템 프레임워크 로딩 시간은 거의 ‘0’에 가깝습니다.

---

### 🛠️ 문제 해결과 진단 (Troubleshooting)

#### 기기가 먹통일 때 (Recovery vs DFU)
- **Recovery Mode**: `iBoot` 단계에서 멈추고 OS를 다시 설치하는 모드입니다. 화면에 케이블 연결 그림이 뜹니다.
- **DFU (Device Firmware Update)**: `Boot ROM` 단계에서 멈추고 펌웨어 자체를 다시 쓰는 모드입니다. 화면이 완전히 까맣게 나옵니다. 정말 심각한 벽돌 상태 복구용입니다.

#### 업데이트 (OTA)
- iOS 업데이트는 전체를 다시 받는 게 아니라, 변경된 부분(Delta)만 받아서 기존 파티션에 덧씌우는 방식이 아닙니다.
- 새로운 파티션에 업데이트된 이미지를 준비해두고, **부팅 순서를 바꿔치기**하는 방식(A/B Update와 유사)이라 안전합니다.

### 더 보기
- [[apple-architecture-stack]] - 커널과 유저 공간의 분리
- [[apple-sandbox-and-security]] - 앱 실행 후의 보안 (샌드박스)
