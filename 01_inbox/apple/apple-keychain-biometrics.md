---
title: apple-keychain-biometrics
tags: [apple, keychain, security, biometrics, touchid, faceid]
aliases: []
date modified: 2025-12-16 17:01:32 +09:00
date created: 2025-12-16 17:01:32 +09:00
---

## Keychain & Biometrics apple keychain security biometrics

Keychain 과 생체 인증. 기본은 [[apple-sandbox-and-security]] 참고.

### Keychain 저장

```swift
import Security

func saveToKeychain(password: String, account: String) -> Bool {
    let data = password.data(using: .utf8)!
    
    let query: [String: Any] = [
        kSecClass as String: kSecClassGenericPassword,
        kSecAttrAccount as String: account,
        kSecValueData as String: data
    ]
    
    SecItemDelete(query as CFDictionary) // 기존 항목 삭제
    
    let status = SecItemAdd(query as CFDictionary, nil)
    return status == errSecSuccess
}
```

### Keychain 조회

```swift
func loadFromKeychain(account: String) -> String? {
    let query: [String: Any] = [
        kSecClass as String: kSecClassGenericPassword,
        kSecAttrAccount as String: account,
        kSecReturnData as String: true,
        kSecMatchLimit as String: kSecMatchLimitOne
    ]
    
    var result: AnyObject?
    let status = SecItemCopyMatching(query as CFDictionary, &result)
    
    guard status == errSecSuccess,
          let data = result as? Data,
          let password = String(data: data, encoding: .utf8) else {
        return nil
    }
    
    return password
}
```

### Touch ID / Face ID

```swift
import LocalAuthentication

func authenticateWithBiometrics(completion: @escaping (Bool, Error?) -> Void) {
    let context = LAContext()
    var error: NSError?
    
    guard context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &error) else {
        completion(false, error)
        return
    }
    
    context.evaluatePolicy(
        .deviceOwnerAuthenticationWithBiometrics,
        localizedReason: "로그인하려면 인증이 필요합니다"
    ) { success, error in
        DispatchQueue.main.async {
            completion(success, error)
        }
    }
}
```

### Keychain + Biometrics

```swift
func saveToBiometricKeychain(password: String, account: String) -> Bool {
    let data = password.data(using: .utf8)!
    
    let access = SecAccessControlCreateWithFlags(
        nil,
        kSecAttrAccessibleWhenUnlockedThisDeviceOnly,
        .biometryCurrentSet,
        nil
    )!
    
    let query: [String: Any] = [
        kSecClass as String: kSecClassGenericPassword,
        kSecAttrAccount as String: account,
        kSecValueData as String: data,
        kSecAttrAccessControl as String: access
    ]
    
    SecItemDelete(query as CFDictionary)
    
    let status = SecItemAdd(query as CFDictionary, nil)
    return status == errSecSuccess
}

func loadFromBiometricKeychain(account: String, completion: @escaping (String?) -> Void) {
    let query: [String: Any] = [
        kSecClass as String: kSecClassGenericPassword,
        kSecAttrAccount as String: account,
        kSecReturnData as String: true,
        kSecUseOperationPrompt as String: "비밀번호를 확인하려면 인증이 필요합니다"
    ]
    
    DispatchQueue.global().async {
        var result: AnyObject?
        let status = SecItemCopyMatching(query as CFDictionary, &result)
        
        DispatchQueue.main.async {
            guard status == errSecSuccess,
                  let data = result as? Data,
                  let password = String(data: data, encoding: .utf8) else {
                completion(nil)
                return
            }
            
            completion(password)
        }
    }
}
```

### 더 보기

[[apple-sandbox-and-security]], [[apple-app-tracking-privacy]], [[common-security/apple-cryptography-and-keychain]]
