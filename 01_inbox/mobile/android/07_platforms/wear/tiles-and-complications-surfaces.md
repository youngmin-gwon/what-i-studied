---
title: tiles-and-complications-surfaces
tags: ["android", "android/platforms"]
aliases: []
date modified: 2026-08-04 15:35:00 +09:00
date created: 2026-08-03 17:28:21 +09:00
---

## Tile 과 Complication 은 워치페이스/런처에 데이터를 노출하는 별도 표면이다

상위 문서: [Android 폼 팩터와 플랫폼 확장 지도](../android-platforms-and-form-factors.md)

관련 지도: [Wear OS 계약](wear.md)

### 핵심 정의

Tile 은 워치의 홈 화면 옆(스와이프로 접근하는 화면)에 표시되는 빠른 조회/조작용 카드이고, Complication 은 워치페이스 위에 표시되는 작은 데이터 조각(걸음 수, 날씨 등)이다. 둘 다 메인 앱 액티비티를 실행하지 않고도 정보를 보여주는 별도 렌더링 표면으로, 각각 `TileService` 와 `ComplicationDataSourceService` 라는 별도 서비스 컴포넌트로 구현한다.

### 메커니즘 및 ProtoLayout / TileService 구현

`TileService` 는 ProtoLayout 계층으로 레이아웃 트리를 생성해 반환한다. 메인 액티비티 프로세스가 켜져 있지 않아도 시스템 요청 시점에 비동기 실행된다.

```kotlin
class FitnessTileService : TileService() {
    override fun onTileRequest(requestParams: TileRequest): ListenableFuture<Tile> {
        val rootLayout = LayoutElementBuilders.Layout.Builder()
            .setRoot(
                PrimaryLayout.Builder(buildDeviceParameters(requestParams))
                    .setContent(
                        Text.Builder(this, "Daily Steps: 8,420").build()
                    )
                    .build()
            ).build()

        val tile = Tile.Builder()
            .setResourcesVersion("1")
            .setTileTimeline(Timeline.fromLayoutElement(rootLayout))
            .build()

        return Futures.immediateFuture(tile)
    }
}
```

### 판단 기준

- Tile/Complication 에 표시할 데이터는 메인 앱과 별도의 저장소(캐시)에서 읽어야 하며, 메인 액티비티가 실행 중이어야만 최신 데이터를 얻을 수 있는 구조로 설계하지 않는다.
- Complication 은 화면 공간이 매우 작으므로 표시할 정보를 한두 개의 핵심 지표로 좁힌다. 여러 정보를 한 Complication 에 욱여넣지 않는다.
- Tile/Complication 데이터를 최신으로 유지하려면 WorkManager 같은 백그라운드 갱신 메커니즘과 함께 설계해야 하며, 이는 `04_system_services/background-and-notifications/background-work-contracts` 의 실행 수단 선택과 연결된다.

### 경계

- 이 노트는 Tile/Complication 이 메인 앱과 분리된 표면이라는 사실을 다룬다. 메인 앱 화면 자체의 절전 상태 처리는 [Ambient mode는 절전 화면에서 앱 화면을 유지하는 별도 lifecycle이다](ambient-mode-lifecycle.md) 가 다룬다.
- 백그라운드 데이터 갱신 실행 수단 자체의 선택 기준은 이 지도가 아니라 `04_system_services/background-and-notifications/background-work-contracts` 가 다룬다.

### 관측 가능한 증거 (Observable Evidence)

```bash
# 1. TileService 바인딩 상태 및 렌더링 세션 관측
adb shell dumpsys activity service TileService

# 2. Complication 데이터 제공 서비스(ComplicationDataSourceService) 덤프
adb shell dumpsys activity service ComplicationDataSourceService

# 3. ProtoLayout 렌더링 트리 로그캣 모니터링
adb logcat -v threadtime | grep -E "ProtoLayout|TileService"
```

### 공식 문서

- https://developer.android.com/training/wearables/tiles
- https://developer.android.com/training/wearables/complications

