---
title: network-diagnostic-tools
tags: [networking, tools, tcpdump, netstat, diagnostics, linux]
aliases: [네트워크 진단 도구, netstat, tcpdump, 패킷 캡처]
date modified: 2026-01-08 16:15:32 +09:00
date created: 2026-01-08 16:15:32 +09:00
---

## 🌐 개요 (Overview)

네트워크 설정 확인 및 문제 진단을 위한 주요 도구들을 다룹니다.

## 🔧 네트워크 설정 확인

### ipconfig (Windows) / ifconfig (Linux)

IP 주소, 서브넷 마스크, 게이트웨이, MAC 주소 등 인터페이스 설정을 확인합니다.

```bash
# Linux
ifconfig           # 전체 인터페이스
ifconfig eth0      # 특정 인터페이스
ip addr            # 권장 (최신)

# Windows
ipconfig           # 기본 정보
ipconfig /all      # 상세 정보 (MAC 포함)
ipconfig /release  # DHCP IP 해제
ipconfig /renew    # DHCP IP 갱신
ipconfig /flushdns # DNS 캐시 삭제
```

### ip 명령어 (Linux 권장)

```bash
# IP 주소 확인
ip addr show

# 라우팅 테이블
ip route show

# 이웃 (ARP) 테이블
ip neigh show

# 링크 상태
ip link show
```

---

## 🏓 연결 테스트

### ping

**ICMP Echo Request/Reply**를 이용해 호스트 도달 가능 여부와 응답 시간(RTT)을 측정합니다.

```bash
# 기본 ping
ping 8.8.8.8

# 횟수 제한 (Linux)
ping -c 4 google.com

# 횟수 제한 (Windows)
ping -n 4 google.com

# 패킷 크기 지정
ping -s 1000 192.168.1.1
```

### TTL (Time To Live)

패킷이 거쳐갈 수 있는 라우터의 수입니다. **OS마다 기본값이 다릅니다**.

| OS | 기본 TTL |
|-----|:-------:|
| **Windows** | 128 |
| **Linux** | 64 |
| **Cisco** | 255 |

> 응답의 TTL 값으로 **원격지 OS 추정** 가능

---

## 🛤️ 경로 추적

### traceroute (Linux) / tracert (Windows)

목적지까지 거쳐가는 **경로(라우터들)를 추적**합니다.

**원리**:
```plaintext
1. TTL=1인 패킷 전송 → 첫 번째 라우터에서 ICMP Time Exceeded
2. TTL=2인 패킷 전송 → 두 번째 라우터에서 Time Exceeded
3. 목적지 도착까지 반복
```

```bash
# Linux
traceroute google.com
traceroute -I google.com  # ICMP 사용
traceroute -T -p 80 google.com  # TCP 사용

# Windows
tracert google.com
```

**출력 예시**:
```plaintext
 1  192.168.1.1      1.234 ms
 2  10.0.0.1         5.678 ms
 3  * * *            (응답 없음)
 4  142.250.185.46  12.345 ms
```

---

## 📊 네트워크 상태 확인

### netstat

시스템의 현재 **네트워크 연결 상태**, 라우팅 테이블, 인터페이스 통계 등을 보여줍니다.

```bash
# 모든 연결 표시
netstat -a

# 숫자로 표시 (DNS 해석 안 함)
netstat -n

# 프로세스 표시 (Linux)
netstat -p

# 라우팅 테이블
netstat -r

# 조합: TCP 연결 + 숫자 + 프로세스
netstat -tnp   # Linux
netstat -ano   # Windows
```

### 주요 상태 코드

| 상태 | 설명 |
|------|------|
| **LISTEN** | 연결 대기 중 (서버) |
| **ESTABLISHED** | 연결됨 |
| **SYN_SENT** | 연결 요청 중 |
| **SYN_RECEIVED** | 연결 요청 수신 |
| **FIN_WAIT_1** | 종료 요청 전송 |
| **FIN_WAIT_2** | 종료 ACK 수신 |
| **TIME_WAIT** | 종료 대기 (2MSL) |
| **CLOSE_WAIT** | 종료 요청 수신 |
| **CLOSED** | 연결 없음 |

### ss (Linux 권장)

netstat의 현대적 대체품으로 더 빠르고 상세합니다.

```bash
# TCP 연결 + 숫자 + 프로세스
ss -tnp

# 리스닝 소켓
ss -tlnp

# UDP 소켓
ss -ulnp

# 통계
ss -s
```

---

## 📦 패킷 캡처

### tcpdump

Linux/Unix 환경의 강력한 **패킷 캡처 도구**입니다.

```bash
# 기본 캡처
sudo tcpdump -i eth0

# 특정 포트
sudo tcpdump -i eth0 port 80

# 특정 호스트
sudo tcpdump -i eth0 host 192.168.1.100

# 패킷 내용 표시 (ASCII)
sudo tcpdump -i eth0 -A port 80

# 패킷 내용 표시 (HEX + ASCII)
sudo tcpdump -i eth0 -X port 80

# 파일로 저장
sudo tcpdump -i eth0 -w capture.pcap

# 파일 읽기
tcpdump -r capture.pcap

# 필터 조합
sudo tcpdump -i eth0 'tcp port 80 and host 192.168.1.100'
```

### Promiscuous Mode (무차별 모드)

인터페이스를 Promiscuous Mode로 설정하면 **자신에게 오지 않는 패킷도 캡처** 가능합니다.

```bash
# 무차별 모드 활성화
sudo ip link set eth0 promisc on

# 확인
ip link show eth0
# PROMISC 플래그 확인

# 해제
sudo ip link set eth0 promisc off
```

---

## 📋 명령어 요약

| 명령어 | 용도 | 플랫폼 |
|--------|------|--------|
| `ifconfig` / `ip addr` | IP 설정 확인 | Linux |
| `ipconfig` | IP 설정 확인 | Windows |
| `ping` | 호스트 연결 테스트 | 공통 |
| `traceroute` / `tracert` | 경로 추적 | Linux / Windows |
| `netstat` / `ss` | 네트워크 상태 | 공통 / Linux |
| `tcpdump` | 패킷 캡처 | Linux |
| `arp` | ARP 테이블 | 공통 |
| `nslookup` / `dig` | DNS 조회 | 공통 / Linux |

---

## 💡 문제 해결 절차

```plaintext
1. 로컬 설정 확인
   ip addr / ipconfig

2. 게이트웨이 연결 확인
   ping [게이트웨이]

3. 외부 연결 확인
   ping 8.8.8.8

4. DNS 확인
   ping google.com
   nslookup google.com

5. 경로 확인
   traceroute google.com

6. 포트/연결 확인
   netstat -tnp | grep :443
```

## 🔗 연결 문서 (Related Documents)

- [icmp-protocol](icmp-protocol.md) - ping, traceroute 동작 원리
- [tcp-udp-protocols](tcp-udp-protocols.md) - TCP 상태 코드
- [routing-basics](routing-basics.md) - 라우팅과 게이트웨이
- [arp-protocol](arp-protocol.md) - ARP 테이블
