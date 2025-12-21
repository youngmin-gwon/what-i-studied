---
title: Network Commands
tags: [linux, commands, networking, ip, ping, curl]
aliases: [네트워크 명령어, Network, ip, ifconfig]
date modified: 2025-12-20 13:59:24 +09:00
date created: 2025-12-20 13:59:24 +09:00
---

## 🌐 개요 (Overview)

[[tcp-ip-model|네트워크]] 설정, 진단, 데이터 전송 명령어들입니다.

## 📋 Quick Reference

| 명령어 | 용도 |
|--------|------|
| `ip` | 네트워크 설정 (현대) |
| `ifconfig` | 네트워크 설정 (레거시) |
| `ping` | 연결 테스트 |
| `traceroute` | 경로 추적 |
| `netstat|ss` | 네트워크 연결 |
| `dig`/`nslookup` | [[dns-fundamentals\|DNS]] 조회 |
| `curl`/`wget` | HTTP 전송 |
| `scp`/`rsync` | 파일 전송 |

## 🔧 Network Configuration

### ip - Network Configuration

```bash
# 인터페이스 확인
ip addr                    # IP 주소
ip link                    # 링크 상태
ip -s link                 # 통계 포함

# IP 추가/삭제
ip addr add 192.168.1.100/24 dev eth0
ip addr del 192.168.1.100/24 dev eth0

# 인터페이스 활성화/비활성화
ip link set eth0 up
ip link set eth0 down

# 라우팅
ip route                   # 라우팅 테이블
ip route add default via 192.168.1.1
ip route del default
ip route get 8.8.8.8       # 경로 확인
```

### ifconfig - Legacy Network Config

```bash
ifconfig                   # 모든 인터페이스
ifconfig eth0              # 특정 인터페이스
ifconfig eth0 up           # 활성화
ifconfig eth0 192.168.1.100 netmask 255.255.255.0
```

## 🔍 Network Diagnostics

### ping - Test Connectivity

```bash
ping 8.8.8.8               # 기본
ping -c 4 google.com       # 4회
ping -i 0.5 192.168.1.1    # 0.5초 간격
ping -s 1000 host          # 패킷 크기
```

### traceroute - Trace Route

```bash
traceroute google.com
traceroute -n google.com   # 숫자로만
tracepath google.com       # root 불필요
mtr google.com             # 실시간 traceroute
```

### netstat - Network Statistics

```bash
netstat -tulpn             # TCP/UDP Listen
netstat -an                # 모든 연결
netstat -r                 # 라우팅 테이블
netstat -i                 # 인터페이스 통계
```

### ss - Socket Statistics (현대)

```bash
ss -tulpn                  # Listen 포트
ss -tan                    # TCP 연결
ss -s                      # 통계
ss src 192.168.1.100       # 소스 IP
```

## 🌐 DNS Tools

### dig - DNS Lookup

```bash
dig google.com             # A 레코드
dig google.com MX          # MX 레코드
dig @8.8.8.8 google.com    # 특정 DNS 서버
dig +short google.com      # 간단히
dig -x 8.8.8.8             # 역방향
dig google.com +trace      # 추적
```

### nslookup - DNS Query

```bash
nslookup google.com
nslookup google.com 8.8.8.8
```

### host - DNS Lookup

```bash
host google.com
host -t MX google.com
host 8.8.8.8               # 역방향
```

## 📥 Data Transfer

### curl - Transfer Data

```bash
curl https://example.com
curl -o file.html https://example.com
curl -O https://example.com/file.zip
curl -I https://example.com         # 헤더만
curl -L https://example.com         # 리다이렉트 따라가기
curl -u user:pass https://api.com   # 인증
curl -X POST -d "data" https://api.com
curl -H "Content-Type: application/json" -d '{"key":"value"}' https://api.com
```

### wget - Download Files

```bash
wget https://example.com/file.zip
wget -c https://example.com/file.zip    # 이어받기
wget -r https://example.com             # 재귀
wget -b https://example.com/large.zip   # 백그라운드
wget --limit-rate=200k https://file.zip # 속도 제한
```

### scp - Secure Copy

```bash
scp file.txt user@host:/path/
scp user@host:/path/file.txt ./
scp -r directory/ user@host:/path/
scp -P 2222 file.txt user@host:/path/   # 포트
```

### rsync - Remote Sync

```bash
rsync -av source/ dest/
rsync -av user@host:/path/ ./
rsync -avz --delete source/ dest/       # 압축, 미러링
rsync -av --progress source/ dest/
```

## 🔥 Firewall

### iptables - Firewall

```bash
iptables -L                # 규칙 목록
iptables -L -n             # 숫자로
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -s 192.168.1.0/24 -j ACCEPT
iptables -D INPUT 5        # 5번 규칙 삭제
```

### ufw - Ubuntu Firewall

```bash
ufw status
ufw enable
ufw allow 22
ufw allow 80/tcp
ufw deny from 192.168.1.100
ufw delete allow 80
```

### firewall-cmd - firewalld

```bash
firewall-cmd --list-all
firewall-cmd --add-service=http --permanent
firewall-cmd --add-port=8080/tcp --permanent
firewall-cmd --reload
```

## 💡 Scenarios

### 네트워크 문제 진단

```bash
# 1. 연결 확인
ping 8.8.8.8
ping google.com

# 2. DNS 확인
dig google.com

# 3. 라우팅 확인
ip route
traceroute google.com

# 4. 포트 확인
ss -tulpn | grep :80
```

### 포트 열림 확인

```bash
nc -zv host 80             # netcat
telnet host 80
curl -v telnet://host:80
```

## 🔗 연결 문서 (Related Documents)

- [[tcp-ip-model]] - 네트워크 계층
- [[ip-addressing]] - IP 주소 체계
- [[dns-fundamentals]] - DNS
- [[routing-basics]] - 라우팅
- [[network-security-protocols]] - SSH, TLS
