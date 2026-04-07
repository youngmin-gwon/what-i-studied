---
title: dhcp-server
tags: [dhcp, dhcpd, linux, network]
aliases: [DHCP 서버, dhcpd]
date modified: 2026-04-07 10:42:30 +09:00
date created: 2026-01-06 19:44:00 +09:00
---

## 🌐 개요 (Overview)

**DHCP (Dynamic Host Configuration Protocol)**는 네트워크 장치에 IP 주소, 서브넷 마스크, 게이트웨이, DNS 서버 등의 네트워크 구성 정보를 자동으로 할당하는 프로토콜입니다.

---

## 📦 설치 및 서비스

```bash
# RHEL/CentOS
dnf install dhcp-server
systemctl enable --now dhcpd

# Ubuntu/Debian
apt install isc-dhcp-server
systemctl enable --now isc-dhcp-server
```

---

## ⚙️ /etc/dhcp/dhcpd.conf 설정

### 기본 구조

```bash
# 전역 설정
option domain-name "example.com";
option domain-name-servers 192.168.1.1, 8.8.8.8;

# 기본 임대 시간 (초 단위)
default-lease-time 600;      # 10분 (기본값)
max-lease-time 7200;         # 최대 2시간

# 서브넷 정의
subnet 192.168.1.0 netmask 255.255.255.0 {
    range 192.168.1.100 192.168.1.200;        # IP 할당 범위
    option routers 192.168.1.1;               # 기본 게이트웨이
    option subnet-mask 255.255.255.0;
    option broadcast-address 192.168.1.255;
}
```

### 주요 옵션

| 옵션 | 설명 | 예시 |
| :--- | :--- | :--- |
| **default-lease-time** | 기본 IP 임대 시간 (초) | `600` (10 분) |
| **max-lease-time** | 최대 IP 임대 시간 (초) | `7200` (2 시간) |
| **range** | 동적 할당할 IP 범위 | `192.168.1.100 192.168.1.200` |
| **option routers** | 기본 게이트웨이 | `192.168.1.1` |
| **option domain-name-servers** | DNS 서버 | `8.8.8.8, 8.8.4.4` |
| **option domain-name** | 도메인 이름 | `"example.com"` |

>[!IMPORTANT]
>**시험 Tip**: `default-lease-time` 은 클라이언트가 요청하지 않을 경우의 기본 임대 시간이고, `max-lease-time` 은 클라이언트가 요청해도 넘을 수 없는 최대값입니다.

---

## 🔒 고정 IP 할당 (예약)

특정 MAC 주소에 항상 같은 IP 를 할당합니다.

```bash
host printer {
    hardware ethernet 00:11:22:33:44:55;
    fixed-address 192.168.1.50;
}

host server1 {
    hardware ethernet aa:bb:cc:dd:ee:ff;
    fixed-address 192.168.1.10;
    option host-name "server1";
}
```

---

## 📄 전체 설정 예시

```bash
# /etc/dhcp/dhcpd.conf

# 글로벌 옵션
authoritative;
option domain-name "mycompany.local";
option domain-name-servers 192.168.1.1, 8.8.8.8;

default-lease-time 3600;     # 1시간
max-lease-time 86400;        # 24시간

# 서브넷 정의
subnet 192.168.1.0 netmask 255.255.255.0 {
    range 192.168.1.100 192.168.1.200;
    option routers 192.168.1.1;
    option subnet-mask 255.255.255.0;
    option broadcast-address 192.168.1.255;
}

# 고정 IP 예약
host boss-laptop {
    hardware ethernet 00:aa:bb:cc:dd:ee;
    fixed-address 192.168.1.10;
}
```

---

## 🔧 관리 및 확인

```bash
# 설정 문법 검사
dhcpd -t -cf /etc/dhcp/dhcpd.conf

# 서비스 재시작
systemctl restart dhcpd

# 현재 임대 정보 확인
cat /var/lib/dhcpd/dhcpd.leases
```

### 임대 파일 형식 예시

```
lease 192.168.1.150 {
  starts 1 2026/01/06 10:30:00;
  ends 1 2026/01/06 11:30:00;
  cltt 1 2026/01/06 10:30:00;
  binding state active;
  hardware ethernet 00:11:22:33:44:55;
  client-hostname "client1";
}
```

---

## 💻 클라이언트 측 명령어

```bash
# IP 갱신 요청
dhclient -r           # 현재 IP 해제
dhclient eth0         # 새 IP 요청

# NetworkManager 환경
nmcli connection reload
nmcli device reapply eth0
```

---

## 🔗 연결 문서 (Related Documents)

- [[dns-bind-server]] - DNS 서버 설정
- [[network-commands]] - 네트워크 명령어
- [[network-configuration]] - 네트워크 인터페이스 설정
