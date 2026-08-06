---
title: file-operations-commands
tags: [commands, file-operations, filesystem, linux]
aliases: [cp, File Commands, find, ls, mv, 파일 명령어]
date modified: 2025-12-28 21:22:53 +09:00
date created: 2025-12-20 13:59:24 +09:00
---

## 🌐 개요 (Overview)

Linux 에서 가장 자주 사용하는 파일 및 디렉토리 관련 명령어들입니다. 파일 탐색, 생성, 복사, 이동, 삭제, 검색, 권한 관리 등을 다룹니다.

## 📋 Quick Reference

| 명령어 | 용도 | 핵심 옵션 |
|--------|------|-----------|
| `ls` | 파일 목록 | `-l`, `-a`, `-h`, `-R` |
| `cd` | 디렉토리 이동 | `~`, `-`, `..` |
| `pwd` | 현재 경로 | - |
| `cp` | 복사 | `-r`, `-p`, `-i` |
| `mv` | 이동/이름변경 | `-i`, `-f` |
| `rm` | 삭제 | `-r`, `-f`, `-i` |
| `mkdir` | 디렉토리 생성 | `-p` |
| `touch` | 파일 생성/갱신 | - |
| `find` | 파일 검색 | `-name`, `-type`, `-size` |
| `chmod` | 권한 변경 | `u/g/o`, `+/-/=` |
| `chown` | 소유자 변경 | - |

## 🔧 Navigation Commands

### pwd - Print Working Directory

**현재 작업 디렉토리 절대 경로 출력**

```bash
pwd
# 출력: /home/user/documents

pwd -P  # 심볼릭 링크의 실제 경로
```

### cd - Change Directory

```bash
cd /path/to/directory   # 절대 경로
cd relative/path        # 상대 경로
cd ~                    # 홈 디렉토리 (/home/username)
cd ~/documents          # 홈 디렉토리 하위
cd -                    # 이전 디렉토리 (토글)
cd ..                   # 상위 디렉토리
cd ../..                # 2단계 상위
cd                      # 홈으로 (cd ~와 동일)
```

**팁**:
```bash
# 긴 경로 빠르게 이동
export CDPATH=.:~:~/projects
cd myproject  # ~/projects/myproject로 이동
```

## 📂 Listing Files

### ls - List Directory Contents

**Syntax**:
```bash
ls [OPTIONS] [FILE...]
```

**주요 옵션**:

| 옵션 | 설명 | 예시 |
|------|------|------|
| `-l` | Long format (상세 정보) | `ls -l` |
| `-a` | 숨김 파일 포함 (`.` 으로 시작) | `ls -a` |
| `-A` | `.` 과 `..` 제외하고 모두 | `ls -A` |
| `-h` | 사람이 읽기 쉬운 크기 (K, M, G) | `ls -lh` |
| `-R` | 재귀적 (하위 디렉토리 포함) | `ls -R` |
| `-t` | 수정 시간순 정렬 (최신 먼저) | `ls -lt` |
| `-r` | 역순 정렬 | `ls -ltr` |
| `-S` | 파일 크기순 정렬 | `ls -lS` |
| `-d` | 디렉토리 자체만 표시 | `ls -ld /tmp` |
| `-i` | inode 번호 표시 | `ls -li` |
| `--color` | 색상 표시 | `ls --color=auto` |

**실용 예제**:

```bash
# 가장 많이 사용하는 조합
ls -lah          # 모든 파일, 상세, 사람이 읽기 쉽게

# 최근 수정된 파일 5개
ls -lt | head -6

# 크기가 큰 파일부터
ls -lSh

# 특정 확장자만
ls *.txt
ls -l *.{jpg,png,gif}

# 하위 디렉토리의 모든 .conf 파일
ls -R /etc/*.conf

# 숨김 파일만
ls -ld .*
```

**ls -l 출력 해석**:
```
-rw-r--r-- 1 user group 1024 Jan 01 12:00 file.txt
│││││││││  │ │    │     │    │           │
│││││││││  │ │    │     │    │           └─ 파일명
│││││││││  │ │    │     │    └─ 수정 시간
│││││││││  │ │    │     └─ 크기 (바이트)
│││││││││  │ │    └─ 그룹
│││││││││  │ └─ 소유자
│││││││││  └─ 하드링크 수
└┴┴┴┴┴┴┴┴─ 권한 (파일타입 + rwx × 3)
```

## 📝 File Creation

### touch - Create Empty File or Update Timestamp

```bash
touch file.txt              # 파일 생성 (없으면) 또는 타임스탬프 갱신
touch file1.txt file2.txt   # 여러 파일 동시 생성
touch -c file.txt           # 파일이 없으면 생성하지 않음
touch -t 202501011200 file.txt  # 특정 시간으로 설정 (YYYYMMDDhhmm)
touch -d "2025-01-01 12:00" file.txt  # 사람이 읽기 쉬운 형식
touch -r reference.txt newfile.txt  # reference와 같은 타임스탬프
```

### mkdir - Make Directory

```bash
mkdir mydir                 # 디렉토리 생성
mkdir dir1 dir2 dir3        # 여러 디렉토리
mkdir -p a/b/c              # 중간 디렉토리도 자동 생성
mkdir -m 755 mydir          # 권한 지정
mkdir -v mydir              # Verbose (생성 확인 메시지)
```

## 📋 File Operations

### cp - Copy Files

**Syntax**:
```bash
cp [OPTIONS] SOURCE DEST
cp [OPTIONS] SOURCE... DIRECTORY
```

**주요 옵션**:

| 옵션 | 설명 |
|------|------|
| `-r`, `-R` | 재귀 복사 (디렉토리 복사 시 필수) |
| `-p` | 권한, 소유자, 타임스탬프 보존 |
| `-a` | 아카이브 모드 (`-dR --preserve=all`) |
| `-i` | 덮어쓰기 전 확인 |
| `-f` | 강제 덮어쓰기 |
| `-u` | 소스가 더 최신일 때만 복사 |
| `-v` | Verbose |
| `-l` | 하드링크 생성 (복사 대신) |
| `-s` | 심볼릭 링크 생성 |

**실용 예제**:

```bash
# 파일 복사
cp source.txt dest.txt

# 디렉토리 복사 (재귀)
cp -r dir1/ dir2/

# 속성 보존하여 복사
cp -p important.txt backup.txt

# 아카이브 복사 (백업용)
cp -a /data/ /backup/data/

# 여러 파일을 디렉토리로
cp file1.txt file2.txt file3.txt /destination/

# 확인하며 복사
cp -i source.txt dest.txt

/최신 파일만 업데이트
cp -u source/* destination/

# 심볼릭 링크 생성
cp -s /path/to/original.txt link.txt
```

### mv - Move or Rename

**Syntax**:
```bash
mv [OPTIONS] SOURCE DEST
mv [OPTIONS] SOURCE... DIRECTORY
```

**주요 옵션**:

| 옵션 | 설명 |
|------|------|
| `-i` | 덮어쓰기 전 확인 |
| `-f` | 강제 덮어쓰기 |
| `-n` | 기존 파일 덮어쓰지 않음 |
| `-u` | 소스가 더 최신일 때만 |
| `-v` | Verbose |
| `-b` | 백업 생성 |

**실용 예제**:

```bash
# 파일 이름 변경
mv oldname.txt newname.txt

# 파일 이동
mv file.txt /path/to/destination/

# 여러 파일 이동
mv file1.txt file2.txt file3.txt /destination/

# 확인하며 이동
mv -i file.txt /destination/

# 백업 생성하며 이동
mv -b file.txt /destination/

# 디렉토리 이름 변경
mv old_directory new_directory
```

### rm - Remove Files

**Syntax**:
```bash
rm [OPTIONS] FILE...
```

**주요 옵션**:

| 옵션 | 설명 |
|------|------|
| `-r`, `-R` | 재귀 삭제 (디렉토리 삭제 시 필수) |
| `-f` | 강제 삭제 (확인 안 함, 에러 무시) |
| `-i` | 삭제 전 확인 |
| `-I` | 3 개 이상 파일 또는 재귀 시만 확인 |
| `-v` | Verbose |
| `--preserve-root` | `/` 삭제 방지 (기본값) |

**실용 예제**:

```bash
# 파일 삭제
rm file.txt

# 확인하며 삭제
rm -i file.txt

# 강제 삭제
rm -f file.txt

# 디렉토리 삭제
rm -r directory/

# 위험! 강제 재귀 삭제
rm -rf directory/  # ⚠️ 주의: 복구 불가능

# 특정 패턴 파일 삭제
rm *.log
rm file*.txt

# 빈 디렉토리 삭제
rmdir emptydir  # 빈 디렉토리만 삭제 (안전)
```

>[!WARNING]
>`rm -rf` 는 매우 위험합니다! 특히 `/` 나 `*` 와 함께 사용 시 시스템 전체를 삭제할 수 있습니다.

### ln - Create Links

파일이나 디렉토리에 대한 링크(지름길)를 생성합니다.

**Syntax**:
```bash
ln [OPTIONS] TARGET LINK_NAME
```

**실용 예제**:
```bash
# 하드 링크 생성 (동일 inode 공유)
ln file.txt hardlink.txt

# 심볼릭 링크 생성 (소프트 링크/지름길)
ln -s /path/to/original.txt symlink.txt

# 디렉토리 심볼릭 링크
ln -s /var/log/nginx ~/web_logs
```

> [!TIP]
> **하드 링크 vs 심볼릭 링크**의 차이와 **inode**의 원리에 대한 상세한 설명은 [inode](../inode.md) 및 [file-types-links](../file-types-links.md) 문서를 참조하세요.

## 🔍 File Search

### find - Search for Files

**Syntax**:
```bash
find [PATH...] [EXPRESSION]
```

**주요 옵션**:

#### 이름 검색
```bash
find /path -name "filename"        # 정확한 이름
find /path -name "*.txt"           # 패턴
find /path -iname "*.TXT"          # 대소문자 무시
```

#### 타입 검색
```bash
find /path -type f        # 일반 파일
find /path -type d        # 디렉토리
find /path -type l        # 심볼릭 링크
```

#### 크기 검색
```bash
find /path -size +100M    # 100MB 초과
find /path -size -10k     # 10KB 미만
find /path -size 50M      # 정확히 50MB
find /path -empty         # 빈 파일/디렉토리
```

#### 시간 검색
```bash
find /path -mtime -7      # 7일 이내 수정
find /path -mtime +30     # 30일 이전 수정
find /path -atime -1      # 1일 이내 접근
find /path -newer file.txt  # file.txt보다 최신
```

#### 권한/소유자 검색
```bash
find /path -perm 644      # 정확히 644
find /path -perm -644     # 최소 644
find /path -user username # 소유자
find /path -group groupname  # 그룹
```

#### 실행 액션
```bash
# 찾은 파일에 명령 실행
find /path -name "*.log" -delete  # 삭제
find /path -name "*.txt" -exec cat {} \;  # 실행
find /path -name "*.jpg" -exec mv {} /dest/ \;  # 이동

# 확인 후 실행
find /path -name "*.tmp" -ok rm {} \;

# 여러 파일 한번에 처리 (더 효율적)
find /path -name "*.txt" -exec grep "pattern" {} +
```

**실용 예제**:

```bash
# 큰 파일 찾기 (100MB 이상)
find / -type f -size +100M 2>/dev/null

# 최근 7일간 수정된 .conf 파일
find /etc -name "*.conf" -mtime -7

# 권한이 777인 파일 (보안 위험)
find / -type f -perm 777

# 특정 사용자의 파일
find /home -user john

# 빈 디렉토리 찾아서 삭제
find /tmp -type d -empty -delete

# 로그 파일에서 패턴 검색
find /var/log -name "*.log" -exec grep -l "error" {} \;

# 오래된 백업 파일 삭제 (30일 이상)
find /backup -name "*.bak" -mtime +30 -delete
```

### locate - Fast File Search

```bash
locate filename           # 데이터베이스에서 빠른 검색
locate -i filename        # 대소문자 무시
locate -c filename        # 개수만 표시
locate -e filename        # 존재하는 파일만

# 데이터베이스 업데이트 (root)
sudo updatedb
```

**find vs locate**:
- `find`: 실시간 검색, 느림, 정확
- `locate`: DB 기반, 빠름, 정확도 낮을 수 있음

### which / whereis - Command Location

```bash
which ls                  # 명령어 실행 파일 경로
which -a python           # 모든 경로

whereis ls                # 바이너리, 소스, 매뉴얼 위치
whereis -b ls             # 바이너리만
whereis -m ls             # 매뉴얼만
```

## 🔐 Permissions and Ownership

### chmod - Change File Mode

**Syntax**:
```bash
chmod [OPTIONS] MODE FILE...
```

**숫자 모드 (Octal)**:
```
r(읽기) = 4
w(쓰기) = 2
x(실행) = 1

755 = rwxr-xr-x
    = 소유자(7=rwx) 그룹(5=r-x) 기타(5=r-x)
644 = rw-r--r--
    = 소유자(6=rw-) 그룹(4=r--) 기타(4=r--)
777 = rwxrwxrwx (전체 권한 - 보안 위험!)
```

**심볼릭 모드**:
```bash
u = 소유자(user)
g = 그룹(group)
o = 기타(others)
a = 모두(all)

+ = 권한 추가
- = 권한 제거
= = 권한 설정

chmod u+x file.sh          # 소유자에게 실행 권한 추가
chmod g-w file.txt         # 그룹의 쓰기 권한 제거
chmod o= file.txt          # 기타 사용자 권한 모두 제거
chmod a+r file.txt         # 모두에게 읽기 권한
chmod u=rwx,g=rx,o=r file  # 복합 설정
```

**실용 예제**:
```bash
# 실행 파일로 만들기
chmod +x script.sh
chmod 755 script.sh

# 일반 문서
chmod 644 document.txt

# 디렉토리 (실행 권한 필요)
chmod 755 mydir/
chmod -R 755 mydir/  # 재귀적

# 특수 권한
chmod 4755 binary    # setuid
chmod 2755 directory # setgid
chmod 1777 /tmp      # sticky bit
```

### chown - Change Ownership

```bash
chown user file.txt                # 소유자 변경
chown user:group file.txt          # 소유자와 그룹
chown :group file.txt              # 그룹만
chown -R user:group directory/     # 재귀적
```

### chgrp - Change Group

```bash
chgrp group file.txt               # 그룹 변경
chgrp -R group directory/          # 재귀적
```

## 💡 Real-World Scenarios

### 시나리오 1: 프로젝트 백업

```bash
# 1. 백업 디렉토리 생성
mkdir -p ~/backups/$(date +%Y%m%d)

# 2. 프로젝트 복사 (속성 보존)
cp -a ~/projects/myapp ~/backups/$(date +%Y%m%d)/

# 3. 오래된 백업 삭제 (30일 이상)
find ~/backups -type d -mtime +30 -exec rm -rf {} +
```

### 시나리오 2: 로그 파일 정리

```bash
# 큰 로그 파일 찾기
find /var/log -type f -size +100M

# 30일 이상 된 로그 삭제
find /var/log -name "*.log" -mtime +30 -delete

# 압축
find /var/log -name "*.log" -mtime +7 -exec gzip {} \;
```

### 시나리오 3: 권한 일괄 수정

```bash
# 웹 서버 디렉토리 권한 설정
find /var/www/html -type d -exec chmod 755 {} \;
find /var/www/html -type f -exec chmod 644 {} \;
chown -R www-data:www-data /var/www/html
```

## 🔗 연결 문서 (Related Documents)

- [filesystem-hierarchy-standard](../filesystem-hierarchy-standard.md) - 디렉토리 구조 이해
- [inode](../inode.md) - 파일 시스템 내부 구조
- [file-types-links](../file-types-links.md) - 파일 타입과 링크
- [text-processing-commands](text-processing-commands.md) - 텍스트 파일 처리
