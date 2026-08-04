---
title: vendor-kernel-modules-load-through-first-stage-init-boundaries
tags: [android, android/boot, android/gki, android/kernel]
aliases: [Vendor Kernel Modules, modules.load, first-stage init]
date modified: 2026-08-04 15:52:00 +09:00
date created: 2026-07-31 23:45:00 +09:00
---

## Vendor kernel module은 first-stage init 경계에서 로드된다

상위 문서: [Kernel contracts](kernel-contracts.md)

Generic Kernel Image(GKI) 환경에서 범용 코어 커널(`boot.img`)은 SoC 칩셋 특화 드라이버나 스토리지/디스플레이 컨트롤러 드라이버를 커널 바이너리에 직접 내장하지 않는다.

대신 부팅 초기 필수 드라이버 모듈(`.ko`)은 `vendor_boot` 파티션의 First-stage RAMDisk에 탑재되며, 부팅 1단계 프로세스인 **First-stage init**이 `modules.load` 및 `modules.dep` 종속성 순서에 따라 커널 동적 모듈 로드(`modprobe` / `init_module`)를 수행한다.

---

### 메커니즘: 2단계 커널 모듈 동적 로드 파이프라인

```mermaid
graph TD
    A["Bootloader -> GKI boot.img Launch"] --> B["First-stage init Execution"]
    
    subgraph First-Stage Load (vendor_boot RAMDisk)
        B --> C["Read /lib/modules/modules.load"]
        C --> D["Load Critical Drivers\n(Storage, UFS/eMMC, Pinctrl, Regulator .ko)"]
        D --> E["Mount system.img, vendor.img, vendor_dlkm.img"]
    end
    
    subgraph Second-Stage Load (vendor_dlkm)
        E --> F["Second-stage init Execution"]
        F --> G["Read /vendor_dlkm/etc/modules.load"]
        G --> H["Load Non-critical Drivers\n(GPU, Camera, Audio, Wi-Fi, Sensor .ko)"]
    end

    H --> I["Full Userspace System Boot"]
```

1. **First-Stage Module Loading**: 스토리지, 파워 관리, 디스플레이 컨트롤러 등 `system.img` 및 `vendor.img` 파티션을 마운트(`first_stage_mount`)하기 위해 반드시 필요한 최소 드라이버 모듈을 `vendor_boot` 파티션 램디스크에서 로드.
2. **Second-Stage Module Loading**: 파티션 마운트 완료 후 GPU, 카메라, 센서, Wi-Fi 등 대용량 미디어/통신 드라이버 모듈을 `vendor_dlkm` 파티션에서 마운트하여 로드.

---

### First-Stage init의 `modules.load` 구성 및 modprobe 실행 예시

```text
# vendor_boot RAMDisk 내 /lib/modules/modules.load 예시
pinctrl-msm.ko
qcom-pdc.ko
ufs-qcom.ko
phy-qcom-ufs.ko
```

```cpp
#// system/core/init/modprobe_utils.cpp (First-stage init 모듈 로드 루프 예시)
#include <modprobe/modprobe.h>

bool LoadKernelModules(const std::string& modules_dir) {
    Modprobe m({modules_dir});
    // modules.load 파일을 읽어 모듈 의존성 역순에 따라 sys_finit_module 실행
    return m.LoadModulesFromListFile("modules.load");
}
```

---

### 실무 규칙

- First-stage RAMDisk에 탑재되는 모듈 목록(`vendor_boot` 파티션)에 스토리지/버스 드라이버 모듈이 누락되면 `first_stage_mount` 단계에서 `system.img` 파티션을 찾지 못해 커널 Panic 또는 Bootloop가 발생한다.
- 커널 모듈 작성 시 `MODULE_SOFTDEP("post: msm_drm")` 선언을 활용하여 모듈 간 의존성 관계를 타이트하게 정의해야 init 이 정방향으로 심볼을 링크할 수 있다.

---

### 관측 가능한 증거 (Observable Evidence)

1. **First-Stage 및 Second-Stage 모듈 로드 로그 확인**:
   ```bash
   adb shell dmesg | grep -E "init: Loaded kernel module|modprobe"
   # [ 0.812345] init: Loaded kernel module /lib/modules/ufs-qcom.ko
   ```
2. **Loaded Module 종속성 맵(`modules.dep`) 조회**:
   ```bash
   adb shell cat /vendor_dlkm/etc/modules.dep
   # msm_drm.ko: drm_kms_helper.ko drm.ko
   ```

---

### 관련 문서

- [First-stage init builds minimal filesystem](../../boot-and-runtime/init-service-contracts/first-stage-init-builds-minimal-filesystem-for-second-stage.md)
- [GKI는 공통 core kernel과 vendor module을 분리한다](gki-splits-generic-core-from-vendor-modules.md)
- [Kernel debugging은 logcat 이전의 신호에서 시작한다](kernel-debugging-starts-before-logcat-with-bootloader-dmesg-and-trace.md)

공식 문서: [AOSP Kernel Module Support](https://source.android.com/docs/core/architecture/kernel/kernel-module-support)

