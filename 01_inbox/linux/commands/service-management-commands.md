---
title: Service Management Commands
tags: [linux, commands, service, systemctl, systemd]
aliases: [서비스 관리, systemctl, systemd]
date modified: 2025-12-20 14:17:48 +09:00
date created: 2025-12-20 14:17:48 +09:00
---

## 🌐 개요 (Overview)

Linux 시스템 서비스(데몬) 관리 명령어들입니다. systemd가 표준이 되었지만 레거시 시스템도 다룹니다.

## 📋 Quick Reference

| 명령어 | 용도 | 시스템 |
|--------|------|--------|
| `systemctl` | 서비스 제어 | systemd (현대) |
| `journalctl` | systemd 로그 | systemd |
| `service` | 서비스 제어 | SysV/Upstart (레거시) |

## 🔧 systemctl - Service Control

### 기본 서비스 관리

```bash
# 서비스 시작
systemctl start nginx
systemctl start apache2
systemctl start mysql

# 서비스 중지
systemctl stop nginx

# 서비스 재시작
systemctl restart nginx

# 설정 변경 후 재로드 (다운타임 없음)
systemctl reload nginx

# 재로드 실패 시 재시작
systemctl reload-or-restart nginx
```

### 서비스 상태 확인

```bash
# 상태 확인
systemctl status nginx
systemctl status nginx.service    # .service는 생략 가능

# 실행 중인지만 확인
systemctl is-active nginx

# 활성화되어 있는지 확인
systemctl is-enabled nginx

# 실패했는지 확인
systemctl is-failed nginx
```

### 부팅 시 자동 시작

```bash
# 부팅 시 자동 시작 활성화
systemctl enable nginx

# 활성화 + 즉시 시작
systemctl enable --now nginx

# 자동 시작 비활성화
systemctl disable nginx

# 비활성화 + 즉시 중지
systemctl disable --now nginx

# 완전히 차단 (enable 불가능)
systemctl mask nginx

# 차단 해제
systemctl unmask nginx
```

### 서비스 목록

```bash
# 모든 유닛
systemctl list-units

# 서비스만
systemctl list-units --type=service

# 실행 중인 서비스만
systemctl list-units --type=service --state=running

# 실패한 서비스
systemctl list-units --type=service --state=failed

# 모든 서비스 (비활성 포함)
systemctl list-unit-files --type=service

# 활성화된 서비스
systemctl list-unit-files --type=service --state=enabled
```

### Unit 파일 관리

```bash
# Unit 파일 위치 확인
systemctl cat nginx

# Unit 파일 편집
systemctl edit nginx               # 오버라이드 파일 생성
systemctl edit --full nginx        # 전체 파일 편집

# 설정 리로드 (unit 파일 변경 후)
systemctl daemon-reload

# Unit 파일 의존성 확인
systemctl list-dependencies nginx
```

### 시스템 제어 (System Control)

| 명령어 | 결과 | 설명 |
| :--- | :--- | :--- |
| **`shutdown -h now`** | **종료 (Halt)** | 시스템을 즉시 종료 (전력 종료 포함) |
| **`poweroff`** | **종료 (Poweroff)** | 시스템 종료 및 전원 끄기 |
| **`halt`** | **중지 (Halt)** | OS를 중지시키나 하드웨어 전원을 끄지 않을 수 있음 |
| **`reboot`** | **재부팅 (Reboot)** | 시스템 재시작 |
| **`init 0`** | **종료** | SysV 런레벨 0 (종료)으로 전환 |
| **`init 6`** | **재부팅** | SysV 런레벨 6 (재부팅)으로 전환 |

> [!IMPORTANT]
> **자주 틀리는 포인트 (Exam Tip)**:
> `shutdown -h now`, `poweroff`, `halt`는 모두 시스템을 **멈추거나 끄는** 목적의 명령입니다. 반면, **`init 6`**이나 **`reboot`**은 시스템을 **재부팅**하는 명령이므로 실행 결과가 다릅니다.

```bash
# 특정 시간 후 종료
shutdown -h +10 "10분 후 점검을 위해 종료합니다."

# 종료 취소
shutdown -c

# 절전 관련
systemctl suspend      # 대기 모드 (RAM에 상태 유지)
systemctl hibernate    # 최대 절전 모드 (Disk에 상태 저장)
```

### 타겟 (Runlevel)

```bash
# 현재 타겟 확인
systemctl get-default

# 기본 타겟 변경
systemctl set-default multi-user.target    # CLI (runlevel 3)
systemctl set-default graphical.target     # GUI (runlevel 5)

# 타겟으로 전환
systemctl isolate multi-user.target
systemctl isolate rescue.target            # 단일 사용자 모드
```

**주요 타겟**:

| 타겟 | Runlevel | 설명 |
| :--- | :---: | :--- |
| **`poweroff.target`** | **0** | **종료 (Halt)**: 시스템의 모든 프로세스를 종료하고 전원을 끌 준비를 함 |
| **`rescue.target`** | **1** | **단일 사용자 모드 (Single-User)**: 시스템 복구용. 네트워크가 꺼지고 root만 사용 가능 |
| **`multi-user.target`** | **2** | **다중 사용자 모드 (NFS 미지원)**: 네트워크기능이 제한된 텍스트 모드 (잘 안 쓰임) |
| **`multi-user.target`** | **3** | **다중 사용자 모드 (NFS 지원, CLI)**: 표준 텍스트 기반 서버 환경 |
| **`multi-user.target`** | **4** | **미정의 (Unused)**: 사용자가 정의하여 사용할 수 있도록 비워둔 레벨 |
| **`graphical.target`** | **5** | **다중 사용자 모드 (GUI)**: X Window 시스템이 실행되는 그래픽 환경 |
| **`reboot.target`** | **6** | **재부팅 (Reboot)**: 시스템을 즉시 재시작 |

> [!TIP]
> **런레벨 숫자의 의미**: 숫자가 높을수록 시스템의 기능(네트워크, 그래픽 등)이 더 많이 활성화된 상태를 의미한다고 이해하면 쉽습니다. (0: 꺼짐 -> 1: 최소 복구 -> 3: 서버 환경 -> 5: 그래픽 환경)

## 📜 journalctl - systemd Logs

### 기본 로그 조회

```bash
# 전체 로그
journalctl

# 실시간 (tail -f)
journalctl -f

# 최근 N줄
journalctl -n 100
journalctl -n 50 --no-pager

# 역순 (최신부터)
journalctl -r
```

### 시간 필터

```bash
# 오늘
journalctl --since today
journalctl --since 00:00

# 어제
journalctl --since yesterday

# 특정 시간 이후
journalctl --since "2025-01-01"
journalctl --since "2025-01-01 10:00:00"
journalctl --since "1 hour ago"
journalctl --since "30 min ago"

# 시간 범위
journalctl --since "2025-01-01" --until "2025-01-31"
journalctl --since "1 hour ago" --until "30 min ago"
```

### 서비스별 로그

```bash
# 특정 서비스
journalctl -u nginx
journalctl -u nginx.service
journalctl -u ssh

# 여러 서비스
journalctl -u nginx -u mysql

# 서비스 + 실시간
journalctl -u nginx -f

# 서비스 + 오늘
journalctl -u nginx --since today
```

### 우선순위 필터

```bash
# 에러 이상
journalctl -p err

# 경고 이상
journalctl -p warning

# 특정 우선순위
journalctl -p 3                    # err
journalctl -p 4                    # warning
```

**우선순위 레벨**:
- 0: emerg
- 1: alert
- 2: crit
- 3: err
- 4: warning
- 5: notice
- 6: info
- 7: debug

### 부팅 로그

```bash
# 현재 부팅
journalctl -b
journalctl -b 0

# 이전 부팅
journalctl -b -1
journalctl -b -2

# 부팅 목록
journalctl --list-boots

# 특정 부팅
journalctl -b 2a3b4c5d...
```

### 커널 메시지

```bash
journalctl -k                      # 현재 부팅의 커널 메시지
journalctl -k -b -1                # 이전 부팅
```

### 출력 형식

```bash
# JSON
journalctl -o json
journalctl -o json-pretty

# 간단히 (메시지만)
journalctl -o cat

# 상세 정보
journalctl -o verbose

# 단축 형식
journalctl -o short
journalctl -o short-iso            # ISO 시간
```

### 디스크 사용량 관리

```bash
# 로그 크기 확인
journalctl --disk-usage

# 오래된 로그 삭제
journalctl --vacuum-time=1week     # 1주일 이상
journalctl --vacuum-size=100M      # 100MB로 제한
journalctl --vacuum-files=5        # 5개 파일만 유지

# 로그 검증
journalctl --verify
```

## 🔄 service (레거시)

### SysV Init 서비스

```bash
# 서비스 시작/중지/재시작
service nginx start
service nginx stop
service nginx restart
service nginx status

# 모든 서비스 상태
service --status-all
```

### chkconfig (RHEL/CentOS 레거시)

```bash
# 부팅 시 자동 시작
chkconfig nginx on
chkconfig nginx off

# 목록
chkconfig --list
```

## 💡 실무 시나리오

### 웹 서버 배포 후 재시작

```bash
# 1. 설정 파일 수정
sudo vim /etc/nginx/nginx.conf

# 2. 문법 검사
sudo nginx -t

# 3. 설정 리로드 (다운타임 없음)
sudo systemctl reload nginx

# 4. 실패 시 로그 확인
sudo journalctl -u nginx -n 50
```

### 서비스 문제 진단

```bash
# 1. 상태 확인
systemctl status mysql

# 2. 상세 로그
journalctl -u mysql -n 100 --no-pager

# 3. 에러만 확인
journalctl -u mysql -p err

# 4. 최근 부팅 로그
journalctl -u mysql -b

# 5. 재시작
systemctl restart mysql
```

### Custom Service 생성

```bash
# /etc/systemd/system/myapp.service
cat << EOF | sudo tee /etc/systemd/system/myapp.service
[Unit]
Description=My Application
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/myapp
ExecStart=/opt/myapp/start.sh
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# daemon-reload
sudo systemctl daemon-reload

# 활성화 및 시작
sudo systemctl enable --now myapp
```

### 부팅 속도 분석

```bash
# 부팅 시간 확인
systemd-analyze

# 상세 분석
systemd-analyze blame

# 크리티컬 체인
systemd-analyze critical-chain

# 그래프 (SVG)
systemd-analyze plot > boot.svg
```

## 🔗 연결 문서 (Related Documents)

- [[boot-sequence]] - 부팅 프로세스
- [[process-states-lifecycle]] - 프로세스와 서비스
- [[system-monitoring-commands]] - 시스템 모니터링
