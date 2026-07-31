# AlarmManager는 시간 자체가 기능인 이벤트에 쓴다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [백그라운드 작업 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md)

## 핵심 주장

- AlarmManager는 특정 시각 또는 시간 간격에 시스템이 앱을 깨워야 하는 기능에 적합하다.
- 알람 시계, 약 복용 알림, 캘린더 리마인더처럼 시간 자체가 기능의 핵심인 경우를 우선 검토한다.
- 일반적인 서버 동기화는 시간이 조금 밀려도 되므로 WorkManager가 보통 더 적합하다.
- 정확한 알람은 배터리 비용이 있으므로 꼭 필요한 경우에만 사용한다.
- Android 12 이상에서는 exact alarm 사용 가능 여부와 권한 정책을 확인해야 한다.
- exact alarm 권한이 없으면 부정확한 알람이나 다른 작업 수단으로 요구사항을 낮춘다.
- setExactAndAllowWhileIdle은 유휴 상태에서도 정확성을 높이는 대신 남용해서는 안 된다.
- 알람은 실행을 시작하는 신호이지 장시간 작업을 수행할 공간 자체가 아니다.

## PendingIntent와 재예약

- PendingIntent의 action, data, extras가 같은 알람을 식별하는 방식에 영향을 준다.
- 알람을 갱신할 때는 동일한 식별자를 사용하고 이전 예약과의 관계를 명확히 한다.
- 사용자가 설정을 바꾸면 기존 알람을 취소한 뒤 새 설정으로 예약한다.
- 재부팅 뒤에도 필요한 알람은 부팅 이벤트와 저장된 설정을 이용해 재예약한다.
- 반복 알람의 간격이 기능적으로 충분하면 정확한 개별 알람보다 반복 예약을 고려한다.
- 수신기에서는 알림 표시나 짧은 위임만 수행하고 긴 네트워크 작업은 별도로 넘긴다.

## 검증 항목

- 시간대, 서머타임, 기기 시계 변경을 테스트한다.
- Doze와 앱 대기 상태에서 허용되는 지연을 확인한다.
- 알람 권한 거부, 배터리 제한, 앱 데이터 삭제 후 동작을 확인한다.
- 알람을 사용해 백그라운드 정책을 우회하려는 설계는 요구사항부터 다시 분류한다.

## 사용자 설정과 정확성

- 사용자에게 정확한 시각이 필요한지 아니면 대략적인 시간대면 충분한지 먼저 묻는다.
- 대략적인 알림은 부정확한 알람이나 WorkManager로 배터리 비용을 낮출 수 있다.
- exact alarm 권한은 기능에 필수인 경우에만 요청하고 거부 시 대체 경로를 제공한다.
- 알람 식별자와 설정을 영속 저장해 재부팅과 시간대 변경에 대응한다.
- 알람 수를 기능별로 제한해 같은 목적의 예약이 누적되지 않게 한다.
- PendingIntent에 필요한 변경 불가 플래그와 명시적 컴포넌트를 사용한다.
- 예약 시각과 실제 수신 시각을 기록하면 제조사별 지연을 진단할 수 있다.
- 알람 수신 후의 사용자 알림은 알람의 목적과 동일한 시간 의미를 유지해야 한다.

## 공식 문서

- [알람 예약](https://developer.android.com/develop/background-work/services/alarms)
- [정확한 알람 권한](https://developer.android.com/about/versions/12/behavior-changes-12#exact-alarm-permission)
- [AlarmManager API](https://developer.android.com/reference/android/app/AlarmManager)
