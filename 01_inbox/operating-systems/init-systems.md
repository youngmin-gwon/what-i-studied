---
title: Init Systems
tags: [operating-systems, linux, init, systemd, sysvinit, upstart, process-management]
aliases: [Init 시스템, PID 1, System Setup]
date modified: 2026-04-06 18:55:00 +09:00
date created: 2026-04-06 18:55:00 +09:00
---

## 🌐 개요 (Overview)

**Init 시스템**은 운영체제 커널이 로딩된 후 가장 먼저 실행되는 프로세스로, 시스템의 모든 다른 프로세스를 시작하고 관리하는 역할을 합니다. 리눅스 시스템에서 항상 **PID 1**을 가집니다.

- **부모 프로세스**: 모든 프로세스의 조상입니다. 부모가 종료된 고아 프로세스를 입양하여 관리합니다.
- **시스템 상태 제어**: 서비스 시작/종료, 시스템 종료 및 재부팅 등을 관리합니다.

---

## 🔄 Init 시스템의 진화 (Evolution)

리눅스 역사를 통해 세 가지 주요 Init 시스템이 사용되었습니다.

### 1. SysV init (전통적 방식)
UNIX 시스템 V 계열에서 유래한 전통적인 방식입니다.

- **특징**: `/etc/init.d/` 디렉토리에 있는 셸 스크립트를 순차적으로 실행합니다.
- **런레벨(Runlevels)**: 0~6번의 숫자로 시스템 상태를 구분합니다.
- **단점**: 서비스가 순차적으로 실행되므로 부팅 속도가 느리고, 복잡한 의존성 관리가 어렵습니다.

### 2. Upstart (이벤트 기반)
Ubuntu에서 SysV init의 한계를 극복하기 위해 개발한 방식입니다.

- **특징**: 하드웨어 감지, 네트워크 연결 등 특정 **이벤트**가 발생할 때 서비스를 실행합니다.
- **장점**: 병렬 실행이 가능해졌으며, 장치 연결 등에 유연하게 대응합니다.

### 3. systemd (현대적 표준)
대부분의 현대 리눅스 배포판(RHEL, CentOS, Ubuntu, Debian, Fedora 등)에서 사용하는 표준입니다.

- **특징**: **Unit** 단위 관리, 공격적인 **병렬 실행**, **소켓 활성화(Socket Activation)** 등을 지원합니다.
- **장점**: 의존성 문제를 자동으로 해결하며, 부팅 속도가 가장 빠르고 명령어가 표준화되어 있습니다.
- **PID 1**: `/sbin/init`은 실제로는 `/lib/systemd/systemd`로 연결된 심볼릭 링크인 경우가 많습니다.

---

## 🆚 주요 차이점 비교

| 기능 | SysV init | Upstart | systemd |
| :--- | :--- | :--- | :--- |
| **실행 방식** | 순차적 (Serial) | 이벤트 기반 (Event) | 병렬 (Parallel) |
| **관리 단위** | 셸 스크립트 | Job | Unit (Service, Target 등) |
| **상태 구분** | Runlevel (0-6) | State | Target |
| **의존성 관리** | 수동 (파일 이름 순서) | 이벤트 연결 | 자동 (Wants, Requires) |
| **로그 관리** | `/var/log/messages` | 로그 파일 개별 관리 | `journald` (바이너리 로그) |

---

## 🎯 왜 systemd가 표준이 되었나?

1.  **공격적 병렬화**: 소켓 활성화 기술을 통해 의존 관계에 있는 서비스들을 동시에 시작할 수 있습니다.
2.  **통합 관리**: 서비스뿐만 아니라 마운트 포인트, 타이머(Cron 대체), 장치 등을 모두 Unit으로 관리합니다.
3.  **의존성 해결**: `After`, `Before`, `Requires` 등의 지시어를 통해 서비스 간 실행 순서를 명확히 정의합니다.
4.  **로그 통합**: `journalctl`을 통해 시스템 전체 로그를 일관된 방식으로 조회할 수 있습니다.

---

## 🔗 연결 문서 (Related Documents)

- [[systemd]] - 현대 리눅스 서비스 관리의 상세 가이드 (Unit, Target, Socket)
- [[boot-sequence]] - BIOS에서 Init 실행까지의 부팅 과정
- [[process-states-lifecycle]] - 프로세스의 생성과 소멸, PID 1의 역할
- [[android-init-and-services]] - 안드로이드 특유의 `init.rc` 기반 초기화 방식
