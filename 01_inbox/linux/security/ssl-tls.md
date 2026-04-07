---
title: ssl-tls
tags: [certificate, https, openssl, security, ssl, tls]
aliases: [HTTPS, openssl, SSL, TLS, 인증서]
date modified: 2026-04-07 15:14:51 +09:00
date created: 2026-04-07 10:52:00 +09:00
---

## 🌐 개요 (Overview)

**SSL (Secure Sockets Layer)** 과 그 후속인 **TLS (Transport Layer Security)** 는 네트워크 통신 보안을 제공하는 암호 규약입니다. 웹(HTTPS), 메일(SMTPS/IMAPS) 등에서 데이터의 암호화, 무결성, 신원 확인을 위해 사용됩니다.

## 📄 인증서 구성 요소

| 파일 확장자                   | 용도                | 설명                   |
| :----------------------- | :---------------- | :------------------- |
| **.key**                 | 개인키 (Private Key) | 서버만 보관해야 함 (유출 금지)   |
| **.csr**                 | 인증서 서명 요청         | CA 에 제출하기 위한 요청서 정보  |
| **.crt / .pem**          | 공개키/인증서           | 클라이언트에게 전송되는 공개 인증서  |
| **.bundle / .ca-bundle** | 중간 인증서 체인         | 신뢰할 수 있는 기관까지의 연결 정보 |

## 🛠️ OpenSSL 주요 명령어

OpenSSL 은 인증서 생성 및 관리를 위한 표준 도구입니다.

### 1. 개인키 및 CSR 생성
```bash
# 2048비트 RSA 개인키 생성
openssl genrsa -out server.key 2048

# CSR(서명 요청서) 생성
openssl req -new -key server.key -out server.csr
```

### 2. 셀프 사인 인증서 (Self-Signed) 생성

테스트 용도로 직접 서명한 인증서를 생성합니다.

```bash
openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt
```

### 3. 인증서 정보 확인

```bash
# CSR 정보 확인
openssl req -noout -text -in server.csr

# CRT 인증서 정보 확인
openssl x509 -noout -text -in server.crt
```

## 🌿 Let's Encrypt (무료 보급형 SSL)

`Certbot` 을 사용하여 자동화된 무료 SSL 인증서를 발급받을 수 있습니다.

```bash
# Apache용 설치 및 자동 설정
apt install certbot python3-certbot-apache
certbot --apache

# Nginx용 설치 및 자동 설정
apt install certbot python3-certbot-nginx
certbot --nginx

# 인증서 갱신 테스트
certbot renew --dry-run
```

## ⚙️ 웹 서버 설정 예시

### Apache (`httpd.conf` 또는 `ssl.conf`)

```apache
<VirtualHost *:443>
    ServerName www.example.com
    SSLEngine on
    SSLCertificateFile /path/to/server.crt
    SSLCertificateKeyFile /path/to/server.key
    SSLCertificateChainFile /path/to/ca-bundle.crt
</VirtualHost>
```

### Nginx (`nginx.conf`)

```nginx
server {
    listen 443 ssl;
    server_name www.example.com;
    ssl_certificate /path/to/fullchain.pem;
    ssl_certificate_key /path/to/privkey.pem;
}
```

## 🔗 연결 문서 (Related Documents)

- [[apache-server]] - 아파치 웹 서버 HTTPS 설정
- [[network-fundamentals]] - TCP/IP 및 포트 번호(443)
- [[security-commands]] - 방화벽 설정
