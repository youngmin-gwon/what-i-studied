---
title: "Android 생태계 개념 Learning Spine 준비"
tags: ["android", "knowledge-base", "learning-spine", "coverage-audit"]
aliases: []
date modified: 2026-08-03 17:30:35 +09:00
date created: 2026-08-03 17:22:12 +09:00
---

## Android 생태계 개념 Learning Spine 준비

## 목적

이 문서는 Android Studio 설치나 첫 앱 제작 절차를 설명하는 follow-along 계획이 아니다. Android 생태계를 처음 조망하는 개발자가 다음을 하나의 모델로 연결하도록 만드는 Learning Spine의 준비 자료다.

- Android라는 제품과 플랫폼을 누가 만들고 배포하는가?
- 앱 소스는 어떤 산출물로 변환되어 기기에 설치되는가?
- 설치된 패키지는 어떻게 시스템에 등록되고 프로세스와 component로 실행되는가?
- framework API 호출은 언제 Binder, system service, HAL과 kernel을 통과하는가?
- UI state는 어떻게 window, Surface와 display의 실제 frame으로 이어지는가?
- 앱의 identity, lifetime, permission, background execution과 데이터 복구는 어떻게 연결되는가?
- 같은 앱이 OS 버전, OEM, Google service surface와 form factor에 따라 왜 다르게 동작하는가?

대상 독자는 일반적인 프로그래밍 개념과 앱 코드 읽기에 익숙하지만 Android 생태계의 구성과 내부 인과관계는 모르는 사람이다. Kotlin 문법, IDE 설치, 버튼 위치, 예제 앱 따라 만들기는 범위에 포함하지 않는다.

## 동시 작업 경계

- [Android Knowledge Base Quality Plan](./android-knowledge-base-quality-plan.md)의 Phase 1 taxonomy 작업과 병렬로 수행한다.
- Phase 1이 수정 중인 top-level map, 폴더 이름과 신규 cluster에는 손대지 않는다.
- 계획 기준선은 `_meta` 제외 585개 노트지만, Phase 1에서 신규 노트가 생기고 있으므로 이 문서는 실시간 파일 수를 완료 기준으로 고정하지 않는다.
- 여기서 제안하는 장 구조는 taxonomy 결정 이후 조정할 수 있는 curriculum 입력이지 최종 폴더 구조가 아니다.

## 중심 모델

Android는 하나의 SDK나 하나의 운영체제 이미지로 이해하면 안 된다. 다음 다섯 관점을 겹쳐 봐야 한다.

### 주체

- AOSP는 공개 플랫폼 소스와 호환 계약의 기반을 제공한다.
- Google은 Android API 문서와 도구, Jetpack/AndroidX, Google Play services, Google Play 배포 인프라 등 서로 다른 surface를 제공한다.
- SoC vendor는 chipset, firmware, kernel과 vendor 구현의 일부를 공급한다.
- OEM/ODM은 board와 product 구성, system image, system app, 정책, 업데이트를 기기 제품으로 통합한다.
- 앱 개발자와 library 제작자는 public API 및 배포 계약 위에 APK/AAB와 dependency를 만든다.
- store/distributor는 AAB에서 기기별 APK 집합을 생성하거나 이미 만들어진 APK를 전달한다.
- 기기의 PackageInstaller/PackageManager 경계는 전달받은 APK 집합을 검증하고 설치된 package 상태로 만든다.

### 산출물

앱과 library의 산출물 흐름은 분리한다.

- 앱: `source/resource/manifest/dependency → compile/resource processing/DEX/package → APK 또는 AAB → 서명·배포 → device용 APK → 설치된 package`
- library: `source/resource/manifest/public API → AAR → 소비하는 앱의 build dependency`

AAR은 보통 앱 build의 입력이지 설치 산출물이 아니다. AAB는 게시 형식이고 APK는 기기 설치 형식이다. 플랫폼 image, APEX/Mainline module, app APK도 모두 Android에 존재하지만 소유자, 업데이트 경계와 실행 권한이 다르다.

### 실행 계층

- In-process library 경로: `app code → Jetpack/AndroidX 또는 다른 library → app process 안의 결과`
- Platform service 경로: `app code → android.* manager/proxy → Binder → system_server/native service → 필요하면 HAL/kernel/hardware`
- Native app 경로: `app Kotlin/Java ↔ JNI bridge → 앱 native library → NDK stable API/ABI 등 허용된 native platform surface`
- Google service 경로: `app code → Google client library → 기기의 Google runtime/service 또는 backend`

모든 호출이 Binder나 hardware까지 내려가지 않는다. 각 장은 실제 요청이 어느 경로를 택하고 어느 계층이 identity, policy, state와 hardware access를 소유하는지 구분해야 한다.

### 독립적인 lifetime

- 설치된 package identity와 사용자·profile별 app data
- Linux process와 ART instance
- task와 back stack
- Activity, Service, Receiver, Provider instance
- ViewModel, saved state와 persistent state
- Compose composition, View tree, Window와 Surface
- coroutine의 취소 가능한 작업 lifetime
- Service/foreground service의 component와 사용자 가시성 계약
- WorkManager/JobScheduler의 durable scheduling 계약

이 lifetime들은 함께 시작하거나 끝난다고 가정할 수 없다. configuration change, task removal, component destroy, process death, force-stop과 uninstall의 차이는 이 모델로 설명한다.

### 호환성 축

- `compileSdk`: 빌드 시 참조할 수 있는 API surface
- `minSdk`: 지원 가능한 runtime 하한과 fallback 책임
- `targetSdk`: 앱이 선언한 동작 계약과 compatibility behavior 기준
- device API/SDK extension: 실행 중 실제 API availability
- Jetpack/library version: 앱에 포함되는 library 계약과 자체 최소 요구사항
- Play policy: 플랫폼 runtime과 별개인 제출·배포 조건
- Mainline, OEM 구현과 device feature: API level 하나로 환원되지 않는 실행 환경

## 생태계 개념 Coverage Matrix

| 개념 축 | 현재 판정 | 재사용할 주요 정본 | Learning Spine에서 새로 연결할 내용 |
| --- | --- | --- | --- |
| AOSP, Google, OEM, SoC vendor | 원자 자료 있음, 산업 생태계 서사 없음 | [Platform customization contracts](../01_system_internals/platform-customization/platform-customization-contracts/platform-customization-contracts.md), [HAL/native boundary](../01_system_internals/kernel-and-hal/hal-native-boundary.md) | AOSP release에서 vendor/OEM 제품, compatibility test, GMS와 사용자 기기까지의 책임 흐름 |
| Platform SDK, Jetpack, Play services | 큰 공백 | [Jetpack architecture map](../02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture-map.md)과 개별 library 노트 | OS 내장 API, 앱에 포함되는 AndroidX, Google 서비스 client/runtime surface의 차이 |
| Gradle/AGP와 build artifact | 개별 계약 강함, 변환 파이프라인 약함 | [Packaging and deployment](../03_packaging_deployment/android-packaging-deployment.md), [Gradle contracts](../03_packaging_deployment/build/gradle/gradle-build-contracts/gradle-build-contracts.md) | manifest/resource/dependency merge, compile, DEX, package, shrink, sign의 인과 흐름과 실패 경계 |
| Resource와 runtime configuration | 큰 공백 | [Configuration change](../02_app_framework/architecture/app-components/app-component-contracts/configuration-change-recreates-activity-but-not-all-screen-state.md), [RRO](../01_system_internals/platform-customization/platform-customization-contracts/rro-changes-resources-without-rebuilding-target-apk.md) | resource merge/AAPT2/ID와 table, locale·density·night mode·window별 선택, configuration change, OEM overlay의 관계 |
| APK/AAB, signing, Play, install/update | 게시·서명 강함, device install 공백 | [Release distribution contracts](../03_packaging_deployment/distribution/release-distribution-contracts/release-distribution-contracts.md), [Play Delivery contracts](../03_packaging_deployment/distribution/play-delivery-contracts/play-delivery-contracts.md) | distributor와 installer 분리, PackageInstaller/PackageManager 검증, numeric appId·사용자별 UID/data/component 등록, sideload/store의 공통 설치 경계 |
| API level과 호환성 | 원자 자료 강함, 통합 계산 모델 부족 | [Android release history](../00_foundations/history/android-release-history.md), [Platform modularity](../01_system_internals/platform-modularity/android-platform-modularity.md) | compile/min/target/device/extension/library/Play policy/OEM feature를 한 판단 모델로 결합 |
| Platform runtime stack | 계층별 정본 강함, 요청 왕복 서사 부족 | [Android System Map](../00_foundations/overview/android-system-map.md), [Boot and runtime](../01_system_internals/boot-and-runtime/android-boot-and-runtime.md), [IPC/process contracts](../01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md) | app 요청이 framework, Binder, system service, native/HAL/kernel을 통과하고 결과를 받는 흐름 |
| Package, Manifest와 component | 개별 개념 강함, 설치 등록과 실행 연결 부족 | [Android app components](../02_app_framework/architecture/app-components/android-app-components.md), [Intent/Manifest contracts](../02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-manifest-contracts.md) | 설치 시 선언 등록, intent resolution, policy 판정, component entry와 process start의 관계 |
| Task, process, lifecycle와 state | 개별 개념 강함, lifetime 통합 모델 없음 | [App component contracts](../02_app_framework/architecture/app-components/app-component-contracts/app-component-contracts.md), [Android state management](../02_app_framework/architecture/state-management/android-state-management.md) | task/process/component/ViewModel/composition/saved/persistent state가 서로 독립인 이유 |
| Main thread, Binder와 coroutine | Binder/coroutine 정본 강함, 공통 실행 모델 약함 | [IPC/process contracts](../01_system_internals/ipc-and-process/ipc-process-contracts/ipc-process-contracts.md), [Coroutine contracts](../02_app_framework/data/async-flow/coroutines/coroutine-contracts.md) | main Looper와 callback 직렬화, Binder thread pool, coroutine context/lifetime, OS scheduler의 차이 |
| Input에서 UI state, display까지 | 출력 양 끝은 강함, 입력과 Window 중간 계층 공백 | [Android UI system](../02_app_framework/ui/system/android-ui-system.md), [Compose runtime](../02_app_framework/jetpack-compose/runtime/compose-runtime-and-state-model.md), [Graphics/media runtime](../01_system_internals/graphics-and-media/android-graphics-media-runtime.md) | input→dispatcher→Window→main queue→View·Compose event/state와 state→render→Surface→SurfaceFlinger→display의 상호작용 loop |
| Data, network와 offline recovery | storage/connectivity 강함, 앱 데이터 순환 서사 부족 | [Android data layer map](../02_app_framework/data/android-data-layer-map.md), [Android connectivity](../01_system_internals/connectivity/android-connectivity.md) | remote protocol, repository, local source of truth, outbox, retry/idempotency, conflict/freshness와 UI 관찰 |
| Background work와 notification | 선택 모델 강함, end-to-end 기능 서사 부족 | [Background work contracts](../04_system_services/background-and-notifications/background-work-contracts/background-work-contracts.md), [Notification/messaging contracts](../04_system_services/background-and-notifications/notification-messaging-contracts/notification-messaging-contracts.md) | durable state→schedule→constraint/quota→중단/재시도→서버 동기화→notification→UI 복구 |
| Identity와 security policy | 계층별 정본 강함, identity와 독립 gate의 통합 모델 부족 | [Security and privacy](../05_security_privacy/android-security-and-privacy.md), [Permission contracts](../05_security_privacy/permissions-and-sandbox/permission-contracts/permission-contracts.md) | package name/applicationId, signing identity, numeric appId, 사용자별 UID·data·grant와 Binder caller, permission, AppOps, SELinux, server authorization의 적용 경계 |
| System service와 device capability | 공통 모델 작성 중, capability 폭 부족 | [System services and device capabilities](../04_system_services/android-system-services-and-device-capabilities.md) | feature discovery→manager/proxy→policy/service→HAL/hardware→callback/fallback과 Google/OEM surface 구분 |
| Form factor 생태계 | large screen/XR 강함, 전체 coverage 부족 | [Platforms and form factors](../07_platforms/android-platforms-and-form-factors.md) | phone baseline과 TV/Wear/Auto/Automotive/ChromeOS/XR의 input, window, lifecycle, distribution 차이 |
| Testing, diagnostics와 release feedback | 개별 도구와 원칙 강함, 운영 loop 부족 | [Performance and quality map](../06_testing_performance/performance/android-performance-quality-and-build-optimization.md) | 계약→재현 환경→log/state/trace→benchmark→regression test→device matrix→staged release/field signal |

## 가장 중요한 연결 공백

### 생태계 주체와 API surface

현재 문서는 AOSP, GMS, HAL, OEM customization을 각각 설명하지만 다음 구분을 한 자리에서 제공하지 않는다.

| Surface | 주된 소유·배포 방식 | 앱에서 보이는 형태 |
| --- | --- | --- |
| Android platform API | OS/framework에 포함, 기기 OS와 함께 제공 | `android.*` API와 system service |
| Android NDK native surface | 앱 native code가 사용하는 stable native API/ABI | NDK API와 native library. JNI는 managed/native code 사이의 연결 방식이다. |
| Jetpack/AndroidX | 앱 dependency로 선택하고 앱과 함께 배포 | lifecycle, Room, WorkManager, Compose 등 |
| Google Play services | Google 서비스가 있는 기기의 runtime과 client library가 협력 | location, identity 등 Google 제공 surface |
| OEM API/behavior | 특정 제조사 제품과 system image에 종속 | vendor SDK, feature, 설정과 구현 차이 |

이 구분이 없으면 독자는 library update와 OS update, public platform contract와 Google/OEM capability를 같은 것으로 오해한다.

### Source에서 설치된 app identity까지

필요한 개념 흐름은 다음과 같다.

`source + manifest + resource + dependency`
→ Gradle/AGP build와 variant 결정
→ compile/resource processing/DEX/package
→ APK 또는 AAB
→ signing과 distribution
→ device용 APK 전달
→ installer와 PackageManager의 version/signature/manifest 검증
→ 문자열 package name/applicationId와 signing lineage 관리
→ PackageManager가 숫자 appId 할당
→ 사용자·profile별 UID, 설치 상태, data directory와 permission state
→ component registry
→ 이후 launch와 update의 identity 기준

현재 배포 노트는 Play와 signing에 강하지만 PackageManager가 설치된 앱을 OS-visible entity로 만드는 중간 연결이 약하다.

### 설치된 package에서 첫 frame까지

`launcher 또는 외부 요청`
→ Intent resolution과 policy 판정
→ ATMS/AMS가 task, component와 process 상태 확인
→ 필요하면 Zygote가 app process fork
→ ActivityThread가 framework에 attach
→ component instance와 lifecycle callback
→ Window/ViewRoot와 View 또는 Compose tree
→ measure/layout/draw와 RenderThread
→ Surface/BufferQueue
→ SurfaceFlinger/HWC/display

이 흐름은 기존 원자 노트를 연결하는 대표 인과 서사이며 build, install, runtime, lifecycle과 rendering을 동시에 묶는다.

사용자 입력은 반대 방향에서 앱 상태로 들어온다.

`input device → kernel → InputReader/InputDispatcher → 대상 Window → app main queue → View/Compose event dispatch → state change`

따라서 UI 장은 입력과 출력의 두 직선을 별개로 끝내지 않고 `input → state transition → frame` 상호작용 loop로 설명해야 한다.

### Framework API에서 hardware capability까지

`capability/feature 확인`
→ app의 manager 또는 Google client API
→ local proxy와 Binder/별도 runtime boundary
→ 해당 API가 요구하는 caller UID, permission, AppOps, foreground/global state 판정
→ system/native service
→ HAL/driver/hardware
→ callback, error 또는 fallback

모든 device capability가 같은 경로나 gate를 사용하지 않는다는 점과 AOSP platform surface, Google service surface, OEM 구현을 구분해야 한다. Permission, AppOps, SELinux와 server authorization도 모든 호출이 정해진 순서로 통과하는 하나의 pipeline이 아니라 API와 resource별로 서로 다르게 조합되는 독립 gate다.

### 사용자 상태에서 durable recovery까지

`UI event와 in-memory state`
→ repository와 local transaction
→ durable source of truth/outbox
→ scheduler constraint와 quota
→ network/server reconciliation
→ local state 갱신
→ UI observation와 notification

process death, callback 누락과 중복 실행을 정상 조건으로 두고 idempotency와 checkpoint가 어디에 필요한지 설명한다.

## Learning Spine 12장 후보

이 순서는 기존 계획의 12개 주제를 생태계 개념 흐름에 맞게 구체화한 후보안이다.

| 장 | 핵심 질문 | 장을 관통할 흐름 |
| --- | --- | --- |
| 1. Android 생태계와 계약 surface | AOSP, Google, OEM, vendor, Jetpack, Play는 각각 무엇을 소유하는가? | AOSP release→vendor/OEM device→Google surface→app/runtime/distribution |
| 2. Android platform stack | 앱 요청은 어느 실행 계층을 통과하는가? | app→framework→Binder/service→native/HAL→kernel/hardware |
| 3. Source에서 설치된 package까지 | 소스, resource와 dependency는 어떻게 OS가 신뢰하는 package identity가 되는가? | build/resource table→artifact→sign→distribute→install→package name·numeric appId·사용자별 UID 등록 |
| 4. Manifest와 app component | OS는 앱의 진입점과 capability를 어떻게 발견하는가? | manifest 등록→intent resolution→component activation |
| 5. Task, process, lifecycle와 state | 화면, component, process와 사용자 상태는 왜 함께 죽지 않는가? | request→task/component→process→callback→destroy/recreate/recover |
| 6. Main thread, Binder, coroutine과 작업 lifetime | 코드는 어느 thread/process와 lifetime에서 실행되는가? | Looper, Binder, coroutine, FGS와 durable scheduler의 병렬 책임 비교 |
| 7. Input, resource와 display frame | 입력과 configuration은 어떻게 UI state와 실제 픽셀로 이어지는가? | input→Window/main queue→state→resource 선택/View·Compose→SurfaceFlinger→display |
| 8. Data, storage, network와 offline recovery | 데이터는 어느 owner가 보존하고 실패 뒤 어떻게 복구하는가? | remote/local source→outbox/sync→UI observation |
| 9. Identity, permission과 security boundary | 권한이 있는데도 호출이 실패하는 이유는 무엇인가? | package/signing/app ID와 사용자별 UID→API·resource별 독립 policy gate |
| 10. System capability와 background execution | 앱은 device 기능과 지속 작업을 어떤 시스템 계약으로 사용하는가? | discovery→service/hardware, durable state→scheduler→notification |
| 11. 관찰, 테스트와 품질 feedback | 보이지 않는 Android 상태를 어떤 증거로 확인하는가? | reproduce→log/state/trace→test/benchmark→release/field feedback |
| 12. 호환성, update와 form factor | 같은 앱이 기기와 버전에 따라 달라지는 축은 무엇인가? | SDK axes→Mainline/OEM feature→form factor→distribution/testing matrix |

## 1장 상세 목차: Android 생태계와 계약 접점(contract surface)

### 장의 역할

1장은 Android를 API 모음이나 단일 운영체제 이미지로 소개하지 않는다. Android라는 이름 아래 여러 주체, 산출물, 실행 환경과 배포 경로가 서로 다른 계약으로 연결된다는 전체 모델을 제공한다.

이 장을 먼저 읽어야 뒤 장에서 다음 혼동을 피할 수 있다.

- AOSP와 Google Mobile Services(GMS)를 같은 제품으로 보는 혼동
- Android platform API와 Jetpack/AndroidX를 같은 업데이트 단위로 보는 혼동
- Google Play services와 Google Play Store를 같은 역할로 보는 혼동
- SDK에서 보이는 API와 실제 기기에서 사용할 수 있는 기능을 같은 것으로 보는 혼동
- OEM 차이를 모두 Android 파편화 또는 API 위반으로 보는 혼동
- 앱, 라이브러리, 시스템 이미지, Mainline 모듈과 Google 실행 환경의 배포 주체를 구분하지 않는 혼동

### 독자 전제와 범위

독자는 운영체제, 라이브러리, 프로세스, API, 패키지 같은 일반 소프트웨어 용어만 알고 있다고 가정한다. Android 앱을 빌드해 본 경험이나 AOSP 내부 지식은 요구하지 않는다. 장에 처음 나오는 Android 고유 용어는 사용 전에 한 문장으로 뜻을 설명한다.

이 장에서 다룬다.

- Android 생태계를 구성하는 주체와 각자의 소유 범위
- Android-compatible device가 만들어지는 큰 흐름
- 앱 개발자가 만나는 주요 API와 라이브러리 접점
- 시스템 이미지, Mainline, Google 실행 환경, 라이브러리와 앱의 업데이트 주체
- 호환성과 사용 가능성을 판단하는 기본 축
- 같은 기능이 Android platform, Google, OEM 접점에서 다르게 제공되는 이유

이 장에서 미룬다.

- Android Studio 설치와 프로젝트 생성 절차
- Kotlin/Java 문법과 API 호출 예제
- Gradle task, DEX, signing과 PackageManager의 상세 메커니즘
- Binder 호출, HAL, kernel driver의 내부 구현
- 권한, AppOps, SELinux의 구체적인 판정 방식
- 특정 OEM이나 제품의 시장 점유율과 일시적인 정책

### 장을 읽은 뒤 답해야 하는 핵심 질문

> Android 앱이 의존하는 기능을 보았을 때, 누가 사양을 정하고 누가 구현·배포·업데이트하며 어떤 대체 경로 책임이 앱에 남는지 설명할 수 있는가?

여기서 **계약**은 한 주체가 다른 주체에게 무엇을 제공하고 보장하며, 어떤 조건과 실패 처리는 상대에게 남기는지를 뜻한다. **계약 접점(contract surface)**은 그 약속이 API, 라이브러리, 패키지, 호환성 규칙 또는 배포 경계로 드러나는 지점이다.

### 도입 사례: 같은 위치 기능에 여러 Android가 겹친다

하나의 위치 기능을 장 전체의 대표 사례로 사용한다. 코드를 따라 작성하지 않고 책임 경계를 추적한다.

사례를 읽기 위한 용어 방향표는 다음과 같다.

- **AOSP**: Android platform의 공개 source 기반이다.
- **Android-compatible device**: AOSP 사용 여부만이 아니라 Android 호환성 요구사항을 만족한 기기다.
- **Google Play services**: 모든 호환 기기에 항상 포함되는 platform 구성 요소가 아니라, 지원 기기에 별도로 존재하고 업데이트되는 Google 실행 환경과 client library의 결합이다.

1. 앱은 운영체제가 제공하는 위치 API 또는 Google Play services가 제공하는 위치 API 중 하나를 선택할 수 있다.
2. 운영체제 API의 실제 구현은 기기의 Android 시스템에 있고, Google API는 앱에 포함된 client library(클라이언트 라이브러리)와 기기의 별도 Google 실행 환경이 협력한다.
3. Google 실행 환경이 없는 Android-compatible device에서 Google 위치 접점만 전제하면 기능을 시작할 수 없다.
4. 이때 앱은 실행 환경의 존재를 확인한다. 요구 기능을 운영체제 위치 접점으로도 충족할 수 있을 때만 대체하고, 정확도·전력·기능 조건이 맞지 않으면 기능을 제한하거나 사용할 수 없음을 명확히 처리해야 한다.
5. 두 경로 모두 실제 기기의 위치 capability와 사용자 허용 상태에 의존하지만 구현·업데이트 주체와 대체 경로 책임은 다르다.

이 사례는 `Android 기능`이라는 한 표현 안에 사양, client API, 기기 내 구현, 하드웨어 통합, 배포와 업데이트 주체가 겹쳐 있음을 보여준다.

### 절별 상세 구성

| 절 | 독자가 답할 질문 | 핵심 논지 | 필수 도표·사례 |
| --- | --- | --- | --- |
| 1. Android라는 이름 | AOSP, Android-compatible device와 Google 제품은 같은가? | 공개 source, 호환성 계약, 실제 기기와 선택적 Google 접점을 구분한다. | `이름 → 실제 대상 → 보장 범위` 구분표 |
| 2. 누가 무엇을 제공하는가 | platform, OEM, Google, 앱·라이브러리 개발자, 배포자와 기기 installer는 무엇을 맡는가? | 한 주체가 전체 Android를 만들지 않는다. 배포자는 앱 산출물을 전달하고 기기 installer와 package 관리 service는 이를 검증·등록하며, 각 주체의 업데이트 책임도 다르다. | 주체-산출물-업데이트 책임표 |
| 3. 앱이 만나는 세 접점 | 운영체제 API, Jetpack과 Google Play services는 어디에 존재하는가? | 앱 안의 라이브러리, 기기 OS, 별도 Google 실행 환경을 물리적으로 구분한다. | 세 접점의 위치·배포·업데이트 비교 |
| 4. 위치 기능이 실패하는 사례 | Google 실행 환경이 없는 기기에서는 어떤 전제가 깨지는가? | 호환 기기라는 사실만으로 선택적 Google 접점의 존재가 보장되지는 않으며 앱에 확인과 대체 경로 책임이 남는다. | 시작 상태→실패 결과→판단→대체 경로 |
| 5. 새 기능을 분류하는 방법 | 기능이 다르게 동작할 때 어느 업데이트와 구현을 조사해야 하는가? | 소유자, 구현 위치, 배포 단위, 업데이트 주체, 존재 조건과 대체 경로를 묻는다. | 6개 분류 질문과 2장 연결 |

위 다섯 절만 실제 1장 본문 구조로 사용한다. 아래의 세부 표와 기술 용어는 저자가 사실관계와 후속 장 경계를 확인하기 위한 연구 메모이며, 정의 없이 1장 본문에 그대로 옮기지 않는다.

### 저자용 상세 연구 메모

#### 연구 메모 1. Android라는 이름을 다섯 대상으로 분리한다

첫 절에서는 Android를 다음 대상으로 나눈다.

| 대상 | 설명 | 혼동하면 생기는 오류 |
| --- | --- | --- |
| AOSP source | 공개된 platform source와 reference implementation의 기반 | AOSP에 없으면 Android에서 불가능하다고 단정한다. |
| 호환성 계약 | Android-compatible device가 지켜야 할 CDD와 CTS 중심 계약 | 모든 기기의 하드웨어와 사용자 경험이 같다고 기대한다. |
| 기기 구현 | OEM/ODM이 SoC, board, vendor software와 제품 구성을 통합한 실제 기기 | platform 계약과 제조사 구현 차이를 구분하지 못한다. |
| 앱 개발 생태계 | SDK/NDK, Jetpack, 도구, 라이브러리, 앱과 배포 생태계 | OS API와 앱 dependency를 같은 업데이트 단위로 본다. |
| Google 제품 접점 | GMS, Google Play services, Play Store와 Google 배포·서비스 | Google 기능을 모든 AOSP 기반 기기의 기본 기능으로 본다. |

핵심 문장은 다음과 같다.

> AOSP는 Android 생태계의 기반이지만, AOSP source, Android 호환성, Google service와 특정 OEM 제품은 같은 집합이 아니다.

#### 연구 메모 2. 주체와 책임을 연결한다

| 주체 | 주로 소유하는 것 | 다른 주체와 만나는 계약 |
| --- | --- | --- |
| Google platform·compatibility team | platform 방향, public API, release별 CDD와 compatibility program | 기기 구현자와 앱 개발자가 의존하는 호환성 계약 |
| AOSP contributor | 공개 source에 code와 문서를 기여 | Google이 관리하는 platform 방향과 review/release 경계 안에서 기여 |
| SoC vendor | chipset, firmware, board support, kernel/vendor 구현의 일부 | platform과 OEM이 정의한 hardware integration 경계 |
| OEM/ODM | 제품 구성, 시스템 이미지, system app, overlay, 기기 업데이트 | Android 호환성, vendor interface와 app-visible behavior |
| Jetpack/AndroidX 제작자 | 앱과 함께 배포되는 라이브러리 산출물 | Android platform API와 library version/minSdk 계약 |
| Google Play services 제작자 | client SDK와 Google-certified device의 shared runtime/service | client-runtime version과 사용 가능성 계약 |
| 앱·library 개발자 | APK/AAB/AAR, 앱 데이터와 backend 계약 | platform/library API, signing, store와 실행 환경 호환성 |
| Store/distributor | app 게시, filtering, 산출물 전달과 rollout | 개발자의 publishing artifact와 기기의 installer 경계 |
| 기기의 PackageInstaller | 설치 session, APK set 준비·제출과 필요한 사용자 승인 | 전달받은 APK 또는 APK set과 package 관리 service의 검증 경계 |
| PackageManager service | package/signature/version/manifest consistency 검증과 설치 상태·identity 관리 | 사용자별 설치 상태, component registry와 앱 실행 경계 |
| 사용자·관리자 | permission, role, special access, profile와 device policy의 일부 결정 | 앱 요청, system policy와 조직 관리 경계 |

이 표는 조직도를 외우게 하기 위한 것이 아니다. 문제가 발생했을 때 어느 주체의 업데이트나 정책을 확인해야 하는지 판단하게 하는 기준이다.

#### 연구 메모 3. AOSP, 호환성과 GMS를 분리한다

설명 순서는 다음과 같다.

1. AOSP source로 device implementation을 만들 수 있다.
2. Android-compatible device가 되려면 해당 release의 Compatibility Definition Document(CDD)를 만족하고 Compatibility Test Suite(CTS)를 통과해야 한다.
3. compatibility는 third-party Android app이 기대할 공통 API와 behavior 기반을 보호한다.
4. compatible device는 GMS와 Google Play Store licensing을 검토할 수 있지만 compatibility 통과와 GMS 포함은 같은 사건이 아니다.
5. OEM은 compatibility 범위 안에서 hardware, system app, UI와 product capability를 차별화할 수 있다.

이 절에서는 `AOSP 기반`, `Android-compatible`, `Google-certified/GMS 포함`을 서로 바꿔 쓰지 않는다.

#### 연구 메모 4. 앱 개발자가 만나는 접점을 분류한다

| 접점 | 구현이 주로 존재하는 곳 | 앱과 함께 배포되는 부분 | 업데이트 주체 | 실행 환경 확인 |
| --- | --- | --- | --- | --- |
| Android platform API | framework/system image와 system service | 앱의 호출 코드 | device OS, 일부 Mainline | device API, extension, feature와 state |
| Android NDK native API | 앱 native library가 링크하는 stable native platform API/ABI | 앱의 `.so` | 앱과 device OS | ABI, API level과 symbol availability |
| Jetpack/AndroidX | 대부분 앱 process의 library code, 일부 platform service 위임 | 선택한 Maven artifact | 앱 release | library version, minSdk와 platform 대체 경로 |
| Google Play services | 앱 client library와 기기의 shared Google runtime/service | 경량 client dependency | 앱 dependency와 Google 실행 환경이 각각 업데이트 | 설치·활성·version과 device support |
| OEM/device API | vendor framework, system app 또는 device service | vendor SDK가 있을 수 있음 | OEM/device 업데이트 | model/feature와 실행 capability, 대체 경로 |

분류 질문은 다음 순서를 따른다.

1. 이 API는 어느 package와 artifact에서 compile되는가?
2. 실제 구현은 app process, system image, shared runtime, backend 중 어디에 있는가?
3. 앱과 구현 사이에 다른 process 또는 network 경계가 있는가? Managed code와 native code를 연결하는 JNI는 2장에서 별도로 설명한다.
4. 새 기능과 bug fix는 앱, 라이브러리, Google 실행 환경, Mainline 또는 system OTA 중 무엇의 업데이트로 전달되는가?
5. 요구 실행 환경이 없거나 오래됐을 때 앱이 제공할 대체 경로는 무엇인가?

#### 연구 메모 5. 산출물과 업데이트 권한을 분리한다

| 산출물·구성 요소 | 대표 소유자 | 대표 전달 경로 | 앱이 관찰할 변화 |
| --- | --- | --- | --- |
| System image와 framework | OEM/platform integrator | system OTA | platform behavior, framework API와 device policy |
| Vendor firmware/HAL/kernel module | SoC vendor와 OEM | firmware/system OTA | hardware behavior, driver와 capability 차이 |
| Mainline module | platform module owner와 OEM delivery integration | module에 따라 APK 또는 APEX 형식과 지원되는 업데이트 경로 | 일부 system component가 전체 OS release와 다른 주기로 변경 |
| Google Play services 실행 환경 | Google | Google-certified device의 별도 업데이트 | Google API 구현과 shared service behavior |
| Jetpack/AndroidX와 일반 library | library publisher와 app team | Maven dependency를 포함한 app release | 앱에 포함된 library code와 behavior |
| App APK 또는 APK set | app publisher | Play, 다른 store, enterprise 또는 sideload | 설치된 app code/resource와 version |
| Backend contract | app/service operator | server deployment | 같은 app binary에서도 remote behavior 변화 |

`최신 Android`라는 표현은 어느 구성 요소가 최신인지 밝히지 않으면 의미가 없다. OS release, security patch, Mainline module, Google 실행 환경, 라이브러리와 앱 version을 구분한다.

#### 연구 메모 6. 호환성과 사용 가능성을 한 축으로 뭉치지 않는다

기능 사용 가능성은 다음 질문의 교집합이다.

- build 시점에 필요한 API와 library를 참조할 수 있는가?
- 기기 실행 환경에 필요한 OS 기능과 선택적 service가 존재하는가?
- 사용자·system policy가 기능 사용을 허용하는가?
- 배포자가 required feature와 store policy에 따라 해당 기기에 앱을 전달하는가?

이 장에서는 조건의 존재만 소개한다. 각 gate의 세부 판정은 9장과 12장에서 설명한다.

#### 연구 메모 7. 위치 기능 사례를 생태계 질문으로 다시 읽는다

| 질문 | Platform 위치 접점 | Google Play services 위치 접점 |
| --- | --- | --- |
| 빌드 접점 | Android SDK의 platform API | Google Maven의 client library |
| 주된 실행 환경 구현 | framework/system service와 device provider | client library와 Google Play services 실행 환경 |
| device dependency | platform location feature, provider와 OEM hardware integration | Google Play services 존재·상태와 device location capability |
| 업데이트 경로 | device system image와 OEM의 실제 배포 경로 | client dependency와 Google 실행 환경이 별도로 업데이트 |
| 공통으로 남는 앱 책임 | permission/state 확인, failure 처리, 데이터 최소화, capability와 대체 경로, device test | permission/state 확인, failure 처리, 데이터 최소화, capability와 대체 경로, device test |

이 비교의 목적은 어느 API가 더 좋다고 결론 내리는 것이 아니다. 같은 사용자 기능도 선택한 계약 접점에 따라 dependency, 사용 가능성, 업데이트와 대체 경로 책임이 달라진다는 사실을 보여주는 것이다.

실제 실패 분기는 다음과 같이 끝까지 적는다.

`Google 위치 접점만 선택한 앱 → Google 실행 환경이 없는 Android-compatible device에서 연결 불가 → 앱이 실행 환경 부재를 식별 → 요구 기능을 충족하는 운영체제 접점이 있으면 대체하고, 없으면 해당 기능을 명시적으로 제한 또는 비활성화`

#### 연구 메모 8. 2장으로 넘길 질문

1장은 누가 무엇을 제공하는지 설명한다. 2장은 제공된 접점을 호출했을 때 코드가 실제로 어디에서 실행되는지 설명한다.

- Jetpack 호출은 언제 app process 안에서 끝나는가?
- platform manager는 언제 Binder proxy가 되는가?
- system_server와 native service는 어떤 책임을 나누는가?
- hardware 요청은 언제 HAL, driver와 kernel까지 내려가는가?
- callback과 error는 어느 thread와 process 경계를 거쳐 돌아오는가?

### 필수 도표

1. **Android 이름 구분표**: AOSP, 호환 기기와 선택적 Google 제품을 보장 범위로 나눈다.
2. **주체와 업데이트 지도**: platform, OEM, Google, 앱·라이브러리 개발자와 배포자를 각 산출물에 연결한다.
3. **세 계약 접점 비교**: 운영체제 API, Jetpack과 Google Play services가 앱 안과 기기 안의 어디에 존재하는지 보여준다.
4. **위치 기능 실패 흐름**: Google 실행 환경 부재에서 실패 결과와 대체 경로까지 보여준다.

### 반드시 교정할 오해

| 오해 | 교정 문장 |
| --- | --- |
| Android는 Google이 전부 만드는 하나의 제품이다. | Android 생태계는 AOSP/platform, vendor/OEM device, 선택적 Google surface와 app ecosystem의 계약으로 구성된다. |
| AOSP를 사용한 모든 기기는 Android app과 완전히 호환된다. | Android compatibility는 CDD 준수와 CTS 통과라는 별도 계약이다. |
| Android-compatible device에는 항상 Google Play services와 Play Store가 있다. | compatibility와 GMS licensing·포함 여부는 분리된 조건이다. |
| Jetpack API는 OS에 내장되어 있다. | Jetpack은 대체로 앱 dependency로 배포되며 필요할 때 platform API에 위임한다. |
| Google Play services는 Play Store의 다른 이름이다. | Play services는 app-facing shared runtime/SDK이고 Play Store는 app distribution과 update를 담당하는 제품이다. |
| compile에 성공하면 지원 기기에서 기능이 항상 동작한다. | compile availability와 runtime capability, policy, product implementation은 서로 다른 조건이다. |
| OEM 차이는 모두 Android compatibility 위반이다. | compatibility contract가 허용하는 product differentiation과 실제 contract 위반을 구분해야 한다. |
| 최신 OS면 모든 system component와 library도 최신이다. | OS, Mainline, Google 실행 환경, library와 app은 서로 다른 업데이트 축을 가진다. |

### 장에서 도입할 용어와 뒤로 미룰 용어

이 장에서 정의한다.

- AOSP
- Android-compatible device
- CDD와 CTS
- GMS
- Android platform API
- Jetpack/AndroidX
- Google Play services와 Google Play Store
- OEM/ODM과 SoC vendor
- system image, Mainline module, app/library artifact
- 계약 접점, 구현, 호환성, capability와 업데이트 주체

뒤 장으로 미룬다.

- Zygote, ART, ActivityThread, AMS/ATMS
- Binder driver와 thread pool
- NDK/JNI, HAL, VINTF와 GKI 세부 계약
- PackageManager 설치 transaction과 UID 계산
- Looper, Window, SurfaceFlinger와 rendering pipeline
- permission protection level, AppOps mode와 SELinux rule

### 독자 확인 질문

1. AOSP source를 사용한 기기, Android-compatible device와 GMS를 포함한 기기는 어떤 관계인가?
2. SoC vendor와 OEM은 Android device 구현에서 서로 무엇을 주로 소유하는가?
3. Android platform API와 Jetpack library는 구현 위치와 update 방식이 어떻게 다른가?
4. Google Play services와 Google Play Store는 각각 어떤 역할을 맡는가?
5. 앱 코드, 앱에 포함된 Jetpack library, 기기에 설치된 OS와 Google 실행 환경은 물리적으로 어디에 존재하는가?
6. 같은 위치 기능이 platform API와 Google API로 제공될 때 앱의 실행 환경 의존성과 대체 경로 책임은 어떻게 달라지는가?
7. system OTA, Mainline 업데이트, Google 실행 환경 업데이트와 app 업데이트가 서로 독립적이라는 것은 무엇을 의미하는가?
8. build에 성공한 기능이 실제 기기에서 사용할 수 없을 수 있는 이유는 무엇인가?
9. Android 호환성 계약이 보장하는 것과 OEM마다 달라질 수 있는 것은 무엇인가?
10. 기능이 다르게 동작할 때 app, library, Google 실행 환경, OS/OEM 중 어느 업데이트를 확인할지 어떻게 판단하는가?

### 독립 검수 기준

- reviewer가 AOSP, compatibility와 GMS를 동의어로 사용하지 않는다.
- reviewer가 platform API, Jetpack, Play services와 OEM API를 구현 위치와 update 주체로 분류한다.
- reviewer가 distributor와 기기 installer의 책임을 구분한다.
- reviewer가 위치 기능 사례에서 platform과 Google service 경로의 공통점과 차이를 설명한다.
- reviewer가 build 성공만으로 실제 기기의 기능 존재와 정책 허용을 판단하지 않는다.
- reviewer가 2장을 읽기 전에 app process 안의 library 호출과 system boundary를 넘는 호출이 존재한다는 점을 설명한다.
- 문서가 특정 API의 설정·클릭·코드 작성 절차로 흐르지 않는다.

### 공식 출처와 검증 범위

- [Platform architecture](https://developer.android.com/guide/platform): Android software stack의 공식 개요
- [Android Compatibility program overview](https://source.android.com/docs/compatibility/overview): AOSP, CDD, CTS, Android-compatible device와 GMS licensing의 관계
- [AndroidX releases](https://developer.android.com/jetpack/androidx/versions): Jetpack/AndroidX의 OS와 분리된 release 특성
- [Google Play services overview](https://developers.google.com/android/guides/overview): client library와 shared Google runtime의 관계
- [AOSP architecture overview](https://source.android.com/docs/core/architecture): platform 구성과 system architecture

실제 1장 본문을 작성할 때는 시점에 따라 바뀌는 지원 API level이나 update 조건보다 역할과 경계를 우선 설명한다. 숫자와 정책을 사용할 경우 검증일을 남기고 독립 Researcher가 다시 확인한다.

## 장 사이의 선행 관계

- 1장은 누가 어떤 contract를 소유하는지 정하고 나머지 장의 용어를 제한한다.
- 2장은 runtime 계층을 제공하고 4, 6, 7, 9, 10장의 호출 경로 기반이 된다.
- 3장은 설치 identity를 만든 뒤 4장의 component 등록과 9장의 UID/security로 이어진다.
- 4와 5장은 component 실행과 state survival을 분리한다.
- 6장은 coroutine, service/FGS와 scheduler를 직선 실행 단계가 아니라 execution, visibility와 durability의 병렬 계약으로 배치한다.
- 7은 input dispatch와 resource selection을 app UI abstraction, Window와 system compositor에 연결한다.
- 8과 10은 process보다 오래 살아야 하는 state와 work를 서로 연결한다.
- 9는 API 호출 실패를 app code, framework policy, kernel/platform policy로 분류하게 한다.
- 11은 앞 장의 주장을 실제 log, state와 trace로 검증하는 공통 방법을 제공한다.
- 12는 모든 앞 장의 계약이 version, device와 distribution에 따라 달라지는 조건을 정리한다.

## 독자 확인 질문 초안

1. AOSP, Android platform API, Jetpack, Google Play services와 OEM API는 업데이트와 배포 주체가 어떻게 다른가?
2. framework API 호출이 단순한 in-process library 호출로 끝나는 경우와 system service로 넘어가는 경우는 어떻게 다른가?
3. AAB가 기기에 직접 설치되지 않는 이유와 APK, signing key, package identity의 관계는 무엇인가?
4. Manifest의 선언이 install 이후 Intent resolution과 component 시작에 어떻게 사용되는가?
5. task 제거, Activity 재생성, process death, force-stop과 uninstall은 어떤 state를 각각 남기는가?
6. main Looper, Binder thread, coroutine, foreground service와 WorkManager는 각각 실행 순서, component visibility와 durability 중 무엇을 결정하는가?
7. 사용자 입력과 configuration/resource 선택은 UI state를 어떻게 바꾸며, 그 결과는 Window와 Surface를 거쳐 어떻게 display frame이 되는가?
8. 연결된 network가 있어도 요청이 실패할 수 있는 이유와 offline recovery에 durable local state가 필요한 이유는 무엇인가?
9. permission, AppOps, foreground state, SELinux와 server authorization은 왜 단일 순차 pipeline이 아니며 API별로 어떤 gate가 적용되는가?
10. device capability가 없거나 OEM 구현이 다를 때 앱은 어느 단계에서 이를 발견하고 fallback해야 하는가?
11. logcat, dumpsys, trace, profiler, test와 benchmark는 서로 어떤 종류의 증거를 제공하는가?
12. `compileSdk`, `minSdk`, `targetSdk`, device API, SDK extension, library version과 Play policy는 서로 어떤 결정을 제한하는가?

## 저작 원칙

- API 목록보다 하나의 요청, identity, state 또는 artifact가 이동하는 순서를 먼저 설명한다.
- 각 장은 위와 아래 계층의 소유권을 밝히고 local object와 remote/system boundary를 구분한다.
- `Android`, `AOSP`, `Jetpack`, `Google Play services`, `Google Play`, `OEM 구현`을 동의어처럼 쓰지 않는다.
- 최소 하나의 end-to-end flow와 반례를 포함하지만 설치·클릭 순서 중심의 tutorial로 만들지 않는다.
- 원자 노트는 근거와 상세 판단에 재사용하고, 연결 서사가 링크 목록으로 붕괴하지 않게 핵심 인과관계를 본문에 반복한다.
- 버전과 정책 수치는 stable mechanism과 분리하고 공식 1차 출처와 검증일을 남긴다.
- 장을 읽지 않은 독립 reviewer가 확인 질문에 자신의 말로 답할 수 있어야 완료로 판정한다.

## Phase 1 종료 전 준비 작업

1. 1장 `Android 생태계와 계약 surface`의 상세 outline과 actor/artifact 관계표 작성 완료.
2. 3장의 source-to-installed-package 흐름에서 PackageInstaller/PackageManager, AAPT2/D8/R8/signing의 설명 깊이를 결정한다.
3. 5장의 독립 lifetime 표와 configuration change/process death/task removal/force-stop/uninstall 비교 사례를 설계한다.
4. 7장의 Window, ViewRootImpl, WindowManagerService와 SurfaceControl 공백을 공식 문서/AOSP 근거로 조사한다.
5. 8~10장의 offline outbox, security denial, system capability 호출을 하나씩 대표 흐름으로 설계한다.
6. 12장의 호환성 축 표와 AOSP/Google/OEM/form-factor 변형 모델을 설계한다.
7. Phase 1 결과가 확정된 뒤 최종 장 이름, 배치 경로와 기존 map 연결만 결정한다.

## 1차 공식 근거

- [Platform architecture](https://developer.android.com/guide/platform)
- [Application fundamentals](https://developer.android.com/guide/components/fundamentals)
- [AOSP architecture overview](https://source.android.com/docs/core/architecture)
- [Configure your build](https://developer.android.com/build)

검증일: 2026-08-03. 이 문서는 curriculum 준비 자료다. API와 정책의 최종 fact-check는 각 장 저작 시 Author와 분리된 Researcher/Reviewer가 수행한다.
