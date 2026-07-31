# Wi-Fi API는 스캔, 제안, 요청, 로컬 연결을 분리한다

상위 문서: [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

Android Wi-Fi API는 앱이 임의로 Wi-Fi를 켜고 네트워크를 바꾸는 권한을 주지 않는다. 스캔 관찰, 사용자에게 연결 후보 제안, 특정 네트워크 요청, local-only hotspot, Wi-Fi Aware는 서로 다른 권한과 UX 계약을 가진다.

## 실무 규칙

- `WifiManager.startScan()`과 scan result 접근은 위치 권한, Wi-Fi 권한, 위치 서비스, scan throttling의 영향을 받는다.
- Android 13(API 33) 이상 target에서 주변 Wi-Fi 기기 접근은 용도에 따라 `NEARBY_WIFI_DEVICES` 권한을 요구할 수 있다.
- 저장된 네트워크를 앱이 직접 수정하는 레거시 방식은 최신 Android에서 제한된다.
- 인터넷 자동 연결 후보는 Wi-Fi Network Suggestion으로 제출하지만 실제 선택은 시스템과 사용자가 결정한다.
- IoT 설정처럼 특정 피어에 일시 연결해야 하면 Wi-Fi Network Specifier를 `ConnectivityManager.requestNetwork()`와 함께 검토한다.
- local-only hotspot은 인터넷 공유가 아니라 근거리 통신용 SoftAP다.
- Wi-Fi Aware는 인터넷 연결이 아니라 주변 기기 발견과 peer-to-peer 데이터 경로를 위한 기능이다.

## 관련 문서

- [기본 네트워크와 요청 네트워크는 서로 다른 수명 계약을 가진다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/default-network-and-requested-network-have-different-lifetimes.md)
- [Android HAL과 커널](01_inbox/mobile/android/01_system_internals/kernel-and-hal/hal-native-contracts/hal-is-stable-userspace-contract-between-framework-and-vendor.md)

공식 문서: [Wi-Fi infrastructure](https://developer.android.com/develop/connectivity/wifi), [Wi-Fi scanning overview](https://developer.android.com/develop/connectivity/wifi/wifi-scan), [Wi-Fi permissions](https://developer.android.com/develop/connectivity/wifi/wifi-permissions), [Wi-Fi Aware](https://developer.android.com/develop/connectivity/wifi/wifi-aware)
