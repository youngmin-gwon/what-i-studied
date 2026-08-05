---
title: android-topics-map
tags: [android, android/foundations, topic-synthesis]
aliases: ["Android 주제별 합성 문서(Topic Synthesis) 지도"]
date modified: 2026-08-05 10:20:00 +09:00
date created: 2026-08-05 09:00:00 +09:00
---

## Android 주제별 합성 문서(Topic Synthesis) 지도

이 지도는 `00_foundations/topics/` 의 33개 주제 합성 문서를 모은다. 각 문서는 하나의 실무 주제(예: "Jetpack Compose 완전 이해")를 다루는 원자 노트들을 모아 그 주제의 80%를 한 문서로 이해할 수 있게 조합한 글루(glue) 레이어다. 개별 원자 노트가 정본이고, 이 문서들은 정본으로 가는 진입점이다.

이 지도는 Learning Spine 처럼 순서대로 읽는 문서가 아니라, 특정 주제가 궁금할 때 바로 찾아 들어가는 색인이다.

### A. System Internals

- [A1 · Android 부팅과 프로세스 생성](./A1-boot-and-process.md)
- [A2 · Binder와 IPC 완전 이해](./A2-binder-and-ipc.md)
- [A3 · 커널·HAL·드라이버 계층](./A3-kernel-hal-driver.md)
- [A4 · 렌더링 파이프라인 (Surface → SurfaceFlinger → 화면)](./A4-rendering-pipeline.md)
- [A5 · 네트워크 스택 (ConnectivityService → netd → 커널)](./A5-network-stack.md)
- [A6 · 플랫폼 모듈화 (APEX, Mainline, Treble, GKI)](./A6-platform-modularity.md)

### B. App Framework

- [B1 · 컴포넌트 생명주기와 Task / Back Stack](./B1-component-lifecycle-and-task.md)
- [B2 · Jetpack Compose 완전 이해](./B2-jetpack-compose.md)
- [B3 · 데이터 레이어: Flow·Room·DataStore·Paging](./B3-data-layer.md)
- [B4 · 내비게이션과 딥링크](./B4-navigation-and-deeplink.md)

### C. System Services

- [C1 · 백그라운드 실행과 스케줄링 선택](./C1-background-and-scheduling.md)
- [C2 · 디바이스 기능 접근](./C2-device-capabilities.md)
- [C3 · 시스템 서비스 조회 패턴](./C3-system-service-lookup.md)

### D. Security & Privacy

- [D1 · 권한 모델 완전 이해 (Permission → AppOps → SELinux)](./D1-permission-model.md)
- [D2 · 안전한 저장소와 암호화](./D2-secure-storage-and-crypto.md)
- [D3 · 앱 무결성 검증 (Play Integrity, AVB, dm-verity)](./D3-app-integrity-verification.md)

### E. Packaging, Performance & Testing

- [E1 · 빌드에서 설치까지 (Gradle → APK/AAB → PackageManager)](./E1-build-to-install.md)
- [E2 · 성능 측정과 최적화 (Baseline Profile, Macrobenchmark)](./E2-performance-measurement-and-optimization.md)
- [E3 · 테스트 전략 (Unit → Integration → UI → E2E)](./E3-testing-strategy.md)

### F. Platforms & Form Factors

- [F1 · 대화면·폴더블 적응형 레이아웃](./F1-large-screen-adaptive-layout.md)
- [F2 · 폼 팩터별 계약 (Wear OS / TV / Auto / ChromeOS / XR)](./F2-form-factor-contracts.md)

### G. Coverage Gap 보강 주제 (Phase 9)

Phase 1 coverage matrix 와 사용자 요청으로 새로 신설된 클러스터를 다루는 주제다.

- [G1 · 인앱 결제 (Google Play Billing)](./G1-in-app-billing.md)
- [G2 · Bluetooth Classic·BLE](./G2-bluetooth-classic-and-ble.md)
- [G3 · App Widget과 Glance](./G3-app-widget-and-glance.md)
- [G4 · 온디바이스 AI/ML (ML Kit, TFLite, AICore)](./G4-on-device-ai-ml.md)
- [G5 · WebView](./G5-webview.md)
- [G6 · App Shortcuts](./G6-app-shortcuts.md)
- [G7 · Android CI/CD와 자동화 배포 파이프라인](./G7-android-ci-cd.md)
- [G8 · 네트워크 클라이언트 계층과 통신 규약 (Retrofit/OkHttp)](./G8-network-client-layer.md)
- [G9 · Espresso와 기기 기반 UI 테스트 전략](./G9-espresso-and-instrumented-ui-test.md)
- [G10 · 지역화(Localization)와 RTL 레이아웃 대응](./G10-localization-and-rtl.md)
- [G11 · Play Core 서비스와 배포 및 리뷰 관리](./G11-play-core-in-app-update-and-review.md)
- [G12 · Custom Tabs와 브라우저 통합 탐색](./G12-custom-tabs.md)

### G13~G17. Tier 2 보강 주제

Phase 9 에서 우선순위가 낮다고 판단해 보류했다가, 사용자 요청으로 뒤이어 착수한 5개 주제다. 원자 노트는 대응하는 기존 클러스터(networking-contracts, 신설 multiplatform-contracts/appsearch-contracts/speech-contracts/downloadable-fonts-contracts)에 있다.

- [gRPC는 REST와 다른 타입 세이프 스트리밍 계약을 선언한다](../../02_app_framework/data/networking/networking-contracts/grpc-declares-typed-streaming-contract-while-rest-stays-single-shot-request-response.md)
- [Kotlin Multiplatform 계약](../../02_app_framework/architecture/multiplatform-contracts/multiplatform-contracts.md)
- [AppSearch 접근 계약](../../04_system_services/device-capabilities/appsearch-contracts/appsearch-contracts.md)
- [음성 합성/인식 접근 계약](../../04_system_services/device-capabilities/speech-contracts/speech-contracts.md)
- [Downloadable Fonts 접근 계약](../../02_app_framework/ui/system/downloadable-fonts-contracts/downloadable-fonts-contracts.md)

### 이 지도가 다루지 않는 것

- 순서를 갖고 처음부터 끝까지 읽는 커리큘럼은 [Learning Spine](../learning-spine/01-android-ecosystem-and-contract-surfaces.md)이 다룬다.
- 여러 계층을 하나의 실패/성공 흐름으로 추적하는 서사는 [Worked Examples](../worked-examples/01-app-icon-tap-to-first-frame.md)가 다룬다.
- 증상에서 조사 절차로 바로 이어지는 진단은 [Diagnostic Runbooks](../diagnostic-runbooks/01-app-launch-slow-or-fails.md)가 다룬다.
