---
title: init-security-is-selinux-domain-and-capability-boundary
tags: [android, android/boot-runtime, android/init, android/system-internals]
aliases: ["init 보안은 SELinux domain과 capability 경계로 정의된다"]
date modified: 2026-08-05 14:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## init 보안은 SELinux domain 과 capability 경계로 정의된다

상위 문서: [init 서비스 계약](init-service-contracts.md)
배경 지식: [SELinux](01_inbox/linux/security/selinux.md), [네임스페이스](01_inbox/linux/container-basics.md)

init 보안 모델은 서비스 프로세스 실행 시 Linux의 root 권한 남용을 방지하기 위해 UID/GID 분리뿐만 아니라 POSIX Capabilities의 엄격한 제한(Drop Capabilities) 및 SELinux Domain Transition을 통해 보안 경계(Security Boundary)를 격리하는 메커니즘이다.

### 내부 동작 메커니즘 (Internal Mechanism)

1. **SELinux Domain Transition (`seclabel` / `type_transition`)**:
   - `init` 프로세스 자체는 `u:r:init:s0` 도메인에서 실행된다.
   - 자식 서비스를 `fork`/`execv`할 때, Executable 파일의 SELinux Context(예: `u:object_r:zygote_exec:s0`)와 정책 규칙에 따라 자식 프로세스를 표적 도메인(예: `u:r:zygote:s0`)으로 자동 전이시킨다.
2. **Linux Capability Drop & Ambient Capabilities**:
   - `init`은 `SetCapsAndCombatibleCapabilities()`를 통해 `capabilities` 옵션에 명시된 비트마스크만 획득(Inheritable / Permitted / Effective / Ambient)시키고 나머지 Root Capability(예: `CAP_SYS_ADMIN`, `CAP_SYS_RAWIO`)를 모두 Drop 처리한다.
3. **Namespace Isolation & Seccomp Filter**:
   - `seccomp`, `mount namespace`, `net namespace` 옵션을 이용하여 하드웨어 접근 및 시스템 호출 수면을 추가 격리한다.

```mermaid
flowchart LR
    INIT["init Process
(Domain: u:r:init:s0)
[Full Capabilities]"] -->|fork & SetSecurityContext()| TRANS["SELinux Domain Transition
+ CapSet / Seccomp Filter"]
    TRANS -->|Zygote Service| ZYGOTE["Zygote Daemon
(Domain: u:r:zygote:s0)
[CAP_KILL, CAP_SETUID]"]
    TRANS -->|Vendor Daemon| VEND["Vendor Service
(Domain: u:r:hal_foo:s0)
[No Capabilities]"]

    style INIT fill:#f9f,stroke:#333,stroke-width:2px
    style TRANS fill:#bbf,stroke:#333,stroke-width:2px
```

### 코드 및 구체 예시 (Concrete Snippets)

`system/core/init/service.cpp` 보안 및 Capability 설정 로직 구현부:

```cpp
// system/core/init/service.cpp (Security context and capabilities setup before exec)
void Service::Start() {
    pid_t pid = fork();
    if (pid == 0) {
        // 1. Set SELinux Security Context
        if (!seclabel_.empty()) {
            if (setcon(seclabel_.c_str()) < 0) {
                _exit(127);
            }
        }

        // 2. Set Supplementary Groups & User IDs
        if (gid_ != 0 && setgid(gid_) != 0) {
            _exit(127);
        }
        if (uid_ != 0 && setuid(uid_) != 0) {
            _exit(127);
        }

        // 3. Set Ambient POSIX Capabilities
        if (capabilities_) {
            if (!SetCapsAndCombatibleCapabilities(*capabilities_)) {
                _exit(127);
            }
        }

        // 4. Exec Service Binary
        execv(args_[0].c_str(), (char**)args_data);
    }
}
```

`init.rc` 서비스 선언에서 Capability 및 SELinux Domain 지정 예시:

```text
# Explicit capability and security label definition
service netd /system/bin/netd
    class main
    user root
    group root net_admin net_raw
    capabilities NET_ADMIN NET_RAW SYS_MODULE
    seclabel u:r:netd:s0
```

### 관측 가능 증거 (Observable Evidence)

`adb shell`을 통해 현재 구동 중인 서비스들의 SELinux Context 및 Linux Capability를 확인할 수 있다:

```bash
# 프로세스별 SELinux Security Context 조회
adb shell ps -AZ
# 출력 예시:
# u:r:init:s0                     root       1 ... /system/bin/init
# u:r:zygote:s0                   root     650 ... zygote
# u:r:surfaceflinger:s0           system   680 ... surfaceflinger

# 특정 서비스 프로세스의 Capability 허용 상태 확인
adb shell cat /proc/$(adb shell pidof netd)/status | grep -i Cap
```

### 관련 문서

- [service option은 identity, resource, class, socket 계약을 고정한다](service-options-fix-identity-resource-class-and-socket-contracts.md)
- [init service는 재시작 정책을 가진 supervised process다](init-service-is-supervised-process-with-explicit-lifecycle.md)

공식 문서: [SELinux for Android](https://source.android.com/docs/security/features/selinux)
