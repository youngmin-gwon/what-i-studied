# NFC와 비접촉 기능 계약

이 지도는 Android NFC를 태그 읽기/쓰기, NDEF, HCE/APDU, Observe Mode, 결제 엔지니어링으로 분리한다.

## 정본 노트
- [Android NFC는 리더, 태그, 카드 에뮬레이션 모드로 나뉜다](01_inbox/mobile/android/04_system_services/device-capabilities/nfc-contracts/android-nfc-splits-reader-tag-and-card-emulation-modes.md)
- [NDEF는 태그 데이터를 메시지와 레코드로 구조화한다](01_inbox/mobile/android/04_system_services/device-capabilities/nfc-contracts/ndef-structures-tag-data-as-messages-and-records.md)
- [HCE는 HostApduService가 APDU 거래를 처리하는 모델이다](01_inbox/mobile/android/04_system_services/device-capabilities/nfc-contracts/hce-uses-hostapduservice-to-handle-apdu-transactions.md)
- [Android 15 Observe Mode는 HCE 거래 전 폴링을 관찰한다](01_inbox/mobile/android/04_system_services/device-capabilities/nfc-contracts/android-15-observe-mode-observes-polling-before-hce-transactions.md)
- [비접촉 결제는 NFC 태깅과 별도 엔지니어링 문제다](01_inbox/mobile/android/04_system_services/device-capabilities/nfc-contracts/contactless-payment-is-separate-from-nfc-tagging.md)
