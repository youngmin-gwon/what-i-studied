---
title: fcm-registration-identifier-targets-app-instance-not-user-account
tags: ["android", "android/system-services"]
aliases: []
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 17:42:24 +09:00
---

## FCM 등록 식별자는 사용자 계정이 아니라 앱 인스턴스를 가리킨다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)

관련 지도: [알림과 FCM 메시징 계약](./notification-messaging-contracts.md)

관련 노트: [FCM은 메시지 전송 서비스이지 비즈니스 실행 보장이 아니다](./fcm-is-message-delivery-not-business-execution-guarantee.md)

### 식별자의 의미

FCM 등록 식별자는 특정 앱 설치 또는 앱 인스턴스로 메시지를 보내기 위한 대상 값이다.

2026-08-03 기준 Firebase 문서는 **FID**(Firebase Installation ID, 앱 인스턴스 고유 식별자) 기반 등록으로 전환 중이며 FID 방식과 legacy registration token 방식을 함께 지원한다.

새 구현은 FID 기반 API 를 우선하고, 기존 구현은 legacy token 의 갱신·폐기 규칙을 별도 경로로 유지한다.

FID 와 token 어느 쪽도 사용자 계정 자체의 영구 식별자나 비밀 인증 자격으로 사용하지 않는다.

### 클라이언트 처리

- FID 기반 자동 초기화에서는 `onRegistered(installationId)` 콜백으로 등록 값을 서버에 업로드하고 갱신 시각을 함께 저장한다.
- 자동 초기화를 끈 경우 앱 시작 시 `register()` 를 호출해 등록 흐름과 콜백을 명시적으로 시작한다.
- legacy token API 를 유지하는 앱은 `onNewToken` 과 현재 token 조회·주기 갱신을 기존 SDK 버전에 맞춰 처리한다.
- 두 API 세대의 callback 과 서버 필드 이름을 한 경로에 섞지 말고, 마이그레이션 기간에는 등록 종류를 함께 저장한다.
- 한 사용자에게 여러 앱 인스턴스가 연결될 수 있으며 로그아웃은 사용자 매핑을 끊는 동작이지 FCM 등록 자체의 인증 폐기를 의미하지 않는다.

### 토큰이 바뀔 수 있는 경우

- 앱을 새 기기로 복원하거나 재설치한 경우
- 앱 데이터를 삭제하거나 Firebase Installation 이 재발급된 경우
- 보안 또는 서비스 내부 사유로 등록이 갱신된 경우
- 장기간 비활성으로 등록이 만료된 뒤 앱이 다시 연결된 경우

서버 전송 결과가 `UNREGISTERED` 이면 해당 등록을 제거한다.

`INVALID_ARGUMENT` 는 payload 오류일 수도 있으므로 요청 형식이 유효한 경우에만 등록 무효로 판단한다.

### 서버 정리 정책

등록 레코드에는 사용자 ID, 현재 식별자, 등록 방식, 플랫폼, 앱 버전, 마지막 동기화 시각을 저장한다.

오래 사용되지 않은 등록과 반복 실패 등록은 별도 정책으로 비활성화한다.

Android 등록은 270 일 비활성 후 FCM 에서 만료될 수 있으므로 오류 응답을 정리 신호로 사용한다.

topic 을 쓴다면 식별자 변경 시 재구독하고, 오래된 등록의 topic 매핑도 정리한다.

서버에 식별자를 저장할 때는 업로드 요청의 인증된 사용자와 대상 앱 인스턴스를 검증한다.

로그아웃 시 해당 사용자와의 매핑을 제거하거나 익명 상태로 전환한다.

### 참고

- [FCM 등록 관리 모범 사례](https://firebase.google.com/docs/cloud-messaging/manage-tokens)
- [Android FCM 시작하기](https://firebase.google.com/docs/cloud-messaging/android/get-started)

검증일: 2026-08-03. FID 전환 문서는 계속 변경 중이므로 사용하는 Firebase Messaging SDK 의 실제 callback/API 와 공식 마이그레이션 안내를 함께 확인한다.