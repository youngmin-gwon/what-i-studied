# Google Play Instant는 종료되었고 딥링크 중심 대안으로 전환한다

상위 문서: [Android 패키징과 배포 지도](01_inbox/mobile/android/03_packaging_deployment/android-packaging-deployment.md)
관련 지도: [Play Delivery 계약](01_inbox/mobile/android/03_packaging_deployment/distribution/play-delivery-contracts/play-delivery-contracts.md)
관련 정본: [AAB는 Play가 기기별 APK를 생성하는 게시 아티팩트다](01_inbox/mobile/android/03_packaging_deployment/distribution/release-distribution-contracts/aab-is-publishing-artifact-for-play-generated-apks.md)

## 현재 상태

Google Play Instant는 더 이상 신규 설계 대상으로 삼지 않는다.
Google 공식 안내에 따라 2025년 12월부터 Instant Apps는 Google Play를 통해
게시할 수 없고, Google Play services Instant API가 동작하지 않는다.
사용자에게 Play가 Instant Apps를 어떤 경로로도 제공하지 않는다.

따라서 `dist:instant="true"`를 새 기능 모듈에 추가하는 접근은 폐기한다.
기존 Instant 전용 모듈과 instant-enabled bundle은 마이그레이션 대상으로 분류한다.
과거의 용량 제한, instant와 on-demand 조합 같은 규칙은 신규 구현 기준이 아니다.

## 대체 사용자 여정

1. 웹 또는 광고 링크가 일반 앱의 의미 있는 목적지로 연결되게 한다.
2. Android App Links로 검증된 도메인과 앱 화면을 매핑한다.
3. 미설치 사용자는 Play 설치 화면으로 보내고, 설치 후 원래 목적지로 복귀시킨다.
4. 설치된 사용자는 앱의 특정 기능 화면으로 바로 이동시킨다.
5. 첫 실행에 필요한 기능만 install-time으로 남기고 나머지는 on-demand로 분리한다.

딥링크는 Instant Apps를 재현하는 것이 아니라, 설치 전후의 진입 경로를 단순화하는
대안이다. 링크 처리 실패, 인증, 앱 미설치, 이미 설치된 경우를 각각 테스트한다.

## 기존 앱 정리

- Instant 전용 manifest 선언과 release track을 식별한다.
- Instant API 호출과 런타임 분기 코드를 제거하거나 일반 앱 경로로 바꾼다.
- Instant에서만 접근 가능했던 화면의 설치 앱 동작을 정의한다.
- 링크는 일반 앱의 deep link 또는 App Links로 재검증한다.
- Play Console과 분석 이벤트에서 Instant 전용 지표를 분리 종료한다.

## 주의

현재 Android Developers의 Instant 문서는 역사적 동작과 종료 공지를 함께 담는다.
새 문서나 아키텍처에서 Instant를 활성 기능으로 소개하지 않는다.
종료 시점은 “2025년 12월부터”로 기록하며 “종료 예정”이라고 표현하지 않는다.

## 마이그레이션 완료 기준

- 일반 설치 앱에서 동일한 핵심 시나리오가 시작되고 완료된다.
- 앱이 설치되지 않은 링크 방문자는 설치 안내 후 원래 화면으로 돌아온다.
- 설치된 링크 방문자는 인증 상태를 보존한 채 대상 화면을 연다.
- Instant 전용 분석 이벤트는 일반 설치·딥링크 이벤트로 치환된다.
- 릴리스 bundle에 더 이상 Instant 전용 delivery 선언이 남지 않는다.

## 공식 문서

- [Overview of Google Play Instant](https://developer.android.com/topic/google-play-instant/overview)
- [Google Play Instant platform notice](https://developer.android.com/topic/google-play-instant)
- [Verify App Links](https://developer.android.com/training/app-links/verify-site-associations)
