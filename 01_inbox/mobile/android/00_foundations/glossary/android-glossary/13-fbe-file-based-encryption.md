---
title: "FBE는 기기의 개별 파일을 서로 다른 키로 암호화하는 파일 기반 보안 방식이다"
tags: ["android", "android/glossary"]
aliases: ["Credential Encrypted storage", "Device Encrypted storage", "File Based Encryption"]
date modified: 2026-08-03 16:25:49 +09:00
date created: 2026-07-31 15:29:55 +09:00
---

# FBE는 기기의 개별 파일을 서로 다른 키로 암호화하는 파일 기반 보안 방식이다

정의: FBE 는 파일 단위 encryption domain 을 사용해 device encrypted storage 와 credential encrypted storage 의 사용 가능 시점을 분리하는 Android storage protection model 이다.

혼동 방지: FBE 를 앱 내부 암호화 라이브러리와 혼동하면 안 된다. Direct Boot 전후에 어떤 data 가 열리는지, 그리고 backup/restore 와 사용자 unlock lifecycle 을 함께 판단해야 한다.

정본 링크:

- [FBE CE/DE storage boundary](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/fbe-ce-and-de-separate-storage-availability.md)
- [Direct Boot storage boundary](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/direct-boot-requires-minimal-device-protected-data.md)
