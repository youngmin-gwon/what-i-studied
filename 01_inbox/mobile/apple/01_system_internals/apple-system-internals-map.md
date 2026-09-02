---
title: apple-system-internals-map
tags: [apple, apple/internals, map, moc, system-internals]
aliases: ["01_system_internals 는 앱 API 뒤에서 실제로 실행되는 6 개 플랫폼 계층을 다룬다", "Apple System Internals Map", "Apple 시스템 내부 지도"]
date modified: 2026-09-03 00:00:00 +09:00
date created: 2026-09-03 00:00:00 +09:00
---

## 01_system_internals 는 앱 API 뒤에서 실제로 실행되는 6 개 플랫폼 계층을 다룬다

이 폴더는 앱 코드가 호출하는 API 가 아니라, **그 API 뒤에서 커널과 시스템 데몬이 실제로 하는 일**을 다룬다. `URLSession.data(from:)` 한 줄이 왜 백그라운드에서도 계속되는지, `layer.cornerRadius` 하나가 왜 프레임을 떨어뜨리는지, 앱이 왜 예고 없이 사라지는지는 앱 API 문서가 아니라 이 계층에서 답이 나온다.

앱 관점의 사용법은 각 정본 영역에 있고, 이 폴더는 **그 아래에서 누가 무엇을 소유하고 강제하는가**만 다룬다.

### 하위 클러스터

| 클러스터 | hub 노트 | 다루는 범위 |
|---|---|---|
| [boot-and-runtime](boot-and-runtime/apple-boot-and-runtime.md) | 부팅과 실행 초기화 | Boot ROM → iBoot → XNU → launchd 신뢰 사슬, Mach-O/dyld 링크, pre-main 예산, RunLoop |
| [ipc-and-process](ipc-and-process/apple-ipc-and-process.md) | 프로세스와 통신 | Mach port/message, XPC, launchd 온디맨드 실행, RunningBoard assertion, Jetsam, watchdog |
| [kernel-and-driver](kernel-and-driver/apple-kernel-and-driver.md) | 커널과 드라이버 | XNU 의 Mach/BSD 분담, VM 과 메모리 압축, TrustedBSD MAC, AMFI, IOKit/DriverKit |
| [graphics-and-media](graphics-and-media/apple-graphics-and-media.md) | 화면과 미디어 | 레이어 트리 commit, Render Server 합성, offscreen 비용, 가변 주사율, IOSurface, mediaserverd |
| [storage](storage/apple-storage-internals.md) | 저장소 | APFS 클론/스냅샷, Data Protection 클래스, 앱 컨테이너 디렉터리 정책, 파일 조정 |
| [connectivity](connectivity/apple-connectivity-internals.md) | 네트워크 | Network.framework 상태 머신, ATS 기본값, 백그라운드 전송 데몬, 제약 경로 신호 |

### 읽는 순서

1. **boot-and-runtime** 으로 시작한다. 서명 검증 사슬과 `launchd` 가 이후 모든 클러스터의 전제다. 프로세스가 어떻게 생기고 무엇이 그것을 허가했는지를 먼저 잡는다.
2. **ipc-and-process** 로 이동한다. `launchd` 가 띄운 프로세스들이 서로 어떻게 말하고, 시스템이 그 프로세스를 언제 재우고 죽이는지를 다룬다. 앱이 예고 없이 사라지는 문제는 대부분 여기서 답이 나온다.
3. **kernel-and-driver** 로 내려간다. Mach port 도 sandbox 도 결국 커널 자료구조와 정책 모듈이므로 IPC 다음에 읽는다.
4. **graphics-and-media** 와 **connectivity** 는 이 시점부터 순서 상관없다. 둘 다 "앱 프로세스가 전담 데몬에게 일을 넘기고 결과만 받는다"는 같은 패턴을 화면과 네트워크에 적용한 사례다.
5. **storage** 는 언제 읽어도 되지만, Data Protection 클래스는 잠금 상태와 얽히므로 ipc-and-process 의 프로세스 수명을 먼저 읽으면 이해가 쉽다.

### 포함하지 않는 범위

- 앱이 직접 호출하는 프레임워크 사용법은 다루지 않는다. `URLSession` 레시피는 [03_data_networking](../03_data_networking/apple-networking-and-cloud.md), `BGTaskScheduler` 사용은 [04_system_services](../04_system_services/apple-background-tasks.md) 로 간다.
- Swift/ObjC 의 메서드 dispatch 와 ARC 는 언어 런타임이므로 [apple-runtime-and-swift](../00_foundations/apple-runtime-and-swift.md) 와 [apple-memory-management](../01_language_concurrency/apple-memory-management.md) 에 둔다. 이 폴더는 그 아래 커널 VM 까지만 다룬다.
- entitlement 를 어떻게 신청하고 서명에 넣는지는 [08_packaging_deployment](../08_packaging_deployment/apple-packaging-deployment-map.md) 에 둔다. 여기서는 커널이 그것을 **어떻게 강제하는지**만 다룬다.

### 문제 분류

- **앱 시작이 느리다**: boot-and-runtime 의 [pre-main 예산](boot-and-runtime/pre-main-launch-time-budget.md) 과 [dyld shared cache](boot-and-runtime/dyld-shared-cache.md) 를 본다.
- **앱이 백그라운드에서 예고 없이 죽는다**: ipc-and-process 의 [Jetsam](ipc-and-process/jetsam-memory-pressure-bands.md) 과 [watchdog 종료 코드](ipc-and-process/watchdog-termination-codes.md) 로 원인을 먼저 나눈다.
- **권한은 받았는데 API 가 실패한다**: kernel-and-driver 의 [AMFI](kernel-and-driver/amfi-code-signature-enforcement.md) 와 [TrustedBSD MAC](kernel-and-driver/trustedbsd-mac-and-sandbox-enforcement.md) 에서 게이트를 나눈 뒤 [apple-sandbox-and-security](../05_security_privacy/apple-sandbox-and-security.md) 로 간다.
- **스크롤이 끊긴다**: graphics-and-media 의 [commit 경계](graphics-and-media/layer-tree-commit-to-render-server.md) 와 [offscreen 비용](graphics-and-media/offscreen-rendering-cost.md) 으로 CPU/GPU 예산을 나눈다.
- **네트워크가 기기/상황마다 다르게 동작한다**: connectivity 의 [제약 경로 신호](connectivity/constrained-and-expensive-paths.md) 와 [ATS 기본값](connectivity/ats-transport-security-defaults.md) 을 본다.
- **파일이 사라지거나 잠금 상태에서 읽히지 않는다**: storage 의 [컨테이너 정책](storage/app-container-directory-policies.md) 과 [Data Protection 클래스](storage/data-protection-classes.md) 를 함께 본다.

### 관련 지도

- [apple-foundations](../00_foundations/apple-foundations.md) — 플랫폼 공통 철학과 학습 경로의 최상위 진입점.
- [apple-architecture-stack](../00_foundations/apple-architecture-stack.md) — 커널부터 앱까지의 계층 개괄. 이 지도는 그 개괄을 클러스터별로 펼친 것이다.
- [android-system-internals-map](../../android/01_system_internals/android-system-internals-map.md) — 안드로이드 대응 영역. Binder ↔ Mach port, Zygote ↔ dyld shared cache, SurfaceFlinger ↔ Render Server 로 대응시켜 읽으면 좋다.
