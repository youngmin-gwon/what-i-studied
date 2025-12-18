# 프로세스 및 작업 관리

## 1. 프로세스 개념

### 1.1 프로세스란?
- **정의**: 실행 중인 프로그램의 인스턴스
- **구성**: 코드, 데이터, 스택, 힙, PCB(Process Control Block)
- **PID**: 프로세스 ID, 고유 식별자
- **PPID**: 부모 프로세스 ID

### 1.2 프로세스 상태
```
Running (R)     - 실행 중 또는 실행 대기
Sleeping (S)    - 인터럽트 가능한 대기
Uninterruptible (D) - 인터럽트 불가능한 대기 (I/O)
Stopped (T)     - 중지됨 (Ctrl+Z)
Zombie (Z)      - 종료되었지만 부모가 회수 안 함
```

### 1.3 프로세스 유형
- **포그라운드**: 터미널에서 실행, 입력 대기
- **백그라운드**: 터미널과 독립적으로 실행
- **데몬**: 백그라운드 서비스 프로세스
- **고아 프로세스**: 부모가 먼저 종료됨
- **좀비 프로세스**: 종료되었지만 자원 미회수

## 2. 프로세스 확인

### 2.1 ps 명령어

**기본 사용**:
```bash
ps                      # 현재 터미널의 프로세스
ps -e                   # 모든 프로세스
ps -ef                  # 전체 포맷
ps aux                  # BSD 스타일
ps -eLf                 # 스레드 포함
```

**출력 필드 (ps aux)**:
```
USER  PID %CPU %MEM    VSZ   RSS TTY STAT START TIME COMMAND
root    1  0.0  0.1 169416 11234 ?   Ss   Jan01 0:05 /usr/lib/systemd/systemd
```

- **USER**: 소유자
- **PID**: 프로세스 ID
- **%CPU**: CPU 사용률
- **%MEM**: 메모리 사용률
- **VSZ**: 가상 메모리 크기 (KB)
- **RSS**: 물리 메모리 크기 (KB)
- **TTY**: 터미널
- **STAT**: 상태
- **START**: 시작 시간
- **TIME**: CPU 사용 시간
- **COMMAND**: 명령어

**유용한 옵션**:
```bash
ps -ef | grep httpd             # httpd 프로세스 검색
ps aux --sort=-%cpu             # CPU 사용률 순 정렬
ps aux --sort=-%mem             # 메모리 사용률 순
ps -u username                  # 특정 사용자 프로세스
ps -C httpd                     # 명령어 이름으로 검색
ps -p 1234                      # PID로 검색
ps -o pid,comm,%cpu,%mem        # 출력 필드 지정
```

### 2.2 top 명령어

**실시간 모니터링**:
```bash
top                     # 실시간 프로세스 모니터링
top -u username         # 특정 사용자
top -p 1234             # 특정 PID
top -d 5                # 5초 간격 업데이트
```

**top 내부 명령**:
```
h       - 도움말
k       - 프로세스 종료 (PID 입력)
r       - nice 값 변경
M       - 메모리 사용률 순 정렬
P       - CPU 사용률 순 정렬
T       - 실행 시간 순 정렬
u       - 사용자 필터
q       - 종료
```

**top 출력**:
```
top - 12:00:00 up 10 days, 2:30, 3 users, load average: 0.15, 0.20, 0.18
Tasks: 200 total, 1 running, 199 sleeping, 0 stopped, 0 zombie
%Cpu(s): 5.2 us, 2.1 sy, 0.0 ni, 92.5 id, 0.2 wa, 0.0 hi, 0.0 si
MiB Mem: 16000 total, 8000 free, 6000 used, 2000 buff/cache
MiB Swap: 8000 total, 8000 free, 0 used, 9500 avail Mem
```

- **load average**: 1분, 5분, 15분 평균 부하
- **us**: 사용자 공간 CPU
- **sy**: 시스템(커널) CPU
- **ni**: nice 프로세스 CPU
- **id**: 유휴 CPU
- **wa**: I/O 대기

### 2.3 기타 모니터링 도구

**htop** (향상된 top):
```bash
htop                    # 컬러풀한 인터페이스, 마우스 지원
```

**pstree** - 프로세스 트리:
```bash
pstree                  # 프로세스 계층 구조
pstree -p               # PID 표시
pstree username         # 특정 사용자
```

**pgrep** - 프로세스 검색:
```bash
pgrep httpd             # httpd 프로세스 PID
pgrep -u username       # 사용자별
pgrep -l httpd          # PID와 이름
```

## 3. 프로세스 제어

### 3.1 시그널

**주요 시그널**:
```
SIGHUP (1)      - 터미널 종료, 설정 다시 로드
SIGINT (2)      - 인터럽트 (Ctrl+C)
SIGQUIT (3)     - 종료 및 코어 덤프 (Ctrl+\)
SIGKILL (9)     - 강제 종료 (차단 불가)
SIGTERM (15)    - 정상 종료 요청 (기본)
SIGSTOP (19)    - 일시 정지 (차단 불가)
SIGCONT (18)    - 계속 실행
SIGTSTP (20)    - 일시 정지 (Ctrl+Z)
```

**시그널 확인**:
```bash
kill -l                 # 모든 시그널 목록
man 7 signal            # 시그널 매뉴얼
```

### 3.2 kill 명령어

```bash
kill PID                # SIGTERM (15) 전송
kill -9 PID             # SIGKILL (강제 종료)
kill -15 PID            # SIGTERM (정상 종료)
kill -HUP PID           # SIGHUP (재시작)
kill -STOP PID          # 일시 정지
kill -CONT PID          # 계속 실행
kill -l                 # 시그널 목록
```

**killall** - 이름으로 종료:
```bash
killall httpd           # 모든 httpd 프로세스 종료
killall -9 httpd        # 강제 종료
killall -u username     # 사용자의 모든 프로세스
```

**pkill** - 패턴으로 종료:
```bash
pkill httpd             # httpd 프로세스 종료
pkill -9 -u username    # 사용자 프로세스 강제 종료
pkill -STOP httpd       # 일시 정지
```

### 3.3 프로세스 우선순위

**nice 값**:
- **범위**: -20 (최고 우선순위) ~ 19 (최저 우선순위)
- **기본**: 0
- **일반 사용자**: 0~19만 설정 가능
- **root**: -20~19 설정 가능

**nice** - 우선순위로 실행:
```bash
nice command            # nice 10으로 실행
nice -n 10 command      # nice 10으로 실행
nice -n -5 command      # nice -5로 실행 (root)
```

**renice** - 실행 중 프로세스 우선순위 변경:
```bash
renice 10 -p PID        # PID의 nice를 10으로
renice -5 -p PID        # nice를 -5로 (root)
renice 10 -u username   # 사용자의 모든 프로세스
renice 10 -g groupname  # 그룹의 모든 프로세스
```

**확인**:
```bash
ps -eo pid,ni,comm      # PID, nice, 명령어
top                     # NI 열에서 확인
```

## 4. 작업 제어 (Job Control)

### 4.1 포그라운드와 백그라운드

**백그라운드 실행**:
```bash
command &               # 백그라운드로 실행
sleep 100 &             # 예제
[1] 12345               # [작업번호] PID
```

**포그라운드로 전환**:
```bash
fg                      # 최근 백그라운드 작업을 포그라운드로
fg %1                   # 작업 번호 1을 포그라운드로
```

**백그라운드로 전환**:
```bash
Ctrl+Z                  # 현재 작업 일시 정지
bg                      # 일시 정지된 작업을 백그라운드로
bg %1                   # 작업 번호 1을 백그라운드로
```

### 4.2 작업 관리

**jobs** - 작업 목록:
```bash
jobs                    # 모든 작업
jobs -l                 # PID 포함
jobs -r                 # 실행 중인 작업만
jobs -s                 # 정지된 작업만
```

**출력 예**:
```
[1]   Running         sleep 100 &
[2]-  Stopped         vim file.txt
[3]+  Running         find / -name "*.log" &
```

- `+`: 현재 작업 (기본 대상)
- `-`: 이전 작업

**작업 종료**:
```bash
kill %1                 # 작업 번호 1 종료
kill %sleep             # sleep 명령 종료
kill %%                 # 현재 작업 종료
```

### 4.3 nohup과 disown

**nohup** - 터미널 종료 후에도 계속 실행:
```bash
nohup command &         # 백그라운드로 실행, 출력은 nohup.out
nohup command > output.log 2>&1 &  # 출력 리다이렉션
```

**disown** - 작업을 셸에서 분리:
```bash
command &               # 백그라운드 실행
disown                  # 현재 작업 분리
disown %1               # 작업 1 분리
disown -a               # 모든 작업 분리
disown -h %1            # SIGHUP 무시하도록 설정
```

## 5. 프로세스 정보

### 5.1 /proc 파일시스템

**프로세스 디렉토리**: `/proc/[PID]/`
```bash
/proc/1234/cmdline      # 명령줄 인수
/proc/1234/environ      # 환경 변수
/proc/1234/status       # 상태 정보
/proc/1234/fd/          # 파일 디스크립터
/proc/1234/exe          # 실행 파일 심볼릭 링크
/proc/1234/cwd          # 현재 작업 디렉토리
```

**확인**:
```bash
cat /proc/1234/cmdline  # 명령줄
cat /proc/1234/status   # 상태
ls -l /proc/1234/fd/    # 열린 파일
ls -l /proc/1234/exe    # 실행 파일
```

### 5.2 lsof - 열린 파일 확인

```bash
lsof                    # 모든 열린 파일
lsof -p PID             # 특정 프로세스
lsof -u username        # 특정 사용자
lsof /path/to/file      # 파일을 사용 중인 프로세스
lsof -i :80             # 포트 80 사용 프로세스
lsof -i TCP:22          # TCP 22번 포트
lsof -c httpd           # httpd 프로세스
```

### 5.3 strace - 시스템 콜 추적

```bash
strace command          # 명령 실행 추적
strace -p PID           # 실행 중 프로세스 추적
strace -c command       # 시스템 콜 통계
strace -e open command  # open 시스템 콜만
strace -o output.txt command  # 출력 저장
```

## 6. 시스템 리소스 제한

### 6.1 ulimit

**리소스 제한 확인 및 설정**:
```bash
ulimit -a               # 모든 제한 확인
ulimit -n               # 열린 파일 수 제한
ulimit -u               # 프로세스 수 제한
ulimit -f               # 파일 크기 제한
ulimit -m               # 메모리 제한
ulimit -t               # CPU 시간 제한

ulimit -n 4096          # 열린 파일 수를 4096으로
ulimit -u 100           # 프로세스 수를 100으로
ulimit -f unlimited     # 파일 크기 무제한
```

**하드/소프트 제한**:
```bash
ulimit -Hn              # 하드 제한 (최대값)
ulimit -Sn              # 소프트 제한 (현재값)
ulimit -Hn 8192         # 하드 제한 설정 (root)
```

### 6.2 /etc/security/limits.conf

**영구 설정**:
```
# 형식: <domain> <type> <item> <value>
username    soft    nproc   100
username    hard    nproc   200
@group      soft    nofile  4096
@group      hard    nofile  8192
*           soft    core    0
*           hard    rss     10000
```

**domain**:
- 사용자명
- `@그룹명`
- `*` (모든 사용자)

**type**:
- `soft`: 소프트 제한
- `hard`: 하드 제한

**item**:
- `nofile`: 열린 파일 수
- `nproc`: 프로세스 수
- `core`: 코어 파일 크기
- `fsize`: 파일 크기
- `cpu`: CPU 시간
- `rss`: 메모리

## 7. 프로세스 간 통신 (IPC)

### 7.1 IPC 메커니즘

**종류**:
- **파이프**: 단방향 통신
- **Named Pipe (FIFO)**: 파일시스템에 존재
- **메시지 큐**: 메시지 기반
- **공유 메모리**: 가장 빠름
- **세마포어**: 동기화
- **소켓**: 네트워크 통신

### 7.2 IPC 확인

**ipcs** - IPC 자원 확인:
```bash
ipcs                    # 모든 IPC
ipcs -q                 # 메시지 큐
ipcs -m                 # 공유 메모리
ipcs -s                 # 세마포어
ipcs -p                 # 생성자 PID
ipcs -t                 # 시간 정보
```

**ipcrm** - IPC 자원 제거:
```bash
ipcrm -q <msqid>        # 메시지 큐 제거
ipcrm -m <shmid>        # 공유 메모리 제거
ipcrm -s <semid>        # 세마포어 제거
```

## 8. 시험 대비 핵심 요약

### 프로세스 확인
- **ps aux**: 모든 프로세스
- **ps -ef**: 전체 포맷
- **top**: 실시간 모니터링
- **pgrep**: 프로세스 검색

### 프로세스 제어
- **kill PID**: SIGTERM (15)
- **kill -9 PID**: SIGKILL (강제)
- **killall**: 이름으로 종료
- **pkill**: 패턴으로 종료

### 우선순위
- **nice**: -20 (높음) ~ 19 (낮음)
- **nice -n 10 command**: nice 10으로 실행
- **renice 10 -p PID**: 우선순위 변경

### 작업 제어
- **command &**: 백그라운드
- **Ctrl+Z**: 일시 정지
- **fg**: 포그라운드로
- **bg**: 백그라운드로
- **jobs**: 작업 목록
- **nohup**: 터미널 종료 후에도 실행

### 시그널
- **1 (HUP)**: 재시작
- **2 (INT)**: Ctrl+C
- **9 (KILL)**: 강제 종료
- **15 (TERM)**: 정상 종료
- **20 (TSTP)**: Ctrl+Z

---

**이전 챕터**: [사용자 및 권한 관리](05-users-permissions.md)  
**다음 챕터**: [패키지 관리](07-package-management.md)
