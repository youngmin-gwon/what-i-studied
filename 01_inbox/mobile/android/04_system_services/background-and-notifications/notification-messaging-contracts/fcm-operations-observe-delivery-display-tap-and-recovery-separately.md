# FCM 운영은 전달, 표시, 탭, 복구를 분리해 관측한다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [알림과 FCM 메시징 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/notification-messaging-contracts.md)
관련 정본: [Android 백그라운드 실행은 보장, 지연, 사용자 가시성으로 선택한다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-execution-is-selected-by-guarantee-delay-and-visibility.md)

## 초기 설정

- Firebase 프로젝트와 Android 앱의 application ID가 일치하는지 확인한다.
- FCM SDK와 `FirebaseMessagingService`를 등록한다.
- 서버 전송은 Admin SDK 또는 HTTP v1 API를 신뢰된 백엔드에서만 호출한다.
- Android 8 이상용 채널과 Android 13 이상용 권한 흐름을 구현한다.
- 기본 알림 아이콘, 색상, 클릭 목적지를 정의한다.

## 수신 처리

- 포그라운드 notification, data, combined 메시지를 각각 검증한다.
- 백그라운드 notification 메시지가 시스템 트레이로 가는지 확인한다.
- combined 메시지의 data가 탭 Intent extras에 도착하는지 확인한다.
- data-only 수신 후 짧은 처리와 장기 작업 예약을 분리한다.
- 앱 강제 종료, 프로세스 종료, Doze, 네트워크 불가 상태를 테스트한다.

## 서버와 식별자

- `onNewToken` 또는 현재 등록 조회 결과를 서버에 업로드한다.
- 사용자 한 명의 여러 기기와 로그아웃·계정 전환을 분리한다.
- `UNREGISTERED` 등록을 제거하고 전송 오류를 유형별로 기록한다.
- token 또는 FID의 마지막 갱신 시각과 앱 버전을 저장한다.
- topic 구독은 식별자 변경과 사용자 권한 변경 시 다시 계산한다.

## 내용과 보안

- payload에는 최소 데이터만 넣고 서버에서 최신 상태를 재조회한다.
- 메시지 ID, 버전, 만료 시각으로 멱등성과 오래된 이벤트 폐기를 구현한다.
- 알림 탭으로 열린 화면에서 Intent extras를 검증한다.
- 잠금 화면에 민감한 본문이 노출되지 않도록 채널과 표시 정책을 설정한다.
- FCM token을 사용자 비밀번호나 세션 자격 증명으로 취급하지 않는다.

## 관측 지표

- 전송 요청, FCM 오류, 앱 수신, 알림 게시, 사용자 탭을 별도 이벤트로 기록한다.
- 권한 거부와 채널 차단을 전달 실패로 합산하지 않는다.
- high 메시지가 실제 사용자 표시로 이어지는 비율을 확인한다.
- 누락 복구를 위한 앱 시작 전체 동기화 성공률을 측정한다.

## 참고

- [FCM Android 시작 안내](https://firebase.google.com/docs/cloud-messaging/android/get-started)
- [FCM 메시지 전달 이해](https://firebase.google.com/docs/cloud-messaging/understand-delivery)
- [Android 백그라운드 작업 개요](https://developer.android.com/develop/background-work/background-tasks)
