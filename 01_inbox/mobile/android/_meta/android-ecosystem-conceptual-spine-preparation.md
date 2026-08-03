---
title: "Android 생태계 개념 Learning Spine 준비"
tags: ["android", "knowledge-base", "learning-spine", "coverage-audit"]
aliases: []
date modified: 2026-08-03 17:22:12 +09:00
date created: 2026-08-03 17:22:12 +09:00
---

# Android 생태계 개념 Learning Spine 준비

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
- Native app 경로: `app Kotlin/Java ↔ JNI → NDK stable API/ABI 또는 앱 native library → 허용된 platform/native surface`
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
| Android NDK/JNI surface | 앱 native code가 사용하는 stable native API/ABI와 managed/native 연결 계약 | NDK API, native library와 JNI boundary |
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

1. 1장 `Android 생태계와 계약 surface`의 상세 outline과 actor/artifact 관계표를 설계한다.
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
