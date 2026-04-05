---
title: apple-nfc-and-contactless
tags: [apple, ios/26, nfc, corenfc, payments, contactless, secure-element]
aliases: [CoreNFC, NFC, Contactless Payments, SE Entitlement]
date modified: 2026-04-04 00:33:00 +09:00
date created: 2026-04-04 00:33:00 +09:00
---

## Apple NFC & Contactless Payments

애플은 역사적으로 NFC 기능을 Apple Pay에 한정하였으나, 최근(iOS 18.1/26+) 유럽 연합(EU)의 디지털 시장법(DMA)과 글로벌 결제 환경 변화에 발맞춰 **제3자 비접촉 결제(Contactless Payments)**를 개방하였다.

> [!NOTE] **Android 비교: NFC HCE vs Apple SE Entitlement**
> - **Android**: 소프트웨어 기반의 HCE(Host-based Card Emulation)를 통해 누구나 자유롭게 결제 앱을 만들 수 있다. (개방적)
> - **iOS**: 하드웨어 보안 칩인 **Secure Element (SE)**에 직접 접근할 수 있는 권한을 제공한다. 애플과 상업적 계약을 맺고 특정 자격(Entitlement)을 획득한 앱만 결제 기능을 구현할 수 있다. (통제된 개방)
> 자세한 내용은 [android-nfc-and-contactless](../../android/04_system_services/android-nfc-and-contactless.md)를 참고하세요.

### 1. SE Entitlement & 제3자 비접촉 결제 (iOS 26+)

애플은 보안과 개인정보 보호를 위해 결제 앱이 하드웨어 보안 요소(SE)를 안전하게 사용할 수 있도록 통제한다.

- **요구사항**: 애플과 상업적 계약 체결, 특정 보안 표준 준수, 권한(Entitlement) 승인 필요.
- **기능**: Apple Pay와 독립적으로 매장 결제, 교통카드, 자동차 키, 호텔 키 등을 구현할 수 있다.

#### 결제 세션 시작 예시 (`CoreNFC`)

```swift
import CoreNFC

// iOS 26+ 신규 비접촉 결제 세션
let session = NFCPaymentTagReaderSession(delegate: self, queue: nil, invalidateAfterFirstRead: true)
session.begin()

// Delegate에서 SE 통신 처리
func paymentTagReaderSession(_ session: NFCPaymentTagReaderSession, didDetect tags: [NFCPaymentTag]) {
    // 보안 요소(SE)를 통한 트랜잭션 수행
}
```

### 2. 기본 비접촉 결제 앱 설정

사용자는 설정에서 **"기본 비접촉 결제 앱"**을 선택할 수 있다. 선택된 앱은 측면 버튼(Side Button)을 두 번 클릭하는 제스처를 통해 Apple Pay처럼 즉시 실행될 수 있다.

### 3. CoreNFC 태그 읽기/쓰기 (NDEF)

비결제 기능인 NDEF 태그 읽기/쓰기는 모든 개발자가 `CoreNFC`를 통해 사용할 수 있다.

- **Reader Session**: `NFCNDEFReaderSession`을 통해 태그를 스캔하고 데이터를 추출한다.
- **Background Tag Reading**: 앱이 켜져 있지 않아도 특정 태그에 반응하여 알림을 띄울 수 있다.

---

### 🏛️ 애플 NFC 개발 전략

애플의 NFC 개방은 여전히 **보안**을 최우선으로 한다. 기술적 구현보다 권한 획득과 상업적 요건(비용 등)을 갖추는 것이 앱 런칭의 핵심이다.

> [!IMPORTANT] **Apple 개발자를 위한 제언 : UX 의 일관성**
> 제3자 결제를 구현하더라도 사용자가 Apple Pay에서 경험하던 "측면 버튼 더블 클릭"과 같은 시스템 통합 경험을 제공해야 한다. 독자적인 UI만 고집하기보다 시스템 기본 동작에 녹아드는 설계가 필수적이다.

### 더 보기
- [apple-app-lifecycle-and-ui](../02_ui_frameworks/apple-app-lifecycle-and-ui.md) - 앱의 상태와 NFC 세션
- [apple-sandbox-and-security](../05_security_privacy/apple-sandbox-and-security.md) - 보안 요소(SE)의 구조
- [apple-intelligence-and-agentic-intents](apple-intelligence-and-agentic-intents.md) - 에이전트 결제 승인
