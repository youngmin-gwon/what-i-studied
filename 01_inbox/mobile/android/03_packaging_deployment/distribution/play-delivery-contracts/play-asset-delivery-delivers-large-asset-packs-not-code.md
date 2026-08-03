---
title: play-asset-delivery-delivers-large-asset-packs-not-code
tags: ["android", "android/packaging-deployment"]
aliases: []
date modified: 2026-08-03 18:12:42 +09:00
date created: 2026-07-31 17:52:17 +09:00
---

## Play Asset Delivery 는 코드가 아니라 대용량 asset pack 을 전달한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)

관련 지도: [Play Delivery 계약](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/play-delivery-contracts.md)

관련 노트: [AAB는 Play가 기기별 APK를 생성하는 게시 아티팩트다](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/aab-is-publishing-artifact-for-play-generated-apks.md), [Delivery mode는 기능 필수성, 조건, 런타임 요청으로 선택한다](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/delivery-mode-is-selected-by-necessity-condition-and-runtime-request.md)

### 역할

Play Asset Delivery 는 게임의 texture, shader, sound 같은 대형 리소스를

Android App Bundle 에 포함해 Google Play 가 전달하도록 하는 시스템이다.

실행 가능한 코드는 asset pack 에 넣지 않는다.

기존 OBB 를 대체하고, 하나의 게시 아티팩트와 Play 호스팅을 사용한다.

### 세 가지 모드

| 모드 | 동작 | 사용 가능 시점 |
| --- | --- | --- |
| install-time | 앱 설치와 함께 전달 | 앱 실행 즉시 |
| fast-follow | 설치 직후 자동 다운로드 시작 | 완료 전에도 앱 실행 가능 |
| on-demand | 앱이 실행 중 요청 | 다운로드 완료 후 |

install-time pack 은 Play Store 표시 앱 크기에 포함되고 split APK 로 제공된다.

fast-follow 와 on-demand pack 은 archive 로 제공된 뒤 앱 내부 저장소에 풀린다.

두 모드는 Play Store 표시 앱 크기에 같은 방식으로 포함되지 않는다.

### Gradle 설정

```kotlin
// asset-pack/build.gradle.kts
plugins { id("com.android.asset-pack") }

assetPack {
    packName.set("level_assets")
    dynamicDelivery { deliveryType.set("fast-follow") }
}

// app/build.gradle.kts
android { assetPacks += listOf(":asset-pack") }
```

### 런타임 주의

fast-follow 는 다운로드 완료를 보장하지 않으므로 매 실행마다 상태를 확인한다.

on-demand 는 다운로드 크기를 먼저 조회하고 네트워크·저장 공간 오류를 처리한다.

200MB 보다 큰 모바일 데이터 다운로드는 사용자 확인이나 Wi-Fi 대기가 발생할 수 있다.

asset 위치를 캐시하지 말고 매 실행 시 Play Asset Delivery API 로 조회한다.

업데이트나 데이터 삭제로 위치가 바뀌거나 pack 이 무효화될 수 있다.

앱은 반환된 asset 을 읽기 전용으로 취급해 patch 무결성을 보존한다.

### 테스트

로컬 테스트에서 fast-follow 는 on-demand 처럼 동작할 수 있다.

실제 전달·네트워크·업데이트 동작은 Play 내부 테스트 또는 내부 앱 공유로 검증한다.

### 공식 문서

- [Play Asset Delivery](https://developer.android.com/guide/playcore/asset-delivery)
- [Integrate asset delivery for Kotlin and Java](https://developer.android.com/guide/playcore/asset-delivery/integrate-java)
- [Test asset delivery](https://developer.android.com/guide/playcore/asset-delivery/test)
