---
title: Process and Job Control Commands
tags: [linux, commands, process, job, kill, nice, fork, exec, daemon]
aliases: [프로세스 제어, kill, nice, jobs, fork, exec]
date modified: 2026-01-06 21:50:00 +09:00
date created: 2025-12-20 13:59:24 +09:00
---

## 🌐 개요 (Overview)

[프로세스](../../operating-systems/process-states-lifecycle.md) 제어, [시그널](../../operating-systems/signals.md), 작업 관리 명령어들입니다.

## 📋 Quick Reference

| 명령어 | 용도 |
|--------|------|
| `kill` | 시그널 전송 |
| `killall` | 이름으로 종료 |
| `pkill` | 패턴으로 종료 |
| `nice` | 우선순위로 실행 |
| `renice` | 우선순위 변경 |
| `jobs` | 작업 목록 |
| `fg`/`bg` | 포그라운드/백그라운드 |
| `nohup` | 터미널 종료 후에도 실행 |

---

## 🔀 프로세스 생성 방식

### fork vs exec

| 방식 | 설명 | 원래 프로세스 |
| :--- | :--- | :--- |
| **fork** | 새 메모리 할당, **복사본** 생성 | 유지됨 |
| **exec** | 원래 프로세스를 **덮어씀** | 종료됨 |

- **fork**: 부모 프로세스의 복제본을 생성. 부모 프로세스는 그대로 실행됨
- **exec**: 현재 프로세스의 메모리에 새 코드를 덮어씀. 원래 프로세스는 사라짐

> [!IMPORTANT]
> **시험 포인트**: 리눅스 부팅 시 프로세스는 **fork 방식**으로 생성됩니다.
> systemd(PID **1**)가 최초 프로세스입니다. (PID 0이 아님!)

---

## 🔄 데몬 실행 방식

| 방식 | 설명 | 메모리 |
| :--- | :--- | :--- |
| **standalone** | 부팅 시 실행, 항상 메모리 상주 | 항상 사용 |
| **inet (inetd/xinetd)** | 요청 시에만 실행, 접속 종료 후 종료 | 절약 |

- **standalone**: 항상 대기 (httpd, sshd 등)
- **inet**: 슈퍼 데몬이 연결 받아 실제 데몬 시작

---

## 🎯 Process Control

### kill - Send Signal

**주요 시그널**:

| 시그널 | 번호 | 의미 | 키보드 |
|--------|------|------|--------|
| SIGHUP | 1 | 재시작/설정 리로드 | - |
| **SIGINT** | **2** | 인터럽트 | **Ctrl+C** |
| **SIGQUIT** | **3** | 종료 + 코어 덤프 | **Ctrl+\\** |
| SIGKILL | 9 | **강제 종료** (무시 불가) | - |
| SIGTERM | 15 | 정상 종료 (기본) | - |
| SIGTSTP | 20 | 일시 정지 | **Ctrl+Z** |
| SIGSTOP | 19 | 일시정지 (무시 불가) | - |
| SIGCONT | 18 | 계속 | - |

> [!TIP]
> **키보드 단축키**:
> - **Ctrl+C**: SIGINT (인터럽트, 종료)
> - **Ctrl+Z**: SIGTSTP (일시 정지 → bg/fg로 제어)
> - **Ctrl+\\**: SIGQUIT (종료 + 코어 덤프)

```bash
kill PID                   # SIGTERM (15)
kill -9 PID                # SIGKILL (강제)
kill -15 PID               # SIGTERM
kill -HUP PID              # SIGHUP
kill -STOP PID             # 일시정지
kill -CONT PID             # 계속

# 시그널 목록
kill -l
```

### killall - Kill by Name

```bash
killall process_name
killall -9 firefox
killall -u username        # 사용자의 모든 프로세스
killall -i process_name    # 확인하며 종료
```

### pkill - Kill by Pattern

```bash
pkill process_name
pkill -9 firefox
pkill -u username
pkill -f pattern           # 명령줄 패턴
```

## ⚖️ Process Priority

### nice - Run with Priority

``` 
Nice 값: -20 (highest) ~ 19 (lowest)
기본값: 0
일반 사용자: 0~19만 가능
```

```bash
nice -n 10 ./process       # Nice +10
nice -n -5 ./process       # Nice -5 (root만)
nice --10 ./process        # +10
```

### renice - Change Priority

```bash
renice 10 -p PID           # PID의 nice 변경
renice 10 -u username      # 사용자의 모든 프로세스
renice -5 -p 1234          # -5로 (root)
```

## 🔄 Job Control

### Foreground/Background

```bash
./long_process &           # 백그라운드로 실행
# [1] 1234

# 실행 중 프로세스
Ctrl+Z                     # 일시정지 (SIGTSTP)
bg                         # 백그라운드로
fg                         # 포그라운드로

jobs                       # 작업 목록
jobs -l                    # PID 포함

fg %1                      # 1번 작업을 포그라운드로
bg %2                      # 2번 작업을 백그라운드로
kill %1                    # 1번 작업 종료
```

### nohup - No Hangup

```bash
nohup ./process &          # 터미널 종료 후에도 실행
# 출력: nohup.out

nohup ./process > output.log 2>&1 &
```

### disown - Detach from Shell

```bash
./process &
disown                     # 현재 셸에서 분리
disown %1                  # 1번 작업 분리
disown -a                  # 모든 작업 분리
```

## ⏰ Scheduling

### at - One-time Execution

```bash
at 10:00                   # 10:00에 실행
at> command
at> Ctrl+D

at now + 1 hour
at 10:00 tomorrow
at 10:00 2025-12-31

# 목록
atq

# 삭제
atrm job_number
```

### cron - Periodic Execution

```bash
crontab -e                 # 편집
crontab -l                 # 목록
crontab -r                 # 삭제
crontab -u username -e     # 다른 사용자 (root만)
```

**crontab 형식**:

```
분 시 일 월 요일 명령
*  *  *  *  *    command
│  │  │  │  └── 요일 (0-7, 0과 7은 일요일, 또는 Sun-Sat)
│  │  │  └───── 월 (1-12 또는 Jan-Dec)
│  │  └──────── 일 (1-31)
│  └─────────── 시 (0-23)
└────────────── 분 (0-59)
```

**특수 문자**:

| 문자 | 의미 | 예시 |
| :--- | :--- | :--- |
| `*` | 모든 값 | `* * * * *` = 매분 |
| `,` | 여러 값 | `0,30 * * * *` = 매시 0분, 30분 |
| `-` | 범위 | `0 9-17 * * *` = 9시~17시 정각 |
| `/` | 간격 | `*/5 * * * *` = 5분마다 |

**자주 사용되는 패턴**:

```bash
# 매일 새벽 2시
0 2 * * *   /path/to/backup.sh

# 매주 일요일 0시
0 0 * * 0   /path/to/weekly.sh

# 매주 월~금 9시
0 9 * * 1-5 /path/to/work.sh

# 5분마다
*/5 * * * * /path/to/check.sh

# 매월 1일 0시
0 0 1 * *   /path/to/monthly.sh

# 매년 1월 1일 0시
0 0 1 1 *   /path/to/yearly.sh
```

> [!IMPORTANT]
> **시험 Tip**: crontab 필드 순서는 **분-시-일-월-요일** (작은 단위부터). 요일에서 0과 7은 둘 다 일요일입니다.

## 💡 Scenarios

### 응답 없는 프로세스 종료

```bash
# 1. SIGTERM 시도
kill PID

# 2. 응답 없으면 SIGKILL
kill -9 PID
```

### 백그라운드 실행

```bash
# 방법 1: nohup
nohup ./process > /dev/null 2>&1 &

# 방법 2: screen/tmux
screen -dmS mysession ./process
tmux new -d -s mysession './process'
```

### CPU 사용률 제한

```bash
# Nice로 낮은 우선순위
nice -n 19 ./cpu_intensive_process

# 실행 중인 프로세스
renice 19 -p PID
```

## 🔗 연결 문서 (Related Documents)

- [process-states-lifecycle](../../operating-systems/process-states-lifecycle.md) - 프로세스 개념
- [signals](../../operating-systems/signals.md) - 시그널 상세
- [system-monitoring-commands](system-monitoring-commands.md) - 프로세스 모니터링
