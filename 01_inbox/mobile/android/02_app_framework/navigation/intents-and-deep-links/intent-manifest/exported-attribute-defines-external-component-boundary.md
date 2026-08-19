---
title: exported-attribute-defines-external-component-boundary
tags: [android, android/navigation, android/manifest, security]
aliases: ["Exported 속성은 외부 컴포넌트 경계를 정의한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Exported 속성은 외부 컴포넌트 경계를 정의한다

상위 문서: [Intent & Manifest 계약](intent-manifest.md)

---

### 개념과 필요성 (What & Why)

1. **개념 (What)**:
   - `AndroidManifest.xml`의 컴포넌트 선언부에 작성되는 **`android:exported`** 속성은 타 애플리케이션 프로세스나 안드로이드 시스템 외부가 해당 컴포넌트를 직접 실행(`startActivity`, `startService`, `sendBroadcast`)할 수 있는지 여부를 통제하는 **최우선 보안 경계 속성**이다.
2. **필요성 (Why)**:
   - **권한 우회 및 컴포넌트 인젝션 차단**: 앱 내부 전용 화면이나 서비스에 `exported="true"`가 실수로 기재되면, 악성 앱이 인텐트를 발송하여 인증 절차를 우회하고 내부 DB를 덤프하거나 관리자 화면으로 진입할 수 있다.
   - **Android 12 (API 31)+ 강제 규칙**: `<intent-filter>`를 포함하는 모든 컴포넌트는 `android:exported` 속성을 `true` 또는 `false`로 명시적으로 작성해야만 빌드 및 설치가 완료된다.

---

### 보안 판단 가이드라인 (How)

```xml
<!-- 1. 외부 앱 진입점 (론처, 딥링크 수신) -> exported="true" -->
<activity
    android:name=".MainActivity"
    android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>

<!-- 2. 앱 내부 전용 결제 처리 화면 -> exported="false" 필수 -->
<activity
    android:name=".InternalPaymentActivity"
    android:exported="false" />
```

---

### 관련 상위 및 연관 노트

- 상위 계약: [Intent & Manifest 계약](intent-manifest.md)
- 연관 계약: [AndroidManifest는 OS에 노출되는 컴포넌트와 진입점을 선언한다](android-manifest-declares-os-visible-components-and-entry-points.md)
