# [[mobile-security]] > [[android-nfc-and-contactless]]

## NFC & Payments: Contactless Strategy

안드로이드의 비접촉 결제 표준인 **HCE (Host-based Card Emulation)** 기술과 Android 16에서 강화된 **NFC Forum 2026** 표준 대응 방안을 분석합니다. 

단순히 태그를 읽고 쓰는 기능을 넘어, 보안 요소(Secure Element) 없이도 안전한 결제 환경을 구축하고 다목적 탭(Multi-purpose Tap) 기능을 통해 사용자 경험을 혁신하는 것이 목표입니다.

---

### 💡 Context: 개방형 결제 플랫폼의 진화

안드로이드는 초기부터 NFC를 개방적으로 운영하며 HCE를 통해 독자적인 지갑 앱 구축을 지원해 왔습니다. 최근 플랫폼의 변화는 더 빠른 전송 속도와 시스템 수준의 통합 비접촉 결제 앱 설정을 통한 사용자 선택권 강화에 집중하고 있습니다. [[android-app-components-deep-dive]]의 Service 구조 위에서 동작합니다.

> [!NOTE] **상호 참조**
> iOS의 NFC 및 비접촉 결제 지원 방식은 [[apple-nfc-and-contactless]]를 참고하세요.

---

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

### See Also

- [[android-app-components-deep-dive]] - 서비스 구조
- [[android-security-and-sandboxing]] - NFC 통신 보안
- [[android-appfunctions-and-ai-agents]] - 에이전트 기반 결제 요청
