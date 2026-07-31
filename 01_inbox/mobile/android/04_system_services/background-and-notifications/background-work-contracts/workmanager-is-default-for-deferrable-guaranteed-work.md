# WorkManager는 지연 가능한 보장 작업의 기본 선택이다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [백그라운드 작업 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)

## 핵심 주장

- WorkManager는 앱이 종료되거나 기기가 재부팅되어도 이어져야 하는 작업을 위한 기본 도구다.
- 실행 시각을 조금 늦출 수 있지만 결국 수행되어야 하는 동기화, 업로드, 정리 작업에 적합하다.
- WorkManager의 “보장”은 시스템 조건이 맞을 때 실행을 관리하고 실패 시 복구하는 의미다.
- 특정 시각에 정확히 시작하거나 계속 실행되는 것을 보장한다는 뜻은 아니다.
- 제약 조건을 추가하면 작업은 조건이 충족될 때까지 대기한다.
- 네트워크 타입, 충전 상태, 저장 공간 등의 조건은 작업의 비용과 필요성에 맞게 설정한다.
- 일회성 작업과 주기적 작업은 서로 다른 요청 타입으로 표현한다.
- 동일한 논리 작업에는 고유 작업 이름을 사용해 중복 예약 정책을 명시한다.

## 실패와 재시도

- 일시적 네트워크 오류는 Result.retry와 백오프 정책으로 처리한다.
- 잘못된 입력이나 인증 만료처럼 자동 재시도가 무의미한 오류는 실패로 종료한다.
- 재시도 횟수는 무한히 늘리지 않고 서버와 배터리 비용을 고려한다.
- 작업은 재시도 중 중복 수행될 수 있으므로 멱등성을 갖춰야 한다.
- 긴 작업은 중단 지점과 진행 상태를 저장해 재실행 비용을 줄인다.
- 관찰자는 성공, 실패, 취소, 실행 중 상태를 UI에 반영할 수 있다.

## 구현 경계

- CoroutineWorker는 suspend 기반 작업과 취소 전파를 연결하기에 적합하다.
- 작업 객체에 화면이나 액티비티 참조를 보관하지 않는다.
- 비동기 콜백을 사용할 때는 작업이 완료되기 전에 반환하지 않도록 한다.
- 장시간 사용자 가시 작업은 일반 Worker만으로 처리하지 말고 expedited work 또는 foreground 실행 요구를 검토한다.

## 예약 설계

- 주기적 작업의 반복 간격은 플랫폼의 최소 간격과 배터리 비용을 고려한다.
- 여러 데이터 변경을 하나의 작업으로 묶을 때 실패 시 부분 완료를 복구할 수 있어야 한다.
- ExistingWorkPolicy는 최신 요청을 우선할지 기존 요청을 보존할지에 따라 선택한다.
- 입력 데이터는 작고 직렬화 가능한 값으로 제한하고 큰 데이터는 영속 저장소에 둔다.
- 작업 결과를 UI에서 관찰하되 UI가 관찰을 중단해도 작업은 독립적으로 계속되어야 한다.
- 테스트에서는 제약 충족 전 대기, 제약 해제 후 실행, 재시도와 취소를 각각 검증한다.
- 네트워크 작업은 서버의 중복 요청 방지 키와 함께 설계하면 재시도 안전성이 높아진다.
- 예약 시점과 실제 실행 시점의 차이는 정상적인 시스템 동작으로 취급한다.

## 공식 문서

- [WorkManager 개요](https://developer.android.com/develop/background-work/background-tasks/persistent)
- [작업 제약 조건](https://developer.android.com/develop/background-work/background-tasks/persistent/getting-started/define-work)
- [WorkManager 작업 상태](https://developer.android.com/develop/background-work/background-tasks/persistent/how-to/observe)
