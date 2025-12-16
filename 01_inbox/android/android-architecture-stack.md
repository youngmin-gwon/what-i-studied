---
title: android-architecture-stack
tags: [android, android/architecture, android/layers]
aliases: []
date modified: 2025-12-16 15:41:28 +09:00
date created: 2025-12-16 15:22:42 +09:00
---

## Android Architecture Stack android android/architecture android/layers

[[android-foundations]] · [[android-hal-and-kernel]] · [[android-zygote-and-runtime]] · [[android-binder-and-ipc]]

### 계층 개요
1. Linux Kernel: 프로세스/스레드, 메모리 관리, SELinux, cgroups, ION/DMABuf, 커널 드라이버.
2. Hardware Abstraction Layer(HAL): 공급업체 구현이 준수해야 할 C/C++ 인터페이스. HIDL→AIDL 전환 중.
3. Native Services: SurfaceFlinger, MediaServer, AudioFlinger, sensors, keystore 등.
4. Android Runtime(ART): DEX 실행, JIT/AOT, GC, JNI bridge.
5. System Services(Java framework): ActivityManagerService, PackageManagerService, WindowManagerService, ConnectivityService 등.
6. Framework APIs & Jetpack: SDK/Jetpack, compatibility shims, AndroidX.
7. Apps: 앱 샌드박스에서 동작하는 Activity/Service/Receiver/Provider.

### 리눅스 커널 역할
- 스케줄링: CFS + RT class; freezer cgroup 으로 백그라운드 작업 일시 정지.
- 메모리: overcommit, lowmemorykiller daemon(LMKD) 와 psi 기반 pressure stall metrics 로 OOM 조정.
- 보안: SELinux enforcing(denial→audit); seccomp-BPF 필터로 syscalls 제한; namespaces(UTS, PID, mount, net) 와 capabilities.
- 파워: wakelock 커널 인터페이스, cpuidle/cpufreq scaling, suspend blockers, wakelock_stats.
- 디바이스: binder driver, ashmem→memfd, ion→dmabuf, display/audio/camera drivers.

### HAL 세부
- HIDL(HAL Interface Definition Language): older binderized HAL 정의; 버전별 안정성을 제공하지만 언어 제약이 있음.
- AIDL(HAL 용): Android 11+ 에서 mainline 화, stability annotations(@VintfStability), frozen parcelables, 테스트 편의성.
- Passthrough HAL → binderized HAL 전환: 프로세스 격리 강화, 안정성/보안 개선.
- VINTF(Vendor Interface): framework/hal 호환성 계약 (manifest + matrix). System/vendor 파티션 독립적 업데이트를 가능하게 함.

### Native 서비스와 그래픽 파이프라인
- SurfaceFlinger: 컴포지터; HWC2 와 협업, layer stack, transaction + fences. [[android-performance-and-debug]] 참고.
- RenderThread: View/Compose 렌더링을 오프로딩; Skia GPU backend(ANGLE/Vulkan/OpenGL).
- AudioFlinger/AudioPolicy: 스트림 믹싱, 정책 라우팅, 효과 체인, AAudio/AAudio MMAP.
- MediaServer(MediaCodec/Extractor/Drm): codec2/codec1, stagefright; DRM 은 clearkey/widevine plugin 모델.

### 앱 호환성 계층
- Compatibility Framework: change ID 토글로 targetSdk 별 behavioral change 를 관리. `adb shell am compat` 로 테스트.
- hidden API enforcement: whitelist/greylist/blacklist; reflection 제한을 통해 안정성 확보.
- AndroidX 는 백포트 라이브러리 역할을 하며, SplashScreen/Activity/Lifecycle/Compose/Navigation 등으로 OS 버전 차이를 평탄화.
- Mainline(APEX) 모듈: ART/Media/NNAPI/Conscrypt/PermissionController/Statsd/Connectivity 등이 독립 업데이트되어 보안/호환성 개선.
- WebView 는 별도 APK 로 업데이트되며, Trichrome 라이브러리 분리 모델로 크기 최적화.

### ART 층
- GC: generational/region-based, concurrent mark-sweep, TLAB. Pause time 목표로 다양 조정.
- JIT/AOT: profile-guided; quick vs speed vs speed-profile filters; app startup 중 warmup compile.
- Images: boot image + app image; preloaded classes reduce startup. Relocation vs shared relro.
- JNI: local/global refs, critical sections, CheckJNI, native bridge(houdini) for ABI translation.

### 시스템 서비스 (Java)
- SystemServer 프로세스에서 기동. AMS/WMS/PMS/ConnectivityService/JobScheduler/AlarmManager/NotificationManager 등.
- ServiceManager 는 binder 서비스 registry 역할; lazy HAL/service init 로 부팅 최적화.
- Permission enforcement: 시스템 서비스 경계에서 binder transaction 마다 체크.
- System UI 는 별도 프로세스 (launcher/status bar) 로 동작, binder 통해 시스템 서비스 호출.

### 프레임워크 레이어
- SDK API surface 는 backward compatibility 에 민감; hidden API list(whitelist/greylist/blacklist) 로 동적 차단.
- Jetpack(AndroidX) 은 OS 버전 차이를 라이브러리로 보완; Compose/Activity/Fragment/KTX 등.
- Compatibility Modules(Mainline): ART, Media, NNAPI, Conscrypt, PermissionController 등 APEX 로 배포.

### 앱 레이어
- 앱은 sandboxed UID + SELinux domain 으로 격리. Permission 기반 access 제어.
- 프로세스 생성은 [[android-zygote-and-runtime]] 에서 설명한 zygote/fork 메커니즘.
- IPC 는 [[android-binder-and-ipc]] 를 통해 시스템 서비스와 통신.

### 스택 간 협업 흐름 예시: Activity start
1. 앱이 Intent 로 startActivity 호출 → ActivityTaskManager/ActivityManager binder 트랜잭션.
2. AMS 가 프로세스 존재 여부 확인→없으면 zygote 에 fork 요청.
3. 새 프로세스가 ActivityThread main 을 실행→Application/Activity 초기화→Binder attach→WindowManager 와 연결.
4. Input/Render 파이프라인이 붙으면서 최종 화면이 나타남.

### 스택 간 협업 흐름 예시: 카메라 캡처
1. 앱이 CameraX/Camera2 로 요청 → camera service binder.
2. HAL 이 sensor/ISP 와 인터랙트→DMABuf 공유 메모리→SurfaceFlinger/HWC 로 전달.
3. MediaCodec 이 인코딩→MediaMuxer/MediaStore 로 저장→Scoped storage 정책 적용.

### 전환기술 사례
- Dalvik VM → ART: ahead-of-time 컴파일로 성능·배터리 향상, 프로파일 기반 컴파일로 JIT 보완.
- HIDL → AIDL for HALs: 언어 호환성, 테스트 용이성, stability annotation 으로 vendor/framework 분리 강화.
- ION → DMABuf: 표준화된 buffer sharing, 보안/호환성 개선.
- Ashmem → memfd: upstream-friendly, sealing 지원으로 안전한 공유 메모리.
- kernel module → GKI + vendor modules: 커널 ABI 안정성과 OTA 간소화.

### 플랫폼 UX 계층
- System UI/Launcher 는 별도 프로세스로, status bar/notifications/quick settings/nav bar 를 제공. Shell transitions 로 애니메이션.
- Accessibility services 가 입력/윈도우 이벤트를 관찰·변형하며, TalkBack/Select-to-speak/Color correction 포함.
- InputMethod(IME)/Clipboard/Drag&Drop/DisplayManager 와 상호작용.

### 그래프 뷰를 위한 주요 링크
- [[android-boot-flow]], [[android-activity-manager-and-system-services]], [[android-security-and-sandboxing]], [[android-adb-and-images]], [[android-customization-and-oem]], [[android-evolution-history]].
