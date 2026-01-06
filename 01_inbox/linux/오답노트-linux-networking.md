---
title: 오답노트 - 리눅스 전체
tags: [linux, 오답노트, networking, shell, process, xwindow, systemd]
aliases: [Linux Wrong Answers, 리눅스 오답노트, 리눅스마스터]
date modified: 2026-01-06 21:50:00 +09:00
date created: 2026-01-06 21:50:00 +09:00
---

## 🌐 개요

리눅스 자격증 시험 오답노트입니다. 모든 문제를 원문 그대로 수록하고 해설을 추가했습니다.

---

# 📡 네트워크 기초

---

## Q4. IEEE 802.6 (MAN 표준)

**문제**: 다음 중 MAN을 위한 국제 표준안으로 IEEE 802.6에 정의되어 있는 것으로 알맞은 것은?
- ① FDDI
- ② DQDB
- ③ X.25
- ④ Frame Relay

**정답**: ② DQDB

**해설**: IEEE 802.6 = **DQDB (Distributed Queue Dual Bus)** = MAN(Metropolitan Area Network) 표준

**관련 문서**: [[network-standards#🔌 IEEE 802 표준]]

---

## Q7. 이더넷 매체 표기법

**문제**: 다음 중 이더넷 매체 표기법에 대한 설명으로 틀린 것은?
- ① 10BASE-5는 10Mbps의 전송 속도에 전송매체는 동축케이블이다.
- ② 100BASE-TX는 100Mbps의 전송속도에 전송매체는 UTP-5 케이블이다.
- ③ 1000BASE-LX는 단파장의 광케이블을 사용한다.
- ④ 100BASE-FX는 100Mbps의 전송속도에 전송매체는 광케이블이다.

**정답**: ③

**해설**: 
- **LX** = **Long wavelength (장파장)** 광케이블
- **SX** = Short wavelength (단파장) 광케이블

**관련 문서**: [[network-standards#🔗 이더넷 매체 표기법]]

---

## Q8. Cell Relay (ATM)

**문제**: ATM으로 더 많이 알려져 있으며, 53Byte의 고정 길이 패킷을 이용하여 순서대로 자료를 전송하는 방식이다.
- ① Cell Relay
- ② Frame Relay
- ③ FDDI
- ④ X.25

**정답**: ① Cell Relay

**해설**: ATM = Cell Relay, 53바이트 고정 길이 셀 사용

**관련 문서**: [[network-standards#📦 WAN 기술]]

---

## Q9. T568B 배선 순서

**문제**: 다음 중 일반적인 이더넷 연결에 사용하는 T568B의 배열 순서로 알맞은 것은?
- ① 흰녹, 녹, 흰주, 파, 흰파, 주, 흰갈, 갈
- ② 흰주, 주, 흰녹, 파, 흰파, 녹, 흰갈, 갈
- ③ 흰주, 주, 흰녹, 녹, 흰파, 파, 흰갈, 갈
- ④ 흰녹, 녹, 흰파, 파, 흰주, 주, 흰갈, 갈

**정답**: ② 흰주, 주, 흰녹, 파, 흰파, 녹, 흰갈, 갈

**해설**: T568B: 흰주→주→흰녹→파→흰파→녹→흰갈→갈

**관련 문서**: [[network-standards#🔌 UTP 케이블 배선 (T568B)]]

---

## Q11. OSI 데이터 링크 계층 장비

**문제**: OSI 모델의 데이터 링크 계층에 있는 여러 개의 네트워크 세그먼트를 연결해주는 장치로 특정 네트워크에 오는 트래픽을 관리하는 장치이다.
- ① Repeater
- ② Bridge
- ③ Router
- ④ HUB

**정답**: ② Bridge

**해설**: 
- L1 (물리): Repeater, Hub
- **L2 (데이터링크): Bridge**, Switch
- L3 (네트워크): Router

**관련 문서**: [[network-standards#📡 네트워크 장비]]

---

## Q12. 가장 많은 OSI 계층 지원 장비

**문제**: 다음 중 OSI 모델 기준으로 가장 많은 계층을 지원하는 장치로 알맞은 것은?
- ① Repeater
- ② Bridge
- ③ Router
- ④ HUB

**정답**: ③ Router

**해설**: Router는 L3까지 지원 (L1~L3)

**관련 문서**: [[network-standards#📡 네트워크 장비]]

---

## Q16. OSI 참조 모델 제정 기관

**문제**: 다음 중 OSI 참조 모델을 제정한 기관으로 알맞은 것은?
- ① ISO
- ② IEEE
- ③ EIA
- ④ ITU-T

**정답**: ① ISO

**해설**: OSI = ISO에서 제정. IEEE는 LAN 표준(802.x)

**관련 문서**: [[network-fundamentals#🌍 국제 표준 기구]]

---

## Q17. IEEE와 EIA

**문제**: ( ㄱ ): LAN 및 MAN 관련 표준 제정 / ( ㄴ ): RS-232C, UTP 케이블 표준 규격
- ① ㄱ ISO ㄴ IEEE
- ② ㄱ IEEE ㄴ EIA
- ③ ㄱ EIA ㄴ IEEE
- ④ ㄱ IEEE ㄴ ISO

**정답**: ② ㄱ IEEE ㄴ EIA

**해설**: 
- IEEE: LAN/MAN 표준 (802.x)
- EIA: 케이블 규격 (RS-232C, UTP)

**관련 문서**: [[network-fundamentals#🌍 국제 표준 기구]]

---

## Q18. ITU-T

**문제**: 전기 통신의 개선과 효율적인 사용을 위해 국제 협력을 증진하고, 전기 통신의 능률 향상, 이용 증대 및 보급을 위해 만들어진 정부간 국제기구이다.
- ① ISO
- ② IEEE
- ③ EIA
- ④ ITU-T

**정답**: ④ ITU-T

**해설**: ITU-T = 국제전기통신연합 (정부간 기구)

**관련 문서**: [[network-fundamentals#🌍 국제 표준 기구]]

---

# 🖥️ X Window System

---

## Q21. XCB 라이브러리

**문제**: 다음 중 xlib를 대체하기 위해 등장한 것으로 향상된 쓰레드 기능을 지원하고 확장성이 뛰어난 라이브러리로 알맞은 것은?
- ① Xt
- ② XCB
- ③ Xm
- ④ Xaw

**정답**: ② XCB

**해설**: XCB = Xlib 대체, 멀티쓰레드 지원, 확장성 우수

**관련 문서**: [[x-window-system#📚 X 라이브러리]]

---

## Q23. UDP와 관련된 프로토콜

**문제**: 다음 중 UDP 프로토콜과 가장 밀접한 관계가 있는 프로토콜로 알맞은 것은?
- ① HTTP
- ② MAIL
- ③ FTP
- ④ DNS

**정답**: ④ DNS

**해설**: DNS는 주로 UDP 53번 포트 사용 (빠른 조회 필요)

**관련 문서**: [[network-fundamentals#주요 프로토콜-포트 매핑]]

---

## Q24. Display Manager

**문제**: 다음 X 윈도의 구성요소 중에 사용자 로그인 및 세션 관리 역할을 수행하는 것으로 알맞은 것은?
- ① 디스플레이 매니저
- ② 데스크톱 환경
- ③ 윈도 매니저
- ④ 유저 인터페이스

**정답**: ① 디스플레이 매니저

**해설**: Display Manager = 로그인/세션 관리 (GDM, SDDM, LightDM)

**관련 문서**: [[x-window-system#Display Manager (디스플레이 매니저)]]

---

## Q27. KDE의 윈도 매니저

**문제**: 다음 중 KDE에 대한 설명으로 틀린 것은?
- ① 데스크톱 환경의 일종이다.
- ② Qt 라이브러리를 기반으로 만들어졌다.
- ③ 리눅스뿐만 아니라, FreeBSD, Solaris, OS X 등도 지원한다.
- ④ Metacity라는 윈도 매니저를 사용한다.

**정답**: ④

**해설**: 
- KDE → **KWin** (윈도 매니저)
- GNOME → Metacity/Mutter

**관련 문서**: [[x-window-system#Window Manager (윈도 매니저)]]

---

## Q28. GNOME 설명

**문제**: 다음 중 GNOME에 대한 설명으로 틀린 것은?
- ① 대표적인 윈도 매니저이다.
- ② GPL 및 LGPL 라이선스를 따른다.
- ③ GNU 프로젝트를 통해 만들어졌다.
- ④ GTK+라는 라이브러리를 기반으로 만들어졌다.

**정답**: ①

**해설**: GNOME은 **데스크탑 환경(DE)**, 윈도 매니저가 아님

**관련 문서**: [[x-window-system#GNOME]]

---

## Q29. GNOME과 관련 없는 것

**문제**: 다음 중 GNOME과 가장 관련이 없는 것으로 알맞은 것은?
- ① nautilus
- ② XFce
- ③ metacity
- ④ Mutter

**정답**: ② XFce

**해설**: XFce는 별개의 데스크탑 환경

**관련 문서**: [[x-window-system#🖼️ 데스크탑 환경 (Desktop Environment)]]

---

## Q30. 윈도 매니저 vs 데스크탑 환경

**문제**: 다음 중 나머지 셋과 종류가 틀린 것은?
- ① GNOME
- ② KWin
- ③ KDE
- ④ XFce

**정답**: ②

**해설**: 
- **KWin**: 윈도 매니저
- GNOME, KDE, XFce: 데스크탑 환경

**관련 문서**: [[x-window-system#Window Manager (윈도 매니저)]]

---

## Q31. GNOME 윈도 매니저 변화

**문제**: GNOME 2 버전까지는 (ㄱ)라는 윈도 매니저를 사용하였고, GNOME 3 버전부터는 (ㄴ)라는 윈도 매니저를 사용한다.
- ① ㄱ nautilus ㄴ metacity
- ② ㄱ metacity ㄴ Mutter
- ③ ㄱ nautilus ㄴ Mutter
- ④ ㄱ metacity ㄴ nautilus

**정답**: ② ㄱ metacity ㄴ Mutter

**해설**: GNOME 2: Metacity → GNOME 3: Mutter

**관련 문서**: [[x-window-system#GNOME]]

---

## Q33. 윈도 매니저 종류

**문제**: 다음 중 윈도 매니저 종류로 틀린 것은?
- ① Metacity
- ② Window Maker
- ③ Enlightenment
- ④ XFce

**정답**: ④ XFce

**해설**: XFce는 **데스크탑 환경**

**관련 문서**: [[x-window-system#Window Manager (윈도 매니저)]]

---

## Q34. DISPLAY 환경변수

**문제**: 다음 중 X 클라이언트를 원격지로 전송하기 위해 변경하는 환경변수로 알맞은 것은?
- ① VISUAL
- ② XTERM
- ③ DISPLAY
- ④ TERM

**정답**: ③ DISPLAY

**해설**: `export DISPLAY=원격IP:0.0`

**관련 문서**: [[x-window-system#DISPLAY 환경변수]]

---

## Q35. xhost 명령

**문제**: 다음 중 X 서버에 접근하는 192.168.12.22번 IP 주소의 X 클라이언트를 허가하려고 할 때 알맞은 것은?
- ① xhost + 192.168.12.22
- ② xhost - 192.168.12.22
- ③ xhost +a 192.168.12.22
- ④ xhost add 192.168.12.22

**정답**: ① xhost + 192.168.12.22

**해설**: `xhost +` = 허가, `xhost -` = 해제

**관련 문서**: [[x-window-system#xhost - 호스트 기반 접근 제어]]

---

## Q36. xauth

**문제**: 원격지에서 접속하는 X 클라이언트를 허가할 때 IP주소나 호스트명이 아닌 X윈도 실행 시에 생성되는 키값으로 인증할 때 사용한다.
- ① xhost
- ② xauth
- ③ xmodmap
- ④ xwininfo

**정답**: ② xauth

**해설**: xauth = 키 기반 인증

**관련 문서**: [[x-window-system#xauth - 키 기반 인증]]

---

## Q37. .Xauthority 파일

**문제**: 다음 중 사용자가 X 윈도 실행 시에 관련 키 정보를 저장하는 파일로 알맞은 것은?
- ① .Xsession
- ② .xinitrc
- ③ .Xsetup
- ④ .Xauthority

**정답**: ④ .Xauthority

**해설**: ~/.Xauthority에 X 윈도 키 정보 저장

**관련 문서**: [[x-window-system#xauth - 키 기반 인증]]

---

## Q38. 이미지 뷰어

**문제**: 다음 중 이미지 뷰어 프로그램으로 가장 거리가 먼 것은?
- ① GIMP
- ② Totem
- ③ ImageMagick
- ④ eog

**정답**: ② Totem

**해설**: **Totem = 동영상 플레이어** (이미지 뷰어 아님)

**관련 문서**: [[x-window-system#📷 GUI 응용 프로그램]]

---

## Q39. PDF 뷰어

**문제**: 다음 중 PDF 문서를 볼 때 사용하는 프로그램으로 알맞은 것은?
- ① GIMP
- ② eog
- ③ totem
- ④ evince

**정답**: ④ evince

**해설**: evince = GNOME PDF 뷰어

**관련 문서**: [[x-window-system#📷 GUI 응용 프로그램]]

---

# 🐚 Shell

---

## Q44. /etc/shells

**문제**: 다음 중 사용가능한 셀의 목록을 확인할 수 있는 파일로 알맞은 것은?
- ① /etc/shell
- ② /etc/shells
- ③ /etc/profile
- ④ /etc/bashrc

**정답**: ② /etc/shells

**해설**: `/etc/shells` = 사용 가능한 셸 목록

**관련 문서**: [[shell-types#/etc/shells - 사용 가능한 셸 목록]]

---

## Q45. history 명령

**문제**: 다음 중 최근에 실행한 명령 목록을 확인할 수 있는 명령으로 알맞은 것은?
- ① alias
- ② chsh
- ③ history
- ④ set

**정답**: ③ history

**해설**: history = 실행 명령 이력 확인

**관련 문서**: [[shell-environment-commands#history 명령]]

---

## Q46. !! (마지막 명령)

**문제**: 다음 중 가장 마지막에 실행한 명령을 호출하는 방법으로 알맞은 것은?
- ① ??
- ② !!
- ③ !?
- ④ !1

**정답**: ② !!

**해설**: `!!` = 마지막 명령 재실행

**관련 문서**: [[shell-types#📝 히스토리 확장 (History Expansion)]]

---

## Q47. !?pattern?

**문제**: 다음 중 가장 최근에 실행한 명령 중에 'al'이라는 문자열을 포함하는 명령을 실행하기 위한 방법으로 알맞은 것은?
- ① !?al?
- ② !*al*
- ③ !!al!
- ④ !^al^

**정답**: ① !?al?

**해설**: `!?string?` = string 포함 최근 명령 실행

**관련 문서**: [[shell-types#📝 히스토리 확장 (History Expansion)]]

---

## Q48. HISTSIZE

**문제**: 다음 중 히스토리에 저장되는 명령의 개수를 제한할 때 사용하는 환경변수로 알맞은 것은?
- ① HISTFILE
- ② HISTFILESIZE
- ③ HISTSIZE
- ④ HISTORYSIZE

**정답**: ③ HISTSIZE

**해설**: HISTSIZE = 메모리에 저장할 명령 수

**관련 문서**: [[shell-environment-commands#히스토리 설정]]

---

## Q49. .bash_profile

**문제**: 다음 중 bash에서 개인 사용자의 환경변수와 시작 프로그램 관련 설정 시에 사용하는 파일로 가장 알맞은 것은?
- ① .profile
- ② .bash_profile
- ③ .bashrc
- ④ .bash_logout

**정답**: ② .bash_profile

**해설**: .bash_profile = 로그인 셸 환경 설정

**관련 문서**: [[shell-types#📂 셸 설정 파일]]

---

## Q50. /etc/bashrc

**문제**: 다음 중 bash에서 모든 사용자에게 적용되는 alias와 함수를 설정할 때 사용하는 파일로 가장 알맞은 것은?
- ① /etc/profile
- ② /etc/bashrc
- ③ /etc/bash_profile
- ④ /etc/shells

**정답**: ② /etc/bashrc

**해설**: /etc/bashrc = 전역 alias, function 설정

**관련 문서**: [[shell-types#📂 셸 설정 파일]]

---

## Q54. 백슬래시 용도

**문제**: 다음 중 셸에서 '\(Backslash)'의 사용에 대한 설명으로 틀린 것은?
- ① alias가 설정된 ls 명령 대신에 원래의 ls 명령을 호출할 때 사용한다.
- ② $PATH라는 문자열을 그대로 출력하기 위해 사용한다.
- ③ 여러 디렉터리를 분리할 때 분리자로 사용한다.
- ④ 명령어가 긴 경우에 다음 줄로 연장할 때 사용한다.

**정답**: ③

**해설**: 리눅스 디렉터리 분리자는 `/` (슬래시)

**관련 문서**: [[shell-scripting]]

---

## Q55. $0, $1 위치 매개변수

**문제**: 
```bash
[posein@www ~]$ cat test.sh
#!/bin/bash
echo "$0"
echo "$1"
[posein@www ~]$ ./test.sh lin joon
( ㄱ )
( ㄴ )
```
- ① ㄱ ./test.sh ㄴ lin
- ② ㄱ lin ㄴ joon
- ③ ㄱ joon ㄴ lin
- ④ ㄱ ./test.sh ㄴ joon

**정답**: ① ㄱ ./test.sh ㄴ lin

**해설**: 
- $0 = 스크립트 이름
- $1 = 첫 번째 인자

**관련 문서**: [[shell-scripting]]

---

## Q71. 현재 셸 확인 방법

**문제**: 다음 중 사용자가 로그인한 직후에 부여된 셀을 확인하는 방법으로 틀린 것은?
- ① ps 명령을 실행해서 확인해본다.
- ② 'chsh -l' 명령을 실행해서 확인해본다.
- ③ 'echo $SHELL' 명령을 실행해서 확인해본다.
- ④ 'grep 본인계정명 /etc/passwd' 명령을 실행해서 확인해본다.

**정답**: ②

**해설**: `chsh -l` = 사용 가능한 셸 **목록** 출력 (현재 셸이 아님)

**관련 문서**: [[shell-types#chsh - 기본 셸 변경]]

---

## Q72. 가장 오래된 셸

**문제**: 다음 중 가장 오래된 셀로 알맞은 것은?
- ① csh
- ② ksh
- ③ bash
- ④ bourne shell

**정답**: ④ bourne shell

**해설**: Bourne Shell (1977) = 가장 오래된 셸

**관련 문서**: [[shell-types#📜 셸의 역사 및 종류]]

---

## Q73. C Shell

**문제**: 1978년 버클리 대학의 빌 조이가 개발한 것으로 히스토리 기능, alias 기능, 작업 제어 등의 유용한 기능을 포함시켰다.
- ① bash
- ② csh
- ③ tcsh
- ④ ksh

**정답**: ② csh

**해설**: csh = Bill Joy, 버클리 대학, 1978년

**관련 문서**: [[shell-types#C Shell (csh)]]

---

## Q74. 셸 목록 확인

**문제**: 다음 중 사용 가능한 셀의 목록을 확인하는 명령으로 알맞은 것은?
- ① echo /etc/shells
- ② echo $SHELL
- ③ cat $SHELL
- ④ cat /etc/shells

**정답**: ④ cat /etc/shells

**해설**: `$SHELL`은 현재 셸만 출력

**관련 문서**: [[shell-types#/etc/shells - 사용 가능한 셸 목록]]

---

## Q76. 가장 최근 셸

**문제**: 다음 중 가장 최근에 등장한 셀로 알맞은 것은?
- ① csh
- ② ksh
- ③ tcsh
- ④ bash

**정답**: ④ bash

**해설**: bash (1989) = 가장 최근 (ksh=1983)

**관련 문서**: [[shell-types#📜 셸의 역사 및 종류]]

---

## Q77. Bash 설명

**문제**: 브라이언 폭스가 GNU 프로젝트를 위해 개발한 셀로 현재 GNU 운영체제, 리눅스, Mac OS X 등에 사용되고 있다.
- ① bash
- ② dash
- ③ tcsh
- ④ ksh

**정답**: ① bash

**해설**: Bash = Brian Fox, GNU 프로젝트

**관련 문서**: [[shell-types#Bash (Bourne Again Shell)]]

---

## Q78. 시스템 계정 셸

**문제**: 다음 중 시스템 계정에 설정되는 셀로 알맞은 것은?
- ① /bin/bash
- ② /bin/dash
- ③ /bin/tcsh
- ④ /sbin/nologin

**정답**: ④ /sbin/nologin

**해설**: 시스템 계정은 로그인 불가 셸 설정

**관련 문서**: [[shell-types#/sbin/nologin - 로그인 불가 셸]]

---

## Q79. set vs env

**문제**: 다음 중 셀에서 선언된 셀 변수 전부를 확인할 때 사용하는 명령으로 알맞은 것은?
- ① set
- ② env
- ③ chsh
- ④ export

**정답**: ① set

**해설**: 
- set = 셸 변수 + 환경 변수 전부
- env = 환경 변수만

**관련 문서**: [[shell-types#🔧 셸 변수 vs 환경 변수]]

---

## Q81. $USER 환경변수

**문제**: 
```
[posein@www ~]$ user=lin
[posein@www ~]$ echo $USER
```
- ① lin
- ② posein
- ③ $USER
- ④ 화면에 아무것도 출력되지 않는다.

**정답**: ② posein

**해설**: `user=lin`은 셸 변수. `$USER`는 시스템 환경변수 (영향 없음)

**관련 문서**: [[shell-types#🔧 셸 변수 vs 환경 변수]]

---

## Q82. TMOUT

**문제**: 사용자가 로그인한 후 일정시간 동안 작업을 하지 않을 경우에 로그아웃 시키려고 한다.
- ① EXIT
- ② TMOUT
- ③ LOGOUT
- ④ USEROUT

**정답**: ② TMOUT

**해설**: TMOUT = 자동 로그아웃 시간 (초)

**관련 문서**: [[shell-types#⏰ TMOUT 환경 변수]]

---

## Q83. PS1

**문제**: 
- 변경 전: `[posein@www ~]$`
- 변경 후: `[posein@21:05:12 ~]$`

- ① PS1
- ② PS2
- ③ DISPLAY
- ④ PROMPT

**정답**: ① PS1

**해설**: PS1 = 프롬프트 형식. `\t` = 시간

**관련 문서**: [[shell-environment-commands#PS1 프롬프트]]

---

## Q84. .bashrc 설정

**문제**: 다음 중 특정 사용자의 ~/.bashrc 파일에 설정하는 항목으로 가장 알맞은 것은?
- ① 프롬프트와 function
- ② alias와 프롬프트
- ③ alias와 function
- ④ 프롬프트와 PATH

**정답**: ③ alias와 function

**해설**: .bashrc = alias, function 설정

**관련 문서**: [[shell-types#📂 셸 설정 파일]]

---

## Q87. !5 (히스토리 확장)

**문제**: `[posein@www ~]$ !5`
- ① 최근에 실행한 마지막 5개의 명령어 목록을 출력한다.
- ② 히스토리 명령 목록의 번호 중에서 5번에 해당하는 명령을 실행한다.
- ③ 히스토리 명령 목록에서 5만큼 거슬러 올라가서 해당 명령을 실행한다.
- ④ 히스토리 명령 목록에서 번호가 1번부터 5번에 해당하는 명령을 출력한다.

**정답**: ② 히스토리 명령 목록의 번호 중에서 5번에 해당하는 명령을 실행한다.

**해설**: `!n` = n번째 히스토리 명령 실행

**관련 문서**: [[shell-types#📝 히스토리 확장 (History Expansion)]]

---

# 🔄 Process

---

## Q58. 프로세스 설명 (systemd PID)

**문제**: 다음 중 프로세스에 관한 설명으로 틀린 것은?
- ① 하나의 프로세스가 다른 프로세스를 실행하기 위한 방법에는 fork와 exec가 있다.
- ② 최초의 프로세스인 systemd는 PID 번호가 0이다.
- ③ inet방식은 항상 프로세스가 메모리에 상주하는 것이 아니라, 클라이언트의 서비스 요청이 있을 때 메모리에 상주한다.
- ④ 리눅스 부팅 시에 발생하는 프로세스는 fork 방식이다.

**정답**: ②

**해설**: systemd PID = **1** (0이 아님)

**관련 문서**: [[process-job-control-commands#fork vs exec]]

---

## Q59. fork vs exec

**문제**: 하나의 프로세스가 다른 프로세스를 실행하기 위한 시스템 호출방법에는 ( ㄱ )와 ( ㄴ )가 있다. ( ㄱ )는 새로운 프로세스를 위해 메모리를 할당받아 복사본 형태의 프로세스를 실행하는 형태로 기존의 프로세스는 그대로 실행되어 있다. ( ㄴ )는 원래의 프로세스를 새로운 프로세스로 대체하는 형태로 호출한 프로세스의 메모리에 새로운 프로세스의 코드를 덮어씌워 버린다.
- ① ㄱ exec ㄴ fork
- ② ㄱ fork ㄴ exec
- ③ ㄱ background ㄴ foreground
- ④ ㄱ foreground ㄴ background

**정답**: ②

**해설**: fork=복사, exec=덮어쓰기

**관련 문서**: [[process-job-control-commands#fork vs exec]]

---

## Q60. 백그라운드 특수기호

**문제**: 다음 중 백그라운드 프로세스와 가장 관련 있는 특수기호로 알맞은 것은?
- ① ?
- ② !
- ③ &
- ④ /

**정답**: ③ &

**해설**: `command &` = 백그라운드 실행

**관련 문서**: [[process-job-control-commands#Foreground/Background]]

---

## Q61. Ctrl+Z

**문제**: 다음 중 포어그라운드 프로세스를 백그라운드 프로세스로 전환할 때 사용하는 인터럽트 키 조합으로 알맞은 것은?
- ① [Ctrl]+[c]
- ② [Ctrl]+[d]
- ③ [Ctrl]+[W]
- ④ [Ctrl]+[z]

**정답**: ④ [Ctrl]+[z]

**해설**: Ctrl+Z = 일시 정지 (SIGTSTP), 이후 bg로 백그라운드 전환

**관련 문서**: [[process-job-control-commands#kill - Send Signal]]

---

## Q62. fg %2

**문제**: 다음 중 백그라운드로 실행중인 작업번호 2번인 프로세스를 포어그라운드로 전환할 때 알맞은 것은?
- ① bg 2
- ② bg %2
- ③ fg &2
- ④ fg %2

**정답**: ④ fg %2

**해설**: `fg %n` = n번 작업을 포어그라운드로

**관련 문서**: [[process-job-control-commands#Foreground/Background]]

---

## Q63. Ctrl+C (SIGINT)

**문제**: 다음 중 [Ctrl]+[c] 입력 시에 전송되는 시그널로 알맞은 것은?
- ① SIGHUP
- ② SIGTERM
- ③ SIGINT
- ④ SIGQUIT

**정답**: ③ SIGINT

**해설**: Ctrl+C = SIGINT (2)

**관련 문서**: [[process-job-control-commands#kill - Send Signal]]

---

## Q64. SIGQUIT

**문제**: 다음 중 [Ctrl]+[W] 입력 시에 전송되는 시그널로 알맞은 것은? (Ctrl+\를 의도)
- ① SIGHUP
- ② SIGTERM
- ③ SIGINT
- ④ SIGQUIT

**정답**: ④ SIGQUIT

**해설**: Ctrl+\ = SIGQUIT (3)

**관련 문서**: [[process-job-control-commands#kill - Send Signal]]

---

## Q65. standalone vs inet

**문제**: 지속적인 서비스 요청을 처리하기 위해 사용하는 데몬 프로세스를 실행하는 방법에는 ( ㄱ )와 ( ㄴ )가 있다. ( ㄱ )은 보통 부팅시에 실행되어 해당 프로세스가 메모리에 계속 상주하면서 클라이언트의 서비스 요청을 처리하는 방식이다. ( ㄴ )는 프로세스가 항상 메모리에 상주하는 것이 아니라, 클라이언트의 서비스 요청이 들어왔을 때 관련 프로세스를 실행시키고 접속 종료 후에는 자동으로 프로세스를 종료시킨다.
- ① ㄱ exec ㄴ fork
- ② ㄱ fork ㄴ exec
- ③ ㄱ inet ㄴ standalone
- ④ ㄱ standalone ㄴ inet

**정답**: ④ ㄱ standalone ㄴ inet

**해설**: standalone=상주, inet=요청시만

**관련 문서**: [[process-job-control-commands#🔄 데몬 실행 방식]]

---

## Q66. SIGKILL (9)

**문제**: 다음 중 사용자 로그인 프로세스와 같이 쉽게 종료되지 않는 프로세스를 강제 종료할 때 사용되는 시그널번호로 알맞은 것은?
- ① 1
- ② 9
- ③ 15
- ④ 19

**정답**: ② 9

**해설**: SIGKILL (9) = 강제 종료

**관련 문서**: [[process-job-control-commands#kill - Send Signal]]

---

# ⚙️ systemd

---

## Q67. systemctl stop

**문제**: 다음 중 실행 상태인 sshd 데몬을 중지시키는 명령으로 알맞은 것은?
- ① systemctl stop sshd
- ② systemctl sshd stop
- ③ systemctl disable sshd
- ④ systemctl sshd disable

**정답**: ① systemctl stop sshd

**해설**: 
- stop = 즉시 중지
- disable = 부팅 시 자동시작 해제

**관련 문서**: [[systemd#Service (서비스)]]

---

## Q68. systemctl status

**문제**: 다음 중 sshd 데몬의 실행 여부를 확인하는 명령으로 알맞은 것은?
- ① systemctl sshd ps
- ② systemctl sshd status
- ③ systemctl ps sshd
- ④ systemctl status sshd

**정답**: ④ systemctl status sshd

**해설**: `systemctl status 서비스명`

**관련 문서**: [[systemd]]

---

## Q69. /lib/systemd/system

**문제**: 다음 중 시스템에서 사용되는 service 및 target 유닛 파일을 확인할 수 있는 디렉터리로 알맞은 것은?
- ① /usr/systemd/system
- ② /run/systemd/system
- ③ /var/systemd/system
- ④ /lib/systemd/system

**정답**: ④ /lib/systemd/system

**해설**: /lib/systemd/system 또는 /usr/lib/systemd/system

**관련 문서**: [[systemd#Unit 파일]]

---

## Q70. hostnamectl

**문제**: 다음 결과에 해당하는 명령으로 알맞은 것은?
```
Static hostname: www
Icon name: computer-vm
...
Operating System: CentOS Linux 7 (Core)
```
- ① systemctl
- ② machinectl
- ③ hostnamectl
- ④ journalctl

**정답**: ③ hostnamectl

**해설**: hostnamectl = 호스트 정보 확인

**관련 문서**: [[systemd]]

---

# 🌐 네트워크 설정

---

## Q28 (네트워크). /etc/protocols

**문제**: 다음 중 프로토콜 및 프로토콜 번호를 확인할 수 있는 파일로 알맞은 것은?
- ① /etc/protocol
- ② /etc/protocols
- ③ /etc/service
- ④ /etc/services

**정답**: ② /etc/protocols

**해설**: protocols = 프로토콜 번호, services = 포트 번호

**관련 문서**: [[network-fundamentals#프로토콜 및 서비스 파일]]

---

## Q29 (네트워크). /etc/services

**문제**: 다음 중 프로토콜과 관련된 포트 번호를 확인할 수 있는 파일로 알맞은 것은?
- ① /etc/protocol
- ② /etc/protocols
- ③ /etc/service
- ④ /etc/services

**정답**: ④ /etc/services

**해설**: /etc/services = 포트 번호 매핑

**관련 문서**: [[network-fundamentals#프로토콜 및 서비스 파일]]

---

## Q31. 프로토콜-포트 조합

**문제**: 다음 중 프로토콜과 포트 번호의 조합으로 틀린 것은?
- ① FTP - 21
- ② SMTP - 53
- ③ SSH - 22
- ④ TELNET - 23

**정답**: ② SMTP - 53

**해설**: SMTP = **25**, DNS = 53

**관련 문서**: [[network-fundamentals#주요 프로토콜-포트 매핑]]

---

## Q32. B 클래스 IP

**문제**: 다음 중 B 클래스에 속한 IP 주소로 알맞은 것은?
- ① 126.34.22.12
- ② 10.22.123.44
- ③ 203.44.44.12
- ④ 191.128.3.12

**정답**: ④ 191.128.3.12

**해설**: B 클래스 = 128~191

**관련 문서**: [[network-fundamentals#IPv4 클래스 구분]]

---

## Q33. B 클래스 서브넷마스크

**문제**: 다음 중 B 클래스의 기본 서브넷마스크값으로 알맞은 것은?
- ① 255.0.0.0
- ② 255.255.0.0
- ③ 255.255.255.0
- ④ 255.255.255.255

**정답**: ② 255.255.0.0

**해설**: B 클래스 = /16 = 255.255.0.0

**관련 문서**: [[network-fundamentals#IPv4 클래스 구분]]

---

## Q34 (IP). 일반 목적 IP

**문제**: 다음 중 일반적인 목적으로 사용하는 IP 주소로 틀린 것은?
- ① 12.127.0.12
- ② 172.16.220.44
- ③ 223.105.8.9
- ④ 193.223.202.4

**정답**: ② (172.16.x.x = B 클래스 사설 IP)

**해설**: 172.16.0.0 ~ 172.31.255.255는 사설 IP 대역으로 인터넷 일반 목적 사용 불가

**관련 문서**: [[network-fundamentals#사설 IP 대역 (Private IP)]]

---

## Q35 (IP). 루프백 IP

**문제**: 다음 중 루프백(Loopback) IP 주소로 알맞은 것은?
- ① 10.0.0.1
- ② 127.0.0.1
- ③ 192.168.0.1
- ④ 172.16.0.1

**정답**: ② 127.0.0.1

**해설**: 127.0.0.1 = localhost

**관련 문서**: [[network-fundamentals#루프백 주소]]

---

## Q36 (IP). ICANN

**문제**: 다음 중 IP 주소 할당 및 도메인을 관리하는 국제기구?
- ① ISO
- ② IEEE
- ③ ICANN
- ④ ITU-T

**정답**: ③ ICANN

**해설**: ICANN = IP, 도메인 관리

**관련 문서**: [[network-fundamentals#🌍 국제 표준 기구]]

---

## Q37. /etc/hosts

**문제**: 다음 중 DNS의 탄생의 효시가 된 파일로 알맞은 것은?
- ① /etc/hosts
- ② /etc/protocols
- ③ /etc/services
- ④ /etc/host.conf

**정답**: ① /etc/hosts

**해설**: DNS 이전 호스트명 매핑

**관련 문서**: [[network-fundamentals#DNS 관련 파일]]

---

## Q39. IPv6

**문제**: 다음 중 IPv6에 대한 설명으로 틀린 것은?
- ① IPv4에 비해 헤더 구조가 복잡하다.
- ② 주소 표시 공간이 128비트이다.
- ③ 패킷 출처 인증과 데이터 무결성 보장이 가능하다.
- ④ IPv6 호스트는 네트워크 접속시에 자동으로 주소를 할당받는다.

**정답**: ①

**해설**: IPv6 = 헤더 **단순화** (복잡하지 않음)

**관련 문서**: [[network-fundamentals]]

---

## Q40. 루프백 인터페이스

**문제**: 다음 중 루프백 장치를 나타내는 파일명으로 알맞은 것은?
- ① lo
- ② lo0
- ③ eth
- ④ eth0

**정답**: ① lo

**해설**: 리눅스 = lo (BSD = lo0)

**관련 문서**: [[network-fundamentals#🖥️ 네트워크 인터페이스]]

---

## Q41. 호스트 수 계산

**문제**: C 클래스 IP 주소 대역, 서브넷마스크 255.255.255.0, **인터넷에 연결**시 사용가능한 호스트 IP 주소 개수?
- ① 256
- ② 254
- ③ 253
- ④ 252

**정답**: ③ 253

**해설**: 
- 전체: 256개 (2^8)
- 네트워크 주소: -1 (x.x.x.0)
- 브로드캐스트 주소: -1 (x.x.x.255)
- **게이트웨이 주소**: -1 (인터넷 연결 시 필요)
- **결과**: 256 - 3 = **253**

**관련 문서**: [[network-fundamentals#사용 가능한 호스트 수]]

---

## Q43. /etc/resolv.conf

**문제**: 다음 중 설정되어 있는 DNS 서버를 확인할 수 있는 파일로 알맞은 것은?
- ① /etc/hosts
- ② /etc/host.conf
- ③ /etc/resolv.conf
- ④ /etc/networks

**정답**: ③ /etc/resolv.conf

**해설**: DNS 서버 설정 = resolv.conf

**관련 문서**: [[network-fundamentals#DNS 관련 파일]]

---

## Q45. 네트워크 재시작 (틀린 것)

**문제**: 다음 중 네트워크 관련 설정 파일 변경 후 네트워크 데몬을 재시작하는 방법으로 틀린 것은?
- ① service network restart
- ② /etc/rc.d/init.d/network restart
- ③ /etc/network restart
- ④ /etc/init.d/network restart

**정답**: ③ /etc/network restart

**해설**: `/etc/network restart`는 없는 경로

**관련 문서**: [[network-configuration-files#🔄 네트워크 서비스 재시작]]

---

## Q46. route (게이트웨이)

**문제**: 다음 중 시스템에 설정되어 있는 게이트웨이 주소를 확인하기 위한 명령으로 알맞은 것은?
- ① ifconfig
- ② arp
- ③ mii-tool
- ④ route

**정답**: ④ route

**해설**: route = 라우팅 테이블/게이트웨이 확인

**관련 문서**: [[network-commands]]

---

## Q47. route 게이트웨이 설정

**문제**: 다음 중 게이트웨이 주소를 설정하는 방법으로 알맞은 것은?
- ① route default gw 192.168.3.254
- ② route -default gw 192.168.3.254
- ③ route add default gw 192.168.3.254
- ④ route -add default gw 192.168.3.254

**정답**: ③ route add default gw 192.168.3.254

**해설**: `route add default gw <IP>` 형식으로 게이트웨이 추가

**관련 문서**: [[network-commands]]

---

## netstat 옵션

**문제**: 모든 소켓의 PID 및 프로그램명을 출력하고, 호스트명 및 포트명은 숫자값으로 출력하려 할 때 다음 옵션은?
- (1) -ap, (2) -an, (3) -anp, (4) -aux

**정답**: (3) -anp

**해설**: 
- -a = all
- -n = numeric
- -p = PID/program

**관련 문서**: [[network-configuration-files]]

---

## netstat SYN_RECEIVED

**문제**: 서버시스템이 원격 클라이언트로부터 접속 요구를 받아 클라이언트에게 응답을 하였지만 아직 클라이언트에게 확인 메시지는 받지 않는 상태
- (1) SYS-SENT, (2) SYN_RECEIVED, (3) LISTEN, (4) ESTABLISHED

**정답**: (2) SYN_RECEIVED

**해설**: SYN+ACK 보낸 후 ACK 대기 상태

**관련 문서**: [[network-configuration-files#📊 netstat 상태값]]

---

## Q51. mii-tool

**문제**: `[root@www ~]$ ( ) eth0` → `eth0: no autonegotiation, 100baseTx-FD, link ok`
- (1) mii-tool, (2) ethtool, (3) ifconfig, (4) route

**정답**: (1) mii-tool

**해설**: mii-tool = 이더넷 링크 상태 확인 (레거시). `no autonegotiation` 출력은 mii-tool 특징.

**관련 문서**: [[network-configuration-files#mii-tool - 이더넷 링크 상태 (레거시)]]

---

## /etc/sysconfig/network

**문제**: 부팅 시에 네트워크 사용 유무를 지정하는 파일
- (1) /etc/network, (2) /etc/sysconfig/network, (3) /etc/resolv.conf, (4) /etc/networks

**정답**: (2) /etc/sysconfig/network

**해설**: NETWORKING=yes/no

**관련 문서**: [[network-configuration-files#/etc/sysconfig/network]]

---

## ifcfg-eth0

**문제**: 이더넷 카드를 하나만 장착한 시스템에서 IP 주소가 기록되는 파일
- (1) /etc/networks, (2) /etc/sysconfig/network, (3) /etc/sysconfig/network-scripts/ifcfg-eth0, (4) /etc/sysconfig/network-scripts/ifcfg-eth1

**정답**: (3) /etc/sysconfig/network-scripts/ifcfg-eth0

**해설**: 인터페이스별 IP 설정 파일

**관련 문서**: [[network-configuration-files#/etc/sysconfig/network-scripts/ifcfg-*]]

---

## ip 명령

**문제**: IP 주소 확인/등록/삭제, 인터페이스 활성/비활성, 라우팅 테이블 확인, 게이트웨이 설정/삭제
- (1) ifconfig, (2) ip, (3) route, (4) ethtool

**정답**: (2) ip

**해설**: ip = 통합 네트워크 명령

**관련 문서**: [[network-configuration-files#⚙️ ip 명령 (통합 도구)]]

---

## 서브넷 개수

**문제**: C 클래스, 넷마스크 255.255.255.192 → 서브네트워크 개수?
- (1) 4, (2) 64, (3) 128, (4) 192

**정답**: (1) 4

**해설**: /26 - /24 = 2비트 → 2^2 = 4개

**관련 문서**: [[network-fundamentals#서브네트워크 개수 계산]]

---

## 네트워크 주소 계산

**문제**: IP 192.168.3.129, 서브넷 255.255.255.128 → 네트워크 주소?
- (1) 192.168.3.0, (2) 192.168.3.126, (3) 192.168.3.127, (4) 192.168.3.128

**정답**: (4) 192.168.3.128

**해설**: /25 블록 크기=128, 129>128 → 192.168.3.128

**관련 문서**: [[network-fundamentals#네트워크 주소 계산]]

---

## B 클래스 사설 IP

**문제**: IPv4 B 클래스 사설 IP 범위?
- (1) 171.15.0.0 ~ 172.31.255.255
- (2) 171.15.0.0 ~ 172.32.255.255
- (3) 172.16.0.0 ~ 172.31.255.255
- (4) 172.16.0.0 ~ 172.32.255.255

**정답**: (3) 172.16.0.0 ~ 172.31.255.255

**해설**: B 클래스 사설 IP = 172.16~172.31

**관련 문서**: [[network-fundamentals#사설 IP 대역 (Private IP)]]

---

## IP 확인 명령

**문제**: 리눅스에서 IP 주소 확인 명령 조합?
- (1) ip, ifconfig, (2) ss, ifconfig, (3) ifconfig, ipconfig, (4) ip, ipconfig

**정답**: (1) ip, ifconfig

**해설**: ipconfig는 Windows 명령

**관련 문서**: [[network-commands]]

---

## ss 명령

**문제**: 서버에 접속한 클라이언트의 IP 및 포트 확인 명령?
- (1) ip, (2) ss, (3) arp, (4) route

**정답**: (2) ss

**해설**: ss = 소켓 상태 확인

**관련 문서**: [[network-commands]]

---

## tracepath

**문제**: ihd.or.kr 서버까지의 이동 경로 확인 명령?
- (1) ip, (2) ss, (3) route, (4) tracepath

**정답**: (4) tracepath

**해설**: tracepath = 경로 추적 (root 불필요)

**관련 문서**: [[network-commands#traceroute - Trace Route]]
