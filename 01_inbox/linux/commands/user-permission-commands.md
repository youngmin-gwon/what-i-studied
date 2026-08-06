---
title: User and Permission Commands
tags: [linux, commands, user, permission, chmod, sudo]
aliases: [사용자 권한, useradd, chmod, sudo]
date modified: 2025-12-20 13:59:24 +09:00
date created: 2025-12-20 13:59:24 +09:00
---

## 🌐 개요 (Overview)

사용자 관리, 그룹 관리, 권한 설정 명령어들입니다.

## 📋 Quick Reference

| 명령어 | 용도 |
|--------|------|
| `useradd`/`adduser` | 사용자 생성 |
| `usermod` | 사용자 수정 |
| `userdel` | 사용자 삭제 |
| `passwd` | 패스워드 변경 |
| `groupadd` | 그룹 생성 |
| `sudo` | 권한 상승 |
| `chmod` | 권한 변경 |
| `chown` | 소유자 변경 |

## 👤 User Management

### useradd - Create User

```bash
sudo useradd username              # 기본 생성
sudo useradd -m username           # 홈 디렉토리 생성
sudo useradd -m -s /bin/bash username  # 셸 지정
sudo useradd -m -G sudo username   # 그룹 추가
sudo useradd -u 1500 username      # UID 지정
sudo useradd -e 2025-12-31 username  # 만료일

# Debian의 adduser (더 인터랙티브)
sudo adduser username
```

### usermod - Modify User

```bash
sudo usermod -aG sudo username     # 그룹 추가 (append)
sudo usermod -L username           # 계정 잠금
sudo usermod -U username           # 잠금 해제
sudo usermod -s /bin/zsh username  # 셸 변경
sudo usermod -d /new/home username # 홈 디렉토리 변경
```

### userdel - Delete User

```bash
sudo userdel username              # 사용자만 삭제
sudo userdel -r username           # 홈 디렉토리도 삭제
```

### passwd - Change Password

```bash
passwd                             # 자신의 패스워드
sudo passwd username               # 다른 사용자
sudo passwd -l username            # 잠금
sudo passwd -u username            # 잠금 해제
sudo passwd -e username            # 만료 (다음 로그인 시 변경 강제)
```

## 👥 Group Management

### groupadd - Create Group

```bash
sudo groupadd groupname
sudo groupadd -g 1500 groupname    # GID 지정
```

### groupmod - Modify Group

```bash
sudo groupmod -n newname oldname   # 이름 변경
sudo groupmod -g 2000 groupname    # GID 변경
```

### groupdel - Delete Group

```bash
sudo groupdel groupname
```

### gpasswd - Group Password

```bash
sudo gpasswd -a username group     # 사용자 추가
sudo gpasswd -d username group     # 사용자 제거
sudo gpasswd -A username group     # 관리자 지정
```

## 🔑 Permissions

### chmod - Change Mode

**숫자 모드**:
```
r=4, w=2, x=1
755 = rwxr-xr-x
644 = rw-r--r--
777 = rwxrwxrwx (위험!)
```

```bash
chmod 755 file.sh                  # rwxr-xr-x
chmod 644 file.txt                 # rw-r--r--
chmod -R 755 directory/            # 재귀

# 심볼릭 모드
chmod u+x file.sh                  # 소유자에게 실행 추가
chmod g-w file.txt                 # 그룹 쓰기 제거
chmod o= file.txt                  # 기타 권한 모두 제거
chmod a+r file.txt                 # 모두에게 읽기

# 특수 권한
chmod u+s binary                   # setuid (4xxx)
chmod g+s directory                # setgid (2xxx)
chmod +t directory                 # sticky bit (1xxx)
chmod 4755 binary                  # setuid + 755
```

### chown - Change Owner

```bash
chown user file.txt                # 소유자만
chown user:group file.txt          # 소유자와 그룹
chown :group file.txt              # 그룹만
chown -R user:group directory/     # 재귀
```

### chgrp - Change Group

```bash
chgrp group file.txt
chgrp -R group directory/
```

### umask - Default Permissions

```bash
umask                              # 현재 umask
umask 022                          # 755 (디렉토리), 644 (파일)
umask 002                          # 775, 664

# ~/.bashrc에 추가하여 영구 설정
```

## 🔐 Privilege Escalation

### su - Switch User

```bash
su username                        # 사용자 전환
su -                               # root로 (로그인 셸)
su - username                      # 사용자로 (로그인 셸)
exit                               # 원래 사용자로
```

### sudo - Superuser Do

```bash
sudo command                       # 관리자 권한으로 실행
sudo -i                            # root 셸
sudo -s                            # 셸 실행
sudo -u username command           # 다른 사용자로

# /etc/sudoers 편집
sudo visudo

# 예제 설정
username ALL=(ALL:ALL) ALL
%sudo ALL=(ALL:ALL) ALL
username ALL=NOPASSWD: /usr/bin/systemctl
```

## 🔍 Query Commands

### id - User/Group Info

```bash
id                                 # 현재 사용자
id username                        # 특정 사용자
whoami                             # 현재 사용자 이름
groups                             # 소속 그룹
groups username                    # 사용자의 그룹
```

### who/w - Logged in Users

```bash
who                                # 로그인 사용자
w                                  # 더 상세
last                               # 로그인 기록
lastlog                            # 마지막 로그인
```

## 💡 Scenarios

### 새 사용자 생성 (전체 과정)

```bash
# 1. 사용자 생성
sudo useradd -m -s /bin/bash john

# 2. 패스워드 설정
sudo passwd john

# 3. sudo 그룹 추가
sudo usermod -aG sudo john

# 4. 확인
id john
```

### 웹 서버 권한 설정

```bash
# 소유자: www-data, 그룹: www-data
sudo chown -R www-data:www-data /var/www/html

# 디렉토리: 755, 파일: 644
sudo find /var/www/html -type d -exec chmod 755 {} \;
sudo find /var/www/html -type f -exec chmod 644 {} \;
```

### 공유 디렉토리 설정

```bash
# 1. 그룹 생성
sudo groupadd developers

# 2. 사용자를 그룹에 추가
sudo usermod -aG developers alice
sudo usermod -aG developers bob

# 3. 디렉토리 생성 및 권한
sudo mkdir /shared
sudo chown :developers /shared
sudo chmod 2775 /shared            # setgid + rwxrwxr-x
```

## 🔗 연결 문서 (Related Documents)

- [file-operations-commands](file-operations-commands.md) - chmod, chown 상세
- [process-job-control-commands](process-job-control-commands.md) - 프로세스 소유자
