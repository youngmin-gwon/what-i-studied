# Host-based Card Emulation (HCE)

HCE 는 물리적 보안 칩셋 대신 호스트 CPU 와 소프트웨어를 통해 NFC 통신을 처리한다.

##### HCE 서비스 구현 (`HostApduService`)

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

- **AID (Application ID)**: 지갑 앱은 고유한 AID 를 등록해야 시스템이 적절한 앱으로 이벤트를 라우팅한다.
