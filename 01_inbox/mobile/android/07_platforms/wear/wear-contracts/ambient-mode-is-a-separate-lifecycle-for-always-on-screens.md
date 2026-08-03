---
title: ambient-mode-is-a-separate-lifecycle-for-always-on-screens
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-03 18:16:03 +09:00
date created: 2026-08-03 17:28:06 +09:00
---

## Ambient mode 는 절전 화면에서 앱 화면을 유지하는 별도 lifecycle 이다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](01_inbox/mobile/android/07_platforms/android-platforms-and-form-factors.md)

관련 지도: [Wear OS 계약](01_inbox/mobile/android/07_platforms/wear/wear-contracts/wear-contracts.md)

### 핵심 정의

일반 휴대폰 앱은 화면이 꺼지면 백그라운드로 전환되지만, Wear OS 의 always-on 지원 화면에서는 앱이 저전력 "ambient mode"로 전환되며 화면 자체는 계속 표시된다(밝기와 갱신 빈도가 낮아진 형태로). 이는 일반적인 Activity 의 stop/resume 과 다른 별도의 상태 전이다.

### 메커니즘

`androidx.wear.ambient` 라이브러리는 `AmbientModeSupport`(또는 Compose 에서 대응 API)로 interactive 모드와 ambient 모드 전환 콜백(`onEnterAmbient()`, `onUpdateAmbient()`, `onExitAmbient()`)을 제공한다. ambient 모드에서는 시스템이 배터리 절약을 위해 화면 갱신 주기를 제한하므로(예: 분 단위로만 갱신), 앱은 이 시점에 색상 팔레트를 단순화하고(번인 방지를 위한 저휘도/단색 처리) 애니메이션을 멈춰야 한다.

### 판단 기준

- ambient 진입 시 화면 요소의 밝은 색상과 세밀한 애니메이션을 제거해 번인(burn-in)을 방지하고 배터리 소모를 줄인다. interactive 모드의 화면을 그대로 유지하지 않는다.
- `onUpdateAmbient()` 가 호출되는 주기(대략 분 단위)에 맞춰 화면에 표시할 최소 정보(시간, 핵심 지표)만 갱신한다. 초 단위로 갱신되는 정보를 ambient 에서 그대로 보여주려 하지 않는다.
- always-on 화면을 지원하지 않는 워치 모델도 있으므로, ambient 콜백이 아예 호출되지 않는 기기에서도 일반 lifecycle 만으로 앱이 정상 동작해야 한다.

### 경계

- 이 노트는 ambient 진입/유지 시점의 화면 처리를 다룬다. 워치와 휴대폰 간 통신 모델은 [Wear OS 앱은 동반 휴대폰 앱과 독립적으로 실행될 수 있다](01_inbox/mobile/android/07_platforms/wear/wear-contracts/wear-os-apps-can-run-independently-of-a-companion-phone-app.md) 가 다룬다.
- 앱 화면 밖에서 정보를 보여주는 Tile/Complication 은 [Tile과 Complication은 워치페이스/런처에 데이터를 노출하는 별도 표면이다](01_inbox/mobile/android/07_platforms/wear/wear-contracts/tiles-and-complications-are-separate-surfaces-from-the-main-app.md) 가 다룬다.

### 관찰 가능한 신호

워치 에뮬레이터/실기기에서 화면 터치 없이 일정 시간을 두면 ambient 전환이 발생하며, 이때 로그로 `onEnterAmbient()` 호출과 화면 갱신 빈도 변화를 관찰할 수 있다.

### 공식 문서

- https://developer.android.com/training/wearables/views/always-on
