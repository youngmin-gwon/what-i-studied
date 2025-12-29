---
title: 12-backup-recovery
tags: []
aliases: []
date modified: 2025-12-29 10:35:57 +09:00
date created: 2025-12-18 16:21:20 +09:00
---

## 백업 및 복구

### 1. 백업 전략

#### 1.1 백업 유형

**전체 백업 (Full Backup)**:
- 모든 데이터 백업
- 복구 간단
- 시간과 공간 많이 소요
- 주기: 주 1 회 또는 월 1 회

**증분 백업 (Incremental Backup)**:
- 마지막 백업 이후 변경된 파일만
- 빠르고 공간 절약
- 복구 시 모든 증분 필요
- 주기: 매일

**차등 백업 (Differential Backup)**:
- 마지막 전체 백업 이후 변경된 파일
- 증분보다 느리지만 복구 쉬움
- 전체 + 마지막 차등만 필요
- 주기: 매일 또는 주 2-3 회

#### 1.2 백업 계획

**3-2-1 규칙**:
- **3 개 복사본**: 원본 + 백업 2 개
- **2 개 매체**: 다른 저장 매체 사용
- **1 개 오프사이트**: 원격 위치에 보관

**고려사항**:
- **RPO (Recovery Point Objective)**: 허용 가능한 데이터 손실량
- **RTO (Recovery Time Objective)**: 허용 가능한 복구 시간
- **보관 기간**: 법적 요구사항, 비즈니스 요구
- **암호화**: 민감한 데이터 보호
- **테스트**: 정기적인 복구 테스트

### 2. tar 를 이용한 백업

#### 2.1 tar 기본

**아카이브 생성**:
```bash
tar -cvf backup.tar /path/to/dir        # 아카이브 생성
tar -czvf backup.tar.gz /path/to/dir    # gzip 압축
tar -cjvf backup.tar.bz2 /path/to/dir   # bzip2 압축
tar -cJvf backup.tar.xz /path/to/dir    # xz 압축
```

**옵션**:
- `-c`: create (생성)
- `-x`: extract (추출)
- `-t`: list (목록)
- `-v`: verbose (상세)
- `-f`: file (파일 지정)
- `-z`: gzip
- `-j`: bzip2
- `-J`: xz
- `-p`: 권한 보존
- `-P`: 절대 경로 사용

**아카이브 추출**:
```bash
tar -xvf backup.tar                     # 추출
tar -xzvf backup.tar.gz                 # gzip 압축 해제
tar -xvf backup.tar -C /restore/path    # 특정 디렉토리에
tar -xvf backup.tar file.txt            # 특정 파일만
```

**아카이브 확인**:
```bash
tar -tvf backup.tar                     # 목록 확인
tar -tvf backup.tar | grep file.txt     # 파일 검색
```

#### 2.2 증분 백업

**스냅샷 파일 사용**:
```bash
# 전체 백업
tar -czf full_backup.tar.gz -g snapshot.snar /data

# 증분 백업 (1일차)
tar -czf incr_day1.tar.gz -g snapshot.snar /data

# 증분 백업 (2일차)
tar -czf incr_day2.tar.gz -g snapshot.snar /data
```

**복구**:
```bash
# 전체 백업 복구
tar -xzf full_backup.tar.gz -g /dev/null

# 증분 백업 순차 복구
tar -xzf incr_day1.tar.gz -g /dev/null
tar -xzf incr_day2.tar.gz -g /dev/null
```

#### 2.3 백업 스크립트 예제

```bash
#!/bin/bash
# 일일 백업 스크립트

BACKUP_DIR="/backup"
SOURCE_DIR="/data"
DATE=$(date +%Y%m%d)
BACKUP_FILE="backup_${DATE}.tar.gz"

# 백업 생성
tar -czf "${BACKUP_DIR}/${BACKUP_FILE}" "${SOURCE_DIR}"

# 결과 확인
if [ $? -eq 0 ]; then
    echo "Backup successful: ${BACKUP_FILE}"
    
    # 30일 이상 된 백업 삭제
    find "${BACKUP_DIR}" -name "backup_*.tar.gz" -mtime +30 -delete
else
    echo "Backup failed!"
    exit 1
fi
```

### 3. rsync 를 이용한 백업

#### 3.1 rsync 기본

**특징**:
- 증분 전송 (변경된 부분만)
- 네트워크 백업 지원
- 권한, 타임스탬프 보존
- 압축 전송

**기본 사용**:
```bash
rsync -av /source/ /destination/        # 로컬 동기화
rsync -av --delete /source/ /dest/      # 삭제된 파일도 반영
rsync -avz /source/ user@remote:/dest/  # 원격 백업
rsync -av --progress /source/ /dest/    # 진행률 표시
```

**옵션**:
- `-a`: archive (권한, 타임스탬프 등 보존)
- `-v`: verbose
- `-z`: 압축 전송
- `-r`: 재귀
- `-u`: 업데이트 (최신 파일만)
- `-n`: dry-run (실제 실행 안 함)
- `--delete`: 소스에 없는 파일 삭제
- `--exclude`: 제외 패턴
- `--include`: 포함 패턴
- `--progress`: 진행률
- `--bwlimit`: 대역폭 제한 (KB/s)

#### 3.2 rsync 고급 사용

**제외 패턴**:
```bash
rsync -av --exclude='*.log' /source/ /dest/
rsync -av --exclude='*.tmp' --exclude='cache/' /source/ /dest/
rsync -av --exclude-from=exclude.txt /source/ /dest/
```

**SSH 를 통한 원격 백업**:
```bash
rsync -avz -e ssh /source/ user@remote:/dest/
rsync -avz -e "ssh -p 2222" /source/ user@remote:/dest/  # 포트 지정
```

**대역폭 제한**:
```bash
rsync -avz --bwlimit=1000 /source/ /dest/  # 1000 KB/s 제한
```

**백업 스크립트**:
```bash
#!/bin/bash
# rsync 백업 스크립트

SOURCE="/data"
DEST="/backup/current"
BACKUP_DIR="/backup"
DATE=$(date +%Y%m%d)

# 이전 백업을 날짜별로 이동
if [ -d "$DEST" ]; then
    mv "$DEST" "${BACKUP_DIR}/backup_${DATE}"
fi

# 새 백업 생성
rsync -av --delete "$SOURCE/" "$DEST/"

# 결과 확인
if [ $? -eq 0 ]; then
    echo "Backup successful"
else
    echo "Backup failed"
    exit 1
fi
```

#### 3.3 스냅샷 백업

**하드 링크를 이용한 공간 절약**:
```bash
#!/bin/bash
# 스냅샷 백업

BACKUP_DIR="/backup"
CURRENT="${BACKUP_DIR}/current"
DATE=$(date +%Y%m%d_%H%M%S)
SNAPSHOT="${BACKUP_DIR}/snapshot_${DATE}"

# 이전 백업과 링크하여 새 스냅샷 생성
rsync -av --delete --link-dest="${CURRENT}" /data/ "${SNAPSHOT}/"

# current 링크 업데이트
rm -f "${CURRENT}"
ln -s "${SNAPSHOT}" "${CURRENT}"
```

### 4. dd 를 이용한 백업

#### 4.1 dd 기본

**디스크 이미지 생성**:
```bash
dd if=/dev/sda of=/backup/disk.img      # 전체 디스크
dd if=/dev/sda1 of=/backup/sda1.img     # 파티션
dd if=/dev/sda of=/dev/sdb               # 디스크 복제
```

**옵션**:
- `if`: input file (소스)
- `of`: output file (대상)
- `bs`: block size (기본 512 바이트)
- `count`: 블록 개수
- `status=progress`: 진행률 표시

**블록 크기 최적화**:
```bash
dd if=/dev/sda of=/backup/disk.img bs=4M status=progress
```

#### 4.2 압축과 함께 사용

```bash
# 백업
dd if=/dev/sda bs=4M | gzip > /backup/disk.img.gz

# 복구
gunzip -c /backup/disk.img.gz | dd of=/dev/sda bs=4M
```

#### 4.3 네트워크를 통한 백업

```bash
# 서버 (수신)
nc -l 9000 | dd of=/dev/sdb bs=4M

# 클라이언트 (송신)
dd if=/dev/sda bs=4M | nc server_ip 9000
```

#### 4.4 주의사항

- **위험**: 잘못 사용 시 데이터 손실
- **대상 확인**: of 경로 신중히 확인
- **크기**: 전체 디스크 복사로 시간 오래 걸림
- **파일시스템 무관**: 바이트 단위 복사

### 5. 데이터베이스 백업

#### 5.1 MySQL/MariaDB

**mysqldump**:
```bash
# 단일 데이터베이스
mysqldump -u root -p database_name > backup.sql

# 모든 데이터베이스
mysqldump -u root -p --all-databases > all_backup.sql

# 특정 테이블
mysqldump -u root -p database_name table1 table2 > tables.sql

# 압축
mysqldump -u root -p database_name | gzip > backup.sql.gz

# 원격 서버
mysqldump -h remote_host -u root -p database_name > backup.sql
```

**복구**:
```bash
mysql -u root -p database_name < backup.sql
gunzip < backup.sql.gz | mysql -u root -p database_name
```

#### 5.2 PostgreSQL

**pg_dump**:
```bash
# 단일 데이터베이스
pg_dump database_name > backup.sql

# 압축 형식
pg_dump -Fc database_name > backup.dump

# 모든 데이터베이스
pg_dumpall > all_backup.sql
```

**복구**:
```bash
psql database_name < backup.sql
pg_restore -d database_name backup.dump
```

### 6. LVM 스냅샷

#### 6.1 스냅샷 생성

```bash
# 스냅샷 생성 (10GB 크기)
lvcreate -L 10G -s -n snap_lv /dev/vg0/lv0

# 스냅샷 마운트
mkdir /mnt/snapshot
mount /dev/vg0/snap_lv /mnt/snapshot

# 백업 수행
tar -czf /backup/lv_backup.tar.gz /mnt/snapshot

# 스냅샷 제거
umount /mnt/snapshot
lvremove /dev/vg0/snap_lv
```

#### 6.2 장점

- **일관성**: 특정 시점의 일관된 백업
- **온라인**: 서비스 중단 없이 백업
- **빠름**: 스냅샷 생성 즉시

### 7. 클라우드 백업

#### 7.1 rclone

**설정**:
```bash
rclone config              # 대화형 설정
```

**사용**:
```bash
# 업로드
rclone copy /data remote:backup

# 동기화
rclone sync /data remote:backup

# 다운로드
rclone copy remote:backup /restore
```

#### 7.2 AWS S3

**aws-cli**:
```bash
# 업로드
aws s3 cp /data s3://bucket/backup/ --recursive

# 동기화
aws s3 sync /data s3://bucket/backup/

# 다운로드
aws s3 cp s3://bucket/backup/ /restore --recursive
```

### 8. 복구 절차

#### 8.1 파일 복구

**tar**:
```bash
# 전체 복구
tar -xzvf backup.tar.gz -C /restore/

# 특정 파일만
tar -xzvf backup.tar.gz path/to/file
```

**rsync**:
```bash
rsync -av /backup/current/ /restore/
```

#### 8.2 시스템 복구

**Live CD/USB 부팅**:
1. Live 환경 부팅
2. 파티션 마운트
3. 백업 복구
4. GRUB 재설치

**예제**:
```bash
# 파티션 마운트
mount /dev/sda1 /mnt
mount /dev/sda2 /mnt/home

# 백업 복구
tar -xzvf /backup/system.tar.gz -C /mnt

# chroot
mount --bind /dev /mnt/dev
mount --bind /proc /mnt/proc
mount --bind /sys /mnt/sys
chroot /mnt

# GRUB 재설치
grub2-install /dev/sda
grub2-mkconfig -o /boot/grub2/grub.cfg

# 재부팅
exit
umount -R /mnt
reboot
```

#### 8.3 데이터베이스 복구

**MySQL**:
```bash
mysql -u root -p database_name < backup.sql
```

**PostgreSQL**:
```bash
psql database_name < backup.sql
```

### 9. 백업 자동화

#### 9.1 cron 을 이용한 스케줄링

```bash
# crontab -e
# 매일 02:00에 백업
0 2 * * * /usr/local/bin/backup.sh

# 매주 일요일 03:00에 전체 백업
0 3 * * 0 /usr/local/bin/full_backup.sh

# 평일 매일 02:00에 증분 백업
0 2 * * 1-5 /usr/local/bin/incremental_backup.sh
```

#### 9.2 systemd timer

**backup.timer**:
```ini
[Unit]
Description=Daily Backup Timer

[Timer]
OnCalendar=daily
OnCalendar=*-*-* 02:00:00
Persistent=true

[Install]
WantedBy=timers.target
```

**backup.service**:
```ini
[Unit]
Description=Backup Service

[Service]
Type=oneshot
ExecStart=/usr/local/bin/backup.sh
```

### 10. 시험 대비 핵심 요약

#### 백업 유형
- **전체**: 모든 데이터
- **증분**: 마지막 백업 이후 변경분
- **차등**: 마지막 전체 백업 이후 변경분

#### tar
- **생성**: `tar -czf backup.tar.gz /data`
- **추출**: `tar -xzf backup.tar.gz`
- **목록**: `tar -tzf backup.tar.gz`
- **증분**: `-g snapshot.snar`

#### rsync
- **기본**: `rsync -av /source/ /dest/`
- **삭제 반영**: `rsync -av --delete`
- **원격**: `rsync -avz user@remote:/dest/`
- **제외**: `--exclude='*.log'`

#### dd
- **백업**: `dd if=/dev/sda of=disk.img bs=4M`
- **복구**: `dd if=disk.img of=/dev/sda bs=4M`
- **압축**: `dd if=/dev/sda | gzip > disk.img.gz`

#### 데이터베이스
- **MySQL**: `mysqldump`, `mysql`
- **PostgreSQL**: `pg_dump`, `psql`

#### 자동화
- **cron**: `crontab -e`
- **systemd**: timer unit

---

**이전 챕터**: [시스템 모니터링 및 로그](11-monitoring-logs.md)
**메인으로**: [리눅스마스터 1급 자격증 학습 가이드](../bash-scripting-summary/README.md)
