---
title: linux-kernel
tags:
  - operating-systems
  - linux
  - kernel
  - OS
---

# Linux Kernel (리눅스 커널)

## 1. 개요 (Overview)
**리눅스 커널(Linux Kernel)**은 시스템의 핵심 하드웨어 자원을 관리하고, 상위 소프트웨어(애플리케이션 및 프레임워크)가 하드웨어와 통신할 수 있도록 중계하는 핵심 운영체제(OS) 커널입니다. 모놀리식 커널(Monolithic Kernel) 구조를 기반으로 설계되었으나, 동적 모듈 로딩(Loadable Kernel Modules)을 지원하여 높은 유연성과 확장성을 자랑합니다.

안드로이드(Android) 시스템 역시 리눅스 커널을 베이스로 구축되어 있으며, 이를 기반으로 상위의 [HAL](../mobile/android/01_system_internals/hal.md) 및 [ART](../mobile/android/01_system_internals/art.md) 레이어가 동작합니다.

---

## 2. 핵심 기능 및 역할 (Core Features)

### ① 하드웨어 추상화 (Hardware Abstraction)
- 복잡하고 다양한 물리적 하드웨어(CPU, RAM, 저장장치, 네트워크 카드 등)를 일관된 일련의 시스템 콜(System Call) 및 파일 시스템 인터페이스로 추상화합니다.
- 사용자 공간(User Space)의 프로그램은 하드웨어의 세부적인 작동 방식을 몰라도 표준 시스템 콜을 통해 자원을 요청할 수 있습니다.

### ② 프로세스 관리 (Process Management)
- **스케줄링(Scheduling)**: 여러 프로세스와 스레드가 CPU 자원을 효율적으로 나눠 쓸 수 있도록 CPU 스케줄러(CFS - Completely Fair Scheduler 등)를 관리합니다.
- **프로세스 생명주기 관리**: 프로세스의 생성(`fork`, `exec`), 동기화, 자원 할당 및 종료(`exit`)를 관장합니다.

### ③ 메모리 관리 (Memory Management)
- **가상 메모리(Virtual Memory)**: 각 프로세스에 독립된 가상 주소 공간을 제공하여 보안 및 안정성을 확보합니다.
- **페이징 및 할당(Paging & Allocation)**: 물리 메모리(RAM)와 가상 메모리 간의 매핑을 관리하며, 메모리 부족 시 올바른 회수 전략을 수행합니다.

### ④ 디바이스 드라이버 (Device Drivers)
- 하드웨어 제어 장치와 직접 대화하는 소프트웨어 모듈입니다.
- 커널 공간(Kernel Space)에서 동작하며, 디스플레이, 카메라, 센서, Wi-Fi, Bluetooth 등 다양한 주변장치를 구동하는 핵심 역할을 담당합니다.

---

## 3. 안드로이드 OS의 기반으로서의 역할 (Foundation of Android OS)

안드로이드는 표준 리눅스 메인라인 커널을 기반으로 하되, 모바일 환경의 제약사항(전력 소비, 메모리 부족, 프로세스 간 통신 성능)을 극복하기 위해 안드로이드 특화 커널 드라이버 및 패치를 추가하여 사용합니다.

- **Binder IPC**: 안드로이드 시스템의 핵심 프로세스 간 통신(IPC) 메커니즘으로, 커널 드라이버 수준에서 고성능 메시지 전달 및 객체 참조 전달을 처리합니다.
- **Low Memory Killer (LMK)**: 모바일 단말의 메모리가 부족해질 때 우선순위가 낮은 백그라운드 프로세스를 강제 종료하여 시스템 안정성을 유지합니다.
- **Ashmem (Anonymous Shared Memory)**: 프로세스 간 대용량 메모리 버퍼를 공유하기 위한 안드로이드 전용 공유 메모리 시스템입니다.
- **전력 관리 (Power Management / Wake Locks)**: 모바일 기기의 배터리 효율 극대화를 위해 불필요한 자원 소비를 제한하는 안드로이드 전용 전원 관리 드라이버를 탑재하고 있습니다.

---

## 4. 연관 개념 (Related Notes)
- [HAL (Hardware Abstraction Layer)](../mobile/android/01_system_internals/hal.md) - 커널 드라이버 위에서 안드로이드 프레임워크에 하드웨어 표준 인터페이스를 제공하는 계층
- [ART (Android Runtime)](../mobile/android/01_system_internals/art.md) - 리눅스 커널 위 사용자 공간(User Space)에서 애플리케이션 바이트코드를 실행하는 안드로이드 런타임
