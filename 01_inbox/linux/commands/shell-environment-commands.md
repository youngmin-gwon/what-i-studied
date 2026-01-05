---
title: shell-environment-commands
tags: [bash, commands, environment, linux, shell]
aliases: [Bash, Shell, 쉘 명령어, 환경변수]
date modified: 2025-12-28 22:25:38 +09:00
date created: 2025-12-20 14:17:48 +09:00
---

## 🌐 개요 (Overview)

Bash 쉘 환경 설정과 유틸리티 명령어들입니다. 별칭, 히스토리, 환경변수 등을 다룹니다.

## 📋 Quick Reference

| 명령어 | 용도 |
|--------|------|
| `alias` | 별칭 설정 |
| `history` | 명령어 히스토리 |
| `env`/`export` | 환경변수 |
| `source`/`.` | 스크립트 실행 |
| `echo` | 출력 |
| `type`/`which` | 명령어 타입 확인 |

## 🐚 셸의 종류 및 특징 (Shell Types)

| 종류 | 특징 |
| :--- | :--- |
| **Bourne Shell (sh)** | 유닉스의 표준 셸. 모든 POSIX 호환 셸의 기초. |
| **bash** | GNU 표준 셸. 명령 히스토리, 별칭, 탭 완성 등 강력한 기능 제공. |
| **C Shell (csh/tcsh)** | C 언어와 유사한 문법. 히스토리, 작업 제어 중심. |
| **Korn Shell (ksh)** | Bourne 셸을 기반으로 C 셸의 기능을 흡수한 고성능 셸. |
| **dash** | 가벼운 Bourne 셸 구현체. 성능 중심(스크립트 실행 속도가 빠름). |

### 🏗️ 셸 환경 설정 로드 순서 (Loading Order)

사용자가 로그인할 때 셸은 다음 순서로 설정 파일을 읽어들입니다:

1. `/etc/profile` (전체 설정)
2. `~/.bash_profile`, `~/.bash_login`, `~/.profile` 중 먼저 존재하는 하나 (개별 설정)
3. `$HOME/.bashrc` (인터랙티브 셸인 경우)

> [!TIP]
> 상세한 로딩 시퀀스와 **로그인 셸 vs 비로그인 셸**의 차이점은 [[09-environment-startup]] 가이드를 참조하세요.

> [!NOTE]
> **명령어 우선순위**: 1 순위: **Alias** > 2 순위: **내부 명령어(Builtin)** > 3 순위: **함수(Function)** > 4 순위: **외부 명령어($PATH 경로)**

## 🔖 Alias - 명령어 별칭

### 별칭 생성

```bash
# 기본 사용
alias ll='ls -alh'
alias la='ls -A'
alias l='ls -CF'

# 자주 사용하는 별칭
alias ..='cd ..'
alias ...='cd ../..'
alias grep='grep --color=auto'
alias df='df -h'
alias du='du -h'
alias free='free -h'

# 안전 옵션
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Git 단축키
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git log --oneline'
```

### 별칭 관리

```bash
# 현재 별칭 목록
alias

# 특정 별칭 확인
alias ll

# 별칭 제거
unalias ll
unalias -a                         # 모든 별칭 제거
```

### 영구 별칭 설정

```bash
# ~/.bashrc 또는 ~/.bash_aliases에 추가
echo "alias ll='ls -alh'" >> ~/.bashrc
source ~/.bashrc

# 또는 ~/.bash_aliases 파일 생성
cat << 'EOF' >> ~/.bash_aliases
# 파일 조작
alias ll='ls -alh'
alias la='ls -A'

# 디렉토리 이동
alias ..='cd ..'
alias ...='cd ../..'

# Git
alias gs='git status'
alias ga='git add'
EOF

# ~/.bashrc에서 로드 (보통 기본으로 있음)
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```

## 📜 History - 명령어 히스토리

### 기본 사용

```bash
# 히스토리 보기
history

# 최근 N개
history 10
history 20

# 히스토리 파일 위치
echo $HISTFILE
# ~/.bash_history
```

### 히스토리 재실행

```bash
# 명령어 재실행
!!                                 # 직전 명령
!100                               # 100번 명령
!-2                                # 2개 전 명령

# 패턴으로 재실행
!git                               # 'git'으로 시작하는 최근 명령
!?commit                           # 'commit'을 포함하는 최근 명령

# 인수만 가져오기
!$                                 # 직전 명령의 마지막 인수
!^                                 # 직전 명령의 첫 인수
!*                                 # 직전 명령의 모든 인수
```

### 히스토리 편집

```bash
# 히스토리에서 제거
history -d 100                     # 100번 삭제

# 히스토리 지우기
history -c                         # 메모리 히스토리 삭제
> ~/.bash_history                  # 파일도 삭제
```

### 히스토리 설정

```bash
# ~/.bashrc에 추가
export HISTSIZE=10000              # 메모리에 저장할 명령어 수
export HISTFILESIZE=20000          # 파일에 저장할 명령어 수
export HISTCONTROL=ignoredups:erasedups  # 중복 무시
export HISTIGNORE="ls:cd:pwd:exit:clear"  # 특정 명령 무시
export HISTTIMEFORMAT="%F %T "     # 타임스탬프 포함

# 즉시 히스토리 저장
shopt -s histappend                # 덮어쓰기 대신 추가
PROMPT_COMMAND="history -a"        # 명령 실행 후 즉시 저장
```

### 히스토리 검색

```bash
# Ctrl+R: 역방향 검색
# 입력 후 Ctrl+R로 검색
# Enter로 실행, Ctrl+G로 취소

# fzf와 함께 사용 (설치 필요)
history | fzf
```

## 🌍 Environment Variables - 환경변수

### 환경변수 확인

```bash
# 모든 환경변수
env
printenv

# 특정 변수
echo $PATH
echo $HOME
echo $USER
echo $SHELL

# 변수 목록 (지역 변수 포함)
set

# export된 변수만
export -p
```

### 변수 설정

```bash
# 지역 변수 (현재 셸만)
NAME="value"

# 환경변수 (자식 프로세스로 전달)
export NAME="value"
export PATH="/usr/local/bin:$PATH"

# 한 줄로
NAME="value" command

# 변수 제거
unset NAME
```

### 주요 환경변수 상세

| 변수 (Variable) | 설명 (Description) | 용도 및 특징 |
| :--- | :--- | :--- |
| **`$HOME`** | 사용자의 홈 디렉터리 경로 | `cd` 입력 시 이동하는 기본 위치 |
| **`$PATH`** | 실행 파일 검색 경로 목록 | `:` 으로 구분된 디렉터리 리스트 |
| **`$USER`** / **`$UID`** | 사용자 이름 및 고유 ID | 현재 로그인 계정 식별 |
| **`$SHELL`** | 현재 로그인 셸 경로 | 기본 셸 환경 확인 (`/bin/bash` 등) |
| **`$PWD`** / **`$OLDPWD`** | 현재 및 이전 작업 경로 | 디렉터리 이동 추적 |
| **`$HOSTNAME`** | 시스템의 호스트 이름 | 네트워크 상의 장치 식별자 |
| **`$LANG`** / **`$LC_ALL`** | 시스템 언어 및 로케일 설정 | 정렬 순서, 시간 형식, 인코딩 제어 |
| **`$PS1`** / **`$PS2`** | 셸 프롬프트 모양 정의 | 1 차(기본) 및 2 차(미완성 시) 프롬프트 |
| **`$HISTSIZE`** | 히스토리 스택 크기 | 메모리에 유지할 명령어 개수 |
| **`$TMOUT`** | 자동 로그아웃 시간 | 보안을 위한 유휴 시간 설정 (초 단위) |
| **`$DISPLAY`** | X 윈도 출력 대상 | GUI 프로그램이 표시될 화면 지정 |
| **`$LD_LIBRARY_PATH`** | 공유 라이브러리 검색 경로 | 동적 라이브러리(`*.so`) 로드 시 참조 |

### PATH 관리

```bash
# PATH 확인
echo $PATH

# PATH 추가 (앞)
export PATH="/new/path:$PATH"

# PATH 추가 (뒤)
export PATH="$PATH:/new/path"

# 영구 설정 (~/.bashrc)
echo 'export PATH="/opt/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

## 📂 Source & Scripts

### source / . (점)

```bash
# 스크립트를 현재 셸에서 실행
source ~/.bashrc
. ~/.bashrc                        # 동일

# 새 셸에서 실행 (변수 전달 안됨)
bash script.sh
./script.sh                        # 실행 권한 필요
```

**차이점**:
```bash
# script.sh: VAR=hello

# 1. 실행
./script.sh
echo $VAR                          # (비어있음)

# 2. source
source script.sh
echo $VAR                          # hello
```

## 📤 Echo & Printf

### echo

```bash
# 기본 출력
echo "Hello, World!"
echo Hello World                   # 따옴표 생략 가능

# 변수 출력
echo $PATH
echo "User: $USER"

# 옵션
echo -n "No newline"               # 줄바꿈 없음
echo -e "Line1\nLine2"             # 이스케이프 해석

# 리다이렉션
echo "text" > file.txt
echo "append" >> file.txt

> [!TIP]
> **표준 스트림(FD 0, 1, 2)**과 **히어독(Here-doc)** 등 상세한 데이터 흐름 제어는 [[06-io-redirection]] 가이드를 참조하세요.
```

### printf

```bash
# 포맷 지정
printf "Name: %s, Age: %d\n" "Alice" 30
printf "%.2f\n" 3.14159            # 3.14

# 왼쪽/오른쪽 정렬
printf "%-10s %10s\n" "Left" "Right"

# 테이블 형식
printf "%-15s %-10s %5s\n" "Name" "City" "Age"
printf "%-15s %-10s %5d\n" "Alice" "Seoul" 30
```

## 🔍 Command Type - 명령어 타입 확인

### type

```bash
# 명령어 타입 확인
type ls                            # ls is aliased to `ls --color=auto'
type cd                            # cd is a shell builtin
type python                        # python is /usr/bin/python

# 모든 위치
type -a python

# 타입만
type -t ls                         # alias
type -t cd                         # builtin
```

### which

```bash
# 실행 파일 경로
which python
which -a python                    # 모든 경로
```

### whereis

```bash
# 바이너리, 소스, 매뉴얼 위치
whereis ls
whereis -b ls                      # 바이너리만
whereis -m ls                      # 매뉴얼만
```

## 💡 실무 팁

### 프롬프트 구성 요소 (PS1 특수 문자)

| 코드                  | 설명                           | 예시                       |
| :------------------ | :--------------------------- | :----------------------- |
| **`\u`**            | 현재 사용자 이름                    | `root`, `user`           |
| **`\h`** / **`\H`** | 호스트 이름 (단축 / 전체)             | `myhost`, `myhost.local` |
| **`\w`** / **`\W`** | 작업 디렉터리 (절대 경로 / 마지막 폴더)     | `/etc/nginx`, `nginx`    |
| **`\d`**            | 날짜 표시 (요일 월 일)               | `Wed Jan 15`             |
| **`\t`** / **`\T`** | 24 시 / 12 시 형태의 시간           | `23:59:59`, `11:59:59`   |
| **`\@`**            | 12 시 형태 시간 + AM/PM           | `11:59 PM`               |
| **`\s`**            | 현재 사용 중인 셸 이름                | `bash`                   |
| **`\!`**            | 히스토리 번호                      | `501`                    |
| **`\$`**            | 사용자 구분 (root 면 `#`, 아니면 `$`) | `$`                      |
| **`\n`**            | 줄바꿈 (New line)               | 프롬프트를 2 줄로 구성 시 사용       |

### 프롬프트 설정 예시

```bash
# 기본 형태
PS1='\u@\h:\w\$ '

# 컬러
PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

# Git branch 표시
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
PS1='\u@\h:\w\[\033[32m\]$(parse_git_branch)\[\033[00m\]\$ '
```

### 유용한 함수

```bash
# ~/.bashrc에 추가

# 디렉토리 생성 후 이동
mkcd() {
    mkdir -p "$1" && cd "$1"
}

# 파일 백업
backup() {
    cp "$1" "$1.bak.$(date +%Y%m%d_%H%M%S)"
}

# 프로세스 찾기
psgrep() {
    ps aux | grep -v grep | grep -i -e VSZ -e "$1"
}

# 포트 확인
port() {
    lsof -i :"$1"
}
```

### .bashrc vs .bash_profile

```
.bash_profile: 로그인 셸 (SSH 접속 시)
.bashrc: 인터랙티브 셸 (터미널 열 때)

권장: .bash_profile에서 .bashrc 로드
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi
```

### 📢 시스템 배너 및 로그 정보 (Banners & MOTD)

시스템 로그인 시 사용자에게 메시지를 전달하는 설정 파일들입니다.

| 파일 경로 | 시점 | 용도 및 특징 |
| :--- | :--- | :--- |
| **`/etc/motd`** | **로그인 직후** | Message Of The Day. 로그인 성공 후 사용자에게 공지사항 전달 |
| **`/etc/issue`** | **로그인 전** | 로컬 터미널에서 로그인 프롬프트 위에 메시지 출력 |
| **`/etc/issue.net`** | **로그인 전** | 원격(SSH, Telnet) 접속 시 로그인 프롬프트 위에 메시지 출력 |

> [!TIP]
> `/etc/issue` 파일에는 `\n` (호스트명), `\l` (TTY 번호), `\t` (현재시간) 등의 이스케이프 문자를 사용하여 동적인 정보를 표시할 수 있습니다.

## 🖥️ 가상 콘솔 및 터미널 조작 (Virtual Console & Terminal Interaction)

Linux 시스템은 GUI 환경이 없더라도 여러 개의 **가상 콘솔(Virtual Console)**을 제공하여 동시에 여러 작업을 수행할 수 있게 해줍니다.

### 가상 콘솔 (TTY)

가상 콘솔은 `tty1`, `tty2` 등으로 불리며, 물리적인 모니터와 키보드 하나를 여러 개의 논리적인 단말로 나누어 사용하는 개념입니다.

*   **가상 콘솔 전환**: `Ctrl` + `Alt` + `F1` ~ `F6`
    *   보당 `F1`~`F6`은 텍스트 모드 기반의 가상 콘솔(TTY)입니다.
    *   커널 수준에서 제공하므로 GUI가 멈추었을 때 시스템을 복구하거나 로그를 확인하는 용도로 자주 사용됩니다.
*   **GUI 환경 복귀**: 보통 `Ctrl` + `Alt` + `F1` 혹은 `F7` (배포판마다 다를 수 있음)

### 화면 스크롤 및 지나간 작업 확인 (Scrollback)

텍스트 모드 기반의 가상 콘솔(Virtual Console) 환경에서는 마우스를 사용할 수 없으므로, 화면 위로 지나가버린 출력 결과를 확인하기 위해 다음 키 조합을 사용합니다.

| 작업 | 키 조합 (Key Combination) | 설명 |
| :--- | :--- | :--- |
| **화면 위로 스크롤** | **`Shift` + `Page Up`** | 이전에 출력된 내용을 보기 위해 위로 한 화면씩 이동 |
| **화면 아래로 스크롤** | **`Shift` + `Page Down`** | 다시 최근 출력 내용으로 내려오기 위해 아래로 이동 |

> [!IMPORTANT]
> **터미널 에뮬레이터와의 차이**:
> *   GNOME Terminal, iTerm2, VS Code 터미널 같은 **GUI 터미널 에뮬레이터**에서는 소프트웨어가 자체적으로 스크롤 기능을 제공하므로 마우스 휠이나 `Cmd/Ctrl + Up/Down` 등을 사용합니다.
> *   하지만 리눅스마스터 시험 등에서 묻는 **"텍스트 모드 기반 가상 콘솔"** 환경은 커널의 콘솔 드라이버가 직접 제어하는 환경을 의미하므로 반드시 **`Shift` + `Page Up/Down`**을 사용해야 합니다.

### 유용한 터미널 제어 단축키 (Terminal Shortcuts)

터미널이나 셸에서 작업 생산성을 높여주는 필수 단축키들입니다.

| 단축키 | 기능 |
| :--- | :--- |
| **`Ctrl` + `L`** | 화면 깨끗이 지우기 (`clear` 명령어와 동일) |
| **`Ctrl` + `U`** | 커서 이전의 텍스트 모두 삭제 |
| **`Ctrl` + `K`** | 커서 이후의 텍스트 모두 삭제 |
| **`Ctrl` + `A`** | 커서를 라인 맨 앞으로 이동 |
| **`Ctrl` + `E`** | 커서를 라인 맨 뒤로 이동 |
| **`Ctrl` + `W`** | 커서 왼쪽의 단어 하나 삭제 |
| **`Ctrl` + `C`** | 현재 실행 중인 프로세스 강제 종료 (SIGINT) |
| **`Ctrl` + `D`** | 셸 종료 (EOF 입력) 또는 로그아웃 |
| **`Ctrl` + `Z`** | 현재 프로세스를 백그라운드로 일시 중지 (SIGTSTP) |

## 🔗 연결 문서 (Related Documents)

- [[shell-scripting]] - 통합 셸 스크립팅 가이드 (상세)
- [[file-operations-commands]] - 파일 작업
- [[process-job-control-commands]] - 프로세스 제어
- [[text-processing-commands]] - 텍스트 처리
