---
title: SELinux는 domain/type 정책으로 mandatory access control을 강제한다
tags: [android, android/kernel, android/security]
aliases: [SELinux]
date modified: 2026-07-31 23:45:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

SELinux는 Linux discretionary access control(DAC)을 대체하는 것이 아니라, 그 위에 mandatory access control(MAC)을 추가한다. root 권한이나 Linux capability가 있더라도 policy가 허용하지 않은 동작은 차단될 수 있다.

Android SELinux policy는 type enforcement를 중심으로 한다. process label은 domain으로, file/socket/service 같은 object label은 type으로 이해하면 된다. 예를 들어 앱 process는 `untrusted_app` 계열 domain이고 앱 데이터 파일은 `app_data_file` type으로 분리된다.

SELinux는 default deny 모델이다. permissive mode는 denial을 log만 남기고 허용하며, enforcing mode는 log와 차단을 함께 수행한다. Android 5.0 이상에서는 전체 enforcement가 기본 전제다.

정책 작성의 목표는 denial log를 무작정 allow로 바꾸는 것이 아니다. 어떤 domain이 어떤 type/class/permission을 가져야 하는지 최소 권한으로 모델링하고, generic denial이 나오면 서비스 domain이나 label 설계가 잘못됐는지 먼저 본다.

관련 노트: {link(CONTRACTS / "selinux-policy-controls-binder-service-and-file-boundaries.md", "SELinux policy는 Binder service와 file boundary를 함께 제어한다")}, {link(ANDROID / "05_security_privacy/permissions-and-sandbox/android-security-sandbox.md", "Android security sandbox")}

근거: [Security-Enhanced Linux in Android](https://source.android.com/docs/security/features/selinux), [SELinux concepts](https://source.android.com/docs/security/features/selinux/concepts)
