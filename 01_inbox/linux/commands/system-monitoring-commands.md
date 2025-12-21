---
title: System Monitoring Commands
tags: [linux, commands, monitoring, performance, ps, top]
aliases: [시스템 모니터링, Monitoring, ps, top, free]
date modified: 2025-12-20 13:59:24 +09:00
date created: 2025-12-20 13:59:24 +09:00
---

## 🌐 개요 (Overview)

시스템과 리소스를 모니터링하는 명령어들입니다. CPU, 메모리, 디스크, [[process-states-lifecycle|프로세스]] 상태를 실시간으로 확인할 수 있습니다.

## 📋 Quick Reference

| 명령어 | 용도 |
|--------|------|
| `ps` | 프로세스 목록 |
| `top`/`htop` | 실시간 프로세스 모니터링 |
| `free` | 메모리 사용량 |
| `df` | 디스크 사용량 |
| `du` | 디렉토리 크기 |
| `uptime` | 가동 시간, 로드 |
| `lsof` | 열린 파일 |
| `vmstat` | 가상 메모리 통계 |
| `iostat` | I/O 통계 |

## 🖥️ Process Monitoring

### ps - Process Status

```bash
ps                      # 현재 셸의 프로세스
ps aux                  # 모든 프로세스 (BSD 스타일)
ps -ef                  # 모든 프로세스 (Unix 스타일)
ps -eLf                 # 스레드 포함

# 정렬
ps aux --sort=-%cpu     # CPU 사용률 내림차순
ps aux --sort=-%mem     # 메모리 사용률
ps aux --sort=-rss      # RSS(메모리) 내림차순

# 필터링
ps -u username          # 특정 사용자
ps -C httpd             # 명령어 이름
ps -p 1234              # PID
ps axjf                  # 트리 형태

# 커스텀 출력
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu
```

### top - Real-time Monitor

```bash
top                     # 실시간 모니터
top -u username         # 특정 사용자만
top -p 1234,5678        # 특정 PID

# 인터랙티브 키
M       # 메모리 사용률 순
P       # CPU 사용률 순
T       # 실행 시간 순
k       # 프로세스 종료
r       # Nice 값 변경
1       # CPU 코어별 표시
```

### htop - Enhanced top

```bash
htop                    # 더 나은 UI
# F2: 설정, F3: 검색, F4: 필터, F9: 종료
```

## 💾 Memory Monitoring

### free - Memory Usage

```bash
free -h                 # Human-readable
free -m                 # MB
free -s 1               # 1초마다 갱신

# available = 실제 사용 가능한 메모리
```

### vmstat - Virtual Memory Statistics

```bash
vmstat 1 5              # 1초 간격, 5회
vmstat -s               # 메모리 통계
vmstat -d               # 디스크 통계
```

## 💿 Disk Monitoring

### df - Disk Free

```bash
df -h                   # 파일시스템 사용량
df -i                   # inode 사용량
df -T                   # 파일시스템 타입
df -h /var              # 특정 마운트
```

### du - Disk Usage

```bash
du -sh directory/       # 전체 크기
du -h --max-depth=1     # 1레벨만
du -ah directory/       # 모든 파일
du -sh * | sort -h      # 크기 순정렬

# 큰 디렉토리 찾기 (10GB 이상)
du -h --max-depth=1 /var | grep [0-9]G
```

### iostat - I/O Statistics

```bash
iostat                  # I/O 통계
iostat -x 1 5           # 확장, 1초, 5회
iostat -d               # 디스크만
```

## 🔍 System Information

### uname - System Info

```bash
uname -a                # 모든 정보
uname -r                # 커널 버전
uname -m                # 아키텍처
```

### uptime - System Uptime

```bash
uptime
# 출력: 14:30:00 up 10 days, load average: 0.15, 0.20, 0.18
# 로드: 1분, 5분, 15분 평균
```

### lscpu - CPU Info

```bash
lscpu                   # CPU 정보
nproc                   # CPU 코어 수
```

### lsblk - Block Devices

```bash
lsblk                   # 블록 디바이스
lsblk -f                # 파일시스템 포함
```

## 📂 Open Files

### lsof - List Open Files

```bash
lsof                    # 모든 열린 파일
lsof -p 1234            # PID의 파일
lsof -u username        # 사용자의 파일
lsof /path/to/file      # 파일 사용 프로세스
lsof -i :80             # 포트 80 사용
lsof -i TCP:22          # SSH 연결
lsof -c httpd           # httpd 프로세스의 파일
```

## 📊 Logs

### journalctl - systemd Logs

```bash
journalctl                          # 전체 로그
journalctl -f                       # 실시간
journalctl -u apache2               # 서비스
journalctl --since "1 hour ago"
journalctl -p err                   # 에러만
journalctl -b                       # 현재 부팅
```

### dmesg - Kernel Messages

```bash
dmesg                   # 커널 메시지
dmesg | tail            # 최근 메시지
dmesg -T                # 타임스탬프
dmesg -l err            # 에러만
dmesg -w                # 실시간
```

## 💡 Real-World Scenarios

### CPU 사용률 높은 프로세스 찾기

```bash
ps aux --sort=-%cpu | head -10
top # 그다음 P 키
```

### 메모리 많이 쓰는 프로세스

```bash
ps aux --sort=-%mem | head -10
```

### 디스크 공간 부족 조사

```bash
df -h                   # 전체 확인
du -sh /* 2>/dev/null | sort -h  # 큰 디렉토리
find / -type f -size +100M  # 큰 파일
```

### 포트 사용 프로세스 확인

```bash
lsof -i :80
netstat -tulpn | grep :80
ss -tulpn | grep :80
```

## 🔗 연결 문서 (Related Documents)

- [[process-states-lifecycle]] - 프로세스 개념
- [[signals]] - 프로세스 제어
- [[file-operations-commands]] - 파일 작업
