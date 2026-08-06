---
title: Package Management Commands
tags: [linux, commands, package, apt, yum, dnf]
aliases: [패키지 관리, apt, yum, Package]
date modified: 2025-12-20 13:59:24 +09:00
date created: 2025-12-20 13:59:24 +09:00
---

## 🌐 개요 (Overview)

Linux 배포판별 패키지 관리 명령어들입니다.

## 📋 Quick Reference

| 배포판 | 고수준 | 저수준 |
|--------|--------|--------|
| **Debian/Ubuntu** | `apt`, `apt-get` | `dpkg` |
| **RHEL/CentOS** | `yum`, `dnf` | `rpm` |

## 🔹 Debian/Ubuntu

### apt - Advanced Package Tool

```bash
# 패키지 목록 업데이트
sudo apt update

# 시스템 업그레이드
sudo apt upgrade
sudo apt full-upgrade              # 의존성 변경 허용

# 패키지 설치
sudo apt install nginx
sudo apt install nginx mysql-server php

# 패키지 제거
sudo apt remove nginx
sudo apt purge nginx               # 설정 파일도 삭제
sudo apt autoremove                # 불필요한 의존성 제거

# 패키지 검색
apt search keyword
apt show nginx                     # 상세 정보

# 패키지 목록
apt list --installed
apt list --upgradable
```

### dpkg - Debian Package

```bash
# .deb 파일 설치
sudo dpkg -i package.deb

# 제거
sudo dpkg -r package
sudo dpkg -P package               # 설정 포함

# 목록
dpkg -l                            # 설치된 패키지
dpkg -L nginx                      # 파일 목록
dpkg -S /usr/bin/nginx             # 파일이 속한 패키지

# 의존성 문제 해결
sudo apt --fix-broken install
```

## 🔸 RHEL/CentOS

### yum/dnf - Yellowdog Updater Modified

```bash
# 패키지 설치
sudo yum install nginx
sudo dnf install nginx            # CentOS 8+

# 업그레이드
sudo yum update
sudo yum upgrade

# 패키지 제거
sudo yum remove nginx

# 검색
yum search keyword
yum info nginx

# 목록
yum list installed
yum list available

# 저장소
yum repolist
sudo yum-config-manager --add-repo URL
```

### rpm - RPM Package Manager

```bash
# .rpm 파일 설치
sudo rpm -ivh package.rpm

# 업그레이드
sudo rpm -Uvh package.rpm

# 제거
sudo rpm -e package

# 쿼리
rpm -qa                           # 전체 목록
rpm -qi nginx                     # 정보
rpm -ql nginx                     # 파일 목록
rpm -qf /usr/bin/nginx            # 파일이 속한 패키지
```

## 💡 Scenarios

### 시스템 전체 업데이트

```bash
# Debian/Ubuntu
sudo apt update && sudo apt upgrade -y

# RHEL/CentOS
sudo yum update -y
```

### 패키지 찾아서 설치

```bash
# Debian
apt search nginx
sudo apt install nginx

# RHEL
yum search nginx
sudo yum install nginx
```

### 의존성 확인

```bash
# Debian
apt-cache depends nginx
apt-cache rdepends nginx          # 역의존성

# RHEL
yum deplist nginx
```

## 🔗 연결 문서 (Related Documents)

- [system-monitoring-commands](system-monitoring-commands.md) - 시스템 모니터링
- [file-operations-commands](file-operations-commands.md) - 파일 작업
