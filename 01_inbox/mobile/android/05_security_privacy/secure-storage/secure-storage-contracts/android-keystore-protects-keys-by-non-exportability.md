---
title: android-keystore-protects-keys-by-non-exportability
tags: ["android", "android/security-privacy"]
aliases: ["Android Keystore 는 추출 불가능성으로 키를 보호한다"]
date modified: 2026-08-06 14:48:27 +09:00
date created: 2026-07-31 17:04:40 +09:00
---

## Android Keystore 는 추출 불가능성으로 키를 보호한다

Android Keystore 시스템의 핵심 가치는 앱이 키 재료를 직접 내보내지 않고 시스템이 키 사용 목적과 인증 조건을 집행한다는 데 있다. Android Keystore 키의 원본 바이트는 앱 프로세스로 반환되지 않는다. 다만 모든 키가 TEE 또는 StrongBox에 저장되는 것은 아니다. 알고리즘·기기 지원에 따라 소프트웨어 보안 수준일 수 있으므로 하드웨어 격리가 요구사항이면 `KeyInfo.getSecurityLevel()` 또는 원격 key attestation으로 확인한다. 공개 `SecretKey` API에 추출 가능 여부를 확인하는 판별 메서드는 없다.

```mermaid
flowchart LR
    subgraph AppProcess [Android App Linux Process]
        AppCode[Cipher.init / Cipher.doFinal]
        KeyRef[KeyStore Key Handle / Alias Reference]
    end

    subgraph SystemBoundary [Android Keystore Provider / keystore2]
        KeystoreDaemon[System crypto operation]
        KeyMaterial[Non-exportable key material]
        CryptoEngine[Software, TEE, or StrongBox backend]
    end

    AppCode -->|[binder ipc](../../../01_system_internals/binder-ipc.md) Request with Key Alias| KeystoreDaemon
    KeystoreDaemon --> CryptoEngine
    KeyMaterial -. Not returned to app .-> AppProcess
    CryptoEngine -->|Result Ciphertext / Plaintext| AppCode
```

### 내부 동작 메커니즘

1. **TEE vs StrongBox**:
   - **TEE (Trusted Execution Environment)**: 메인 CPU(ARM TrustZone 등) 내 물리적으로 분리된 보안 OS 환경. **Keymaster / KeyMint** HAL 인터페이스를 통해 암호화 연산을 수행한다.
   - **StrongBox (Secure Element)**: 전용 고립 하드웨어 보안 모듈(HSM). 자체 CPU, 보안 스토리지, 무작위 수 생성기(TRNG) 및 변조 방지(Tamper-resistant) 칩셋을 지닌 독립 하드웨어로 최고 수준의 물리적 비추출성을 제공한다.
2. **보안 수준 확인**: `KeyGenParameterSpec`으로 Android Keystore 키를 생성했다고 해서 자동으로 hardware-backed가 되는 것은 아니다. API 29+에서는 `KeyInfo.getSecurityLevel()`이 `TRUSTED_ENVIRONMENT` 또는 `STRONGBOX`인지 확인한다. API 28 이하에서는 `isInsideSecureHardware()`를 사용할 수 있다. 루팅 기기까지 포함한 공격 저항성을 앱 코드만으로 절대 보장하지 않는다.
3. **Key Invalidated on New Biometrics**: `setInvalidatedByBiometricEnrollment(true)` 속성을 부여하면 새로운 손가락 생체 정보가 기기에 추가 등록되는 순간 하드웨어에 의해 기존 키가 영구 무효화된다.
4. **Initialization Vector (IV) Unique Constraint**: AES-GCM 암호화 시 IV(Initialization Vector) 재사용은 보안 파괴 위험이 있으므로 `setRandomizedEncryptionRequired(true)`를 통해 매 암호화 시 무작위 IV 생성을 보장해야 한다.

### Hardware-Backed Keystore AES 키 생성 구현 (Kotlin)

```kotlin
import android.security.keystore.KeyGenParameterSpec
import android.security.keystore.KeyProperties
import java.security.KeyStore
import javax.crypto.KeyGenerator
import javax.crypto.SecretKey

fun getOrCreateMasterKey(keyAlias: String): SecretKey {
    val keyStore = KeyStore.getInstance("AndroidKeyStore").apply { load(null) }
    
    if (keyStore.containsAlias(keyAlias)) {
        val entry = keyStore.getEntry(keyAlias, null) as KeyStore.SecretKeyEntry
        return entry.secretKey
    }

    val keyGenerator = KeyGenerator.getInstance(
        KeyProperties.KEY_ALGORITHM_AES, 
        "AndroidKeyStore"
    )
    
    val spec = KeyGenParameterSpec.Builder(
        keyAlias,
        KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT
    )
        .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
        .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
        .setKeySize(256)
        .setUserAuthenticationRequired(false) // 필요 시 true 지정
        .setRandomizedEncryptionRequired(true)
        .build()

    keyGenerator.init(spec)
    return keyGenerator.generateKey()
}
```

StrongBox가 정책상 필요하면 먼저 `PackageManager.FEATURE_STRONGBOX_KEYSTORE`를 확인하고 `setIsStrongBoxBacked(true)`로 생성한다. 그래도 요청한 키 구성을 StrongBox가 지원하지 않으면 `StrongBoxUnavailableException`이 발생할 수 있으므로, 정책에 따라 실패시키거나 TEE 키로 명시적으로 재생성한다. 조용히 보안 수준을 낮추지 않는다.

### 관찰 가능한 증거 (Observable Evidence)

- **adb dumpsys를 통한 Keystore2 서비스 덤프 확인**:
  ```bash
  adb shell dumpsys keystore2
  ```
- **생체정보 추가 등록 후 무효화된 키 사용 시 예외**:
  ```text
  android.security.keystore.KeyPermanentlyInvalidatedException: Key permanently invalidated
      at android.security.keystore2.AndroidKeyStoreCipherSpiBase.ensureKeystoreOperationInitialized
  ```

### 판단 기준

Secure storage 노트는 키 소유권(Key Ownership), 인증 암호화(AEAD), 생체 인증 바인딩, 백업 제외 설계가 서로 다른 방어선임을 구분하는 기준으로 읽는다.

### 경계

암호화 라이브러리 적용 자체를 안전 보장으로 오해하지 않고, 키 수명주기와 데이터 백업 경계를 별도로 설계한다.

상위 문서: [보안 저장소 계약](secure-storage-contracts.md)

관련 노트: [BiometricPrompt는 Keystore 키 사용을 인가한다](biometricprompt-authorizes-keystore-key-use.md), [AES-GCM은 고유한 IV와 Authentication Tag를 요구한다](aes-gcm-requires-unique-iv-and-authentication-tag.md)

### 공식 문서

- https://developer.android.com/privacy-and-security/keystore
- https://developer.android.com/privacy-and-security/security-key-attestation

검증일: 2026-08-06. Android Keystore의 비추출성과 hardware-backed 보장은 별개이며 `KeyInfo.securityLevel`로 확인해야 한다는 공식 계약을 반영했다.
