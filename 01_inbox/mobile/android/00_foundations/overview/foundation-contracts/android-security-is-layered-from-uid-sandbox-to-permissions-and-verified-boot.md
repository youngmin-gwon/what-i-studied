# Android 보안은 UID sandbox, permission, SELinux, verified boot가 나뉜 계층이다

Android security를 "permission 팝업" 하나로 줄이면 부족하다. 앱 process는 UID와 sandbox로 분리되고, component access는 Manifest/exported/permission으로 제한되며, system process와 파일 접근은 SELinux와 platform policy가 제한한다.

더 아래에는 Verified Boot, dm-verity, rollback protection 같은 boot integrity 계층이 있다. Secure storage와 key management는 다시 data/key ownership 문제다.

따라서 security overview는 각 계층의 한 문장 역할과 정본 링크만 유지하고, 개별 정책은 security/privacy 문서로 보낸다.

관련 노트: [sandbox](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/android-security-sandbox.md), [permissions](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/android-security-permissions.md), [SELinux](01_inbox/mobile/android/05_security_privacy/platform-hardening/android-security-selinux.md), [Verified Boot](01_inbox/mobile/android/05_security_privacy/integrity-and-attestation/android-security-verified-boot.md), [secure storage](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/secure-storage-contracts.md).
