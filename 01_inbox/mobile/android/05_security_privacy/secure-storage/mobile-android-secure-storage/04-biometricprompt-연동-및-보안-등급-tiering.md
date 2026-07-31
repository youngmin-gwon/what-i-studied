# BiometricPrompt 연동 및 보안 등급 (Tiering)

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
