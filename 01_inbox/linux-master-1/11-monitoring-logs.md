# 시스템 모니터링 및 로그

## 1. 시스템 정보 확인

### 1.1 시스템 정보

**uname** - 시스템 정보:
```bash
uname -a                # 모든 정보
uname -s                # 커널 이름 (Linux)
uname -r                # 커널 릴리스
uname -v                # 커널 버전
uname -m                # 머신 아키텍처 (x86_64)
uname -p                # 프로세서 타입
uname -o                # 운영체제
```

**hostname** - 호스트명:
```bash
hostname                # 호스트명
hostname -f             # FQDN
hostname -i             # IP 주소
hostnamectl             # 상세 정보 (systemd)
hostnamectl set-hostname newname  # 호스트명 변경
```

**시스템 파일**:
```bash
cat /etc/os-release     # OS 정보
cat /etc/redhat-release # RHEL 버전
cat /etc/debian_version # Debian 버전
lsb_release -a          # LSB 정보
```

### 1.2 하드웨어 정보

**CPU**:
```bash
lscpu                   # CPU 정보
cat /proc/cpuinfo       # 상세 CPU 정보
nproc                   # CPU 코어 수
```

**메모리**:
```bash
free -h                 # 메모리 사용량 (human-readable)
free -m                 # MB 단위
cat /proc/meminfo       # 상세 메모리 정보
```

**디스크**:
```bash
lsblk                   # 블록 디바이스
lsblk -f                # 파일시스템 포함
fdisk -l                # 파티션 정보
blkid                   # UUID 및 파일시스템 타입
```

**PCI 디바이스**:
```bash
lspci                   # PCI 디바이스
lspci -v                # 상세 정보
lspci -k                # 커널 드라이버
```

**USB 디바이스**:
```bash
lsusb                   # USB 디바이스
lsusb -v                # 상세 정보
```

**기타**:
```bash
dmidecode               # DMI/SMBIOS 정보 (root)
dmidecode -t system     # 시스템 정보
dmidecode -t memory     # 메모리 정보
dmidecode -t processor  # 프로세서 정보
```

## 2. 리소스 모니터링

### 2.1 CPU 모니터링

**top/htop**:
```bash
top                     # 실시간 프로세스 모니터링
htop                    # 향상된 top
```

**mpstat** (sysstat 패키지):
```bash
mpstat                  # CPU 통계
mpstat -P ALL           # 모든 CPU
mpstat 1 5              # 1초 간격, 5회
```

**uptime**:
```bash
uptime                  # 가동 시간 및 부하
# 출력: 12:00:00 up 10 days, 2:30, 3 users, load average: 0.15, 0.20, 0.18
```

**로드 평균**:
- 1분, 5분, 15분 평균
- CPU 코어 수보다 낮으면 정상
- 예: 4코어 시스템에서 4.0 = 100% 사용

### 2.2 메모리 모니터링

**free**:
```bash
free -h                 # 사람이 읽기 쉬운 형식
free -m                 # MB 단위
free -s 1               # 1초마다 갱신
```

**출력 해석**:
```
              total        used        free      shared  buff/cache   available
Mem:           16Gi       6.0Gi       2.0Gi       500Mi       8.0Gi       9.5Gi
Swap:          8.0Gi         0B       8.0Gi
```

- **total**: 전체 메모리
- **used**: 사용 중
- **free**: 완전히 비어있음
- **buff/cache**: 버퍼/캐시 (필요 시 해제 가능)
- **available**: 실제 사용 가능한 메모리

**vmstat**:
```bash
vmstat                  # 가상 메모리 통계
vmstat 1 5              # 1초 간격, 5회
vmstat -s               # 메모리 통계
vmstat -d               # 디스크 통계
```

### 2.3 디스크 모니터링

**df** - 디스크 사용량:
```bash
df -h                   # 파일시스템 사용량
df -i                   # inode 사용량
df -T                   # 파일시스템 타입 포함
df -h /home             # 특정 마운트 포인트
```

**du** - 디렉토리 크기:
```bash
du -sh /home            # 디렉토리 총 크기
du -h --max-depth=1 /   # 1단계 하위 디렉토리
du -ah /var/log         # 모든 파일 크기
du -sh * | sort -h      # 크기 순 정렬
```

**iostat** (sysstat 패키지):
```bash
iostat                  # I/O 통계
iostat -x               # 확장 통계
iostat 1 5              # 1초 간격, 5회
iostat -d               # 디바이스만
```

**iotop** - 프로세스별 I/O:
```bash
iotop                   # 실시간 I/O 모니터링
iotop -o                # I/O 발생 프로세스만
```

### 2.4 네트워크 모니터링

**ifconfig/ip**:
```bash
ifconfig                # 네트워크 인터페이스
ip -s link              # 통계 포함
```

**netstat/ss**:
```bash
netstat -i              # 인터페이스 통계
netstat -s              # 프로토콜 통계
ss -s                   # 소켓 통계
```

**iftop** - 대역폭 모니터링:
```bash
iftop                   # 실시간 대역폭
iftop -i eth0           # 특정 인터페이스
```

**nload**:
```bash
nload                   # 네트워크 트래픽
nload eth0              # 특정 인터페이스
```

**vnstat** - 네트워크 트래픽 통계:
```bash
vnstat                  # 월별 통계
vnstat -d               # 일별
vnstat -h               # 시간별
vnstat -l               # 실시간
```

## 3. 로그 시스템

### 3.1 로그 파일 위치

**주요 로그 파일**: `/var/log/`
```
/var/log/messages       # 일반 시스템 메시지 (RHEL)
/var/log/syslog         # 시스템 로그 (Debian)
/var/log/auth.log       # 인증 로그 (Debian)
/var/log/secure         # 보안 로그 (RHEL)
/var/log/kern.log       # 커널 로그
/var/log/dmesg          # 부팅 메시지
/var/log/boot.log       # 부팅 로그
/var/log/cron           # cron 로그
/var/log/maillog        # 메일 로그
/var/log/httpd/         # Apache 로그
/var/log/nginx/         # Nginx 로그
/var/log/mysql/         # MySQL 로그
```

### 3.2 로그 확인

**기본 명령**:
```bash
tail -f /var/log/syslog         # 실시간 모니터링
tail -n 100 /var/log/messages   # 마지막 100줄
head -n 50 /var/log/auth.log    # 처음 50줄
less /var/log/syslog            # 페이지 단위
grep "error" /var/log/syslog    # 에러 검색
grep -i "failed" /var/log/secure  # 대소문자 무시
```

**여러 파일 검색**:
```bash
grep -r "error" /var/log/       # 재귀 검색
zgrep "error" /var/log/*.gz     # 압축 파일 검색
```

### 3.3 rsyslog

**설정 파일**: `/etc/rsyslog.conf`, `/etc/rsyslog.d/*.conf`

**로그 형식**:
```
facility.priority    action
```

**Facility** (로그 소스):
```
auth, authpriv  # 인증
cron            # cron
daemon          # 데몬
kern            # 커널
mail            # 메일
user            # 사용자
local0-local7   # 사용자 정의
```

**Priority** (심각도):
```
emerg   (0)     # 긴급
alert   (1)     # 즉시 조치 필요
crit    (2)     # 치명적
err     (3)     # 에러
warning (4)     # 경고
notice  (5)     # 알림
info    (6)     # 정보
debug   (7)     # 디버그
```

**설정 예**:
```
# 모든 에러 이상을 /var/log/errors
*.err                           /var/log/errors

# 커널 메시지
kern.*                          /var/log/kern.log

# 인증 로그
auth,authpriv.*                 /var/log/auth.log

# cron 로그
cron.*                          /var/log/cron

# 원격 로그 서버로 전송
*.* @@remote-server:514
```

**rsyslog 재시작**:
```bash
systemctl restart rsyslog
```

### 3.4 journalctl (systemd)

**기본 사용**:
```bash
journalctl                      # 모든 로그
journalctl -f                   # 실시간 (tail -f)
journalctl -n 100               # 최근 100줄
journalctl -r                   # 역순
journalctl --no-pager           # 페이저 없이
```

**시간 필터**:
```bash
journalctl --since "2025-01-01"
journalctl --since "1 hour ago"
journalctl --since today
journalctl --until "2025-01-31"
journalctl --since "2025-01-01" --until "2025-01-31"
```

**Unit 필터**:
```bash
journalctl -u httpd             # httpd 서비스
journalctl -u httpd -u mysql    # 여러 서비스
journalctl -u httpd --since today
```

**부팅 로그**:
```bash
journalctl -b                   # 현재 부팅
journalctl -b -1                # 이전 부팅
journalctl --list-boots         # 부팅 목록
```

**우선순위**:
```bash
journalctl -p err               # 에러 이상
journalctl -p warning           # 경고 이상
journalctl -p 3                 # 숫자로
```

**기타 필터**:
```bash
journalctl _PID=1234            # PID
journalctl _UID=1000            # UID
journalctl -k                   # 커널 메시지
journalctl _COMM=sshd           # 명령어 이름
```

**출력 형식**:
```bash
journalctl -o json              # JSON
journalctl -o json-pretty       # 보기 좋은 JSON
journalctl -o verbose           # 상세
journalctl -o cat               # 메시지만
```

**디스크 관리**:
```bash
journalctl --disk-usage         # 사용량
journalctl --vacuum-size=100M   # 100MB로 제한
journalctl --vacuum-time=1week  # 1주일 이상 삭제
```

### 3.5 로그 로테이션

**logrotate** - 로그 순환

**설정 파일**: `/etc/logrotate.conf`, `/etc/logrotate.d/*`

**예제**: `/etc/logrotate.d/nginx`
```
/var/log/nginx/*.log {
    daily                   # 매일 순환
    missingok               # 파일 없어도 에러 안 냄
    rotate 14               # 14개 보관
    compress                # 압축
    delaycompress           # 다음 순환 때 압축
    notifempty              # 비어있으면 순환 안 함
    create 0640 nginx adm   # 새 파일 생성
    sharedscripts           # 스크립트 한 번만 실행
    postrotate
        if [ -f /var/run/nginx.pid ]; then
            kill -USR1 `cat /var/run/nginx.pid`
        fi
    endscript
}
```

**옵션**:
- `daily/weekly/monthly`: 순환 주기
- `rotate N`: N개 보관
- `size 100M`: 크기 기준
- `compress`: gzip 압축
- `create mode owner group`: 새 파일 생성
- `postrotate ... endscript`: 순환 후 실행

**수동 실행**:
```bash
logrotate /etc/logrotate.conf   # 실행
logrotate -d /etc/logrotate.conf  # 디버그 (실제 실행 안 함)
logrotate -f /etc/logrotate.conf  # 강제 실행
```

## 4. 성능 분석

### 4.1 sar (System Activity Reporter)

**설치**: sysstat 패키지

**사용**:
```bash
sar                     # CPU 사용률
sar -u 1 5              # CPU, 1초 간격, 5회
sar -r                  # 메모리
sar -b                  # I/O
sar -n DEV              # 네트워크
sar -q                  # 로드 평균
sar -f /var/log/sa/sa10 # 특정 날짜 (10일)
```

**데이터 수집**: `/etc/cron.d/sysstat`

### 4.2 dmesg - 커널 메시지

```bash
dmesg                   # 커널 링 버퍼
dmesg | tail            # 최근 메시지
dmesg | grep -i error   # 에러 검색
dmesg -T                # 타임스탬프
dmesg -l err            # 에러 레벨
dmesg -w                # 실시간 모니터링
dmesg -c                # 버퍼 지우기
```

### 4.3 strace - 시스템 콜 추적

```bash
strace ls               # ls 명령 추적
strace -p 1234          # PID 추적
strace -c ls            # 통계
strace -e open ls       # open 시스템 콜만
strace -o output.txt ls # 파일로 저장
```

## 5. 시스템 감사 (auditd)

### 5.1 auditd 개요

**설치 및 시작**:
```bash
yum install audit       # RHEL
apt install auditd      # Debian
systemctl start auditd
systemctl enable auditd
```

### 5.2 감사 규칙

**규칙 추가**:
```bash
# 파일 접근 감사
auditctl -w /etc/passwd -p wa -k passwd_changes

# 시스템 콜 감사
auditctl -a always,exit -F arch=b64 -S open -k file_open

# 규칙 목록
auditctl -l

# 규칙 삭제
auditctl -D
```

**옵션**:
- `-w`: 파일 감시
- `-p`: 권한 (r=read, w=write, x=execute, a=attribute)
- `-k`: 키 (검색용)
- `-a`: 규칙 추가
- `-S`: 시스템 콜

### 5.3 감사 로그 검색

```bash
ausearch -k passwd_changes      # 키로 검색
ausearch -f /etc/passwd          # 파일로 검색
ausearch -ui 1000                # UID로 검색
ausearch -ts today               # 오늘
ausearch -ts recent              # 최근 10분

aureport                         # 요약 리포트
aureport -au                     # 인증 리포트
aureport -f                      # 파일 리포트
```

## 6. 시험 대비 핵심 요약

### 시스템 정보
- **커널**: `uname -r`
- **CPU**: `lscpu`, `/proc/cpuinfo`
- **메모리**: `free -h`, `/proc/meminfo`
- **디스크**: `lsblk`, `fdisk -l`

### 리소스 모니터링
- **CPU**: `top`, `mpstat`, `uptime`
- **메모리**: `free`, `vmstat`
- **디스크**: `df`, `du`, `iostat`
- **네트워크**: `ifconfig`, `netstat`, `ss`

### 로그
- **위치**: `/var/log/`
- **시스템**: `/var/log/messages`, `/var/log/syslog`
- **인증**: `/var/log/secure`, `/var/log/auth.log`
- **실시간**: `tail -f`

### journalctl
- **전체**: `journalctl`
- **실시간**: `journalctl -f`
- **서비스**: `journalctl -u service`
- **시간**: `journalctl --since "1 hour ago"`

### 기타
- **커널 메시지**: `dmesg`
- **로그 순환**: `logrotate`
- **성능**: `sar`
- **감사**: `auditd`, `ausearch`

---

**이전 챕터**: [[10-shell-scripting|셸 스크립팅]]  
**다음 챕터**: [[12-backup-recovery|백업 및 복구]]
