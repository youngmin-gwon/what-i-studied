---
title: project-treble-hal
tags: [android, android/native, android/system-internals]
aliases: [Project Treble, Treble Architecture]
date modified: 2026-08-04 15:52:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

## Treble은 system과 vendor 업데이트 경계를 stable interface로 분리한다

상위 문서: [HAL native contracts](hal-native.md)

Android 8.0부터 수립된 **Project Treble** 아키텍처의 핵심 실무 계약은 OS 프레임워크 이미지(`system.img`)와 SoC/하드웨어 벤더 이미지(`vendor.img`) 사이를 물리적 파티션과 Stable Interface(Stable AIDL / HIDL)로 완벽히 분리(Decoupling)하는 것이다.

Treble 이전에는 Android OS 버전 업그레이드 시 벤더 소스 코드가 프레임워크 내부에 밀접하게 결합되어 있어 매번 디바이스 드라이버와 커스텀 HAL을 전면 다시 개발해야 했으나, Treble 도입 이후에는 벤더 바이너리 재컴파일 없이도 `system.img`만 개별 단독 업데이트(Framework-only OTA)가 가능해졌다.

---

### 메커니즘: Pre-Treble Monolithic vs Treble Modular Architecture

```mermaid
graph TD
    subgraph Pre-Treble Monolithic System (Android 7.0 이전)
        A1["Android Framework (system.img)"]
        A2["Vendor HAL (.so) & Device Drivers"]
        A1 -->|"Direct Shared Library Link"| A2
        note1["OS Upgrade requires vendor code rebuild"]
    end

    subgraph Treble Modular System (Android 8.0+)
        B1["System Partition (system.img)\n(Android Framework & Services)"]
        B2["Stable Interfaces (Stable AIDL / HIDL)\n(VINTF Alignment & IPC Boundary)"]
        B3["Vendor Partition (vendor.img)\n(Vendor HAL Services & Drivers)"]
        
        B1 <-->|"IPC via /dev/binder"| B2
        B2 <-->|"Binderized HAL"| B3
        note2["Independent Framework OTA Upgrade Supported"]
    end
```

1. **Partition Physical Separation**: `/system` 파티션(Google/AOSP 관리)과 `/vendor` 파티션(SoC/OEM 제조사 관리)이 물리적 이미지 파일로 분리 마운트됨.
2. **Stable Interface Contract**: Framework와 Vendor 파티션 간의 모든 통신은 버전이 고정되고 ABI 호환성이 보장된 Binderized HAL 인터페이스만 허용하며, 직접적인 동적 라이브러리 심볼 참조를 엄격히 금지함.

---

### `Android.bp` Vendor Interface & Stability 선언 예시

```python
// hardware/interfaces/foo/aidl/Android.bp 예시
aidl_interface {
    name: "android.hardware.foo",
    vendor_available: true,
    srcs: ["android/hardware/foo/*.aidl"],
    stability: "vintf", // VINTF 규격을 따르는 Stable Interface 선언
    backend: {
        cpp: {
            enabled: true,
        },
        ndk: {
            enabled: true,
        },
    },
}
```

---

### 실무 규칙

- Vendor 파티션의 C/C++ 네이티브 데몬이 System 파티션의 비공개 공유 라이브러리(`/system/lib64/libutils.so` 등)를 직접 `dlopen`하거나 링크하도록 작성하면 CTS/VTS 호환성 테스트에서 거부된다. 반드시 NDK Stable C API 또는 VNDK 허용 라이브러리만 링크해야 한다.
- GSI(Generic System Image)를 디바이스에 플래싱하여 부팅을 검증하는 CTS-on-GSI 테스트는 Treble 분리 계약이 완벽히 준수되고 있는지를 측정하는 최종 호환성 검증 기준이다.

---

### 관측 가능한 증거 (Observable Evidence)

1. **디바이스의 Treble 아키텍처 활성화 여부 조망**:
   ```bash
   adb shell getprop ro.treble.enabled
   # true
   ```
2. **VINTF 호환성 매니페스트 및 디바이스 분리 확인**:
   ```bash
   adb shell cat /system/etc/vintf/manifest.xml | grep -i "framework"
   adb shell cat /vendor/etc/vintf/manifest.xml | grep -i "device"
   ```

---

### 관련 문서

- [HAL은 framework와 vendor 구현 사이의 안정된 userspace contract다](hal-userspace-boundary.md)
- [VINTF는 framework/vendor 호환성을 manifest와 matrix로 선언한다](vintf-manifest-compatibility.md)
- [AIDL HAL은 신규 HAL의 현재 stable interface 선택지다](aidl-hal.md)

공식 문서: [AOSP Project Treble Overview](https://source.android.com/docs/core/architecture/hal)

