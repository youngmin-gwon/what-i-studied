---
title: SSH Remote Access
tags: [linux, network, remote, ssh, security]
aliases: [SSH, sshd, Secure Shell, 원격 접속]
date modified: 2026-04-07 10:52:00 +09:00
date created: 2026-04-07 10:52:00 +09:00
---

## 🌐 개요 (Overview)

**SSH (Secure Shell)**는 네트워크 상의 다른 컴퓨터에 로그인하거나 명령을 실행할 수 있게 해주는 암호화된 네트워크 프로토콜입니다. 기본적으로 **TCP 22번 포트**를 사용하며, 텔넷(Telnet)이나 RSH를 대체하는 보안 표준입니다.

---

## 🏗️ SSH 주요 도구

| 도구 | 설명 |
| :--- | :--- |
| **ssh** | 원격 접속 및 명령 실행 클라이언트 |
| **sshd** | SSH 서비스 데몬 |
| **scp** | SSH 기반 보안 파일 복사 |
| **sftp** | SSH 기반 보안 파일 전송 프로토콜 |
| **ssh-keygen** | 인증용 키 쌍(공개키/개인키) 생성 |
| **ssh-copy-id** | 공개키를 원격 서버에 등록 |
| **ssh-agent** | 개인키 비밀번호를 관리하는 데몬 |

---

## 🔑 키 기반 인증 (Key-based Authentication)

비밀번호 대신 키 쌍을 사용하여 보안을 강화하고 자동 로그인을 구현합니다.

### 1. 키 쌍 생성
```bash
# 기본 RSA 3072비트 이상 권장
ssh-keygen -t rsa -b 4096

# Ed25519 (최신, 고성능) 권장
ssh-keygen -t ed25519
```
- 생성 파일: `~/.ssh/id_rsa` (개인키), `~/.ssh/id_rsa.pub` (공개키)

### 2. 공개키 전송
```bash
ssh-copy-id user@remote-host
```
- 작동 원리: 원격 서버의 `~/.ssh/authorized_keys` 파일에 공개키 내용이 추가됩니다.

---

## ⚙️ SSH 서버 설정 (/etc/ssh/sshd_config)

설정 변경 후 반드시 서비스를 재시작(`systemctl restart sshd`)해야 합니다.

| 항목 | 설정 예시 | 설명 |
| :--- | :--- | :--- |
| **Port** | `Port 2222` | 기본 포트 변경 (보안 강화) |
| **PermitRootLogin** | `no` | root 로그인 금지 (권장) |
| **PasswordAuthentication** | `no` | 키 기반 인증만 허용 |
| **PubkeyAuthentication** | `yes` | 공개키 인증 사용 여부 |
| **AllowUsers** | `user1 user2` | 허용할 사용자 지정 |
| **X11Forwarding** | `yes` | X11 그래픽 포워딩 허용 |

---

## 🔐 SSH 터널링 (SSH Tunneling)

보안되지 않은 프로토콜을 SSH 암호화 채널을 통해 전송합니다.

### 1. 로컬 포트 포워딩 (Local Forwarding)
로컬상의 특정 포트를 원격 서버로 터널링합니다.
```bash
# 내 컴퓨터의 5901 포트를 서버의 5901 포트로 연결
ssh -L 5901:localhost:5901 user@server-ip
```

### 2. 원격 포트 포워딩 (Remote Forwarding)
원격 서버의 포트를 내 컴퓨터로 연결합니다. (외부에서 내부망 접속 시 사용)
```bash
ssh -R 8080:localhost:80 user@remote-ip
```

### 3. 동적 포트 포워딩 (Dynamic Forwarding)
SSH 서버를 SOCKS 프록시 서버로 사용합니다.
```bash
ssh -D 1080 user@remote-ip
```

---

## 📁 클라이언트 설정 (~/.ssh/config)

복잡한 접속 정보를 간단한 별칭으로 관리할 수 있습니다.

```bash
# ~/.ssh/config
Host myserver
    HostName 1.2.3.4
    User admin
    Port 2222
    IdentityFile ~/.ssh/id_ed25519
```

접속 시: `ssh myserver`

---

## 🔧 주요 명령어 예시

```bash
# 특정 포트로 접속
ssh -p 2222 user@host

# 원격에서 단일 명령 실행
ssh user@host "ls -l /var/log"

# X11 포워딩 활성화 접속
ssh -X user@host

# scp 파일 전송
scp -P 2222 localfile.txt user@host:/path/to/remote/
```

---

## 🔗 연결 문서 (Related Documents)

- [[network-commands]] - 기본 네트워크 명령어
- [[security-commands]] - 방화벽 및 보안 설정
- [[vnc-remote-access]] - VNC와 SSH 터널링
- [[x-window-system]] - X11 포워딩 개념
