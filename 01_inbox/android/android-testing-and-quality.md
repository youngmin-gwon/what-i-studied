# Testing & Quality #android #android/testing #android/quality

[[android-foundations]] · [[android-performance-and-debug]] · [[android-os-development-guide]]

## 테스트 유형
- Unit tests: JVM(local) vs Instrumentation(device). Mockito/Truth/Kotlinx Coroutines test. Robolectric for framework shadowing.
- UI tests: Espresso(View), Compose UI test rule, macrobenchmark for startup/render/perf.
- End-to-end: orchestrator, Gradle Managed Devices, Firebase Test Lab/cloud farm.
- Native tests: GTest, instrumentation for JNI, fuzzing(libFuzzer) on native libs.
- Contract tests: AIDL/IPC stability tests, Compatibility Test Suite(CTS) subsets for SDK/library behavior.

## 아키텍처와 테스트 용이성
- MVVM/MVI/Clean architecture로 비즈니스 로직을 View/IO에서 분리해 테스트 가능성 향상.
- Repository + use case layer, interface-driven design. Dependency injection(Hilt/Koin/Dagger)로 mock 교체 용이.
- State holders(ViewModel/Presenter)에서 pure function/Flow 기반 설계.
- Compose UI tests: semantics tree, `performClick/TouchInput`, screenshot baselines. View tests: IdlingResource/CountingIdlingResource.
- Fake vs mock 구분; in-memory DB/HTTP fake로 flaky를 줄임. Clock abstraction으로 시간 의존성 제거.

## 도구/프레임워크
- JUnit4→JUnit5(gradle support), AssertJ/Truth, Kotlin test. CoroutineTestRule/MainDispatcherRule for dispatcher swap.
- Espresso IdlingResource/CountingIdlingResource, Compose `awaitIdle`, `runOnIdle`.
- Test orchestrator clears app state between tests; `clearPackageData` helps isolation.
- Snapshot/Golden tests: Paparazzi/Shot, Compose screenshot. Baseline images 관리 정책.
- Detekt/Lint custom rules to enforce architecture boundaries; API lint for libraries.

## 장치 구성 관리
- Gradle Managed Devices/AVD definitions. Snapshot boot for speed. `adb` selectors with `-s`.
- Device farm: FTL, AWS Device Farm. Sharding/parameterized runs. locale/orientation/density matrix.
- Performance-sensitive tests pin to hw accelerated emulators or physical devices; CPU/GPU throttling off. Thermal state control.

## 안정성/회귀 방지
- Contract tests for IPC/ContentProvider. Baseline profiles verification. API surface tests for libraries.
- Mutation testing(PIT), coverage reporting(Jacoco/Gradle). flaky test quarantine policies.
- Test impact analysis to select affected modules. incremental test runs; hermetic data seeds.
- Regression triage rituals: sheriffs/oncall rotation, automated bug filing with stacktrace clustering.

## 성능/배터리 테스트
- Macrobenchmark: startup/scroll/Jank. Perfetto trace parsing, metrics export.
- Microbenchmark(JMH/Jetpack Benchmark) for tight loops/allocations. Compose recomposition counts.
- Battery/thermal: `dumpsys batterystats --enable full-wake-history`, `perfetto power rail`. Game Mode/GameManager integration.
- Network/CPU/GPU/Memory KPIs tracked per build; threshold-based gating. E2E flows measured with scenario scripts.\n

## 네이티브/플랫폼 테스팅
- CTS/VTS for compatibility. `atest <module>` to target specific suites. Tradefed/sharding.
- sepolicy tests, hidden API enforcement tests, CTS verifier(manual). GSI device bring-up verification.
- vendor test suites(VTS) focus on HAL stability; MTS(Mainline Test Suite) for APEX.\n

## 릴리즈 품질 게이팅
- Static analysis: Android Lint/Detekt/Spotless, API lint. R8 shrink/obfuscate warnings budget.
- Crashlytics/Play Vitals ANR/crash rate gating. staged rollout with metrics. Feature flag kill switch.
- Accessibility checks: TalkBack, focus order, color contrast, font scaling. Pre-launch report bots.
- Release checklist: perf budgets, bundle size, baseline profile present, privacy/security review, changelog/rollback plan.
- rollout stages: internal dogfood → alpha → beta → prod staged; guardrails on ANR/Crash/FS violations.

## 디버깅/실험 문화
- Canary/internal builds with runtime flags(DeviceConfig/remote config). Experiment analysis dashboards.
- Structured logging with event IDs/tags, log sampling. PII redaction guidelines.
- Postmortem/RCAs on regressions, blameless culture, runbooks for incident response.
- SLO/SLA 정의: availability, crash-free sessions, latency targets. Error budgets와 릴리즈 동결 정책.

## 문서화/지식 공유
- ADR(Architecture Decision Record), design doc templates. code owners/review rotations.
- Onboarding playbook for new modules: build/run/test commands, trace recipes, perf baselines.
- Graph links for knowledge mapping: [[android-activity-manager-and-system-services]], [[android-security-and-sandboxing]], [[android-evolution-history]].
