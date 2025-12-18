# 시스템 설치 및 부팅 프로세스

## 1. 리눅스 설치

### 1.1 설치 전 준비사항

**하드웨어 요구사항**:
- **최소**: CPU 1GHz, RAM 512MB, HDD 10GB
- **권장**: CPU 2GHz 이상, RAM 2GB 이상, SSD 20GB 이상
- **호환성 확인**: `lspci`, `lsusb` 명령으로 하드웨어 인식 확인

**설치 매체**:
- **DVD/USB**: ISO 이미지 다운로드 후 부팅 가능한 매체 생성
- **네트워크 설치**: PXE 부팅을 통한 원격 설치
- **가상 머신**: VirtualBox, VMware, KVM

### 1.2 파티션 구성

**파티션 종류**:
- **주 파티션 (Primary)**: 최대 4개, 부팅 가능
- **확장 파티션 (Extended)**: 주 파티션 1개를 확장으로 사용
- **논리 파티션 (Logical)**: 확장 파티션 내부에 생성

**파티션 테이블**:
- **MBR (Master Boot Record)**: 최대 2TB, 4개 주 파티션
- **GPT (GUID Partition Table)**: 2TB 이상, 128개 파티션, UEFI 지원

**권장 파티션 구성**:
```
/boot      - 500MB~1GB   (부트 로더, 커널 이미지)
swap       - RAM의 1~2배 (스왑 공간)
/          - 20GB 이상   (루트 파일시스템)
/home      - 나머지      (사용자 데이터)
```

**추가 파티션 (서버 환경)**:
```
/var       - 로그, 캐시, 스풀
/tmp       - 임시 파일
/usr       - 응용 프로그램
/opt       - 추가 소프트웨어
```

### 1.3 파일 시스템 선택

**주요 파일 시스템**:
- **ext4**: 리눅스 표준, 저널링, 최대 16TB
- **XFS**: 대용량 파일, 높은 성능, RHEL 기본
- **Btrfs**: 스냅샷, 압축, 아직 실험적
- **swap**: 스왑 공간 전용

**파일 시스템 생성**:
```bash
mkfs.ext4 /dev/sda1
mkfs.xfs /dev/sda2
mkswap /dev/sda3
```

## 2. 부팅 프로세스

### 2.1 부팅 단계 개요

```
1. BIOS/UEFI 초기화
   ↓
2. 부트 로더 실행 (GRUB)
   ↓
3. 커널 로딩
   ↓
4. initramfs 실행
   ↓
5. systemd/init 시작
   ↓
6. 타겟/런레벨 도달
   ↓
7. 로그인 프롬프트
```

### 2.2 BIOS vs UEFI

**BIOS (Basic Input/Output System)**:
- **레거시 방식**: 1980년대부터 사용
- **16비트 모드**: 제한적인 기능
- **MBR 부팅**: 첫 512바이트에서 부트 로더 실행
- **제약**: 2TB 디스크 제한

**UEFI (Unified Extensible Firmware Interface)**:
- **현대적 인터페이스**: GUI, 마우스 지원
- **GPT 지원**: 2TB 이상 디스크
- **Secure Boot**: 서명된 부트 로더만 실행
- **EFI 시스템 파티션**: FAT32, 100~500MB

### 2.3 GRUB 부트 로더

**GRUB2 (GRand Unified Bootloader)**:
- **설정 파일**: `/boot/grub2/grub.cfg` (자동 생성)
- **사용자 설정**: `/etc/default/grub`
- **설정 적용**: `grub2-mkconfig -o /boot/grub2/grub.cfg`

**주요 설정 옵션**:
```bash
GRUB_TIMEOUT=5                    # 부팅 대기 시간
GRUB_DEFAULT=0                    # 기본 부팅 항목
GRUB_CMDLINE_LINUX="quiet splash" # 커널 파라미터
GRUB_DISABLE_RECOVERY="true"      # 복구 모드 비활성화
```

**GRUB 명령어**:
```bash
grub2-install /dev/sda           # GRUB 설치
grub2-mkconfig -o /boot/grub2/grub.cfg  # 설정 생성
grubby --default-kernel          # 기본 커널 확인
```

**부팅 시 편집**:
- `e` 키: 부팅 항목 편집
- `c` 키: GRUB 콘솔
- 커널 라인에 `single` 또는 `1` 추가: 싱글 유저 모드

### 2.4 커널 부팅

**커널 이미지**:
- **위치**: `/boot/vmlinuz-<version>`
- **압축**: gzip 또는 bzip2로 압축된 커널
- **로딩**: GRUB이 메모리에 로드

**커널 파라미터**:
```bash
quiet          # 부팅 메시지 최소화
splash         # 부팅 스플래시 화면
ro             # 루트를 읽기 전용으로 마운트
root=/dev/sda1 # 루트 파일 시스템 지정
init=/bin/bash # 대체 init 프로세스
```

**커널 확인**:
```bash
uname -r       # 커널 버전
uname -a       # 전체 시스템 정보
cat /proc/version  # 커널 상세 정보
```

### 2.5 initramfs

**역할**:
- **초기 램 디스크**: 임시 루트 파일 시스템
- **드라이버 로딩**: 루트 파일 시스템 접근에 필요한 모듈
- **위치**: `/boot/initramfs-<version>.img`

**생성 및 관리**:
```bash
# Debian/Ubuntu
update-initramfs -u          # 업데이트
update-initramfs -c -k all   # 모든 커널용 생성

# RHEL/CentOS
dracut --force               # 현재 커널용 생성
dracut --force --kver <version>  # 특정 커널용
```

**내용 확인**:
```bash
lsinitrd /boot/initramfs-$(uname -r).img
# 또는
zcat /boot/initrd.img-$(uname -r) | cpio -t
```

## 3. Init 시스템

### 3.1 systemd

**특징**:
- **병렬 시작**: 서비스 동시 시작으로 부팅 속도 향상
- **의존성 관리**: 서비스 간 의존성 자동 해결
- **소켓 활성화**: 필요 시 서비스 시작
- **표준화**: 대부분의 주요 배포판 채택

**주요 개념**:
- **Unit**: systemd가 관리하는 객체 (service, socket, target 등)
- **Target**: 여러 unit의 그룹 (런레벨과 유사)
- **Unit 파일**: `/usr/lib/systemd/system/`, `/etc/systemd/system/`

**systemctl 명령어**:
```bash
systemctl start httpd        # 서비스 시작
systemctl stop httpd         # 서비스 중지
systemctl restart httpd      # 서비스 재시작
systemctl reload httpd       # 설정 다시 로드
systemctl status httpd       # 상태 확인
systemctl enable httpd       # 부팅 시 자동 시작
systemctl disable httpd      # 자동 시작 비활성화
systemctl is-enabled httpd   # 활성화 여부 확인
systemctl list-units         # 모든 unit 목록
systemctl list-unit-files    # unit 파일 목록
```

**타겟 관리**:
```bash
systemctl get-default        # 기본 타겟 확인
systemctl set-default multi-user.target  # 기본 타겟 설정
systemctl isolate rescue.target  # 타겟 전환
```

### 3.2 런레벨과 타겟

**전통적 런레벨 (SysV init)**:
```
0 - halt (시스템 종료)
1 - single user mode (싱글 유저, 복구 모드)
2 - multi-user without networking
3 - multi-user with networking (텍스트 모드)
4 - unused (사용자 정의)
5 - graphical (그래픽 모드)
6 - reboot (재부팅)
```

**systemd 타겟 매핑**:
```
poweroff.target    ← runlevel 0
rescue.target      ← runlevel 1
multi-user.target  ← runlevel 3
graphical.target   ← runlevel 5
reboot.target      ← runlevel 6
```

**타겟 전환**:
```bash
systemctl isolate multi-user.target  # 텍스트 모드
systemctl isolate graphical.target   # 그래픽 모드
systemctl isolate rescue.target      # 복구 모드
```

### 3.3 부팅 문제 해결

**싱글 유저 모드 진입**:
1. GRUB 메뉴에서 `e` 키
2. 커널 라인 끝에 `single` 또는 `systemd.unit=rescue.target` 추가
3. `Ctrl+X`로 부팅

**응급 모드 (Emergency Mode)**:
- 커널 파라미터: `systemd.unit=emergency.target`
- 최소한의 환경, 루트 파일시스템만 마운트

**부팅 로그 확인**:
```bash
journalctl -b           # 현재 부팅 로그
journalctl -b -1        # 이전 부팅 로그
dmesg                   # 커널 메시지
dmesg | grep -i error   # 에러 메시지만
```

**일반적인 문제**:
- **GRUB 손상**: Live CD로 부팅 후 `grub2-install` 실행
- **fstab 오류**: 싱글 유저 모드에서 `/etc/fstab` 수정
- **커널 패닉**: 이전 커널로 부팅 또는 커널 파라미터 조정

## 4. 시스템 종료 및 재부팅

### 4.1 종료 명령어

**shutdown**:
```bash
shutdown -h now         # 즉시 종료
shutdown -h +10         # 10분 후 종료
shutdown -h 23:00       # 23시에 종료
shutdown -r now         # 즉시 재부팅
shutdown -c             # 예약된 종료 취소
```

**기타 명령어**:
```bash
halt                    # 시스템 정지
poweroff                # 전원 끄기
reboot                  # 재부팅
init 0                  # 종료 (런레벨 0)
init 6                  # 재부팅 (런레벨 6)
systemctl poweroff      # systemd 종료
systemctl reboot        # systemd 재부팅
```

### 4.2 전원 관리

**ACPI (Advanced Configuration and Power Interface)**:
- **절전 모드**: Suspend to RAM (S3)
- **최대 절전**: Hibernate, Suspend to Disk (S4)
- **하이브리드**: 두 가지 혼합

**명령어**:
```bash
systemctl suspend       # 절전 모드
systemctl hibernate     # 최대 절전 모드
systemctl hybrid-sleep  # 하이브리드 절전
```

## 5. 시험 대비 핵심 요약

### 파티션 및 파일시스템
- **MBR**: 2TB 제한, 4개 주 파티션
- **GPT**: UEFI, 2TB 이상, 128개 파티션
- **ext4**: 리눅스 표준 파일시스템
- **XFS**: 대용량, 고성능

### 부팅 프로세스
1. BIOS/UEFI → 2. GRUB → 3. 커널 → 4. initramfs → 5. systemd → 6. 타겟

### GRUB
- **설정**: `/etc/default/grub`
- **적용**: `grub2-mkconfig`
- **설치**: `grub2-install`

### systemd
- **서비스 관리**: `systemctl start/stop/restart/status`
- **부팅 설정**: `systemctl enable/disable`
- **타겟**: `multi-user.target`, `graphical.target`

### 런레벨
- **3**: 텍스트 모드 (multi-user.target)
- **5**: 그래픽 모드 (graphical.target)
- **1**: 싱글 유저 모드 (rescue.target)

---

**이전 챕터**: [리눅스 개요 및 역사](01-linux-overview.md)  
**다음 챕터**: [파일 시스템 및 디렉토리 구조](03-filesystem.md)
