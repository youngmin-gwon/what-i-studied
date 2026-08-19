---
title: packagemanager-queries-are-limited-by-package-visibility
tags: ["android", "android/system-services"]
aliases: ["PackageManager 조회는 Android 11부터 패키지 가시성 제한을 받는다"]
date modified: 2026-08-06 14:59:18 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## PackageManager 조회는 Android 11부터 패키지 가시성 제한을 받는다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [패키지/사용자/역할 조회 계약](./package-user-role.md)

### 핵심 정의

Android 11(API 30)부터 `PackageManager`의 `getInstalledPackages()`, `getInstalledApplications()`, `queryIntentActivities()` 같은 조회 API는 기본적으로 기기에 설치된 다른 앱을 모두 보여주지 않는다. 앱은 매니페스트의 `<queries>` 요소로 조회하고 싶은 패키지, 인텐트, provider authority를 명시적으로 선언해야 한다.

### 메커니즘

이 제한은 개인정보 보호를 위해 도입됐다. 사용자 기기에 설치된 전체 앱 목록은 사용자의 관심사 등을 추론하는 지문(fingerprint)으로 악용될 수 있기 때문이다. `<queries>`와 자동 가시성 규칙에 포함되지 않은 패키지는 조회 API에서 "설치되어 있지 않은 것"처럼 보인다. 자기 앱, 설치한 앱, 일부 시스템 패키지와 내 activity를 `startActivityForResult()`로 연 앱 등은 자동으로 보이지만, 단순히 과거에 임의의 명시적 인텐트를 주고받았다는 이유만으로 항상 보이는 것은 아니다.

`QUERY_ALL_PACKAGES` permission으로 전체 조회를 우회할 수 있지만 Play 정책상 제한적으로만 승인되며, 대부분의 통상적인 상호운용 목적(공유 대상 앱 목록 등)에는 사용이 거부된다.

### 판단 기준

- 특정 앱과의 연동(딥링크 처리 여부 확인, 특정 브라우저 존재 확인)이 필요하면 대상 패키지명 또는 인텐트 필터를 `<queries>`에 구체적으로 선언한다.
- "설치된 모든 앱 목록"이 정말 제품 요구사항인지 다시 검토한다. 대부분의 경우 특정 카테고리의 인텐트 필터 조회로 대체 가능하다.
- `<queries>`를 과도하게 넓게 선언하면(예: 모든 `ACTION_VIEW` 인텐트) Play 심사에서 사유 소명을 요구받을 수 있다.

### 최소 선언과 호출 흐름

조회하려는 상호운용 계약만 매니페스트에 적는다. 다음 예는 HTTPS 처리기를 찾는 경우다.

```xml
<manifest ...>
    <queries>
        <intent>
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.BROWSABLE" />
            <data android:scheme="https" />
        </intent>
    </queries>
</manifest>
```

```kotlin
val intent = Intent(Intent.ACTION_VIEW, Uri.parse("https://example.com"))
val visibleHandlers = packageManager.queryIntentActivities(
    intent,
    PackageManager.ResolveInfoFlags.of(0) // API 33+
)

try {
    startActivity(intent) // 시작 자체는 조회 가시성이 없어도 시도할 수 있다.
} catch (_: ActivityNotFoundException) {
    showNoHandlerFallback()
}
```

조회 결과가 비었다고 설치되지 않았다고 확정하지 않는다. "사전 발견"이 제품에 필요할 때만 `<queries>`를 추가하고, 단순 실행은 `ActivityNotFoundException`을 처리하는 흐름이 더 좁다.

### 경계

- 이 노트는 다른 앱을 조회하는 시점의 가시성 제한을 다룬다. 사용자/work profile 분리는 [UserManager는 여러 사용자와 work profile을 별도 UserHandle로 다룬다](./user-manager-userhandle.md)가 다룬다.
- 앱 설치/업데이트 자체의 흐름(서명, 배포)은 `03_packaging_deployment`가 다룬다.

### 관찰 가능한 신호

필터된 대상은 `queryIntentActivities()`의 누락이나 `getPackageInfo()`의 `NameNotFoundException`으로 나타날 수 있다. 디버그 기기에서 `adb shell pm log-visibility --enable <pkg>`를 켜면 Logcat의 `AppsFilter ... BLOCKED`를 관찰할 수 있고, `adb shell dumpsys package queries`로 자동 가시성 관계를 대조할 수 있다. 테스트 후 visibility 로그는 다시 끈다.

### 공식 문서

- https://developer.android.com/training/package-visibility
- https://developer.android.com/training/package-visibility/declaring
- https://developer.android.com/training/package-visibility/automatic
- https://developer.android.com/training/package-visibility/testing

검증일: 2026-08-06. 패키지 조회와 activity 시작은 같은 계약이 아니며, `startActivity()`는 대상이 조회에 보이지 않아도 시도할 수 있다는 공식 가이드를 반영했다.
