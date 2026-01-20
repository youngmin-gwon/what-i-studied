---
title: android-performance-and-debug
tags: [android, android/debugging, android/performance]
aliases: []
date modified: 2026-01-20 15:56:00 +09:00
date created: 2025-12-16 15:26:05 +09:00
---

## Performance & Debugging android android/performance android/debugging

앱을 부드럽고 튼튼하게 만드는 쉬운 체크리스트. 도구/용어는 [android-glossary](../00_foundations/android-glossary.md).

### 목표
- 시작: 차가운 시작 몇 초 안, 뜨거운 시작 1 초 내.
- 프레임: 16ms 안에 그려서 끊김을 줄이기.
- 메모리: 누수 없이, [[android-glossary#lmkd|LMKD]] 가 닫지 않도록 적정선 유지.
- 배터리: 불필요한 깨움 ([[android-glossary#wakelock|Wakelock]]) 줄이기.

### 시작 빠르게
- Baseline/Cloud 프로필로 자주 쓰는 코드를 먼저 준비한다.
- Application/DI 초기화를 늦추고, Splash 뒤에서 비동기로 처리한다.
- WebView/지도 같은 무거운 SDK 는 필요할 때만 예열한다.

### 렌더링 매끄럽게
- Compose: 재구성이 자주 일어나는지 체크, 상태를 화면 가까이 두기.
- View: RecyclerView 재사용/차이 계산, 중첩 레이아웃 줄이기, 과도한 그림자/투명도 줄이기.
- SurfaceView/TextureView 선택을 상황에 맞게. 프레임 지연 원인이 입력/CPU/GPU 중 어디인지 구분한다.

### 메모리 관리
- LeakCanary/Profiler 로 누수 탐지. `dumpsys meminfo` 로 Java/Native/Graphics 비율을 본다.
- 큰 이미지/버퍼는 재사용 풀을 쓰고, 필요 없으면 바로 해제한다.
- 네이티브 메모리도 모니터링 (simpleperf/Perfetto/`meminfo --unreachable`).

### 스레드/동시성
- 메인 스레드에는 화면·입력만. 나머지는 IO/Default 스레드 풀이나 [[android-glossary#workmanager|WorkManager]].
- [[android-glossary#binder|Binder]] 호출은 짧게, 큰 일은 비동기. 과한 oneway 호출은 큐를 막는다.
- [[android-glossary#anr|ANR]] 로그 (`traces.txt`, Perfetto) 로 어디서 멈췄는지 찾는다.

### 저장소/네트워크 효율
- Room 인덱스, WAL 사용, Paging 으로 큰 목록 나누기.
- HTTP 는 캐시/압축을 활용하고, 백오프/재시도 정책을 세운다.
- 네트워크 상태/비용을 보고 작업을 예약한다 (JobScheduler/WorkManager).

### 배터리 지키기
- Doze/App Standby 를 존중하고, 정확 알람은 꼭 필요할 때만.
- Foreground Service 는 사용자에게 보이는 일에만 사용, 알림을 항상 표시.
- Battery Historian/`dumpsys batterystats` 로 상위 소비자를 찾는다.

### 도구
- Perfetto/atrace: 전체 타임라인 추적.
- `dumpsys gfxinfo/frameStats` 와 FrameMetrics: 렌더링 확인.
- `simpleperf`/`android-addr2line`: CPU/네이티브 심볼 분석.
- [[android-glossary#bugreport|Bugreport]]: 종합 스냅샷.

### 릴리즈 안전망
- Lint/Detekt/CI 테스트로 기본 품질 확보.
- R8 난독화 후 mapping 파일 보관, Play Vitals 로 크래시/ANR 모니터링.
- 실험/롤백을 위한 리모트 설정과 안전 스위치 마련.

### 더 보기

[android-activity-manager-and-system-services](../01_system_internals/android-activity-manager-and-system-services.md), [android-security-and-sandboxing](../05_security_privacy/android-security-and-sandboxing.md), [android-adb-and-images](android-adb-and-images.md), [android-testing-and-quality](android-testing-and-quality.md).
