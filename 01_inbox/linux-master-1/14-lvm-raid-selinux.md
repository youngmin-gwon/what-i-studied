---
title: 14-lvm-raid-selinux
tags: []
aliases: []
date modified: 2025-12-29 10:37:00 +09:00
date created: 2025-12-11 09:28:32 +09:00
---

## LVM 및 RAID 추가 내용

### LVM (Logical Volume Manager)

#### LVM 개요

**장점**:
- 유연한 디스크 관리
- 온라인 크기 조정
- 스냅샷 지원
- 여러 디스크를 하나로 통합

**구성 요소**:
```
물리 디스크 (Physical Disk)
    ↓
물리 볼륨 (PV - Physical Volume)
    ↓
볼륨 그룹 (VG - Volume Group)
    ↓
논리 볼륨 (LV - Logical Volume)
    ↓
파일시스템
```

#### LVM 명령어

**물리 볼륨 (PV)**:
```bash
pvcreate /dev/sdb1              # PV 생성
pvdisplay                       # PV 정보
pvs                             # PV 요약
pvremove /dev/sdb1              # PV 제거
```

**볼륨 그룹 (VG)**:
```bash
vgcreate vg0 /dev/sdb1 /dev/sdc1  # VG 생성
vgdisplay                       # VG 정보
vgs                             # VG 요약
vgextend vg0 /dev/sdd1          # VG 확장
vgreduce vg0 /dev/sdd1          # VG 축소
vgremove vg0                    # VG 제거
```

**논리 볼륨 (LV)**:
```bash
lvcreate -L 10G -n lv0 vg0      # 10GB LV 생성
lvcreate -l 100%FREE -n lv1 vg0 # 남은 공간 전체 사용
lvdisplay                       # LV 정보
lvs                             # LV 요약
lvextend -L +5G /dev/vg0/lv0    # 5GB 확장
lvextend -l +100%FREE /dev/vg0/lv0  # 남은 공간 전체 사용
lvreduce -L -5G /dev/vg0/lv0    # 5GB 축소
lvremove /dev/vg0/lv0           # LV 제거
```

**파일시스템 크기 조정**:
```bash
# ext4 확장
lvextend -L +5G /dev/vg0/lv0
resize2fs /dev/vg0/lv0

# ext4 축소 (언마운트 필요)
umount /mnt
e2fsck -f /dev/vg0/lv0
resize2fs /dev/vg0/lv0 10G
lvreduce -L 10G /dev/vg0/lv0

# XFS 확장 (축소 불가)
lvextend -L +5G /dev/vg0/lv0
xfs_growfs /mnt
```

**LVM 스냅샷**:
```bash
# 스냅샷 생성
lvcreate -L 1G -s -n snap0 /dev/vg0/lv0

# 스냅샷 마운트
mount /dev/vg0/snap0 /mnt/snapshot

# 스냅샷 제거
lvremove /dev/vg0/snap0
```

### RAID (Redundant Array of Independent Disks)

#### RAID 레벨

**RAID 0 (Striping)**:
- 최소 디스크: 2 개
- 용량: 전체 합
- 성능: 향상
- 안정성: 없음 (하나 고장 시 전체 손실)
- 용도: 성능 중시, 임시 데이터

**RAID 1 (Mirroring)**:
- 최소 디스크: 2 개
- 용량: 1 개 디스크 크기
- 성능: 읽기 향상
- 안정성: 높음 (하나 고장 시 복구 가능)
- 용도: 중요 데이터, 시스템 디스크

**RAID 5 (Striping with Parity)**:
- 최소 디스크: 3 개
- 용량: (N-1) × 디스크 크기
- 성능: 읽기 향상
- 안정성: 1 개 디스크 고장 허용
- 용도: 균형잡힌 선택

**RAID 6 (Double Parity)**:
- 최소 디스크: 4 개
- 용량: (N-2) × 디스크 크기
- 안정성: 2 개 디스크 고장 허용
- 용도: 높은 안정성 필요

**RAID 10 (1+0)**:
- 최소 디스크: 4 개
- RAID 1 + RAID 0 조합
- 용량: 전체의 50%
- 성능: 높음
- 안정성: 높음

#### mdadm 명령어

**RAID 생성**:
```bash
# RAID 1 생성
mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb1 /dev/sdc1

# RAID 5 생성
mdadm --create /dev/md0 --level=5 --raid-devices=3 /dev/sdb1 /dev/sdc1 /dev/sdd1

# 스페어 디스크 추가
mdadm --create /dev/md0 --level=5 --raid-devices=3 --spare-devices=1 \
  /dev/sdb1 /dev/sdc1 /dev/sdd1 /dev/sde1
```

**RAID 관리**:
```bash
mdadm --detail /dev/md0         # RAID 상세 정보
cat /proc/mdstat                # RAID 상태
mdadm --add /dev/md0 /dev/sde1  # 디스크 추가
mdadm --fail /dev/md0 /dev/sdb1 # 디스크 고장 표시
mdadm --remove /dev/md0 /dev/sdb1  # 디스크 제거
mdadm --stop /dev/md0           # RAID 중지
mdadm --assemble /dev/md0       # RAID 조립
```

**RAID 설정 저장**:
```bash
mdadm --detail --scan >> /etc/mdadm.conf
# 또는
mdadm --detail --scan >> /etc/mdadm/mdadm.conf
```

**RAID 모니터링**:
```bash
mdadm --monitor --scan --daemonise  # 데몬으로 모니터링
```

### SELinux (Security-Enhanced Linux)

#### SELinux 개요

**목적**:
- 강제 접근 제어 (MAC - Mandatory Access Control)
- 프로세스 권한 제한
- 시스템 보안 강화

**모드**:
- **Enforcing**: 정책 강제 적용
- **Permissive**: 정책 위반 로그만 기록
- **Disabled**: SELinux 비활성화

#### SELinux 명령어

**상태 확인**:
```bash
getenforce                      # 현재 모드
sestatus                        # 상세 상태
```

**모드 변경**:
```bash
setenforce 0                    # Permissive 모드
setenforce 1                    # Enforcing 모드
```

**영구 설정**: `/etc/selinux/config`
```
SELINUX=enforcing
# 또는 permissive, disabled
```

**컨텍스트 확인**:
```bash
ls -Z file.txt                  # 파일 컨텍스트
ps -Z                           # 프로세스 컨텍스트
id -Z                           # 사용자 컨텍스트
```

**컨텍스트 변경**:
```bash
chcon -t httpd_sys_content_t /var/www/html/index.html
restorecon -v /var/www/html/index.html  # 기본값으로 복원
```

**불린 값**:
```bash
getsebool -a                    # 모든 불린 값
getsebool httpd_can_network_connect
setsebool httpd_can_network_connect on  # 임시
setsebool -P httpd_can_network_connect on  # 영구
```

**로그 확인**:
```bash
ausearch -m avc -ts recent      # 최근 AVC 거부
audit2why < /var/log/audit/audit.log  # 거부 이유
audit2allow -a                  # 정책 제안
```

---

이 내용을 03-filesystem.md 파일 끝에 추가하면 좋습니다.
