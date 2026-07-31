---
title: dynamic-app-links-refine-but-do-not-expand-manifest-scope
tags: []
aliases: []
date modified: 2026-07-31 18:21:51 +09:00
date created: 2026-07-31 17:13:53 +09:00
---

## Dynamic App Links 는 선언 범위를 확장하지 않는다

상위 문서: [Deep Link 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-contracts.md)

관련 정본: [매니페스트 선언과 assetlinks.json은 서로 다른 역할을 가진다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/manifest-and-assetlinks-have-distinct-roles.md)

### 개념

Android 15(API 35)부터 assetlinks.json 에 동적 URL 규칙을 둘 수 있다.

이 규칙은 앱 업데이트 없이 서버가 기존 App Link 범위를 세밀하게 조정하도록 돕는다.

예를 들어 특정 path 를 제외하거나 query 조건을 더 구체적으로 만들 수 있다.

웹 라우팅 정책이 자주 바뀌는 서비스에서 배포 지연을 줄이는 데 유용하다.

### 가장 중요한 제한

Dynamic App Links 는 매니페스트에 이미 선언된 범위 안에서만 동작한다.

서버 파일은 앱 매니페스트에 없는 새로운 host 를 추가할 수 없다.

매니페스트가 `/product` 만 선언했다면 서버 규칙도 그 정적 상한을 넘을 수 없다.

따라서 미래의 동적 확장을 고려해 매니페스트의 host 와 scheme 을 먼저 설계해야 한다.

다만 처음부터 지나치게 넓은 path 를 선언하면 의도하지 않은 URL 처리 위험이 생긴다.

### 정적 상한과 동적 세부 규칙

매니페스트는 설치된 앱 버전이 알고 있는 도메인과 큰 URL 표면을 제공한다.

assetlinks.json 은 해당 표면에서 현재 처리할 path, query, 제외 패턴을 조정한다.

정적 선언은 앱 업데이트가 있어야 바뀌지만 동적 규칙은 서버 배포로 바꿀 수 있다.

동적 규칙이 제거되거나 검증에 실패할 때의 fallback 도 제품적으로 정의해야 한다.

웹 URL 은 앱 연결이 사라져도 브라우저에서 의미 있는 결과를 제공해야 한다.

### 운영 모델

동적 규칙을 배포하기 전에 구버전 Android 와 미지원 클라이언트의 동작을 확인한다.

규칙 변경은 앱 화면 라우터가 예상하는 path 와 함께 버전 관리한다.

긴급 제외는 서버에서 할 수 있지만 이미 열린 화면의 상태를 되돌리지는 않는다.

캐시와 재검증 주기를 고려해 변경이 즉시 모든 기기에 반영된다고 가정하지 않는다.

로그에는 매칭된 URI 와 앱 버전, 검증 상태를 남기되 개인정보는 최소화한다.

### 예시적 정책

`/product/*` 는 앱으로 열고 `/product/preview/*` 는 웹에 남길 수 있다.

`campaign=summer` 같은 query 조건은 마케팅 URL 의 일부 흐름에만 적용할 수 있다.

그러나 새 `/account/*` host 또는 별도 도메인을 서버 파일만으로 추가할 수는 없다.

새 host 가 필요하면 매니페스트와 앱 배포를 함께 변경해야 한다.

### 연결 문서

정적 선언의 기준은 [매니페스트 선언과 assetlinks.json의 역할](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/manifest-and-assetlinks-have-distinct-roles.md) 이다.

App Links 의 전체 개념은 [Android App Link는 검증된 HTTPS 딥 링크다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/app-link-is-verified-https-deep-link.md) 에서 확인한다.

공식 개요는 [Android App Links 개요](https://developer.android.com/training/app-links/about) 를 참고한다.

### 결론

Dynamic App Links 는 서버 주도 refinement 다.

앱의 선언 상한을 늘리는 권한 위임이 아니다.

이 제한을 지켜야 서버 정책 변경이 앱의 의도하지 않은 외부 표면 확장으로 이어지지 않는다.

### 공식 문서

- [Add Intent filters for App Links](https://developer.android.com/training/app-links/add-applinks)
- [Configure website associations and dynamic rules](https://developer.android.com/training/app-links/configure-assetlinks)
