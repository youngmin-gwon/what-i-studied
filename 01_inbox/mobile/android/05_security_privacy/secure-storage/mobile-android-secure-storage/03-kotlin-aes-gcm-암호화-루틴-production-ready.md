# [Kotlin] AES-GCM 암호화 루틴 (Production-ready)

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
