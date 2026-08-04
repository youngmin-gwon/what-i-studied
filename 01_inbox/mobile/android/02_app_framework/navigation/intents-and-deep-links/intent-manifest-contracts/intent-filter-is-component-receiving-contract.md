---
title: intent-filter-is-component-receiving-contract
tags: [android, android/intents, android/navigation]
aliases: ["intent-filter 는 컴포넌트의 수신 계약이다"]
date modified: 2026-08-03 18:11:38 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## intent-filter 는 컴포넌트의 수신 계약이다

상위 문서: [Intent와 Manifest 계약](./intent-manifest-contracts.md)

관련 노트: [AndroidManifest는 OS가 발견할 컴포넌트와 진입점을 선언한다](./android-manifest-declares-os-visible-components-and-entry-points.md)

### 역할

`intent-filter` 는 컴포넌트가 어떤 암시적 Intent 를 받을 수 있는지 선언한다.

필터는 코드가 아니라 AndroidManifest 에 기록되며 OS 의 Intent 해석에 사용된다.

따라서 필터는 "이 컴포넌트를 어떻게 실행하는가"보다 "어떤 요청을 받을 것인가"에 가깝다.

```xml
<activity
    android:name=".ShareActivity"
    android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.SEND" />
        <category android:name="android.intent.category.DEFAULT" />
        <data android:mimeType="text/plain" />
    </intent-filter>
</activity>
```

### 필터와 명시적 호출의 차이

명시적 Intent 는 필터가 없어도 대상 컴포넌트를 직접 지정할 수 있다.

암시적 Intent 는 필터가 있어야 시스템이 후보를 찾을 수 있다.

필터를 추가하면 앱 외부에서 접근 가능한 진입점이 될 수 있으므로 공개 범위를 검토한다.

### 필터의 세 가지 축

`action` 은 요청의 작업 종류를 나타낸다.

`category` 는 호출 맥락과 실행 환경을 나타낸다.

`data` 는 URI 와 MIME 타입이라는 처리 대상을 나타낸다.

일반적인 암시적 액티비티 호출에는 `DEFAULT` 카테고리가 필요하다.

웹 링크 진입점에는 보통 `BROWSABLE` 과 `https` 데이터 조건을 함께 선언한다.

### 선언 시 주의점

필터 안의 여러 `action` 은 해당 필터가 여러 작업을 받을 수 있다는 의미다.

데이터 선언을 넓게 잡으면 예상하지 못한 링크나 파일까지 수신할 수 있다.

서로 독립적인 계약은 여러 필터로 나누어 의도를 분명하게 만드는 편이 낫다.

`android:exported` 는 필터의 존재만으로 추론하지 말고 명시적으로 작성한다.

### 수신 측 구현

수신 액티비티는 `intent.action`, `intent.data`, `intent.type` 을 확인한다.

`extras` 는 호출자 입력이므로 null, 타입, 길이, 허용 목록을 검증한다.

필터가 링크를 허용해도 모든 path 가 동일한 기능 권한을 가져야 하는 것은 아니다.

로그인이나 소유권 검사가 필요한 리소스는 진입 후 별도로 인증한다.

### 정리

intent-filter 는 라우팅 표이자 공개된 입력 계약이다.

작동하는 예제보다 앱이 실제로 받을 필요가 있는 요청만 정확히 표현하는 것이 중요하다.

### 공식 문서

- [Intents and intent filters](https://developer.android.com/guide/components/intents-filters)
- [IntentFilter API reference](https://developer.android.com/reference/android/content/IntentFilter.html)
