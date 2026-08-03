---
title: Navigation 3 deep link: URI 에서 NavKey 로
tags: [android, android/navigation, android/navigation3]
aliases: ["Navigation 3 deep link: URI 에서 NavKey 로"]
date modified: 2026-08-03 16:37:07 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Navigation 3 deep link: URI 에서 NavKey 로

상위 문서: [Navigation 3 계약](01_inbox/mobile/android/02_app_framework/navigation/navigation3/navigation3-contracts/navigation3-contracts.md)

관련 노트: [Android 딥 링크는 외부 URI 계약이다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/deep-link-contracts/deep-link-is-external-uri-contract.md)

### 변환 위치

Android OS 가 deep link 를 전달하는 입구는 Activity 지만, 앱 내부 목적지는 `NavKey` 다.

따라서 `Intent.data` 를 받은 뒤 app layer 에서 URI 를 검증하고 typed key 로 변환한다.

feature 화면은 외부 URL schema 를 알지 않아도 된다.

```kotlin
fun Uri.toNavKeyOrNull(): NavKey? {
    if (scheme != "https" || host != "example.com") return null
    if (pathSegments.firstOrNull() != "training") return null
    val id = pathSegments.getOrNull(1) ?: return null
    return TrainingDetailRoute(id)
}
```

파싱 함수는 다음을 한 번에 처리한다.

- scheme 과 host 검증
- path segment 개수와 의미 검증
- query parameter 의 타입 변환
- 허용되지 않은 값의 거부
- 성공 시 route key 생성

문자열 URI 를 back stack 에 그대로 넣지 않는다.

URL 의 표현 방식은 바뀔 수 있지만 `TrainingDetailRoute` 같은 내부 계약은 앱이 통제해야 한다.

### 초기 stack 만들기

deep link 는 최종 목적지만 알리므로 필요한 synthetic root 를 앱이 직접 만든다.

```text
https://example.com/training/123
 -> TrainingRoute
 -> TrainingDetailRoute("123")
```

로그인 상태가 이미 유효하면 선택 destination 을 Training 으로 바꾸고 위 stack 을 렌더링한다.

로그인되지 않았다면 원래 목적지 key 를 pending 상태로 보관하고 인증 stack 을 먼저 보여준다.

인증 성공 뒤 pending key 를 검증한 다음 feature root 와 함께 적용한다.

잘못된 URI 는 빈 stack 이나 암묵적 예외로 끝내지 않는다.

기본 destination, 명시적 오류 화면, 또는 지원하지 않는 링크 안내 중 하나로 결정한다.

동일한 URI 가 반복 전달될 때 기존 화면 위에 중복 push 하지 않는 정책도 정한다.

Manifest intent filter 와 Android App Links 설정은 URI 수신을 담당한다.

수신 이후의 route 구성과 back 동작은 Navigation 3 앱 상태의 책임이다.

기본 구현 흐름은 [Navigation 3 deep link recipe](https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-basic) 에서 확인할 수 있다.

### 공식 문서

- [Navigation 3 Deep Link Basic Recipe](https://developer.android.com/guide/navigation/navigation-3/recipes/deeplinks-basic)
