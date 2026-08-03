---
title: package-visibility-limits-which-apps-can-be-queried
tags: [android, android/intents, android/navigation]
aliases: ["Package visibility 는 다른 앱 조회 범위를 제한한다"]
date modified: 2026-08-03 18:11:46 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Package visibility 는 다른 앱 조회 범위를 제한한다

상위 문서: [Intent와 Manifest 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md)

### 문제

Android 11 부터 앱은 설치된 모든 앱의 존재를 무제한으로 조회하기 어렵다.

이는 앱 목록 수집과 지문 추적을 줄이기 위한 패키지 가시성 제한이다.

Intent 를 실제로 실행하는 것과 처리 앱의 존재를 조회하는 것은 서로 다른 문제다.

### `<queries>` 선언

앱이 특정 패키지나 특정 Intent 처리 앱을 조회해야 하면 Manifest 에 이유를 선언한다.

```xml
<manifest ...>
    <queries>
        <package android:name="com.example.partner" />
        <intent>
            <action android:name="android.intent.action.SEND" />
            <data android:mimeType="image/*" />
        </intent>
    </queries>
</manifest>
```

`<package>` 는 특정 패키지를 대상으로 한다.

`<intent>` 는 특정 작업을 처리할 수 있는 앱을 대상으로 한다.

ContentProvider 를 조회해야 하는 경우에는 provider authority 를 선언할 수 있다.

### 실행과 조회를 구분하기

사용자에게 웹 링크나 공유 대상을 열어 주는 Intent 실행은 일반적인 계약을 따른다.

하지만 사전에 `resolveActivity()` 나 `queryIntentActivities()` 로 목록을 조사하면 가시성 영향을 받을 수 있다.

따라서 필요 이상의 앱 목록을 수집하지 말고 실제 기능에 필요한 조회만 선언한다.

`QUERY_ALL_PACKAGES` 는 일반적인 해결책이 아니다.

Google Play 에서는 런처, 보안 앱처럼 핵심 기능상 광범위 조회가 필요한 앱에 제한적으로 허용된다.

### 설계 점검

1. 정말 설치 여부를 알아야 하는가?
2. 직접 호출 대신 Intent 실행과 실패 처리로 충분한가?
3. 조회 대상은 특정 패키지인가, 특정 작업을 처리하는 앱인가?
4. 선언한 `<queries>` 가 실제 기능과 최소 범위로 일치하는가?
5. Android 11 이상과 낮은 버전에서 동작 차이를 테스트했는가?

### 정리

Package visibility 는 앱 간 연동을 막는 기능이 아니라 불필요한 앱 탐색을 줄이는 정책이다.

조회가 필요할 때는 `<queries>` 로 의도를 명시하고, 광범위 권한은 정책과 기능 요구를 함께 검토한다.
