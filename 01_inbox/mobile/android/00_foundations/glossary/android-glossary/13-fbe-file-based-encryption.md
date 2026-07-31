---
title: "FBE"
tags: ["android", "android/glossary"]
aliases: ["File Based Encryption", "Credential Encrypted storage", "Device Encrypted storage"]
---

# FBE

정의: FBE는 파일 단위 encryption domain을 사용해 device encrypted storage와 credential encrypted storage의 사용 가능 시점을 분리하는 Android storage protection model이다.

혼동 방지: FBE를 앱 내부 암호화 라이브러리와 혼동하면 안 된다. Direct Boot 전후에 어떤 data가 열리는지, 그리고 backup/restore와 사용자 unlock lifecycle을 함께 판단해야 한다.

정본 링크:
- [FBE CE/DE storage boundary](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/fbe-ce-and-de-separate-storage-availability.md)
- [Direct Boot storage boundary](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/direct-boot-requires-minimal-device-protected-data.md)
