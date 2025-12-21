---
title: Shell Environment Commands
tags: [linux, commands, shell, bash, environment]
aliases: [쉘 명령어, Shell, Bash, 환경변수]
date modified: 2025-12-20 14:17:48 +09:00
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

### 주요 환경변수

```bash
# 시스템
$PATH                              # 실행 파일 검색 경로
$HOME                              # 홈 디렉토리
$USER                              # 사용자 이름
$SHELL                             # 현재 셸
$PWD                               # 현재 디렉토리
$OLDPWD                            # 이전 디렉토리
$HOSTNAME                          # 호스트명

# 로케일
$LANG                              # 언어 설정
$LC_ALL                            # 모든 로케일

# 프롬프트
$PS1                               # 기본 프롬프트
$PS2                               # 다음 줄 프롬프트 (>)
```

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

### 프롬프트 커스터마이징

```bash
# ~/.bashrc
# 기본
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

## 🔗 연결 문서 (Related Documents)

- [[file-operations-commands]] - 파일 작업
- [[process-job-control-commands]] - 프로세스 제어
- [[text-processing-commands]] - 텍스트 처리
