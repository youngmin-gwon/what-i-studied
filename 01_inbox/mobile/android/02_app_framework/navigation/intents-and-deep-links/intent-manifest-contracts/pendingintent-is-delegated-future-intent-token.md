---
title: pendingintent-is-delegated-future-intent-token
tags: [android, android/intents, android/navigation]
aliases: ["PendingIntent 는 나중에 실행할 권한을 위임하는 토큰이다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## **PendingIntent**(외부 시스템 프로세스가 미래 시점에 미리 설정된 Intent를 내 앱의 권한으로 실행하도록 위임하는 보안 토큰) 는 나중에 실행할 권한을 위임하는 토큰이다

상위 문서: [Intent와 Manifest 계약](intent-manifest-contracts.md)

배경 지식: [인증과 인가](../../../../../../security/fundamentals/authentication-authorization.md)

### 개념

PendingIntent 는 다른 앱이나 시스템이 나중에 앱 대신 Intent 를 실행할 수 있게 하는 토큰이다.

알림 클릭, AlarmManager, 위젯, 시스템 UI 와의 연동에서 주로 사용한다.

일반 Intent 가 즉시 요청 메시지라면 PendingIntent 는 미래 실행 권한을 나타낸다.

```kotlin
val intent = Intent(context, MainActivity::class.java)
val pendingIntent = PendingIntent.getActivity(
    context,
    100,
    intent,
    PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT
)
```

### 불변성과 가변성

Android 12 부터 PendingIntent 생성 시 `FLAG_IMMUTABLE` 또는 `FLAG_MUTABLE` 을 명시해야 한다.

대부분의 알림 이동은 수신자가 Intent 를 바꿀 필요가 없으므로 `FLAG_IMMUTABLE` 을 사용한다.

인라인 답장처럼 시스템이 실행 시 입력을 채워야 하는 특별한 경우에만 mutable 을 검토한다.

mutable 토큰은 수정 가능한 범위와 호출자를 더 엄격하게 분석해야 한다.

### 토큰 식별과 재사용

request code, 대상 컴포넌트, Intent 필드에 따라 기존 PendingIntent 와 동일성이 결정될 수 있다.

`FLAG_UPDATE_CURRENT` 는 기존 토큰의 extras 를 갱신할 때 사용한다.

`FLAG_ONE_SHOT` 은 한 번 실행한 뒤 재사용되지 않도록 한다.

사용자나 리소스 식별자가 바뀌면 토큰이 잘못 재사용되지 않는지 확인한다.

### 보안 점검

민감한 작업은 명시적 Intent 를 사용해 대상 컴포넌트를 고정한다.

토큰에 비밀번호나 장기 비밀값을 넣지 말고 필요한 식별자만 전달한다.

수신 화면은 PendingIntent 를 통해 들어온 extras 도 다시 검증해야 한다.

알림에 노출되는 제목과 내용은 잠금 화면 공개 정책도 고려한다.

### 흔한 실수

1. Android 12 에서 mutability flag 를 빠뜨려 예외가 발생한다.
2. mutable 을 기본값처럼 사용해 Intent 변조 가능성을 키운다.
3. `FLAG_UPDATE_CURRENT` 와 request code 조합을 잘못해 다른 사용자 데이터로 갱신한다.
4. 토큰이 열어 주는 작업에 인증 검사를 두지 않는다.

### 정리

PendingIntent 는 단순히 Intent 를 저장하는 객체가 아니라 실행 권한의 위임 수단이다.

누가 언제 어떤 대상에 어떤 입력으로 실행할 수 있는지까지 포함해 보안 계약을 설계한다.
