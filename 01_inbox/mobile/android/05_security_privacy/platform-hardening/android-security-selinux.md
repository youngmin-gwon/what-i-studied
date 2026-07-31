---
title: android-security-selinux
tags: [android, android/security, android/selinux]
aliases: [MAC, SEAndroid, 강제적 접근 통제]
date modified: 2026-04-05 17:43:38 +09:00
date created: 2026-04-05 16:29:29 +09:00
---

## [[mobile-security]] > [[android-security-selinux]]

### SEAndroid (Security Enhancements for Android)

안드로이드는 리눅스 커널의 **LSM(Linux Security Module)** 프레임워크 위에 커스텀된 **SELinux** 정책인 **SEAndroid**를 탑재하여 강제적 접근 통제(MAC)를 수행한다.

#### MAC(Mandatory Access Control) vs DAC

- **DAC (Discretionary Access Control)**: 파일의 소유자가 권한(`rwx`)을 결정. 루트(Root)는 모든 권한을 가진다.
- **MAC (SEAndroid)**: 시스템 관리자가 정의한 보안 정책에 따라 모든 접근이 결정된다. **루트 사용자라도 정책에 위배되는 행동은 차단된다.**

#### 도메인 및 타입 격리 (Domain & Type Enforcement)

모든 프로세스는 `domain` 을, 모든 객체(파일, 소켓 등)는 `type` 을 부여받는다.

```bash
# 앱 프로세스의 보안 컨텍스트
u:r:untrusted_app:s0:c512,c768  # domain: untrusted_app

# 파일의 보안 컨텍스트
u:object_r:app_data_file:s0    # type: app_data_file
```

**주요 정책 정책**:

1. `file_contexts`: 경로별 레이블 설정.
2. `seapp_contexts`: 앱의 `UID`, `isPrivileged` 여부에 따라 도메인 할당.
3. `property_contexts`: 시스템 속성 접근 제어.

#### 실무적 의의: 권한 상승 공격 방어

공격자가 커널 취약점을 이용해 `UID 0`(Root)을 획득하더라도, SELinux 정책이 `untrusted_app` 도메인에 대해 `/system` 파티션 쓰기나 특정 커널 노드 접근을 금지(`neverallow`)하고 있다면 공격은 실패한다. 이는 샌드박스의 "마지막 방어선" 역할을 한다.

#### 연관 문서

- [[android-security-sandbox]] - 기본 격리 계층
- [[android-kernel]] - SELinux 를 구동하는 커널 기초
