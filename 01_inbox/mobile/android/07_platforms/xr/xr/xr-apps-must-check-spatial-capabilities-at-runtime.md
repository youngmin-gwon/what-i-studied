---
title: xr-apps-must-check-spatial-capabilities-at-runtime
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-07-31 18:06:11 +09:00
---

## XR 앱은 공간 capability 를 실행 중에 확인해야 한다

상위 문서: [Android XR 계약](./xr.md)

XR 앱은 어떤 공간 기능이 항상 가능하다고 가정하면 안 된다. Home Space, Full Space, 기기 종류, 사용자 조작, 시스템 상태에 따라 spatial UI, 3D content, environment, passthrough, spatial audio 같은 capability 가 달라질 수 있다.

### Capability 쿼리 및 Listener 연동 메커니즘

```kotlin
fun observeSpatialCapabilities(activity: ComponentActivity, onCapabilitiesChanged: (SpatialCapabilities) -> Unit) {
    val session = Session.getOrCreate(activity)
    
    // 1. 현재 동기적 Capability 확인
    val currentCapabilities = session.spatialCapabilities
    onCapabilitiesChanged(currentCapabilities)
    
    // 2. 런타임 Capability 동적 변동 수신
    session.addSpatialCapabilitiesChangedListener { updatedCapabilities ->
        val canSpatialAudio = updatedCapabilities.hasCapability(SpatialCapabilities.SPATIAL_AUDIO)
        val can3DEnvironment = updatedCapabilities.hasCapability(SpatialCapabilities.SPATIAL_ENVIRONMENT)
        onCapabilitiesChanged(updatedCapabilities)
    }
}
```

### 실무 규칙

- 현재 환경에서 가능한 기능을 `Session.spatialCapabilities` 로 확인한 뒤 UI 를 선택한다.
- 공간 기능이 없을 때 2D fallback 이 자연스럽게 남아야 한다.
- capability 변화는 일회성 초기화 값이 아니라 UI state 입력으로 취급하고 `addSpatialCapabilitiesChangedListener` 로 갱신을 관찰한다.
- 권한이 필요한 perception 또는 scene understanding 기능은 권한 요청과 실패 UI 를 함께 설계한다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# XR Spatial Capabilities 변경 동적 이벤트를 로그캣으로 관측
adb logcat -v threadtime | grep -E "SpatialCapabilities|onCapabilitiesChanged"

# 헤드셋 Passthrough 및 Spatial Capabilities 시스템 서명 덤프
adb shell dumpsys activity service XrSystemService
```

### 관련 문서

- [Compose for XR은 기존 Compose를 subspace와 spatial component로 확장한다](./compose-for-xr-extends-compose-with-subspace-and-spatial-components.md)

공식 문서: [Check for spatial capabilities](https://developer.android.com/develop/xr/jetpack-xr-sdk/check-spatial-capabilities), [Transition from Home Space to Full Space](https://developer.android.com/develop/xr/jetpack-xr-sdk/transition-home-space-to-full-space)

검증일: 2026-08-03. capability 는 기기뿐 아니라 Home Space/Full Space 전환과 시스템·사용자 조작으로도 달라질 수 있다.

