---
title: app-process-specializes-before-activitythread-attaches-to-framework
tags: [android, android/boot-runtime, android/runtime, android/system-internals]
aliases: ["앱 프로세스는 specialization 뒤 ActivityThread로 framework에 attach한다"]
date modified: 2026-08-03 17:24:01 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## 앱 프로세스는 specialization 뒤 ActivityThread 로 framework 에 attach 한다

상위 문서: [Zygote 런타임 계약](zygote-runtime-contracts.md)

앱 프로세스 생성 과정은 단순히 Zygote의 `fork()`로 끝나지 않으며, 고유 UID/GID 적용, SELinux 도메인 강등, Cgroup 바인딩, App-specific ClassLoader 로딩으로 고유 샌드박스 환경을 구체화하는 **Specialization** 단계를 거친 직후, `ActivityThread.main()`에서 AMS로 Binder `attachApplication()`을 호출하여 비로소 Android 프레임워크 프로세스로 통합되는 메커니즘이다.

### 내부 동작 메커니즘 (Internal Mechanism)

1. **Zygote Fork & Specialize (`Zygote.nativeForkAndSpecialize`)**:
   - Zygote 프로세스는 Socket 요청에서 전달받은 `target_sdk`, `uid`, `gids`, `runtime_flags`, `seinfo`, `nice_name` 매개변수를 기반으로 자식 프로세스를 `fork()`한다.
   - 자식 프로세스 내에서 순차적으로 샌드박스 격리(Specialization)를 진행한다:
     a. **Identity Transition**: `setresgid()` 및 `setresuid()`로 root/zygote 권한에서 앱 고유 UID/GID(`u0_aXXX`)로 전이한다.
     b. **Capability Drop**: `capset()`을 호출하여 리눅스 root 캡파빌리티(CAP_SYS_ADMIN 등)를 전부 제거한다.
     c. **Seccomp Filtering**: `SetSeccompPolicy()`를 통해 미승인 시스템 콜 호출을 차단하는 커널 샌드박스 필터를 적용한다.
     d. **Storage Mount Isolation**: `unshare(CLONE_NEWNS)` 및 mount propagation 설정을 통해 앱 전용 격리 파일시스템 네임스페이스를 구축한다.
     e. **SELinux Domain Transition**: `selinux_android_setcontext()`로 Zygote 도메인(`u:r:zygote:s0`)에서 앱 샌드박스 도메인(`u:r:untrusted_app:s0`)으로 보안 컨텍스트를 강등 전환한다.
2. **`ActivityThread` Entrypoint Invocation**:
   - Specialization이 완료되면 `ZygoteInit`은 `ActivityThread.main(args)` 메서드를 리플렉션(Reflection)으로 호출한다.
   - `ActivityThread.main()`은 `Looper.prepareMainLooper()`를 호출해 앱의 메인 스레드 MessageQueue 및 Handler를 생성한다.
3. **AMS Attach (`attachApplication`)**:
   - `ActivityThread` 인스턴스는 AMS로 Binder IPC인 `attachApplication(mAppThread)`을 호출하여 자식 프로세스가 구동 완료되었음을 프레임워크에 알린다.

```mermaid
sequenceDiagram
    autonumber
    participant ZYG as Zygote Daemon
    participant APP as App Process Child
    participant AT as ActivityThread
    participant AMS as ActivityManagerService

    ZYG->>APP: fork()
    Note over APP: Specialize Process:
- setresuid(uid)
- Drop Capabilities
- Set SELinux Context
    APP->>AT: Invoke ActivityThread.main()
    AT->>AT: Looper.prepareMainLooper()
    AT->>AMS: Binder IPC: attachApplication(IApplicationThread)
    AMS->>AT: bindApplication() & Launch Activity/Service
```

### 코드 및 구체 예시 (Concrete Snippets)

`ActivityThread.main()` 프레임워크 메인 함수 스니펫 (`frameworks/base/core/java/android/app/ActivityThread.java`):

```java
// ActivityThread.java
public static void main(String[] args) {
    // 1. Prepare main looper for app thread
    Looper.prepareMainLooper();

    // 2. Instantiate ActivityThread and attach to AMS
    ActivityThread thread = new ActivityThread();
    thread.attach(false, startSeq);

    // 3. Start main event loop
    Looper.loop();
    throw new RuntimeException("Main thread loop unexpectedly exited");
}

private void attach(boolean system, long startSeq) {
    final IActivityManager mgr = ActivityManager.getService();
    try {
        mgr.attachApplication(mAppThread, startSeq);
    } catch (RemoteException ex) {
        throw ex.rethrowFromSystemServer();
    }
}
```

### 관측 가능 증거 (Observable Evidence)

`adb shell`을 활용하여 특화(Specialized) 완료된 앱 프로세스의 UID, SELinux 도메인 및 메인 스레드 Looper 상태를 점검할 수 있다:

```bash
# 앱 프로세스 특화 결과 (UID: u0_aXXX 및 SELinux Domain: u:r:untrusted_app:s0) 확인
adb shell ps -Z | grep com.example.app
# 출력 예시:
# u:r:untrusted_app:s0:c512,c768  u0_a185  14250 650 1485920 85400 0 S com.example.app

# ActivityThread attach 과정의 logcat 이벤트 확인
adb logcat -s ActivityThread ActivityManager
```

### 관련 문서

- [zygote-socket-is-system-server-process-factory-interface](zygote-socket-is-system-server-process-factory-interface.md)
- [ams-coordinates-app-process-and-component-lifecycle](../system-server-contracts/ams-coordinates-app-process-and-component-lifecycle.md)

공식 문서: [Android Process Lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle)
