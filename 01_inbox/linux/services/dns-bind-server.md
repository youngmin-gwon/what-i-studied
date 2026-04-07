---
title: DNS/BIND Server
tags: [linux, network, dns, bind, named]
aliases: [DNS 서버, BIND, named]
date modified: 2026-01-06 19:35:00 +09:00
date created: 2026-01-06 19:35:00 +09:00
---

## 🌐 개요 (Overview)

**DNS (Domain Name System)**는 도메인 이름(예: `www.example.com`)을 IP 주소로 변환하는 시스템입니다. 리눅스에서 가장 널리 사용되는 DNS 서버 소프트웨어는 **BIND (Berkeley Internet Name Domain)**입니다.

---

## 🏗️ BIND 구성 요소

| 구성 요소 | 경로 (RHEL/CentOS 기준) | 설명 |
| :--- | :--- | :--- |
| **데몬** | `named` | BIND DNS 서버 프로세스 |
| **메인 설정 파일** | `/etc/named.conf` | 서버 전역 설정 및 Zone 정의 |
| **Zone 파일 디렉토리** | `/var/named/` | 실제 DNS 레코드가 저장된 Zone 파일들 |
| **서비스 관리** | `systemctl start named` | 서비스 시작/중지 |

---

## 📄 /etc/named.conf 구조

```bash
options {
    listen-on port 53 { 127.0.0.1; 192.168.1.1; };  # 청취할 IP
    directory "/var/named";                          # Zone 파일 위치
    allow-query { any; };                            # 질의 허용 범위
    recursion yes;                                   # 재귀 질의 허용
    forwarders { 8.8.8.8; 8.8.4.4; };               # 포워딩 서버
};

zone "example.com" IN {
    type master;                                     # 주(Primary) 서버
    file "example.com.zone";                         # Zone 파일 이름
    allow-update { none; };
};

zone "1.168.192.in-addr.arpa" IN {
    type master;
    file "192.168.1.rev";                            # 역방향 Zone 파일
};
```

---

## 📝 Zone 파일 형식

### 정방향 Zone 파일 (`/var/named/example.com.zone`)

```
$TTL 86400
@   IN  SOA   ns1.example.com. admin.example.com. (
                2026010601  ; Serial (YYYYMMDDNN 형식)
                3600        ; Refresh (1시간)
                1800        ; Retry (30분)
                604800      ; Expire (1주)
                86400 )     ; Minimum TTL (1일)

; NS 레코드 (네임서버)
@       IN  NS      ns1.example.com.
@       IN  NS      ns2.example.com.

; A 레코드 (호스트 -> IP)
@       IN  A       192.168.1.10
ns1     IN  A       192.168.1.1
ns2     IN  A       192.168.1.2
www     IN  A       192.168.1.10
ftp     IN  A       192.168.1.20

; CNAME 레코드 (별칭)
mail    IN  CNAME   www

; MX 레코드 (메일 서버)
@       IN  MX  10  mail.example.com.
```

### 역방향 Zone 파일 (`/var/named/192.168.1.rev`)

```
$TTL 86400
@   IN  SOA   ns1.example.com. admin.example.com. (
                2026010601
                3600
                1800
                604800
                86400 )

@       IN  NS      ns1.example.com.

; PTR 레코드 (IP -> 호스트)
10      IN  PTR     www.example.com.
1       IN  PTR     ns1.example.com.
2       IN  PTR     ns2.example.com.
```

---

## 📊 DNS 레코드 타입 비교

| 레코드 | 이름 | 용도 | 예시 |
| :--- | :--- | :--- | :--- |
| **SOA** | Start of Authority | Zone의 권한 정보 (시리얼, TTL 등) | `@ IN SOA ns1... admin...` |
| **NS** | Name Server | 도메인의 네임서버 지정 | `@ IN NS ns1.example.com.` |
| **A** | Address | 호스트명 → IPv4 주소 | `www IN A 192.168.1.10` |
| **AAAA** | IPv6 Address | 호스트명 → IPv6 주소 | `www IN AAAA 2001:db8::1` |
| **CNAME** | Canonical Name | 별칭 (다른 도메인으로 연결) | `mail IN CNAME www` |
| **MX** | Mail Exchanger | 메일 서버 지정 (우선순위 포함) | `@ IN MX 10 mail.example.com.` |
| **PTR** | Pointer | IP 주소 → 호스트명 (역방향) | `10 IN PTR www.example.com.` |
| **TXT** | Text | SPF, DKIM 등 텍스트 정보 | `@ IN TXT "v=spf1 ..."` |

> [!IMPORTANT]
> **시험 Tip**: **PTR 레코드**는 역방향 조회(IP → 도메인)에 사용됩니다. 역방향 Zone 파일에서만 사용됩니다.

---

## 🔧 관리 명령어

```bash
# 설정 파일 문법 검사
named-checkconf /etc/named.conf

# Zone 파일 문법 검사
named-checkzone example.com /var/named/example.com.zone

# 서비스 재시작
systemctl restart named

# Zone 리로드 (재시작 없이)
rndc reload

# 캐시 초기화
rndc flush
```

---

## 🔗 연결 문서 (Related Documents)

- [[network-fundamentals]] - 네트워크 기본 개념 및 DNS 설정
- [[commands/network-commands|네트워크 명령어 (dig, nslookup)]]
- [[network-security-protocols]] - DNSSEC
