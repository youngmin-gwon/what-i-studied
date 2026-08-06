---
title: linux-account-security
tags: [account, authentication, linux, password, security]
aliases: [passwd, SetUID, shadow, 계정 보안]
date modified: 2026-01-08 15:56:43 +09:00
date created: 2026-01-08 10:15:25 +09:00
---

## 🌐 개요 (Overview)

Linux 시스템에서 **사용자 계정과 패스워드 관리**는 보안의 기본입니다. 이 문서에서는 `/etc/passwd`, `/etc/shadow` 파일 구조와 특수 권한(SetUID, SetGID, Sticky Bit)을 다룹니다.

## 📁 사용자 계정 파일

### /etc/passwd

**모든 사용자의 기본 계정 정보**를 저장합니다. 누구나 읽을 수 있습니다.

```bash
# 파일 확인
cat /etc/passwd
ls -l /etc/passwd
# -rw-r--r-- 1 root root 2345 Jan 1 00:00 /etc/passwd
```

**구조 (7 개 필드, 콜론으로 구분)**:

```plaintext
username:x:UID:GID:Comment:HomeDir:Shell
   1     2  3   4     5       6      7
```

| 필드 | 이름 | 설명 | 예시 |
|------|------|------|------|
| 1 | **Username** | 사용자 계정 이름 | `youngmin` |
| 2 | **Password** | 패스워드 (x = shadow 사용) | `x` |
| 3 | **UID** | 사용자 ID (0 = root) | `1000` |
| 4 | **GID** | 주 그룹 ID | `1000` |
| 5 | **Comment** | 설명 (GECOS 필드) | `Youngmin,Room 101,1234` |
| 6 | **Home Directory** | 홈 디렉토리 경로 | `/home/youngmin` |
| 7 | **Login Shell** | 로그인 쉘 | `/bin/bash` |

**예시**:
```plaintext
root:x:0:0:root:/root:/bin/bash
youngmin:x:1000:1000:Youngmin Gwon:/home/youngmin:/bin/bash
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
```

**특수 계정**:
- `root` (UID 0): 슈퍼유저
- `nobody` (UID 65534): 권한 없는 계정
- 서비스 계정 (UID < 1000): `www-data`, `mysql` 등

---

### /etc/shadow

**암호화된 패스워드**를 저장합니다. **root 만 읽기 가능**합니다.

```bash
# 파일 확인 (root 권한 필요)
sudo cat /etc/shadow
ls -l /etc/shadow
# -rw-r----- 1 root shadow 1456 Jan 1 00:00 /etc/shadow
```

**구조 (9 개 필드)**:

```plaintext
username:hash:lastchange:min:max:warn:inactive:expire:reserved
   1      2       3       4   5    6      7       8       9
```

| 필드 | 이름 | 설명 |
|------|------|------|
| 1 | **Username** | 사용자 계정 이름 |
| 2 | **Password Hash** | 암호화된 패스워드 |
| 3 | **Last Change** | 마지막 변경일 (1970-01-01 기준 일수) |
| 4 | **Min Days** | 변경 후 재변경 불가 기간 |
| 5 | **Max Days** | 패스워드 유효 기간 |
| 6 | **Warn Days** | 만료 경고 시작 일수 |
| 7 | **Inactive Days** | 만료 후 비활성화까지 유예 기간 |
| 8 | **Expire Date** | 계정 만료일 |
| 9 | **Reserved** | 예약 필드 |

**패스워드 해시 형식**:
```plaintext
$algorithm$salt$hash

$1$ : MD5 (취약, 사용 비권장)
$5$ : SHA-256
$6$ : SHA-512 (현재 기본)
$y$ : yescrypt (최신)
```

**예시**:
```plaintext
youngmin:$6$randomsalt$hashedpassword:19357:0:99999:7:::
         └─ SHA-512 해시 ─────────────┘ 
                                       └─ 19357일 = 2022-12-25 마지막 변경
                                          0 = 즉시 변경 가능
                                          99999 = 273년 (사실상 무제한)
                                          7 = 만료 7일 전 경고
```

**특수 값**:
- `!` 또는 `*`: 계정 잠금 (로그인 불가)
- `!!`: 패스워드 미설정
- 빈 값: 패스워드 없이 로그인 가능 (위험!)

---

### /etc/group

**그룹 정보**를 저장합니다.

```bash
cat /etc/group
# sudo:x:27:youngmin
```

**구조**:
```plaintext
groupname:password:GID:members
sudo:x:27:youngmin,admin
```

---

## 🔐 패스워드 관리

### 패스워드 정책 설정

```bash
# /etc/login.defs - 시스템 전역 설정
PASS_MAX_DAYS   90      # 최대 유효 기간
PASS_MIN_DAYS   7       # 최소 사용 기간
PASS_MIN_LEN    12      # 최소 길이
PASS_WARN_AGE   14      # 만료 경고 일수

# chage - 사용자별 정책 설정
chage -l youngmin       # 정책 확인
chage -M 90 youngmin    # 최대 90일
chage -m 7 youngmin     # 최소 7일
chage -W 14 youngmin    # 만료 14일 전 경고
chage -E 2026-12-31 youngmin  # 계정 만료일
```

### PAM (Pluggable Authentication Modules)

패스워드 복잡성 정책을 설정합니다.

```bash
# /etc/pam.d/common-password (Debian/Ubuntu)
password requisite pam_pwquality.so retry=3 minlen=12 difok=3 \
    ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1

# 옵션 설명:
# minlen=12   : 최소 12자
# difok=3     : 이전 패스워드와 3자 이상 다름
# ucredit=-1  : 최소 대문자 1개
# lcredit=-1  : 최소 소문자 1개
# dcredit=-1  : 최소 숫자 1개
# ocredit=-1  : 최소 특수문자 1개
```

### 계정 잠금/해제

```bash
# 계정 잠금
passwd -l username      # 패스워드 앞에 ! 추가
usermod -L username     # 동일

# 계정 해제
passwd -u username
usermod -U username

# 로그인 불가 쉘 설정
usermod -s /usr/sbin/nologin username
chsh -s /usr/sbin/nologin username
```

---

## ⚡ 특수 권한

### 일반 권한 복습

```bash
chmod 755 file
# rwxr-xr-x
#  7  5  5
#  │  │  └─ Others: r+x = 5
#  │  └──── Group:  r+x = 5
#  └─────── Owner:  r+w+x = 7
```

### 1. SetUID (4000)

**실행 시 파일 소유자의 권한**으로 실행됩니다.

```bash
# SetUID 설정
chmod 4755 file
chmod u+s file

# 확인 (소유자 x 대신 s)
ls -l /usr/bin/passwd
# -rwsr-xr-x 1 root root 68208 /usr/bin/passwd
```

**동작 원리**:
```mermaid
graph LR
    USER[일반 사용자] -->|"실행"| PASSWD[/usr/bin/passwd]
    PASSWD -->|"SetUID"| ROOT[root 권한으로 실행]
    ROOT -->|"수정"| SHADOW[/etc/shadow]
```

```plaintext
일반 사용자가 passwd 명령 실행
→ SetUID로 인해 root 권한 획득
→ /etc/shadow 파일 수정 가능
→ 명령 종료 시 root 권한 반환
```

**⚠️ 보안 위험**:
- SetUID 가 설정된 취약한 프로그램 = **권한 상승 (Privilege Escalation)** 공격 벡터
- 정기적인 감사 필요

```bash
# SetUID 파일 찾기
find / -perm -4000 -type f 2>/dev/null

# 일반적인 SetUID 파일
/usr/bin/passwd
/usr/bin/sudo
/usr/bin/su
/usr/bin/chsh
```

### 2. SetGID (2000)

**실행 시 파일 소유 그룹의 권한**으로 실행됩니다.

```bash
# SetGID 설정
chmod 2755 file
chmod g+s file

# 확인 (그룹 x 대신 s)
ls -l /usr/bin/wall
# -rwxr-sr-x 1 root tty 19024 /usr/bin/wall
```

**디렉토리에 SetGID 설정**:
```bash
chmod 2775 /shared
# 이 디렉토리에 생성되는 파일은 부모 디렉토리의 그룹을 상속
```

### 3. Sticky Bit (1000)

디렉토리에 설정하면 **소유자만 파일 삭제 가능**합니다.

```bash
# Sticky Bit 설정
chmod 1777 /tmp
chmod +t /tmp

# 확인 (others x 대신 t)
ls -ld /tmp
# drwxrwxrwt 20 root root 4096 /tmp
```

**동작**:
```plaintext
/tmp (sticky bit 설정)
├── file1 (owner: userA) → userA만 삭제 가능
├── file2 (owner: userB) → userB만 삭제 가능
└── file3 (owner: userC) → userC만 삭제 가능

모든 사용자가 쓰기 가능하지만, 다른 사용자 파일 삭제 불가
```

### 특수 권한 정리

| 권한 | 숫자 | 대상 | 효과 |
|------|------|------|------|
| **SetUID** | 4000 | 파일 | 소유자 권한으로 실행 |
| **SetGID** | 2000 | 파일 | 그룹 권한으로 실행 |
| **SetGID** | 2000 | 디렉토리 | 생성 파일이 그룹 상속 |
| **Sticky Bit** | 1000 | 디렉토리 | 소유자만 삭제 가능 |

---

## 🔍 보안 점검

### SetUID/SetGID 파일 감사

```bash
# SetUID 파일 찾기
find / -perm -4000 -type f -ls 2>/dev/null

# SetGID 파일 찾기
find / -perm -2000 -type f -ls 2>/dev/null

# 둘 다 설정된 파일
find / -perm -6000 -type f -ls 2>/dev/null

# 비정상 SetUID 파일 탐지 (cron으로 정기 실행)
find / -perm -4000 -type f > /var/log/setuid_files.txt
diff /var/log/setuid_files.txt /var/log/setuid_files.txt.bak
```

### 패스워드 파일 점검

```bash
# /etc/passwd에 패스워드가 직접 있는지 (shadow 미사용)
awk -F: '$2 != "x" {print $1}' /etc/passwd

# 빈 패스워드 계정
awk -F: '$2 == "" {print $1}' /etc/shadow

# UID 0인 계정 (root 외)
awk -F: '$3 == 0 && $1 != "root" {print $1}' /etc/passwd

# 로그인 가능한 쉘을 가진 시스템 계정
awk -F: '$3 < 1000 && $7 !~ /nologin|false/ {print $1}' /etc/passwd
```

### 권한 강화

```bash
# shadow 파일 권한 확인
ls -l /etc/shadow
# -rw-r----- 또는 -rw------- 권한이어야 함

# 불필요한 SetUID 제거
chmod u-s /path/to/suspicious_file

# 홈 디렉토리 권한 점검
chmod 750 /home/*
```

---

## 💡 실무 시나리오

### 신규 사용자 생성

```bash
# 사용자 생성
useradd -m -s /bin/bash -c "New User" -G sudo newuser

# 패스워드 설정
passwd newuser

# 패스워드 정책 적용
chage -M 90 -m 7 -W 14 newuser

# 첫 로그인 시 패스워드 변경 강제
chage -d 0 newuser
```

### 계정 비활성화

```bash
# 퇴사자 계정 처리
# 1. 즉시 잠금
usermod -L departed_user

# 2. 쉘 변경
usermod -s /usr/sbin/nologin departed_user

# 3. (선택) 계정 만료일 설정
usermod -e 2026-01-01 departed_user

# 4. 현재 세션 종료
pkill -u departed_user
```

## 🔗 연결 문서 (Related Documents)

- [filesystem-hierarchy-standard](../filesystem-hierarchy-standard.md) - /etc 디렉토리 구조
- [user-permission-commands](../commands/user-permission-commands.md) - chmod, chown 명령어
- [linux-log-management](linux-log-management.md) - 인증 로그 (wtmp, btmp)
- [selinux](selinux.md) - 강제적 접근 통제
