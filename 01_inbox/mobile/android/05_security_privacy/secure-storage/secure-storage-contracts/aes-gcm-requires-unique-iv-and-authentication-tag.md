---
title: aes-gcm-requires-unique-iv-and-authentication-tag
tags: ["android", "android/security-privacy"]
aliases: ["AES-GCM 은 고유한 IV 와 Authentication Tag 를 요구한다"]
date modified: 2026-08-04 22:00:00 +09:00
date created: 2026-07-31 17:04:40 +09:00
---

## AES-GCM 은 고유한 IV 와 Authentication Tag 를 요구한다

AES-GCM(Galois/Counter Mode)은 데이터의 암호화(Confidentiality)와 무결성/인증(Integrity & Authentication)을 동시에 제공하는 **AEAD(Authenticated Encryption with Associated Data)** 방식이다. AES-GCM을 안전하게 사용하기 위해서는 **매 암호화 연산마다 무조건 12-byte의 고유한 난수 IV(Initialization Vector)**를 사용해야 하며, 복호화 시 검증할 **128-bit Authentication Tag**를 암호문과 함께 보관해야 한다.

```mermaid
flowchart TD
    subgraph Encrypt Process
        PT[Plaintext] + Key[Keystore AES Key] + IV12[Random 12-byte IV] --> CipherEngine[AES/GCM/NoPadding Cipher]
        CipherEngine --> Output[Ciphertext + 16-byte Auth Tag]
    end

    subgraph Decrypt Process
        Input[Ciphertext + Auth Tag] + Key + IV12 --> DecEngine[AES/GCM Decrypt & GHASH Tag Check]
        DecEngine -- Tag Match --> PlaintextOutput[Plaintext 복원]
        DecEngine -- Tag Mismatch / Tampered --> Exception[Throw AEADBadTagException: Tamper Detected!]
    end
```

### 내부 동작 메커니즘

1. **Catastrophic IV Reuse Attack**: 동일한 키로 IV를 재사용하면 엑스오르(XOR) 키스트림이 일치하여 공격자가 두 암호문의 차이로부터 평문을 쉽게 복원할 수 있으며 GHASH 키가 노출되어 인증 태그 위조가 가능해진다.
2. **IV Standard Length**: AES-GCM의 표준 IV 길이는 **12-byte (96-bit)**이다. 16-byte IV 사용 시 내부적으로 추가적인 GHASH 연산이 수행되어 성능 저하 및 보안 이슈를 유발할 수 있다.
3. **Authentication Tag Verification**: GCM 모드는 복호화 연산 마지막에 GHASH 계산 결과와 저장된 Tag(16-byte)를 비교한다. 단 1비트라도 위조된 경우 복호화를 즉시 중단하고 예외를 던진다.

### 안드로이드 안전한 AES-GCM 암호화/복호화 구현 예시 (Kotlin)

```kotlin
import javax.crypto.Cipher
import javax.crypto.SecretKey
import javax.crypto.spec.GCMParameterSpec
import java.security.SecureRandom

object AesGcmCipherHelper {
    private const val TRANSFORMATION = "AES/GCM/NoPadding"
    private const val GCM_TAG_LENGTH_BITS = 128
    private const val IV_LENGTH_BYTES = 12

    fun encrypt(plainText: ByteArray, secretKey: SecretKey): ByteArray {
        val iv = ByteArray(IV_LENGTH_BYTES).apply {
            SecureRandom().nextBytes(this)
        }
        val cipher = Cipher.getInstance(TRANSFORMATION)
        val spec = GCMParameterSpec(GCM_TAG_LENGTH_BITS, iv)
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, spec)

        val cipherTextWithTag = cipher.doFinal(plainText)
        
        // [12-byte IV] + [Ciphertext + AuthTag] 형태로 결합 보관
        return iv + cipherTextWithTag
    }

    fun decrypt(encryptedPayload: ByteArray, secretKey: SecretKey): ByteArray {
        require(encryptedPayload.size > IV_LENGTH_BYTES + 16) { "Invalid payload length" }
        
        val iv = encryptedPayload.copyOfRange(0, IV_LENGTH_BYTES)
        val cipherTextWithTag = encryptedPayload.copyOfRange(IV_LENGTH_BYTES, encryptedPayload.size)

        val cipher = Cipher.getInstance(TRANSFORMATION)
        val spec = GCMParameterSpec(GCM_TAG_LENGTH_BITS, iv)
        cipher.init(Cipher.DECRYPT_MODE, secretKey, spec)

        return cipher.doFinal(cipherTextWithTag) // 위조 시 AEADBadTagException 발생
    }
}
```

### 관찰 가능한 증거 (Observable Evidence)

- **adb를 활용한 암호화 파일 바이너리 구조 확인**:
  ```bash
  adb shell xxd /data/data/com.example.app/files/encrypted_payload.bin
  ```

- **암호문 위조 시 발생하는 예외 스택 트레이스**:
  ```text
  javax.crypto.AEADBadTagException: Tag mismatch!
      at com.android.org.conscrypt.NativeCrypto.EVP_AEAD_CTX_open(Native Method)
      at com.android.org.conscrypt.OpenSSLCipherOpenSSL$EVP_AEAD.doFinalInternal(OpenSSLCipherOpenSSL.java:1320)
  ```
- **IV 고정 또는 재사용 시 Android Keystore 보안 예외**:
  ```text
  java.security.InvalidAlgorithmParameterException: Caller-provided IV not permitted
  ```

### 판단 기준

Secure storage 노트는 키 소유권(Key Ownership), 인증 암호화(AEAD), 생체 인증 바인딩, 백업 제외 설계가 서로 다른 방어선임을 구분하는 기준으로 읽는다.

### 경계

암호화 라이브러리 적용 자체를 안전 보장으로 오해하지 않고, 키 수명주기와 데이터 백업 경계를 별도로 설계한다.

상위 문서: [보안 저장소 계약](secure-storage-contracts.md)

관련 노트: [Android Keystore는 추출 불가능성으로 키를 보호한다](android-keystore-protects-keys-by-non-exportability.md)
