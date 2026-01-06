---
title: NFS & autofs
tags: [linux, network, nfs, autofs, filesystem]
aliases: [NFS, Network File System, autofs]
date modified: 2026-01-06 19:38:00 +09:00
date created: 2026-01-06 19:38:00 +09:00
---

## 🌐 개요 (Overview)

**NFS (Network File System)**는 네트워크를 통해 원격 파일시스템을 로컬처럼 마운트하여 사용할 수 있게 해주는 프로토콜입니다. **autofs**는 필요할 때만 자동으로 마운트하고, 사용하지 않으면 자동으로 언마운트하는 서비스입니다.

---

## 📦 NFS 서버 설정

### 1. 패키지 설치

```bash
# RHEL/CentOS
dnf install nfs-utils

# Ubuntu/Debian
apt install nfs-kernel-server
```

### 2. 공유 디렉토리 설정 (`/etc/exports`)

```bash
# 형식: 공유디렉토리 허용클라이언트(옵션)

# 특정 IP에 읽기/쓰기 허용
/data           192.168.1.100(rw,sync,no_root_squash)

# 서브넷 전체에 읽기 전용 허용
/share          192.168.1.0/24(ro,sync)

# 모든 클라이언트에 허용 (보안상 비권장)
/public         *(ro,sync)
```

### 주요 옵션

| 옵션 | 설명 |
| :--- | :--- |
| `rw` | 읽기/쓰기 허용 |
| `ro` | 읽기 전용 |
| `sync` | 동기화 쓰기 (데이터 안전성 보장) |
| `async` | 비동기 쓰기 (성능 향상, 데이터 손실 위험) |
| `no_root_squash` | 클라이언트의 root를 서버에서도 root로 인정 |
| `root_squash` | 클라이언트의 root를 nobody로 매핑 **(기본값)** |
| `all_squash` | 모든 사용자를 nobody로 매핑 |

### 3. 서비스 시작 및 공유 적용

```bash
# 서비스 시작
systemctl enable --now nfs-server

# exports 변경 사항 적용 (재시작 없이)
exportfs -ra

# 현재 공유 목록 확인
exportfs -v
```

---

## 💻 NFS 클라이언트 설정

### 수동 마운트

```bash
# 원격 NFS 공유 마운트
mount -t nfs 192.168.1.10:/data /mnt/nfs_data

# 마운트 확인
df -hT /mnt/nfs_data
```

### /etc/fstab 영구 마운트

```bash
# /etc/fstab에 추가
192.168.1.10:/data  /mnt/nfs_data  nfs  defaults,_netdev  0 0
```

> [!TIP]
> **`_netdev`** 옵션은 네트워크가 활성화된 후에 마운트하도록 지정합니다. NFS 마운트에 필수적입니다.

---

## 🤖 autofs - 자동 마운트

autofs는 사용자가 해당 디렉토리에 접근할 때만 자동으로 마운트하고, 일정 시간 미사용 시 자동으로 언마운트합니다.

### 1. 패키지 설치

```bash
dnf install autofs
```

### 2. 마스터 맵 설정 (`/etc/auto.master`)

```bash
# 형식: 마운트포인트 맵파일 [옵션]

# 직접 맵
/-          /etc/auto.direct

# 간접 맵 (마운트포인트 아래에 자동 생성)
/mnt/nfs    /etc/auto.nfs   --timeout=300
```

### 3. 맵 파일 설정

#### 직접 맵 (`/etc/auto.direct`)

```bash
# 정확한 마운트 포인트 지정
/mnt/data   -rw,sync   192.168.1.10:/data
/mnt/backup -ro,soft   192.168.1.20:/backup
```

#### 간접 맵 (`/etc/auto.nfs`)

```bash
# /mnt/nfs 아래에 자동 생성
# /mnt/nfs/share -> 192.168.1.10:/share
share       -rw,sync   192.168.1.10:/share
data        -rw,sync   192.168.1.10:/data
```

### 4. 서비스 시작

```bash
systemctl enable --now autofs

# 설정 변경 후 리로드
systemctl reload autofs
```

> [!IMPORTANT]
> **시험 Tip**: autofs의 마스터 맵은 `/etc/auto.master`이고, 실제 마운트 정보는 별도의 맵 파일(예: `/etc/auto.nfs`)에 정의합니다.

---

## 🔍 문제 해결

```bash
# NFS 서버 공유 확인
showmount -e 192.168.1.10

# RPC 서비스 상태 확인
rpcinfo -p

# autofs 디버그 로그
journalctl -u autofs -f
```

---

## 🔗 연결 문서 (Related Documents)

- [[filesystems]] - 파일시스템 개념
- [[samba-server]] - Windows 공유 (SMB/CIFS)
- [[network-commands]] - 네트워크 진단 명령어
