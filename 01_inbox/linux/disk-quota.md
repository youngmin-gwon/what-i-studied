---
title: Disk Quota
tags: [linux, filesystem, quota, disk, administration]
aliases: [디스크 쿼터, 쿼터 관리]
date modified: 2026-01-06 19:46:00 +09:00
date created: 2026-01-06 19:46:00 +09:00
---

## 🌐 개요 (Overview)

**Disk Quota**는 사용자 또는 그룹별로 디스크 사용량을 제한하는 기능입니다. 다중 사용자 환경에서 특정 사용자가 과도하게 디스크를 점유하는 것을 방지합니다.

---

## 🔧 쿼터 설정 절차

### 1. 파일시스템 마운트 옵션 추가

`/etc/fstab`에서 쿼터를 적용할 파일시스템에 옵션 추가:

```bash
# /etc/fstab
/dev/sda1  /home  ext4  defaults,usrquota,grpquota  0 2
```

| 옵션 | 설명 |
| :--- | :--- |
| **usrquota** | 사용자별 쿼터 활성화 |
| **grpquota** | 그룹별 쿼터 활성화 |

마운트 재적용:

```bash
mount -o remount /home
```

### 2. 쿼터 데이터베이스 생성

```bash
# 쿼터 파일 생성 및 초기화
quotacheck -cug /home

# -c: 새 쿼터 파일 생성
# -u: 사용자 쿼터
# -g: 그룹 쿼터
```

생성되는 파일:
- `aquota.user` - 사용자 쿼터 데이터베이스
- `aquota.group` - 그룹 쿼터 데이터베이스

### 3. 쿼터 활성화

```bash
# 쿼터 켜기
quotaon /home

# 쿼터 끄기
quotaoff /home

# 모든 파일시스템에서 쿼터 활성화
quotaon -a
```

---

## 📊 쿼터 설정 방식

### 블록 제한 vs 아이노드 제한

| 구분 | 설명 |
| :--- | :--- |
| **블록 (Block)** | 디스크 용량 제한 (KB 단위) |
| **아이노드 (Inode)** | 파일 개수 제한 |

### Soft Limit vs Hard Limit

| 구분 | 설명 |
| :--- | :--- |
| **Soft Limit** | 경고 한도. 유예 기간(Grace Period) 내 초과 허용 |
| **Hard Limit** | 절대 한도. 초과 불가능 |

> [!IMPORTANT]
> **시험 Tip**: Soft Limit 초과 시 유예 기간(기본 7일) 동안은 사용 가능하지만, 유예 기간이 지나면 Soft Limit 이하로 줄여야 새 파일 생성 가능.

---

## ⚙️ edquota - 쿼터 편집

### 사용자 쿼터 설정

```bash
edquota -u username
```

편집기에서 열리는 내용:

```
Disk quotas for user username (uid 1000):
  Filesystem    blocks   soft    hard   inodes   soft   hard
  /dev/sda1      52000   100000  120000    150    1000   1200
```

| 필드 | 설명 |
| :--- | :--- |
| **blocks** | 현재 사용 중인 블록 (KB) |
| **soft** | 블록 소프트 리밋 |
| **hard** | 블록 하드 리밋 |
| **inodes** | 현재 사용 중인 파일 수 |

### 그룹 쿼터 설정

```bash
edquota -g groupname
```

### 유예 기간 설정

```bash
edquota -t
```

```
Grace period before enforcing soft limits for users:
Time units may be: days, hours, minutes, or seconds
  Filesystem     Block grace period     Inode grace period
  /dev/sda1             7days                  7days
```

### 다른 사용자 설정 복사

```bash
# user1의 쿼터를 user2, user3에 복사
edquota -p user1 user2 user3
```

---

## 📈 쿼터 확인 명령어

### repquota - 전체 보고서

```bash
# 특정 파일시스템 보고서
repquota /home

# 모든 파일시스템 보고서 (상세)
repquota -a -v
```

출력 예시:

```
*** Report for user quotas on device /dev/sda1
Block grace time: 7days; Inode grace time: 7days
                        Block limits                File limits
User            used    soft    hard  grace    used  soft  hard  grace
----------------------------------------------------------------------
root      --      20       0       0              2     0     0       
username  +-   105000  100000  120000  6days    200  1000  1200       
```

- `--`: 제한 내
- `+-`: 블록 소프트 리밋 초과
- `-+`: 아이노드 소프트 리밋 초과
- `++`: 둘 다 초과

### quota - 개인 쿼터 확인

```bash
# 자신의 쿼터 확인
quota

# 특정 사용자 확인 (root)
quota -u username

# 그룹 쿼터 확인
quota -g groupname
```

---

## 🔧 쿼터 명령어 요약

| 명령어 | 용도 |
| :--- | :--- |
| `quotacheck` | 쿼터 데이터베이스 생성/검사 |
| `quotaon` | 쿼터 활성화 |
| `quotaoff` | 쿼터 비활성화 |
| `edquota` | 쿼터 편집 (사용자/그룹/유예기간) |
| `repquota` | 쿼터 보고서 출력 |
| `quota` | 개별 쿼터 확인 |
| `setquota` | 명령줄에서 직접 쿼터 설정 |

### setquota 사용법

```bash
# setquota -u user block-soft block-hard inode-soft inode-hard filesystem
setquota -u username 100000 120000 1000 1200 /home
```

---

## 🔗 연결 문서 (Related Documents)

- [lvm](lvm.md) - LVM 볼륨 관리
- [filesystems](filesystems.md) - 파일시스템 개념
- [user-permission-commands](commands/user-permission-commands.md) - 사용자 관리
