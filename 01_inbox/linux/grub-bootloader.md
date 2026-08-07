---
title: GRUB2 Bootloader
tags: [linux, boot, grub2, administration]
aliases: [GRUB, GRUB2, 부트로더]
date modified: 2026-01-05 23:55:12 +09:00
date created: 2026-01-05 23:55:12 +09:00
---

## 🌐 개요 (Overview)

**GRUB2 (GRand Unified Bootloader version 2)** 는 대부분의 현대 Linux 배포판에서 사용하는 표준 부트로더입니다. 커널을 메모리에 로드하고, 부팅 파라미터를 전달하며, 멀티 부팅 환경을 관리하는 역할을 합니다.

## 🏗️ GRUB2 설정 체계 (Configuration Hierarchy)

과거 GRUB Legacy와 달리, `grub.cfg` 파일을 직접 수정하는 것은 권장되지 않습니다. 대신 템플릿과 설정 파일을 수정한 후 **설정 생성 명령** 을 실행해야 합니다.

### 1. 주요 설정 파일 및 경로

| 경로 (Path) | 역할 | 특징 |
| :--- | :--- | :--- |
| **`/etc/default/grub`** | **사용자 주요 설정 파일** | 타임아웃, 커널 파라미터, 배경화면 등 설정 |
| **`/etc/grub.d/`** | 스크립트 디렉토리 | 부팅 메뉴 항목을 생성하는 템플릿들 (00_header, 10_linux 등) |
| **`/boot/grub2/grub.cfg`** | **최종 실행 설정 파일** | 직접 수정 금지 (CentOS/RHEL 계열 기본 경로) |
| `/boot/grub/grub.cfg` | 최종 실행 설정 파일 | Ubuntu/Debian 계열 기본 경로 |

### 2. 설정 적용 명령어

설정을 변경한 후에는 반드시 다음 명령어를 통해 최종 `grub.cfg`를 갱신해야 합니다.

```bash
# CentOS / RHEL (BIOS 환경)
grub2-mkconfig -o /boot/grub2/grub.cfg

# CentOS / RHEL (UEFI 환경)
grub2-mkconfig -o /boot/efi/EFI/centos/grub.cfg

# Ubuntu / Debian
update-grub
# (실제로는 grub-mkconfig -o /boot/grub/grub.cfg를 실행하는 스크립트)
```

> [!IMPORTANT]
> **`-o` 옵션**: Output의 약자로, 생성된 설정을 저장할 경로를 지정합니다. 이 옵션 없이는 화면에 출력만 되고 파일에 저장되지 않습니다.

---

## ⚙️ /etc/default/grub 주요 옵션

```bash
GRUB_TIMEOUT=5              # 부팅 메뉴 대기 시간 (초)
GRUB_DISTRIBUTOR="$(sed 's, release .*,,g' /etc/system-release)"
GRUB_DEFAULT=saved          # 기본 부팅 항목 (0번 또는 saved)
GRUB_DISABLE_SUBMENU=true    # 서브메뉴 사용 안 함
GRUB_TERMINAL_OUTPUT="console"
GRUB_CMDLINE_LINUX="rhgb quiet" # 커널 부팅 파라미터 (그래픽 부팅, 로그 숨김)
GRUB_DISABLE_RECOVERY="true" # 복구 모드 메뉴 숨김
```

---

## 📝 자주 틀리는 포인트 (Exam Tips)

1.  **설정 파일 위치**: 사용자가 편집해야 할 공통 설정 파일은 **`/etc/default/grub`** 입니다.
2.  **명령어**: 설정을 반영하는 명령어는 **`grub2-mkconfig`** 입니다. (`grub2-mkfconfig` 같은 오타 주의)
3.  **경로 함정**: CentOS 7 이후 버전은 `grub2`를 사용하므로 `/boot/grub2/` 경로를 사용합니다. `/boot/grub/`은 예전 방식이거나 타 배포판 방식입니다.
4.  **확인 옵션**: `-o` 옵션을 빼먹지 말 것!

---

## 🔗 연결 문서 (Related Documents)

- [boot-sequence](../operating-systems/boot-sequence.md) - 전체 부팅 단계 (BIOS -> GRUB -> Kernel)
- [linux-kernel](../operating-systems/linux-kernel.md) - 부트로더가 로드하는 리눅스 커널 상세
- [filesystem-hierarchy-standard](filesystem-hierarchy-standard.md) - `/boot` 디렉토리의 의미
