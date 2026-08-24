---
title: hidl-treble-interface
tags: [android, android/native, android/system-internals]
aliases: [HIDL, HAL Interface Definition Language]
date modified: 2026-08-04 15:52:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

## HIDL은 legacy Treble interface이지 신규 기본값이 아니다

상위 문서: [HAL native contracts](hal-native.md)

HIDL(HAL Interface Definition Language)은 Android 8.0 Project Treble 도입 당시 Framework(`system.img`)와 Vendor(`vendor.img`) 간의 하드웨어 추상화 인터페이스를 바이너리 호환성(C++ / Java RPC)을 갖춘 규격으로 선언하기 위해 도입된 IDL 언어다.

그러나 Android 10부터 HIDL은 지원 중단(Deprecated) 수순에 들어갔으며, Android 11+부터는 단일화된 **Stable AIDL HAL**이 신규 표준으로 지정되었다. 기존 기기 호환성을 위해 HIDL 스택이 유지되지만, 신규 벤더 HAL 인터페이스 작성 시 HIDL을 새로 채택해서는 안 된다.

---

### 메커니즘: HIDL 스택 vs Stable AIDL HAL 구조 비교

```mermaid
graph TD
    subgraph Legacy HIDL Architecture (Android 8~10)
        A1["HIDL Interface (.hal)\n(hardware/interfaces/foo/1.0/IFoo.hal)"]
        A2["hwservicemanager Daemon"]
        A3["Kernel Driver: /dev/hwbinder"]
        
        A1 --> A2
        A2 --> A3
    end

    subgraph Modern Stable AIDL Architecture (Android 11+)
        B1["Stable AIDL Interface (.aidl)\n(@VintfStability / IMyHal.aidl)"]
        B2["Unified servicemanager Daemon"]
        B3["Kernel Driver: /dev/binder"]
        
        B1 --> B2
        B2 --> B3
    end
```

1. **`hwservicemanager` vs `servicemanager` 단일화**: HIDL은 벤더 전용 IPC 바인더 노드인 `/dev/hwbinder`와 전용 레지스트리 데몬인 `hwservicemanager`를 별도로 운영했으나, Stable AIDL HAL은 일반 바인더 드라이버(`/dev/binder`)와 통합된 `servicemanager`로 일원화되어 IPC 오버헤드와 데몬 리소스 사용량을 줄였다.
2. **Versioning Model (버전 관리)**: HIDL은 패키지 이름에 메이저/마이너 버전을 명시하는 방식(`android.hardware.foo@1.1`)을 썼으나, AIDL HAL은 `@VintfStability` 어노테이션과 정적 버전 할당(`v1`, `v2`) 방식을 사용한다.

---

### HIDL `.hal` 인터페이스 파일 예시 (Legacy)

```cpp
// hardware/interfaces/nfc/1.2/INfc.hal (Legacy HIDL 정의 예시)
package android.hardware.nfc@1.2;

import android.hardware.nfc@1.1::INfc;

interface INfc extends android.hardware.nfc@1.1::INfc {
    enum Status : uint32_t {
        OK = 0,
        FAILED = 1,
    };

    writeConfig(vec<uint8_t> config) generates (Status status);
};
```

---

### 실무 규칙

- Android 11 이상 플랫폼을 대상으로 타깃팅하는 모든 신규 하드웨어 서브시스템 HAL 개발 시 HIDL `.hal` 파일을 생성하지 말고 `aid_interface` Soong 룰 기반의 Stable AIDL을 사용해야 한다.
- 기존 HIDL 인터페이스를 유지해야 하는 마이그레이션 단계에서는 `hidl2aidl` 변환 툴을 사용하여 AIDL 인터페이스 포팅을 자동화할 수 있다.

---

### 관측 가능한 증거 (Observable Evidence)

1. **`lshal` 명령을 통한 레거시 HIDL vs AIDL HAL 등록 현황 관측**:
   ```bash
   adb shell lshal
   # HIDL 서비스는 android.hardware.foo@1.0 형태로 출력
   # AIDL HAL 서비스는 android.hardware.foo.IFoo/default 형태로 출력
   ```
2. **`hwservicemanager` 프로세스 및 `/dev/hwbinder` 마운트 상태 확인**:
   ```bash
   adb shell ps -eZ | grep hwservicemanager
   adb shell ls -la /dev/hwbinder
   ```

---

### 관련 문서

- [AIDL HAL은 신규 HAL의 현재 stable interface 선택지다](aidl-hal.md)
- [Binderized HAL과 passthrough HAL은 process boundary를 다르게 둔다](binderized-vs-passthrough-hal.md)

공식 문서: [AOSP HIDL Overview](https://source.android.com/docs/core/architecture/hidl), [AOSP HAL Overview](https://source.android.com/docs/core/architecture/hal)

