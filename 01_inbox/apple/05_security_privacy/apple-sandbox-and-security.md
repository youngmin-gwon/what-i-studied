---
title: apple-sandbox-and-security
tags: [apple, ats, entitlement, mac, sandbox, security, tcc]
aliases: []
date modified: 2026-04-03 18:55:58 +09:00
date created: 2025-12-16 16:08:41 +09:00
---

## Sandbox & Security Deep Dive

"왜 내 앱은 옆 앱의 파일을 못 볼까?"

Apple 플랫폼 보안의 핵심은 **"기본 거부(Deny by Default)"**입니다.

이 철학을 이해하지 못하면, 앱 개발 내내 권한 문제로 고통받게 됩니다.

### 💡 왜 이것을 알아야 하나요? (Context)
- **Deny by Default**: 아무리 `FileHandle` 을 열어도 에러가 난다면, 코드가 잘못된 게 아닙니다. 샌드박스가 막고 있는 것입니다. 권한(Entitlement)을 요청하지 않으면 아무것도 할 수 없습니다.
- **앱 심사 거절 1 순위**: "사용자가 선택하지 않은 파일에 접근해선 안 된다"는 규칙을 어기면 심사에서 바로 떨어집니다.
- **사고 예방**: 만약 내 앱이 뚫려도, 해커는 내 앱의 샌드박스 밖으로 나갈 수 없습니다. 이것이 iOS 가 안전한 이유입니다.

---

### 🛡️ Mandatory Access Control (MAC)

리눅스와 달리, Apple 의 보안 모델은 **강제적 접근 제어(MAC)**를 따릅니다.

사용자(User)가 허락해도, 시스템 정책(Kernel)이 거부하면 끝입니다.

1. **Sandbox Profile**: 앱이 실행될 때 커널은 해당 앱이 할 수 있는 일(네트워크 연결, 파일 쓰기 등)이 적힌 프로필을 로드합니다.
2. **System Call Hook**: 앱이 `open()`, `connect()` 같은 시스템 콜을 호출하면, TrustedBSD MAC 프레임워크가 이를 가로채서 프로필과 대조합니다.
3. **Hardened Runtime (macOS/iOS 26+)**: 프로세스 인젝션, 코드 서명되지 않은 라이브러리 로드 등을 커널 수준에서 차단하는 강화된 실행 환경입니다. `Library Validation`을 통해 Apple 이나 개발자 본인이 서명한 라이브러리만 로드하도록 강제할 수 있습니다.
4. **Check**: 프로필에 허용되지 않은 동작이면 `EPERM` (Operation not permitted) 에러를 뱉고 로그를 남깁니다. (Console.app 에서 확인 가능)

---

### 🎟️ Code Signing & Entitlements

"이 앱이 해도 되는 일"을 증명하는 티켓입니다.

#### 1. Code Signing (서명)

앱이 변조되지 않았음(Integrity)을 보장합니다.

- 해커가 바이너리를 수정하면 서명이 깨지고, iOS 는 실행을 거부합니다.

#### 2. Entitlements (권한 부여)

앱의 주민등록증 뒤에 붙은 "특수 면허" 스티커입니다.

- **Push Notification**, **iCloud**, **Apple Pay** 등 시스템 리소스를 쓰려면 Apple 이 발급한 `Provisioning Profile` 에 해당 Entitlement 가 명시되어 있어야 합니다.
- **주의**: Xcode 타겟 설정(`Capabilities`)에서 켜지 않으면 API 호출 시 런타임 에러가 발생합니다.

---

### 앱 검증 & 무결성 (App Attest)

Apple 은 앱의 변조 여부를 확인하기 위해 **DeviceCheck** 프레임워크의 **App Attest** 서비스를 제공합니다. 이는 실제 기기에서 실행 중인 앱임을 하드웨어적으로 증명합니다.

#### [Swift] Production-ready App Attest 구현

```swift
import DeviceCheck
import CryptoKit

class SecurityAttestationClient {
    let service = DCAppAttestService.shared
    
    func performAttestation(challenge: Data) async throws -> (keyId: String, attestation: Data) {
        // 1. App Attest 지원 여부 확인 (시뮬레이터 불가)
        guard service.isSupported else { throw SecurityError.notSupported }
        
        // 2. 새로운 키 쌍 생성 (Secure Enclave 내부)
        let keyId = try await service.generateKey()
        
        // 3. 서버에서 받은 Challenge(nonce) 해싱
        let clientDataHash = Data(SHA256.hash(data: challenge))
        
        // 4. Attestation Object 요청
        let attestation = try await service.attestKey(keyId, clientDataHash: clientDataHash)
        
        return (keyId, attestation)
    }
    
    // 이후 중요한 요청 시 'Assertion'을 생성하여 서버로 전송
    func generateAssertion(keyId: String, clientData: Data) async throws -> Data {
        let clientDataHash = Data(SHA256.hash(data: clientData))
        return try await service.generateAssertion(keyId, clientDataHash: clientDataHash)
    }
}
```

> [!IMPORTANT] **서버 측 검증 로직**
> 서버는 Apple 의 **App Attest Root CA**를 통해 인증서 체인을 검증하고, `clientDataHash`가 보낸 `nonce`와 일치하는지, `appID`가 내 앱인지 확인해야 합니다. 한 번 검증된 `keyId`는 서버 DB에 저장하여 이후의 `Assertion` 검증 시 공개키로 활용합니다.

---

### 🌐 Network Security (ATS)

#### 1. App Transport Security (ATS)

iOS 는 기본적으로 모든 HTTP 연결을 차단하고, **HTTPS (TLS 1.2+)**만 허용합니다.

- Info.plist 에서 `NSAppTransportSecurity` 예외를 추가할 수 있지만, 심사 시 타당한 이유("서버가 내 것이 아님" 등)를 설명해야 합니다.

#### 2. Network Extensions

VPN, DNS Proxy, Content Filter 같은 기능을 구현하려면 단순 서명을 넘어선 **Network Extension Entitlement**가 필요합니다. 이는 Apple 의 추가 승인(Allowlist)이 필요할 수 있습니다.

---

### 🖼️ Photo & File Access (Modern Privacy)

#### 1. Limited Photo Library

iOS 14+ 부터 사용자는 "사진 전체 접근" 대신 **"선택한 사진만 접근(Selected Photos)"**을 고를 수 있습니다.

- 개발자는 `PHPickerViewController` 를 써야 합니다.
- **장점**: 권한 팝업 없이도 사용자가 고른 사진을 바로 가져올 수 있습니다. (System-presents UI 는 신뢰할 수 있으니까요)

#### 2. Security Scoped Bookmark (macOS/iPadOS)

사용자가 파일을 골라줬어도, 앱을 껐다 켜면 권한이 사라집니다(Sandboxed).

- 파일 URL 을 그냥 저장하면 안 되고, **BookmarkData**로 변환하여 영구 권한을 저장해야 합니다.
- 파일에 접근할 때마다 `startAccessingSecurityScopedResource()` 를 호출해야 합니다.

```swift
// 파일 접근권 획득
if url.startAccessingSecurityScopedResource() {
    defer { url.stopAccessingSecurityScopedResource() }
    // 파일 읽기/쓰기 수행
}
```

### 🚨 보안 진단 및 방어 (Security Engineering)

정보보안 전문가 관점의 iOS 앱 진단 포인트와 방어 전략입니다.

#### 1. Frida를 이용한 iOS 후킹
- **진단**: 탈옥(Jailbreak) 기기 또는 사이드로드된 앱에 Frida 를 연결하여 `CommonCrypto` 함수를 후킹, 암호화 키를 가로챕니다.
- **방어 (Anti-Jailbreak)**: 
    - `/Applications/Cydia.app`, `/bin/bash` 등의 파일 경로 존재 여부를 체크하되, **Frida 의 `Interceptor`가 `NSFileManager`를 후킹할 수 있음을 인지**해야 합니다.
    - 따라서 **C 언어 수준의 `stat` 함수**를 사용하여 `svc` (System Call) 명령어로 직접 호출하는 것이 더 안전합니다.

#### 2. 진단 툴 대응 (Anti-Debugging)
- **ptrace(PT_DENY_ATTACH)**: 디버거(LLDB 등)가 프로세스에 붙지 못하도록 차단합니다. (Main 함수 진입점 근처에서 호출)

---

### ⚖️ 보안 법규 및 컴플라이언스 (Compliance)

**개인정보 보호법** 준수를 위한 iOS 개발 가이드라인입니다.

1. **Info.plist 목적 설명 (Purpose String)**: 
    - 카메라, 위치, 연락처 접근 시 사용 이유를 **구체적**으로 적어야 합니다. (성실하지 않은 설명은 심사 거절 사유)
2. **개인정보 처리방침 게시**: 앱 내부와 App Store Connect 에 반드시 최신 정책 링크를 포함해야 합니다.
3. **App Tracking Transparency (ATT)**: 광고 식별자(`IDFA`)를 수집할 경우 반드시 `AppTrackingTransparency` 프레임워크를 통해 사용자 동의를 얻어야 합니다.

### 더 보기
- [apple-keychain-biometrics](apple-keychain-biometrics.md) - 비밀번호와 생체 정보 보호
- [apple-build-and-distribution](apple-build-and-distribution.md) - 서명과 배포 프로세스
