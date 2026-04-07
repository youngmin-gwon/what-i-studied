---
title: network-security-protocols
tags: [ipsec, networking, security, ssh, ssl, tls, vpn]
aliases: [IPSec, SSH, SSL, TLS, VPN]
date modified: 2026-04-07 15:13:43 +09:00
date created: 2025-12-20 00:17:40 +09:00
---

## 🌐 개요 (Overview)

네트워크 보안 프로토콜은 [[tcp-ip-model|TCP/IP 네트워크]] 에서 안전한 통신을 제공하는 프로토콜입니다. 기밀성, 무결성, 인증을 보장하여 중간자 공격, 도청, 데이터 변조를 방지합니다.

## 🔐 TLS/SSL (Transport Layer Security)

### TLS Handshake

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    
    Note over C,S: 1. Hello 단계
    C->>S: ClientHello (지원 암호 스위트, 랜덤값)
    S->>C: ServerHello (선택 암호 스위트, 랜덤값)
    S->>C: Certificate (서버 인증서)
    S->>C: ServerHelloDone
    
    Note over C,S: 2. 키 교환
    C->>C: 인증서 검증
    C->>S: ClientKeyExchange (Pre-Master Secret 암호화)
    C->>S: ChangeCipherSpec
    C->>S: Finished (암호화됨)
    
    S->>S: Master Secret 생성
    S->>C: ChangeCipherSpec
    S->>C: Finished (암호화됨)
    
    Note over C,S: 3. 암호화 통신 시작
    C->>S: Application Data (암호화)
    S->>C: Application Data (암호화)
```

### TLS 버전

| 버전 | 출시 | 상태 | 주요 특징 |
|------|------|------|-----------|
| SSL 2.0 | 1995 | ❌ Deprecated | 치명적 취약점 |
| SSL 3.0 | 1996 | ❌ Deprecated | POODLE 공격 |
| TLS 1.0 | 1999 | ❌ Deprecated | BEAST 공격 |
| TLS 1.1 | 2006 | ❌ Deprecated | - |
| TLS 1.2 | 2008 | ✅ 사용 중 | SHA-256, GCM |
| TLS 1.3 | 2018 | ✅ 권장 | 1-RTT, 0-RTT, 단순화 |

### TLS 1.3 개선사항

- **빠른 핸드셰이크**: 1-RTT (왕복 1 회)
- **0-RTT 재개**: 이전 세션 재사용
- **암호 스위트 단순화**: 안전한 알고리즘만
- **Perfect Forward Secrecy**: 기본 활성화

## 🛡️ IPSec (Internet Protocol Security)

### 구성 요소

1. **AH (Authentication Header)**
   - 무결성 + 인증
   - 암호화 없음
   - 프로토콜 번호: 51

2. **ESP (Encapsulating Security Payload)**
   - 무결성 + 인증 + **암호화**
   - 프로토콜 번호: 50
   - 일반적으로 ESP 사용

### 모드

```mermaid
graph TB
    subgraph "Transport Mode"
        T1[IP Header] --> T2[ESP Header]
        T2 --> T3[Original Data]
        T3 --> T4[ESP Trailer]
        
        style T3 fill:#9f9
    end
    
    subgraph "Tunnel Mode"
        TU1[New IP Header] --> TU2[ESP Header]
        TU2 --> TU3[Original IP Header]
        TU3 --> TU4[Original Data]
        TU4 --> TU5[ESP Trailer]
        
        style TU3 fill:#9f9
        style TU4 fill:#9f9
    end
```

**Transport Mode**: 데이터만 암호화 (호스트 간)

**Tunnel Mode**: 전체 IP 패킷 암호화 (VPN)

### IKE (Internet Key Exchange)

**Phase 1**: SA (Security Association) 수립

**Phase 2**: IPSec SA 협상

## 🔑 SSH (Secure Shell)

### SSH 프로토콜 계층

```
SSH-USERAUTH (인증)
SSH-CONNECTION (채널 다중화)
SSH-TRANS (전송 계층 - 암호화)
TCP (포트 22)
```

### 인증 방식

1. **Password**: 패스워드 인증
2. **Public Key**: [[cryptography-basics|공개키]] 인증 (권장)
3. **Host-based**: 호스트 기반
4. **Keyboard-interactive**: 동적 챌린지

### 공개키 인증

```bash
# 1. 키 쌍 생성
ssh-keygen -t ed25519 -C "email@example.com"
# 또는
ssh-keygen -t rsa -b 4096

# 2. 공개키를 서버에 복사
ssh-copy-id user@server

# 3. 로그인 (패스워드 없이)
ssh user@server
```

### SSH 터널링

```bash
# Local Port Forwarding
ssh -L 8080:localhost:80 user@server

# Remote Port Forwarding  
ssh -R 8080:localhost:3000 user@server

# Dynamic Port Forwarding (SOCKS 프록시)
ssh -D 1080 user@server
```

## 🌐 VPN (Virtual Private Network)

### VPN 유형

```mermaid
graph TB
    subgraph "Site-to-Site VPN"
        Office1[본사] --- VPN1[VPN Gateway]
        VPN1 -.Internet.-> VPN2[VPN Gateway]
        VPN2 --- Office2[지사]
    end
    
    subgraph "Remote Access VPN"
        User[원격 사용자] -.VPN Client.-> Gateway[VPN Gateway]
        Gateway --- Corp[기업 네트워크]
    end
```

### VPN 프로토콜

| 프로토콜 | 계층 | 암호화 | 속도 | 용도 |
|----------|------|--------|------|------|
| **PPTP** | L2 | ❌ 취약 | 빠름 | 사용 금지 |
| **L2TP/IPSec** | L2 | ✅ IPSec | 중간 | 레거시 |
| **OpenVPN** | SSL/TLS | ✅ 강력 | 중간 | 범용 |
| **WireGuard** | L3 | ✅ 경량 | 매우 빠름 | 최신 권장 |
| **IKEv2/IPSec** | L3 | ✅ 강력 | 빠름 | 모바일 |

### WireGuard

- **경량**: 4,000 줄 미만 코드
- **빠름**: 기존 VPN 대비 3~4 배
- **모던 암호**: ChaCha20, Curve25519
- **간단한 설정**

```ini
[Interface]
PrivateKey = <client-private-key>
Address = 10.0.0.2/24

[Peer]
PublicKey = <server-public-key>
Endpoint = server.example.com:51820
AllowedIPs = 0.0.0.0/0
```

## 🔒 HTTPS (HTTP over TLS)

### 인증서 체인

```mermaid
graph TB
    Root[Root CA<br/>신뢰 저장소] -->|서명| Int[Intermediate CA]
    Int -->|서명| Leaf[www.example.com<br/>End-Entity 인증서]
    
    Browser[브라우저] -.검증.-> Leaf
    Browser -.검증.-> Int
    Browser -.검증.-> Root
    
    style Root fill:#f99
    style Browser fill:#99f
```

### HSTS (HTTP Strict Transport Security)

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

**효과**:

- HTTP 자동 HTTPS 전환
- 중간자 공격 방지
- 인증서 경고 무시 방지

## 🔗 연결 문서 (Related Documents)

- [[cryptography-basics]] - 암호화 알고리즘
- [[tcp-ip-model]] - 네트워크 프로토콜 스택
- [[authentication-authorization]] - 인증 메커니즘
- [[dns-fundamentals]] - DNS over HTTPS/TLS
