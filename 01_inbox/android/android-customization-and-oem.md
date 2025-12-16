---
title: android-customization-and-oem
tags: [android, android/customization, android/oem, aosp]
aliases: []
date modified: 2025-12-16 15:41:43 +09:00
date created: 2025-12-16 15:25:24 +09:00
---

## Customization & OEM Workflows android android/oem android/customization aosp

[[android-hal-and-kernel]] · [[android-boot-flow]] · [[android-evolution-history]]

### AOSP→Product 파이프라인
- AOSP 코드 + device/vendor/odm 전용 레이어 추가. BoardConfig/Soong/Bazel build rules 로 장치별 설정.
- GMS 인증 (CTS/VTS/GTS/STS) 통과가 상용 출시 조건. VTS 가 HAL 안정성, CTS 가 API 적합성 검증.
- Product partition(system_ext/product) 로 SKU/캐리어별 기능 분리. feature flag 및 overlays 활용.

### System Properties/Overlays
- `build.prop`/`default.prop`/`prop.default`/`vendor/build.prop` 등에 플래그 배치. runtime setprop 는 일시적.
- RRO(Runtime Resource Overlay): Overlay packages 로 UI/behavior 스위칭. config_*, booleans/dimens. Fabricated overlays 로 동적 적용.
- Feature flags(DeviceConfig/SettingsProvider) 와 서버 기반 실험을 조합해 롤아웃 제어.
- CarrierConfig overlays 와 `com.android.internal.telephony.csc` 룰은 통신사별 정책에 결정적.

### Kernel/Driver 커스터마이징
- Device tree/DTBO 로 하드웨어 변형 대응. GKI + vendor modules 구조.
- Power tuning: cpufreq governor, thermal throttling, HAL power hints, battery saver integration.
- Memory: zram 크기/알고리즘, cgroup/lmkd adj, swappiness 조정.
- Camera/Display 파이프라인: color calibration, auto brightness curve, display refresh policy.\n

### System Service 확장
- privileged/system app + signature permission 으로 플랫폼 기능 추가. system API/backports 를 신중히 사용.
- Mainline 모듈이 늘어나면서 OEM customizing surface 는 Settings overlays/SystemUI plugins 정도로 제한.
- `com.android.internal` API 호출은 hidden API enforcement 우회 필요하므로 향후 호환성 문제를 초래.
- SystemUI plugin/overlay, Quick Settings tiles, status bar layout 조정. lockscreen/Keyguard custom affordance.

### Boot/Recovery 커스터마이징
- Splash/bootanimation.zip. Verified Boot keys 교체 (bootloader unlock 정책).
- Recovery UI 커스터마이징, fastbootd adoption for dynamic partitions.

### Update/OTA 전략
- A/B OTA 설정, payload properties. Preload 앱의 data migration/rollback strategy.
- Incremental OTA vs full OTA. Delta payload 생성 시 block-level vs file-level.
- Treble 분리 덕분에 framework-only OTA 가 가능하지만 vendor API 호환성 (VINTF) 을 만족해야 함.
- update_engine, update_verifier 로그를 모니터링하고 resume-on-reboot/payload metadata 관리.

### Enterprise/MDM 커스터마이징
- DevicePolicyManager + OEM-specific policy. Work profile(profiles) 분리. COSU/Lock task mode.
- Zero-touch/Knox/EMM integration. Attestation/Key provisioning.
- OEM config policy 앱으로 키 재생성/바이오 인증 정책 배포. SafetyNet/Integrity API 통과 필요.
- Corp/Consumer 분리: work profile 에서 cross-profile intent filter 제어, kiosk 앱은 lock task + device owner 정책.
- Managed provisioning flow 커스터마이즈, QR/NFC enrollment, enrolment network constraints.

### Regionalization/Carriers
- CarrierConfig overlays, APN database, IMS provisioning. eSIM/DSDS 설정.
- Locale/Region-based features toggling via RRO + server configs.
- SAR/EMF/Regulatory constraints reflected via config overlays. Emergency services/E911 requirements.

### 디버그 빌드 타입
- user/userdebug/eng 차이: root access, adb permissiveness, SELinux permissive 가능 여부, strictmode.
- userdebug 는 개발/QA 에 적합; eng 는 완전 오픈하지만 보안 취약.
- factory/eng builds may include test-keys; release signing changes OTA compatibility. test harness builds for CTS.\n

### Mainline 영향
- ART/Media/NNAPI/PermissionController/Statsd 등 APEX 모듈화. OEM 커스터마이징 범위 축소, 업데이트 속도 증가.
- GSI(Generic System Image) 로 Treble 적합성 테스트. vendor 이미지와 프레임워크 분리.
- Modular system components(Network Stack, ExtServices 등) 업데이트로 vendor 의존성 감소. overlay 공간이 줄어드는 대신 안정성 향상.
- OEM feature flags 는 DeviceConfig/SettingsProvider/back-end config 를 조합하여 OTA 없이 기능 온오프.

### 그래프 링크
- [[android-architecture-stack]], [[android-hal-and-kernel]], [[android-boot-flow]], [[android-adb-and-images]], [[android-security-and-sandboxing]].
