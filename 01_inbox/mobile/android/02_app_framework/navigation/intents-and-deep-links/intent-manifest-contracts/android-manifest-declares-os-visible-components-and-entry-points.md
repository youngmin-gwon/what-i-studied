---
title: AndroidManifest.xml은 OS 에 앱의 컴포넌트를 선언한다
tags: [android, android/intents, android/navigation]
aliases: ["AndroidManifest.xml 은 OS 에 앱의 컴포넌트를 선언한다"]
date modified: 2026-08-03 16:36:28 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# AndroidManifest.xml은 OS 에 앱의 컴포넌트를 선언한다

상위 문서: [Intent와 Manifest 계약](01_inbox/mobile/android/02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md)

### 매니페스트의 본질

AndroidManifest.xml 은 개발자와 Android OS 사이의 설치·실행 계약이다.

앱 코드가 존재하는 것만으로 OS 가 모든 컴포넌트를 실행할 수 있는 것은 아니다.

OS 는 매니페스트를 읽고 앱의 컴포넌트, 권한, 진입점, 메타데이터를 파악한다.

### 대표적인 선언

| 요소 | OS 가 알아야 하는 내용 |
| --- | --- |
| `<uses-permission>` | 앱이 요청하는 보호 자원 |
| `<application>` | 앱 공통 이름, 테마, 설정 |
| `<activity>` | 화면과 외부 진입점 |
| `<service>` | 백그라운드 작업 컴포넌트 |
| `<receiver>` | 브로드캐스트 수신 컴포넌트 |
| `<provider>` | ContentProvider 와 데이터 경계 |
| `<intent-filter>` | 암시적 Intent 수신 조건 |
| `<queries>` | 앱이 조회할 패키지 범위 |

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android">
    <uses-permission android:name="android.permission.INTERNET" />
    <application android:theme="@style/Theme.App">
        <activity android:name=".MainActivity" android:exported="true" />
    </application>
</manifest>
```

### 설치와 실행에서의 역할

설치 시 패키지 관리자는 매니페스트 정보를 사용해 앱을 등록한다.

런처는 `MAIN` 과 `LAUNCHER` 필터를 보고 시작 화면을 찾을 수 있다.

다른 앱의 링크나 공유 요청은 등록된 필터를 기준으로 후보를 찾는다.

권한과 exported 설정은 다른 UID 의 호출이 가능한지 판단하는 입력이 된다.

### 코드와 매니페스트의 경계

매니페스트는 공개된 구조와 OS 수준 정책을 선언한다.

세부 비즈니스 권한, 사용자 로그인, 리소스 소유권은 코드에서 다시 확인해야 한다.

매니페스트에 링크를 등록했다고 해당 링크의 모든 사용자가 인증된 것은 아니다.

반대로 코드에 액티비티를 만들었어도 매니페스트에 등록하지 않으면 OS 진입점이 아니다.

### 정리

매니페스트는 설정 파일을 넘어 앱이 OS 에 노출하는 컴포넌트 경계다.

Intent 라우팅, 권한, 패키지 가시성은 모두 이 선언과 실행 코드의 조합으로 결정된다.
