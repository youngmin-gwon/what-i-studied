---
title: xr-release-readiness-validation
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-07-31 18:08:32 +09:00
---

## XR 출시 준비는 기능 시연이 아니라 기기, fallback, 정책 검증이다

상위 문서: [Android XR 계약](./xr.md)

XR 앱이 한 번 실행되는 것과 출시 가능한 것은 다르다. 지원 기기, SDK 성숙도, runtime capability, 입력 fallback, 성능, 편안함, 권한, Play 배포 정책까지 반복 검증해야 출시 준비라고 볼 수 있다.

### Device Category 및 Fallback 준비도 검증

| Hardware Category | Core Input Pathway | Mandatory Fallback Route | Play Release Readiness Checklist |
| :--- | :--- | :--- | :--- |
| **XR Headset** | Gaze + Pinch, 6DoF Controllers | 2D Single Panel Mode | Complete 90Hz frame time test & Passthrough disclosure |
| **Wired XR Glasses** | Phone Trackpad, Head Orientation | Flat Phone Screen UI | Verify battery consumption & tethering lifecycle |
| **Display / Audio Glasses** | Voice, Frame Buttons | Companion Phone Notifications | Confirm preview API stability & limited capability fallback |

XR 앱이 기기에 설치되기 위해서는 매니페스트에 필요한 하드웨어 기능을 명시해야 한다. 기기 유형에 따라 필수 여부를 조절한다.

```xml
<!-- XR 앱 설치를 위한 필수 기능 선언 예시 -->
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <!-- XR 전용 앱인 경우 true, 하위 호환을 지원하는 경우 false로 설정 -->
    <uses-feature android:name="android.software.xr.immersive" android:required="false" />
    <!-- 6DoF 트래킹 요구 여부 -->
    <uses-feature android:name="android.hardware.vr.headtracking" android:required="false" />
</manifest>
```

### 체크 기준

- 지원 폼 팩터를 XR headset, wired XR glasses, audio glasses, display glasses 중 어디까지로 둘지 명시하고 각 기기 유형에 적용되는 공식 지침의 preview 범위를 구분한다.
- 필수 capability 가 없거나 권한이 거부되었을 때 2D 또는 축소 기능 fallback 이 남아야 한다.
- 실제 기기와 emulator 에서 frame pacing, 발열, 배터리, 텍스트 가독성, 장시간 사용 편안함을 확인한다.
- alpha/beta 라이브러리는 API 변경 비용을 release risk 로 기록한다.
- Play 배포, 스토어 등록, 기기 호환성 정책은 출시 직전 공식 문서 기준으로 재확인한다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 1. XR 패키지 하드웨어 사양 서명 및 불투명 하드웨어 차단 여부 검증
adb shell pm dump <package_name> | grep -E "uses-feature|reqGlEsVersion"

# 2. XR 기기 호환성 런타임 수신 디버깅
adb logcat -v threadtime | grep -E "XrReleaseValidator|DeviceCapabilityFallback"
```

### 관련 문서

- [Jetpack XR SDK는 preview 성숙도를 전제로 채택해야 한다](jetpack-xr-sdk-adoption.md)
- [XR 앱은 공간 capability를 실행 중에 확인해야 한다](xr-spatial-capability-checks.md)
- [XR 품질은 성능, 편안함, 안전을 기능 요구사항으로 포함한다](xr-comfort-safety-performance.md)
- [Android 패키징과 배포 지도](../../03_packaging_deployment/android-packaging-deployment.md)

공식 문서: [Android XR app quality](https://developer.android.com/docs/quality-guidelines/android-xr), [Develop with the Jetpack XR SDK](https://developer.android.com/develop/xr/jetpack-xr-sdk), [AndroidX releases](https://developer.android.com/jetpack/androidx/versions)

검증일: 2026-08-03. 현재 XR quality checklist 는 headset 과 wired XR glasses 를 대상으로 하며 audio/display glasses 용 augmented experience 지침은 preview 로 표시된다. SDK 전체에 단일 preview 상태를 붙이지 말고 사용 라이브러리와 기기 유형별 상태를 다시 확인한다.

