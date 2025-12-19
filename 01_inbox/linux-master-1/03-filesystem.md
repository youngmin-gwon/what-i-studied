# 파일 시스템 및 디렉토리 구조

## 1. 파일 시스템 계층 구조 (FHS)

### 1.1 FHS 개요

**Filesystem Hierarchy Standard**:
- **목적**: 리눅스 배포판 간 디렉토리 구조 통일
- **관리**: Linux Foundation
- **버전**: FHS 3.0 (2015)

### 1.2 주요 디렉토리

**루트 디렉토리 (`/`)**:

```plaintext
/
├── bin     - 필수 사용자 명령어 (ls, cp, mv)
├── boot    - 부트 로더, 커널 이미지
├── dev     - 디바이스 파일
├── etc     - 시스템 설정 파일
├── home    - 사용자 홈 디렉토리
├── lib     - 공유 라이브러리
├── media   - 이동식 미디어 마운트 포인트
├── mnt     - 임시 마운트 포인트
├── opt     - 추가 응용 프로그램
├── proc    - 프로세스 정보 (가상 파일시스템)
├── root    - root 사용자 홈 디렉토리
├── run     - 런타임 데이터
├── sbin    - 시스템 관리 명령어
├── srv     - 서비스 데이터
├── sys     - 시스템 정보 (가상 파일시스템)
├── tmp     - 임시 파일
├── usr     - 사용자 응용 프로그램
└── var     - 가변 데이터 (로그, 캐시)
```

### 1.3 상세 디렉토리 설명

**/bin (Binaries)**:
- 모든 사용자가 사용하는 필수 명령어
- 예: `ls`, `cp`, `mv`, `cat`, `bash`, `grep`
- 싱글 유저 모드에서도 필요한 명령어

**/sbin (System Binaries)**:
- 시스템 관리자용 명령어
- 예: `fdisk`, `mkfs`, `shutdown`, `ifconfig`
- 일반적으로 root 권한 필요

**/etc (Et Cetera)**:
- 시스템 전역 설정 파일
- 텍스트 기반 설정 파일
- 주요 파일:
  ```
  /etc/passwd       - 사용자 계정 정보
  /etc/shadow       - 암호화된 비밀번호
  /etc/group        - 그룹 정보
  /etc/fstab        - 파일시스템 마운트 정보
  /etc/hosts        - 호스트 이름 매핑
  /etc/hostname     - 시스템 호스트명
  /etc/resolv.conf  - DNS 설정
  /etc/network/     - 네트워크 설정 (Debian)
  /etc/sysconfig/   - 시스템 설정 (RHEL)
  ```

**/home**:
- 일반 사용자의 홈 디렉토리
- `/home/username` 형식
- 사용자 개인 파일, 설정 저장

**/root**:
- root 사용자의 홈 디렉토리
- `/home`이 아닌 별도 위치
- 시스템 복구 시 접근 보장

**/usr (Unix System Resources)**:
```
/usr
├── bin     - 일반 사용자 명령어
├── sbin    - 시스템 관리 명령어
├── lib     - 라이브러리
├── local   - 로컬 설치 소프트웨어
├── share   - 아키텍처 독립적 데이터
├── include - C 헤더 파일
└── src     - 소스 코드
```

**/var (Variable)**:
```
/var
├── log     - 로그 파일
├── mail    - 메일 스풀
├── spool   - 프린터, cron 작업 큐
├── tmp     - 재부팅 후에도 유지되는 임시 파일
├── cache   - 캐시 데이터
└── lib     - 상태 정보, 데이터베이스
```

**/proc**:
- **가상 파일시스템**: 메모리에만 존재
- **프로세스 정보**: `/proc/[PID]/`
- **시스템 정보**: 
  ```
  /proc/cpuinfo     - CPU 정보
  /proc/meminfo     - 메모리 정보
  /proc/version     - 커널 버전
  /proc/sys/        - 커널 파라미터 (sysctl)
  ```

**/sys**:
- **sysfs**: 커널 객체 정보
- **디바이스 관리**: udev와 연동
- **하드웨어 정보**: `/sys/class/`, `/sys/block/`

**/dev (Devices)**:
- **디바이스 파일**: 하드웨어 접근 인터페이스
- **udev**: 동적 디바이스 관리
- 주요 디바이스:
  ```
  /dev/sda          - 첫 번째 SATA/SCSI 디스크
  /dev/sda1         - 첫 번째 파티션
  /dev/nvme0n1      - NVMe SSD
  /dev/tty          - 터미널
  /dev/null         - 비트 버킷 (모든 입력 무시)
  /dev/zero         - 0으로 채워진 무한 스트림
  /dev/random       - 난수 생성기
  ```

## 2. 파일 종류

### 2.1 파일 타입

**일반 파일 (`-`)**:
- 텍스트, 바이너리, 실행 파일
- 가장 일반적인 파일 형태

**디렉토리 (`d`)**:
- 파일과 디렉토리를 포함하는 컨테이너
- 특수 파일로 취급

**심볼릭 링크 (`l`)**:
- 다른 파일을 가리키는 포인터
- Windows의 바로가기와 유사
- 생성: `ln -s target linkname`

**블록 디바이스 (`b`)**:
- 블록 단위로 데이터 전송
- 예: 하드 디스크, USB
- 버퍼링 지원

**캐릭터 디바이스 (`c`)**:
- 문자 단위로 데이터 전송
- 예: 터미널, 시리얼 포트
- 버퍼링 없음

**파이프 (`p`)**:
- Named pipe (FIFO)
- 프로세스 간 통신

**소켓 (`s`)**:
- 네트워크 또는 로컬 통신
- Unix domain socket

### 2.2 파일 타입 확인

```bash
ls -l /
# 출력 예:
# drwxr-xr-x  2 root root 4096 Jan 1 12:00 bin
# -rw-r--r--  1 root root  123 Jan 1 12:00 file.txt
# lrwxrwxrwx  1 root root    7 Jan 1 12:00 link -> target
# brw-rw----  1 root disk 8, 0 Jan 1 12:00 sda
# crw-rw-rw-  1 root tty  5, 0 Jan 1 12:00 tty

file /bin/ls            # 파일 타입 상세 정보
stat /bin/ls            # 파일 상태 정보
```

## 3. 링크

### 3.1 하드 링크

**특징**:
- 같은 inode를 공유
- 원본 파일 삭제해도 접근 가능
- 디렉토리에는 생성 불가
- 다른 파일시스템 간 생성 불가

**생성**:
```bash
ln source.txt hardlink.txt
ls -li source.txt hardlink.txt  # 같은 inode 번호
```

### 3.2 심볼릭 링크 (소프트 링크)

**특징**:
- 파일 경로를 저장하는 별도 파일
- 원본 삭제 시 깨진 링크
- 디렉토리에도 생성 가능
- 다른 파일시스템 간 생성 가능

**생성**:
```bash
ln -s /path/to/source.txt symlink.txt
ls -l symlink.txt
# lrwxrwxrwx 1 user user 20 Jan 1 12:00 symlink.txt -> /path/to/source.txt

readlink symlink.txt    # 링크 대상 확인
```

**차이점 비교**:
| 특성 | 하드 링크 | 심볼릭 링크 |
|------|-----------|-------------|
| inode | 동일 | 다름 |
| 원본 삭제 | 영향 없음 | 깨짐 |
| 디렉토리 | 불가 | 가능 |
| 파일시스템 | 동일해야 함 | 상관없음 |
| 크기 | 원본과 동일 | 경로 길이 |

## 4. inode

### 4.1 inode 개념

**정의**:
- **Index Node**: 파일의 메타데이터 저장
- 파일 내용은 별도 데이터 블록에 저장
- 파일 이름은 디렉토리에 저장

**inode 정보**:
- 파일 타입 및 권한
- 소유자 UID, 그룹 GID
- 파일 크기
- 타임스탬프 (atime, mtime, ctime)
- 링크 카운트
- 데이터 블록 포인터

### 4.2 inode 확인

```bash
ls -i file.txt          # inode 번호 확인
stat file.txt           # 상세 정보
df -i                   # inode 사용량

# inode 정보 상세
stat file.txt
# 출력:
#   File: file.txt
#   Size: 1024      Blocks: 8          IO Block: 4096
#   Inode: 12345678 Links: 1
#   Access: 2025-01-01 12:00:00
#   Modify: 2025-01-01 12:00:00
#   Change: 2025-01-01 12:00:00
```

### 4.3 inode 고갈

**문제**:
- 많은 작은 파일 생성 시 inode 부족
- 디스크 공간은 남았지만 파일 생성 불가

**확인 및 해결**:
```bash
df -i                   # inode 사용률 확인
find / -xdev -type f | wc -l  # 파일 개수 확인
# 불필요한 파일 삭제 또는 파일시스템 재생성
```

## 5. 파일시스템 마운트

### 5.1 마운트 개념

**마운트**:
- 파일시스템을 디렉토리 트리에 연결
- 마운트 포인트: 파일시스템이 연결되는 디렉토리

### 5.2 마운트 명령어

**수동 마운트**:
```bash
mount /dev/sdb1 /mnt/usb        # 마운트
mount -t ext4 /dev/sdb1 /mnt    # 파일시스템 타입 지정
mount -o ro /dev/sdb1 /mnt      # 읽기 전용
umount /mnt/usb                 # 언마운트
umount /dev/sdb1                # 디바이스로 언마운트
```

**마운트 확인**:
```bash
mount                   # 마운트된 파일시스템 목록
df -h                   # 디스크 사용량
findmnt                 # 트리 형태로 표시
cat /proc/mounts        # 커널 마운트 정보
```

### 5.3 /etc/fstab

**자동 마운트 설정**:
```
# 형식: <device> <mount point> <type> <options> <dump> <pass>
/dev/sda1    /           ext4    defaults        1 1
/dev/sda2    /home       ext4    defaults        1 2
/dev/sda3    swap        swap    defaults        0 0
UUID=xxx     /boot       ext4    defaults        1 2
/dev/sdb1    /mnt/data   ext4    noauto,user     0 0
```

**필드 설명**:
1. **Device**: 디바이스 파일 또는 UUID
2. **Mount Point**: 마운트 위치
3. **Type**: 파일시스템 타입
4. **Options**: 마운트 옵션
   - `defaults`: rw, suid, dev, exec, auto, nouser, async
   - `noauto`: 부팅 시 자동 마운트 안 함
   - `user`: 일반 사용자도 마운트 가능
   - `ro`: 읽기 전용
   - `rw`: 읽기/쓰기
5. **Dump**: 백업 여부 (0 또는 1)
6. **Pass**: fsck 검사 순서 (0, 1, 2)

**UUID 사용**:
```bash
blkid                   # UUID 확인
blkid /dev/sda1
# /dev/sda1: UUID="xxx-xxx-xxx" TYPE="ext4"

# fstab에 UUID 사용
UUID=xxx-xxx-xxx  /  ext4  defaults  1 1
```

**fstab 테스트**:
```bash
mount -a                # fstab의 모든 항목 마운트
findmnt --verify        # fstab 검증
```

## 6. 파일시스템 관리

### 6.1 파일시스템 생성

```bash
mkfs.ext4 /dev/sdb1             # ext4 생성
mkfs.xfs /dev/sdb1              # XFS 생성
mkfs -t ext4 /dev/sdb1          # 타입 지정
mkfs.ext4 -L mylabel /dev/sdb1  # 레이블 지정
```

### 6.2 파일시스템 검사

```bash
fsck /dev/sdb1                  # 파일시스템 검사
fsck -y /dev/sdb1               # 자동으로 수정
e2fsck /dev/sdb1                # ext 파일시스템 전용
xfs_repair /dev/sdb1            # XFS 복구
```

**주의사항**:
- 언마운트 상태에서 실행
- 루트 파일시스템은 싱글 유저 모드에서 검사

### 6.3 파일시스템 튜닝

```bash
tune2fs -l /dev/sdb1            # ext 정보 확인
tune2fs -L newlabel /dev/sdb1   # 레이블 변경
tune2fs -c 30 /dev/sdb1         # 30번 마운트마다 검사
tune2fs -i 180d /dev/sdb1       # 180일마다 검사
dumpe2fs /dev/sdb1              # 상세 정보
```

### 6.4 디스크 사용량

```bash
df -h                   # 파일시스템 사용량 (human-readable)
df -i                   # inode 사용량
du -sh /home            # 디렉토리 크기
du -h --max-depth=1 /   # 1단계 하위 디렉토리 크기
```

## 7. 시험 대비 핵심 요약

### FHS 주요 디렉토리
- **/bin, /sbin**: 필수 명령어
- **/etc**: 설정 파일
- **/home**: 사용자 홈
- **/var**: 로그, 가변 데이터
- **/proc, /sys**: 가상 파일시스템

### 파일 타입
- `-`: 일반 파일
- `d`: 디렉토리
- `l`: 심볼릭 링크
- `b`: 블록 디바이스
- `c`: 캐릭터 디바이스

### 링크
- **하드 링크**: 같은 inode, `ln source target`
- **심볼릭 링크**: 다른 inode, `ln -s source target`

### 마운트
- **수동**: `mount /dev/sdb1 /mnt`
- **자동**: `/etc/fstab` 설정
- **확인**: `df -h`, `mount`
- **언마운트**: `umount /mnt`

### 파일시스템 관리
- **생성**: `mkfs.ext4`
- **검사**: `fsck`
- **튜닝**: `tune2fs`

---

**이전 챕터**: [시스템 설치 및 부팅 프로세스](02-installation-boot.md)  
**다음 챕터**: [기본 명령어 및 셸](04-basic-commands.md)
