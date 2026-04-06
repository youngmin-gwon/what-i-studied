---
title: mobile-android-secure-storage
tags: [android, biometric, keystore, security]
aliases: [Android 보안 저장소, 생체 인증]
date modified: 2026-04-06 18:50:47 +09:00
date created: 2026-04-05 12:40:00 +09:00
---

## [[mobile-security]] > [[mobile-android-secure-storage]]

### Android Secure Storage: Keystore & Biometrics

상용 서비스에서 민감 정보(사용자 토큰, 서명 키 등)를 보호하기 위해 하드웨어 기반의 **Android Keystore**와 **BiometricPrompt**를 결합한 보안 저장소 구현 가이드입니다.

#### 🛡️ Context: 왜 Keystore 인가?

소프트웨어 수준의 암호화는 기기가 루팅되거나 OS 취약점이 발견될 경우 키가 유출될 위험이 큽니다. Keystore 는 키를 **TEE(Trusted Execution Environment)** 또는 **StrongBox** 등 격리된 하드웨어 영역에 가두어 물리적인 탈취를 방지합니다.

#### 1. Android Keystore 시스템 아키텍처

- **하드웨어 격리**: 키는 **TEE(Trusted Execution Environment)** 또는 **StrongBox(보안 칩)** 내부에서 생성 및 관리되며, 운영체제(Android)로 키 원본이 유출되지 않습니다.
- **Keymaster / KeyMint**: 하드웨어 측에서 암호화 연산을 수행하는 인터페이스입니다.

#### 2. [Kotlin] AES-GCM 암호화 루틴 (Production-ready)

가장 권장되는 대칭키 암호화 방식인 **AES-GCM (256-bit)** 라이브러리 레벨 구현입니다.

```kotlin
import android.security.keystore.KeyGenParameterSpec
import android.security.keystore.KeyProperties
import java.security.KeyStore
import javax.crypto.Cipher
import javax.crypto.KeyGenerator
import javax.crypto.spec.GCMParameterSpec

class SecureStorageManager {
    private val provider = "AndroidKeyStore"
    private val keyAlias = "production_encryption_key"

    init {
        generateKeyIfNeeded()
    }

    private fun generateKeyIfNeeded() {
        val keyStore = KeyStore.getInstance(provider).apply { load(null) }
        if (!keyStore.containsAlias(keyAlias)) {
            val keyGenerator = KeyGenerator.getInstance(KeyProperties.KEY_ALGORITHM_AES, provider)
            keyGenerator.init(
                KeyGenParameterSpec.Builder(keyAlias, KeyProperties.PURPOSE_ENCRYPT or KeyProperties.PURPOSE_DECRYPT)
                    .setBlockModes(KeyProperties.BLOCK_MODE_GCM)
                    .setEncryptionPaddings(KeyProperties.ENCRYPTION_PADDING_NONE)
                    .setKeySize(256)
                    // .setUserAuthenticationRequired(true) // 생체인증 후 사용 시 활성화
                    .setIsStrongBoxBacked(true) // StrongBox 지원 기기 활용
                    .build()
            )
            keyGenerator.generateKey()
        }
    }

    fun encrypt(data: String): Pair<ByteArray, ByteArray> {
        val cipher = Cipher.getInstance("AES/GCM/NoPadding")
        val keyStore = KeyStore.getInstance(provider).apply { load(null) }
        val secretKey = (keyStore.getEntry(keyAlias, null) as KeyStore.SecretKeyEntry).secretKey
        
        cipher.init(Cipher.ENCRYPT_MODE, secretKey)
        val iv = cipher.iv
        val encryptedData = cipher.doFinal(data.toByteArray())
        return iv to encryptedData
    }

    fun decrypt(iv: ByteArray, encryptedData: ByteArray): String {
        val cipher = Cipher.getInstance("AES/GCM/NoPadding")
        val keyStore = KeyStore.getInstance(provider).apply { load(null) }
        val secretKey = (keyStore.getEntry(keyAlias, null) as KeyStore.SecretKeyEntry).secretKey
        
        val spec = GCMParameterSpec(128, iv)
        cipher.init(Cipher.DECRYPT_MODE, secretKey, spec)
        return String(cipher.doFinal(encryptedData))
    }
}
```

#### 3. BiometricPrompt 연동 및 보안 등급 (Tiering)

안드로이드 10+ 부터는 **BiometricPrompt**를 통해 일관된 UI 와 보안 등급별 제어를 수행합니다.

##### 보안 등급(Authentication Tiers) 이해

- **BIOMETRIC_STRONG (Class 3)**: 하드웨어 보안 수준이 가장 높으며, **Keystore 키 잠금 해제** 에 사용 가능합니다. (지문, 3D 얼굴인식 등)
- **BIOMETRIC_WEAK (Class 2)**: 2D 얼굴 인식 등 보안성이 상대적으로 낮으며, 단순 서비스 진입 등 앱 내 로직용으로 사용합니다.

##### [Kotlin] 생체 인증 구현 예시

```kotlin
val biometricPrompt = BiometricPrompt(activity, executor, object : BiometricPrompt.AuthenticationCallback() {
    override fun onAuthenticationSucceeded(result: BiometricPrompt.AuthenticationResult) {
        super.onAuthenticationSucceeded(result)
        // 지문 일치 시 처리 (예: Keystore 키를 사용한 토큰 복호화)
    }
})

val promptInfo = BiometricPrompt.PromptInfo.Builder()
    .setTitle("보안 인증")
    .setSubtitle("생체 정보를 사용하여 인증을 완료하십시오.")
    .setAllowedAuthenticators(BiometricManager.Authenticators.BIOMETRIC_STRONG or BiometricManager.Authenticators.DEVICE_CREDENTIAL)
    .build()

biometricPrompt.authenticate(promptInfo)
```

#### 🛡️ 정보보안기사 실무 대응 가이드

1. **중요 데이터 저장 금지**: Keystore 에 키를 저장하되, **서버 URL 이나 비즈니스 로직에 기반한 고정된 값**은 소스 코드에 하드코딩하지 말고 환경변수나 TEE 내부에서 파생된 키를 사용해야 합니다.
2. **Key Invalidated on New Biometric**: `setInvalidatedByBiometricEnrollment(true)` 옵션을 주어, 사용자가 새로운 지문을 등록했을 때 기존 키를 무효화하여 부정 사용을 방지하십시오.
3. **취약점 대응**: `Cipher` 객체를 초기화할 때 `IV(Initialization Vector)` 를 매번 랜덤하게 생성하여 동일 평문에 대해 다른 암호문이 나오도록 보장해야 합니다. (GCM 모드 필수 사항)

#### 📚 연결 문서

- [android-security-and-sandboxing](android-security-and-sandboxing.md) - 안드로이드 기초 보안 아키텍처
- [mobile-vulnerability-check](../../cross-platform/mobile-vulnerability-check.md)- 모바일 취약점 진단 가이드
