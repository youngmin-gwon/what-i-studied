---
title: apple-security-app-attest
tags: [app-attest, apple, apple/security, devicecheck]
aliases: []
date modified: 2026-04-05 17:45:27 +09:00
date created: 2026-04-05 17:07:59 +09:00
---

## [[mobile-security]] > [[apple-security-app-attest]]

### App Attest & DeviceCheck

앱의 변조 여부를 확인하고, 실제 기기에서 실행 중인 합법적인 앱임을 서버 측에서 검증하는 메커니즘입니다.

---

#### 🛡️ App Attest (DeviceCheck Framework)

Apple 은 앱의 무결성을 증명하기 위해 하드웨어 기반의 증명을 제공합니다.

- **Key Generation**: `DCAppAttestService` 를 통해 Secure Enclave 내부에 키 쌍을 생성합니다.
- **Attestation**: 서버에서 보낸 `challenge`(nonce)와 앱 식별자를 결합하여 Apple 측에 증명을 요청합니다.
- **Assertion**: 서버에 중요한 요청을 보낼 때마다 이 키로 디지털 서명을 생성하여 전송합니다.

```swift
import DeviceCheck
import CryptoKit

class SecurityAttestationClient {
    let service = DCAppAttestService.shared
    
    func performAttestation(challenge: Data) async throws -> (keyId: String, attestation: Data) {
        guard service.isSupported else { throw SecurityError.notSupported }
        let keyId = try await service.generateKey()
        let clientDataHash = Data(SHA256.hash(data: challenge))
        let attestation = try await service.attestKey(keyId, clientDataHash: clientDataHash)
        return (keyId, attestation)
    }
}
```

---

#### 🌐 서버 측 검증 로직

서버는 단순히 데이터를 받는 것이 아니라 Apple 의 **App Attest Root CA**를 통해 다음을 검증해야 합니다.

1. **인증서 체인**: Apple 이 발급한 인증서인지 확인합니다.
2. **Nonce 일리성**: 서버가 보낸 `challenge` 와 일치하는지 확인하여 Replay 공격을 방지합니다.
3. **App ID**: 데이터가 내 앱 내에서 생성되었는지 확인합니다.

>[!IMPORTANT]
>App Attest 는 탈옥(Jailbreak) 기기에서는 동작하지 않거나 부정확한 결과를 반환할 수 있으므로, 서버 측 로직에서 이를 고려해야 합니다.

#### 연관 문서
- [[apple-security-entitlements]] - 권한 증명
- [[apple-security-tcc-compliance]] - 프라이버시 법규
- [[mobile-vulnerability-check]] - 앱 무결성 진단
