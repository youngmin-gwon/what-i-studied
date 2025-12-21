---
title: Linux Security Commands
tags: [linux, commands, security, firewall, selinux, iptables]
aliases: [보안 명령어, Security, iptables, SELinux]
date modified: 2025-12-20 14:06:33 +09:00
date created: 2025-12-20 14:06:33 +09:00
---

## 🌐 개요 (Overview)

Linux 시스템 보안 관련 명령어들입니다. 방화벽, SELinux, 보안 감사 등을 다룹니다.

## 📋 Quick Reference

| 명령어 | 용도 |
|--------|------|
| `iptables` | 방화벽 규칙 관리 |
| `firewall-cmd` | firewalld 관리 (RHEL/CentOS) |
| `ufw` | 방화벽 (Ubuntu) |
| `getenforce`/`setenforce` | [[selinux]] 모드 확인/변경 |
| `chcon`/`restorecon` | SELinux 컨텍스트 |
| `ausearch`/`aureport` | 보안 감사 로그 |

## 🔥 Firewall - iptables

### 기본 구조

```
iptables -t [table] [action] [chain] [rule] -j [target]
```

**Tables**:
- `filter`: 기본, 패킷 필터링
- `nat`: NAT
- `mangle`: 패킷 수정

**Chains**:
- `INPUT`: 들어오는 패킷
- `OUTPUT`: 나가는 패킷
- `FORWARD`: 포워딩 패킷

**Targets**:
- `ACCEPT`: 허용
- `DROP`: 차단 (조용히)
- `REJECT`: 차단 (ICMP 응답)
- `LOG`: 로그 기록

### 규칙 조회

```bash
iptables -L                    # 규칙 목록
iptables -L -n                 # 숫자로 표시 (빠름)
iptables -L -v                 # 상세 정보
iptables -L -n -v --line-numbers  # 줄 번호 포함

iptables -t nat -L             # NAT 테이블
iptables -S                    # 규칙을 명령어 형식으로
```

### 규칙 추가

```bash
# INPUT 체인에 추가
iptables -A INPUT -p tcp --dport 22 -j ACCEPT        # SSH 허용
iptables -A INPUT -p tcp --dport 80 -j ACCEPT        # HTTP 허용
iptables -A INPUT -p tcp --dport 443 -j ACCEPT       # HTTPS 허용

# 특정 IP만 허용
iptables -A INPUT -s 192.168.1.100 -j ACCEPT

# 네트워크 대역 허용
iptables -A INPUT -s 192.168.1.0/24 -j ACCEPT

# 인터페이스 지정
iptables -A INPUT -i eth0 -p tcp --dport 22 -j ACCEPT

# ESTABLISHED 연결 허용 (중요!)
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
```

### 규칙 삭제

```bash
# 줄 번호로 삭제
iptables -D INPUT 5

# 규칙 지정하여 삭제
iptables -D INPUT -p tcp --dport 80 -j ACCEPT

# 체인 전체 삭제
iptables -F INPUT
iptables -F                    # 모든 체인
```

### 기본 정책 설정

```bash
# 기본 DROP (화이트리스트 방식)
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# 기본 ACCEPT (블랙리스트 방식)
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
```

### NAT 설정

```bash
# 포트 포워딩 (8080 → 80)
iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80

# SNAT (출발지 IP 변경)
iptables -t nat -A POSTROUTING -o eth0 -j SNAT --to-source 1.2.3.4

# MASQUERADE (동적 IP용 SNAT)
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

### 규칙 저장/복원

```bash
# Debian/Ubuntu
iptables-save > /etc/iptables/rules.v4
iptables-restore < /etc/iptables/rules.v4

# RHEL/CentOS
service iptables save
service iptables restart
```

### 실용 예제: 기본 방화벽

```bash
#!/bin/bash
# 기본 방화벽 설정

# 1. 모든 규칙 초기화
iptables -F
iptables -X
iptables -t nat -F

# 2. 기본 정책: DROP
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# 3. loopback 허용
iptables -A INPUT -i lo -j ACCEPT

# 4. ESTABLISHED 연결 허용
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# 5. SSH 허용
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# 6. HTTP/HTTPS 허용
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# 7. ping 허용
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT

# 8. 저장
iptables-save > /etc/iptables/rules.v4
```

## 🔥 firewalld (RHEL/CentOS)

### 기본 명령어

```bash
# 상태 확인
systemctl status firewalld
firewall-cmd --state

# 시작/중지
systemctl start firewalld
systemctl stop firewalld
systemctl enable firewalld
```

### Zone 관리

```bash
# Zone 목록
firewall-cmd --get-zones
firewall-cmd --get-active-zones
firewall-cmd --get-default-zone

# Zone 변경
firewall-cmd --set-default-zone=public

# 인터페이스 zone 지정
firewall-cmd --zone=dmz --change-interface=eth0 --permanent
```

### 서비스/포트 관리

```bash
# 서비스 허용
firewall-cmd --add-service=http
firewall-cmd --add-service=https
firewall-cmd --add-service=ssh

# 영구 적용
firewall-cmd --add-service=http --permanent
firewall-cmd --reload

# 포트 허용
firewall-cmd --add-port=8080/tcp
firewall-cmd --add-port=3000-3010/tcp          # 범위

# 제거
firewall-cmd --remove-service=http
firewall-cmd --remove-port=8080/tcp

# 목록 확인
firewall-cmd --list-all
firewall-cmd --list-services
firewall-cmd --list-ports
```

### Rich Rules

```bash
# 특정 IP만 SSH 허용
firewall-cmd --add-rich-rule='rule family="ipv4" source address="192.168.1.100" service name="ssh" accept'

# IP 차단
firewall-cmd --add-rich-rule='rule family="ipv4" source address="10.0.0.0/8" reject'

# 포트 포워딩
firewall-cmd --add-forward-port=port=80:proto=tcp:toport=8080
```

## 🔥 ufw (Ubuntu)

### 기본 사용

```bash
# 상태
sudo ufw status
sudo ufw status verbose

# 활성화/비활성화
sudo ufw enable
sudo ufw disable

# 기본 정책
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

### 규칙 관리

```bash
# 포트 허용
sudo ufw allow 22
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# 서비스 허용
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https

# 특정 IP 허용
sudo ufw allow from 192.168.1.100
sudo ufw allow from 192.168.1.0/24 to any port 22

# 규칙 삭제
sudo ufw delete allow 80
sudo ufw delete 5                      # 번호로

# 목록
sudo ufw status numbered
```

## 🔒 SELinux Commands

### 모드 관리

```bash
# 현재 모드 확인
getenforce                             # Enforcing/Permissive/Disabled

# 상세 정보
sestatus

# 모드 변경 (임시)
setenforce 0                           # Permissive
setenforce 1                           # Enforcing

# 영구 변경: /etc/selinux/config
# SELINUX=enforcing
```

### 컨텍스트 관리

```bash
# 컨텍스트 확인
ls -Z /var/www/html/
ps -eZ | grep httpd
id -Z

# 컨텍스트 변경 (임시)
chcon -t httpd_sys_content_t /var/www/html/index.html
chcon -R -t httpd_sys_content_t /var/www/html/

# 기본 컨텍스트로 복원
restorecon -v /var/www/html/index.html
restorecon -Rv /var/www/html/

# 기본 컨텍스트 설정 (영구)
semanage fcontext -a -t httpd_sys_content_t "/var/www/html(/.*)?"
restorecon -Rv /var/www/html
```

### Boolean 관리

```bash
# Boolean 목록
getsebool -a
getsebool httpd_can_network_connect

# Boolean 변경 (임시)
setsebool httpd_can_network_connect on

# Boolean 변경 (영구)
setsebool -P httpd_can_network_connect on
```

### 로그 및 문제 해결

```bash
# AVC denial 확인
ausearch -m avc -ts recent
ausearch -m avc -ts today

# 거부 이유
audit2why < /var/log/audit/audit.log

# 정책 제안 (주의: 검토 필요)
audit2allow -a
audit2allow -a -M my_policy              # 모듈 생성
semodule -i my_policy.pp                 # 모듈 로드
```

### 포트 레이블 관리

```bash
# 포트 확인
semanage port -l | grep http

# 포트 추가
semanage port -a -t http_port_t -p tcp 8080

# 포트 삭제
semanage port -d -t http_port_t -p tcp 8080
```

## 🔍 보안 감사

### auditd

```bash
# 서비스 관리
systemctl status auditd
systemctl start auditd

# 감사 규칙
auditctl -l                            # 규칙 목록
auditctl -w /etc/passwd -p wa -k passwd_changes  # 파일 감시
auditctl -w /etc/shadow -p wa -k shadow_changes

# 로그 검색
ausearch -m USER_LOGIN -ts today       # 로그인
ausearch -k passwd_changes             # 키로 검색
ausearch -ui 1000                      # UID로

# 보고서
aureport                               # 요약
aureport -au                           # 인증
aureport -f                            # 파일
aureport -l                            # 로그인
```

## 💡 Scenarios

### 웹 서버 방화벽 설정

```bash
# iptables
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# firewalld
firewall-cmd --add-service=http --permanent
firewall-cmd --add-service=https --permanent
firewall-cmd --reload

# ufw
sudo ufw allow 'Nginx Full'
# 또는
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
```

### SELinux 문제 해결

```bash
# 1. 로그 확인
ausearch -m avc -ts recent

# 2. 왜 거부되었는지 확인
audit2why < /var/log/audit/audit.log

# 3. Boolean 확인
getsebool -a | grep httpd

# 4. 필요시 Boolean 활성화
setsebool -P httpd_can_network_connect on

# 5. 컨텍스트 확인
ls -Z /var/www/html

# 6. 컨텍스트 복원
restorecon -Rv /var/www/html
```

## 🔗 연결 문서 (Related Documents)

- [[selinux]] - SELinux 상세 개념
- [[network-commands]] - 네트워크 명령어
- [[system-monitoring-commands]] - 로그 모니터링
- [[firewall-ids-ips]] - 방화벽/IDS/IPS 개념
