---
title: mobile-apple-secure-storage
tags: [apple, biometric, faceid, keychain, security]
aliases: [iOS 보안 저장소, 생체인증, 키체인]
date modified: 2026-04-06 18:14:34 +09:00
date created: 2026-04-05 12:45:00 +09:00
---

## [[mobile-security]] > [[mobile-apple-secure-storage]]

### Apple Secure Storage: Keychain & Biometrics

Apple 플랫폼에서 사용자 자격 증명(Tokens, Passwords)과 암호화 키를 하드웨어 수준에서 보호하기 위한 **Keychain Services**와 **LocalAuthentication** 아키텍처 실무 가이드입니다.

---

#### 🛡️ Context: 왜 Keychain & SEP 인가?

iOS 는 앱의 데이터를 물리적으로 암호화하여 저장하지만, **Keychain**은 앱이 삭제되어도 암호화된 상태로 시스템 영역에 유지될 수 있으며, **Secure Enclave(SEP)**는 물리적인 키 추출을 불가능하게 만드는 최후의 방어선입니다.

---

#### 1. iOS Keychain & Secure Enclave 로직

- **Keychain**: 운영체제 수준에서 제공하는 암호화 보관소입니다. (앱 삭제 후에도 데이터가 유지될 수 있음)
- **Secure Enclave (SEP)**: 메인 프로세서와 독립된 하드웨어 보안 모듈로, 암호학적 키 생성 및 생체 데이터 검증을 수행합니다.
- **Data Protection API**: 파일 시스템 계층의 암호화로, 앱 스토리지의 개별 파일에 대해 `FileProtectionType` 을 지정하여 기기 잠금 상태에 따른 접근성을 제어합니다.
- **Passkeys (FIDO2)**: 비밀번호를 대체하는 차세대 인증 표준으로, iCloud Keychain 을 통해 기기 간 동기화되며 생체 인증으로 보호됩니다.

---

#### 2. [Swift] Secure Keychain Wrapper (AES-GCM/RSA)

전문가 수준의 **Keychain** 접근 및 **Secure Enclave** 연동 코드입니다.

##### [Swift] Keychain CRUD 래퍼 예시

```swift
import Foundation
import Security

class KeychainManager {
    static let shared = KeychainManager()
    private let service = "com.production.myapp.security"

    func save(key: String, data: Data) -> OSStatus {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: service,
            kSecAttrAccount as String: key,
            kSecValueData as String: data,
            // 기기가 잠금 해제된 상태에서만 접근 가능하도록 설정
            kSecAttrAccessible as String: kSecAttrAccessibleWhenUnlockedThisDeviceOnly
        ]
        
        SecItemDelete(query as CFDictionary)
        return SecItemAdd(query as CFDictionary, nil)
    }

    func load(key: String) -> Data? {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: service,
            kSecAttrAccount as String: key,
            kSecReturnData as String: true,
            kSecMatchLimit as String: kSecMatchLimitOne
        ]
        
        var dataTypeRef: AnyObject?
        let status = SecItemCopyMatching(query as CFDictionary, &dataTypeRef)
        
        return status == errSecSuccess ? dataTypeRef as? Data : nil
    }
}
```

##### [Swift] Secure Enclave 키 생성 (비공개키가 칩 밖으로 나가지 않음)

```swift
func generateSecureEnclaveKeyPair() throws {
    let accessControl = SecAccessControlCreateWithFlags(
        nil,
        kSecAttrAccessibleWhenUnlockedThisDeviceOnly,
        [.privateKeyUsage, .biometryCurrentSet], // 생체 정보 변경 시 무효화
        nil
    )!
    
    let attributes: [String: Any] = [
        kSecAttrKeyType as String: kSecAttrKeyTypeECSECPrimeRandom,
        kSecAttrKeySizeInBits as String: 256,
        kSecAttrTokenID as String: kSecAttrTokenIDSecureEnclave, // 하드웨어 고립
        kSecPrivateKeyAttrs as String: [
            kSecAttrIsPermanent as String: true,
            kSecAttrAccessControl as String: accessControl
        ]
    ]
    // ... 생략 (키 생성 로직)
}
```

---

#### 3. LocalAuthentication (FaceID / TouchID)

생체 인증을 통해 앱 진입이나 중요 결제를 승인하는 코드입니다.

```swift
import LocalAuthentication

class BioAuthManager {
    func authenticateUser() async -> Bool {
        let context = LAContext()
        var error: NSError?
        
        // 1. 생체 인증 가능 여부 확인
        if context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &error) {
            do {
                // 2. 인증 수행 (UI 팝업)
                let success = try await context.evaluatePolicy(
                    .deviceOwnerAuthenticationWithBiometrics,
                    localizedReason: "보안 결제를 위해 본인 인증이 필요합니다."
                )
                return success
            } catch {
                return false
            }
        }
        return false
    }
}
```

---

#### 🔑 Passkeys & 차세대 인증 (Modern Auth)

iOS 16+ 부터 도입된 **Passkeys**는 피싱 불가능한 자격 증명을 제공합니다.

- **Authentication Services**: `ASAuthorizationController` 를 통해 패스키 생성 및 로그인을 구현합니다.
- **iCloud Keychain Sync**: 사용자가 한 기기에서 생성한 패스키는 동일한 Apple ID 를 사용하는 다른 기기에서도 안전하게 사용 가능합니다.

---

#### 🛡️ 정보보안기사 실무 대응 가이드

1. **Authentication Context 취약점**: 단순히 `evaluatePolicy` 의 `Boolean` 결과만 체크하는 것은 탈옥 기기에서 **Frida 후킹**으로 우회가 가능합니다.
    - **대응**: 생체 인증 성공 시에만 해제되는 **Keychain ACL(Access Control List)**을 연동하여, 인증 성공 후에 실제 데이터(토큰)를 키체인에서 읽어오는 방식으로 구현하십시오.
2. **biometryCurrentSet**: 사용자가 새 지문이나 얼굴을 등록하면 키가 삭제되도록 설정하여 보안성을 강화하십시오.
3. **Data Loss on Backup**: `kSecAttrAccessibleWhenUnlockedThisDeviceOnly` 를 사용하여 iCloud 백업이나 다른 기기로의 복원을 방지하고, 물리적 기기 바인딩을 유지하십시오.

#### 📚 연관 문서 및 가이드

- [[mobile-apple-foundation-security]] - Apple 기초 보안 모델 및 샌드박싱
- [[mobile-vulnerability-check]] - 모바일 취약점 종합 진단 가이드
- [[mobile-advanced-security-tips]] - RASP 및 심화 보안 기술
