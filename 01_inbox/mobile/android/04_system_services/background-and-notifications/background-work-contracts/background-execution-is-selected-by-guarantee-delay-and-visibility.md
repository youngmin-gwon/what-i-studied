# Android 백그라운드 실행은 보장, 지연, 사용자 가시성으로 선택한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [백그라운드 작업 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)

## 핵심 주장

- 백그라운드 실행의 첫 질문은 어떤 API가 편한지가 아니라 작업의 실행 보장과 사용자 가시성이다.
- 앱 프로세스가 살아 있다는 사실은 백그라운드 작업이 계속 실행된다는 보장이 아니다.
- Android는 배터리와 시스템 자원을 보호하기 위해 백그라운드 서비스와 암시적 실행을 제한한다.
- 따라서 작업은 지연 가능 여부, 지속 시간, 정확한 시각 필요 여부, 사용자가 인지해야 하는지로 분류한다.
- 지연 가능한 일회성 또는 반복 작업은 WorkManager를 기본 선택으로 삼는다.
- 사용자가 현재 진행 중임을 알아야 하는 긴 작업은 정당한 foreground service 후보이다.
- 특정 시각에 깨우는 것이 본질인 기능은 AlarmManager를 검토한다.
- 화면이 열려 있을 때 끝나는 짧은 작업은 코루틴 등 현재 화면의 수명 범위에서 처리할 수 있다.

## 선택 순서

1. 작업이 현재 화면의 수명 안에서 끝나는가?
2. 화면이 사라져도 실행되어야 하는가?
3. 실행 시각의 정확성이 결과의 핵심인가?
4. 작업이 진행되는 동안 사용자에게 지속적인 상태를 보여야 하는가?
5. 네트워크, 충전, 유휴 상태 같은 제약이 있는가?

## 오해를 피하는 기준

- WorkManager는 즉시 실행이나 밀리초 단위의 시각 실행을 약속하는 API가 아니다.
- AlarmManager는 일반적인 데이터 동기화 스케줄러가 아니다.
- foreground service는 백그라운드 제한을 우회하기 위한 만능 권한이 아니다.
- 알람이 울렸다고 해서 수 초 이상 무거운 작업을 리시버에서 직접 수행해도 되는 것은 아니다.
- 장시간 작업은 알람이나 서비스 시작을 계기로 별도의 적절한 실행 컴포넌트에 위임한다.

## 설계 결과물

- 기능 명세에는 허용 가능한 지연 시간과 최대 실행 시간을 함께 기록한다.
- 사용자가 작업을 시작했는지 시스템이 작업을 예약했는지 시작 주체를 구분한다.
- 작업 중단 시 사용자에게 보여줄 상태와 다시 시도할 경로를 정의한다.
- 예약은 화면 코드가 아니라 애플리케이션의 작업 조정 계층에서 관리한다.
- 플랫폼이 실행을 늦출 수 있다는 사실을 사용자 경험 문구와 상태 모델에 반영한다.
- 실행 수단을 바꿔도 동일한 도메인 작업을 재사용할 수 있도록 실행 로직을 분리한다.
- 최종 선택은 API 이름이 아니라 작업의 실패 허용도와 사용자 기대를 만족해야 한다.
- 선택 기준은 문서화해 기능 변경과 Android 버전 상승 때 다시 검토한다.

## 공식 문서

- [백그라운드 작업 개요](https://developer.android.com/develop/background-work/background-tasks)
- [백그라운드 작업 선택](https://developer.android.com/develop/background-work/background-tasks)
- [앱 전원 관리](https://developer.android.com/topic/performance/power)
