---
title: components-as-entry-points
tags: [android, android/app-components, android/architecture]
aliases: ["안드로이드 앱 컴포넌트는 OS가 호출하는 실행 경계다"]
date modified: 2026-08-06 15:03:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 안드로이드 앱 컴포넌트는 시스템이 인스턴스화하는 진입 경계다

Activity, Service, manifest receiver, ContentProvider의 실제 lifecycle instance는 앱이 임의로 `new` 해서 실행하는 객체가 아니다. 시스템은 manifest나 runtime 등록 정보로 대상을 찾고, 필요하면 앱 process를 시작한 뒤 framework callback을 호출한다. 생성자가 호출됐다는 사실만으로 component가 task, service registry, broadcast delivery에 등록되는 것은 아니다.

### 내부 동작

```text
외부/내부 요청
  → 시스템이 component·exported·permission을 해석
  → 필요하면 application process 시작
  → component class 인스턴스화
  → main thread에서 lifecycle/entry callback 전달
```

기본 설정에서는 한 앱의 component가 같은 process와 main thread에서 실행된다. 따라서 Intent가 쓰였다고 항상 IPC인 것은 아니며, 같은 process의 일반 Kotlin 객체끼리는 직접 호출해도 된다. 금지할 것은 Activity나 Service instance를 직접 만들고 lifecycle callback을 호출하거나, 다른 component의 실제 instance reference를 전역에 저장하는 일이다.

### 안전한 최소 선언

```xml
<activity
    android:name=".MainActivity"
    android:exported="true">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>

<service
    android:name=".SyncSessionService"
    android:exported="false" />
```

런처 Activity는 시스템 launcher가 진입해야 하므로 exported이고, 앱 내부 전용 Service는 닫는다. 동적 receiver는 manifest가 아니라 `registerReceiver()` 호출이 등록 경계다.

### 판단·관찰 신호

- `adb shell dumpsys package <package>`에서 최종 등록 component와 intent filter를 확인한다.
- `adb shell am start -W -n <package>/.MainActivity` 뒤 `onCreate()`의 PID를 기록하면 process가 없던 상태에서 시스템 진입이 process를 만들었는지 볼 수 있다.
- `MainActivity()`를 unit test에서 생성해도 실제 window·task·lifecycle owner가 생기지 않는다. UI component test는 ActivityScenario 같은 framework harness를 사용한다.
- Intent/Binder/URI는 경계를 통과하기 위한 protocol이지 모든 앱 내부 호출의 의무가 아니다.

상위 문서: [App Component Contracts](component-contracts.md)

공식 문서: [Application fundamentals](https://developer.android.com/guide/components/fundamentals), [Processes and threads](https://developer.android.com/guide/components/processes-and-threads)
