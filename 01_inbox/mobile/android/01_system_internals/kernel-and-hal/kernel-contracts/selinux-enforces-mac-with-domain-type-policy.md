---
title: selinux-enforces-mac-with-domain-type-policy
tags: [android, android/kernel, android/security]
aliases: [SELinux]
date modified: 2026-08-03 17:26:12 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

## SELinux 는 domain/type 정책으로 mandatory access control 을 강제한다

SELinux 는 Linux discretionary access control(DAC)을 대체하는 것이 아니라, 그 위에 mandatory access control(MAC)을 추가한다. root 권한이나 Linux capability 가 있더라도 policy 가 허용하지 않은 동작은 차단될 수 있다.

Android SELinux policy 는 type enforcement 를 중심으로 한다. process label 은 domain 으로, file/socket/service 같은 object label 은 type 으로 이해하면 된다. 예를 들어 앱 process 는 `untrusted_app` 계열 domain 이고 앱 데이터 파일은 `app_data_file` type 으로 분리된다.

SELinux 는 default deny 모델이다. permissive mode 는 denial 을 log 만 남기고 허용하며, enforcing mode 는 log 와 차단을 함께 수행한다. Android 5.0 이상에서는 전체 enforcement 가 기본 전제다.

정책 작성의 목표는 denial log 를 무작정 allow 로 바꾸는 것이 아니다. 어떤 domain 이 어떤 type/class/permission 을 가져야 하는지 최소 권한으로 모델링하고, generic denial 이 나오면 서비스 domain 이나 label 설계가 잘못됐는지 먼저 본다.

관련 노트: [SELinux policy는 Binder service와 file boundary를 함께 제어한다](01_inbox/mobile/android/01_system_internals/kernel-and-hal/kernel-contracts/selinux-policy-controls-binder-service-and-file-boundaries.md), [Android app sandbox는 UID와 프로세스 경계로 앱을 격리한다](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/android-app-sandbox-is-uid-and-process-boundary.md)

근거: [Security-Enhanced Linux in Android](https://source.android.com/docs/security/features/selinux), [SELinux concepts](https://source.android.com/docs/security/features/selinux/concepts)
