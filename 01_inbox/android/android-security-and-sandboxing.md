---
title: android-security-and-sandboxing
tags: [android, android/sandbox, android/security]
aliases: []
date modified: 2025-12-16 15:50:26 +09:00
date created: 2025-12-16 15:24:27 +09:00
---

## Security & Sandboxing android android/security android/sandbox

[[android-architecture-stack]] · [[android-hal-and-kernel]] · [[android-binder-and-ipc]]

### 보안 모델 핵심

Linux UID/GID 격리 + SELinux domain + 앱 서명/퍼미션이 삼각 구도를 이룸.

각 앱은 독립 UID 로 실행, /data/user/0/<pkg> private dir. sharedUserId 는 점차 폐지.

서명은 업데이트 검증, signature-level permission 부여, key rotation 지원.

### SELinux
- sepolicy 는 domain(type) 과 allow 규칙으로 access 제어. system_server, app, isolated_app 등 도메인 별 정책.
- neverallow 규칙으로 금지선 설정. `audit2allow` 는 개발 보조로만 사용.
- binder_call/binder_transfer 규칙으로 IPC 제어. file/socket/netlink/ptrace 모두 policy 대상.

### Permission & AppOps
- Permission 보호 레벨: normal, dangerous(runtime), signature, privileged, internal.
- AppOps 는 퍼미션보다 세밀한 실행 시점 정책; user/context/state 기반 모드 (allow/deny/ignore/foreground). Notification access, clipboard access 등.
- Background location, camera/mic indicators/privacy dashboard, approximate location, photo picker 로 개인정보 보호 강화.

### 샌드박스와 프로세스 격리
- UID 격리 + SELinux + mount namespace + seccomp filter 로 다중 샌드박스.
- IsolatedProcess/ExternalService: 별도 UID/permissions 없이 실행, 무해화된 샌드박스.
- WebView/Renderers: site isolation, sandboxed renderers; GPU process separation.

### 파일/저장소 보안
- Scoped storage: 앱별 external storage sandbox + MediaStore API + Storage Access Framework. `MANAGE_EXTERNAL_STORAGE` 는 제한적.
- File-based encryption(FBE): user credential dependent 디렉터리, direct boot 영역 (`/data/user_de`).
- fs-verity: 개별 파일 무결성, Play Protect integrity.
- keystore-backed file encryption, synthetic password framework(SPF) 로 credential 분리.
- Backup/restore 시 키 핸들링: Auto Backup 예외 목록, KeyChain/Keystore key non-exportable.

### 네트워크/통신 보안
- TLS by default(Conscrypt/BoringSSL). Network Security Config 로 cleartext opt-in, pinning.
- VPN/Work profile 별 네트워크 격리. Private DNS(DoT) 강제 설정 가능.
- BLE/Wi-Fi/Location 권한 분리. Nearby/advertising 제한.
- SAF/ContentProvider URI permissions 로 공유 제어. ClipData/drag-and-drop 역시 URI permission 을 동반.\n
- WebRTC/VoIP 는 권한 +network security config 검토. TURN/STUN 서버 주소 보호, ICE candidate redaction.
- Bluetooth LE pairing/bonding 모드, Just Works vs Passkey, out-of-band credential. Nearby share key rotations.\n

### 실행 시 보호
- SafetyNet → Play Integrity API: device integrity, CTS profile, licensing. Integrity verdict 기반 기능 제한.
- Verified Boot: boot chain signature, rollback index/fuse. AVB 2.0 with vbmeta chaining.
- SELinux + seccomp + hardened malloc(optional), control flow integrity(CFI) native.
- TEE/StrongBox 사용으로 key material 보호. Gatekeeper/Weaver 로 retry 제한과 anti-hammering.\n

### 시스템 서비스 하드닝
- system_server privilege reduction: 서비스별 separate process 로 이동 (Media, keystore, statsd).
- keystore2: StrongBox/TEE integration, KeyMint HAL. Auth-bound keys, biometrics(HAL + HAT tokens).
- permission controller mainline module: runtime permission UI/logic 분리.

### 진화와 전환
- Device admin → Android Enterprise(Device Policy Manager/Work Profile) 보안 모델 변화.
- Legacy storage permissions → scoped storage + MediaStore. background start limits 로 악성 알림 스팸 차단.
- WebView multi-process, site isolation rollout.

### 개발자 주의사항
- PendingIntent 는 FLAG_IMMUTABLE 기본, mutable 필요 시 최소 범위만 허용.
- Exported components 는 명시적 intent filter/permission 설정. deep link/filter 악용 주의.
- Clipboard/privacy indicator/logging redaction, `android:allowBackup`/`fullBackupContent` 설정 검토.
- WebView 프로세스 격리, safe browsing, file:// exposure 차단. intent scheme URL 처리 시 allowlist 필요.
- debugging builds 는 android:debuggable=true → attack surface 증가, network security config relaxed 모드 금지.

### 링크
- [[android-activity-manager-and-system-services]]: background 제한과 보안 정책 교차.
- [[android-adb-and-images]]: adb root/debuggable build 차이, secure adb.
- [[android-evolution-history]]: 주요 보안 정책 변화.
