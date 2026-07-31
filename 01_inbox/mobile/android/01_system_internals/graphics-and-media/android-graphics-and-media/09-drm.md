# DRM

상위 노트: [[android-graphics-and-media]]

### Widevine

```kotlin
val drmSessionManager = DefaultDrmSessionManager.Builder()
    .setUuidAndExoMediaDrmProvider(
        C.WIDEVINE_UUID,
        FrameworkMediaDrm.DEFAULT_PROVIDER
    )
    .build(object : MediaDrmCallback {
        override fun executeProvisionRequest(request: ProvisionRequest): ByteArray {
            // 라이선스 서버에서 provision 받기
        }
        
        override fun executeKeyRequest(request: KeyRequest): ByteArray {
            // 콘텐츠 키 받기
        }
    })

val mediaSource = DashMediaSource.Factory(dataSourceFactory)
    .setDrmSessionManagerProvider { drmSessionManager }
    .createMediaSource(mediaItem)
```

**보안**:

- L1: 하드웨어 보안 (TEE)
- L3: 소프트웨어 보안

---
