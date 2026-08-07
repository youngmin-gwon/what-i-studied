---
title: android-knowledge-base-phase12-audit-report
tags: ["android", "knowledge-base", "quality-audit", "phase-12"]
aliases: ["Android 지식 베이스 Phase 12 전수 감사 보고서"]
date modified: 2026-08-06 14:45:00 +09:00
date created: 2026-08-06 14:45:00 +09:00
---

## Android 지식 베이스 Phase 12 전수 감사 보고서

감사 기준: [Android 개인 지식 베이스 고품질화 계획](android-knowledge-base-quality-plan.md)의 Phase 12.

이 보고서는 2026-08-06 시점의 `01_inbox/mobile/android/` 전체를 대상으로 한 감사 결과다. 주관적 판단이 필요한 본문 재작성·문체 통일·문서 병합과 삭제는 수행하지 않았고, 원문 손상임이 기계적으로 확정되는 항목만 복구했다.

### 범위와 검수 배치

| 범위 | 확인 수 | 검수 방식 |
|---|---:|---|
| `00_foundations` | 115/115 | 고 reasoning 의미 감사 |
| `01_system_internals` | 155/155 | 고 reasoning 의미 감사 |
| `02_app_framework` | 261/261 | 고 reasoning 의미 감사 |
| `03_packaging_deployment` | 55/55 | 고 reasoning 의미 감사 |
| `04_system_services` | 88/88 | 고 reasoning 의미 감사 |
| `05_security_privacy` | 28/28 | 고 reasoning 의미 감사 |
| `06_testing_performance` | 33/33 | 고 reasoning 의미 감사 |
| `07_platforms` | 43/43 | 고 reasoning 의미 감사 |
| 지식 문서 합계 | **778/778** | 본문 약 56,206줄 전수 확인 |
| `_meta` | 4/4 | 저비용 형식 감사와 계획 대조 |
| 감사 입력 Markdown | **782/782** | 링크·frontmatter·중복·도달성 기계 검사 |

이 보고서가 새로 추가되어 최종 재검사 시점의 Android Markdown은 783개이며, 지식 문서 수는 778개로 동일하다.

모델 역할은 다음처럼 분리했다.

- 저비용 agent: 782개 파일의 frontmatter, 링크 대상, 제목, 중복 본문, H1, 코드 fence, Mermaid, 제어문자와 그래프 도달성만 검사했다.
- 고 reasoning agent 2개: 서로 겹치지 않는 778개 지식 문서를 나눠 읽고 사실·코드·실무 공백·문체·다이어그램·fundamental 연결을 판정했다.
- 고 reasoning 구조 agent: Git 이력, exact/near duplicate, 고아 문서, 허브 중복과 복구 가능성을 별도로 판정했다.
- 주 검수: agent 보고를 원문·Git 이력·공식 1차 문서와 교차 확인했다.

### 결론

이 vault는 링크 수와 문서 수는 충분하지만, 이전 Phase 5/11의 “전량 A/B” 또는 “완료” 선언을 신뢰할 상태는 아니다. 확인된 핵심 문제는 다음과 같다.

1. 문서 두 개가 다른 내용 또는 절대경로 한 줄로 덮어써진 실제 데이터 손상이 있었다.
2. 최신 Android·Play·AGP·Billing·Wear·ML Kit 계약과 어긋나는 사실 또는 컴파일 불가능한 예제가 여러 핵심 문서에 남아 있다.
3. App Framework의 일부 생성 배치는 원자 노트 수를 늘렸지만 코드·관찰 신호·실패 형태가 없어 실제 구현 판단에 쓰기 어렵다.
4. Phase 11의 자동 인라인 용어 풀이가 API 식별자와 LaTeX escape를 훼손했다.
5. 최상위 map과 Learning Spine의 연결이 약하고, 지식 문서 3개가 Foundation map 기준으로 도달 불가능하다.
6. Obsidian에서는 유효하지만 저장소 설정·GitHub/CommonMark와 맞지 않는 vault-root 링크가 대량으로 섞여 있다.

## P0: 데이터 손상과 실행 불가능한 내용

### 복구 완료

- `02_app_framework/architecture/multiplatform-contracts/multiplatform-contracts.md`
  - commit `1f16a629`에서 정상 28줄 허브가 자신의 절대경로 한 줄로 덮어써졌다.
  - `a56245db`의 정상본을 기준으로 허브 구조와 링크를 복구하고 수정일을 갱신했다.

### 재작성 대기

- `00_foundations/history/history-contracts/android-16-and-17-continue-faster-api-and-form-factor-change.md`
  - commit `d502c890`에서 `history-contracts.md` 본문으로 덮어써졌다.
  - 정상본은 commit `383f9dfb`에 남아 있다.
  - 정상본의 Android 17 상태 문장은 2026-08-06 공식 상태와 다시 맞춰야 하므로 자동 복구하지 않았다. 구조를 복원하면서 API 37, Platform Stability, preview SDK 표기를 각각 분리해 서술해야 한다.

### 사실 또는 코드 오류가 확정된 핵심 문서

#### Foundations와 System Internals

- `00_foundations/diagnostic-runbooks/01-app-launch-slow-or-fails.md`
  - 16KB page size 미대응을 보편적인 `dlopen` 실패로 단정하고, SplashScreen·Android 15/16 조건을 혼합한다.
- `00_foundations/diagnostic-runbooks/02-anr.md`
  - Android Vitals의 전체 0.47%와 기기별 8% 기준을 잘못 적고, foreground service 시작 제한과 승격 시간 초과를 혼동한다.
- `00_foundations/diagnostic-runbooks/06-notification-missing.md`
  - FCM invalid token 응답과 high-priority/data-only 전달을 보장처럼 설명한다.
- `00_foundations/diagnostic-runbooks/08-install-update-failure.md`
  - 16KB ELF 정렬 실패를 `INSTALL_FAILED_NO_MATCHING_ABIS`로 잘못 매핑하고 유효성이 불분명한 manifest 속성을 제시한다.
- `00_foundations/topics/G1-in-app-billing.md`
  - Google Play Billing만 유일하게 허용된다고 단정한다. 현재는 지역·프로그램에 따른 alternative billing, user choice billing, external offers가 있다.
- `00_foundations/topics/F2-form-factor-contracts.md`
  - ChromeOS 실행 환경을 항상 container로 단정한다. ARC++와 ARCVM을 구분해야 한다.
- `01_system_internals/boot-and-runtime/system-server-contracts/process-priority-is-memory-reclaim-policy-input-not-app-state-truth.md`
  - `-1000`을 `SYSTEM_ADJ`로 적었고 “절대 희생되지 않음”이라고 단정한다.
- `01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-preloads-framework-state-before-app-fork.md`
  - fork 시 공통 환경이 100% 준비된다는 표현과 고정 시간·클래스 수를 계약처럼 쓴다.
- `01_system_internals/ipc-and-process/ipc-process-contracts/posix-ipc-vs-android-binder-contracts.md`
  - Android가 POSIX IPC를 배제한다는 전제, peer credential, 자원 수명, Ashmem, Binder thread pool과 관측 경로 설명이 부정확하다.
- `01_system_internals/kernel-and-hal/kernel-contracts/kernel-builds-depend-on-branch-toolchain-and-build-system.md`
  - Android 13부터 Kleaf가 강제라고 적었다. Android 14+ common kernel과 구분해야 한다.
- `01_system_internals/connectivity/connectivity-contracts/cellular-connectivity-is-shaped-by-plan-and-system-policy.md`
  - 제한·deprecated API를 일반 앱 표면처럼 제시하고 데이터 소진 후 전환을 보장처럼 쓴다.
- `01_system_internals/kernel-and-hal/hal-native-contracts/ndk-is-native-library-toolchain-not-app-architecture.md`
  - 공식 NDK `.so` API가 정적으로만 링크된다는 설명은 틀리다.
- `01_system_internals/kernel-and-hal/hal-native-contracts/cmake-gradle-and-abi-define-native-build-and-packaging.md`
  - native `.so` 로딩 주체를 ART로 적고 `pickFirsts`를 보편 해결책으로 제시한다.

#### App Framework, Packaging, Services와 Testing

- `02_app_framework/architecture/multiplatform-contracts/expect-actual-is-compile-time-contract-for-platform-specific-implementation.md`
  - 무인자 `expect` 생성자와 `Context` 인자를 요구하는 `actual` 생성자가 일치하지 않아 예제가 컴파일 계약을 만족하지 못한다.
- `02_app_framework/architecture/multiplatform-contracts/kmp-shares-business-logic-and-data-layer-while-ui-stays-native-by-default.md`
  - native UI를 KMP의 기본·100% 품질 보장으로 단정한다. Compose Multiplatform과 platform UI를 선택지로 분리해야 한다.
- `02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/compose-ui-is-declarative-function-of-state.md`
  - Slot Table, [recomposition](../02_app_framework/jetpack-compose/runtime/recomposition.md), Applier, measure/layout/draw invalidation을 하나의 UI tree diff 단계처럼 설명한다.
- `03_packaging_deployment/distribution/billing-contracts/play-billing-library-is-the-only-approved-in-app-purchase-path.md`
  - 정책 제목이 지역별 예외를 무시한다. Billing 6.2.1과 제거된 무인자 `enablePendingPurchases()` 예제도 갱신해야 한다.
- `03_packaging_deployment/android-packaging-deployment.md`
  - 지원이 끝난 Billing Library v6+ 기준이 남아 있다.
- `03_packaging_deployment/optimization/build-optimization-contracts/r8-full-mode-and-configuration-analyzer-expose-blocked-optimization.md`
  - AGP 8+에서 기본인 R8 full mode를 별도 활성화하는 옛 절차를 제시한다.
- `03_packaging_deployment/build/gradle/gradle-build-contracts/android-gradle-plugin-adds-android-build-rules-to-gradle.md`
  - `apksigner`가 AAB도 서명하는 흐름으로 표현한다.
- `03_packaging_deployment/build/gradle/gradle-build-contracts/convention-plugins-centralize-shared-gradle-configuration-in-build-logic.md`
- `03_packaging_deployment/build/dependency-versioning/dependency-ci-contracts/version-catalog-names-dependency-and-plugin-coordinates.md`
  - AGP 9의 built-in Kotlin 전환을 반영하지 않고 `org.jetbrains.kotlin.android`를 현대 기본으로 고정한다.
- `04_system_services/device-capabilities/on-device-ai-contracts/on-device-ai-feature-availability-must-be-checked-before-use.md`
  - 비동기 callback 완료 전에 local result를 반환한다. 다운로드·close·foreground·busy·quota·기기 지원 조건도 빠졌다.
- `04_system_services/device-capabilities/haptics-vibrator-contracts/haptic-feedback-types-map-ux-interactions-to-platform-patterns.md`
  - 의미 상수와 특정 `VibrationEffect`, 구형 fallback을 1:1 보장처럼 설명한다.
- `04_system_services/device-capabilities/media-audio-camera-contracts/cameramanager-access-starts-with-availability-and-characteristics.md`
  - 카메라를 항상 단일 client 독점으로 단정해 concurrent camera와 priority 경쟁을 누락한다.
- `04_system_services/service-lookup/service-lookup-contracts/getsystemservice-returns-a-cached-manager-backed-by-binder-ipc.md`
  - 모든 manager가 process cache라는 일반화가 부정확하다.
- `04_system_services/service-lookup/service-lookup-contracts/system-server-checks-caller-uid-and-pid-for-every-call.md`
  - 모든 service·call이 직접 UID/PID를 검사한다고 일반화한다.
- `04_system_services/device-capabilities/biometrics-credential-contracts/biometricprompt-couples-authentication-ui-with-key-authorization.md`
  - 모든 민감 기능이 `CryptoObject`를 반드시 써야 한다고 단정한다.
- `06_testing_performance/testing/testing-quality-contracts/compose-ui-tests-should-use-stable-selectors-and-semantics.md`
  - Checkbox 상태에 `assertIsSelected()`를 제시한다. toggle semantics에는 `assertIsOn()`/`assertIsOff()`가 맞다.
- `06_testing_performance/performance/benchmark-baseline-contracts/macrobenchmark-compilation-mode-is-part-of-test-contract.md`
  - `Full()`을 100% native machine code로 확대 해석한다.
- `06_testing_performance/performance/benchmark-baseline-contracts/benchmark-results-require-physical-device-and-ci-controls.md`
  - emulator 사용 시 ATD가 필수라는 규칙은 대표 성능 측정 지침과 맞지 않는다.
- `06_testing_performance/performance/performance-contracts/memory-performance-requires-leak-and-allocation-evidence.md`
  - ART collector와 LeakCanary 동작을 버전 독립 고정 계약처럼 쓴다.
- `06_testing_performance/testing/testing-quality-contracts/unit-integration-ui-e2e-tests-have-different-failure-signals.md`
  - 모든 E2E 결함을 unit test로 먼저 재현하라는 규칙은 계층 고유 결함에 적용할 수 없다.
- `06_testing_performance/testing/coroutine-flow-tests-control-dispatchers-and-virtual-time.md`
  - dispatcher 주입을 반드시 Hilt/Koin으로 해야 한다고 제한한다.

#### Security와 Platforms

- `05_security_privacy/secure-storage/secure-storage-contracts/android-keystore-protects-keys-by-non-exportability.md`
  - 존재하지 않는 `key.isExportable()`을 사용하고 모든 key operation이 TEE/StrongBox에 있다고 단정한다. hardware-backed 여부는 `KeyInfo.getSecurityLevel()`로 확인해야 한다.
- `05_security_privacy/secure-storage/secure-storage-contracts/encrypted-storage-apis-do-not-replace-key-and-data-boundary.md`
  - deprecated `MasterKey`와 `EncryptedSharedPreferences`를 현재 권장 구현으로 제시하고, 모든 예외에서 저장소를 삭제하는 위험한 복구 예제를 둔다.
- `05_security_privacy/secure-storage/secure-storage-contracts/sensitive-data-requires-encryption-and-key-ownership.md`
  - immutable `String` 평문 복사본이 남는데 wipe 가능하다고 설명한다.
- `07_platforms/android-platforms-and-form-factors.md`
  - 존재하지 않는 `PackageManager.HAS_FEATURE_*` 상수와 부적절한 ChromeOS 확인 속성을 사용한다.
- `07_platforms/wear/wear-contracts/ambient-mode-is-a-separate-lifecycle-for-always-on-screens.md`
  - deprecated `AmbientModeSupport`를 현재 구현으로 가르친다.
- `07_platforms/auto/auto-contracts/android-auto-is-projection-android-automotive-os-is-an-embedded-os.md`
  - Android Auto와 AAOS의 manifest·배포 단위를 한 예제로 합친다.

## 축 1: 내용 밀도와 원자 문서 품질

App Framework 기계 휴리스틱은 원자 후보 189개 중 131개가 mechanism/code/diagram/evidence 네 신호 중 세 개 미만이라고 표시했다. 휴리스틱만으로 결함을 확정하지 않고 전부 다시 읽었으며, 아래 묶음은 실제로 보강 또는 병합이 필요하다고 판정했다.

- App Components 10개: 선언과 링크 중심이며 receiver timeout, `goAsync`, exported 실패, foreground service 제한, task/launchMode, process death 재현이 없다.
- DI 19개: 대체로 21~47줄이며 binding code, generated graph error, scope 관찰, assisted injection이 없다.
- Compose design-system 10개: provider/consumer code, recomposition 관찰, test가 없다.
- Compose accessibility 4개: semantics code, merged/unmerged tree 출력, TalkBack 관찰이 없다.
- Compose performance 6개: compiler report나 recomposition 전후 증거가 없다.
- System Services 27개: biometrics, input/accessibility, location, media/audio/camera, sensor, telephony, service lookup, package/user/role, power 묶음이 mechanism 문단과 관찰 한 줄에 머문다.
- Foundations overview atomic 6개: 19~25줄의 routing shim에 가까우며 제목이 약속한 end-to-end mechanism과 evidence가 없다.

“짧다”는 이유만으로 결함 판정하지 않았다. map·glossary·routing 역할을 명시한 문서는 atomic 4요소 예외로 다뤘다.

## 축 2: 실제 앱 개발 관점의 공백

### App Framework

- KMP cluster가 App Framework map에서 빠졌고 이미 존재하는 networking/widget을 “신설 예정”으로 적은 진행 문구가 남았다.
- Networking에는 HTTP cache/ETag, auth refresh single-flight, TLS/Network Security Config, connectivity 변화, WebSocket/SSE 운영 계약이 없다.
- DI에는 실제 `@Binds`·`@Provides`·qualifier·scope code, generated graph failure, assisted injection 판단이 없다.
- Compose accessibility에는 focus, custom action, touch target, merged tree 출력과 테스트가 없다.
- KMP에는 source-set hierarchy, AGP 9 KMP plugin, Android lifecycle/thread interop, interface/factory와 expect/actual의 선택 기준이 없다.

### Packaging와 배포

- PBL 8/9 migration, auto service reconnection, unfetched product 상태와 제거 API가 없다.
- AGP 9 built-in Kotlin/KMP migration이 없다.
- dependency verification·locking, SBOM, software supply chain, reproducible build가 없다.
- 장기 service-account JSON과 OIDC/workload identity 같은 단기 자격증명의 선택 기준이 없다.

### System Services

- ConnectivityManager, NetworkCallback, metered/validated/captive portal, VPN의 앱 개발 계약이 System Internals로 밀려 있다.
- Wi-Fi, USB, UWB, CompanionDeviceManager 진입점이 없다.
- Bluetooth에는 GATT operation serialization, MTU, service changed, reconnect 전략이 없다.
- Media/Audio/Camera에는 Media3 lifecycle, 최신 audio focus 처리, CameraX use-case 결합과 concurrent camera가 없다.

### Testing과 성능

- 테스트 피라미드에서 Robolectric을 언급하지만 정본 노트가 없다.
- Gradle Managed Devices, Android Test Orchestrator, Room/WorkManager integration test, property-based testing, test data isolation이 없다.
- Android vitals/Play Console regression gate, network/energy measurement, statistical significance와 percentile 해석 정본이 없다.

### Security와 form factor

- Security에는 Credential Manager/passkey, authentication과 authorization 구분, exported component·WebView·IPC threat model 허브가 없다.
- crash diagnostic runbook이 없다.
- Wear에는 현행 Compose for Wear, Health Services, Watch Face Format, Ongoing Activity/Live Update, Data Layer migration이 없다.
- TV에는 Media3/session, playback lifecycle, home recommendation/channel, 최신 Compose for TV migration이 없다.
- Auto에는 category별 지원 행렬, DHU/AAOS emulator test, distraction-optimized 상태, 별도 packaging·distribution 계약이 없다.
- ChromeOS에는 ARCVM 전환, file/clipboard/drag-and-drop, external display와 camera test가 없다.

## 축 3: 문체 불일치

- `00_foundations/topics/A3-A6`, `C1-C3`, `D1-D3`, `E1-E3`, `F1-F2`, `G1-G12`의 27개는 `합니다/됩니다`체와 영어 section title을 사용한다. A1·A2·B1-B4의 `-다`체·한국어 section과 생성 배치 경계가 뚜렷하다.
- `00_foundations/learning-spine/11-observation-testing-and-quality-feedback.md`와 `12-compatibility-update-and-form-factor.md`는 `feedback`, `trace`, `flaky`, `release gate`, `surface`, `lifecycle`을 인라인 풀이 없이 반복한다.
- `03_packaging_deployment` 55개 전체가 모든 section에 `(What & Why)`, `(Internal Mechanism)`, `(Observable Evidence)`를 반복한다.
- Packaging의 “완벽한 청사진”, “완벽히 조율”, “혁신적으로 단축”, “완벽히 예방”은 근거보다 홍보 어조가 강하다.
- Navigation의 “구시대 레거시 대 현대 표준”, Widget·Haptics의 “현대 표준/전수/정밀”도 이웃 문서보다 홍보문에 가깝다.
- Compose accessibility 원자 4개의 영어 문장 제목이 이웃 한글 제목과 다르다.
- DI 원자 노트는 `lifetime`, `owner`, `boundary`, `framework`, `graph`, `replacement seam`을 설명 없이 반복한다.

문체는 좋은 exemplar 한 개를 먼저 확정한 뒤 생성 배치 단위로 고쳐야 한다. 이번 감사에서는 일괄 수정하지 않았다.

## 축 4: Mermaid가 더 적합한 표현

다음 다섯 문서의 ASCII 표현은 단순 표가 아니라 관계·순환·상태 전이를 나타내므로 Mermaid가 더 정확하다.

- `02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/compose-state-owner-is-the-lowest-common-owner-that-needs-read-or-write.md`
- `02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/compose-runtime-links-state-effects-performance-and-tooling.md`
- `02_app_framework/jetpack-compose/runtime/compose-runtime-contracts/compose-ui-is-declarative-function-of-state.md`
- `02_app_framework/architecture/state-management/viewmodel/viewmodel-survives-configuration-change-not-process-death.md`
- `02_app_framework/architecture/state-management/ui-state/restorable-progress-belongs-in-uistate-not-one-off-event.md`

나머지 범위에서 발견한 directory tree, log, shell output, 단순 2행 mapping은 ASCII를 유지하는 편이 낫다. Foundations·System Internals·Security·Platforms 341개에서는 변환 가치가 있는 추가 후보가 없었다.

## 축 5: Fundamental과 상위 학습 경로

- `00_foundations/android-foundation-map.md`가 완성된 12장 Learning Spine을 기본 읽기 경로에 포함하지 않는다.
- System Internals 155개, Security 28개, Platforms 43개에는 Learning Spine 직접 링크가 없다.
- App Framework map은 Learning Spine 4~8장, Packaging map은 3·12장, System Services map은 10장, Testing/Performance map은 11장으로 연결해야 한다.
- Packaging 55개에는 `배경 지식:`과 Learning Spine 연결이 없다. dependency graph/DAG, compiler-linker, semantic versioning, cryptographic signature/chain of trust, software supply chain 정본이 필요하다.
- Testing/Performance 33개에는 `배경 지식:` 1개와 Learning Spine 연결 1개만 있다. benchmark statistics, percentile/variance, test double, deterministic execution 정본이 필요하다.
- DI의 `dagger-is-static...`, `scope-matches...`, `dsl-syntax...`는 기존 DIP 정본 대신 관련성이 낮은 memory-layout 문서를 연결한다.
- sensor batching의 POSIX pipe/FIFO, Compose performance의 process lifecycle 링크는 해당 mechanism의 적절한 배경 문서가 아니다.
- Binder object capability 문서는 기존 IPC mechanism과 access control model 정본으로 연결해야 한다.

## 링크·중복·도달성 감사

### 링크

- vault-root Markdown target: 지식 문서 51개에서 113건, `_meta`에서 42건.
- 대상 파일은 155/155 모두 존재한다.
- Obsidian은 vault-root path를 지원하므로 앱 내부 broken link가 아니다.
- `.obsidian/app.json`은 `useMarkdownLinks: true`, `newLinkFormat: "relative"`이므로 새 링크 설정과 불일치한다.
- GitHub/CommonMark와 일반 exporter에서는 파일 기준 상대경로가 아니어서 깨질 수 있다. 113개 지식 링크는 실제 대상을 계산해 상대경로로 기계 변환할 수 있다.
- `_meta`의 존재하지 않는 target 5건은 계획서가 설명용으로 적은 `경로.md`, `상대경로` placeholder이며 실제 지식 링크가 아니다.
- wikilink처럼 보인 6건은 계획서 예시, Kotlin compiler 문자열, Bash 조건식으로 확인했다.
- 절대 filesystem path 또는 `file://` 링크, H1, 중복 filename stem은 없다.

### 도달 불가능한 지식 문서 3개

- `01_system_internals/ipc-and-process/ipc-process-contracts/posix-ipc-vs-android-binder-contracts.md`
  - 단순 연결하지 않는다. 사실을 전면 교정한 뒤 유효 비교만 Binder 정본에 흡수하고 삭제하는 방안이 우선이다.
- `02_app_framework/data/async-flow/android-coroutines-flow.md`
  - 유효한 중간 허브다. `data/android-data-layer-map.md`에서 연결한다.
- `02_app_framework/navigation/intents-and-deep-links/intent-and-deep-link.md`
  - navigation master와 하위 contract hub를 중복하는 얕은 router다. 삭제가 적절하다.

### 중복과 합치기·쪼개기 후보

- exact body duplicate는 Android 16/17 피해 문서와 History Contracts 한 쌍뿐이다.
- DI 19개 micro note는 생성/binding, ownership/scope, tool comparison 세 묶음으로 먼저 합친 뒤 독립 evidence가 있는 주제만 다시 분리한다.
- Compose design-system/accessibility 14개 thin note는 design-system과 accessibility 두 정본으로 합친 뒤 독립 예시가 있는 주제만 분리한다.
- `file-storage-is-selected-by-owner-and-public-purpose.md`와 `choose-storage-by-data-lifetime-and-ownership.md`는 병합 후보이다.
- app-components의 entry-point atomic은 `android-app-components.md`와 `app-component-contracts.md`에 흡수한다.
- `media-audio-camera-contracts`는 보강할 때 media, audio, camera 세 cluster로 분리한다.
- Compose Runtime map과 inner contracts, Paging map과 contracts, Compose Design System map과 contracts는 원자 목록을 중복한다. 한쪽을 진입 지도, 다른 쪽을 local index로 명확히 축약한다.
- DI 바깥 map은 inner contracts의 20개 목록을 전부 반복한다. 바깥은 local contracts 링크 하나로 축약한다.
- `dsl-syntax...`와 `modular-di...` 안의 형제 20개 목록은 parent link 하나로 축약한다.
- Koin trade-off 문서는 compile-time/runtime DI 비교 문서와 통합하거나 Koin 고유 resolution·verification evidence를 보강한다.
- Kernel map/contracts와 HAL map/contracts는 역할 중복을 줄인다.
- Android release history는 연대표 checkpoint와 장기 architecture transition을 분리한다.
- Android Auto와 AAOS의 manifest·배포·test 경로는 별도 문서로 분리한다.

## 즉시 수행한 기계 복구

총 30개 고유 파일에서 다음 확정 결함을 수정했다.

| 수정 | 수량 |
|---|---:|
| 손상된 KMP hub 복구 | 1파일 |
| `derivedStateOf`, `CompositionLocal`, `clearAndSetSemantics` 식별자 오염 | 4행/4파일 |
| `<CR>ightarrow`를 `\rightarrow`로 복구 | 13곳/7파일 |
| `<TAB>ext`, `<TAB>imes`를 `\text`, `\times`로 복구 | 3행/3파일 |
| `.md`가 붙은 frontmatter title 수정 | 4파일 |
| 누락된 `date created` 추가 | 1파일 |
| H2보다 앞선 `배경 지식:` 행 이동 | 11파일 |

본문 사실 교정, 문체 통일, ASCII→Mermaid, fundamental 신설, 113개 링크 변환, 고아 연결·삭제, history 재작성은 이번 감사에서 수행하지 않았다.

## 다음 수정 Phase 권장 순서

1. Android 16/17 history 피해 문서를 최신 공식 상태로 복구한다.
2. P0 사실·코드 오류를 공식 1차 문서와 대조해 수정하고 예제를 compile/test 가능한 형태로 바꾼다.
3. App Components·DI·Compose·System Services thin batch를 병합 우선으로 재설계한다.
4. 고아 3개를 각각 흡수·연결·삭제한다.
5. top-level map에서 Learning Spine과 기존 fundamental 정본을 연결한다.
6. 문체 exemplar 하나를 확정하고 Foundations topics 27개와 Packaging 55개를 batch 정규화한다.
7. 5개 ASCII 관계도를 Mermaid로 전환한다.
8. vault-root link 113개를 파일 상대경로로 변환하고 Obsidian·CommonMark 양쪽에서 검증한다.
9. exact duplicate, link resolution, BFS orphan, first-H2, CR/tab, API identifier 검사를 다시 실행한다.

### 공식 교차 검증 자료

- [Android 16KB page sizes](https://developer.android.com/guide/practices/page-sizes)
- [Android Vitals ANR](https://developer.android.com/topic/performance/vitals/anr)
- [Google Play alternative billing](https://developer.android.com/google/play/billing/alternative)
- [Google Play payments policy programs](https://support.google.com/googleplay/android-developer/answer/13821247)
- [Android Keystore](https://developer.android.com/privacy-and-security/keystore)
- [KeyInfo](https://developer.android.com/reference/android/security/keystore/KeyInfo)
- [Kleaf support matrix](https://source.android.com/docs/setup/reference/bazel-support)
- [Wear always-on guidance](https://developer.android.com/training/wearables/always-on)
- [Compose for TV](https://developer.android.com/codelabs/compose-for-tv-introduction)
- [Obsidian internal links](https://obsidian.md/help/links)
