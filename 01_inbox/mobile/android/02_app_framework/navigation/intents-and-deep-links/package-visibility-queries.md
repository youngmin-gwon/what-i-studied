---
title: package-visibility-queries
tags: [android, android/navigation, android/manifest, security]
aliases: ["Package visibility는 조회 가능한 앱을 제한한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Package visibility 는 조회 가능한 앱을 제한한다

상위 문서: [Intent & Manifest 계약](intent-manifest.md)

---

### 개념과 필요성 (What & Why)

1. **개념 (What)**:
   - Android 11 (API level 30)부터 도입된 **Package Visibility (패키지 가시성)** 정책은, 앱이 디바이스에 설치된 타 애플리케이션 패키지 목록을 무분별하게 조회(`PackageManager.queryIntentActivities()`)하는 것을 제한하는 보안 정책이다.
2. **필요성 (Why)**:
   - 악성 앱이 기기에 설치된 모든 앱 리스트(백킹 앱, 데이팅 앱 등)를 수집하여 사용자 개인정보를 스크래핑하는 프라이버시 침해를 방지한다.

---

### Manifest `<queries>` 선언 예시 (How)

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <!-- 앱이 조회 및 인텐트 발송을 허용할 타겟 패키지 및 인텐트 명시 -->
    <queries>
        <!-- 1. 명시적 패키지 지정 -->
        <package android:name="com.example.store" />
        <!-- 2. 암시적 인텐트 스키마 지정 (예: 웹 브라우저 앱 조회) -->
        <intent>
            <action android:name="android.intent.action.VIEW" />
            <data android:scheme="https" />
        </intent>
    </queries>
</manifest>
```

---

### 관련 상위 및 연관 노트

- 상위 계약: [Intent & Manifest 계약](intent-manifest.md)
- 연관 가이드: [Android Intent 및 IPC 종합 가이드](android-intent-and-ipc.md)
