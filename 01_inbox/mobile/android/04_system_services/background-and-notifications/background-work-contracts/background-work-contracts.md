# 백그라운드 작업 계약

이 지도는 Android 백그라운드 실행을 API 목록이 아니라 실행 보장, 지연 허용도, 사용자 가시성, 시간 정확성의 판단 단위로 나눈다.

## 정본 노트
- [Android 백그라운드 실행은 보장, 지연, 사용자 가시성으로 선택한다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-execution-is-selected-by-guarantee-delay-and-visibility.md)
- [백그라운드 제한은 작업 상태를 영속적으로 설계하게 만든다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-restrictions-require-persistent-work-state.md)
- [WorkManager는 지연 가능한 보장 작업의 기본 선택이다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/workmanager-is-default-for-deferrable-guaranteed-work.md)
- [Foreground service는 사용자에게 보이는 지속 작업에 쓴다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/foreground-service-is-for-visible-continuous-work.md)
- [AlarmManager는 시간 자체가 기능인 이벤트에 쓴다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/alarmmanager-is-for-time-based-user-events.md)
- [백그라운드 실행 수단은 실패 비용으로 결정한다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-api-selection-is-a-failure-cost-decision.md)
