---
title: binderized-and-passthrough-hal-define-process-boundary
tags: [android, android/native, android/system-internals]
aliases: [Binderized HAL, Passthrough HAL]
date modified: 2026-08-05 14:15:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

## Binderized HAL과 passthrough HAL은 프로세스 경계를 다르게 둔다

상위 문서: [HAL native contracts](hal-native-contracts.md)
배경 지식: [IPC](01_inbox/operating-systems/ipc-mechanisms.md), [SELinux/MAC](01_inbox/linux/security/selinux.md)

Android Treble 아키텍처에서 HAL(Hardware Abstraction Layer)은 실행 시점의 프로세스 경계(Process Boundary) 배치 방식에 따라 **Binderized HAL**과 **Passthrough HAL**의 두 가지 형태 모델로 구분된다.

Modern Android(Android 8.0 Treble 이후) 표준인 Binderized HAL은 HAL 서비스가 독립된 별도의 데몬 프로세스(`/vendor/bin/hw/*`)로 실행되어 Binder IPC를 통해 클라이언트(Framework)와 통신하는 반면, Passthrough HAL은 클라이언트 프로세스 메모리 공간에 `dlopen()`으로 동적 공유 라이브러리(`.so`)를 직접 로드하여 동일 프로세스 내에서 직접 함수 호출로 동작한다.

---

### 메커니즘: Binderized vs Passthrough 실행 프로세스 배치 비교

```mermaid
graph TD
    subgraph Binderized HAL (Modern Default)
        A1["Framework Process (system_server / cameraserver)\n(scontext=u:r:system_server:s0)"]
        A2["Kernel hwbinder / binderfs\n(IPC Transaction & Memory Copy)"]
        A3["Vendor HAL Process (/vendor/bin/hw/android.hardware.camera-service)\n(scontext=u:r:hal_camera_default:s0)"]
        
        A1 -->|IPC Call| A2
        A2 -->|Dispatch| A3
    end

    subgraph Passthrough HAL (Legacy / Direct Load)
        B1["Framework Process"]
        B2["Vendor Shared Library (.so)\n(dlopen / Same Address Space)"]
        
        B1 -->|Direct C/C++ Function Call| B2
    end
```

1. **Crash Isolation (크래시 격리)**: Binderized HAL 환경에서는 HAL 데몬 프로세스가 SIGSEGV 패닉으로 사망하더라도 Framework 프로세스(system_server)가 함께 죽지 않고 `service died` 사망 통지만 받지만, Passthrough HAL 환경에서는 HAL 라이브러리 내부의 메모리 오염 패닉이 Framework 프로세스 전체를 즉시 격추시킨다.
2. **SELinux Domain Separation (보안 격리)**: Binderized HAL은 `system_server` 도메인과 `hal_foo_default` 도메인을 엄격히 분리하여 벤더 드라이버 코드가 커스텀 하드웨어 디바이스 노드(`/dev/my_driver`)에만 제한 접근하도록 MAC 정책을 적용할 수 있다.

---

### Binderized HAL 서비스 실행 스크립트 및 Passthrough 래퍼 예시

```cpp
// 1. Binderized HAL main.cpp (독립 데몬 프로세스로 바인더 스레드 풀 등록)
#include <android/hardware/foo/1.0/IFoo.h>
#include <hidl/HidlTransportSupport.h>

int main() {
    android::hardware::configureRpcThreadpool(4, true);
    android::sp<IFoo> service = new FooImpl();
    if (service->registerAsService("default") != android::OK) {
        return 1;
    }
    android::hardware::joinRpcThreadpool();
    return 0;
}
```

```text
# 2. /vendor/etc/init/android.hardware.foo@1.0-service.rc
service vendor.foo-1-0 /vendor/bin/hw/android.hardware.foo@1.0-service
    class hal
    user hal
    group hidden
```

---

### 실무 규칙

- Android 11+ 이후 릴리스 기기의 모든 신규 HAL 개발은 `@VintfStability` 규격을 준수하는 **Stable AIDL Binderized HAL**로 작성되어야 한다.
- Passthrough HAL은 Treble 마이그레이션 과도기의 레거시 잔재 또는 초저지연 오디오/스페셜 하드웨어에 한정된 예외이며, `system` 파티션과 `vendor` 파티션을 물리 분리하여 업데이트하는 Treble 계약을 충족하려면 Binderized 배치가 필수적이다.

---

### 관측 가능한 증거 (Observable Evidence)

1. **lshal 명령을 통한 Binderized vs Passthrough 모드 확인**:
   ```bash
   adb shell lshal
   # Interface                              Server PID   Client PID   Format
   # android.hardware.camera.provider@2.4::ICameraProvider/legacy/0  1234  567  binderized
   # android.hardware.graphics.mapper@2.0::IMapper/default            N/A   567  passthrough
   ```
2. **`ps` 명령을 통한 Vendor HAL 독립 프로세스 생성 상태 검증**:
   ```bash
   adb shell ps -eZ | grep -E "vendor\.bin\.hw|hal_"
   # u:r:hal_camera_default:s0  vendor  1234  1  /vendor/bin/hw/android.hardware.camera-service
   ```

---

### 관련 문서

- [AIDL HAL은 신규 HAL의 현재 stable interface 선택지다](aidl-hal-is-current-stable-interface-for-new-hals.md)
- [HIDL은 legacy Treble interface이지 신규 기본값이 아니다](hidl-is-legacy-treble-interface-not-new-default.md)
- [Native service 디버깅은 init, Binder, VINTF, SELinux, tombstone을 분리한다](native-service-debugging-separates-init-binder-vintf-selinux-and-tombstones.md)

공식 문서: [AOSP HAL Types Overview](https://source.android.com/docs/core/architecture/hal/types)

