---
title: android-ecosystem-conceptual-spine-preparation
tags: ["android", "coverage-audit", "knowledge-base", "learning-spine"]
aliases: []
date modified: 2026-08-04 16:55:12 +09:00
date created: 2026-08-03 17:22:12 +09:00
---

## Android 생태계 개념 Learning Spine 준비

## 목적

이 문서는 Android Studio 설치나 첫 앱 제작 절차를 설명하는 follow-along 계획이 아니다. Android 생태계를 처음 조망하는 개발자가 다음을 하나의 모델로 연결하도록 만드는 Learning Spine 의 준비 자료다.

- Android 라는 제품과 플랫폼을 누가 만들고 배포하는가?
- 앱 소스는 어떤 산출물로 변환되어 기기에 설치되는가?
- 설치된 패키지는 어떻게 시스템에 등록되고 프로세스와 component 로 실행되는가?
- framework API 호출은 언제 Binder, system service, HAL 과 kernel 을 통과하는가?
- UI state 는 어떻게 window, Surface 와 display 의 실제 frame 으로 이어지는가?
- 앱의 identity, lifetime, permission, background execution 과 데이터 복구는 어떻게 연결되는가?
- 같은 앱이 OS 버전, OEM, Google service surface 와 form factor 에 따라 왜 다르게 동작하는가?

대상 독자는 일반적인 프로그래밍 개념과 앱 코드 읽기에 익숙하지만 Android 생태계의 구성과 내부 인과관계는 모르는 사람이다. Kotlin 문법, IDE 설치, 버튼 위치, 예제 앱 따라 만들기는 범위에 포함하지 않는다.

## 중심 모델

Android 는 하나의 SDK 나 하나의 운영체제 이미지로 이해하면 안 된다. 다음 다섯 관점을 겹쳐 봐야 한다.

### 주체

- AOSP 는 공개 플랫폼 소스와 호환 계약의 기반을 제공한다.
- Google 은 Android API 문서와 도구, Jetpack/AndroidX, Google Play services, Google Play 배포 인프라 등 서로 다른 surface 를 제공한다.
- SoC vendor 는 chipset, firmware, kernel 과 vendor 구현의 일부를 공급한다.
- OEM/ODM 은 board 와 product 구성, system image, system app, 정책, 업데이트를 기기 제품으로 통합한다.
- 앱 개발자와 library 제작자는 public API 및 배포 계약 위에 APK/AAB 와 dependency 를 만든다.
- store/distributor 는 AAB 에서 기기별 APK 집합을 생성하거나 이미 만들어진 APK 를 전달한다.
- 기기의 PackageInstaller/PackageManager 경계는 전달받은 APK 집합을 검증하고 설치된 package 상태로 만든다.

### 산출물

앱과 library 의 산출물 흐름은 분리한다.

- 앱: `source/resource/manifest/dependency → compile/resource processing/DEX/package → APK 또는 AAB → 서명·배포 → device용 APK → 설치된 package`
- library: `source/resource/manifest/public API → AAR → 소비하는 앱의 build dependency`

AAR 은 보통 앱 build 의 입력이지 설치 산출물이 아니다. AAB 는 게시 형식이고 APK 는 기기 설치 형식이다. 플랫폼 image, APEX/Mainline module, app APK 도 모두 Android 에 존재하지만 소유자, 업데이트 경계와 실행 권한이 다르다.

### 실행 계층

- In-process library 경로: `app code → Jetpack/AndroidX 또는 다른 library → app process 안의 결과`
- Platform service 경로: `app code → android.* manager/proxy → Binder → system_server/native service → 필요하면 HAL/kernel/hardware`
- Native app 경로: `app Kotlin/Java ↔ JNI bridge → 앱 native library → NDK stable API/ABI 등 허용된 native platform surface`
- Google service 경로: `app code → Google client library → 기기의 Google runtime/service 또는 backend`

모든 호출이 Binder 나 hardware 까지 내려가지 않는다. 각 장은 실제 요청이 어느 경로를 택하고 어느 계층이 identity, policy, state 와 hardware access 를 소유하는지 구분해야 한다.

### 독립적인 lifetime

- 설치된 package identity 와 사용자·profile 별 app data
- Linux process 와 ART instance
- task 와 back stack
- Activity, Service, Receiver, Provider instance
- [viewmodel](../02_app_framework/viewmodel.md), saved state 와 persistent state
- Compose composition, View tree, Window 와 Surface
- coroutine 의 취소 가능한 작업 lifetime
- Service/foreground service 의 component 와 사용자 가시성 계약
- WorkManager/JobScheduler 의 durable scheduling 계약

이 lifetime 들은 함께 시작하거나 끝난다고 가정할 수 없다. configuration change, task removal, component destroy, process death, force-stop 과 uninstall 의 차이는 이 모델로 설명한다.

### 호환성 축

- `compileSdk`: 빌드 시 참조할 수 있는 API surface
- `minSdk`: 지원 가능한 runtime 하한과 fallback 책임
- `targetSdk`: 앱이 선언한 동작 계약과 compatibility behavior 기준
- device API/SDK extension: 실행 중 실제 API availability
- Jetpack/library version: 앱에 포함되는 library 계약과 자체 최소 요구사항
- Play policy: 플랫폼 runtime 과 별개인 제출·배포 조건
- Mainline, OEM 구현과 device feature: API level 하나로 환원되지 않는 실행 환경

## 생태계 개념 Coverage Matrix

| 개념 축 | 현재 판정 | 재사용할 주요 정본 | Learning Spine 에서 새로 연결할 내용 |
| --- | --- | --- | --- |
| AOSP, Google, OEM, SoC vendor | 원자 자료 있음, 산업 생태계 서사 없음 | [Platform customization contracts](../01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md), [HAL/native boundary](../01_system_internals/kernel-and-hal/hal-native-boundary.md) | AOSP release 에서 vendor/OEM 제품, compatibility test, GMS 와 사용자 기기까지의 책임 흐름 |
| Platform SDK, Jetpack, Play services | 큰 공백 | [Jetpack architecture map](../02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture-map.md) 과 개별 library 노트 | OS 내장 API, 앱에 포함되는 AndroidX, Google 서비스 client/runtime surface 의 차이 |
| Gradle/AGP 와 build artifact | 개별 계약 강함, 변환 파이프라인 약함 | [Packaging and deployment](../03_packaging_deployment/android-packaging-deployment.md), [Gradle contracts](../03_packaging_deployment/build/gradle/gradle-build-contracts/gradle-build-contracts.md) | manifest/resource/dependency merge, compile, DEX, package, shrink, sign 의 인과 흐름과 실패 경계 |
| Resource 와 runtime configuration | 큰 공백 | [Configuration change](../02_app_framework/architecture/app-components/app-component-contracts/configuration-change-recreates-activity-but-not-all-screen-state.md), [RRO](../01_system_internals/platform-customization/platform-customization-contracts/rro-changes-resources-without-rebuilding-target-apk.md) | resource merge/AAPT2/ID 와 table, locale·density·night mode·window 별 선택, configuration change, OEM overlay 의 관계 |
| APK/AAB, signing, Play, install/update | 게시·서명 강함, device install 공백 | [Release distribution contracts](../03_packaging_deployment/distribution/release-distribution-contracts/release-distribution-contracts.md), [Play Delivery contracts](../03_packaging_deployment/distribution/play-delivery-contracts/play-delivery-contracts.md) | distributor 와 installer 분리, PackageInstaller/PackageManager 검증, numeric appId·사용자별 UID/data/component 등록, sideload/store 의 공통 설치 경계 |
| API level 과 호환성 | 원자 자료 강함, 통합 계산 모델 부족 | [Android release history](../00_foundations/history/android-release-history.md), [Platform modularity](../01_system_internals/platform-modularity/android-platform-modularity.md) | compile/min/target/device/extension/library/Play policy/OEM feature 를 한 판단 모델로 결합 |
| Platform runtime stack | 계층별 정본 강함, 요청 왕복 서사 부족 | [Android System Map](../00_foundations/overview/android-system-map.md), [Boot and runtime](../01_system_internals/boot-and-runtime/android-boot-and-runtime.md), [IPC/process contracts](../01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md) | app 요청이 framework, Binder, system service, native/HAL/kernel 을 통과하고 결과를 받는 흐름 |
| Package, Manifest 와 component | 개별 개념 강함, 설치 등록과 실행 연결 부족 | [Android app components](../02_app_framework/architecture/app-components/android-app-components.md), [Intent/Manifest contracts](../02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md) | 설치 시 선언 등록, intent resolution, policy 판정, component entry 와 process start 의 관계 |
| Task, process, lifecycle 와 state | 개별 개념 강함, lifetime 통합 모델 없음 | [App component contracts](../02_app_framework/architecture/app-components/app-component-contracts/app-component-contracts.md), [Android state management](../02_app_framework/architecture/state-management/android-state-management.md) | task/process/component/ViewModel/composition/saved/persistent state 가 서로 독립인 이유 |
| Main thread, Binder 와 coroutine | Binder/coroutine 정본 강함, 공통 실행 모델 약함 | [IPC/process contracts](../01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md), [Coroutine contracts](../02_app_framework/data/async-flow/coroutines/coroutine-contracts.md) | main Looper 와 callback 직렬화, Binder thread pool, coroutine context/lifetime, OS scheduler 의 차이 |
| Input 에서 UI state, display 까지 | 출력 양 끝은 강함, 입력과 Window 중간 계층 공백 | [Android UI system](../02_app_framework/ui/system/android-ui-system.md), [Compose runtime](../02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md), [Graphics/media runtime](../01_system_internals/graphics-and-media/android-graphics-media-runtime.md) | input→dispatcher→Window→main queue→View·Compose event/state 와 state→render→Surface→SurfaceFlinger→display 의 상호작용 loop |
| Data, network 와 offline recovery | storage/connectivity 강함, 앱 데이터 순환 서사 부족 | [Android data layer map](../02_app_framework/data/android-data-layer-map.md), [Android connectivity](../01_system_internals/connectivity/android-connectivity.md) | remote protocol, repository, local source of truth, outbox, retry/idempotency, conflict/freshness 와 UI 관찰 |
| Background work 와 notification | 선택 모델 강함, end-to-end 기능 서사 부족 | [Background work contracts](../04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md), [Notification/messaging contracts](../04_system_services/background-and-notifications/notification-messaging-contracts/notification-messaging-contracts.md) | durable state→schedule→constraint/quota→중단/재시도→서버 동기화→notification→UI 복구 |
| Identity 와 security policy | 계층별 정본 강함, identity 와 독립 gate 의 통합 모델 부족 | [Security and privacy](../05_security_privacy/android-security-and-privacy.md), [Permission contracts](../05_security_privacy/permissions-and-sandbox/permission-contracts/permission-contracts.md) | package name/applicationId, signing identity, numeric appId, 사용자별 UID·data·grant 와 Binder caller, permission, AppOps, SELinux, server authorization 의 적용 경계 |
| System service 와 device capability | 공통 모델 작성 중, capability 폭 부족 | [System services and device capabilities](../04_system_services/android-system-services-and-device-capabilities.md) | feature discovery→manager/proxy→policy/service→HAL/hardware→callback/fallback 과 Google/OEM surface 구분 |
| Form factor 생태계 | large screen/XR 강함, 전체 coverage 부족 | [Platforms and form factors](../07_platforms/android-platforms-and-form-factors.md) | phone baseline 과 TV/Wear/Auto/Automotive/ChromeOS/XR 의 input, window, lifecycle, distribution 차이 |
| Testing, diagnostics 와 release feedback | 개별 도구와 원칙 강함, 운영 loop 부족 | [Performance and quality map](../06_testing_performance/performance/android-performance-quality-and-build-optimization.md) | 계약→재현 환경→log/state/trace→benchmark→regression test→device matrix→staged release/field signal |

## 가장 중요한 연결 공백

### 생태계 주체와 API surface

현재 문서는 AOSP, GMS, HAL, OEM customization 을 각각 설명하지만 다음 구분을 한 자리에서 제공하지 않는다.

| Surface | 주된 소유·배포 방식 | 앱에서 보이는 형태 |
| --- | --- | --- |
| Android platform API | OS/framework 에 포함, 기기 OS 와 함께 제공 | `android.*` API 와 system service |
| Android NDK native surface | 앱 native code 가 사용하는 stable native API/ABI | NDK API 와 native library. JNI 는 managed/native code 사이의 연결 방식이다. |
| Jetpack/AndroidX | 앱 dependency 로 선택하고 앱과 함께 배포 | lifecycle, Room, WorkManager, Compose 등 |
| Google Play services | Google 서비스가 있는 기기의 runtime 과 client library 가 협력 | location, identity 등 Google 제공 surface |
| OEM API/behavior | 특정 제조사 제품과 system image 에 종속 | vendor SDK, feature, 설정과 구현 차이 |

이 구분이 없으면 독자는 library update 와 OS update, public platform contract 와 Google/OEM capability 를 같은 것으로 오해한다.

### Source 에서 설치된 app identity 까지

필요한 개념 흐름은 다음과 같다.

`source + manifest + resource + dependency`

```plaintext
→ Gradle/AGP build 와 variant 결정
→ compile/resource processing/DEX/package
→ APK 또는 AAB
→ signing 과 distribution
→ device 용 APK 전달
→ installer 와 PackageManager 의 version/signature/manifest 검증
→ 문자열 package name/applicationId 와 signing lineage 관리
→ PackageManager 가 숫자 appId 할당
→ 사용자·profile 별 UID, 설치 상태, data directory 와 permission state
→ component registry
→ 이후 launch 와 update 의 identity 기준
```

현재 배포 노트는 Play 와 signing 에 강하지만 PackageManager 가 설치된 앱을 OS-visible entity 로 만드는 중간 연결이 약하다.

### 설치된 package 에서 첫 frame 까지

`launcher 또는 외부 요청`

```plaintext
→ Intent resolution 과 policy 판정
→ ATMS/AMS 가 task, component 와 process 상태 확인
→ 필요하면 Zygote 가 app process fork
→ ActivityThread 가 framework 에 attach
→ component instance 와 lifecycle callback
→ Window/ViewRoot 와 View 또는 Compose tree
→ measure/layout/draw 와 RenderThread
→ Surface/BufferQueue
→ SurfaceFlinger/HWC/display
```

이 흐름은 기존 원자 노트를 연결하는 대표 인과 서사이며 build, install, runtime, lifecycle 과 rendering 을 동시에 묶는다.

사용자 입력은 반대 방향에서 앱 상태로 들어온다.

`input device → kernel → InputReader/InputDispatcher → 대상 Window → app main queue → View/Compose event dispatch → state change`

따라서 UI 장은 입력과 출력의 두 직선을 별개로 끝내지 않고 `input → state transition → frame` 상호작용 loop 로 설명해야 한다.

### Framework API 에서 hardware capability 까지

`capability/feature 확인`

```plaintext
→ app 의 manager 또는 Google client API
→ local proxy 와 Binder/별도 runtime boundary
→ 해당 API 가 요구하는 caller UID, permission, AppOps, foreground/global state 판정
→ system/native service
→ HAL/driver/hardware
→ callback, error 또는 fallback
```

모든 device capability 가 같은 경로나 gate 를 사용하지 않는다는 점과 AOSP platform surface, Google service surface, OEM 구현을 구분해야 한다. Permission, AppOps, SELinux 와 server authorization 도 모든 호출이 정해진 순서로 통과하는 하나의 pipeline 이 아니라 API 와 resource 별로 서로 다르게 조합되는 독립 gate 다.

### 사용자 상태에서 durable recovery 까지

`UI event와 in-memory state`

```plaintext
→ repository 와 local transaction
→ durable source of truth/outbox
→ scheduler constraint 와 quota
→ network/server reconciliation
→ local state 갱신
→ UI observation 와 notification
```

process death, callback 누락과 중복 실행을 정상 조건으로 두고 idempotency 와 checkpoint 가 어디에 필요한지 설명한다.

## Learning Spine 12 장 후보

이 순서는 기존 계획의 12 개 주제를 생태계 개념 흐름에 맞게 구체화한 후보안이다.

| 장                                               | 핵심 질문                                                             | 장을 관통할 흐름                                                                                    |
| ----------------------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| 1. Android 생태계와 계약 surface                      | AOSP, Google, OEM, vendor, Jetpack, Play 는 각각 무엇을 소유하는가?          | AOSP release→vendor/OEM device→Google surface→app/runtime/distribution                       |
| 2. Android platform stack                       | 앱 요청은 어느 실행 계층을 통과하는가?                                            | app→framework→Binder/service→native/HAL→kernel/hardware                                      |
| 3. Source 에서 설치된 package 까지                     | 소스, resource 와 dependency 는 어떻게 OS 가 신뢰하는 package identity 가 되는가? | build/resource table→artifact→sign→distribute→install→package name·numeric appId·사용자별 UID 등록 |
| 4. Manifest 와 app component                     | OS 는 앱의 진입점과 capability 를 어떻게 발견하는가?                              | manifest 등록→intent resolution→component activation                                           |
| 5. Task, process, lifecycle 와 state             | 화면, component, process 와 사용자 상태는 왜 함께 죽지 않는가?                     | request→task/component→process→callback→destroy/recreate/recover                             |
| 6. Main thread, Binder, coroutine 과 작업 lifetime | 코드는 어느 thread/process 와 lifetime 에서 실행되는가?                        | Looper, Binder, coroutine, FGS 와 durable scheduler 의 병렬 책임 비교                                |
| 7. Input, resource 와 display frame              | 입력과 configuration 은 어떻게 UI state 와 실제 픽셀로 이어지는가?                  | input→Window/main queue→state→resource 선택/View·Compose→SurfaceFlinger→display                |
| 8. Data, storage, network 와 offline recovery    | 데이터는 어느 owner 가 보존하고 실패 뒤 어떻게 복구하는가?                              | remote/local source→outbox/sync→UI observation                                               |
| 9. Identity, permission 과 security boundary     | 권한이 있는데도 호출이 실패하는 이유는 무엇인가?                                       | package/signing/app ID 와 사용자별 UID→API·resource 별 독립 policy gate                              |
| 10. System capability 와 background execution    | 앱은 device 기능과 지속 작업을 어떤 시스템 계약으로 사용하는가?                           | discovery→service/hardware, durable state→scheduler→notification                             |
| 11. 관찰, 테스트와 품질 feedback                        | 보이지 않는 Android 상태를 어떤 증거로 확인하는가?                                  | reproduce→log/state/trace→test/benchmark→release/field feedback                              |
| 12. 호환성, update 와 form factor                   | 같은 앱이 기기와 버전에 따라 달라지는 축은 무엇인가?                                    | SDK axes→Mainline/OEM feature→form factor→distribution/testing matrix                        |

## 1 장 상세 목차: Android 생태계와 계약 접점(contract surface)

실제 본문: [Android 생태계와 계약 접점](../00_foundations/learning-spine/01-android-ecosystem-and-contract-surfaces.md)

### 장의 역할

1 장은 Android 를 API 모음이나 단일 운영체제 이미지로 소개하지 않는다. Android 라는 이름 아래 여러 주체, 산출물, 실행 환경과 배포 경로가 서로 다른 계약으로 연결된다는 전체 모델을 제공한다.

이 장을 먼저 읽어야 뒤 장에서 다음 혼동을 피할 수 있다.

- AOSP 와 Google Mobile Services(GMS)를 같은 제품으로 보는 혼동
- Android platform API 와 Jetpack/AndroidX 를 같은 업데이트 단위로 보는 혼동
- Google Play services 와 Google Play Store 를 같은 역할로 보는 혼동
- SDK 에서 보이는 API 와 실제 기기에서 사용할 수 있는 기능을 같은 것으로 보는 혼동
- OEM 차이를 모두 Android 파편화 또는 API 위반으로 보는 혼동
- 앱, 라이브러리, 시스템 이미지, Mainline 모듈과 Google 실행 환경의 배포 주체를 구분하지 않는 혼동

### 독자 전제와 범위

독자는 운영체제, 라이브러리, 프로세스, API, 패키지 같은 일반 소프트웨어 용어만 알고 있다고 가정한다. Android 앱을 빌드해 본 경험이나 AOSP 내부 지식은 요구하지 않는다. 장에 처음 나오는 Android 고유 용어는 사용 전에 한 문장으로 뜻을 설명한다.

이 장에서 다룬다.

- Android 생태계를 구성하는 주체와 각자의 소유 범위
- Android-compatible device 가 만들어지는 큰 흐름
- 앱 개발자가 만나는 주요 API 와 라이브러리 접점
- 시스템 이미지, Mainline, Google 실행 환경, 라이브러리와 앱의 업데이트 주체
- 호환성과 사용 가능성을 판단하는 기본 축
- 같은 기능이 Android platform, Google, OEM 접점에서 다르게 제공되는 이유

이 장에서 미룬다.

- Android Studio 설치와 프로젝트 생성 절차
- Kotlin/Java 문법과 API 호출 예제
- Gradle task, DEX, signing 과 PackageManager 의 상세 메커니즘
- Binder 호출, HAL, kernel driver 의 내부 구현
- 권한, AppOps, SELinux 의 구체적인 판정 방식
- 특정 OEM 이나 제품의 시장 점유율과 일시적인 정책

### 장을 읽은 뒤 답해야 하는 핵심 질문

>Android 앱이 의존하는 기능을 보았을 때, 누가 사양을 정하고 누가 구현·배포·업데이트하며 어떤 대체 경로 책임이 앱에 남는지 설명할 수 있는가?

여기서 **계약**은 한 주체가 다른 주체에게 무엇을 제공하고 보장하며, 어떤 조건과 실패 처리는 상대에게 남기는지를 뜻한다. **계약 접점(contract surface)**은 그 약속이 API, 라이브러리, 패키지, 호환성 규칙 또는 배포 경계로 드러나는 지점이다.

### 도입 사례: 같은 위치 기능에 여러 Android 가 겹친다

하나의 위치 기능을 장 전체의 대표 사례로 사용한다. 코드를 따라 작성하지 않고 책임 경계를 추적한다.

사례를 읽기 위한 용어 방향표는 다음과 같다.

- **AOSP**: Android platform 의 공개 source 기반이다.
- **Android-compatible device**: AOSP 사용 여부만이 아니라 Android 호환성 요구사항을 만족한 기기다.
- **Google Play services**: 모든 호환 기기에 항상 포함되는 platform 구성 요소가 아니라, 지원 기기에 별도로 존재하고 업데이트되는 Google 실행 환경과 client library 의 결합이다.

1. 앱은 운영체제가 제공하는 위치 API 또는 Google Play services 가 제공하는 위치 API 중 하나를 선택할 수 있다.
2. 운영체제 API 의 실제 구현은 기기의 Android 시스템에 있고, Google API 는 앱에 포함된 client library(클라이언트 라이브러리)와 기기의 별도 Google 실행 환경이 협력한다.
3. Google 실행 환경이 없는 Android-compatible device 에서 Google 위치 접점만 전제하면 기능을 시작할 수 없다.
4. 이때 앱은 실행 환경의 존재를 확인한다. 요구 기능을 운영체제 위치 접점으로도 충족할 수 있을 때만 대체하고, 정확도·전력·기능 조건이 맞지 않으면 기능을 제한하거나 사용할 수 없음을 명확히 처리해야 한다.
5. 두 경로 모두 실제 기기의 위치 capability 와 사용자 허용 상태에 의존하지만 구현·업데이트 주체와 대체 경로 책임은 다르다.

이 사례는 `Android 기능` 이라는 한 표현 안에 사양, client API, 기기 내 구현, 하드웨어 통합, 배포와 업데이트 주체가 겹쳐 있음을 보여준다.

### 절별 상세 구성

| 절 | 독자가 답할 질문 | 핵심 논지 | 필수 도표·사례 |
| --- | --- | --- | --- |
| 1. Android 라는 이름 | AOSP, Android-compatible device 와 Google 제품은 같은가? | 공개 source, 호환성 계약, 실제 기기와 선택적 Google 접점을 구분한다. | `이름 → 실제 대상 → 보장 범위` 구분표 |
| 2. 누가 무엇을 제공하는가 | platform, OEM, Google, 앱·라이브러리 개발자, 배포자와 기기 installer 는 무엇을 맡는가? | 한 주체가 전체 Android 를 만들지 않는다. 배포자는 앱 산출물을 전달하고 기기 installer 와 package 관리 service 는 이를 검증·등록하며, 각 주체의 업데이트 책임도 다르다. | 주체 - 산출물 - 업데이트 책임표 |
| 3. 앱이 만나는 세 접점 | 운영체제 API, Jetpack 과 Google Play services 는 어디에 존재하는가? | 앱 안의 라이브러리, 기기 OS, 별도 Google 실행 환경을 물리적으로 구분한다. | 세 접점의 위치·배포·업데이트 비교 |
| 4. 위치 기능이 실패하는 사례 | Google 실행 환경이 없는 기기에서는 어떤 전제가 깨지는가? | 호환 기기라는 사실만으로 선택적 Google 접점의 존재가 보장되지는 않으며 앱에 확인과 대체 경로 책임이 남는다. | 시작 상태→실패 결과→판단→대체 경로 |
| 5. 새 기능을 분류하는 방법 | 기능이 다르게 동작할 때 어느 업데이트와 구현을 조사해야 하는가? | 소유자, 구현 위치, 배포 단위, 업데이트 주체, 존재 조건과 대체 경로를 묻는다. | 6 개 분류 질문과 2 장 연결 |

위 다섯 절만 실제 1 장 본문 구조로 사용한다. 아래의 세부 표와 기술 용어는 저자가 사실관계와 후속 장 경계를 확인하기 위한 연구 메모이며, 정의 없이 1 장 본문에 그대로 옮기지 않는다.

### 저자용 상세 연구 메모

#### 연구 메모 1. Android 라는 이름을 다섯 대상으로 분리한다

첫 절에서는 Android 를 다음 대상으로 나눈다.

| 대상 | 설명 | 혼동하면 생기는 오류 |
| --- | --- | --- |
| AOSP source | 공개된 platform source 와 reference implementation 의 기반 | AOSP 에 없으면 Android 에서 불가능하다고 단정한다. |
| 호환성 계약 | Android-compatible device 가 지켜야 할 CDD 와 CTS 중심 계약 | 모든 기기의 하드웨어와 사용자 경험이 같다고 기대한다. |
| 기기 구현 | OEM/ODM 이 SoC, board, vendor software 와 제품 구성을 통합한 실제 기기 | platform 계약과 제조사 구현 차이를 구분하지 못한다. |
| 앱 개발 생태계 | SDK/NDK, Jetpack, 도구, 라이브러리, 앱과 배포 생태계 | OS API 와 앱 dependency 를 같은 업데이트 단위로 본다. |
| Google 제품 접점 | GMS, Google Play services, Play Store 와 Google 배포·서비스 | Google 기능을 모든 AOSP 기반 기기의 기본 기능으로 본다. |

핵심 문장은 다음과 같다.

>AOSP 는 Android 생태계의 기반이지만, AOSP source, Android 호환성, Google service 와 특정 OEM 제품은 같은 집합이 아니다.

#### 연구 메모 2. 주체와 책임을 연결한다

| 주체 | 주로 소유하는 것 | 다른 주체와 만나는 계약 |
| --- | --- | --- |
| Google platform·compatibility team | platform 방향, public API, release 별 CDD 와 compatibility program | 기기 구현자와 앱 개발자가 의존하는 호환성 계약 |
| AOSP contributor | 공개 source 에 code 와 문서를 기여 | Google 이 관리하는 platform 방향과 review/release 경계 안에서 기여 |
| SoC vendor | chipset, firmware, board support, kernel/vendor 구현의 일부 | platform 과 OEM 이 정의한 hardware integration 경계 |
| OEM/ODM | 제품 구성, 시스템 이미지, system app, overlay, 기기 업데이트 | Android 호환성, vendor interface 와 app-visible behavior |
| Jetpack/AndroidX 제작자 | 앱과 함께 배포되는 라이브러리 산출물 | Android platform API 와 library version/minSdk 계약 |
| Google Play services 제작자 | client SDK 와 Google-certified device 의 shared runtime/service | client-runtime version 과 사용 가능성 계약 |
| 앱·library 개발자 | APK/AAB/AAR, 앱 데이터와 backend 계약 | platform/library API, signing, store 와 실행 환경 호환성 |
| Store/distributor | app 게시, filtering, 산출물 전달과 rollout | 개발자의 publishing artifact 와 기기의 installer 경계 |
| 기기의 PackageInstaller | 설치 session, APK set 준비·제출과 필요한 사용자 승인 | 전달받은 APK 또는 APK set 과 package 관리 service 의 검증 경계 |
| PackageManager service | package/signature/version/manifest consistency 검증과 설치 상태·identity 관리 | 사용자별 설치 상태, component registry 와 앱 실행 경계 |
| 사용자·관리자 | permission, role, special access, profile 와 device policy 의 일부 결정 | 앱 요청, system policy 와 조직 관리 경계 |

이 표는 조직도를 외우게 하기 위한 것이 아니다. 문제가 발생했을 때 어느 주체의 업데이트나 정책을 확인해야 하는지 판단하게 하는 기준이다.

#### 연구 메모 3. AOSP, 호환성과 GMS 를 분리한다

설명 순서는 다음과 같다.

1. AOSP source 로 device implementation 을 만들 수 있다.
2. Android-compatible device 가 되려면 해당 release 의 Compatibility Definition Document(CDD)를 만족하고 Compatibility Test Suite(CTS)를 통과해야 한다.
3. compatibility 는 third-party Android app 이 기대할 공통 API 와 behavior 기반을 보호한다.
4. compatible device 는 GMS 와 Google Play Store licensing 을 검토할 수 있지만 compatibility 통과와 GMS 포함은 같은 사건이 아니다.
5. OEM 은 compatibility 범위 안에서 hardware, system app, UI 와 product capability 를 차별화할 수 있다.

이 절에서는 `AOSP 기반`, `Android-compatible`, `Google-certified/GMS 포함` 을 서로 바꿔 쓰지 않는다.

#### 연구 메모 4. 앱 개발자가 만나는 접점을 분류한다

| 접점 | 구현이 주로 존재하는 곳 | 앱과 함께 배포되는 부분 | 업데이트 주체 | 실행 환경 확인 |
| --- | --- | --- | --- | --- |
| Android platform API | framework/system image 와 system service | 앱의 호출 코드 | device OS, 일부 Mainline | device API, extension, feature 와 state |
| Android NDK native API | 앱 native library 가 링크하는 stable native platform API/ABI | 앱의 `.so` | 앱과 device OS | ABI, API level 과 symbol availability |
| Jetpack/AndroidX | 대부분 앱 process 의 library code, 일부 platform service 위임 | 선택한 Maven artifact | 앱 release | library version, minSdk 와 platform 대체 경로 |
| Google Play services | 앱 client library 와 기기의 shared Google runtime/service | 경량 client dependency | 앱 dependency 와 Google 실행 환경이 각각 업데이트 | 설치·활성·version 과 device support |
| OEM/device API | vendor framework, system app 또는 device service | vendor SDK 가 있을 수 있음 | OEM/device 업데이트 | model/feature 와 실행 capability, 대체 경로 |

분류 질문은 다음 순서를 따른다.

1. 이 API 는 어느 package 와 artifact 에서 compile 되는가?
2. 실제 구현은 app process, system image, shared runtime, backend 중 어디에 있는가?
3. 앱과 구현 사이에 다른 process 또는 network 경계가 있는가? Managed code 와 native code 를 연결하는 JNI 는 2 장에서 별도로 설명한다.
4. 새 기능과 bug fix 는 앱, 라이브러리, Google 실행 환경, Mainline 또는 system OTA 중 무엇의 업데이트로 전달되는가?
5. 요구 실행 환경이 없거나 오래됐을 때 앱이 제공할 대체 경로는 무엇인가?

#### 연구 메모 5. 산출물과 업데이트 권한을 분리한다

| 산출물·구성 요소 | 대표 소유자 | 대표 전달 경로 | 앱이 관찰할 변화 |
| --- | --- | --- | --- |
| System image 와 framework | OEM/platform integrator | system OTA | platform behavior, framework API 와 device policy |
| Vendor firmware/HAL/kernel module | SoC vendor 와 OEM | firmware/system OTA | hardware behavior, driver 와 capability 차이 |
| Mainline module | platform module owner 와 OEM delivery integration | module 에 따라 APK 또는 APEX 형식과 지원되는 업데이트 경로 | 일부 system component 가 전체 OS release 와 다른 주기로 변경 |
| Google Play services 실행 환경 | Google | Google-certified device 의 별도 업데이트 | Google API 구현과 shared service behavior |
| Jetpack/AndroidX 와 일반 library | library publisher 와 app team | Maven dependency 를 포함한 app release | 앱에 포함된 library code 와 behavior |
| App APK 또는 APK set | app publisher | Play, 다른 store, enterprise 또는 sideload | 설치된 app code/resource 와 version |
| Backend contract | app/service operator | server deployment | 같은 app binary 에서도 remote behavior 변화 |

`최신 Android` 라는 표현은 어느 구성 요소가 최신인지 밝히지 않으면 의미가 없다. OS release, security patch, Mainline module, Google 실행 환경, 라이브러리와 앱 version 을 구분한다.

#### 연구 메모 6. 호환성과 사용 가능성을 한 축으로 뭉치지 않는다

기능 사용 가능성은 다음 질문의 교집합이다.

- build 시점에 필요한 API 와 library 를 참조할 수 있는가?
- 기기 실행 환경에 필요한 OS 기능과 선택적 service 가 존재하는가?
- 사용자·system policy 가 기능 사용을 허용하는가?
- 배포자가 required feature 와 store policy 에 따라 해당 기기에 앱을 전달하는가?

이 장에서는 조건의 존재만 소개한다. 각 gate 의 세부 판정은 9 장과 12 장에서 설명한다.

#### 연구 메모 7. 위치 기능 사례를 생태계 질문으로 다시 읽는다

| 질문 | Platform 위치 접점 | Google Play services 위치 접점 |
| --- | --- | --- |
| 빌드 접점 | Android SDK 의 platform API | Google Maven 의 client library |
| 주된 실행 환경 구현 | framework/system service 와 device provider | client library 와 Google Play services 실행 환경 |
| device dependency | platform location feature, provider 와 OEM hardware integration | Google Play services 존재·상태와 device location capability |
| 업데이트 경로 | device system image 와 OEM 의 실제 배포 경로 | client dependency 와 Google 실행 환경이 별도로 업데이트 |
| 공통으로 남는 앱 책임 | permission/state 확인, failure 처리, 데이터 최소화, capability 와 대체 경로, device test | permission/state 확인, failure 처리, 데이터 최소화, capability 와 대체 경로, device test |

이 비교의 목적은 어느 API 가 더 좋다고 결론 내리는 것이 아니다. 같은 사용자 기능도 선택한 계약 접점에 따라 dependency, 사용 가능성, 업데이트와 대체 경로 책임이 달라진다는 사실을 보여주는 것이다.

실제 실패 분기는 다음과 같이 끝까지 적는다.

`Google 위치 접점만 선택한 앱 → Google 실행 환경이 없는 Android-compatible device에서 연결 불가 → 앱이 실행 환경 부재를 식별 → 요구 기능을 충족하는 운영체제 접점이 있으면 대체하고, 없으면 해당 기능을 명시적으로 제한 또는 비활성화`

#### 연구 메모 8. 2 장으로 넘길 질문

1 장은 누가 무엇을 제공하는지 설명한다. 2 장은 제공된 접점을 호출했을 때 코드가 실제로 어디에서 실행되는지 설명한다.

- Jetpack 호출은 언제 app process 안에서 끝나는가?
- platform manager 는 언제 Binder proxy 가 되는가?
- system_server 와 native service 는 어떤 책임을 나누는가?
- hardware 요청은 언제 HAL, driver 와 kernel 까지 내려가는가?
- callback 과 error 는 어느 thread 와 process 경계를 거쳐 돌아오는가?

### 필수 도표

1. **Android 이름 구분표**: AOSP, 호환 기기와 선택적 Google 제품을 보장 범위로 나눈다.
2. **주체와 업데이트 지도**: platform, OEM, Google, 앱·라이브러리 개발자와 배포자를 각 산출물에 연결한다.
3. **세 계약 접점 비교**: 운영체제 API, Jetpack 과 Google Play services 가 앱 안과 기기 안의 어디에 존재하는지 보여준다.
4. **위치 기능 실패 흐름**: Google 실행 환경 부재에서 실패 결과와 대체 경로까지 보여준다.

### 반드시 교정할 오해

| 오해 | 교정 문장 |
| --- | --- |
| Android 는 Google 이 전부 만드는 하나의 제품이다. | Android 생태계는 AOSP/platform, vendor/OEM device, 선택적 Google surface 와 app ecosystem 의 계약으로 구성된다. |
| AOSP 를 사용한 모든 기기는 Android app 과 완전히 호환된다. | Android compatibility 는 CDD 준수와 CTS 통과라는 별도 계약이다. |
| Android-compatible device 에는 항상 Google Play services 와 Play Store 가 있다. | compatibility 와 GMS licensing·포함 여부는 분리된 조건이다. |
| Jetpack API 는 OS 에 내장되어 있다. | Jetpack 은 대체로 앱 dependency 로 배포되며 필요할 때 platform API 에 위임한다. |
| Google Play services 는 Play Store 의 다른 이름이다. | Play services 는 app-facing shared runtime/SDK 이고 Play Store 는 app distribution 과 update 를 담당하는 제품이다. |
| compile 에 성공하면 지원 기기에서 기능이 항상 동작한다. | compile availability 와 runtime capability, policy, product implementation 은 서로 다른 조건이다. |
| OEM 차이는 모두 Android compatibility 위반이다. | compatibility contract 가 허용하는 product differentiation 과 실제 contract 위반을 구분해야 한다. |
| 최신 OS 면 모든 system component 와 library 도 최신이다. | OS, Mainline, Google 실행 환경, library 와 app 은 서로 다른 업데이트 축을 가진다. |

### 장에서 도입할 용어와 뒤로 미룰 용어

이 장에서 정의한다.

- AOSP
- Android-compatible device
- CDD 와 CTS
- GMS
- Android platform API
- Jetpack/AndroidX
- Google Play services 와 Google Play Store
- OEM/ODM 과 SoC vendor
- system image, Mainline module, app/library artifact
- 계약 접점, 구현, 호환성, capability 와 업데이트 주체

뒤 장으로 미룬다.

- Zygote, ART, ActivityThread, [AMS](../04_system_services/activity-manager-service.md)/ATMS
- Binder driver 와 thread pool
- NDK/JNI, HAL, VINTF 와 GKI 세부 계약
- PackageManager 설치 transaction 과 UID 계산
- Looper, Window, SurfaceFlinger 와 rendering pipeline
- permission protection level, AppOps mode 와 SELinux rule

### 독자 확인 질문

1. AOSP source 를 사용한 기기, Android-compatible device 와 GMS 를 포함한 기기는 어떤 관계인가?
2. SoC vendor 와 OEM 은 Android device 구현에서 서로 무엇을 주로 소유하는가?
3. Android platform API 와 Jetpack library 는 구현 위치와 update 방식이 어떻게 다른가?
4. Google Play services 와 Google Play Store 는 각각 어떤 역할을 맡는가?
5. 앱 코드, 앱에 포함된 Jetpack library, 기기에 설치된 OS 와 Google 실행 환경은 물리적으로 어디에 존재하는가?
6. 같은 위치 기능이 platform API 와 Google API 로 제공될 때 앱의 실행 환경 의존성과 대체 경로 책임은 어떻게 달라지는가?
7. system OTA, Mainline 업데이트, Google 실행 환경 업데이트와 app 업데이트가 서로 독립적이라는 것은 무엇을 의미하는가?
8. build 에 성공한 기능이 실제 기기에서 사용할 수 없을 수 있는 이유는 무엇인가?
9. Android 호환성 계약이 보장하는 것과 OEM 마다 달라질 수 있는 것은 무엇인가?
10. 기능이 다르게 동작할 때 app, library, Google 실행 환경, OS/OEM 중 어느 업데이트를 확인할지 어떻게 판단하는가?

### 독립 검수 기준

- reviewer 가 AOSP, compatibility 와 GMS 를 동의어로 사용하지 않는다.
- reviewer 가 platform API, Jetpack, Play services 와 OEM API 를 구현 위치와 update 주체로 분류한다.
- reviewer 가 distributor 와 기기 installer 의 책임을 구분한다.
- reviewer 가 위치 기능 사례에서 platform 과 Google service 경로의 공통점과 차이를 설명한다.
- reviewer 가 build 성공만으로 실제 기기의 기능 존재와 정책 허용을 판단하지 않는다.
- reviewer 가 2 장을 읽기 전에 app process 안의 library 호출과 system boundary 를 넘는 호출이 존재한다는 점을 설명한다.
- 문서가 특정 API 의 설정·클릭·코드 작성 절차로 흐르지 않는다.

### 공식 출처와 검증 범위

- [Platform architecture](https://developer.android.com/guide/platform): Android software stack 의 공식 개요
- [Android Compatibility program overview](https://source.android.com/docs/compatibility/overview): AOSP, CDD, CTS, Android-compatible device 와 GMS licensing 의 관계
- [AndroidX releases](https://developer.android.com/jetpack/androidx/versions): Jetpack/AndroidX 의 OS 와 분리된 release 특성
- [Google Play services overview](https://developers.google.com/android/guides/overview): client library 와 shared Google runtime 의 관계
- [AOSP architecture overview](https://source.android.com/docs/core/architecture): platform 구성과 system architecture

실제 1 장 본문은 시점에 따라 바뀌는 지원 API 수준이나 업데이트 조건보다 역할과 경계를 우선 설명한다. 숫자와 정책을 사용할 경우 검증일을 남기고 독립 검토자가 다시 확인한다.

## 2 장 상세 개요: Android 플랫폼 실행 계층과 호출 경로

실제 본문: [Android 플랫폼 실행 계층과 호출 경로](../00_foundations/learning-spine/02-android-platform-execution-layers-and-call-paths.md)

### 장의 역할

1 장이 기능의 소유자, 구현 위치와 업데이트 주체를 구분했다면 2 장은 API 를 호출한 뒤 코드가 실제로 어디에서 실행되고 어떤 경계를 넘는지 설명한다.

핵심 질문은 다음과 같다.

>이 호출은 현재 어느 프로세스에서 실행되며, 실제 기능 소유자에게 도달하기 위해 어떤 프로세스·플랫폼·기기 구현·커널 경계를 넘는가?

Android 플랫폼 계층을 모든 요청이 끝까지 통과하는 고정 파이프라인으로 설명하지 않는다. 로컬 호출, 시스템 서비스 호출과 하드웨어 기능 호출을 구분하고, 요청이 정책 판정이나 캐시된 상태에서 끝날 수 있음을 먼저 밝힌다.

### 선행 지식과 장 경계

독자는 1 장을 통해 Android 플랫폼 API, Jetpack 과 Google Play services 의 구현 위치와 배포 경로가 다르다는 사실을 알고 있다고 가정한다. 프로세스와 IPC 는 이 장에서 처음 정의한다.

이 장에서는 다음 내용을 다루지 않는다.

- Binder 드라이버 자료구조, 스레드 풀, `oneway`, 교착 상태와 취소
- 권한, AppOps, SELinux 의 세부 판정 순서
- AIDL·HIDL·VINTF 와 HAL 버전 체계
- Zygote, 앱 프로세스 생성과 컴포넌트 수명주기
- Window, Surface, BufferQueue 와 화면 합성 자료 경로

이 내용은 각각 5~7 장, 9 장과 기존 시스템 내부 정본에서 다룬다.

### 실제 독자 구조

| 절 | 독자가 답할 질문 | 핵심 내용 |
| --- | --- | --- |
| 1. API 와 실행 위치 | SDK 에서 API 가 보이는 것과 구현이 실행되는 것은 왜 다른가? | 프로세스, 앱 프로세스와 기기 시스템 구현 |
| 2. 호출 경로의 세 유형 | 어떤 호출이 앱 안에서 끝나고 어떤 호출이 시스템 경계를 넘는가? | 로컬, 시스템 서비스, 하드웨어 기능 호출 비교 |
| 3. Manager 와 Binder | 앱 쪽 객체와 실제 서비스는 어떻게 연결되는가? | manager, proxy, Binder, stub, service 책임 |
| 4. 서비스 아래의 계층 | `system_server`, 네이티브 서비스, JNI, HAL 과 커널은 어떻게 다른가? | 구현 언어와 프로세스 경계 분리, 플랫폼·기기 구현 경계 |
| 5. 센서 요청 왕복 | 요청과 센서 데이터는 어떤 경로로 오가는가? | 제어 요청 하향, 센서 이벤트 상향, 중간 조율과 실패 지점 |
| 6. 새 호출을 추적하는 방법 | 낯선 API 의 마지막 실행 계층을 어떻게 찾는가? | 실행 위치·경계·상태 소유자·반환 경로 분류 질문 |

### 1. API 와 실행 위치는 다르다

- SDK 의 공개 API 는 호출 형식과 계약을 제공하지만 구현이 앱 APK 에 포함됐다는 뜻은 아니다.
- 프로세스는 독립된 메모리와 실행 경계를 가진 프로그램 단위로 소개한다.
- 앱 코드, 앱에 포함된 라이브러리와 프레임워크 클라이언트 코드는 앱 프로세스에서 실행될 수 있다.
- 기기 전체 상태와 여러 앱의 요청을 조율하는 구현은 다른 시스템 프로세스에 있을 수 있다.
- `android.*` 라고 모두 원격 호출이 아니고 Jetpack 이라고 모두 앱 안에서 끝나는 것도 아니다.

### 2. 호출 경로의 세 유형

| 유형 | 대표 흐름 | 마지막 책임 계층 |
| --- | --- | --- |
| 로컬 호출 | 앱 코드 → 앱 프로세스의 라이브러리·객체 | 앱 프로세스 |
| 시스템 서비스 호출 | 앱 → 관리 객체 → Binder → 시스템 서비스 | `system_server` 또는 별도 서비스 프로세스 |
| 하드웨어 기능 호출 | 앱 → 시스템·네이티브 서비스 → 필요 시 HAL → 커널 드라이버·하드웨어 | 요청에 필요한 가장 아래 계층 |

같은 API 도 캐시된 결과, 입력 오류나 정책 거절로 더 아래 계층에 도달하지 않을 수 있다. 시스템 서비스 호출이라고 모두 HAL 을 사용하지 않으며, 하드웨어 기능 API 라고 매 호출마다 실제 장치를 활성화하는 것도 아니다.

### 3. 관리 객체와 Binder

기본 흐름은 다음과 같다.

`앱 메서드 호출`

```plaintext
→ 앱 프로세스의 관리 객체
→ binder ipc 경계
→ 서비스 구현
→ 즉시 응답 또는 나중의 콜백
```

- 관리 객체는 앱이 사용하는 진입 객체이며 인수 검사, 요청 구성이나 캐시 조회 일부를 수행할 수 있다.
- Binder 는 프로세스 사이의 요청과 호출자 식별 정보 전달을 중재한다.
- 서비스는 공유 상태, 여러 호출자의 조율과 기능별 플랫폼 정책을 소유한다.
- Binder 는 요청을 전달하지만 기능 정책 자체를 결정하지 않는다.
- `ServiceManager` 는 이름으로 Binder 서비스 접점을 등록·조회하며 앱의 관리 객체나 앱 `Service` 와 다르다.

### 4. 서비스 아래의 계층

| 실행 위치 또는 경계 | 주된 책임 |
| --- | --- |
| 앱 프로세스 | 앱 상태, 요청 구성, 앱 라이브러리와 프레임워크 클라이언트 코드 |
| `system_server` | 여러 관리형 프레임워크 시스템 서비스와 기기 전체 정책·상태 조율 |
| 별도 네이티브 서비스·데몬 | 카메라, 그래픽, 네트워크처럼 독립 프로세스에서 동작하는 저수준 하위 시스템 |
| JNI | 같은 프로세스 안에서 Kotlin/Java 관리 코드와 C/C++ 네이티브 코드를 연결하는 호출 경계 |
| HAL | Android 프레임워크·시스템 구성 요소와 기기별 공급자 구현 사이의 사용자 공간 계약 |
| 커널·드라이버 | 프로세스 격리, IPC, 메모리·장치 접근을 중재하고 실제 장치를 제어하는 계층 |

`system_server` 도 ART 에서 실행되는 하나의 Linux 프로세스이며 모든 시스템 서비스가 그 안에 있는 것은 아니다. 네이티브 코드는 구현 언어·실행 환경을 뜻할 뿐 별도 프로세스나 높은 권한을 자동으로 뜻하지 않는다. JNI, Binder, HAL 과 커널 드라이버는 서로 다른 경계다.

### 5. 센서 요청 왕복

가속도계 이벤트 등록을 대표 사례로 사용한다.

`앱의 SensorManager 등록 요청`

```plaintext
→ 앱 프로세스의 프레임워크와 센서 서비스 접근
→ 센서 프레임워크가 여러 앱의 샘플링·지연 요구를 조율
→ 필요하면 Sensors HAL이 센서를 활성화하고 커널 드라이버·센서 장치와 상호작용
→ 센서 데이터가 HAL·센서 서비스의 별도 이벤트 경로를 거쳐 앱 리스너로 돌아옴
```

이 사례에서 아래로 내려가는 것은 등록·활성화 같은 제어 요청이고 위로 올라오는 것은 센서 데이터다. 구체적인 전송 구조는 버전과 기기 구현에 따라 달라질 수 있으므로 모든 데이터가 단순한 동기 Binder 응답으로 돌아온다고 설명하지 않는다.

대조 사례를 함께 둔다.

- 앱 객체의 값 변경은 앱 프로세스 안에서 끝날 수 있다.
- 설치 패키지 상태 조회는 시스템 서비스까지 가지만 HAL 이나 하드웨어가 필요하지 않다.
- 센서 등록은 실제 활성화가 필요할 때 HAL·드라이버·하드웨어까지 이어질 수 있다.

### 6. 새 호출을 추적하는 질문

1. 지금 실행하는 코드는 앱 APK 와 앱 프로세스 안에 있는가?
2. 관리 객체 뒤에 다른 프로세스의 상태 소유자가 있는가?
3. 프로세스 경계를 넘는다면 Binder, 소켓, 공유 메모리 중 어떤 경계를 사용하는가?
4. 실제 서비스는 `system_server` 와 별도 네이티브 프로세스 중 어디에 있는가?
5. 요청이 기기별 구현을 필요로 하며 HAL 경계를 넘는가?
6. 커널은 단순히 IPC 를 중재하는가, 장치 드라이버를 통해 하드웨어도 제어하는가?
7. 결과는 즉시 응답, 콜백 또는 별도 데이터 통로 중 무엇으로 돌아오며 앱 안에서 어떤 실행 문맥으로 전달되는가?
8. 실패가 발생했다면 마지막으로 성공한 경계와 최초로 실패한 경계는 어디인가?

### 반드시 교정할 오해

| 오해 | 교정 |
| --- | --- |
| 공개 API 구현은 모두 앱 프로세스 안에 있다. | 공개 API 는 진입 계약이며 실제 구현은 앱, 시스템 서비스 또는 다른 실행 계층에 있을 수 있다. |
| 모든 `android.*` 호출은 Binder 를 넘는다. | 같은 프로세스에서 끝나는 프레임워크 객체와 메서드도 있다. |
| 모든 시스템 서비스는 `system_server` 에 있다. | 관리형 프레임워크 서비스 다수가 그 안에 있지만 별도 네이티브 서비스·데몬도 존재한다. |
| Binder 가 권한과 기능 정책을 결정한다. | Binder 는 전달과 호출자 식별을 중재하고 기능별 정책은 서비스가 판정한다. |
| JNI 는 IPC 다. | JNI 는 기본적으로 같은 프로세스 안의 관리 코드·네이티브 코드 호출 경계다. |
| 네이티브 코드는 커널 코드이며 권한이 더 높다. | 네이티브는 구현 방식이고 프로세스 권한과 커널 실행 여부는 별도 문제다. |
| HAL 은 커널 드라이버의 다른 이름이다. | HAL 은 사용자 공간의 플랫폼·공급자 계약이고 드라이버는 커널에서 장치를 중재한다. |
| 하드웨어 API 는 매번 실제 장치까지 내려간다. | 캐시, 정책, 요청 통합과 현재 활성 상태에 따라 더 위에서 끝날 수 있다. |
| 콜백은 항상 메인 스레드로 돌아온다. | 반환 경계와 앱 내부 실행 문맥은 별도이며 상세 실행 모델은 6 장에서 다룬다. |

### 독자 확인 질문

1. SDK 의 API 선언과 기기에 있는 실제 구현은 어떻게 다른가?
2. 앱 프로세스 안의 호출과 Binder 를 넘는 호출은 무엇이 다른가?
3. 관리 객체, Binder 와 원격 서비스는 각각 무엇을 맡는가?
4. Binder 와 시스템 서비스는 각각 무엇을 전달하고 결정하는가?
5. `system_server`, 별도 네이티브 서비스와 앱 `Service` 는 왜 같은 개념이 아닌가?
6. 프로세스 경계, 사용자 공간의 기기 구현 경계와 커널 장치 경계는 어떻게 다른가?
7. 센서 등록 요청과 센서 데이터는 어떤 방향과 경로로 이동하는가?
8. 모든 플랫폼 API 가 HAL 과 하드웨어까지 내려가지 않는 이유는 무엇인가?
9. 낯선 호출의 실행 위치를 조사할 때 어떤 순서로 경계를 확인해야 하는가?

### 독립 검수 기준

- 검토자가 Android 플랫폼 계층을 모든 호출이 통과하는 하나의 고정 파이프라인으로 설명하지 않는다.
- 검토자가 로컬 호출, 시스템 서비스 호출과 하드웨어 기능 호출을 구분한다.
- 검토자가 Binder 의 전달 책임과 서비스의 정책·상태 책임을 구분한다.
- 검토자가 `system_server`, 별도 네이티브 서비스, JNI, HAL 과 커널을 서로 바꾸어 쓰지 않는다.
- 검토자가 센서 제어 요청의 하향 경로와 데이터의 상향 경로를 설명한다.
- 문서가 Binder 구현 강의나 특정 API 설정·코드 작성 절차로 흐르지 않는다.

### 공식 출처와 검증 범위

- [Platform architecture](https://developer.android.com/guide/platform): 앱, 프레임워크 API, 시스템 서비스, ART, 네이티브 계층, HAL 과 커널의 공식 개요
- [AOSP architecture overview](https://source.android.com/docs/core/architecture): Android 플랫폼 내부 구조
- [Binder overview](https://source.android.com/docs/core/architecture/ipc/binder-overview): proxy, 커널 드라이버, 대상 프로세스와 응답 흐름
- [AIDL overview](https://source.android.com/docs/core/architecture/aidl): proxy·stub 과 같은 프로세스 최적화의 경계
- [Sensor stack](https://source.android.com/docs/core/interaction/sensors/sensor-stack): 앱 제어 요청과 센서 데이터, 프레임워크·HAL·드라이버의 책임
- [HAL overview](https://source.android.com/docs/core/architecture/hal): 프레임워크와 기기별 구현 사이의 사용자 공간 계약

## 장 사이의 선행 관계

- 1 장은 누가 어떤 contract 를 소유하는지 정하고 나머지 장의 용어를 제한한다.
- 2 장은 runtime 계층을 제공하고 4, 6, 7, 9, 10 장의 호출 경로 기반이 된다.
- 3 장은 설치 identity 를 만든 뒤 4 장의 component 등록과 9 장의 UID/security 로 이어진다.
- 4 와 5 장은 component 실행과 state survival 을 분리한다.
- 6 장은 coroutine, service/FGS 와 scheduler 를 직선 실행 단계가 아니라 execution, visibility 와 durability 의 병렬 계약으로 배치한다.
- 7 은 input dispatch 와 resource selection 을 app UI abstraction, Window 와 system compositor 에 연결한다.
- 8 과 10 은 process 보다 오래 살아야 하는 state 와 work 를 서로 연결한다.
- 9 는 API 호출 실패를 app code, framework policy, kernel/platform policy 로 분류하게 한다.
- 11 은 앞 장의 주장을 실제 log, state 와 trace 로 검증하는 공통 방법을 제공한다.
- 12 는 모든 앞 장의 계약이 version, device 와 distribution 에 따라 달라지는 조건을 정리한다.

## 독자 확인 질문 초안

1. AOSP, Android platform API, Jetpack, Google Play services 와 OEM API 는 업데이트와 배포 주체가 어떻게 다른가?
2. framework API 호출이 단순한 in-process library 호출로 끝나는 경우와 system service 로 넘어가는 경우는 어떻게 다른가?
3. AAB 가 기기에 직접 설치되지 않는 이유와 APK, signing key, package identity 의 관계는 무엇인가?
4. Manifest 의 선언이 install 이후 Intent resolution 과 component 시작에 어떻게 사용되는가?
5. task 제거, Activity 재생성, process death, force-stop 과 uninstall 은 어떤 state 를 각각 남기는가?
6. main Looper, Binder thread, coroutine, foreground service 와 WorkManager 는 각각 실행 순서, component visibility 와 durability 중 무엇을 결정하는가?
7. 사용자 입력과 configuration/resource 선택은 UI state 를 어떻게 바꾸며, 그 결과는 Window 와 Surface 를 거쳐 어떻게 display frame 이 되는가?
8. 연결된 network 가 있어도 요청이 실패할 수 있는 이유와 offline recovery 에 durable local state 가 필요한 이유는 무엇인가?
9. permission, AppOps, foreground state, SELinux 와 server authorization 은 왜 단일 순차 pipeline 이 아니며 API 별로 어떤 gate 가 적용되는가?
10. device capability 가 없거나 OEM 구현이 다를 때 앱은 어느 단계에서 이를 발견하고 fallback 해야 하는가?
11. logcat, dumpsys, trace, profiler, test 와 benchmark 는 서로 어떤 종류의 증거를 제공하는가?
12. `compileSdk`, `minSdk`, `targetSdk`, device API, SDK extension, library version 과 Play policy 는 서로 어떤 결정을 제한하는가?

## 저작 원칙

- API 목록보다 하나의 요청, identity, state 또는 artifact 가 이동하는 순서를 먼저 설명한다.
- 각 장은 위와 아래 계층의 소유권을 밝히고 local object 와 remote/system boundary 를 구분한다.
- `Android`, `AOSP`, `Jetpack`, `Google Play services`, `Google Play`, `OEM 구현` 을 동의어처럼 쓰지 않는다.
- 최소 하나의 end-to-end flow 와 반례를 포함하지만 설치·클릭 순서 중심의 tutorial 로 만들지 않는다.
- 원자 노트는 근거와 상세 판단에 재사용하고, 연결 서사가 링크 목록으로 붕괴하지 않게 핵심 인과관계를 본문에 반복한다.
- 버전과 정책 수치는 stable mechanism 과 분리하고 공식 1 차 출처와 검증일을 남긴다.
- 장을 읽지 않은 독립 reviewer 가 확인 질문에 자신의 말로 답할 수 있어야 완료로 판정한다.

## Phase 1 종료 전 준비 작업

1. 1 장 `Android 생태계와 계약 surface` 의 상세 outline 과 actor/artifact 관계표 작성 완료.
2. 3 장의 source-to-installed-package 흐름에서 PackageInstaller/PackageManager, AAPT2/D8/R8/signing 의 설명 깊이를 결정한다.
3. 5 장의 독립 lifetime 표와 configuration change/process death/task removal/force-stop/uninstall 비교 사례를 설계한다.
4. 7 장의 Window, ViewRootImpl, WindowManagerService 와 SurfaceControl 공백을 공식 문서/AOSP 근거로 조사한다.
5. 8~10 장의 offline outbox, security denial, system capability 호출을 하나씩 대표 흐름으로 설계한다.
6. 12 장의 호환성 축 표와 AOSP/Google/OEM/form-factor 변형 모델을 설계한다.
7. Phase 1 결과가 확정된 뒤 최종 장 이름, 배치 경로와 기존 map 연결만 결정한다.

## 1 차 공식 근거

- [Platform architecture](https://developer.android.com/guide/platform)
- [Application fundamentals](https://developer.android.com/guide/components/fundamentals)
- [AOSP architecture overview](https://source.android.com/docs/core/architecture)
- [Configure your build](https://developer.android.com/build)

검증일: 2026-08-03. 이 문서는 curriculum 준비 자료다. API 와 정책의 최종 fact-check 는 각 장 저작 시 Author 와 분리된 Researcher/Reviewer 가 수행한다.
