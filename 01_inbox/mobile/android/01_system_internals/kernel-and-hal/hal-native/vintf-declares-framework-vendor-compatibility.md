---
title: vintf-declares-framework-vendor-compatibility
tags: [android, android/native, android/system-internals]
aliases: [Vendor Interface Object, VINTF, Manifest, Compatibility Matrix]
date modified: 2026-08-04 15:52:00 +09:00
date created: 2026-07-31 23:58:00 +09:00
---

## VINTF는 framework/vendor 호환성을 manifest와 matrix로 선언한다

상위 문서: [HAL native contracts](hal-native.md)

VINTF(Vendor Interface Object)는 Framework(`system.img`)와 Device Vendor(`vendor.img`) 간의 런타임 및 부팅 타임 인터페이스 호환성을 XML 기반의 **Manifest(제공 능력 선언)**와 **Compatibility Matrix(필수 요구사항 선언)** 쌍으로 검증하는 호환성 계약 정본이다.

VINTF 체계는 디바이스가 런타임에 불완전한 하드웨어 HAL 서비스에 접근하여 무응답 크래시가 발생하는 것을 사전에 차단하며, OTA Update 시 교체될 `system.img` 프레임워크가 기존 `vendor.img` 하드웨어와 바이너리 호환이 가능한지 부팅 직후 `checkvintf`를 통해 검증한다.

---

### 메커니즘: Dual Directional Manifest & Matrix Matching

```mermaid
graph LR
    subgraph Device Vendor Side (vendor.img)
        A1["Vendor Manifest\n(/vendor/etc/vintf/manifest.xml)\n'What Vendor Provides'"]
        A2["Vendor Compatibility Matrix\n(/vendor/etc/vintf/compatibility_matrix.xml)\n'What Vendor Requires'"]
    end

    subgraph Framework Side (system.img)
        B1["Framework Compatibility Matrix\n(/system/etc/vintf/compatibility_matrix.xml)\n'What Framework Requires'"]
        B2["Framework Manifest\n(/system/etc/vintf/manifest.xml)\n'What Framework Provides'"]
    end

    A1 <-->|"Match Check"| B1
    A2 <-->|"Match Check"| B2
```

1. **Vendor Manifest vs Framework Matrix (주방향 검증)**: Device Vendor가 제공하는 HAL 서비스/인스턴스(`manifest.xml`)가 Framework가 실행 시 필요로 하는 필수 HAL 버전(`compatibility_matrix.xml`)을 모두 만족하는지 검증.
2. **Framework Manifest vs Vendor Matrix (역방향 검증)**: Framework가 내보내는 System API/VNDK 버전이 Vendor 데몬이 요구하는 조건과 일치하는지 검증.

---

### VINTF `manifest.xml` 및 `compatibility_matrix.xml` XML 선언 예시

```xml
<!-- 1. Device Vendor Manifest 예시 (/vendor/etc/vintf/manifest.xml) -->
<manifest version="2.0" type="device">
    <hal format="aidl">
        <name>android.hardware.light</name>
        <version>2</version>
        <interface>
            <name>ILights</name>
            <instance>default</instance>
        </interface>
    </hal>
</manifest>
```

```xml
<!-- 2. Framework Compatibility Matrix 예시 (/system/etc/vintf/compatibility_matrix.xml) -->
<compatibility-matrix version="2.0" type="framework">
    <hal format="aidl" optional="false">
        <name>android.hardware.light</name>
        <version>1-2</version>
        <interface>
            <name>ILights</name>
            <instance>default</instance>
        </interface>
    </hal>
</compatibility-matrix>
```

---

### 실무 규칙

- VINTF Manifest에 HAL 인터페이스를 등록하지 않은 상태에서 `AServiceManager_addService()`를 호출하면, Android 11+의 `servicemanager`가 VINTF 미등록(Undeclared VINTF Interface) 보안 정책에 따라 해당 서비스 등록을 즉시 거부한다.
- 벤더 HAL 개발 시 `.aidl` 선언 파일에 `@VintfStability` 어노테이션을 부여하고 `Android.bp`에 `stability: "vintf"`를 지정해야 VINTF 빌드 및 런타임 호환성 빌드 검증을 통과할 수 있다.

---

### 관측 가능한 증거 (Observable Evidence)

1. **`checkvintf` CLI 도구를 통한 VINTF 호환성 결과 검증**:
   ```bash
   adb shell checkvintf
   # Read VINTF metadata from device...
   # Compatible: SUCCESS
   ```
2. **`vintf` 런타임 정보 dump 출력 확인**:
   ```bash
   adb shell dumpsys vintf
   # Target FCM Version: 202404
   # HALs provided by device: android.hardware.light@2
   ```

---

### 관련 문서

- [Treble은 system과 vendor 업데이트 경계를 stable interface로 분리한다](treble-separates-system-and-vendor-through-stable-interfaces.md)
- [AIDL HAL은 신규 HAL의 현재 stable interface 선택지다](aidl-hal-is-current-stable-interface-for-new-hals.md)
- [HAL은 framework와 vendor 구현 사이의 안정된 userspace contract다](hal-is-stable-userspace-between-framework-and-vendor.md)

공식 문서: [AOSP VINTF Object Overview](https://source.android.com/docs/core/architecture/vintf)

