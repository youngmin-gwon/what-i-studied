---
title: "Android 보안은 UID sandbox, permission, SELinux, verified boot가 나뉜 계층이다"
tags: ["android", "android/foundations"]
---

# Android 보안은 UID sandbox, permission, SELinux, verified boot가 나뉜 계층이다

Android security를 "permission 팝업" 하나로 줄이면 부족하다. 앱 process는 UID와 sandbox로 분리되고, component access는 Manifest/exported/permission으로 제한되며, system process와 파일 접근은 SELinux와 platform policy가 제한한다.

더 아래에는 Verified Boot, dm-verity, rollback protection 같은 boot integrity 계층이 있다. Secure storage와 key management는 다시 data/key ownership 문제다.

따라서 security overview는 각 계층의 한 문장 역할과 정본 링크만 유지하고, 개별 정책은 security/privacy 문서로 보낸다.

관련 노트: [sandbox](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/android-app-sandbox-is-uid-and-process-boundary.md), [permissions](01_inbox/mobile/android/05_security_privacy/permissions-and-sandbox/permission-contracts/permission-contracts.md), [SELinux](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/selinux-enforces-mandatory-policy-beyond-linux-user-permissions.md), [Verified Boot](01_inbox/mobile/android/05_security_privacy/platform-hardening/platform-security-contracts/verified-boot-establishes-device-software-chain-of-trust.md), [secure storage](01_inbox/mobile/android/05_security_privacy/secure-storage/secure-storage-contracts/secure-storage-contracts.md).

## 판단 기준

보안 실패는 먼저 caller UID/process, component 노출과 permission, AppOps/runtime 정책, SELinux platform policy, boot/data integrity 중 어느 계층이 거절했는지 분류한다.

## 경계

permission grant만으로 SELinux나 AppOps 거절을 설명하지 않는다. 이 노트는 계층 분류만 제공하고 정책별 적용 조건은 security/privacy 정본이 소유한다.
