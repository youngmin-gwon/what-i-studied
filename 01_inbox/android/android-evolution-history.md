---
title: android-evolution-history
tags: [android, android/history, android/transitions]
aliases: []
date modified: 2025-12-16 15:41:44 +09:00
date created: 2025-12-16 15:25:47 +09:00
---

## Evolution & Technology Transitions android android/history android/transitions

[[android-foundations]] · [[android-architecture-stack]] · [[android-hal-and-kernel]]

### 런타임/언어 전환
- Dalvik→ART: 2014 Lollipop 에서 AOT 로 부팅/실행 속도 개선. Nougat 에서 hybrid profile-guided JIT/AOT 도입해 디스크/시간 균형.
- Java 6→8→11 desugaring: D8/R8 가 람다/default method/backport 지원. Kotlin 우선 정책으로 null-safety, coroutine 기반 구조 확산.
- Instant Apps→App Bundles(AAB)+Play Feature Delivery: split APK, asset delivery(install-time, on-demand, fast-follow, instant) 로 배포 최적화.
- Jack/Jill 실험적 toolchain 폐기 후 D8/R8 가 표준화.\n

### IPC/HAL 전환
- HIDL→AIDL HAL: interface stability 단순화, 언어 중립성, 테스트 용이성. Stable AIDL(@VintfStability) 로 vendor-framework decoupling.
- ashmem→memfd: upstream 호환성, sealing. ion→dmabuf: 표준 buffer sharing.
- binderized HAL 로 프로세스 격리 강화; passthrough HAL 감소.
- binderfs 도입으로 namespace/권한 분리. binder caching, lazy init 연구.

### 그래픽/미디어
- OpenGL ES→Vulkan: low-overhead rendering, ANGLE adoption for compatibility.
- SurfaceFlinger → HWC2/Composer2: HW composer 우선, BLASTBufferQueue 로 transaction latency 감소.
- MediaCodec2/Codec2: modular codec interface, DRM 개선 (keystore2/KeyMint).

### 보안 정책 변화
- install location/open external storage → scoped storage + SAF + MediaStore.
- background execution → foreground service requirement, JobScheduler/WorkManager 중심.
- Permission 모델 진화: runtime permissions, one-time, approximate location, notification runtime opt-in, photo picker.
- Verified Boot→AVB2 + rollback protection; SafetyNet→Play Integrity.
- AppOps 확장, restricted settings(API 33), clipboard autoredaction, mic/camera indicators/toggles.

### 배포/업데이트
- Non-A/B OTA → A/B seamless; dynamic partitions(super) 로 공간 유연성.
- Mainline/APEX: ART/Media/NNAPI/PermissionController 등 모듈 업데이트. Google Play System Updates.
- Incremental FS & Play Asset Delivery 로 스트리밍 설치.
- Project Treble 로 system/vendor 분리, GSI 를 통한 호환성 테스트 필수화.

### 디버깅/프로파일링
- systrace → Perfetto, simpleperf, heapprofd/memtrack. bugreport 개선 (zip bundle, timestamps).
- StrictMode 확장, ANR trace quality 개선.

### UI 패러다임
- View system → Jetpack Compose: declarative, recomposition, state hoisting. ConstraintLayout→MotionLayout. Navigation component.
- Material Design → Material 3/You/Monet(dynamic color).
- Gesture navigation, predictive back, lockscreen personalization 진화. Foldable/large screen 대응 가이드 추가.\n

### 버전별 하이라이트 (요약)
- Cupcake~Gingerbread: 앱 위젯, copy/paste, NFC 초창기, Dalvik JIT. Holo 디자인 전개 준비.
- Honeycomb: tablet 전용 UI, SystemBar/Fragment 등장, RenderScript(후퇴).
- Ice Cream Sandwich/Jelly Bean: Holo + hardware acceleration, Project Butter(60fps), Doze 개념 전조.
- KitKat: Immersive mode, ART 프리뷰, NFC host card emulation, Storage Access Framework 시작.
- Lollipop: ART 기본, Material Design 1, JobScheduler, Camera2, Project Volta(배터리).
- Marshmallow: runtime permissions, Doze/App Standby, adoptable storage, fingerprint API.
- Nougat: multi-window, Vulkan 1.0, File-based encryption, Doze on the go.
- Oreo: Project Treble, notification channels, background limits, AAudio, Autofill.
- Pie: App Standby Buckets, slices/app actions, display cutouts, Digital Wellbeing.
- 10: gesture navigation, scoped storage(soft launch), privacy toggles(location/mic/camera indicators later).
- 11: one-time permissions, Bubbles, HAF/pandemic-driven background start limits, incremental FS.
- 12: Material You/Monet, Private Compute Core, approximate location, rich haptics.
- 13/14: per-app language, photo picker, predictive back, FGS types, Health Connect, partial screen sharing.

### 배터리/성능 정책
- Doze/App Standby introduced in Marshmallow; adaptive battery/standby buckets in Pie; expedited jobs/FGS restrictions in Android 13/14.
- LMKD psi 기반 → freezer cgroup/cached compaction.

### DevOps 변화
- Gradle plugin incremental improvements, configuration cache. Bazel adoption in AOSP.
- Firebase Test Lab/cloud device farm commonplace.

### 앞으로의 흐름 (추정)
- Rust adoption in platform code(binder/USB/bluetooth), memory safety 확대.
- Better isolation for ML/AI workloads; NNAPI/MediaPipe integration.
- Privacy sandbox on Android(PSA) for 광고 추적 제한.

### 링크
- [[android-customization-and-oem]]: Treble/Mainline 영향.
- [[android-security-and-sandboxing]]: 정책 변화와 보안.
- [[android-performance-and-debug]]: Perfetto 등 신형 도구.
