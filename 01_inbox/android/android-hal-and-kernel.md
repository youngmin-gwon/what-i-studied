# Linux Kernel + Android HAL #android #android/kernel #android/hal #osdev

[[android-architecture-stack]] · [[android-customization-and-oem]] · [[android-binder-and-ipc]]

## 커널 핵심
- 프로세스 모델: clone/fork + namespaces. Android는 각 앱을 독립 PID namespace에 넣지 않지만 UID로 격리.
- 메모리: cgroup v1→v2 전환 진행, LMKD가 PSI 기반 메모리 pressure 감지 후 앱 종료. ZRAM, KSM(선택)으로 메모리 절약.
- 보안: SELinux enforcing 모드, sepolicy에서 domain/type 정의. seccomp-bpf로 위험 syscalls 차단(open_by_handle 등).
- 파워: suspend/resume, wakelock 커널 인터페이스(`/sys/power/wake_lock`). Energy Aware Scheduling(EAS)로 big.LITTLE 코어 활용.
- 스토리지: ext4/f2fs, dm-verity로 파티션 무결성 검증, file-based encryption(FBE)으로 사용자 데이터 보호.

## 드라이버와 서브시스템
- 디스플레이: DRM/KMS + HWC 협업, fence sync. Color management/refresh rate switching.
- 오디오: ALSA + tinyalsa, fast path vs deep buffer. AAudio MMAP.
- 센서: sensors HAL + input subsystem. flush/report latency 설정.
- 카메라: V4L2 + camera HAL3. bufferqueue via gralloc(HAL) → DMABuf.

## HAL 디자인 원칙
- 안정성: VINTF manifest/matrix로 버전 호환성 관리. HAL 인터페이스는 backward compatible evolution 필요.
- 격리: binderized HAL은 ServiceManager에 등록된 별도 프로세스; vendor 파티션에서 실행.
- 성능: zero-copy buffer 관리(DMABuf), binder transaction size 제한 고려, latency 민감 경로는 passthrough가 아닌 shared memory 사용.
- 테스트: VTS/VHAL tests, hwservicemanager/hidl_test, AIDL interface stability check.

## HIDL → AIDL 전환 상세
- HIDL의 interface/struct/enums vs AIDL의 Parcelable/Interface; stability annotation(@VintfStability)로 system/vendor 계약 유지.
- AIDL HAL은 Java/C++/NDK 지원, tooling 일원화. `aidl_interface` Bazel/Soong 모듈로 빌드.
- 데이터 표현: fixed-size array, vectors, nullable types. parcelable versioning/byte padding 주의.

## Vendor 파티션과 Mainline
- System-as-root와 A/B 파티션 구조에서 system/vendor 분리. Updatable APEX/Google Play System Update가 framework 부분을 업데이트해도 vendor는 그대로.
- HAL이 system API에 의존하지 않도록 stable API(SC-HAL) 사용.

## 커널 커스터마이징
- OEM은 device tree, defconfig, out-of-tree drivers 추가. Upstream 합치기 어려울 때 long term fork 유지.
- GKI(Generic Kernel Image): 공통 커널 모듈화를 통해 OTA 부담 감소. Vendor/OEM 모듈은 GKI 위에 로딩.
- Kernel ABI stability: symbol list freeze, `abi.xml` 검사.

## 메모리 관리 고급 주제
- LMKD: psi 파일 모니터링, kill timing heuristic(adjoint scores). AMS oom_score_adj와 연동.
- zygote preloading으로 페이지 공유 증가, page cache reclaim, swapiness tuning.
- userfaultfd 기반 fault isolation, MADV_FREE vs MADV_DONTNEED 차이.

## I/O 및 스토리지 최적화
- I/O scheduler: bfq/kyber. F2FS inline xattr, checkpoint tuning. fs-verity로 개별 파일 무결성.
- Incremental file system(INCFS)로 스트리밍 설치 지원; Play Asset Delivery와 연동.
- dm-user/dm-default-key, wrapped keys with hardware keystore. Inline encryption support(ciphers per file).
- Storage policy: project quotas per UID, reserved disk space for critical services, trim job scheduling.

## 타임/클럭/네트워크
- wakelock timeout, alarm RTC vs ELAPSED_REALTIME vs BOOTTIME. 타이머 coalescing으로 배터리 절약.
- netd + eBPF: data usage, tethering offload, per UID firewall. DNS over TLS, Private DNS enforcement.
- eBPF programs: xt_bpf replacement, clatd offload, traffic stats per UID/iface, Doze/standby enforcement.
- Network stack mainline module(NGS)로 업데이트; kernel hooks remain stable.\n

## 스케줄러/성능 튜닝
- EAS(Energy Aware Scheduling)로 big.LITTLE 워크로드 배치. schedutil governor, cpufreq policy per cluster.
- uclamp(turbo/boost)로 foreground thread latency 개선. task placement hints from userspace(ActivityManager hinting).
- scheduler groups/cgroups: top-app/background/system/rt; frozen group for cached apps. SchedTune legacy vs uclamp.
- thermal: trip points, mitigations(CPU/GPU throttling, camera/performance hints). power HAL과의 hint channel.
- binder/perf hints from SurfaceFlinger/RenderEngine for interactive responsiveness.

## 보안 하드닝
- Kernel self-protection: PAN/SMAP-like features, CONFIG_HARDENED_USERCOPY, CFI for kernel modules, KASLR.
- SELinux policy structure: type enforcement, MCS categories for per-app isolation. seapp_contexts mapping.
- Seccomp filters per process class(zygote child/system_server/webview). Landlock research for future isolation.

## 디버깅 기법
- `adb shell cat /sys/kernel/debug/tracing/trace_pipe` for ftrace; perfetto kernel tracing categories.
- dropbox native_crash/tombstone, kernel pstore/ramoops for panic logs. `kmsg`/`dmesg` availability depends on build type.
- `lmkd_stats`, `meminfo`, `/proc/pressure/*` for LMKD tuning. `binder_logs` in debugfs for binder driver state.\n

## 가상화/컨테이너
- microdroid/AVF(Android Virtualization Framework)로 하드웨어 가상화 기반 샌드박스 제공. crosvm/hypervisor + pVM.
- VirtIO devices for graphics/input/net; trust anchors(TA)로 attestation. VM payload delivery(APEX-based).
- containers: limited usage for app sandbox; isolate mount namespace for isolatedProcess/webview renderer.
- virtualization test: `avf_test_tool`, microdroid sample, protected VM memory constraints. hypervisor vendor support/arm64 features.

## 실전 bring-up 체크리스트
- kernel cmdline 옵션 확인(console, selinux, androidboot.*). verified boot/dm-verity 플래그.
- fstab/partition layout cross-check, dtb/dtbo overlay alignment. earlycon for early boot logs.
- HAL dlopen symbol resolution, linker namespace issues(public.libraries.txt). binder service registration success 여부.
- debug knobs: `adb shell cat /proc/cmdline`, `trace_event` toggles, debugfs mounts(for eng/userdebug). perfetto config for kernel events.

## 관련 링크
- [[android-boot-flow]]: 부팅 시 커널/ramdisk/early init 동작.
- [[android-security-and-sandboxing]]: SELinux/FBE/seccomp 연계.
- [[android-evolution-history]]: ashmem→memfd, ion→dmabuf 등 전환.
