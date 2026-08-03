---
title: tiles-and-complications-are-separate-surfaces-from-the-main-app
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-03 18:16:04 +09:00
date created: 2026-08-03 17:28:21 +09:00
---

## Tile 과 Complication 은 워치페이스/런처에 데이터를 노출하는 별도 표면이다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](01_inbox/mobile/android/07_platforms/android-platforms-and-form-factors.md)

관련 지도: [Wear OS 계약](01_inbox/mobile/android/07_platforms/wear/wear-contracts/wear-contracts.md)

### 핵심 정의

Tile 은 워치의 홈 화면 옆(스와이프로 접근하는 화면)에 표시되는 빠른 조회/조작용 카드이고, Complication 은 워치페이스 위에 표시되는 작은 데이터 조각(걸음 수, 날씨 등)이다. 둘 다 메인 앱 액티비티를 실행하지 않고도 정보를 보여주는 별도 렌더링 표면으로, 각각 `TileService` 와 `ComplicationDataSourceService` 라는 별도 서비스 컴포넌트로 구현한다.

### 메커니즘

`TileService` 는 시스템이 요청할 때(사용자가 해당 Tile 화면으로 스와이프하거나 갱신 주기가 됐을 때) 레이아웃 트리를 생성해 반환하는 방식으로 동작하며, 항상 실행 중인 프로세스가 아니라 필요 시 시스템이 호출하는 형태다. `ComplicationDataSourceService` 도 마찬가지로 워치페이스가 데이터를 요청할 때 짧은 값(텍스트, 아이콘, 진행률 등)을 반환한다. 두 서비스 모두 무거운 연산이나 긴 네트워크 대기를 이 호출 안에서 수행하면 안 되며, 실제 데이터는 백그라운드 작업으로 미리 갱신해 캐시해 두는 것이 일반적이다.

### 판단 기준

- Tile/Complication 에 표시할 데이터는 메인 앱과 별도의 저장소(캐시)에서 읽어야 하며, 메인 액티비티가 실행 중이어야만 최신 데이터를 얻을 수 있는 구조로 설계하지 않는다.
- Complication 은 화면 공간이 매우 작으므로 표시할 정보를 한두 개의 핵심 지표로 좁힌다. 여러 정보를 한 Complication 에 욱여넣지 않는다.
- Tile/Complication 데이터를 최신으로 유지하려면 WorkManager 같은 백그라운드 갱신 메커니즘과 함께 설계해야 하며, 이는 `04_system_services/background-and-notifications/background-work-contracts` 의 실행 수단 선택과 연결된다.

### 경계

- 이 노트는 Tile/Complication 이 메인 앱과 분리된 표면이라는 사실을 다룬다. 메인 앱 화면 자체의 절전 상태 처리는 [Ambient mode는 절전 화면에서 앱 화면을 유지하는 별도 lifecycle이다](01_inbox/mobile/android/07_platforms/wear/wear-contracts/ambient-mode-is-a-separate-lifecycle-for-always-on-screens.md) 가 다룬다.
- 백그라운드 데이터 갱신 실행 수단 자체의 선택 기준은 이 지도가 아니라 `04_system_services/background-and-notifications/background-work-contracts` 가 다룬다.

### 관찰 가능한 신호

`adb shell dumpsys activity services` 에서 `TileService`/`ComplicationDataSourceService` 컴포넌트가 요청 시점에만 바인딩되는지 확인할 수 있다. Complication 이 갱신되지 않으면 데이터 소스 서비스가 실제로 새 데이터를 반환하고 있는지 로그로 먼저 확인한다.

### 공식 문서

- https://developer.android.com/training/wearables/tiles
- https://developer.android.com/training/wearables/complications
