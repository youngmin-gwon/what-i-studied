---
title: "init 보안은 SELinux domain과 capability 경계로 정의된다"
tags: [android, android/system-internals, android/boot-runtime, android/init]
aliases: ["init 보안은 SELinux domain과 capability 경계로 정의된다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# init 보안은 SELinux domain과 capability 경계로 정의된다

상위 문서: [init와 네이티브 서비스 계약](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/init-service-contracts.md)

init service를 root로 실행하는 것은 보안 설계가 아니다. Android native service는 UID/GID, SELinux domain, executable label, Linux capability, property context를 조합해 필요한 권한만 가져야 한다.

## 실무 규칙

- service binary에는 적절한 file context와 entrypoint 정책이 필요하다.
- `seclabel`을 임시 회피 수단으로 쓰지 말고 서비스별 domain을 정의한다.
- `capabilities`는 root 권한 전체를 대체하기 위한 최소 권한 목록으로 본다.
- property write 권한은 property context와 domain allow rule을 함께 검토한다.
- vendor service는 system service와 stable interface 경계를 넘지 않게 둔다.

## 관련 문서

- [ueventd는 kernel uevent를 dev node 권한으로 변환한다](01_inbox/mobile/android/01_system_internals/boot-and-runtime/init-service-contracts/ueventd-turns-kernel-uevents-into-dev-node-permissions.md)
- [Android app sandbox는 UID와 프로세스 경계로 앱을 격리한다](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/android-app-sandbox-is-uid-and-process-boundary.md)
