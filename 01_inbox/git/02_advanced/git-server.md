---
title: git-server
tags: [git, http, protocols, server, ssh]
aliases: [Git 서버 구축, Git 프로토콜, 서버 사이드 Git]
date modified: 2025-12-18 15:22:14 +09:00
date created: 2025-12-18 16:50:00 +09:00
---

## Git on the Server: 저장소 공유와 협업의 기반

Git 은 분산 버전 관리 시스템이지만, 팀 협업을 위해서는 누구나 접근 가능한 '중앙 저장소'가 필요합니다. 이 문서에서는 Git 서버를 운영하기 위한 프로토콜과 구축 방법을 다룹니다.

---

### 💡 Why it matters (Context)

- **협업의 중심**: 팀원들이 코드를 동기화하고 코드 리뷰를 진행하는 허브 역할을 합니다.
- **인프라 이해**: GitHub 같은 서비스가 내부적으로 어떤 프로토콜을 사용하여 데이터를 주고받는지 이해하게 됩니다.
- **자체 호스팅**: 보안이나 비용 문제로 사내에 직접 Git 서버를 구축해야 할 때 필요한 지식을 제공합니다.

---

## 🏗️ 1. Git 전송 프로토콜 (The Protocols)

Git 은 데이터를 전송하기 위해 네 가지 주요 프로토콜을 사용합니다.

| 프로토콜 | URL 예시 | 장점 | 단점 |
| :--- | :--- | :--- | :--- |
| **Local** | `/path/to/repo.git` | 단순함, 기존 파일 권한 활용 | 네트워크 접근 불가, 원격 협업 어려움 |
| **SSH** | `user@server:repo.git` | **표준**, 보안 우수, 효율적 전송 | 익명 접근 불가(모든 유저 계정 필요) |
| **HTTP** | `https://server/repo.git` | 방화벽 통과 용이, 익명 읽기 가능 | 설정이 상대적으로 복잡(Smart HTTP) |
| **Git** | `git://server/repo.git` | 가장 빠른 전송 속도 | 보안(인증) 기능 전무, 전용 포트 필요 |

---

## 🏗️ 2. 서버 구축 및 설정 (Bare Repository)

서버용 저장소는 작업 파일이 없는 **Bare Repository**여야 합니다.

### 서버 저장소 생성
```bash
git init --bare my_project.git
```

### SSH 를 통한 접근 설정
1. 서버에 `git` 사용자를 생성합니다.
2. 개발자의 퍼블릭 키(`id_rsa.pub`)를 서버의 `~git/.ssh/authorized_keys` 에 등록합니다.
3. 보안을 위해 `git-shell` 을 사용하여 SSH 를 통한 일반 쉘 접근을 제한합니다.

---

## 🏗️ 3. 전용 Git 서버 솔루션

직접 서버를 구축하는 것보다 관리 효율을 위해 전용 소프트웨어를 사용하기도 합니다.

- **Gitolite**: SSH 환경에서 세밀한 권한 관리를 지원하는 레이어.
- **GitLab / Gitea**: 자체 호스트 가능한 웹 기반 UI 와 다양한 협업 기능(PR, Issue) 제공.

---

## 🚨 흔한 실수 (Common Mistakes)

1. **Non-Bare 저장소로 Push** ❌
   - 워킹 디렉토리가 있는 일반 저장소로 Push 하면 서버의 워킹 디렉토리와 인덱스가 꼬이게 됩니다. 서버 저장소는 반드시 `--bare` 로 만드세요.
2. **SSH 키 권한 관리 부실**
   - `authorized_keys` 파일이나 `.ssh` 디렉토리의 권한이 너무 넓으면(`chmod 777` 등) SSH 접근이 차단됩니다. (보통 600, 700 권한 필요)
3. **HTTP 포트 개방 누락**
   - 방화벽에서 80/443 포트 외에 Git 전용 포트(9418)를 막아두면 Git 프로토콜 사용이 불가능합니다.

---

### 📚 연결 문서

- [[00_fundamentals/git-internals|Git 인턴십]] - Smart/Dumb 프로토콜의 기술적 차이
- [[01_strategies/branching-strategies|브랜치 전략]] - 서버를 활용한 분산 워크플로우 설계
- [[02_advanced/troubleshooting|트러블슈팅]] - 네트워크 연결 및 권한 문제 해결
- [[03_tools/credential-storage.md|인증 관리]] - 서버 로그인 정보 안전하게 저장하기
