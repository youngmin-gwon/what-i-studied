---
title: Log Analysis Commands
tags: [linux, commands, logs, monitoring, security, audit]
aliases: [로그 분석, Log Files, utmp, wtmp, lastlog]
date modified: 2025-12-21 21:38:57 +09:00
date created: 2025-12-21 21:38:57 +09:00
---

## 🌐 개요 (Overview)

Linux 시스템 로그 파일 분석 명령어들입니다. 사용자 로그인 추적, 시스템 이벤트 분석, 보안 감사에 필수적입니다.

## 📋 Quick Reference

| 로그 파일 | 내용 | 명령어 |
|-----------|------|--------|
| `/var/run/utmp` | 현재 로그인 사용자 | `who`, `w`, `users` |
| `/var/log/wtmp` | 로그인 히스토리 | `last` |
| `/var/log/btmp` | 실패한 로그인 | `lastb` (root) |
| `/var/log/lastlog` | 마지막 로그인 시간 | `lastlog` |
| `/var/log/auth.log` | 인증 로그 | `grep`, `tail` |
| `/var/log/syslog` | 시스템 메시지 | `grep`, `tail` |

## 👥 사용자 로그 파일

### utmp - 현재 로그인 사용자

**파일**: `/var/run/utmp` (바이너리 파일)

**내용**: 현재 시스템에 로그인한 사용자 정보

#### who - 로그인 사용자 확인

```bash
# 기본 사용
who
# alice    pts/0        2025-12-21 10:30 (192.168.1.100)
# bob      tty1         2025-12-21 09:00

# 상세 정보
who -H                           # 헤더 포함
who -a                           # 모든 정보
who -q                           # 사용자 수만
who -b                           # 마지막 부팅 시간

# 특정 정보
who -u                           # 유휴 시간 포함
who -m                           # 현재 사용자만 (whoami와 유사)
```

#### w - 사용자 활동 확인

```bash
# 기본 사용 (더 상세함)
w
# USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
# alice    pts/0    192.168.1.100    10:30    1:05   0.20s  0.05s vim file.txt
# bob      tty1     -                09:00    2:30m  0.03s  0.03s -bash

# 옵션
w -h                             # 헤더 제거
w -s                             # 짧은 형식
w alice                          # 특정 사용자만
```

#### users - 사용자 목록만

```bash
users
# alice bob charlie
```

### wtmp - 로그인 히스토리

**파일**: `/var/log/wtmp` (바이너리 파일)

**내용**: 모든 로그인/로그아웃 기록, 시스템 재부팅

#### last - 로그인 히스토리

```bash
# 기본 사용
last
# alice    pts/0    192.168.1.100    Sun Dec 21 10:30   still logged in
# bob      pts/1    10.0.0.50        Sun Dec 21 09:15 - 12:30  (03:15)
# reboot   system boot  5.15.0        Sun Dec 21 08:00

# 옵션
last -n 10                       # 최근 10개
last -10                         # 동일

# 특정 사용자
last alice
last bob

# 특정 터미널
last pts/0
last tty1

# 시간 범위
last -s yesterday                # 어제부터
last -s 2025-12-20               # 특정 날짜부터
last -t 2025-12-21               # 특정 날짜까지
last -s "2025-12-20 09:00" -t "2025-12-21 18:00"

# 재부팅 기록
last reboot
last shutdown

# IP 주소 표시
last -i

# 전체 도메인명 표시
last -d
```

### btmp - 실패한 로그인 시도

**파일**: `/var/log/btmp` (바이너리 파일, root만 읽기)

**내용**: 실패한 로그인 시도 (보안 감사 중요!)

#### lastb - 실패한 로그인 확인

```bash
# 기본 사용 (root 권한 필요)
sudo lastb
# sshd     ssh:notty    192.168.1.200    Sun Dec 21 15:45 - 15:45  (00:00)
# admin    ssh:notty    10.0.0.100       Sun Dec 21 14:30 - 14:30  (00:00)

# 옵션
sudo lastb -n 20                 # 최근 20개
sudo lastb -s yesterday          # 어제부터
sudo lastb -i                    # IP 주소 표시

# 특정 사용자
sudo lastb root                  # root 로그인 시도

# IP별 집계
sudo lastb | awk '{print $3}' | sort | uniq -c | sort -rn
```

### lastlog - 마지막 로그인

**파일**: `/var/log/lastlog` (바이너리 파일)

**내용**: 각 사용자의 마지막 로그인 시간

#### lastlog - 마지막 로그인 확인

```bash
# 모든 사용자
lastlog
# Username         Port     From             Latest
# root             pts/0                     Sun Dec 21 08:00:00 +0900 2025
# alice            pts/1    192.168.1.100    Sun Dec 21 10:30:15 +0900 2025
# bob              tty1                      Sun Dec 21 09:00:00 +0900 2025
# charlie          **Never logged in**

# 특정 사용자
lastlog -u alice
lastlog -u root

# 특정 UID
lastlog -u 1000

# 최근 N일 이내 로그인
lastlog -t 7                     # 7일 이내

# 로그인한 적 없는 사용자
lastlog | grep "Never logged"
```

## 📝 시스템 로그 파일

### /var/log/auth.log (Debian/Ubuntu)

**내용**: 인증 관련 이벤트
- SSH 로그인/로그아웃
- sudo 사용
- 사용자 추가/삭제
- 패스워드 변경

```bash
# SSH 로그인 성공
grep "Accepted" /var/log/auth.log
grep "Accepted password" /var/log/auth.log

# SSH 로그인 실패
grep "Failed password" /var/log/auth.log
grep "authentication failure" /var/log/auth.log

# sudo 사용
grep "sudo" /var/log/auth.log
grep "sudo.*COMMAND" /var/log/auth.log

# 특정 사용자
grep "alice" /var/log/auth.log

# 실시간 모니터링
tail -f /var/log/auth.log

# IP별 실패 횟수
grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -rn
```

### /var/log/secure (RHEL/CentOS)

auth.log와 동일한 역할 (RHEL/CentOS에서 사용)

```bash
# RHEL/CentOS
grep "Failed password" /var/log/secure
tail -f /var/log/secure
```

### /var/log/syslog (Debian) / /var/log/messages (RHEL)

**내용**: 일반 시스템 메시지, 데몬 로그

```bash
# 에러 검색
grep -i "error" /var/log/syslog
grep -i "fail" /var/log/syslog

# 특정 서비스
grep "nginx" /var/log/syslog
grep "systemd" /var/log/syslog

# 시간대별 검색
grep "Dec 21 15:" /var/log/syslog

# 실시간
tail -f /var/log/syslog
```

### /var/log/kern.log

**내용**: 커널 메시지

```bash
grep -i "error" /var/log/kern.log
grep "USB" /var/log/kern.log
tail -f /var/log/kern.log
```

## 🔄 로그 로테이션

### logrotate 설정

**설정 파일**:
- `/etc/logrotate.conf` (전역 설정)
- `/etc/logrotate.d/*` (서비스별 설정)

**예시**: `/etc/logrotate.d/rsyslog`

```bash
/var/log/syslog
{
    rotate 7                    # 7개 보관
    daily                       # 매일 순환
    missingok                   # 파일 없어도 에러 안냄
    notifempty                  # 비어있으면 순환 안함
    compress                    # 압축
    delaycompress               # 다음 순환 때 압축
    postrotate
        /usr/lib/rsyslog/rsyslog-rotate
    endscript
}
```

**로그 파일 네이밍**:
```
/var/log/syslog           # 현재
/var/log/syslog.1         # 어제
/var/log/syslog.2.gz      # 그제 (압축)
/var/log/syslog.3.gz      # ...
```

**수동 실행**:
```bash
# 모든 로그 순환
logrotate /etc/logrotate.conf

# 디버그 모드 (실제 실행 안함)
logrotate -d /etc/logrotate.conf

# 강제 실행
logrotate -f /etc/logrotate.conf

# 특정 설정만
logrotate /etc/logrotate.d/nginx
```

## 🔍 고급 로그 분석

### 압축된 로그 검색

```bash
# zgrep - 압축 파일에서 grep
zgrep "error" /var/log/syslog.*.gz

# zcat - 압축 해제하여 출력
zcat /var/log/syslog.2.gz | grep "error"

# 모든 로그 통합 검색
zgrep "Failed password" /var/log/auth.log*
```

### 시간대별 분석

```bash
# 오늘
grep "$(date +%b\ %d)" /var/log/syslog

# 어제
date=$(date -d "yesterday" +%b\ %d)
grep "$date" /var/log/syslog

# 특정 시간대 (15:00-16:00)
grep "Dec 21 15:" /var/log/syslog
```

### 통계 분석

```bash
# IP별 로그인 시도 횟수
grep "Failed password" /var/log/auth.log | \
  awk '{print $(NF-3)}' | sort | uniq -c | sort -rn | head -10

# 사용자별 sudo 사용 횟수
grep "sudo.*COMMAND" /var/log/auth.log | \
  awk '{print $6}' | sort | uniq -c | sort -rn

# 시간대별 에러 발생 횟수
grep "error" /var/log/syslog | \
  awk '{print $3}' | cut -d: -f1 | sort | uniq -c
```

## 💡 실무 시나리오

### 시나리오 1: 보안 감사 - 무차별 대입 공격 탐지

```bash
# 1. 실패한 SSH 로그인 확인
sudo lastb -n 100

# 2. IP별 실패 횟수 집계
sudo lastb | awk '{print $3}' | grep -E '^[0-9]' | \
  sort | uniq -c | sort -rn | head -10
# 50 192.168.1.200
# 30 10.0.0.150
# 15 172.16.0.100

# 3. auth.log에서 상세 확인
grep "192.168.1.200" /var/log/auth.log | grep "Failed"

# 4. 패턴 분석
grep "Failed password" /var/log/auth.log | \
  grep "192.168.1.200" | head -5

# 5. 대응: 방화벽 차단
sudo iptables -A INPUT -s 192.168.1.200 -j DROP
```

### 시나리오 2: 사용자 활동 추적

```bash
# 1. 특정 사용자의 최근 로그인
last alice -n 20

# 2. 현재 접속 중인지 확인
who | grep alice

# 3. 무엇을 하고 있는지 확인
w alice

# 4. sudo 사용 이력
grep "alice.*sudo" /var/log/auth.log | tail -20

# 5. 마지막 로그인
lastlog -u alice
```

### 시나리오 3: 시스템 문제 진단

```bash
# 1. 최근 재부팅 기록
last reboot -n 5

# 2. 재부팅 전 시스템 로그
last_reboot=$(last reboot | head -1 | awk '{print $6" "$7" "$8}')
grep -B 100 "shutdown" /var/log/syslog

# 3. 커널 패닉 확인
grep -i "panic" /var/log/kern.log
grep -i "oops" /var/log/kern.log

# 4. 메모리 부족 확인
grep -i "out of memory" /var/log/syslog
grep "OOM killer" /var/log/kern.log

# 5. 디스크 문제 확인
grep -i "I/O error" /var/log/syslog
grep -i "disk" /var/log/kern.log
```

### 시나리오 4: 정기 보안 점검

```bash
#!/bin/bash
# 일간 보안 점검 스크립트

echo "=== 보안 점검 리포트 $(date) ==="

echo -e "\n1. 실패한 로그인 시도 (상위 10개 IP)"
sudo lastb -s yesterday | awk '{print $3}' | \
  grep -E '^[0-9]' | sort | uniq -c | sort -rn | head -10

echo -e "\n2. root 로그인 시도"
grep "root" /var/log/auth.log | grep "Failed" | \
  grep "$(date +%b\ %d)" | wc -l

echo -e "\n3. 새로운 sudo 사용자"
grep "sudo" /var/log/auth.log | grep "$(date +%b\ %d)" | \
  awk '{print $6}' | sort -u

echo -e "\n4. 비정상 시간대 로그인 (00:00-05:00)"
grep "Accepted" /var/log/auth.log | grep "$(date +%b\ %d)" | \
  awk '{if($3 >= "00:00:00" && $3 <= "05:00:00") print}'

echo -e "\n5. 로그인 성공/실패 통계"
success=$(grep "Accepted password" /var/log/auth.log | \
  grep "$(date +%b\ %d)" | wc -l)
failed=$(grep "Failed password" /var/log/auth.log | \
  grep "$(date +%b\ %d)" | wc -l)
echo "성공: $success, 실패: $failed"
```

## 🛡️ 보안 Best Practices

### 로그 보안

```bash
# 1. 로그 파일 권한 확인
ls -l /var/log/auth.log
ls -l /var/log/btmp
# -rw-r----- root adm     (640)
# -rw------- root utmp    (600)

# 2. 로그 무결성 확인
debsums -c rsyslog  # Debian
rpm -V rsyslog      # RHEL

# 3. 원격 로그 서버 설정 (rsyslog)
# /etc/rsyslog.conf
*.* @@remote-log-server:514
```

### 로그 모니터링 자동화

```bash
# fail2ban 설치
sudo apt install fail2ban      # Debian
sudo yum install fail2ban      # RHEL

# 설정: /etc/fail2ban/jail.local
[sshd]
enabled = true
maxretry = 3
bantime = 3600
findtime = 600
```

## 🔗 연결 문서 (Related Documents)

- [[service-management-commands]] - journalctl (systemd 로그)
- [[system-monitoring-commands]] - dmesg (커널 로그)
- [[security-commands]] - auditd (보안 감사)
- [[user-permission-commands]] - 사용자 관리
- [[network-commands]] - 네트워크 연결 로그
