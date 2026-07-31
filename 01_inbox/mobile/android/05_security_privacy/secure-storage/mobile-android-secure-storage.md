# Mobile Android Secure Storage

이 문서는 Android Secure Storage 구현 가이드의 진입점이다. 구현 세부 설명은 보안 저장소 계약 정본으로 흡수했다.

## 정본

- [보안 저장소 계약](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/secure-storage-contracts.md)
- [Android 민감 데이터는 암호화와 키 소유권을 함께 설계한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/sensitive-data-requires-encryption-and-key-ownership.md)
- [Android Keystore 키는 비추출성으로 보호한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/android-keystore-protects-keys-by-non-exportability.md)
- [Android AES-GCM은 IV와 인증 태그를 함께 관리한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/aes-gcm-requires-unique-iv-and-authentication-tag.md)
- [BiometricPrompt는 Keystore 키 사용 권한을 여는 장치다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/biometricprompt-authorizes-keystore-key-use.md)
- [Android 보안 저장소는 저장 금지와 백업 정책까지 포함한다](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/secure-storage-policy-includes-what-not-to-store-and-backup.md)
