---
title: health-connect-is-a-shared-on-device-store-not-a-cloud-sync-service
tags: ["android", "android/system-services"]
aliases: ["Health Connect는 클라우드 동기화가 아니라 앱 간 공유 온디바이스 저장소다"]
date modified: 2026-08-04 20:15:00 +09:00
date created: 2026-08-04 20:15:00 +09:00
---

## Health Connect 는 클라우드 동기화가 아니라 앱 간 공유 온디바이스 저장소다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [Health Connect 접근 계약](./health-connect-contracts.md)

### 핵심 정의

Health Connect 는 걸음 수, 심박수, 수면 세션 같은 건강·피트니스 레코드를 기기 안에 저장하고, 사용자가 허용한 범위 안에서 여러 앱이 그 레코드를 함께 읽고 쓸 수 있게 하는 플랫폼 API 다. 앱이 각자 Room DB 에 자기 데이터만 쌓는 일반적인 데이터 계층과 달리, Health Connect 의 레코드는 애초에 "이 기기의 건강 데이터"라는 하나의 공유 저장소에 속한다.

### 메커니즘

Health Connect 는 별도 앱(APK)으로 존재하며, 클라이언트 앱은 `HealthConnectClient` 를 통해 이 앱이 관리하는 저장소에 IPC 로 접근한다. 저장은 기기 로컬이고, 클라우드 서버로 자동 업로드되지 않는다 — "동기화"라는 단어는 앱이 자기 백엔드와 동기화할 때 Health Connect 의 변경 이력(change token)을 소스로 쓰는 것을 뜻하지, Health Connect 자체가 클라우드 서비스라는 뜻이 아니다.

Health Connect SDK 는 API 26+ 를 지원하지만, 실제로 동작하려면 API 28+ 기기에 Health Connect 앱이 설치돼 있어야 한다. 그래서 모든 호출 전에 가용성을 먼저 확인해야 한다.

```kotlin
val availability = HealthConnectClient.getSdkStatus(context)
when (availability) {
    HealthConnectClient.SDK_UNAVAILABLE -> {
        // 이 기기는 Health Connect를 지원하지 않는다
    }
    HealthConnectClient.SDK_UNAVAILABLE_PROVIDER_UPDATE_REQUIRED -> {
        // Health Connect 앱은 있지만 업데이트가 필요하다
    }
    HealthConnectClient.SDK_AVAILABLE -> {
        val client = HealthConnectClient.getOrCreate(context)
        // 이제 레코드 CRUD/변경 동기화 API를 쓸 수 있다
    }
}
```

가용성 확인 없이 바로 `HealthConnectClient.getOrCreate()` 를 호출하면, Health Connect 가 없는 기기에서 예외로 실패한다.

### 다이어그램

```
App A ──┐
        │  HealthConnectClient (IPC)
App B ──┼─────────────────────────────► Health Connect (별도 앱, 온디바이스 저장소)
        │                                    │
App C ──┘                                    ▼
                                       사용자가 앱별 · 레코드 타입별로
                                       read/write 권한을 개별 승인
```

### 판단 기준

- 우리 앱만 쓰는 내부 상태(예: 오늘 목표 걸음 수 UI 캐시)는 Room/DataStore 로 두고, 다른 앱과 공유하거나 다른 헬스 앱이 기록한 값을 읽어야 하는 데이터만 Health Connect 로 다룬다.
- Wear OS 기기에서 수집한 센서 원시값 자체는 Health Connect 의 책임이 아니다. 앱이 그 값을 레코드로 변환해 Health Connect 에 기록해야 다른 앱이 읽을 수 있다.
- 클라우드 백업이 필요하면 앱이 직접 자기 백엔드와 동기화해야 한다. Health Connect 는 이 동기화를 대신 해주지 않는다.

### 경계

- 이 노트는 Health Connect 의 위치·소유권 모델까지만 다룬다. 권한이 레코드 타입별로 나뉘는 세부는 [Health Connect 권한은 레코드 타입별로 개별 부여된다](./health-connect-permissions-are-granted-per-record-type-not-as-a-single-grant.md)가 다룬다.
- 특정 센서(걸음 수 계, 심박 센서)가 값을 어떻게 측정하는지는 [센서 접근 계약](../sensor-contracts/sensor-contracts.md)이 다룬다.

### 관찰 가능한 신호

`HealthConnectClient.getSdkStatus()` 가 `SDK_UNAVAILABLE` 을 반환하는데 이를 확인하지 않고 API 를 호출하면 클라이언트 생성 또는 첫 호출 시점에 예외가 발생한다. Health Connect 앱이 설치돼 있는지는 실기기/에뮬레이터의 앱 목록에서 "Health Connect" 패키지 존재 여부로 직접 확인할 수 있다.

### 공식 문서

- [Health Connect overview](https://developer.android.com/health-and-fitness/guides/health-connect)
- [Get started with Health Connect](https://developer.android.com/health-and-fitness/guides/health-connect/develop/get-started)

검증일: 2026-08-04. SDK 최소 API(26+)와 Health Connect 앱 요구 API(28+), 가용성 확인 API 를 공식 문서로 확인했다.
