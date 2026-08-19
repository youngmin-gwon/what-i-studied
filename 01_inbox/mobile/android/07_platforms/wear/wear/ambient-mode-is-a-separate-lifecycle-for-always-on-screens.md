---
title: ambient-mode-is-a-separate-lifecycle-for-always-on-screens
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-06 14:48:27 +09:00
date created: 2026-08-03 17:28:06 +09:00
---

## Ambient mode 는 always-on 화면의 별도 저전력 상태다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](../../android-platforms-and-form-factors.md)

관련 지도: [Wear OS 계약](./wear.md)

### 핵심 정의

Wear OS의 fullscreen 앱은 interactive와 ambient라는 전력 상태 사이를 전환할 수 있다. ambient에서는 화면이 어두워지고 갱신이 드물어지지만, 앱 구성과 Wear OS 버전에 따라 앱 UI가 계속 보이거나 시스템이 일시 중지된 화면의 스크린샷과 시간을 표시할 수 있다. 이는 Android `Lifecycle.State`가 하나 더 생긴다는 뜻이 아니라, lifecycle-aware API로 관찰하는 시스템 전력 상태다.

Wear OS 5 이하의 기본 동작은 일시 중지된 앱 스크린샷에 시간을 겹쳐 표시할 수 있다. Wear OS 6 이상에서 target SDK 36 이상인 앱은 기본 always-on 동작이 적용된다. 앱이 자체 UI를 ambient에서도 계속 갱신하는 ambiactive 동작이 필요하면 공식 ambient API를 사용한다.

### 메커니즘 및 Compose 구현

현재 Wear Compose에서는 `rememberAmbientModeManager()`로 manager를 만들고 `LocalAmbientModeManager`로 제공한 뒤 `currentAmbientMode`와 `AmbientTickEffect`를 관찰한다. 기존 View 기반 앱은 `AmbientLifecycleObserver`를 사용할 수 있다. ambient UI는 업데이트를 줄이고 애니메이션·불필요한 정보를 제거하되, 특정 색상이나 콜백 주기를 모든 기기에 고정해서 가정하지 않는다.

```kotlin
@Composable
fun WearApp() {
    val manager = rememberAmbientModeManager()

    CompositionLocalProvider(LocalAmbientModeManager provides manager) {
        val mode = manager.currentAmbientMode

        manager.AmbientTickEffect {
            // ambient에서 시스템이 허용한 tick에 최소 정보만 갱신한다.
        }

        AppContent(
            lowPower = mode is AmbientMode.Ambient,
            animationsEnabled = mode is AmbientMode.Interactive,
        )
    }
}
```

### 판단 기준

- ambient 진입 시 화면 요소의 밝은 색상과 세밀한 애니메이션을 제거해 번인(burn-in)을 방지하고 배터리 소모를 줄인다. interactive 모드의 화면을 그대로 유지하지 않는다.
- ambient tick은 드물 수 있으므로 화면에 표시할 최소 정보만 갱신한다. 정확히 매분 호출된다고 타이머 계약처럼 의존하지 않는다.
- always-on 화면을 지원하지 않는 워치 모델도 있으므로, ambient 콜백이 아예 호출되지 않는 기기에서도 일반 lifecycle 만으로 앱이 정상 동작해야 한다.

### 경계

- 이 노트는 ambient 진입/유지 시점의 화면 처리를 다룬다. 워치와 휴대폰 간 통신 모델은 [Wear OS 앱은 동반 휴대폰 앱과 독립적으로 실행될 수 있다](./wear-os-apps-can-run-independently-of-a-companion-phone-app.md) 가 다룬다.
- 앱 화면 밖에서 정보를 보여주는 Tile/Complication 은 [Tile과 Complication은 워치페이스/런처에 데이터를 노출하는 별도 표면이다](./tiles-and-complications-are-separate-surfaces-from-the-main-app.md) 가 다룬다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 1. Always-on 설정이 켜진 기기를 절전/interactive 상태로 전환
adb shell input keyevent KEYCODE_SLEEP
adb shell input keyevent KEYCODE_WAKEUP

# 2. Ambient Mode 수신 로그 관측
adb logcat -v threadtime | grep -E "AmbientMode|AmbientLifecycle"
```

### 공식 문서

- https://developer.android.com/training/wearables/always-on

검증일: 2026-08-06. 최신 Wear OS always-on 가이드의 `LocalAmbientModeManager`/`AmbientLifecycleObserver`, Wear OS 6·target SDK 36 기본 동작, 공식 ADB keyevent 절차를 반영했다.
