---
title: 09-environment-startup
tags: [bashrc, cron, environnement, linux, profile, shell]
aliases: []
date modified: 2025-12-28 22:25:20 +09:00
date created: 2025-12-28 20:45:09 +09:00
---

## 09. 환경 관리 및 시작 스크립트

사용자의 셸 환경을 정의하는 설정 파일들과 작업의 자동화를 위한 스케줄러 환경을 비교합니다.

### 1. 시작 파일 로딩 순서 (Startup Files)

| 셸 유형 | 파일 로딩 순서 | 주요 용도 |
| :--- | :--- | :--- |
| **로그인 셸** | `/etc/profile` → `~/.bash_profile` (또는 `.profile`) | PATH 설정, 시스템 환경 변수 |
| **비로그인 셸** | `~/.bashrc` | Alias, 사용자 함수, 프롬프트(`PS1`) |
| **비인터랙티브** | `$BASH_ENV` (지정된 경우에만) | 스크립트 실행 전 공통 환경 |

### 2. PATH 관리 전략

| 환경                  | 관리 방법                    | 특징                |
| :------------------ | :----------------------- | :---------------- |
| **일반 터미널**          | `PATH="$PATH:/new/path"` | 뒤에 추가 (기본 명령 우선)  |
| **커스텀 바이너리**        | `PATH="/new/path:$PATH"` | 앞에 추가 (커스텀 명령 우선) |
| **관리 함수 (Prepend)** | `path_prepend() { … }`   | 중복 방지 및 안전한 추가    |

### 3. 스케줄러 환경 비교 (Cron vs Systemd)

| 항목 | Cron | Systemd Timer |
| :--- | :--- | :--- |
| **기본 셸** | `/bin/sh` (POSIX) | `StandardOutput=` 등 설정 가능 |
| **기본 PATH** | 매우 짧음 (`/usr/bin:/bin`) | 유닛 파일 내 `Environment=` 사용 |
| **워크 디렉터리** | 사용자 홈 또는 `/` | `WorkingDirectory=` 명시 가능 |
| **의존성** | 단순 시간 기준 | 다른 서비스 성공 후 실행 가능 |

### 4. 프롬프트 구성 요소 (PS1)

셸 프롬프트에 표시될 정보와 색상을 설정하는 특수 코드들입니다. 상세 목록과 설정 예시는 [[shell-environment-commands#프롬프트-구성-요소-ps1-특수-문자]]를 참조하세요.

---

### 🔗 연결 문서

- [[08-process-control]] - 프로세스 및 잡 제어
- [[10-debugging-style]] - 디버깅 및 스타일 가이드
