---
title: ambient-mode-is-a-separate-lifecycle-for-always-on-screens
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-08-03 17:28:06 +09:00
---

## Ambient mode 는 절전 화면에서 앱 화면을 유지하는 별도 lifecycle 이다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](../../android-platforms-and-form-factors.md)

관련 지도: [Wear OS 계약](./wear-contracts.md)

### 핵심 정의

일반 휴대폰 앱은 화면이 꺼지면 백그라운드로 전환되지만, Wear OS 의 always-on 지원 화면에서는 앱이 저전력 "ambient mode"로 전환되며 화면 자체는 계속 표시된다(밝기와 갱신 빈도가 낮아진 형태로). 이는 일반적인 Activity 의 stop/resume 과 다른 별도의 상태 전이다.

### 메커니즘 및 AmbientModeSupport 구현

`androidx.wear.ambient` 라이브러리는 `AmbientModeSupport.AmbientCallback` 으로 interactive 모드와 ambient 모드 전환 콜백을 제공한다. ambient 모드에서는 배터리 및 번인 방지를 위해 단색/저휘도 렌더링을 적용한다.

```kotlin
class WearActivity : ComponentActivity(), AmbientModeSupport.AmbientCallbackProvider {

    override fun getAmbientCallback(): AmbientModeSupport.AmbientCallback =
        object : AmbientModeSupport.AmbientCallback() {
            override fun onEnterAmbient(ambientDetails: Bundle?) {
                // 저휘도/단색 UI 전환, 애니메이션 중지
                setLowPowerDisplay(true)
            }

            override fun onUpdateAmbient() {
                // 분 단위 최소 정보 갱신
                updateTimeAndMetrics()
            }

            override fun onExitAmbient() {
                // 풀 컬러 UI 및 애니메이션 복원
                setLowPowerDisplay(false)
            }
        }
}
```

### 판단 기준

- ambient 진입 시 화면 요소의 밝은 색상과 세밀한 애니메이션을 제거해 번인(burn-in)을 방지하고 배터리 소모를 줄인다. interactive 모드의 화면을 그대로 유지하지 않는다.
- `onUpdateAmbient()` 가 호출되는 주기(대략 분 단위)에 맞춰 화면에 표시할 최소 정보(시간, 핵심 지표)만 갱신한다. 초 단위로 갱신되는 정보를 ambient 에서 그대로 보여주려 하지 않는다.
- always-on 화면을 지원하지 않는 워치 모델도 있으므로, ambient 콜백이 아예 호출되지 않는 기기에서도 일반 lifecycle 만으로 앱이 정상 동작해야 한다.

### 경계

- 이 노트는 ambient 진입/유지 시점의 화면 처리를 다룬다. 워치와 휴대폰 간 통신 모델은 [Wear OS 앱은 동반 휴대폰 앱과 독립적으로 실행될 수 있다](./wear-os-apps-can-run-independently-of-a-companion-phone-app.md) 가 다룬다.
- 앱 화면 밖에서 정보를 보여주는 Tile/Complication 은 [Tile과 Complication은 워치페이스/런처에 데이터를 노출하는 별도 표면이다](./tiles-and-complications-are-separate-surfaces-from-the-main-app.md) 가 다룬다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 1. ADB로 워치 Ambient 모드 강제 진입/탈출 명령
adb shell am broadcast -a com.google.android.wearable.action.ENTER_AMBIENT
adb shell am broadcast -a com.google.android.wearable.action.EXIT_AMBIENT

# 2. Ambient Mode 수신 로그 관측
adb logcat -v threadtime | grep -E "AmbientModeSupport|onEnterAmbient"
```

### 공식 문서

- https://developer.android.com/training/wearables/views/always-on

