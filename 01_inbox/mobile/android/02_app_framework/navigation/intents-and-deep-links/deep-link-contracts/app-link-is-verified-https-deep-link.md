---
title: app-link-is-verified-https-deep-link
tags: []
aliases: []
date modified: 2026-07-31 18:20:58 +09:00
date created: 2026-07-31 17:13:53 +09:00
---

## Android App Link 는 검증된 HTTPS 딥 링크다

상위 문서: [Deep Link 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-contracts.md)

관련 노트: [매니페스트 선언과 assetlinks.json은 서로 다른 역할을 가진다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/manifest-and-assetlinks-have-distinct-roles.md)

### 정의

App Link 는 HTTPS 웹 URL 을 특정 Android 앱이 처리하도록 연결하는 딥 링크 방식이다.

일반 웹 딥 링크와 달리 Android 가 앱과 도메인의 관계를 검증한다.

검증이 성공하면 사용자가 매번 앱 선택기를 거치지 않고 앱으로 이동할 수 있다.

앱이 설치되지 않은 사용자는 같은 URL 을 웹에서 열 수 있다.

따라서 App Link 는 앱 전용 주소가 아니라 웹과 앱이 공유하는 URL 계약이다.

### 필요한 두 증거

앱 쪽에는 `VIEW`, `DEFAULT`, `BROWSABLE` 을 포함한 `intent-filter` 가 필요하다.

HTTPS scheme 과 처리할 host 및 path 도 필터에 선언해야 한다.

필터에 `android:autoVerify="true"` 를 지정하면 설치 또는 갱신 과정에서 검증을 요청한다.

서버 쪽에는 `/.well-known/assetlinks.json` 을 HTTPS 로 제공해야 한다.

파일은 앱 패키지 이름과 서명 인증서 SHA-256 지문을 연결한다.

Android 는 두 선언이 일치하는지 확인한 뒤 도메인 소유 관계를 신뢰한다.

### 일반 딥 링크와의 차이

custom scheme 은 앱이 등록할 수 있지만 다른 앱이 같은 scheme 을 등록할 수 있다.

따라서 custom scheme 은 앱 사칭이나 모호한 앱 선택 문제를 피하기 어렵다.

App Link 는 조직이 통제하는 HTTPS 도메인과 인증서 지문을 함께 사용한다.

도메인 검증은 URI 를 만든 주체와 앱 패키지의 관계를 확인하는 보안 경계다.

단, 검증은 사용자의 로그인이나 서버 권한을 대신하지 않는다.

앱에 전달된 URI 의 리소스 접근 권한은 앱과 서버가 별도로 검사해야 한다.

### 운영 시 주의점

debug 와 release 서명 인증서 지문이 다르면 개발 환경과 배포 환경의 결과도 달라진다.

여러 앱 변형이 같은 도메인을 처리한다면 assetlinks.json 에 각 대상을 명시해야 한다.

리디렉션, 잘못된 MIME 타입, TLS 오류, 404 응답은 검증 실패 원인이 될 수 있다.

도메인의 모든 경로를 앱으로 열 것인지 제품 정책으로 먼저 결정한다.

앱으로 처리하지 않을 경로는 웹에서 계속 정상 동작해야 한다.

### 구현 흐름

URI 목적지는 [Android 딥 링크는 외부 URI 계약이다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-is-external-uri-contract.md) 에서 정의한다.

매니페스트와 서버 파일의 대응 관계는 [매니페스트 선언과 assetlinks.json의 역할](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/manifest-and-assetlinks-have-distinct-roles.md) 에서 확인한다.

정식 설정 절차는 [App Links 추가](https://developer.android.com/training/app-links/add-applinks) 를 따른다.

서버 파일의 형식은 [assetlinks.json 구성](https://developer.android.com/training/app-links/configure-assetlinks) 을 기준으로 검토한다.

### 결론

App Link 의 핵심은 HTTPS 라는 문자열이 아니라 검증 가능한 소유 관계다.

매니페스트 선언만으로는 App Link 가 완성되지 않는다.

서버 파일만으로도 앱이 새로운 host 를 받을 수는 없다.

두 증거와 앱 내부 라우팅이 함께 맞아야 안정적인 외부 진입점이 된다.

### 공식 문서

- [About App Links](https://developer.android.com/training/app-links/about)
- [Add Intent filters for App Links](https://developer.android.com/training/app-links/add-applinks)
