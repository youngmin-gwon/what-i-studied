# FCM 등록 식별자는 사용자 계정이 아니라 앱 인스턴스를 가리킨다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](01_inbox/mobile/android/04_system_services/android-system-services-and-device-capabilities.md)
관련 지도: [알림과 FCM 메시징 계약](01_inbox/mobile/android/04_system_services/background-and-notifications/notification-messaging-contracts/notification-messaging-contracts.md)
관련 정본: [Android 백그라운드 실행은 보장, 지연, 사용자 가시성으로 선택한다](01_inbox/mobile/android/04_system_services/background-and-notifications/background-work-contracts/background-execution-is-selected-by-guarantee-delay-and-visibility.md)

## 식별자의 의미

FCM 등록 토큰은 특정 앱 설치 또는 앱 인스턴스로 메시지를 보내기 위한 값이다.
현재 Firebase 문서는 Firebase Installation ID(FID) 중심의 등록 관리로 전환 중이라고 설명한다.
기존 등록 토큰 API를 사용하는 앱도 토큰이 바뀐다는 전제를 유지해야 한다.
토큰은 사용자 계정 자체의 영구 식별자나 비밀 인증 토큰으로 사용하지 않는다.

## 클라이언트 처리

`FirebaseMessagingService`를 구현하고 `onNewToken`에서 현재 토큰을 서버에 업로드한다.
앱 시작 시 현재 등록 값을 조회하는 흐름도 두어 서버와 클라이언트의 불일치를 줄인다.
업로드는 재시도 가능하게 만들고, 마지막 성공 시각과 앱 인스턴스 정보를 서버에 기록한다.
토큰 변경 시 기존 값은 교체하며 한 사용자에게 여러 기기가 연결될 수 있음을 고려한다.

```kotlin
override fun onNewToken(token: String) {
    registrationRepository.upsert(token)
}
```

## 토큰이 바뀔 수 있는 경우

- 앱을 새 기기로 복원하거나 재설치한 경우
- 앱 데이터를 삭제하거나 Firebase Installation이 재발급된 경우
- 보안 또는 서비스 내부 사유로 등록이 갱신된 경우
- 장기간 비활성으로 등록이 만료된 뒤 앱이 다시 연결된 경우

서버 전송 결과가 `UNREGISTERED`이면 해당 등록을 제거한다.
`INVALID_ARGUMENT`는 payload 오류일 수도 있으므로 요청 형식이 유효한 경우에만 등록 무효로 판단한다.

## 서버 정리 정책

등록 레코드에는 사용자 ID, 현재 식별자, 플랫폼, 앱 버전, 마지막 동기화 시각을 저장한다.
오래 사용되지 않은 등록과 반복 실패 등록은 별도 정책으로 비활성화한다.
Android 등록은 270일 비활성 후 FCM에서 만료될 수 있으므로 오류 응답을 정리 신호로 사용한다.
topic을 쓴다면 식별자 변경 시 재구독하고, 오래된 등록의 topic 매핑도 정리한다.

서버에 식별자를 저장할 때는 업로드 요청의 인증된 사용자와 대상 앱 인스턴스를 검증한다.
로그아웃 시 해당 사용자와의 매핑을 제거하거나 익명 상태로 전환한다.

## 참고

- [FCM 등록 관리 모범 사례](https://firebase.google.com/docs/cloud-messaging/manage-tokens)
- [Android FCM 시작하기](https://firebase.google.com/docs/cloud-messaging/android/get-started)
