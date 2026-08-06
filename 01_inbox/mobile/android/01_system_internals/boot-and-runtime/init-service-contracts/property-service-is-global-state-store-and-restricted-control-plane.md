---
title: property-service-is-global-state-store-and-restricted-control-plane
tags: [android, android/boot-runtime, android/init, android/system-internals]
aliases: ["property service는 전역 상태 저장소이자 제한된 제어 plane이다"]
date modified: 2026-08-05 16:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## property service 는 전역 상태 저장소이자 제한된 제어 plane 이다

상위 문서: [init 서비스 계약](init-service-contracts.md)
배경 지식: [IPC(공유 메모리/유닉스 소켓)](../../../../../operating-systems/ipc-mechanisms.md)

`Property Service`는 `init` 프로세스 내부에서 구동되는 Android 전역 키-값(Key-Value) 상태 저장소이자 시스템 제어 플레인으로, Shared Memory를 통한 고속 읽기와 **[Unix Domain Socket](../../../../../operating-systems/ipc-mechanisms.md)**(같은 머신 안의 프로세스끼리 파일시스템 경로를 주소로 삼아 통신하는 프로세스 간 통신(IPC) 메커니즘) 통신 및 SELinux 보안 검증을 통한 쓰기 제어 메커니즘을 제공한다.

### 내부 동작 메커니즘 (Internal Mechanism)

1. **Shared Memory Read (mmap `/dev/__properties__`)**:
   - 속성 값 읽기(`SystemProperties.get()`) 시 [binder ipc](../../binder-ipc.md) 오버헤드를 없애기 위해, `init`은 Trie 트리가 구축된 Trie 데이터 구조체의 속성 영역을 `/dev/__properties__` 공유 메모리로 마운트한다.
   - 모든 프로세스는 libc(Bionic) 초기화 과정에서 읽기 전용(`O_RDONLY`)으로 이 메모리를 `mmap`하여 lock-free 직렬화 노드인 `prop_info` 포인터를 통해 직접 1초 미만의 고속 조회를 수행한다.
2. **Socket Write IPC & SELinux Permission Check**:
   - 속성 쓰기(`setprop` / `SystemProperties.set()`) 시 client는 `/dev/socket/property_service` 유닉스 소켓으로 `PROP_MSG_SETPROP2` 패킷을 송신한다.
   - `init`의 `HandlePropertySetMessage()` 함수는 Client의 peer credential(`SO_PEERCRED` -> UID/GID, PID, SELinux Context)을 추출하고, `property_contexts` DB에서 해당 Property Type에 쓰기 권한이 허용되어 있는지 `selinux_check_access()`로 검증 후 속성을 갱신한다.
3. **Control Properties (`ctl.*`)**:
   - `ctl.start`, `ctl.stop`, `ctl.restart` 속성 쓰기 요청을 수신하면 `init` 프로세스는 메인 이벤트 루프의 Action Queue에 서비스 스케줄링 이벤트를 추가하여 네이티브 데몬의 수명주기를 직접 제어한다.

```mermaid
flowchart LR
    APP["App / Native Process"] -->|Read: mmap (Fast Lock-Free)| SHM["/dev/__properties__
Shared Memory (Read-Only)"]
    APP -->|Write: Unix Socket (PROP_MSG_SETPROP2)| SOCKET["/dev/socket/property_service"]
    SOCKET -->|HandlePropertySetMessage() + SELinux Check| PS["Property Service (init - PID 1)"]
    PS -->|Update prop_info Trie| SHM
    PS -->|Trigger Action / Control| INIT["init Control Loop (ctl.*)"]

    style SHM fill:#e8f5e9,stroke:#388e3c
    style PS fill:#f9f,stroke:#333,stroke-width:2px
```

### 코드 및 구체 예시 (Concrete Snippets)

`system/core/init/property_service.cpp` 쓰기 핸들러 및 `property_contexts` 선언 예시:

```cpp
// system/core/init/property_service.cpp (Property Write handling logic)
uint32_t PropertySet(const std::string& name, const std::string& value, std::string* error) {
    // 1. Property Name & Value Length Verification
    if (!IsLegalPropertyName(name)) {
        *error = "Illegal property name";
        return PROP_ERROR_INVALID_NAME;
    }

    // 2. Control Properties Handling (ctl.start, ctl.stop, ctl.restart)
    if (android::base::StartsWith(name, "ctl.")) {
        return HandleControlProperty(name, value, error);
    }

    // 3. Update Trie node in shared memory
    prop_info* pi = (prop_info*) __system_property_find(name.c_str());
    if (pi != nullptr) {
        __system_property_update(pi, value.c_str(), value.size());
    } else {
        __system_property_add(name.c_str(), name.size(), value.c_str(), value.size());
    }

    // 4. Trigger property change listeners in init event loop
    property_changed(name, value);
    return PROP_SUCCESS;
}
```

`property_contexts` SELinux 접근 제어 선언 예시 (`system/sepolicy/private/property_contexts`):

```text
# Access control definitions for system properties
sys.boot_completed      u:object_r:boot_status_prop:s0 exact bool
ro.boot.slot_suffix     u:object_r:bootloader_prop:s0 exact string
ctl.start$zygote        u:object_r:ctl_zygote_prop:s0 exact string
```

### 관측 가능 증거 (Observable Evidence)

`adb shell`을 활용하여 현재 전체 System Property 및 공유 메모리 맵 노드를 확인할 수 있다:

```bash
# 전체 시스템 속성 목록 및 현재 값 조회
adb shell getprop

# 특정 속성 조회
adb shell getprop ro.build.version.release

# 속성 공유 메모리 노드 파일 점검
adb shell ls -la /dev/__properties__/
```

### 관련 문서

- [init security는 SELinux domain과 capability 경계로 정의된다](init-security-is-selinux-domain-and-capability-boundary.md)
- [init triggers는 event와 property 조건을 결합하는 실행 gate다](init-triggers-are-event-and-property-gates.md)

공식 문서: [Android System Properties](https://source.android.com/docs/core/architecture/configuration/properties)
