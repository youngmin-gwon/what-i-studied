# Cellular 연결은 사용자 요금제와 시스템 정책의 영향을 받는다

상위 문서: [연결성 계약](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/connectivity-contracts.md)

Cellular network는 단순 fallback transport가 아니다. 사용자의 요금제, roaming, carrier policy, subscription, Data Saver, metered 상태가 앱의 전송 전략에 영향을 준다.

## 실무 규칙

- large upload/download는 cellular에서 사용자 동의나 pause/resume UX를 둔다.
- roaming과 metered 상태는 backend retry와 media quality 선택에 반영한다.
- 통신사 정보나 subscription 정보는 권한과 개인정보 경계가 있으므로 일반 connectivity 판단과 분리한다.
- cellular을 강제로 요청하는 기능은 배터리와 비용을 사용자에게 설명해야 한다.

## 관련 문서

- [Metered와 Data Saver는 백그라운드 네트워크 비용 정책이다](01_inbox/mobile/android/01_system_internals/connectivity/connectivity-contracts/metered-and-data-saver-are-background-network-cost-policy.md)
- [배터리, 네트워크, 저장소 효율은 리소스 정책이다](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/battery-network-storage-efficiency-is-resource-policy.md)
