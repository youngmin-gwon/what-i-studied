---
title: android-os-development-guide
tags: []
aliases: []
date modified: 2026-04-05 17:43:12 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [[mobile-security]] > [[android-os-development-guide]]

### Android OS Development: AOSP Guide

AOSP(Android Open Source Project)를 기반으로 직접 기기 OS 를 커스텀하고 빌드할 때 필요한 핵심 가이드라인을 제공합니다.

단순히 소스를 빌드하는 것을 넘어, **Mainline 모듈(APEX)**화 및 최신 빌드 시스템(Soong/Ninja)의 동작 원리를 파악하여 제조사 수준의 커스터마이징 역량을 확보하는 것이 목표입니다.

---

#### 💡 Context: OS 개발의 복잡성 관리

안드로이드 OS 개발은 수천 개의 깃 레포지토리와 복잡한 빌드 의존성을 관리해야 합니다. 낯선 용어는 [[android-glossary]] 를 먼저 확인하는 것을 권장합니다.

---

#### 소스와 빌드
- `repo init/sync` 로 소스를 받는다. `source build/envsetup.sh` 후 `lunch` 로 타깃을 고른다.
- Soong/ninja 가 빌드를 수행한다. 모듈 정의는 Android.bp 에 적는다.
- 빌드 산출물: system/vendor/product 이미지, [[android-glossary#boot-image|boot/vendor_boot]], target-files.zip(OTA 재료).

#### APEX/Mainline
- [[android-glossary#apex|APEX]] 는 OS 일부를 모듈로 만들어 따로 서명·업데이트한다 (ART/Media/Permissions 등).
- `apexer/deapexer/apksigner` 로 만들고 검사한다.

#### 기기 Bring-up
- `device/<vendor>/<product>` 트리에 BoardConfig, init 스크립트, fstab, [[android-glossary#selinux|sepolicy]], 오버레이를 둔다.
- VINTF manifest/matrix 가 HAL 버전을 맞추는지 확인한다.
- [[android-glossary#verified-boot|AVB]] 키와 [[android-glossary#boot-image|boot]] 구성이 맞지 않으면 부팅이 막힌다.

#### 커널
- GKI+ 벤더 모듈 구조를 쓴다. defconfig 와 dtb/dtbo 를 관리한다.
- ftrace/perf/Perfetto 로 커널 이벤트를 본다. pstore/ramoops 로 패닉 로그를 확인한다.

#### init/서비스
- init.rc 로 서비스와 트리거를 정의한다. APEX 모듈도 자신의 rc 를 자동으로 가져온다.
- property/selabel/권한이 맞지 않으면 서비스가 뜨지 않는다. [android-init-and-services](../01_system_internals/android-init-and-services.md) 참고.

#### HAL/드라이버
- AIDL/HIDL HAL 인터페이스를 정의하고, binderized 서비스로 등록한다.
- VTS/CTS 로 인터페이스와 보안이 맞는지 검증한다.

#### 테스트
- `atest` 로 단위/통합 테스트, CTS/VTS 로 호환성 테스트.
- fuzzing/sanitizer(ASAN/UBSAN/TSAN/HWASAN) 로 안전성을 올린다.

#### 서명/배포
- releasekey/testkey/platform 등 키를 관리한다. OTA 는 sign_target_files_apks → ota_from_target_files 순으로 만든다.
- [[android-glossary#ota|OTA]] 는 A/B/Virtual A/B 를 고려해 payload 를 만든다.

#### 디버깅/현장 대응
- [[android-glossary#adb|ADB]]/fastboot, [[android-glossary#bugreport|bugreport]], Perfetto/trace 로 문제를 모은다.
- crash/ANR/selinux 거부/boot 실패는 로그를 모아 순서대로 확인한다.

#### CI/CD 힌트
- Lint/포맷/단위테스트를 미리 돌려 실패를 빠르게 잡는다.
- 빌드/테스트/OTA 산출물/심볼을 아카이브해 추적성을 확보한다.

#### 링크

[android-customization-and-oem](../01_system_internals/android-customization-and-oem.md), [android-hal-and-kernel](../01_system_internals/android-hal-and-kernel.md), [android-boot-flow](../01_system_internals/android-boot-flow.md), [android-adb-and-images](../06_testing_performance/android-adb-and-images.md).
