---
title: android-app-sandbox-is-uid-and-process-boundary
tags: ["android", "android/security-privacy"]
aliases: ["Android app sandbox 는 UID 와 프로세스 경계로 앱을 격리한다"]
date modified: 2026-08-06 13:00:00 +09:00
date created: 2026-08-01 00:03:59 +09:00
---

## Android app sandbox 는 UID 와 프로세스 경계로 앱을 격리한다

Android App Sandbox는 전통적인 데스크톱 OS와 달리 **각 앱을 독립된 Linux 사용자(UID, 예: `u0_a150`) 및 별도 프로세스 경계**에 격리시킨다. 기본적으로 앱은 다른 앱의 샌드박스 디렉터리(`/data/data/<package>`), 프로세스 메모리 공간, 파일 서술자(File Descriptor)에 직접 접근하는 것이 Linux 커널 레벨에서 금지된다.

```mermaid
flowchart LR
    subgraph AppA [App A Sandbox: UID u0_a150 / PID 2040]
        PrivateA[/data/data/com.app.a - mode 0700]
        MemA[Process Memory Space]
    end

    subgraph AppB [App B Sandbox: UID u0_a151 / PID 2080]
        PrivateB[/data/data/com.app.b - mode 0700]
        MemB[Process Memory Space]
    end

    KernelBoundary((Linux Kernel Boundary: DAC & Permission Check))
    
    AppA -- Direct File Access Blocked --> KernelBoundary
    KernelBoundary -- Permission Denied --> PrivateB
    AppA ==>|"binder ipc / ContentProvider / Intent"| AppB
```

### 내부 동작 메커니즘

1. **UID Allocation**: `PackageManagerService`는 앱 설치 시 `FIRST_APPLICATION_UID(10000)` 이상 범위에서 고유한 UID를 부여한다 (`u0_a` + `(UID - 10000)`).
2. **Unix File DAC**: 앱 내부 저장소(`/data/data/<package>`)의 파일 owner는 `u0_a150:u0_a150`으로 설정되며, 권한 모드는 `0700` (`rwx------`)이 적용된다.
3. **Zygote Forking & Isolated Processes**: 앱 실행 시 **Zygote**(모든 앱 프로세스의 부모가 되는, 공통 프레임워크 클래스를 미리 적재해 둔 상태로 대기하는 시스템 프로세스)가 `fork()`를 호출한 직후 `setuid()` 및 `setgid()`를 실행하여 커널 레벨 Privileges를 하강시킨다. WebView나 민감 컴포넌트는 `android:isolatedProcess="true"` 속성을 지정하여 무권한 UID(90000번대)로 추가 격리할 수 있다.

### 샌드박스 밖 데이터 교환 및 Manifest 설정 예시

```xml
<!-- AndroidManifest.xml: 웹뷰 렌더러 프로세스를 격리 샌드박스로 구성 -->
<service
    android:name=".IsolatedRenderingService"
    android:isolatedProcess="true"
    android:useEmbeddedDex="true" />
```

```kotlin
// Binder IPC 및 ContentProvider URI Permission을 통한 안전한 샌드박스 간 파일 전달
fun shareFileWithUriPermission(context: Context, targetPackage: String, contentUri: Uri) {
    val intent = Intent(Intent.ACTION_VIEW).apply {
        setDataAndType(contentUri, context.contentResolver.getType(contentUri))
        addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        setPackage(targetPackage)
    }
    context.startActivity(intent)
}
```

### 관찰 가능한 증거 (Observable Evidence)

- **adb 샌드박스 파일 권한 조회**:
  ```bash
  adb shell ls -la /data/data/
  # 출력: drwx------  5 u0_a150 u0_a150 4096 2026-08-04 15:00 com.example.app
  ```
- **샌드박스 침범 시 발생 예외**:
  ```text
  java.io.FileNotFoundException: /data/data/com.other.app/files/secret.db: open failed: EACCES (Permission denied)
  ```

### 판단 기준

Platform security 노트는 앱 권한보다 낮은 계층에서 device integrity 와 mandatory policy 가 어떻게 강제되는지 판단하는 기준으로 읽는다.

### 경계

client-side check 를 authorization 으로 오해하지 않고 server verification, boot trust, sandbox boundary 를 분리한다.

관련 노트: [Permission protection level은 접근 승인 주체를 정의한다](../../permissions-and-sandbox/permission-contracts/permission-protection-level-defines-who-can-grant-access.md)
