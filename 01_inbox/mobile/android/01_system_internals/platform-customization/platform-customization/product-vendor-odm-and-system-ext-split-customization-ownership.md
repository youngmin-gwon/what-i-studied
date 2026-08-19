---
title: product-vendor-odm-and-system-ext-split-customization-ownership
tags: [android, android/aosp, android/partitions]
aliases: ["product, vendor, odm, system_ext는 customization ownership을 나눈다", Android partitions, Vendor partition]
date modified: 2026-08-04 22:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## product, vendor, odm, system_ext 는 customization ownership 을 나눈다

상위 문서: [Platform customization contracts](platform-customization.md)

Android 의 customization 은 한 디렉터리에 덧붙이는 작업이 아니라 partition 별 ownership 을 나누는 작업이다. `system` 은 공통 framework 와 platform code 를 담고, `vendor` 는 SoC/vendor implementation 을, `odm` 은 device maker variation 을, `product` 와 `system_ext` 는 제품별 앱, 설정, framework extension 을 담는다.

이 경계는 update 와 compatibility 를 위해 중요하다. framework 가 vendor 구현을 마음대로 깨면 Treble 경계가 무너지고, 제품별 앱과 permission 을 잘못된 partition 에 넣으면 OTA, factory reset, certification, privileged permission 정책이 꼬인다.

---

### 내부 동작 메커니즘 (Partition Ownership & Build Isolation)

AOSP는 파티션 간의 강결합을 방지하고 각 영역의 업데이트 주체를 분리하기 위해 빌드 레벨에서 파티션을 명확히 구분한다.

1. **`/system` (Google AOSP Platform)**:
   - AOSP Generic Framework 및 핵심 시스템 서비스. GSI(Generic System Image)로 교체 가능한 호환성 기준점.
2. **`/system_ext` (OEM System Extension)**:
   - OEM이 확장한 비표준 프레임워크 API 및 전용 시스템 서비스.
3. **`/product` (OEM System Customization)**:
   - 특정 제품/통신사 전용 프리로드 앱, RRO 오버레이, 폰트, 벨소리, 시스템 설정(sysconfig).
4. **`/vendor` (SoC Vendor Implementation)**:
   - SoC 제조사(Qualcomm, MediaTek, Exynos)가 작성한 HAL 서비스, GPU 드라이버, Vendor Kernel Modules.
5. **`/odm` (Original Design Manufacturer)**:
   - 동일 SoC 기반의 세부 단말 차이(카메라 센서 조합, 디스플레이 파널 차이)를 다루는 Board-level 구성 요소.

```mermaid
graph TD
    subgraph System Domain (AOSP & OEM System)
        SYS[/system - AOSP Core Framework & GSI]
        SYSEXT[/system_ext - OEM Framework Extensions]
        PROD[/product - Product Apps & RRO Overlays]
    end
    
    subgraph Treble Boundary (AIDL / HIDL)
        VINTF[VINTF Compatibility Manifest]
    end
    
    subgraph Vendor Domain (Hardware Board)
        VEND[/vendor - SoC HALs & Drivers]
        ODM[/odm - Board Variation Files]
    end

    SYS <--> VINTF
    SYSEXT <--> VINTF
    PROD <--> VINTF
    VINTF <--> VEND
    VEND <--> ODM
```

---

### `Android.bp` 모듈 파티션 할당 선언 예시

```bp
// 1. Vendor 파티션 전용 HAL 모듈
cc_binary {
    name: "android.hardware.foo@1.0-service",
    vendor: true, // /vendor/bin/ 으로 빌드 타깃 지정
    init_rc: ["android.hardware.foo@1.0-service.rc"],
    shared_libs: ["libbinder_ndk"],
}

// 2. Product 파티션 전용 OEM 앱 모듈
android_app {
    name: "OEMCustomLauncher",
    product_specific: true, // /product/app/ 으로 빌드 타깃 지정
    certificate: "platform",
}

// 3. System Ext 파티션 전용 프레임워크 확장 모듈
java_library {
    name: "com.oem.framework.extension",
    system_ext_specific: true, // /system_ext/framework/ 로 빌드 타깃 지정
}
```

---

### 관찰 가능한 증거 (Observable Evidence)

1. **adb shell 마운트 정보 및 파티션 용량 확인**:
   ```bash
   adb shell df -h /system /system_ext /product /vendor /odm
   ```
2. **파티션별 파일 저장 위치 스캔**:
   ```bash
   adb shell ls -ld /system /system_ext /product /vendor /odm
   # Example output:
   # drwxr-xr-x  root root /system
   # drwxr-xr-x  root root /product -> /system/product (or dedicated block device)
   # drwxr-xr-x  root root /vendor -> /dev/block/mapper/vendor
   ```

---

### 판단 기준

- 파일 위치는 "누가 소유하고 언제 업데이트하는가"의 결정이다.
- vendor/odm 변경은 HAL, VINTF, sepolicy 와 함께 검증한다.
- product/system_ext 변경은 privileged app, sysconfig, permission allowlist, overlay 정책을 같이 본다.
- partition 경계가 애매한 기능은 update 주체와 compatibility 책임부터 정한다.

관련 노트: [Android 플랫폼 모듈화는 system, vendor, kernel 업데이트 경계를 층위별로 나눈다](../../platform-modularity/platform-modularity/android-platform-modularity-splits-update-boundaries-by-system-layer.md)

