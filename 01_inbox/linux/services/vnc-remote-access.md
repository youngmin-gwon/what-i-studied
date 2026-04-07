---
title: vnc-remote-access
tags: [desktop, linux, remote, vnc, x11]
aliases: [VNC, vncserver, 원격 데스크톱]
date modified: 2026-04-07 10:50:00 +09:00
date created: 2026-01-06 19:48:00 +09:00
---

## 🌐 개요 (Overview)

**VNC (Virtual Network Computing)**는 원격으로 그래픽 데스크톱 환경에 접속할 수 있게 해주는 프로토콜입니다. X11 포워딩과 달리 전체 데스크톱 세션을 공유할 수 있습니다.

---

## 📊 VNC 포트 번호

>[!IMPORTANT]
>**핵심 공식**: VNC 포트 = **5900 + 디스플레이 번호**

| 디스플레이 번호 | VNC 포트 | 웹 브라우저 포트 |
| :---: | :---: | :---: |
| `:1` | **5901** | 5801 |
| `:2` | **5902** | 5802 |
| `:3` | **5903** | 5803 |
| `:10` | **5910** | 5810 |

---

## 📦 설치 (TigerVNC)

```bash
# RHEL/CentOS
dnf install tigervnc-server

# Ubuntu/Debian
apt install tigervnc-standalone-server
```

---

## ⚙️ VNC 서버 설정

### 1. VNC 비밀번호 설정

```bash
vncpasswd

# 출력:
# Password: (6~8자)
# Verify:
# Would you like to enter a view-only password (y/n)? n
```

### 2. VNC 서버 시작

```bash
# 디스플레이 :1로 시작
vncserver :1

# 해상도 지정
vncserver :1 -geometry 1920x1080 -depth 24

# 서버 종료
vncserver -kill :1
```

### 3. systemd 서비스 설정 (RHEL 8+)

```bash
# /etc/tigervnc/vncserver.users
:1=username
:2=otheruser
```

```bash
# 서비스 시작
systemctl enable --now vncserver@:1
```

---

## 🖥️ xstartup 설정

VNC 세션에서 실행할 데스크톱 환경을 지정합니다.

### ~/.vnc/xstartup

```bash
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS

# GNOME
exec gnome-session &

# KDE
# exec startplasma-x11 &

# XFCE
# exec startxfce4 &

# 경량 WM (twm)
# exec twm &
```

```bash
chmod +x ~/.vnc/xstartup
```

---

## 💻 VNC 클라이언트 접속

### Linux

```bash
# vncviewer 사용
vncviewer 192.168.1.10:1
# 또는
vncviewer 192.168.1.10:5901
```

### Windows/Mac

- **TigerVNC Viewer**, **RealVNC Viewer** 등 클라이언트 사용
- 접속 주소: `192.168.1.10:1` 또는 `192.168.1.10:5901`

---

## 🔐 SSH 터널링 (보안 접속)

VNC 는 기본적으로 암호화되지 않으므로, SSH 터널을 통한 접속을 권장합니다.

```bash
# 로컬 포트 5901을 원격 서버의 5901로 포워딩
ssh -L 5901:localhost:5901 user@server.example.com

# 다른 터미널에서 localhost로 VNC 접속
vncviewer localhost:1
```

---

## 🔄 X11 포워딩과 비교

| 항목 | VNC | X11 포워딩 |
| :--- | :--- | :--- |
| **접속 방식** | 전체 데스크톱 공유 | 개별 애플리케이션 창 |
| **설정** | VNC 서버 필요 | `ssh -X` 옵션만 필요 |
| **포트** | 5900+ 대역 | SSH 포트 (22) |
| **세션 지속** | 연결 끊어도 세션 유지 | 연결 끊기면 종료 |
| **성능** | 대역폭 많이 사용 | 상대적으로 가벼움 |

### X11 포워딩 사용법

```bash
# 서버에서 X11 애플리케이션 실행하고 로컬에 표시
ssh -X user@server
firefox &

# DISPLAY 환경변수 확인
echo $DISPLAY
# localhost:10.0 형태로 표시됨
```

>[!TIP]
>**X11 포워딩** 활성화를 위해 서버의 `/etc/ssh/sshd_config` 에서 `X11Forwarding yes` 설정이 필요합니다.

---

## 🔧 문제 해결

```bash
# VNC 서버 로그 확인
cat ~/.vnc/*.log

# 포트 확인
ss -tlnp | grep 590

# 방화벽 허용
firewall-cmd --add-port=5901/tcp --permanent
firewall-cmd --reload
```

---

## 🔗 연결 문서 (Related Documents)

- [[x-window-system]] - X Window 시스템 개념
- [[ssh-remote-access]] - SSH 관련 명령어 및 터널링
- [[security-commands]] - 방화벽 설정
