---
title: apple-keychain-and-biometrics
tags: [apple, security, keychain, biometric, faceid]
aliases: [iOS 보안 저장소, 키체인, 생체인증]
date created: 2026-04-05 12:45:00 +09:00
---

## Apple Keychain & Biometrics (Secure Storage)

Apple 기기에서 사용자 비밀번호, 신속 로그인 토큰, 개인키 등을 안전하게 저장하기 위한 **Keychain Services**와 **LocalAuthentication** 연동 실무를 다룹니다.

---

### 1. iOS Keychain & Secure Enclave 로직

- **Keychain**: 운영체제 수준에서 제공하는 암호화 보관소입니다. (앱 삭제 후에도 데이터가 유지될 수 있음)
- **Secure Enclave (SEP)**: 메인 프로세서와 독립된 하드웨어 보안 모듈로, 암호화 키 생성 및 생체 데이터 검증을 수행합니다.
- **Data Protection**: 파일 시스템 암호화와 연동되어 기기가 잠겨 있을 때 데이터 가독성을 제어합니다.

---

### 2. [Swift] Secure Keychain Wrapper (AES-GCM/RSA)

전문가 수준의 **Keychain** 접근 및 **Secure Enclave** 연동 코드입니다.

#### [Swift] Keychain CRUD 래퍼 예시

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

#### [Swift] Secure Enclave 키 생성 (비공개키가 칩 밖으로 나가지 않음)

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

### 3. LocalAuthentication (FaceID / TouchID)

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

### 🛡️ 정보보안기사 실무 대응 가이드

1. **Authentication Context 취약점**: 단순히 `evaluatePolicy`의 `Boolean` 결과만 체크하는 것은 탈옥 기기에서 **Frida 후킹**으로 우회가 가능합니다.
    - **대응**: 생체 인증 성공 시에만 해제되는 **Keychain ACL(Access Control List)**을 연동하여, 인증 성공 후에 실제 데이터(토큰)를 키체인에서 읽어오는 방식으로 구현하십시오.
2. **biometryCurrentSet**: 사용자가 새 지문이나 얼굴을 등록하면 키가 삭제되도록 설정하여 보안성을 강화하십시오.
3. **Data Loss on Backup**: `kSecAttrAccessibleWhenUnlockedThisDeviceOnly`를 사용하여 iCloud 백업이나 다른 기기로의 복원을 방지하고, 물리적 기기 바인딩을 유지하십시오.

### 📚 연결 문서
- [apple-sandbox-and-security](apple-sandbox-and-security.md) - 애플 기초 보안 모델
- [cross-platform-mobile-vulnerability-check](../../cross-platform-mobile-vulnerability-check.md) - 모바일 취약점 종합 진단
