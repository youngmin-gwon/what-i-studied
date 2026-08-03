---
title: wear-os-apps-can-run-independently-of-a-companion-phone-app
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-03 18:15:35 +09:00
date created: 2026-08-03 18:05:35 +09:00
---

## Wear OS 앱은 동반 휴대폰 앱과 독립적으로 실행될 수 있다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](01_inbox/mobile/android/07_platforms/android-platforms-and-form-factors.md)

관련 지도: [Wear OS 계약](01_inbox/mobile/android/07_platforms/wear/wear-contracts/wear-contracts.md)

### 핵심 정의

Wear OS 앱은 페어링된 휴대폰의 동반 앱 없이도 워치 단독(standalone)으로 설치, 실행될 수 있다. 워치는 자체 Play 스토어와 자체 네트워크(Wi-Fi, LTE 모델의 경우 셀룰러)를 가질 수 있는 독립된 Android 기기이며, 동반 앱은 선택적 확장이지 필수 의존성이 아니다.

### 메커니즘

워치 앱과 휴대폰 앱이 데이터를 주고받아야 한다면 Wearable Data Layer API(`DataClient`, `MessageClient`, `CapabilityClient`)를 사용한다. 이 API 는 두 기기가 항상 연결되어 있다고 가정하지 않고, 연결이 끊긴 동안의 데이터는 동기화 큐에 쌓아뒀다가 재연결 시 전달하는 방식으로 동작한다. `CapabilityClient` 로 상대 기기에 특정 앱이 설치되어 있는지, 어떤 기능을 지원하는지 확인할 수 있다.

### 판단 기준

- 워치 앱이 항상 휴대폰과 실시간으로 연결되어 있다고 가정하지 않는다. 연결 끊김을 정상 상태로 다루고, 로컬에서 동작 가능한 최소 기능(오프라인 모드)을 갖춘다.
- 동반 휴대폰 앱이 반드시 필요한 기능(예: 최초 로그인)이 있다면 `CapabilityClient` 로 동반 앱 설치 여부를 확인하고, 없을 경우 설치 유도 흐름을 제공한다.
- 워치 전용 기능(피트니스 트래킹 등)은 동반 앱 실행 여부와 무관하게 워치에서 독립적으로 동작하도록 설계하는 것이 일반적으로 더 나은 사용자 경험이다.

### 경계

- 이 노트는 워치 - 휴대폰 앱 간 독립성과 통신 모델을 다룬다. 화면이 꺼진 것처럼 보이는 절전 상태에서의 UI 유지는 [Ambient mode는 절전 화면에서 앱 화면을 유지하는 별도 lifecycle이다](01_inbox/mobile/android/07_platforms/wear/wear-contracts/ambient-mode-is-a-separate-lifecycle-for-always-on-screens.md) 가 다룬다.
- 일반적인 Android 프로세스/lifecycle 모델 자체는 `02_app_framework` 가 다루며 이 노트는 Wear 고유의 기기 간 통신만 다룬다.

### 관찰 가능한 신호

`adb -s <watch_device> shell dumpsys activity` 로 워치에서 앱이 휴대폰 연결 없이도 독립적으로 프로세스를 유지하는지 확인할 수 있다. Data Layer API 통신은 두 기기 각각에서 로그를 남겨 동기화 지연이나 실패를 관찰한다.

### 공식 문서

- https://developer.android.com/training/wearables
- https://developer.android.com/training/wearables/data/data-layer
