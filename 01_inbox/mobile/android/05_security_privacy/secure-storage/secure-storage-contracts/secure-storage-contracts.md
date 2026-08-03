---
title: secure-storage-contracts
tags: ["android", "android/security-privacy"]
aliases: []
date modified: 2026-08-03 17:01:26 +09:00
date created: 2026-07-31 17:04:40 +09:00
---

## 보안 저장소 계약

보안 저장소는 파일 위치만의 문제가 아니다. 민감 데이터 분류, 암호화 키 소유권, 인증 조건, 백업 제외, 키 무효화 처리를 함께 설계해야 한다.

### 정본 노트

- [Android 민감 데이터는 암호화와 키 소유권을 함께 설계한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/sensitive-data-requires-encryption-and-key-ownership.md)
- [Android Keystore 키는 비추출성으로 보호한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/android-keystore-protects-keys-by-non-exportability.md)
- [Android AES-GCM은 IV와 인증 태그를 함께 관리한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/aes-gcm-requires-unique-iv-and-authentication-tag.md)
- [BiometricPrompt는 Keystore 키 사용 권한을 여는 장치다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/biometricprompt-authorizes-keystore-key-use.md)
- [EncryptedSharedPreferences, DataStore, Room의 보안 경계를 구분한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/encrypted-storage-apis-do-not-replace-key-and-data-boundary.md)
- [Android 보안 저장소는 저장 금지와 백업 정책까지 포함한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/secure-storage-policy-includes-what-not-to-store-and-backup.md)

관련 지도: [Android 저장소와 영속성](01_inbox/mobile/android/02_app_framework/data/storage/android-storage-and-persistence.md), [저장소 수명과 백업 경계](01_inbox/mobile/android/05_security_privacy/secure-storage/storage-lifecycle-and-backup/storage-lifecycle-and-backup.md)

공식 문서: [Android Keystore system](https://developer.android.com/privacy-and-security/keystore)
