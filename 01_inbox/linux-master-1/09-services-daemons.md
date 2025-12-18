# 시스템 서비스 및 데몬

## 1. systemd 개요

### 1.1 systemd란?
- **초기화 시스템**: PID 1, 부팅 시 첫 프로세스
- **서비스 관리자**: 시스템 서비스 관리
- **병렬 시작**: 빠른 부팅
- **의존성 관리**: 자동 의존성 해결
- **표준화**: 대부분의 주요 배포판 채택

### 1.2 Unit 개념

**Unit 타입**:
- **service**: 시스템 서비스
- **socket**: 소켓 기반 활성화
- **target**: Unit 그룹 (런레벨과 유사)
- **mount**: 마운트 포인트
- **device**: 디바이스
- **timer**: 타이머 (cron 대체)
- **path**: 경로 기반 활성화
- **slice**: 리소스 관리 그룹

## 2. systemctl 명령어

### 2.1 서비스 관리

**기본 제어**:
```bash
systemctl start httpd           # 서비스 시작
systemctl stop httpd            # 서비스 중지
systemctl restart httpd         # 서비스 재시작
systemctl reload httpd          # 설정 다시 로드
systemctl reload-or-restart httpd  # 가능하면 reload, 아니면 restart
systemctl status httpd          # 상태 확인
systemctl is-active httpd       # 활성 여부 (active/inactive)
systemctl is-enabled httpd      # 부팅 시 자동 시작 여부
systemctl is-failed httpd       # 실패 여부
```

**부팅 시 자동 시작**:
```bash
systemctl enable httpd          # 자동 시작 활성화
systemctl disable httpd         # 자동 시작 비활성화
systemctl enable --now httpd    # 활성화 + 즉시 시작
systemctl disable --now httpd   # 비활성화 + 즉시 중지
systemctl mask httpd            # 서비스 마스킹 (시작 불가)
systemctl unmask httpd          # 마스킹 해제
```

### 2.2 Unit 목록 및 정보

**목록**:
```bash
systemctl list-units            # 모든 활성 unit
systemctl list-units --all      # 모든 unit (비활성 포함)
systemctl list-units --type=service  # 서비스만
systemctl list-units --state=active  # 활성 unit만
systemctl list-units --state=failed  # 실패한 unit
systemctl list-unit-files       # unit 파일 목록
systemctl list-unit-files --type=service  # 서비스 파일
```

**의존성**:
```bash
systemctl list-dependencies httpd  # 의존성 트리
systemctl list-dependencies --reverse httpd  # 역의존성
```

**상세 정보**:
```bash
systemctl show httpd            # 모든 속성
systemctl show httpd -p MainPID # 특정 속성
systemctl cat httpd             # unit 파일 내용
```

### 2.3 시스템 제어

**전원 관리**:
```bash
systemctl poweroff              # 시스템 종료
systemctl reboot                # 재부팅
systemctl suspend               # 절전 모드
systemctl hibernate             # 최대 절전 모드
systemctl hybrid-sleep          # 하이브리드 절전
```

**systemd 재로드**:
```bash
systemctl daemon-reload         # unit 파일 다시 로드
systemctl reset-failed          # 실패 상태 초기화
```

## 3. Unit 파일

### 3.1 Unit 파일 위치

**우선순위 순**:
1. `/etc/systemd/system/`: 관리자 설정 (최우선)
2. `/run/systemd/system/`: 런타임 설정
3. `/usr/lib/systemd/system/`: 패키지 설치 기본값

### 3.2 Service Unit 파일 구조

**예제**: `/etc/systemd/system/myapp.service`
```ini
[Unit]
Description=My Application
Documentation=https://example.com/docs
After=network.target
Requires=network.target
Wants=mysql.service

[Service]
Type=simple
User=myapp
Group=myapp
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/bin/start.sh
ExecStop=/opt/myapp/bin/stop.sh
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
RestartSec=5s
Environment="VAR1=value1" "VAR2=value2"
EnvironmentFile=/etc/myapp/env

[Install]
WantedBy=multi-user.target
```

**[Unit] 섹션**:
- `Description`: 서비스 설명
- `Documentation`: 문서 URL
- `After`: 이후에 시작
- `Before`: 이전에 시작
- `Requires`: 필수 의존성 (실패 시 함께 실패)
- `Wants`: 선택적 의존성 (실패해도 계속)
- `Conflicts`: 충돌 (동시 실행 불가)

**[Service] 섹션**:
- `Type`: 서비스 타입
  - `simple`: 기본, ExecStart가 메인 프로세스
  - `forking`: 포크 후 부모 종료
  - `oneshot`: 한 번 실행 후 종료
  - `notify`: 준비 완료 알림
  - `dbus`: D-Bus 이름 획득 후 준비
- `ExecStart`: 시작 명령
- `ExecStop`: 중지 명령
- `ExecReload`: 재로드 명령
- `Restart`: 재시작 정책
  - `no`: 재시작 안 함
  - `on-failure`: 실패 시
  - `on-abnormal`: 비정상 종료 시
  - `always`: 항상
- `User/Group`: 실행 사용자/그룹
- `WorkingDirectory`: 작업 디렉토리
- `Environment`: 환경 변수
- `EnvironmentFile`: 환경 변수 파일

**[Install] 섹션**:
- `WantedBy`: 어떤 target이 이 서비스를 원하는지
- `RequiredBy`: 어떤 target이 이 서비스를 필요로 하는지
- `Alias`: 별칭

### 3.3 Unit 파일 생성 및 수정

**생성**:
```bash
# 파일 생성
sudo vim /etc/systemd/system/myapp.service

# 권한 설정
sudo chmod 644 /etc/systemd/system/myapp.service

# systemd 재로드
sudo systemctl daemon-reload

# 서비스 시작 및 활성화
sudo systemctl enable --now myapp
```

**수정**:
```bash
# 편집
sudo systemctl edit myapp       # 오버라이드 파일 생성
sudo systemctl edit --full myapp  # 전체 파일 편집

# 재로드
sudo systemctl daemon-reload
sudo systemctl restart myapp
```

## 4. Target

### 4.1 Target 개념

**런레벨 대응**:
```
runlevel 0 → poweroff.target
runlevel 1 → rescue.target
runlevel 2,3,4 → multi-user.target
runlevel 5 → graphical.target
runlevel 6 → reboot.target
```

**주요 Target**:
- `multi-user.target`: 텍스트 모드, 네트워크
- `graphical.target`: GUI 모드
- `rescue.target`: 복구 모드 (싱글 유저)
- `emergency.target`: 응급 모드 (최소 환경)

### 4.2 Target 관리

```bash
systemctl get-default           # 기본 target 확인
systemctl set-default multi-user.target  # 기본 target 설정
systemctl isolate graphical.target  # target 전환
systemctl list-units --type=target  # target 목록
```

## 5. 로그 관리 (journalctl)

### 5.1 journald

**특징**:
- systemd 통합 로깅
- 바이너리 형식
- 인덱싱으로 빠른 검색
- 자동 로테이션

### 5.2 journalctl 명령어

**기본 사용**:
```bash
journalctl                      # 모든 로그
journalctl -f                   # 실시간 모니터링 (tail -f)
journalctl -n 50                # 최근 50줄
journalctl -r                   # 역순 (최신부터)
journalctl --no-pager           # 페이저 없이
```

**시간 필터**:
```bash
journalctl --since "2025-01-01"
journalctl --since "1 hour ago"
journalctl --since "10 min ago"
journalctl --until "2025-01-31"
journalctl --since today
journalctl --since yesterday
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

**우선순위 필터**:
```bash
journalctl -p err               # 에러 이상
journalctl -p warning           # 경고 이상
journalctl -p 3                 # 숫자로 (0=emerg, 7=debug)
```

**기타 필터**:
```bash
journalctl _PID=1234            # PID로
journalctl _UID=1000            # UID로
journalctl -k                   # 커널 메시지 (dmesg)
journalctl --disk-usage         # 디스크 사용량
journalctl --vacuum-size=100M   # 100MB로 제한
journalctl --vacuum-time=1week  # 1주일 이상 삭제
```

**출력 형식**:
```bash
journalctl -o json              # JSON 형식
journalctl -o json-pretty       # 보기 좋은 JSON
journalctl -o verbose           # 상세 정보
journalctl -o cat               # 메시지만
```

## 6. Timer (cron 대체)

### 6.1 Timer Unit

**Timer 파일**: `/etc/systemd/system/backup.timer`
```ini
[Unit]
Description=Daily Backup Timer

[Timer]
OnCalendar=daily
OnCalendar=*-*-* 02:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

**Service 파일**: `/etc/systemd/system/backup.service`
```ini
[Unit]
Description=Backup Service

[Service]
Type=oneshot
ExecStart=/usr/local/bin/backup.sh
```

**OnCalendar 형식**:
```
daily           # 매일 00:00
weekly          # 매주 월요일 00:00
monthly         # 매월 1일 00:00
*-*-* 02:00:00  # 매일 02:00
Mon *-*-* 10:00:00  # 매주 월요일 10:00
```

### 6.2 Timer 관리

```bash
systemctl enable backup.timer   # 타이머 활성화
systemctl start backup.timer    # 타이머 시작
systemctl list-timers           # 타이머 목록
systemctl list-timers --all     # 모든 타이머
systemctl status backup.timer   # 타이머 상태
```

## 7. cron

### 7.1 cron 개요

**cron 데몬**: `crond` (systemd에서 관리)

**crontab 형식**:
```
분 시 일 월 요일 명령
* * * * * command
```

**필드**:
- 분: 0-59
- 시: 0-23
- 일: 1-31
- 월: 1-12
- 요일: 0-7 (0과 7은 일요일)

**특수 문자**:
- `*`: 모든 값
- `,`: 여러 값 (1,3,5)
- `-`: 범위 (1-5)
- `/`: 간격 (*/5 = 5분마다)

### 7.2 crontab 명령어

```bash
crontab -e                      # 편집
crontab -l                      # 목록
crontab -r                      # 삭제
crontab -u username -e          # 특정 사용자 (root)
```

**예제**:
```cron
# 매일 02:00에 백업
0 2 * * * /usr/local/bin/backup.sh

# 매주 일요일 03:00에 정리
0 3 * * 0 /usr/local/bin/cleanup.sh

# 5분마다 체크
*/5 * * * * /usr/local/bin/check.sh

# 평일 09:00-18:00 매시간
0 9-18 * * 1-5 /usr/local/bin/work.sh

# 매월 1일 00:00
0 0 1 * * /usr/local/bin/monthly.sh
```

### 7.3 시스템 cron

**디렉토리**:
- `/etc/cron.hourly/`: 매시간
- `/etc/cron.daily/`: 매일
- `/etc/cron.weekly/`: 매주
- `/etc/cron.monthly/`: 매월

**사용법**:
```bash
# 실행 가능한 스크립트를 디렉토리에 배치
sudo cp script.sh /etc/cron.daily/
sudo chmod +x /etc/cron.daily/script.sh
```

**/etc/crontab**:
```cron
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

# 분 시 일 월 요일 사용자 명령
0 2 * * * root /usr/local/bin/backup.sh
```

### 7.4 anacron

**용도**: 항상 켜져있지 않은 시스템용

**/etc/anacrontab**:
```
# 기간(일) 지연(분) 작업ID 명령
1 5 cron.daily run-parts /etc/cron.daily
7 10 cron.weekly run-parts /etc/cron.weekly
30 15 cron.monthly run-parts /etc/cron.monthly
```

## 8. at

### 8.1 at 명령어

**일회성 작업 예약**:
```bash
at 14:30                        # 14:30에 실행
at> /usr/local/bin/task.sh
at> <Ctrl+D>

at now + 1 hour                 # 1시간 후
at now + 30 minutes             # 30분 후
at tomorrow                     # 내일 같은 시간
at 10:00 AM tomorrow            # 내일 10:00
at 2:00 PM 12/31/2025           # 특정 날짜
```

**작업 관리**:
```bash
atq                             # 대기 중인 작업
at -l                           # 동일
atrm <job_number>               # 작업 삭제
at -d <job_number>              # 동일
at -c <job_number>              # 작업 내용 확인
```

**파일에서 읽기**:
```bash
at -f script.sh now + 1 hour
```

## 9. 시험 대비 핵심 요약

### systemctl
- **시작/중지**: `systemctl start/stop/restart`
- **상태**: `systemctl status`
- **자동 시작**: `systemctl enable/disable`
- **목록**: `systemctl list-units`

### Unit 파일
- **위치**: `/etc/systemd/system/`, `/usr/lib/systemd/system/`
- **재로드**: `systemctl daemon-reload`
- **편집**: `systemctl edit`

### Target
- **기본**: `systemctl get-default`
- **설정**: `systemctl set-default`
- **전환**: `systemctl isolate`

### journalctl
- **전체**: `journalctl`
- **실시간**: `journalctl -f`
- **서비스**: `journalctl -u service`
- **부팅**: `journalctl -b`

### cron
- **편집**: `crontab -e`
- **목록**: `crontab -l`
- **형식**: `분 시 일 월 요일 명령`
- **디렉토리**: `/etc/cron.{hourly,daily,weekly,monthly}/`

### at
- **예약**: `at 14:30`
- **목록**: `atq`
- **삭제**: `atrm <job>`

---

**이전 챕터**: [네트워크 설정](08-network-config.md)  
**다음 챕터**: [셸 스크립팅](10-shell-scripting.md)
