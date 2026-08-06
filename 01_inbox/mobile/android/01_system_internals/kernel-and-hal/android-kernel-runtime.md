---
title: android-kernel-runtime
tags: ["android", "android/kernel", "android/system-internals"]
aliases: ["Android Kernel", "android-kernel", "안드로이드 커널 런타임"]
date modified: 2026-08-06 16:42:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

## Android Kernel Runtime 개요 및 책임

안드로이드의 최하단에 위치하는 **Android Kernel 영역**은 표준 [Linux Kernel](../../../../operating-systems/linux-kernel.md) 기술과 안드로이드 특화 모바일 시스템 정책(GKI, LMKD, Binder 등)이 교차하는 최하위 시스템 영역이다.

이 인덱스는 [Linux Kernel](../../../../operating-systems/linux-kernel.md) 드라이버, 전원 관리(Power/Suspend), 메모리 관리(zRAM/LMKD), 프로세스 간 통신([Binder IPC](../binder-ipc.md)), [SELinux 보안](../../../05_security_privacy/appops-and-permissions.md) 정책 계약을 하나로 연결하는 허브 역할을 수행한다.

---

### 1. 주요 핵심 구성 요소 (Key Components)

- **GKI (Generic Kernel Image)**: 안드로이드 12부터 도입된 표준 커널 이미지 구조로, 커널 코어와 제조사(SoC) 디바이스 드라이버를 분리하여 OS 업데이트 생산성을 대폭 향상.
- **[Binder IPC Driver](../binder-ipc.md)**: 안드로이드 프로세스 간 통신을 위한 `/dev/binder` 커널 모듈 드라이버.
- **LMKD (Low Memory Killer Daemon) & PSI**: 시스템 메모리 부족 시 중요도가 낮은 앱 프로세스 수거 제어.
- **DMA-BUF (Direct Memory Access Buffer)**: 카메라 및 그래픽 처리 시 메모리 복사 없이 디바이스 간 메모리 버퍼를 대용량 공유.

---

### 2. 읽는 기준 및 탐색 경로

- **커널 모듈 및 호환성 문의**: ACK / GKI / KMI 및 빌드 계약부터 탐색.
- **메모리 부족 및 앱 튕김 현상**: LMKD, PSI, zRAM 메모리 압박 매개변수 조사.
- **하드웨어 및 센서 드라이버 통신**: [HAL and Native Boundary](hal-native-boundary.md) 및 [HAL 레퍼런스](../hal.md)로 이동.

---

### 연결 문서 (Reference Links)

- [Linux Kernel 레퍼런스](../../../../operating-systems/linux-kernel.md) - 안드로이드 하부 토대가 되는 리눅스 커널 레퍼런스
- [HAL & Native Boundary](hal-native-boundary.md) - 커널과 유저스페이스 NDK/C++ 경계
- [HAL 레퍼런스](../hal.md) - 하드웨어 추상화 계층 레퍼런스
- [Binder IPC 레퍼런스](../binder-ipc.md) - 안드로이드 전용 커널 IPC 드라이버
