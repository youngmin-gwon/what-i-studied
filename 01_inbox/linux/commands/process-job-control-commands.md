---
title: Process and Job Control Commands
tags: [linux, commands, process, job, kill, nice]
aliases: [프로세스 제어, kill, nice, jobs]
date modified: 2025-12-20 13:59:24 +09:00
date created: 2025-12-20 13:59:24 +09:00
---

## 🌐 개요 (Overview)

[[process-states-lifecycle|프로세스]] 제어, [[signals|시그널]], 작업 관리 명령어들입니다.

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

## 🎯 Process Control

### kill - Send Signal

**주요 시그널**:

| 시그널 | 번호 | 의미 |
|--------|------|------|
| SIGTERM | 15 | 정상 종료 (기본) |
| SIGKILL | 9 | 강제 종료 |
| SIGHUP | 1 | 재시작 |
| SIGSTOP | 19 | 일시정지 |
| SIGCONT | 18 | 계속 |

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

# 형식: 분 시 일 월 요일 명령
# * * * * * command
# 0 2 * * * /path/to/backup.sh     # 매일 2:00
# 0 0 * * 0 /path/to/weekly.sh     # 매주 일요일 0:00
# */5 * * * * /path/to/check.sh    # 5분마다
```

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

- [[process-states-lifecycle]] - 프로세스 개념
- [[signals]] - 시그널 상세
- [[system-monitoring-commands]] - 프로세스 모니터링
