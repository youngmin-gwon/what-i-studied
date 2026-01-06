---
title: X Window System
tags: [linux, gui, x11, architecture, xorg, gnome, kde]
aliases: [XWindow, X11, X.org, XFree86, X윈도]
date modified: 2026-01-06 21:35:00 +09:00
date created: 2026-01-05 23:59:45 +09:00
---

## 🌐 개요 (Overview)

**X Window System (X11)** 은 유닉스 및 유닉스 계열 운영체제에서 그래픽 사용자 인터페이스(GUI)를 구현하기 위한 네트워크 기반 시스템입니다. 하드웨어 독립적이고 네트워크 투명성을 제공하는 설계 철학이 특징입니다.

## 🏗️ 아키텍처 (Client-Server Model)

X 윈도는 일반적인 응용 프로그램과 반대로 동작하는 **클라이언트-서버 모델** 을 사용합니다.

*   **X Server**: 사용자의 하드웨어(디스플레이, 키보드, 마우스)를 직접 제어하는 프로그램입니다. 화면에 그림을 그리고 입력을 받아 클라이언트에 전달합니다.
*   **X Client**: 실제 돌아가는 응용 프로그램(브라우저, 터미널 등)입니다. X Server에 "여기에 창을 그려달라"고 요청합니다.

> [!NOTE]
> **네트워크 투명성**: X Client와 X Server가 서로 다른 컴퓨터에 있어도 네트워크를 통해 그래픽 화면을 전송할 수 있습니다. (예: 서버에서 돌아가는 프로그램을 내 로컬 화면에서 보기)

---

## 📚 X 라이브러리

| 라이브러리 | 설명 |
| :--- | :--- |
| **Xlib** | 전통적인 X 클라이언트 라이브러리 (레거시) |
| **XCB** | Xlib를 대체하기 위해 등장. 향상된 **쓰레드 기능**, 높은 **확장성** 제공 |
| **Xt (Intrinsics)** | 위젯 툴킷의 기반 라이브러리 |
| **Xm (Motif)** | 상용 위젯 툴킷 |
| **Xaw (Athena)** | 기본 위젯 세트 |

> [!TIP]
> **시험 포인트**: XCB는 Xlib를 대체하는 현대적 라이브러리로, 멀티쓰레드 지원이 핵심입니다.

---

## 🕒 역사 및 프로젝트의 변화 (XFree86 vs X.org)

X 윈도 시스템의 역사적 변화는 시험 및 실무 상식으로 자주 등장합니다.

1.  **XFree86**: 2004년 이전까지 리눅스 및 유닉스 진영에서 가장 선도적인 X 윈도 구현 프로젝트였습니다.
2.  **라이선스 이슈**: 2004년 2월, XFree86 4.4.0 버전이 발표되면서 **GPL 라이선스와 호환되지 않는** 새로운 라이선스를 채택했습니다. 이로 인해 대다수의 리눅스 배포판이 XFree86을 거부하게 되었습니다.
3.  **X.org의 탄생**: XFree86에서 갈라져 나온 포크(Fork) 프로젝트로, 현재 거의 모든 리눅스 배포판이 사용하는 **표준 X 서버** 가 되었습니다.

| 항목 | XFree86 (과거) | X.org (현재 표준) |
| :--- | :--- | :--- |
| **등장 배경** | PC용 유닉스 호환 X 서버 | XFree86 라이선스 변경 후 대체제로 급부상 |
| **특징** | 2004년 이전 주도적 프로젝트 | 현재 거의 모든 리눅스 배포판 채택 |
| **중요 사건** | v4.4.0 라이선스 파동 | X Window System의 사실상 표준 정착 |

---

## 🖥️ X 윈도 구성요소

### Display Manager (디스플레이 매니저)

**사용자 로그인 및 세션 관리** 역할을 수행합니다. 그래픽 로그인 화면을 제공하고 인증 후 데스크탑 환경을 시작합니다.

| 디스플레이 매니저 | 설명 |
| :--- | :--- |
| **GDM** | GNOME Display Manager (GNOME 기본) |
| **SDDM** | Simple Desktop Display Manager (KDE Plasma 기본) |
| **LightDM** | 경량 디스플레이 매니저 (다양한 DE 지원) |
| **XDM** | X Display Manager (가장 기본적) |

### Window Manager (윈도 매니저)

창의 **위치, 크기, 테두리** 등을 관리하는 프로그램입니다. 데스크탑 환경과 구분됩니다.

| 윈도 매니저 | 관련 DE | 설명 |
| :--- | :--- | :--- |
| **Metacity** | GNOME 2 | GNOME 2 버전의 윈도 매니저 |
| **Mutter** | GNOME 3+ | GNOME 3 버전부터 사용, 컴포지팅 지원 |
| **KWin** | KDE Plasma | KDE의 윈도 매니저 |
| **Window Maker** | 독립형 | NeXTSTEP 스타일 |
| **Enlightenment** | 독립형 | 고급 시각 효과 |
| **i3** | 독립형 | 타일링 윈도 매니저 |

> [!IMPORTANT]
> **시험 포인트**: 윈도 매니저 ≠ 데스크탑 환경
> - **윈도 매니저**: Metacity, Mutter, KWin, Window Maker, Enlightenment, i3
> - **데스크탑 환경**: GNOME, KDE, XFce, LXDE

---

## 🖼️ 데스크탑 환경 (Desktop Environment)

X 윈도 시스템 위에서 사용자에게 일관된 인터페이스를 제공하는 소프트웨어 모음입니다.

### GNOME

| 항목 | 내용 |
| :--- | :--- |
| 라이브러리 | **GTK+** |
| 라이선스 | GPL / LGPL |
| 프로젝트 | GNU 프로젝트 |
| 파일 관리자 | **Nautilus** |
| 윈도 매니저 | GNOME 2: **Metacity** → GNOME 3: **Mutter** |

### KDE (Plasma)

| 항목 | 내용 |
| :--- | :--- |
| 라이브러리 | **Qt** |
| 지원 OS | Linux, FreeBSD, Solaris, macOS 등 |
| 윈도 매니저 | **KWin** |

### 기타 데스크탑 환경

- **XFce**: 경량 데스크탑 환경 (GTK+ 기반)
- **LXDE/LXQt**: 초경량 데스크탑 환경

---

## 🔐 X 윈도 보안 및 원격 접속

### DISPLAY 환경변수

X 클라이언트가 연결할 X 서버를 지정합니다.

```bash
# 로컬 디스플레이 (기본)
export DISPLAY=:0

# 원격지 X 서버로 전송
export DISPLAY=192.168.1.100:0.0
```

### xhost - 호스트 기반 접근 제어

```bash
# 특정 IP의 X 클라이언트 허가
xhost + 192.168.12.22

# 특정 IP 접근 해제
xhost - 192.168.12.22

# 모든 접근 허용 (보안 취약)
xhost +
```

### xauth - 키 기반 인증

IP/호스트명 대신 **X 윈도 실행 시 생성되는 키값** 으로 인증합니다.

```bash
# 인증 정보 확인
xauth list

# 키 추가/제거
xauth add display:0 . hexkey
xauth remove display:0
```

> [!TIP]
> **`.Xauthority` 파일**: 사용자 홈 디렉터리에 위치하며, X 윈도 실행 시 키 정보가 저장됩니다.

---

## 🛠️ X 윈도 유틸리티

| 명령어 | 설명 |
| :--- | :--- |
| `xhost` | 호스트 기반 접근 제어 |
| `xauth` | 키 기반 인증 관리 |
| `xmodmap` | 키보드/마우스 매핑 변경 |
| `xwininfo` | 창 정보 조회 |
| `xdpyinfo` | 디스플레이 정보 확인 |
| `xrandr` | 화면 해상도 및 출력 설정 |

---

## 📷 GUI 응용 프로그램

| 프로그램 | 용도 | 비고 |
| :--- | :--- | :--- |
| **evince** | PDF 문서 뷰어 | GNOME 기본 |
| **eog** | 이미지 뷰어 | Eye of GNOME |
| **GIMP** | 이미지 편집기 | Photoshop 대안 |
| **ImageMagick** | 이미지 처리 (CLI/라이브러리) | 변환, 리사이즈 등 |
| **Totem** | 동영상 플레이어 | GNOME 기본 |

> [!IMPORTANT]
> **시험 포인트**: Totem은 **동영상 플레이어**이므로 이미지 뷰어가 아닙니다!

---

## 🔗 연결 문서 (Related Documents)

- [[linux-characteristics]] - 리눅스의 설계 철학
- [[boot-sequence]] - 그래픽 모드(런레벨 5)로의 전환
- [[network-security-protocols]] - X11 포워딩과 SSH
- [[shell-types]] - 셸 종류 및 환경
