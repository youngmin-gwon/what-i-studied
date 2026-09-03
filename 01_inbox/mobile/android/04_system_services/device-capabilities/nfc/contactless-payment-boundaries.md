---
title: contactless-payment-boundaries
tags: ["android", "android/system-services"]
aliases: ["비접촉 결제는 NFC 태깅과 별도 엔지니어링 문제다"]
date modified: 2026-08-24 18:05:00 +09:00
date created: 2026-07-31 17:46:00 +09:00
---

## 비접촉 결제는 NFC 태깅과 별도 엔지니어링 문제다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [NFC와 비접촉 기능 계약](nfc.md)

### 결제와 태깅의 차이

NDEF 태깅은 단순 URI나 MIME 데이터를 읽고 쓰는 흐름인 반면, 비접촉 결제는 결제 단말(POS)과 EMV 표준 기반 ISO 7816-4 APDU를 교환하며 암호화된 토큰을 검증하는 복합 엔지니어링 영역이다. HCE, Secure Element, 키스토어, 백엔드 토큰화(Tokenization)가 결합된다.

### 다이어그램

```mermaid
flowchart TD
    subgraph ClientAndApp["결제 앱 (Client Application)"]
        WalletApp["지갑 앱 (RoleManager.ROLE_WALLET)"]
        Keystore["AndroidKeyStore (인증 키 / 세션 토큰)"]
    end

    subgraph SystemHCE["Android 시스템 HCE 프레임워크"]
        HostService["HostApduService (Payment Category)"]
        CardEmulationService["CardEmulation (Default Wallet 라우팅)"]
    end

    subgraph ExternalPOS["외부 환경 & 결제망"]
        POSTerminal["POS 결제 단말 (ISO-DEP 리더)"]
        PaymentServer["결제 네트워크 서버 (토큰 검증 및 승인)"]
    end

    WalletApp --> HostService
    Keystore --> HostService
    HostService --> CardEmulationService
    CardEmulationService <-->|NFC RF (APDU)| POSTerminal
    POSTerminal -->|온라인 승인 요청| PaymentServer
```

### 코드 예시: 기본 결제 서비스 확인 및 설정 유도

```kotlin
val cardEmulation = CardEmulation.getInstance(nfcAdapter)
val paymentComponent = ComponentName(context, MyPaymentService::class.java)

// 1. 현재 앱이 기본 결제 서비스인지 확인
val isDefault = cardEmulation.isDefaultServiceForCategory(
    paymentComponent,
    CardEmulation.CATEGORY_PAYMENT
)

if (!isDefault) {
    // 2. 기본 결제 서비스 등록 설정 다이얼로그 팝업
    val intent = Intent(CardEmulation.ACTION_CHANGE_DEFAULT).apply {
        putExtra(CardEmulation.EXTRA_CATEGORY, CardEmulation.CATEGORY_PAYMENT)
        putExtra(CardEmulation.EXTRA_SERVICE_COMPONENT, paymentComponent)
    }
    context.startActivity(intent)
}
```

### 거래 상태와 보안 원칙

1. **상태 머신**: SELECT AID -> GET PROCESSING OPTIONS -> READ RECORD -> GENERATE AC(Application Cryptogram)로 이어지는 EMV 거래 상태를 명시적으로 관리한다.
2. **토큰 보안**: 민감한 실제 카드 번호(PAN)를 기기에 저장하지 않고, 결제망(TSP)에서 발급받은 제한적 사용 토큰(LUPC)을 활용한다.
3. **네트워크 지연 격리**: NFC 탭 시간(보통 500ms 이내)을 만족하기 위해 거래 시점에는 오프라인 암호 토큰으로 응답하고 백엔드 승인은 비동기로 처리한다.

### 경계

- 이 노트는 비접촉 결제 시스템의 엔지니어링 경계를 다룬다. 저수준 HCE 구현은 [HCE는 HostApduService가 APDU 거래를 처리하는 모델이다](hce-host-apdu-service.md)가 다룬다.
- 키 관리 및 생체 인증 연동은 [생체 인증/자격 증명 계약](../biometrics-credential/biometrics-credential.md)이 다룬다.

### 관찰 가능한 신호

```bash
# 1. 결제 카테고리 기본 서비스 확인
adb shell dumpsys nfc | grep -A 10 "Payment Defaults"

# 2. 기본 결제 서비스 변경 인텐트 로그 확인
adb logcat -s CardEmulation PaymentService
```

### 공식 문서

- https://developer.android.com/develop/connectivity/nfc
- https://developer.android.com/develop/connectivity/nfc/hce
- https://developer.android.com/develop/connectivity/nfc/advanced-nfc

검증일: 2026-08-03. CardEmulation 결제 카테고리 및 기본 지갑 설정을 공식 문서를 기준으로 확인했다.
