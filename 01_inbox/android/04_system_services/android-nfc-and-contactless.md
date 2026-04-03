---
title: android-nfc-and-contactless
tags: [android, android/16, nfc, hce, payments, contactless]
aliases: [NFC, HCE, Host Card Emulation, Contactless Payments]
date modified: 2026-04-04 00:33:00 +09:00
date created: 2026-04-04 00:33:00 +09:00
---

## Android NFC & Contactless Payments

안드로이드는 초기부터 NFC 기능을 개방적으로 운영해 왔으며, **HCE (Host-based Card Emulation)** 기술을 통해 앱이 보안 요소(Secure Element) 없이도 스마트카드를 에뮬레이션할 수 있도록 지원한다.

> [!NOTE] **iOS 비교: CoreNFC vs Android NFC**
> - **iOS**: 과거에는 Apple Pay 외에 NFC 결제가 불가능했으나, 최근(iOS 26/18.1+) **SE Entitlement**를 통해 제3자 앱도 비접촉 결제 권한을 얻을 수 있게 되었다.
> - **Android**: 오래전부터 HCE를 통해 독자적인 지갑 앱 구축이 가능했다. 안드로이드 16에서는 NFC Forum 2026 표준을 반영하여 전송 속도와 다목적 탭(Multi-purpose Tap) 기능이 대폭 향상되었다.
> 자세한 내용은 [apple-nfc-and-contactless](../../apple/04_system_services/apple-nfc-and-contactless.md)를 참고하세요.

### 1. Host-based Card Emulation (HCE)

HCE는 물리적 보안 칩셋 대신 호스트 CPU와 소프트웨어를 통해 NFC 통신을 처리한다.

#### HCE 서비스 구현 (`HostApduService`)

```kotlin
class MyPaymentService : HostApduService() {
    override fun processCommandApdu(commandApdu: ByteArray, extras: Bundle?): ByteArray {
        // POS 단말기로부터 받은 APDU 명령을 처리하고 응답 반환
        val response = handlePaymentLogic(commandApdu)
        return response
    }

    override fun onDeactivated(reason: Int) {
        // NFC 연결 해제 시 처리
    }
}
```

- **AID (Application ID)**: 지갑 앱은 고유한 AID를 등록해야 시스템이 적절한 앱으로 이벤트를 라우팅한다.

### 2. NFC Forum 2026 신기술 반영 (Android 16+)

- **8x Speed Boost**: 데이터 전송 속도가 최대 8배 빨라져 태그 읽기/쓰기 및 결제 응답성이 획기적으로 개선되었다.
- **Multi-purpose Tap**: 한 번의 탭으로 결제, 멤버십 적립, 디지털 영수증 수령을 동시에 수행할 수 있다.

### 3. NFC 태깅 (NDEF)

비결제 기능인 데이터 읽기/쓰기는 NDEF(NFC Data Exchange Format) 표준을 따른다. `NfcAdapter`를 통해 태그 검색 및 데이터 교환을 수행한다.

---

### 🏛️ 안드로이드 NFC 개발 전략

안드로이드는 개방성이 높지만, 그만큼 기기마다 NFC 안테나 위치와 성능이 다르다는 점(**Fragmentation**)을 고려해야 한다.

> [!TIP] **Devil's Advocate : 시스템 지갑과의 조화**
> 독자적인 결제 기능을 구축하더라도, Android 16의 "기본 비접촉 결제 앱" 설정을 통해 사용자가 시스템 수준에서 앱을 선택할 수 있도록 유도해야 한다. 단순히 HCE를 구현하는 것보다 사용자 경험의 통합(`Live Updates` 연동 등)이 더 중요하다.

### 더 보기
- [android-app-components-deep-dive](../02_app_framework/android-app-components-deep-dive.md) - 서비스 구조
- [android-security-and-sandboxing](../05_security_privacy/android-security-and-sandboxing.md) - NFC 통신 보안
- [android-appfunctions-and-ai-agents](../02_app_framework/android-appfunctions-and-ai-agents.md) - 에이전트 기반 결제 요청
