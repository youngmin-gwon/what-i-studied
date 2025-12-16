---
title: android-os-development-guide
tags: [android, android/aosp, android/build, android/osdev]
aliases: []
date modified: 2025-12-16 15:52:33 +09:00
date created: 2025-12-16 15:27:24 +09:00
---

## Android OS Development Guide android android/osdev android/aosp android/build

[[android-customization-and-oem]] · [[android-hal-and-kernel]] · [[android-boot-flow]]

### 소스 준비
- repo init/sync 로 manifest 기반 fetch. shallow clone 시 특정 브랜치 depth 관리. local manifest 로 사내 미러/프로프라이어터리 blob 포함.
- 빌드 환경: `source build/envsetup.sh` → `lunch <target>`. ccache/distcc 설정, Goma/remote exec.
- Bazel 실험: `bazelisk`/`mixed builds` 로 Soong+Bazel 하이브리드.

### 빌드 시스템
- Soong(bazel-like graph) → ninja. Android.bp 파일로 모듈 정의 (java_library, cc_library, aidl_interface, apex, etc.).
- Make 에서 Soong 으로 전환 진행; Blueprint/soong_config_variables 로 제품별 설정. APEX/APK/CC/Java 모듈 타입.
- Incremental build: `m`/`mmm`/`mma`/`m apex_info`. `soong_ui.bash --dumpvars-mode` 로 변수 확인.
- Kati/Ninja 병렬빌드, remote cache, `USE_RBE` for remote execution. mixed builds with Bazel for selected modules.
- Build artifacts: target-files.zip → OTA payload, super image, vbmeta. `build/make/tools/releasetools` 스크립트 커스터마이징.

### APEX/Module
- APEX: fs container with manifest.json, key-signed. Updates via Play System Update. ART/Mainline modules 배포.
- `apexer`/`deapexer`/`apksigner`/`apexkey` 관리. prebuilts/apex/ for prebuilt modules.
- apex payload 는 dm-verity hash tree 포함. `apexd` 가 install/activate 관리, rollback data 유지.

### Device Bring-up
- `device/<vendor>/<product>` tree: BoardConfig, kernel config, fstab, init scripts, sepolicy, overlays.
- blobs: proprietary vendor files pulled via `extract_utils`. VINTF manifest + matrix alignment.
- Treble: system/vendor 인터페이스 명확화, GSI 부팅 확인.
- boot image signing keys, AVB key provisioning, fastbootd/dynamic partitions 지원 확인.
- sepolicy bring-up: `audit2allow` 분석 → 최소 allowlist. neverallow hit 해결. seapp_contexts for app domains.

### Kernel 작업
- repo synced GKI + vendor modules. defconfig 관리, `build.sh` or `bazel build //common:kernel`. clang/LLVM toolchain.
- kprobes/tracepoints/ftrace/perf for debugging. `CONFIG_KASAN/KCOV` optional for fuzzing.
- SELinux labels/device nodes alignment, `avc: denied` 로그로 policy 조정.

### HAL/Driver 개발
- AIDL/HIDL interface 정의 → codegen → service stub 구현. binderized 서비스 등록 (hwservicemanager/service manager).
- VTS tests 작성/실행 `vts-tradefed`. HAL stability annotation, versioning strategy.
- camera/audio/sensors HAL: bufferqueue, DMABuf, sync fences, timestamp accuracy, power hints.

### Init/서비스 스크립트
- `init.<board>.rc`/`rc` snippets with on early-init/late-init/boot triggers. service class main/core/late_start definitions.
- property triggers(`on property:sys.boot_completed=1`). `write`, `chown`, `chmod`, `setrlimit`, `exec` commands.
- `ueventd.rc` for device node permissions. `fstab.<board>` for mount/encryption flags(late_mount, fileencryption=aes-256-xts, quotas).
- AIDL/HIDL service start order aligns with dependencies(hidl_service, service late_start). socket/perms/caps carefully set.
- init rc imports for APEX(/apex/*/etc/init/*.rc) automatically included; prefer APEXized services.\n

### Debug/Trace
- `adb shell setprop log.tag.<tag> DEBUG` for selective logging. log buffer main/system/events/radio/crash stats size.
- `perfetto` configs for system traces: cpu, sched, binder, wm, sf, hwc, memory, net. `systrace` legacy wrappers.
- tombstones: native crash, ANR traces. `anrd` collects ANR; `debuggerd` interactive backtrace.

### Testing
- CTS/VTS/GTS/STS for compliance. `tradefed.sh run cts --module …`. Filtering/sharding for speed.
- Unit/Integration: JUnit/Mockito/Truth; device-side instrumentation(`atest`, `am instrument`), `GTest` for native.
- Fuzzing: libFuzzer, AFL, sanitizers(ASAN/TSAN/UBSAN), `hwasan` builds for native memory safety.
- Security tests: fuzz binder services, selinux-deny tests, permission policy tests. fuzzing via `clusterfuzzlite`.
- Performance regression tests: microbenchmarks in platform-tests, Perfetto-based metrics diffing.

### Performance/Battery validation
- `perfetto` + `simpleperf`, `bpfloader` for network stats, `batterystats --enable full-wake-history`. Thermal profiles, powerhint logs.
- LMKD metrics/psi tuning. cold/hot start measurement for system apps.

### Signing/Keys
- releasekey/testkey/media/platform/shared keys. APEX keys separate. AVB keys for vbmeta/boot/system/vendor.
- `sign_target_files_apks` → `ota_from_target_files` pipeline. Incremental/full payloads.
- Key rotation, rollback index. OEM unlocking erases userdata.
- keystore signing for privileged apps vs platform cert. Jar signature schemes v1-v4 alignment. apksigner verify.

### Compliance/Privacy
- GDPR/local privacy: statsd/telemetry redaction, incidentd gating, user consent flows.
- Safety labeling/permissions review for system/privileged apps. hidden API exemption process.

### Distribution/Factory
- Factory flashing images, fastboot scripts, `brillo_update_payload`. Device bring-up labs with automation.
- post-init scripts for calibration(sensors), provisioning(attestation keys), oemlock state.

### Field Debug
- Remote bugreport, feedback collector, Device Config/Flags rollout. logcat size constraints, dropbox quotas.
- dogfood builds with gating experiments, OTA channel management.
- adb remap for persistent logs, diag port usage, early-boot traces. Offline symbol packages for native crash triage.
- triage playbook: repro scripts, perfetto template, tombstone/bugreport attachment, suspected change list from `repo forall -pc`.
- postsubmit dashboards: build health, presubmit flakes, CTS/VTS pass rates, crash/ANR regression monitors.

### CI/CD
- presubmit with `atest` selection, Lint/static analysis gates, formatting(Spotless/clang-format). Prebuilts cache to shorten build.
- artifacts: target-files.zip, incremental OTA, factory images, symbol archives. signing pipeline integration.
- release train cadence, branch cut policy, cherry-pick workflow with Gerrit + submit queues.

### 문서화/노트
- Keep design docs in-tree(go/… style internally), API review board for system API changes.
- Upstream patches to kernel/AOSP require CLA and code review (Gerrit). `repo upload` + presubmit.

### Graph Links
- [[android-architecture-stack]], [[android-security-and-sandboxing]], [[android-adb-and-images]], [[android-performance-and-debug]].
