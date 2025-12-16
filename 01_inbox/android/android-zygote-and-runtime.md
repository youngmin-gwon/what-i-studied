---
title: android-zygote-and-runtime
tags: [android, android/runtime, android/zygote]
aliases: []
date modified: 2025-12-16 15:42:20 +09:00
date created: 2025-12-16 15:23:47 +09:00
---

## Zygote & Android Runtime android android/runtime android/zygote

[[android-architecture-stack]] · [[android-binder-and-ipc]] · [[android-activity-manager-and-system-services]]

### Zygote 의 역할
- 최초 부팅 시 zygote 가 startClassPath, preloadClasses/Resources 를 수행해 메모리 공유 기반 마련.
- 새 앱 프로세스 생성은 zygote 에 fork 요청을 보내는 방식으로 수행되어, preloaded page 를 공유함으로써 cold start 비용을 감소.
- 앱 프로세스는 fork 후 `ActivityThread.main()` 을 실행하며, Binder/Looper/Runtime 초기화를 이어간다.

### Preload 메커니즘
- `preloaded-classes` 목록에 핵심 프레임워크 클래스가 포함. boot image 와 함께 메모리 공유.
- `Resources` preloading: Drawable/Color/XML 등. Over-preload 는 메모리 낭비를 유발하므로 목록 튜닝 필요.
- zygote64/zygote32 두 개가 존재할 수 있으며, 앱 ABI 에 따라 선택.

### 앱 프로세스 시작 흐름
1. AMS 가 프로세스가 없음을 감지→ZygoteProcess.start() 호출.
2. Zygote socket 으로 arguments 전달 (nice name, UID/GID, mount namespace, seinfo, instruction set 등).
3. Zygote 가 `fork()` 후 child 에서 runtime flags 설정, `RuntimeInit.applicationInit` 실행.
4. `ActivityThread.main` 에서 Looper 준비, 앱 컨텍스트/Instrumentation 생성, ContentProvider 초기화.

### ART(런타임) 구성요소
- GC: sticky/partial/full mark-sweep, concurrent copying; pause time 줄이기 위한 read barrier, heap compaction 옵션.
- JIT: profile-guided, OSR(on-stack replacement). baseline JIT + hotness counter.
- AOT: `dex2oat` 로 oat/odex 생성. compiler filter: verify, quicken, speed-profile, speed, everything.
- Image: boot.art/boot.oat + app image. relocation/patching; `image.dirty-pages` 모니터링.

### Profile 과 성능
- Baseline Profiles: 빌드 시 제공되는 프로필로 cold start 성능 개선. Play cloud profile 은 서버에서 수집한 프로필을 배포.
- Warmup: Application start 직후 주요 경로를 터치해 프로파일 수집. Startup library/Jetpack Macrobenchmark 로 측정.
- DexLayout: layout profile 기반 dex section 재배치로 I/O locality 개선.

### GC 조정 포인트
- `android:largeHeap` 은 최후 수단. heap growth limit 와 concurrent GC 정책을 이해하고 메모리 leak 을 방지.
- `WeakReference`/`PhantomReference`/`ReferenceQueue` 사용 시 GC 타이밍 고려.
- Native memory(`malloc`, `Bitmap`, `DirectByteBuffer`) 는 separate accounting; `Debug.getNativeHeapAllocatedSize` 로 관찰.

### JNI 와 네이티브 연계
- JNI 호출은 CheckJNI 로 개발 중 오류 탐지. GlobalRef 누수 주의.
- `System.loadLibrary` 는 linker namespace 에 따라 격리; `public.libraries.txt` whitelist 개념.
- ART signal handler 는 managed/unmanaged 스택을 구분. unwinding 이 필요한 ndk-stack/symbolization 준비.

### 메모리 공유와 보안
- Zygote fork 는 COW(Copy-on-Write) 공유를 통해 메모리 절약. 초기화 코드가 많을수록 공유 페이지가 늘어남.
- seccomp filter 는 zygote 에도 적용돼 위험 syscall 차단. child-specific seccomp mask 적용.
- namespace: mount namespace 분리로 앱별 파일시스템 격리.

### 여러 zygote 와 isolated process
- webview/app_process 로 불리는 2nd zygote(webview zygote) 사용 가능해 WebView 전용 preloading 제공.
- IsolatedProcess 는 별도 UID 로 생성돼 권한 없는 샌드박스에서 실행 (Play Billing, WorkManager remote 등).

### 런타임 진화
- Dalvik → ART(KitKat preview/5.0 완전 전환): JIT→AOT, GC 개선. 이후 Nougat 에서 profile-guided hybrid.
- Project Mainline 이후 ART APEX 로 업데이트 가능, JIT/AOT 최적화가 Play System Update 로 배포.
- app compat: hidden API enforcement, greylist tightening.
- GC tuning: heap size target, concurrent copying collector, generational heap, moving GC(semispace) 선택. largeObjectSpace 관리.
- Prefetcher: Zygote 공간을 warm-up 해 cold start 를 줄이는 prefetchd, `dex2oat --image-classes` 목록 최적화.
- JVMTI: 프로파일러/agent 가 ART 에 attach 할 수 있도록 지원 (개발 빌드). JFR-lite 연구.

### 관련 링크
- [[android-performance-and-debug]]: startup profiling/GC 분석.
- [[android-boot-flow]]: zygote start 시퀀스.
- [[android-evolution-history]]: Dalvik→ART 전환 맥락.
