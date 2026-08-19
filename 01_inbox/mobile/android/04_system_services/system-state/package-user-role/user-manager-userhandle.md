---
title: usermanager-separates-users-and-work-profiles-by-userhandle
tags: ["android", "android/system-services"]
aliases: ["UserManager는 여러 사용자와 work profile을 별도 UserHandle로 다룬다"]
date modified: 2026-08-06 14:59:18 +09:00
date created: 2026-08-03 17:29:24 +09:00
---

## UserManager는 여러 사용자와 work profile을 별도 UserHandle로 다룬다

상위 문서: [Android 시스템 서비스와 기기 기능 지도](../../android-system-services-and-device-capabilities.md)
관련 지도: [패키지/사용자/역할 조회 계약](./package-user-role.md)

### 핵심 정의

Android는 한 기기에서 여러 개의 격리된 사용자 공간(다중 사용자, 게스트, work profile)을 지원한다. 각 사용자 공간은 **UserHandle**(OS 수준의 프로필/사용자 식별 핸들)로 식별되며, 같은 앱이라도 서로 다른 `UserHandle`에 각각 별도의 데이터·프로세스·UID 공간을 갖는 인스턴스로 설치될 수 있다.

### 메커니즘

work profile(관리형 프로필)은 개인 공간과 별도의 UserHandle을 가진 격리 공간으로, 기기 관리자(MDM)가 설정한 정책의 적용을 받는다. 같은 앱이 개인 프로필과 work profile에 각각 설치되면 두 인스턴스는 서로 다른 UID를 가지며 파일시스템, SharedPreferences, 알림이 완전히 분리된다. `UserManager.isManagedProfile()`로 현재 프로필이 work profile인지 확인할 수 있고, `CrossProfileApps` API로 개인-업무 프로필 간 제한적인 상호작용(예: 업무용 앱을 개인 화면에서 실행)을 중개할 수 있다.

### 판단 기준

- 파일 공유, 클립보드, 알림 같은 기능이 work profile 환경에서 프로필 경계를 넘지 못할 수 있다는 점을 설계에 반영한다. 기본적으로 시스템은 프로필 간 데이터 이동을 제한한다.
- 기기 관리 앱(EMM/MDM)을 개발하는 경우가 아니라면 대부분의 일반 앱은 자신이 어느 프로필에서 실행 중인지만 알면 되고, 다른 프로필의 데이터에 접근하려 시도하지 않는다.
- 멀티 유저(게스트 모드 등)와 work profile은 다른 개념이다. 멀티 유저는 완전히 별도의 기기 사용자를, work profile은 한 사용자 안의 업무용 부분 공간을 뜻한다.

### 최소 프로필 인식 흐름

앱은 먼저 자신이 실행 중인 `UserHandle`과 관리형 프로필 여부를 상태에 포함한다. 다른 프로필을 임의로 열거하거나 파일 경로로 접근하지 않고, 정책이 허용한 대상만 `CrossProfileApps`가 돌려주는 목록으로 취급한다.

```kotlin
val users = context.getSystemService(UserManager::class.java)
val crossProfile = context.getSystemService(CrossProfileApps::class.java)

val current = Process.myUserHandle()
val state = ProfileState(
    user = current,
    isManaged = users.isManagedProfile,
    allowedTargets = crossProfile.targetUserProfiles
)
renderProfileState(state)
```

`targetUserProfiles`가 비었다면 반대 프로필이 없거나, 앱이 그 프로필에 설치되지 않았거나, 관리 정책이 상호작용을 허용하지 않은 경우일 수 있다. 대상 `UserHandle`을 안다는 사실은 그 프로필의 파일·DB·provider를 직접 읽을 권한을 주지 않는다. 실제 교차 프로필 동작은 `CrossProfileApps`의 허용된 시작 API나 관리자가 설정한 intent filter를 사용한다.

### 경계

- 이 노트는 사용자/프로필 분리 모델을 다룬다. 다른 앱의 설치 여부를 조회하는 제한은 [PackageManager 조회는 Android 11부터 패키지 가시성 제한을 받는다](./package-visibility-queries.md)가 다룬다.
- 기기 관리 정책(MDM) 자체의 API 세부는 이 클러스터의 범위 밖이며 필요 시 별도 클러스터로 확장한다.

### 관찰 가능한 신호

앱 로그의 현재 `UserHandle`, `isManagedProfile`, 허용된 `targetUserProfiles`를 함께 남긴다. `adb shell pm list users`의 사용자/프로필 ID와 `adb shell dumpsys package <pkg>`의 사용자별 설치 상태를 대조하면 "대상 없음", "미설치", "정책 차단"을 분리할 수 있다.

### 공식 문서

- https://developer.android.com/work/managed-profiles
- https://developer.android.com/reference/android/os/UserManager
- https://developer.android.com/reference/android/content/pm/CrossProfileApps

검증일: 2026-08-06. 현재 프로필과 교차 프로필 대상은 별도 상태이며, `CrossProfileApps`가 반환하는 대상도 정책에 의해 제한된다는 계약을 확인했다.
