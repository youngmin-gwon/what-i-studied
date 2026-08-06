---
title: exported-and-permission-boundaries-decide-external-component-access
tags: [android, android/app-components, android/architecture, android/security]
aliases: ["Exported와 permission 경계는 외부 접근을 결정한다"]
date modified: 2026-08-06 15:03:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Exported와 permission은 외부 호출 가능성과 호출자 권한을 함께 결정한다

`android:exported="false"`는 기본적인 내부 component 경계다. 외부 진입이 제품 요구사항이면 `true`로 열되, 민감한 기능은 manifest permission과 입력 검증을 추가한다. intent filter는 어떤 Intent를 해석할지 선언하는 routing 정보이지 authorization 규칙이 아니다.

### 안전한 최소 manifest

```xml
<permission
    android:name="com.example.permission.SEND_PARTNER_EVENT"
    android:protectionLevel="signature" />

<application ...>
    <service
        android:name=".InternalSyncService"
        android:exported="false" />

    <receiver
        android:name=".PartnerEventReceiver"
        android:exported="true"
        android:permission="com.example.permission.SEND_PARTNER_EVENT">
        <intent-filter>
            <action android:name="com.example.PARTNER_EVENT" />
        </intent-filter>
    </receiver>
</application>
```

signature permission은 같은 signing certificate를 가진 caller로 범위를 줄인다. exported component는 permission이 있어도 action, URI authority/path, enum, ID ownership과 payload 크기를 불신 입력으로 검증한다. caller identity가 중요한 Binder API는 `Binder.getCallingUid()`와 permission check를 entry thread에서 수행한다.

### Android 12의 실패 시점

target 31+에서 intent filter가 있는 Activity·Service·Receiver에 `android:exported`가 없으면 최신 toolchain은 보통 설치 단계가 아니라 manifest merge/build 단계에서 `Manifest merger failed`를 낸다. 오래된 toolchain으로 APK가 만들어진 예외적 경우 Android 12+ 설치에서 거부될 수 있다.

### 실패·관찰 신호

- Android Studio의 Merged Manifest에서 library가 추가한 intent filter와 최종 `exported` 값을 확인한다.
- `adb shell am start -n <package>/.InternalActivity`가 `Permission Denial`로 실패해야 내부 경계가 닫힌 것이다.
- exported endpoint에 permission이 없고 앱 권한으로 파일 삭제·결제·설정 변경을 수행하면 confused-deputy 취약점이다.
- lint의 exported component 경고와 manifest merger error를 보안 회귀 신호로 CI에서 실패시킨다.

상위 문서: [App Component Contracts](./app-component-contracts.md)

공식 문서: [Android 12 safer component exporting](https://developer.android.com/about/versions/12/behavior-changes-12#exported), [`android:exported` security risk](https://developer.android.com/privacy-and-security/risks/android-exported), [Access control for exported components](https://developer.android.com/privacy-and-security/risks/access-control-to-exported-components)
