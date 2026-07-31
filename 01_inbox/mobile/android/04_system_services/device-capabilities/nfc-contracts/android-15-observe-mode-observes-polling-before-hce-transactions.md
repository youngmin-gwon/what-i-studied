---
title: "Android 15 Observe Mode는 HCE 거래 전 폴링을 관찰한다"
tags: ["android", "android/system-services"]
---

# Android 15 Observe Mode는 HCE 거래 전 폴링을 관찰한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [NFC와 비접촉 기능 계약](01_inbox/mobile/android/04_system_services/device-capabilities/nfc-contracts/nfc-contracts.md)

## Observe Mode

Android 15에서 HCE 서비스는 NFC polling loop를 관찰하는 Observe Mode를 사용할 수 있다.
Observe Mode가 켜지면 NFC 스택은 거래를 허용하지 않고 폴링을 수동 관찰한다.
관찰 결과는 적절한 HostApduService에 전달되어 단말과 상호작용을 준비하게 한다.
이는 결제를 수행하는 모드가 아니라 거래 전 준비와 감지를 위한 모드다.

## 서비스 API 흐름

HostApduService는 setObserveModeEnabled(true)로 관찰을 활성화할 수 있다.
정확히 일치하는 프레임에는 registerPollingLoopFilterForService를 사용한다.
패턴 기반 조건에는 registerPollingLoopPatternFilterForService를 사용한다.
필터에 맞는 비표준 폴링 프레임은 processPollingFrames로 전달된다.
필터는 필요한 프레임만 매칭하도록 좁게 설계해 오탐을 줄인다.

## 전환 설계

관찰 단계와 실제 APDU 거래 단계를 별도 상태로 모델링한다.
관찰만으로 결제가 완료되었다고 판단하지 않는다.
리더의 실제 선택과 APDU 교환이 시작된 뒤에만 거래 상태를 전진시킨다.
연속 프레임, 중복 알림, 타임아웃, 폴링 중단을 모두 처리한다.
기기와 NFC 컨트롤러 구현 차이를 고려해 실제 단말에서 검증한다.

## 기본 지갑 앱

Android 15 이상은 사용자가 선택할 수 있는 기본 지갑 앱 역할을 제공한다.
설정의 기본 앱에서 사용자가 기본 지갑을 선택할 수 있다.
payment 카테고리 AID 그룹을 선언한 HCE 서비스가 지갑 앱 후보가 된다.
RoleManager.ROLE_WALLET로 현재 역할 보유 여부를 확인할 수 있다.
createRequestRoleIntent로 사용자에게 역할 요청 흐름을 시작할 수 있다.

## 사용자 경험

기본 지갑 역할 요청은 결제 시점이 아니라 사용자가 이해할 수 있는 맥락에서 제시한다.
기본 지갑이 아닌 상태에서도 앱은 가능한 기능과 제한을 명확히 알려야 한다.
Quick Access Wallet을 제공하려면 관련 서비스와 기본 NFC 결제 조건을 함께 검토한다.
잠금 해제 요구, 서비스 배너, 시스템 설정 이동을 실제 흐름에서 확인한다.

## 오해하기 쉬운 점

Observe Mode는 Android 15의 NFC 동작 개선이지만 NFC 전송 속도 8배를 보장하지 않는다.
Android Developers 문서에 없는 NFC Forum 2026 기능을 플랫폼 사실로 단정하지 않는다.
Multi-purpose Tap도 일반 HCE API가 자동 제공하는 기능으로 간주하지 않는다.

## 공식 문서

- https://developer.android.com/develop/connectivity/nfc/hce
- https://developer.android.com/reference/android/app/role/RoleManager
- https://developer.android.com/reference/android/service/quickaccesswallet/QuickAccessWalletService
