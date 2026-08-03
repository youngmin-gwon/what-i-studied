---
title: exported는 컴포넌트의 외부 호출 경계를 결정한다
tags: [android, android/intents, android/navigation]
aliases: ["exported 는 컴포넌트의 외부 호출 경계를 결정한다"]
date modified: 2026-08-03 16:36:30 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# exported는 컴포넌트의 외부 호출 경계를 결정한다

상위 문서: [Intent와 Manifest 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md)

관련 노트: [intent-filter는 컴포넌트의 수신 계약이다](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-filter-is-component-receiving-contract.md)

### 의미

`android:exported` 는 다른 앱이 컴포넌트를 직접 실행할 수 있는지를 나타낸다.

`true` 인 컴포넌트는 외부 호출 가능성이 있으므로 입력과 권한을 공개 API 처럼 다룬다.

`false` 인 컴포넌트는 앱 내부 호출로 범위를 제한한다.

```xml
<activity
    android:name=".DeepLinkActivity"
    android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
    </intent-filter>
</activity>
```

### 필터와의 관계

외부에서 받아야 하는 런처나 딥 링크 진입점은 보통 `true` 여야 한다.

내부 전용 액티비티, 서비스, 리시버는 명시적으로 `false` 로 선언한다.

최근 target SDK 에서는 필터가 있는 컴포넌트의 exported 값을 명시하지 않으면 빌드가 실패할 수 있다.

필터가 없더라도 exported 가 true 이면 다른 앱의 명시적 호출 대상이 될 수 있다.

### 보안 경계로 다루기

exported 컴포넌트의 Intent 는 신뢰할 수 없는 입력으로 취급한다.

URI scheme, host, path, MIME 타입, extras 를 각각 검증한다.

사용자 인증과 리소스 소유권 검사는 진입점 안에서 수행한다.

민감한 컴포넌트에는 permission 을 요구하거나 외부 공개 자체를 제거한다.

```kotlin
val uri = intent.data ?: return finish()
val allowed = uri.scheme == "https" &&
    uri.host == "example.com" &&
    uri.path?.startsWith("/orders/") == true
if (!allowed) return finish()
```

### 흔한 실수

1. 딥 링크 액티비티를 exported=true 로 만들고 인증 검사를 생략한다.
2. 브로드캐스트 수신 컴포넌트에서 호출자와 payload 를 검증하지 않는다.
3. 내부 서비스에 필터를 붙여 외부 호출 표면을 넓힌다.
4. 명시적 Intent 라는 이유만으로 외부 호출 입력을 신뢰한다.

### 정리

`exported` 는 단순한 배포 옵션이 아니라 프로세스 밖으로 경계를 여는 선언이다.

공개가 필요하면 필터, permission, 입력 검증을 함께 설계하고 공개가 필요 없으면 닫는다.
