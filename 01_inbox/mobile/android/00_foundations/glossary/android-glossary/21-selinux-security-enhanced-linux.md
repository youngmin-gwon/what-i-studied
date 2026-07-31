# SELinux (Security-Enhanced Linux)

상위 노트: [android-glossary](01_inbox/mobile/android/00_foundations/glossary/android-glossary.md)

**정의**: Mandatory Access Control 보안 메커니즘

**상세**:

모든 프로세스/파일에 보안 레이블을 부여하고 정책으로 접근을 제어한다. 루트 권한을 획득해도 SELinux 정책이 막으면 시스템 파일을 수정할 수 없다.

**모드**:

```bash
# 모드 확인
adb shell getenforce

# Enforcing: 정책 강제 (기본)
# Permissive: 정책 기록만 (개발용)
```

**도메인 예시**:

```
u:r:untrusted_app:s0:c512     # 일반 앱
u:r:system_server:s0           # system_server
u:r:init:s0                    # init
```

**거부 로그**:

```bash
adb logcat | grep avc

# avc: denied { read } for scontext=u:r:untrusted_app:s0 ...
```

**관련**: [selinux](01_inbox/linux/security/selinux.md), [android-security-sandbox](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/android-security-sandbox.md)

---

---
