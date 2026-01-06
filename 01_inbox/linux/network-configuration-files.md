---
title: 네트워크 설정 파일
tags: [linux, networking, configuration, redhat, centos]
aliases: [Network Configuration Files, 네트워크 설정, ifcfg]
date modified: 2026-01-06 21:45:00 +09:00
date created: 2026-01-06 21:45:00 +09:00
---

## 🌐 개요 (Overview)

리눅스에서 네트워크를 설정하는 주요 파일들과 관련 명령어를 설명합니다. Red Hat 계열 (RHEL, CentOS, Fedora)과 Debian 계열 간 차이가 있습니다.

---

## 📁 Red Hat 계열 설정 파일

### /etc/sysconfig/network

**시스템 전체** 네트워크 설정 (호스트명, 게이트웨이, 네트워크 사용 여부)

```bash
NETWORKING=yes               # 부팅 시 네트워크 사용 여부
HOSTNAME=myserver.example.com
GATEWAY=192.168.1.1
```

> [!IMPORTANT]
> **시험 포인트**: 부팅 시 네트워크 사용 유무 지정 → `/etc/sysconfig/network`

### /etc/sysconfig/network-scripts/ifcfg-*

각 **인터페이스별** IP 주소 설정

```bash
# /etc/sysconfig/network-scripts/ifcfg-eth0
DEVICE=eth0
BOOTPROTO=static            # static | dhcp | none
ONBOOT=yes                  # 부팅 시 활성화
IPADDR=192.168.1.100
NETMASK=255.255.255.0
GATEWAY=192.168.1.1
DNS1=8.8.8.8
DNS2=8.8.4.4
```

> [!TIP]
> **시험 포인트**: 이더넷 카드 1개 장착 시 IP 기록 파일 → `/etc/sysconfig/network-scripts/ifcfg-eth0`

### /etc/networks

네트워크 이름과 네트워크 주소 매핑 (잘 사용되지 않음)

```bash
loopback    127.0.0.0
link-local  169.254.0.0
```

---

## 📁 Debian 계열 설정 파일

### /etc/network/interfaces

```bash
# /etc/network/interfaces
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet static
    address 192.168.1.100
    netmask 255.255.255.0
    gateway 192.168.1.1
    dns-nameservers 8.8.8.8 8.8.4.4
```

---

## 🔄 네트워크 서비스 재시작

설정 파일 변경 후 네트워크 서비스를 재시작해야 합니다.

```bash
# Red Hat/CentOS (SysVinit)
service network restart
/etc/rc.d/init.d/network restart
/etc/init.d/network restart

# systemd (RHEL 7+, Ubuntu 16+)
systemctl restart NetworkManager
systemctl restart network       # RHEL/CentOS

# Debian/Ubuntu
systemctl restart networking
```

> [!WARNING]
> **틀린 방법**: `/etc/network restart` (이런 경로는 없음!)
>
> **올바른 방법**:
> - `service network restart`
> - `/etc/rc.d/init.d/network restart`
> - `/etc/init.d/network restart`

---

## 🛠️ 네트워크 진단 도구

### mii-tool - 이더넷 링크 상태 (레거시)

```bash
# 링크 상태 확인
mii-tool eth0

# 출력 예시
eth0: negotiated 100baseTx-FD, link ok
```

### ethtool - 이더넷 설정 (현대)

```bash
# 인터페이스 정보 확인
ethtool eth0

# 출력 예시
eth0: no autonegotiation, 100baseTx-FD, link ok

# 속도/듀플렉스 설정
ethtool -s eth0 speed 1000 duplex full

# 드라이버 정보
ethtool -i eth0
```

> [!TIP]
> **시험 포인트**: `ethtool eth0` 명령은 이더넷 인터페이스의 상세 정보(속도, 듀플렉스, autonegotiation)를 확인합니다.

---

## 📊 netstat 상태값

```bash
netstat -ant
```

| 상태 | 설명 |
| :--- | :--- |
| **LISTEN** | 연결 대기 중 (서버) |
| **SYN_SENT** | 클라이언트가 SYN 전송 후 대기 |
| **SYN_RECEIVED** | SYN 받고 SYN+ACK 전송 후 대기 |
| **ESTABLISHED** | 연결 완료 |
| **TIME_WAIT** | 연결 종료 후 대기 |
| **CLOSE_WAIT** | 상대방 종료 요청 수신 |

> [!IMPORTANT]
> **시험 포인트**: 서버가 클라이언트로부터 접속 요구(SYN)를 받고 응답(SYN+ACK)을 보냈지만 아직 확인(ACK)을 받지 못한 상태 → **SYN_RECEIVED**

---

## ⚙️ ip 명령 (통합 도구)

`ip` 명령은 ifconfig, route, arp 등을 대체하는 현대적 도구입니다.

| 기능 | 명령어 |
| :--- | :--- |
| IP 주소 확인 | `ip addr` |
| IP 주소 추가 | `ip addr add 192.168.1.100/24 dev eth0` |
| IP 주소 삭제 | `ip addr del 192.168.1.100/24 dev eth0` |
| 인터페이스 활성화 | `ip link set eth0 up` |
| 인터페이스 비활성화 | `ip link set eth0 down` |
| 라우팅 테이블 | `ip route` |
| 게이트웨이 추가 | `ip route add default via 192.168.1.1` |

> [!TIP]
> **시험 포인트**: IP 확인, 라우팅 테이블, 게이트웨이 설정을 모두 할 수 있는 명령 → `ip`

---

## 🔍 연결 확인 명령어

| 명령어 | 용도 |
| :--- | :--- |
| `ip addr`, `ifconfig` | IP 주소 확인 |
| `ss`, `netstat` | 소켓/포트 상태 확인 |
| `route`, `ip route` | 게이트웨이 확인 |
| `tracepath`, `traceroute` | 경로 추적 |
| `arp` | ARP 테이블 (MAC-IP 매핑) |

---

## 🔗 연결 문서 (Related Documents)

- [[network-fundamentals]] - 네트워크 기초
- [[network-commands]] - 네트워크 명령어
- [[systemd]] - systemctl 서비스 관리
