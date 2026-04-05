---
title: android-security-play-integrity
tags: [android, android/security, play-integrity]
aliases: [Play Integrity API, SafetyNet replacement, 구글 무결성 API]
date modified: 2026-04-05 17:43:35 +09:00
date created: 2026-04-05 16:29:26 +09:00
---

## [[mobile-security]] > [[android-security-play-integrity]]

### Play Integrity API

과거의 SafetyNet 을 대체하는 **Play Integrity API**는 앱과 기기의 무결성을 검증하여 부정 행위(Cheat)나 변조(Tampering)를 방지한다.

#### 핵심 검증 레이어

1. **App Integrity**: Google Play 에서 승인한 앱 버전인지 확인.
2. **Device Integrity**: 신뢰할 수 있는 구글 인증 기기(정식 안드로이드 기기)인지 확인.
3. **Account Integrity**: 사용자 계정의 신뢰도(봇 여부 등) 확인.

#### Standard Integrity 실무 구현 (2026 기준)

기존 Classic 방식 대비 레이턴시가 낮고 **Request Binding**이 강화된 Standard Integrity 사용이 필수적이다.

```kotlin
class SecurityIntegrityClient(private val context: Context) {
    private val integrityManager = IntegrityManagerFactory.createStandard(context)
    private var tokenProvider: StandardIntegrityTokenProvider? = null

    // 1. Warm-up (앱 시작 시 호출)
    suspend fun prepareProvider(cloudProjectNumber: Long) {
        val request = StandardIntegrityManager.PrepareIntegrityTokenRequest.builder()
            .setCloudProjectNumber(cloudProjectNumber)
            .build()
        tokenProvider = integrityManager.prepareIntegrityToken(request).await()
    }

    // 2. Token Request with Binding
    suspend fun requestToken(requestPayload: String): String? {
        val provider = tokenProvider ?: return null
        
        // 요청 데이터의 해시를 생성하여 결과 토큰과 바인딩 (Replay Attack 방지)
        val requestHash = MessageDigest.getInstance("SHA-256")
            .digest(requestPayload.toByteArray())
            .joinToString("") { "%02x".format(it) }

        val tokenRequest = StandardIntegrityManager.StandardIntegrityTokenRequest.builder()
            .setRequestHash(requestHash)
            .build()

        return try {
            provider.request(tokenRequest).await().token()
        } catch (e: Exception) {
            null
        }
    }
}
```

#### 서버 측 검증 (Enforcement)

클라이언트의 토큰은 반드시 서버에서 **Google Play Developer API**를 통해 검증해야 한다.

- **MEETS_STRONG_INTEGRITY**: Hardened 하드웨어(TEE, StrongBox) 기반 검증 통과. (금융권 권장)
- **MEETS_DEVICE_INTEGRITY**: 순정 안드로이드 기기 여부.
- **MEETS_BASIC_INTEGRITY**: 루팅 여부나 에뮬레이터 여부 확인.

---
#### 연관 문서
- [[mobile-android-secure-storage]] - 검증 결과를 바탕으로 한 비밀 데이터 저장
- [[mobile-vulnerability-check]] - 무결성 검증 우회 진단
