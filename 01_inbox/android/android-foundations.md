---
title: android-foundations
tags: [android, android/architecture, android/fundamentals, mobile/os]
aliases: []
date modified: 2025-12-16 15:47:03 +09:00
date created: 2025-12-16 15:22:14 +09:00
---

## Android Foundations android android/fundamentals android/architecture mobile/os

[[android-architecture-stack]] · [[android-zygote-and-runtime]] · [[android-binder-and-ipc]] · [[android-security-and-sandboxing]]

### 목적과 철학
- "폰이자 리눅스 머신"이라는 이중성을 가진 플랫폼으로, 배터리·보안·커넥티비티 제약 속에서 확장성과 이식성을 최우선으로 설계됨.
- 오픈소스 (AOSP) 기반이지만, 실질적 제품은 OEM 커스터마이징 +GMS 계층이 얹히는 구조. 이는 [[android-customization-and-oem]] 에서 상세.
- 앱 개발자는 프레임워크 API 와 샌드박스 위에서 동작하며, 시스템 수준은 HAL/커널/런타임/서비스들이 보이지 않게 협조한다.

### 앱 구성 요소 요약
- `Activity`: UI 엔트리; 생명주기 콜백을 통해 자원 관리. [[android-activity-manager-and-system-services]]
- `Service`: 백그라운드 실행; 포그라운드/바인드/스타트 서비스 구분. [[android-binder-and-ipc]] 연계.
- `BroadcastReceiver`: 시스템/앱 이벤트 수신 후 짧은 처리; 지연된 작업은 WorkManager 로 위임.
- `ContentProvider`: 프로세스 간 데이터 공유 계약. 스키마 기반 URI + 퍼미션 제어.
- `Intent`: 컴포넌트 간 메시징 언어; 명시적/암시적, PendingIntent 로 대리 실행 권한 부여.

### 프로세스와 스레드 기본기
- 각 앱은 고유 UID/GID 로 격리된 리눅스 프로세스에서 실행되며, 기본 스레드는 `main(UI)` 이다.
- ANR 는 main 스레드 블로킹 (입력 5s, 브로드캐스트 10s 등) 으로 트리거. [[android-performance-and-debug]] 참고.
- 백그라운드 스레드는 HandlerThread, Executor, Coroutine Dispatchers(IO, Default), WorkManager 로 관리.
- 프로세스 우선순위 (포그라운드, 가시, 서비스, 백그라운드, 빈 프로세스) 는 LMK/psi(OOM killer) 와 연동.

### 패키징과 배포
- APK 는 `AndroidManifest.xml`, DEX, 리소스, native libs, META-INF 서명. AAB/Play Feature Delivery 시 split APK 생성.
- 서명 v1(JAR)/v2(전체 파일)/v3(롤오버)/v4(증분). Key rotation 으로 장기 유지관리.
- Install 과정: 패키지 매니저가 서명 검증→SELinux 정책/UID 할당→/data/app 에 확장→dexopt/compilation filter 적용.
- Update 시 동일 키 요구, 롤링 업데이트 중 atomic install 세트 사용. 롤백 데이터 정책 주의.

### 컴파일과 실행 경로
- DEX → ART JIT/AOT. Speed-profile, background dexopt, cloud profile push(Play) 로 워밍업.
- Baseline Profile 은 [[android-zygote-and-runtime]] 에서 설명한 prefetch/compilation 힌트 세트.
- Native lib 는 Bionic(GLibc 대체) 위에서 실행하며, linker namespacing 으로 ABI/NDK 안정성 확보.

### 리소스·구성 대응
- Qualifier 기반 리소스 선택 (sw600dp, night, land, locales). `Configuration` 변경 시 Activity 재생성 여부를 Manifest 에서 제어.
- Dynamic Feature Module 은 on-demand 설치, instant experience 와 연동.
- LocaleConfig/Per-app language API 로 다국어 런타임 전환.

### 입력·렌더링 파이프라인
- InputDispatcher 가 터치 이벤트를 포커스 윈도우에 전달 후, Choreographer vsync 프레임 스케줄에 맞춰 measure/layout/draw.
- Skia/RenderThread/Hardware Composer(HWC) 협업으로 GPU 컴포지션. SurfaceFlinger 가 최종 합성.
- jank 탐지 (FrameMetrics), DisplayList 재사용, doze/low power 모드에서 프레임 레이트 조정.

### 데이터 저장소
- 프라이빗 파일: /data/user/0/<package> with SELinux labels. Scoped storage 로 외부 저장소 접근 제한.
- Structured data: Room(SQLite), Proto/DataStore, Preferences. 대용량은 MediaStore/SAF 를 통해 공개 URI 로 접근.
- 백업: Auto Backup/Key-Value backup, device-to-device transfer. 암호화·opt-out 고려.

#### 네트워킹·연결성
- ConnectivityService 가 네트워크 정책, Captive portal 검증, multipath, VPN 을 총괄.
- JobScheduler/WorkManager 는 네트워크 제약 (UNMETERED 등) 과 Doze/Standby 정책을 고려해 작업 실행.
- HTTP 스택: HttpUrlConnection→OkHttp(많은 OEM), gRPC/QUIC, Cronet. TLS 는 Conscrypt/BoringSSL.

### 배터리·전력 정책
- Doze/App Standby/Battery Saver 가 타이머·네트워크 사용을 억제. AlarmManager exact trigger 제한.
- JobScheduler/WorkManager 가 배터리 조건을 협상. Foreground service 는 알림 의무화.
- Wakelock 은 PowerManager 로 획득, timeout 지정 필수. 기기 제조사별 aggressive policy 주의.

### 권한 모델
- 런타임 퍼미션 (위험 권한), one-time/precise vs approximate location, background location 별도 승인.
- 권한 그룹, 퍼미션 상속 (Signature/Privileged). Manifest protectionLevel 로 시스템 API 보호.
- 퍼미션은 [[android-security-and-sandboxing]] 의 SELinux/UID 격리와 함께 동작.

### 배포 채널과 업데이트 전략
- Play Store: staged rollout, device exclusion, Play Integrity/API attestation, Play Feature Delivery.
- Enterprise: Managed Google Play/MDM, private channel, OEM system apps with privileged perms.
- OTA: A/B partition, seamless update, rollback index/fuse. [[android-boot-flow]] 참고.

### 프레임워크와 라이브러리 선택
- Jetpack Compose vs XML View system 공존기: Compose 는 declarative UI, recomposition, state hoisting; View 는 legacy 호환/성숙한 위젯.
- Lifecycle/ViewModel/Navigation/Hilt/WorkManager/Room/CameraX 등 Jetpack 모듈이 표준 툴킷으로 정착.
- Kotlin 우선 전략: coroutines, Flow, suspend, KSP. Null-safety 와 inline class 로 API 품질 향상.

### 개발 생산성
- Gradle + AGP: variant-aware build, build cache, configuration cache, VFS watcher. Android Studio(Bazel/IntelliJ 기반) profiling 도구.
- CI: hermetic build, emulator farm, Firebase Test Lab, adb am instrument/Gradle Managed Devices.
- Static analysis: Lint, Detekt, Error-prone, R8 shrinking/obfuscation, StrictMode.

### 앱 아키텍처 패턴
- MVVM/MVI/Clean Architecture: UI state 는 `StateFlow`/`MutableState` 로 표현, reducer/intent 패턴으로 재현 가능성 확보.
- DI: Hilt/Dagger/Koin; entry point 를 최소화하고 scope( Singleton/Activity/ViewModel ) 를 명확히 해 메모리 누수 방지.
- Navigation: single-activity + Compose Navigation/Fragment Navigation; deep link/URI mapping, back stack save/restore.
- Modularization: feature module + core/common; dynamic feature(on-demand) 로 앱 크기/빌드 시간 최적화.
- Offline-first: Room/Datastore 캐시 + WorkManager sync; conflict resolution/merge 정책을 명시.

### 국제화·접근성
- i18n: ICU 기반 plural/gender formatting, locale fallback, per-app language 설정. bidi/RTL 레이아웃 확인.
- a11y: TalkBack focus order, contentDescription, semantics(Compose), touch target 48dp, contrast/animation scale 존중.
- 폰트/텍스트: Downloadable fonts, variable fonts. hyphenation/lineBreak strategy 설정으로 가독성 개선.
- Large screen/foldables: responsive layout, window size classes, posture-aware UI(hinge), drag-and-drop.

### 백엔드 연계
- 데이터 동기화: WorkManager + periodic/expedited job; retry/backoff, constraints(network/battery/idle).
- API 설계: REST/GraphQL/gRPC. Protobuf for contract, backward-compatible schema evolution(field numbering).
- 오프라인 큐잉: Outbox 패턴, idempotent 서버 API, request deduplication, conflict tokens.
- Push: FCM high/normal priority, notification vs data message, collapse keys, topic/device group.

### 오픈 소스/라이센스
- 서드파티 라이브러리 관리: Gradle version catalogs/toml, Dependabot/renovate. license plugin 으로 NOTICE 번들링.
- Play 정책 준수: SAF/MediaStore, 광고 식별자 제한, 백그라운드 위치 공개. 개인정보 처리방침 링크 필요.

### 디버깅·모니터링
- Logcat structured logging, systrace/Perfetto for system-wide tracing, heap profiling(ADB/JVMTI), ANR traces.
- Network Inspector, Layout Inspector(Compose hierarchy), GPU profiler. DropBoxManager 로 시스템 이벤트 수집.
- Crash: Java/Kotlin → uncaught exception handler, native → tombstone & tombstoned service.

### 학습 로드맵 연결

- 시스템 이해부터 앱 최적화까지 단계적으로 읽을 순서: [[android-architecture-stack]] → [[android-hal-and-kernel]] → [[android-zygote-and-runtime]] → [[android-binder-and-ipc]] → [[android-activity-manager-and-system-services]] → [[android-security-and-sandboxing]] → [[android-adb-and-images]] → [[android-customization-and-oem]] → [[android-evolution-history]] → [[android-performance-and-debug]].
- 각 문서는 Graph View 활용을 위해 주요 키워드를 [[link]] 로 상호참조한다.

### 특수 디바이스 고려

- Wear/Auto/TV: form factor 별 UX 정책과 permission/intent 필터 차이. Automotive power states, cold/garage mode, CAN/LIN 연계.
- Foldables/large screen: window size class, drag-and-drop, multi-instance activity, hinge posture. ResizableActivity/manifest flags.
- Low-RAM 기기 (go edition): dexopt filters, zram/tiny config, background limits 강화, lite SDK 선택.
- Rugged/전문 단말: barcode/industrial sensors, offline-first, kiosk/lock task, device owner workflows.\n
