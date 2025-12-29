---
title: 05-users-permissions
tags: []
aliases: []
date modified: 2025-12-29 10:31:53 +09:00
date created: 2025-12-10 19:29:06 +09:00
---

## 사용자 및 권한 관리

### 1. 사용자 계정 관리

#### 1.1 사용자 정보 파일

**/etc/passwd**:
```
username:x:UID:GID:GECOS:home:shell
root:x:0:0:root:/root:/bin/bash
user1:x:1000:1000:User One:/home/user1:/bin/bash
```

**필드 설명**:
1. **사용자명**: 로그인 ID
2. **비밀번호**: `x` (실제는 /etc/shadow 에 저장)
3. **UID**: 사용자 ID (0=root, 1-999=시스템, 1000+=일반)
4. **GID**: 기본 그룹 ID
5. **GECOS**: 사용자 정보 (이름, 연락처 등)
6. **홈 디렉토리**: 사용자 홈
7. **셸**: 로그인 셸

**/etc/shadow**:
```
username:$6$hash:lastchange:min:max:warn:inactive:expire:reserved
```

**필드 설명**:
1. **사용자명**
2. **암호화된 비밀번호**: `$6$` 는 SHA-512
3. **마지막 변경일**: 1970-01-01 부터 일 수
4. **최소 사용 기간**: 변경 후 재변경까지 최소 일 수
5. **최대 사용 기간**: 비밀번호 유효 기간
6. **경고 기간**: 만료 전 경고 일 수
7. **비활성 기간**: 만료 후 계정 잠금까지 일 수
8. **만료일**: 계정 만료일
9. **예약 필드**

#### 1.2 사용자 생성 및 관리

**useradd**:
```bash
useradd user1                   # 기본 설정으로 생성
useradd -m user1                # 홈 디렉토리 생성
useradd -m -s /bin/bash user1   # 셸 지정
useradd -u 1500 user1           # UID 지정
useradd -g users user1          # 기본 그룹 지정
useradd -G wheel,docker user1   # 추가 그룹
useradd -d /custom/home user1   # 홈 디렉토리 지정
useradd -c "User One" user1     # GECOS 정보
useradd -e 2025-12-31 user1     # 만료일 설정
```

**기본 설정**: `/etc/default/useradd`
```bash
useradd -D                      # 기본 설정 확인
useradd -D -s /bin/zsh          # 기본 셸 변경
```

**usermod** - 사용자 수정:
```bash
usermod -l newname oldname      # 사용자명 변경
usermod -d /new/home user1      # 홈 디렉토리 변경
usermod -s /bin/zsh user1       # 셸 변경
usermod -L user1                # 계정 잠금 (Lock)
usermod -U user1                # 계정 잠금 해제 (Unlock)
usermod -aG wheel user1         # 그룹 추가 (-a 없으면 덮어쓰기)
usermod -e 2025-12-31 user1     # 만료일 설정
```

**userdel** - 사용자 삭제:
```bash
userdel user1                   # 사용자 삭제 (홈 유지)
userdel -r user1                # 홈 디렉토리도 삭제
userdel -f user1                # 강제 삭제
```

**passwd** - 비밀번호 관리:
```bash
passwd                          # 자신의 비밀번호 변경
passwd user1                    # user1 비밀번호 변경 (root)
passwd -l user1                 # 계정 잠금
passwd -u user1                 # 잠금 해제
passwd -d user1                 # 비밀번호 삭제
passwd -e user1                 # 비밀번호 만료 (다음 로그인 시 변경)
passwd -n 7 user1               # 최소 사용 기간 7일
passwd -x 90 user1              # 최대 사용 기간 90일
passwd -w 14 user1              # 경고 기간 14일
```

**chage** - 비밀번호 에이징:
```bash
chage -l user1                  # 에이징 정보 확인
chage -m 7 user1                # 최소 사용 기간
chage -M 90 user1               # 최대 사용 기간
chage -W 14 user1               # 경고 기간
chage -I 30 user1               # 비활성 기간
chage -E 2025-12-31 user1       # 만료일
chage -d 0 user1                # 다음 로그인 시 변경
```

### 2. 그룹 관리

#### 2.1 그룹 정보 파일

**/etc/group**:
```
groupname:x:GID:members
root:x:0:
wheel:x:10:user1,user2
users:x:100:
```

**필드**:
1. **그룹명**
2. **비밀번호**: `x` (실제는 /etc/gshadow)
3. **GID**: 그룹 ID
4. **멤버**: 쉼표로 구분된 사용자 목록

#### 2.2 그룹 명령어

**groupadd**:
```bash
groupadd developers             # 그룹 생성
groupadd -g 1500 developers     # GID 지정
groupadd -r system_group        # 시스템 그룹 (GID < 1000)
```

**groupmod**:
```bash
groupmod -n newname oldname     # 그룹명 변경
groupmod -g 1600 developers     # GID 변경
```

**groupdel**:
```bash
groupdel developers             # 그룹 삭제
```

**gpasswd** - 그룹 관리:
```bash
gpasswd -a user1 wheel          # 그룹에 사용자 추가
gpasswd -d user1 wheel          # 그룹에서 사용자 제거
gpasswd -A user1 wheel          # 그룹 관리자 지정
```

**그룹 확인**:
```bash
groups                          # 현재 사용자 그룹
groups user1                    # user1의 그룹
id                              # UID, GID, 그룹 정보
id user1                        # user1 정보
newgrp developers               # 임시로 그룹 전환
```

### 3. 파일 권한

#### 3.1 권한 개념

**권한 표시**:
```
-rw-r--r-- 1 user group 1024 Jan 1 12:00 file.txt
 │││││││││
 │││││││└┴─ 기타(other) 권한: r-- (읽기만)
 ││││└┴┴─── 그룹(group) 권한: r-- (읽기만)
 │└┴┴────── 소유자(owner) 권한: rw- (읽기, 쓰기)
 └───────── 파일 타입: - (일반 파일)
```

**권한 의미**:
- **r (read, 4)**: 읽기
  - 파일: 내용 읽기
  - 디렉토리: 목록 보기 (ls)
- **w (write, 2)**: 쓰기
  - 파일: 내용 수정
  - 디렉토리: 파일 생성/삭제
- **x (execute, 1)**: 실행
  - 파일: 실행 가능
  - 디렉토리: 진입 가능 (cd)

#### 3.2 chmod - 권한 변경

**심볼릭 모드**:
```bash
chmod u+x file.txt              # 소유자에 실행 권한 추가
chmod g-w file.txt              # 그룹에서 쓰기 권한 제거
chmod o=r file.txt              # 기타를 읽기만으로 설정
chmod a+r file.txt              # 모두에게 읽기 권한 추가
chmod u+x,g+x file.txt          # 소유자와 그룹에 실행 권한
chmod -R 755 dir/               # 재귀적으로 권한 변경
```

**대상**:
- `u`: user (소유자)
- `g`: group (그룹)
- `o`: others (기타)
- `a`: all (모두)

**연산자**:
- `+`: 권한 추가
- `-`: 권한 제거
- `=`: 권한 설정

**숫자 모드**:
```bash
chmod 644 file.txt              # rw-r--r--
chmod 755 script.sh             # rwxr-xr-x
chmod 600 private.txt           # rw-------
chmod 777 file.txt              # rwxrwxrwx (비권장)
chmod 000 file.txt              # ---------
```

**숫자 계산**:
```
r = 4, w = 2, x = 1
644 = rw-r--r-- (4+2=6, 4, 4)
755 = rwxr-xr-x (4+2+1=7, 4+1=5, 4+1=5)
700 = rwx------ (4+2+1=7, 0, 0)
```

#### 3.3 chown - 소유자 변경

```bash
chown user1 file.txt            # 소유자 변경
chown user1:group1 file.txt     # 소유자와 그룹 변경
chown :group1 file.txt          # 그룹만 변경
chown -R user1 dir/             # 재귀적으로 변경
```

#### 3.4 chgrp - 그룹 변경

```bash
chgrp group1 file.txt           # 그룹 변경
chgrp -R group1 dir/            # 재귀적으로 변경
```

### 4. 특수 권한

#### 4.1 SetUID (SUID)

**개념**:
- 파일 실행 시 소유자 권한으로 실행
- 주로 root 소유 실행 파일에 사용
- 표시: `s` (실행 권한 있음), `S` (실행 권한 없음)

**설정**:
```bash
chmod u+s file                  # SUID 설정
chmod 4755 file                 # 숫자 모드 (4000 + 755)
ls -l /usr/bin/passwd
# -rwsr-xr-x 1 root root ... /usr/bin/passwd
```

**예**: `passwd` 명령어는 SUID 로 일반 사용자도 /etc/shadow 수정 가능

#### 4.2 SetGID (SGID)

**파일**:
- 실행 시 그룹 권한으로 실행
- 표시: `s` (그룹 실행 권한 위치)

**디렉토리**:
- 생성되는 파일이 디렉토리 그룹 상속
- 협업 디렉토리에 유용

**설정**:
```bash
chmod g+s dir/                  # SGID 설정
chmod 2755 dir/                 # 숫자 모드 (2000 + 755)
ls -ld dir/
# drwxr-sr-x 2 user group ... dir/
```

#### 4.3 Sticky Bit

**개념**:
- 디렉토리에 설정
- 파일 소유자만 삭제 가능
- `/tmp` 디렉토리에 기본 설정

**설정**:
```bash
chmod +t dir/                   # Sticky bit 설정
chmod 1755 dir/                 # 숫자 모드 (1000 + 755)
ls -ld /tmp
# drwxrwxrwt 10 root root ... /tmp
```

**특수 권한 숫자**:
```
SUID = 4000
SGID = 2000
Sticky = 1000
```

**조합 예**:
```bash
chmod 6755 file     # SUID + SGID
chmod 7755 file     # SUID + SGID + Sticky
```

### 5. 기본 권한 (umask)

#### 5.1 umask 개념

**역할**:
- 새 파일/디렉토리의 기본 권한 결정
- 최대 권한에서 umask 값을 뺀 권한 적용

**기본 최대 권한**:
- 파일: 666 (rw-rw-rw-)
- 디렉토리: 777 (rwxrwxrwx)

**계산**:
```
umask 022:
  파일: 666 - 022 = 644 (rw-r--r--)
  디렉토리: 777 - 022 = 755 (rwxr-xr-x)

umask 027:
  파일: 666 - 027 = 640 (rw-r-----)
  디렉토리: 777 - 027 = 750 (rwxr-x---)
```

#### 5.2 umask 설정

```bash
umask                   # 현재 umask 확인
umask -S                # 심볼릭 표시
umask 022               # umask 설정
umask 027               # 더 제한적인 권한
```

**영구 설정**:
- `/etc/profile`: 시스템 전역
- `~/.bashrc`: 사용자별

### 6. ACL (Access Control List)

#### 6.1 ACL 개념

**확장 권한**:
- 전통적 권한(소유자, 그룹, 기타)의 한계 극복
- 특정 사용자/그룹에 개별 권한 부여

#### 6.2 ACL 명령어

**getfacl** - ACL 확인:
```bash
getfacl file.txt
# file: file.txt
# owner: user1
# group: group1
# user::rw-
# user:user2:r--
# group::r--
# mask::r--
# other::r--
```

**setfacl** - ACL 설정:
```bash
setfacl -m u:user2:rw file.txt     # user2에 rw 권한
setfacl -m g:group2:rx file.txt    # group2에 rx 권한
setfacl -m o::r file.txt           # 기타에 r 권한
setfacl -x u:user2 file.txt        # user2 ACL 제거
setfacl -b file.txt                # 모든 ACL 제거
setfacl -R -m u:user2:rx dir/      # 재귀적 설정
setfacl -d -m u:user2:rx dir/      # 기본 ACL (새 파일에 적용)
```

**ACL 표시**:
```bash
ls -l file.txt
# -rw-r--r--+ 1 user1 group1 ... file.txt
#           ^ ACL이 설정되어 있음을 나타냄
```

### 7. sudo

#### 7.1 sudo 개념

**특징**:
- 일반 사용자가 root 권한으로 명령 실행
- 로그 기록
- 세밀한 권한 제어

#### 7.2 sudo 사용

```bash
sudo command                # root 권한으로 실행
sudo -u user1 command       # user1 권한으로 실행
sudo -i                     # root 셸 시작
sudo -s                     # 현재 셸을 root로
sudo -l                     # 허용된 명령 확인
sudo -k                     # 인증 캐시 삭제
```

#### 7.3 sudoers 설정

**파일**: `/etc/sudoers`

**편집**:
```bash
visudo                      # 안전한 편집 (문법 검사)
```

**문법**:
```
user    host=(runas) commands
root    ALL=(ALL:ALL) ALL
user1   ALL=(ALL) ALL
user2   ALL=(ALL) NOPASSWD: /usr/bin/systemctl
%wheel  ALL=(ALL) ALL       # wheel 그룹
```

**예제**:
```
# user1은 모든 명령 실행 가능
user1 ALL=(ALL) ALL

# user2는 비밀번호 없이 systemctl만
user2 ALL=(ALL) NOPASSWD: /usr/bin/systemctl

# wheel 그룹은 모든 명령
%wheel ALL=(ALL) ALL

# developers 그룹은 특정 명령만
%developers ALL=(ALL) /usr/bin/git, /usr/bin/docker
```

**include 디렉토리**:
```
/etc/sudoers.d/             # 추가 설정 파일
```

### 8. PAM (Pluggable Authentication Modules)

#### 8.1 PAM 개념

**역할**:
- 인증, 계정 관리, 세션 관리, 비밀번호 관리
- 모듈식 구조로 유연한 인증 정책

#### 8.2 PAM 설정

**설정 파일**: `/etc/pam.d/`

**구조**:
```
type    control    module-path    module-arguments
```

**타입**:
- `auth`: 인증
- `account`: 계정 유효성
- `password`: 비밀번호 변경
- `session`: 세션 관리

**제어**:
- `required`: 필수, 실패해도 계속
- `requisite`: 필수, 실패 시 즉시 중단
- `sufficient`: 충분, 성공 시 즉시 허용
- `optional`: 선택적

**예제** (`/etc/pam.d/sshd`):
```
auth       required     pam_unix.so
auth       required     pam_env.so
account    required     pam_nologin.so
account    required     pam_unix.so
password   required     pam_unix.so
session    required     pam_limits.so
session    required     pam_unix.so
```

### 9. 시험 대비 핵심 요약

#### 사용자 관리
- **생성**: `useradd -m user1`
- **수정**: `usermod -aG group user1`
- **삭제**: `userdel -r user1`
- **비밀번호**: `passwd user1`

#### 그룹 관리
- **생성**: `groupadd developers`
- **추가**: `gpasswd -a user1 developers`
- **확인**: `groups user1`, `id user1`

#### 권한
- **chmod**: `chmod 755 file`, `chmod u+x file`
- **chown**: `chown user:group file`
- **umask**: `umask 022`

#### 특수 권한
- **SUID**: 4000, `chmod u+s`
- **SGID**: 2000, `chmod g+s`
- **Sticky**: 1000, `chmod +t`

#### 파일
- **/etc/passwd**: 사용자 정보
- **/etc/shadow**: 비밀번호
- **/etc/group**: 그룹 정보
- **/etc/sudoers**: sudo 설정

---

**이전 챕터**: [기본 명령어 및 셸](04-basic-commands.md)
**다음 챕터**: [프로세스 및 작업 관리](06-process-management.md)
