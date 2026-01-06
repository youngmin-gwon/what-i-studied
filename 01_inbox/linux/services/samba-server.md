---
title: Samba Server
tags: [linux, network, samba, smb, cifs, windows]
aliases: [삼바, SMB, CIFS]
date modified: 2026-01-06 19:40:00 +09:00
date created: 2026-01-06 19:40:00 +09:00
---

## 🌐 개요 (Overview)

**Samba** 는 리눅스에서 Windows의 파일/프린터 공유 프로토콜인 **SMB/CIFS** 를 구현한 소프트웨어입니다. 리눅스 서버를 Windows 네트워크의 파일 서버나 도메인 컨트롤러로 사용할 수 있게 해줍니다.

---

## 📦 구성 요소

| 구성 요소 | 역할 |
| :--- | :--- |
| **smbd** | 파일/프린터 공유 서비스 데몬 |
| **nmbd** | NetBIOS 이름 서비스 데몬 (Windows 이름 해석) |
| **winbindd** | Windows 도메인 인증 연동 |
| **/etc/samba/smb.conf** | 메인 설정 파일 |

---

## ⚙️ /etc/samba/smb.conf 설정

### 기본 구조

```ini
[global]
# 전역 설정
workgroup = WORKGROUP
server string = Samba Server %v
security = user
map to guest = bad user

# 로그 설정
log file = /var/log/samba/log.%m
max log size = 50

[공유이름]
# 공유 섹션
path = /path/to/share
comment = 공유 설명
...
```

### [global] 섹션 주요 옵션

| 옵션 | 설명 | 예시 |
| :--- | :--- | :--- |
| **workgroup** | Windows 작업 그룹/도메인 이름 | `WORKGROUP` |
| **server string** | 서버 설명 (`%v` = 버전) | `Samba Server %v` |
| **security** | 인증 방식 | `user` (사용자 인증), `share` (공유 단위) |
| **map to guest** | 인증 실패 시 게스트 처리 | `bad user`, `never` |

### 공유 섹션 주요 옵션

| 옵션 | 설명 | 값 |
| :--- | :--- | :--- |
| **path** | 공유할 디렉토리 경로 | `/data/share` |
| **comment** | 공유 설명 | `Public Files` |
| **browseable** | 네트워크 탐색에 표시 여부 | `yes` / `no` |
| **writable** | 쓰기 허용 여부 | `yes` / `no` |
| **read only** | 읽기 전용 여부 (writable과 반대) | `yes` / `no` |
| **guest ok** | 게스트(비인증) 접근 허용 | `yes` / `no` |
| **valid users** | 접근 허용할 사용자 목록 | `user1, user2, @group` |
| **write list** | 쓰기 허용할 사용자 (read only=yes 일 때) | `user1, @admins` |
| **create mask** | 새 파일 권한 | `0644` |
| **directory mask** | 새 디렉토리 권한 | `0755` |

### 설정 예시

```ini
[global]
workgroup = MYCOMPANY
server string = Linux File Server
security = user
map to guest = bad user

[public]
path = /data/public
comment = Public Share
browseable = yes
writable = yes
guest ok = yes
create mask = 0664
directory mask = 0775

[private]
path = /data/private
comment = Private Share
browseable = yes
writable = yes
valid users = admin, @staff
create mask = 0660
directory mask = 0770
```

---

## 👤 사용자 관리

Samba는 자체 사용자 데이터베이스를 사용합니다. 시스템 사용자를 먼저 생성 후 Samba 사용자로 등록해야 합니다.

```bash
# 1. 시스템 사용자 생성 (로그인 셸 불필요)
useradd -s /sbin/nologin sambauser

# 2. Samba 사용자 추가 및 비밀번호 설정
smbpasswd -a sambauser

# 사용자 활성화/비활성화
smbpasswd -e sambauser   # Enable
smbpasswd -d sambauser   # Disable

# 사용자 삭제
smbpasswd -x sambauser

# Samba 사용자 목록
pdbedit -L
```

---

## 🔧 관리 명령어

```bash
# 설정 파일 문법 검사
testparm

# 서비스 시작/재시작
systemctl enable --now smb nmb
systemctl restart smb nmb

# 현재 연결 확인
smbstatus

# Windows에서 접근: \\서버IP\공유이름
```

---

## 💻 클라이언트 접근

### 리눅스에서 접근

```bash
# 공유 목록 확인
smbclient -L //192.168.1.10 -U user

# 공유 연결
smbclient //192.168.1.10/public -U user

# 마운트
mount -t cifs //192.168.1.10/public /mnt/samba -o username=user,password=pass

# /etc/fstab
//192.168.1.10/public /mnt/samba cifs credentials=/etc/samba/creds,_netdev 0 0
```

---

## 🔗 연결 문서 (Related Documents)

- [[nfs-autofs]] - 리눅스 간 파일 공유 (NFS)
- [[user-permission-commands]] - 사용자/그룹 관리
- [[security-commands]] - 방화벽 설정 (SMB 포트 445)
