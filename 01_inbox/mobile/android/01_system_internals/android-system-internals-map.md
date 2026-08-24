---
title: android-system-internals-map
tags: ["android", "android/system-internals"]
aliases: ["Android System Internals Map 은 7개 하위 클러스터를 부팅부터 커스터마이징까지 순서대로 연결하는 통합 지도다"]
date modified: 2026-08-06 15:00:00 +09:00
date created: 2026-08-04 18:00:00 +09:00
---

## Android System Internals Map 은 7개 하위 클러스터를 부팅부터 커스터마이징까지 순서대로 연결하는 통합 지도다

`01_system_internals` 는 앱 코드가 호출하는 API 가 아니라 그 API 뒤에서 실제로 실행되는 플랫폼 계층을 다룬다. 전원이 켜지는 순간부터 앱 프로세스가 화면에 첫 frame 을 그리기까지, 그리고 OEM 이 그 플랫폼을 커스터마이징하는 지점까지를 7개 클러스터로 나눈다. 이 지도가 신설되기 전에는 각 클러스터가 개별 hub 만 있고 폴더 전체를 조망하는 진입점이 없어 Foundation map 에서 2 단계 이내 도달이 보장되지 않았다(Phase 1 coverage matrix 지적, Phase 9 항목 1 로 해소).

### 하위 클러스터와 hub 경로

| 클러스터 | hub 노트 | 다루는 범위 |
|---|---|---|
| [boot-and-runtime](boot-and-runtime/android-boot-and-runtime.md) | `boot-and-runtime/android-boot-and-runtime.md` | bootloader/AVB 검증부터 init, Zygote/ART, system_server 까지의 부팅·런타임 초기화 체인 |
| [ipc-and-process](ipc-and-process/binder-ipc.md) | `ipc-and-process/binder-ipc.md` | Binder 가 중재하는 process 경계, transaction lifetime, AIDL, oneway/thread pool |
| [kernel-and-hal](kernel-and-hal/android-kernel-runtime.md) | `kernel-and-hal/android-kernel-runtime.md` (커널) + `kernel-and-hal/hal-native-boundary.md` (HAL/native) | Linux kernel 이 Android 플랫폼 정책과 만나는 지점, HAL/Treble/VINTF 와 NDK/JNI 경계 |
| [graphics-and-media](graphics-and-media/android-graphics-media-runtime.md) | `graphics-and-media/android-graphics-media-runtime.md` | Surface/BufferQueue, SurfaceFlinger/HWC 합성, 미디어 파이프라인의 버퍼 소유권과 VSync 마감 |
| [connectivity](connectivity/android-connectivity.md) | `connectivity/android-connectivity.md` | ConnectivityService, NetworkPolicyManager, netd, kernel 라우팅까지의 4개 계층 네트워크 가용성 계약 |
| [platform-modularity](platform-modularity/android-platform-modularity.md) | `platform-modularity/android-platform-modularity.md` | APEX/Mainline module 을 통한 OS 배포와 Google Play system update |
| [platform-customization](platform-customization/platform-customization.md) | `platform-customization/platform-customization.md` | AOSP/GMS/OEM 계층, product/vendor/system_ext 분리, 서명·CTS 호환성 |

### 읽는 순서

1. **boot-and-runtime** 로 시작한다. 전원이 켜진 뒤 bootloader, kernel, init, Zygote, system_server 가 어떤 순서로 서로를 신뢰하고 실행 권한을 넘기는지가 이후 모든 클러스터의 전제가 된다.
2. **ipc-and-process** 로 이동한다. system_server 와 앱 프로세스가 분리된 순간부터 둘 사이의 모든 통신은 Binder 를 거치므로, 이후 connectivity/graphics 클러스터에서 "왜 system_server 를 거쳐야 하는가"를 이해하는 전제가 된다.
3. **kernel-and-hal** 로 내려간다. Binder 자체가 kernel driver 이고, HAL 이 kernel 과 framework 사이의 vendor 경계이므로 IPC 다음에 읽는다.
4. **graphics-and-media** 와 **connectivity** 는 이 시점부터 순서 상관없이 읽어도 된다. 둘 다 "framework service 가 Binder 로 native/kernel 계층을 제어한다"는 동일한 패턴을 다른 대상(화면 합성 vs 네트워크 라우팅)에 적용한 사례다.
5. **platform-modularity** 로 넘어간다. 지금까지 읽은 모든 서비스가 하나의 monolithic OS 이미지가 아니라 APEX 로 분리 배포될 수 있다는 점을 이해한다.
6. **platform-customization** 을 마지막에 읽는다. 이 클러스터는 지금까지의 전체 스택을 AOSP 소스에서 실제 기기 이미지로 조립하는 OEM/platform 엔지니어 관점이며, 앱 개발자에게는 "왜 내 앱이 기기마다 다르게 동작하는가"를 판단하는 배경 지식으로만 필요하다.

### 포함하지 않는 범위

- 앱이 직접 호출하는 Jetpack API 사용법은 다루지 않는다. `Context.getSystemService()` 이후의 앱 관점 서비스 사용은 [App Framework Map](../02_app_framework/android-app-framework-map.md) 또는 `04_system_services` 로 간다.
- Compose/View 렌더링의 앱 코드 관점([recomposition](../02_app_framework/jetpack-compose/runtime/recomposition.md), layout modifier)은 다루지 않는다. graphics-and-media 는 Surface 이하의 native 합성만 다루고, 그 위의 UI 코드는 [App Framework Map](../02_app_framework/android-app-framework-map.md) 의 jetpack-compose 클러스터로 간다.
- 커스텀 ROM 빌드 실습 절차나 특정 SoC vendor 의 개별 driver 소스는 다루지 않는다. platform-customization 은 계약과 경계까지만 설명한다.

### 문제 분류

- **부팅이 안 되거나 부팅 루프에 빠진다**: boot-and-runtime 의 부팅 흐름 계약(AVB, bootconfig)을 먼저 본다.
- **앱 프로세스 생성이 느리거나 시스템 서비스 호출이 SecurityException/ANR 로 실패한다**: boot-and-runtime 의 system_server 계약과 ipc-and-process 의 caller UID/thread pool 계약을 함께 본다.
- **특정 HAL/native daemon 이 죽거나 기기별로 동작이 다르다**: kernel-and-hal 의 HAL/VINTF 경계와 platform-customization 의 product/vendor 분리를 함께 본다.
- **화면이 끊기거나(jank) 프레임이 드랍된다**: graphics-and-media 의 BufferQueue/VSync 계약을 본다. UI state 쪽 원인은 [App Framework Map](../02_app_framework/android-app-framework-map.md) 의 jetpack-compose 성능 클러스터와 함께 본다.
- **네트워크 요청이 기대와 다르게 차단되거나 default network 가 바뀐다**: connectivity 의 NetworkPolicyManager/netd 계층 구분을 본다.
- **보안 패치나 특정 모듈만 별도로 업데이트된다**: platform-modularity 의 APEX/Mainline 계약을 본다.

### 관련 지도

- [Android Foundation Map](../00_foundations/android-foundation-map.md) — 전체 canonical area 로 돌아가는 최상위 지도.
- [Learning Spine 2장](../00_foundations/learning-spine/02-android-platform-execution-layers-and-call-paths.md) — 앱 API 호출이 framework, Binder, native service, kernel로 내려가는 실행 계층.
- [Learning Spine 6장](../00_foundations/learning-spine/06-main-thread-binder-coroutine-and-durable-work-lifetime.md) — main thread와 Binder thread의 독립 수명·실패 경계.
- [Learning Spine 7장](../00_foundations/learning-spine/07-input-resource-selection-and-display-frame.md) — input에서 SurfaceFlinger frame까지의 렌더링 경로.
- [Learning Spine 12장](../00_foundations/learning-spine/12-compatibility-update-and-form-factor.md) — system image, Mainline, target SDK와 form factor compatibility.
- [App Framework Map](../02_app_framework/android-app-framework-map.md) — 이 지도가 다루는 native/platform 계층 위에서 앱 코드가 어떻게 그 계층을 호출하는지.
