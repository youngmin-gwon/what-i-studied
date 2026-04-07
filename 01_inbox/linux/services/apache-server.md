---
title: apache-server
tags: [apache, httpd, linux, network, webserver]
aliases: [httpd, 아파치, 웹서버]
date modified: 2026-04-07 10:37:19 +09:00
date created: 2026-01-06 19:42:00 +09:00
---

## 🌐 개요 (Overview)

**Apache HTTP Server**는 세계에서 가장 널리 사용되는 오픈소스 웹 서버입니다. 리눅스에서는 `httpd`(RHEL 계열) 또는 `apache2`(Debian 계열) 패키지로 제공됩니다.

---

## 📦 설치 및 서비스 관리

```bash
# RHEL/CentOS
dnf install httpd
systemctl enable --now httpd

# Ubuntu/Debian
apt install apache2
systemctl enable --now apache2
```

---

## ⚙️ 주요 설정 파일

| 배포판 | 메인 설정 파일 | 추가 설정 디렉토리 |
| :--- | :--- | :--- |
| **RHEL/CentOS** | `/etc/httpd/conf/httpd.conf` | `/etc/httpd/conf.d/` |
| **Ubuntu/Debian** | `/etc/apache2/apache2.conf` | `/etc/apache2/sites-available/` |

---

## 📄 httpd.conf 주요 지시어

### 서버 기본 설정

| 지시어 | 설명 | 예시 |
| :--- | :--- | :--- |
| **ServerRoot** | 서버 설정 파일 루트 디렉토리 | `/etc/httpd` |
| **Listen** | 청취할 포트 번호 | `80`, `443` |
| **ServerAdmin** | 관리자 이메일 (오류 페이지에 표시) | `admin@example.com` |
| **ServerName** | 서버 도메인 이름 | `www.example.com:80` |
| **DocumentRoot** | 웹 문서 루트 디렉토리 | `/var/www/html` |

### 디렉토리 설정

| 지시어 | 설명 | 예시 |
| :--- | :--- | :--- |
| **DirectoryIndex** | 기본 인덱스 파일 | `index.html index.php` |
| **Options** | 디렉토리 옵션 | `Indexes FollowSymLinks` |
| **AllowOverride** | `.htaccess` 허용 범위 | `All`, `None` |
| **Require** | 접근 제어 | `all granted`, `ip 192.168.1.0/24` |

### 설정 예시

```apache
# 기본 서버 설정
ServerRoot "/etc/httpd"
Listen 80
ServerAdmin webmaster@example.com
ServerName www.example.com:80
DocumentRoot "/var/www/html"

# 문서 루트 설정
<Directory "/var/www/html">
    Options Indexes FollowSymLinks
    AllowOverride All
    Require all granted
</Directory>

# 기본 인덱스 파일
<IfModule dir_module>
    DirectoryIndex index.html index.php
</IfModule>

# 에러 로그
ErrorLog "logs/error_log"
CustomLog "logs/access_log" combined
```

---

## 🏠 가상 호스트 (Virtual Host)

하나의 서버에서 여러 웹사이트를 호스팅할 수 있습니다.

### 이름 기반 가상 호스트

```apache
# /etc/httpd/conf.d/vhost.conf

<VirtualHost *:80>
    ServerName www.site1.com
    ServerAlias site1.com
    DocumentRoot /var/www/site1
    ErrorLog logs/site1_error.log
    CustomLog logs/site1_access.log combined
</VirtualHost>

<VirtualHost *:80>
    ServerName www.site2.com
    DocumentRoot /var/www/site2
</VirtualHost>
```

---

## 🔐 접근 제어

### Apache 2.4+ (Require 지시어)

```apache
<Directory "/var/www/private">
    # 모든 접근 허용
    Require all granted
    
    # 모든 접근 거부
    Require all denied
    
    # 특정 IP만 허용
    Require ip 192.168.1.0/24
    
    # 인증된 사용자만
    Require valid-user
</Directory>
```

### 사용자 인증 (.htpasswd)

```bash
# 사용자 파일 생성
htpasswd -c /etc/httpd/.htpasswd user1

# 사용자 추가
htpasswd /etc/httpd/.htpasswd user2
```

```apache
<Directory "/var/www/secure">
    AuthType Basic
    AuthName "Restricted Area"
    AuthUserFile /etc/httpd/.htpasswd
    Require valid-user
</Directory>
```

---

## 🔧 관리 명령어

```bash
# 설정 문법 검사
apachectl configtest
# 또는
httpd -t

# 서비스 재시작
systemctl restart httpd

# 설정 리로드 (graceful)
systemctl reload httpd
# 또는
apachectl graceful

# 로드된 모듈 확인
httpd -M
```

---

## 📊 주요 디렉토리 구조 (RHEL)

```
/etc/httpd/
├── conf/
│   └── httpd.conf        # 메인 설정
├── conf.d/               # 추가 설정 (*.conf 자동 로드)
├── conf.modules.d/       # 모듈 설정
├── logs -> /var/log/httpd
└── modules -> /usr/lib64/httpd/modules

/var/www/
├── html/                 # DocumentRoot (기본)
└── cgi-bin/              # CGI 스크립트
```

---

## 🔗 연결 문서 (Related Documents)

- [[dns-bind-server]] - DNS 서버 설정
- [[security-commands]] - 방화벽 설정 (HTTP 80, HTTPS 443)
- [[ssl-tls]] - HTTPS 인증서 설정
