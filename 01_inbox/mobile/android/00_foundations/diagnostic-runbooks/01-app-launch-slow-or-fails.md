---
title: 01-app-launch-slow-or-fails
tags: ["android", "android/foundations", "diagnostic-runbook"]
aliases: ["Runbook: app launch is slow or fails"]
date modified: 2026-08-04 16:00:00 +09:00
date created: 2026-08-04 10:30:00 +09:00
---

## 앱 실행이 느리거나 첫 프레임이 뜨지 않는다

### 1. 증상 및 징후 (Symptoms & Diagnostic Signals)

다음 중 하나 이상이 관찰된다.

- 앱 아이콘을 탭한 뒤 첫 화면(첫 프레임)이 뜨기까지 체감상 오래 걸린다(TTID 지연).
- 첫 화면(첫 프레임)은 빨리 뜨지만 콘텐츠가 없는 빈 화면/스켈레톤 상태가 오래 유지된다(TTFD 지연).
- 앱 실행 직후 하얀 화면(Blank Screen) 상태에서 응답이 없다가 ANR 다이얼로그가 뜨거나 앱이 즉시 종료된다(이 경우 [ANR runbook](02-anr.md) 또는 Crash 분석으로 전환한다).
- Android 15 기기에서 실행 직후 native `.so` 라이브러리 로딩 시 크래시(`UnsatisfiedLinkError`)가 발생하며 종료된다.

---

### 2. 재현 조건 및 환경 격리 (Reproduction & Isolation)

- **시작 유형(Cold / Warm / Hot) 분리**:
  - **Cold Launch (냉시작)**: `adb shell am force-stop <pkg>` 실행 후 앱 시작. 프로세스 생성, Zygote specialization, `Application` 생성, Activity 생성을 모두 거치는 최악의 경로.
  - **Warm Launch (온시작)**: 뒤로 가기(Back) 버튼으로 Activity 를 파괴하되 프로세스는 유지한 상태에서 시작.
  - **Hot Launch (열시작)**: 홈(Home) 버튼으로 백그라운드로 보낸 후 다시 전면 복귀.
- **측정 환경 고정**:
  - 반드시 **R8/Dex 최적화가 적용된 Release 빌드**(또는 Benchmark 빌드)에서 측정한다. Debug 빌드의 StrictMode, 디버거 에이전트, 로깅 코드는 시작 성능을 심각하게 왜곡한다.
  - 기기의 배터리 상태, 쓰로틀링(Thermal State), Baseline Profile 적용 여부를 동일하게 맞추고 최소 5회 이상 반복 측정하여 중앙값을 확인한다.

---

### 3. 실패 경계 및 원인 우선순위 (Failure Boundaries & Priority)

1. **`Application.onCreate()` 또는 시작 Activity 의 `onCreate()` / `onStart()` 내 메인 스레드 차단 (우선순위 1)**
   - 가장 흔한 원인. DI 그래프 생성(Dagger/Hilt/Koin), SDK 초기화, SharedPreferences 읽기, SQLite/DB 동기 쿼리, 원격 설정(RemoteConfig) 동기 차단 등.
2. **TTID 는 정상이나 TTFD 가 지연됨 (우선순위 2)**
   - 첫 프레임은 즉시 그려지지만, 메인 화면 UI 가 비동기 네트워크/DB 데이터 응답에 직렬로 의존하여 렌더링을 미루는 경우 ([Worked Example: 앱 아이콘 탭에서 첫 프레임까지](../worked-examples/01-app-icon-tap-to-first-frame.md) 참고).
3. **Android 15+ 16KB Page Size 미보응에 따른 Native Library Loading 실패 (우선순위 3)**
   - Android 15(API 35) 이상 기기에서 native `.so` 파일의 ELF segment 가 16KB boundary 로 정렬(alignment)되지 않아 프로세스 시작 중 `dlopen` 실패 및 `UnsatisfiedLinkError` 발생.
4. **Zygote Fork 및 프로세스 생성 지연 (우선순위 4)**
   - 시스템 전반의 메모리 부족(Low Memory Pressure)으로 인한 Zygote specialization 지연 또는 OEM OS 차원의 프로세스 생성을 방해하는 저전력 모드 정책.
5. **메인 스레드 교착 상태(Deadlock) 또는 무한 루프 (우선순위 5)**
   - 첫 프레임이 뜨기 전 메인 스레드가 Binder 차단, Lock 경합, I/O 대기에 빠진 상태. [ANR runbook](02-anr.md) 으로 전환한다.

---

### 4. 진단 의사결정 흐름도 (Diagnostic Decision Flowchart)

```mermaid
flowchart TD
    A["앱 실행 요청 (Tap App Icon)"] --> B{"프로세스 존재 여부?"}
    B -- "없음 (Cold Launch)" --> C["Zygote Fork & App Process 생성"]
    B -- "있음 (Warm/Hot)" --> F["Activity.onCreate / onStart"]
    
    C --> D{"Native .so 16KB 정렬 통과?"}
    D -- "실패 (Android 15+)" --> D_ERR["UnsatisfiedLinkError / Crash 발생\n(Check: readelf -l *.so)"]
    D -- "성공" --> E["Application.onCreate()"]
    
    E --> F
    F --> G{"Main Thread 블로킹 존재?"}
    G -- "예 (DB/I/O/Lock)" --> G_ERR["ANR / Launch Freeze\n(Refer: 02-anr.md)"]
    G -- "아니오" --> H["첫 프레임 렌더링 (TTID 출사)"]
    
    H --> I{"Displayed 로그 및 TTID 시간 판단"}
    I -- "TotalTime > 2000ms" --> J["Application/Activity onCreate 병목 프로파일링"]
    I -- "TTID 양호 (<500ms)" --> K{"reportFullyDrawn() 호출 여부 (TTFD)"}
    
    K -- "TTFD 지연 / 미호출" --> L["데이터 계층 비동기 파이프라인 점검\n(Refer: Spine Ch 8)"]
    K -- "TTFD 정상" --> M["시작 성능 검증 완료"]
```

---

### 5. 단계별 조사 절차 및 CLI 검증 (Step-by-Step CLI Investigation)

#### 1단계: `am start-activity` (또는 `am start`) 로 TTID 정밀 측정
CLI 실행 시 `-W` (Wait) 옵션을 부여해 시간 측정 결과를 확인한다.
```bash
adb shell am start-activity -W -n com.example.app/.MainActivity
```
*출력 예시:*
```text
Starting: Intent { cmp=com.example.app/.MainActivity }
Status: ok
LaunchState: COLD
Activity: com.example.app/.MainActivity
TotalTime: 842
WaitTime: 845
Complete
```
- `TotalTime`: 시스템이 시작 요청을 수신한 시점부터 첫 프레임 렌der 완료까지의 시간(TTID, ms 단위).
- `LaunchState`: `COLD`, `WARM`, `HOT` 상태를 확인하여 재현 환경이 타당한지 검증.

#### 2단계: Logcat 의 `Displayed` 및 `Fully drawn` 태그 관찰
수동 트리거 외에 실제 앱 실행 로그에서 타임스탬프를 수집한다.
```bash
adb logcat -d | grep -E "ActivityManager: Displayed|Fully drawn"
```
*출력 예시:*
```text
ActivityManager: Displayed com.example.app/.MainActivity: +842ms
system_process I/ActivityManager: Fully drawn com.example.app/.MainActivity: +1s450ms
```
- `Displayed`: TTID 신호. 괄호 안 `(total +2m10s)` 가 표기되면 이전 선행 Activity 나 SplashActivity 가 오래 지연되었음을 의미함.
- `Fully drawn`: 앱 내부에서 `reportFullyDrawn()` 을 호출했을 때 측정되는 TTFD 신호.

#### 3단계: ApplicationExitInfo 를 이용한 실행 직후 종료 원인 조회 (Android 11+ / API 30+)
시작 직후 앱이 소리 없이 튕기거나 죽는 경우 프로세스 종료 원인을 시스템에 쿼리한다.
```bash
adb shell dumpsys activity exit-info com.example.app
```
*핵심 결과 필드:*
- `reason`: `REASON_CRASH_NATIVE`, `REASON_ANR`, `REASON_INITIALIZATION_FAILURE`, `REASON_FREEZER`
- `subreason`: `SUBREASON_UNDEF`, `SUBREASON_IMP_DEF`

#### 4단계: Perfetto Trace 를 통한 메인 스레드 구간별 시간축 타임라인 수집
`Choreographer#doFrame` 이전 구간 중 어느 메인 스레드 콜백이 긴지 측정한다.
```bash
adb shell perfetto -o /data/misc/perfetto-traces/launch.trace -t 5s sched freq idle am wm gfx view
adb pull /data/misc/perfetto-traces/launch.trace .
```
ui.perfetto.dev 에서 트레이스를 열고 `ActivityThread.main` -> `Application.onCreate` -> `Activity.onCreate` 의 duration 을 확인한다.

---

### 6. 성공 / 실패 판정 신호 기준표 (Signal Criteria Matrix)

| 진단 지표 / 신호 (Signal) | 정상 기준 (Success Criteria) | 실패 기준 (Failure Criteria) | 주 원인 및 즉시 조치 (Action Boundary) |
| :--- | :--- | :--- | :--- |
| **am start -W TotalTime (TTID)** | Cold Launch < 1000ms<br>Warm Launch < 500ms | Cold Launch > 2500ms<br>Warm Launch > 1000ms | `Application.onCreate()` 및 DI 그래프 동기 초기화 로직 분산/비동기화 |
| **Fully drawn (TTFD)** | TTID 직후 (< 500ms 이내 차이) | TTID 대비 > 3000ms 이상 지연 또는 미호출 | 첫 프레임 렌더링 후 비동기 데이터 쿼리 파이프라인 전환 ([Worked Example 01](../worked-examples/01-app-icon-tap-to-first-frame.md)) |
| **Logcat Displayed 라인** | 단일 `Displayed` 출력 기록 | 복수의 `Displayed` 유발 또는 `(total ...)` 괄호 지연 존재 | SplashActivity 등 릴레이 액티비티 체인 단축 |
| **Android 15 16KB Page Alignment** | `readelf -l *.so` 커스텀 정렬 통과 | `UnsatisfiedLinkError` 또는 `dlopen failed: alignment...` | NDK/C++ `.so` 빌드 시 `-z max-page-size=16384` 링커 플래그 적용 |
| **ApplicationExitInfo Reason** | N/A (정상 종료 없음) | `REASON_INITIALIZATION_FAILURE`<br>`REASON_CRASH_NATIVE` | 시작 시 Native Crash 로그 및 C++ crash dump 분석 |

---

### 7. OS / API (Android 14 / 15 / 16) 특화 제약 및 진단 신호

- **Android 14 (API 34)**:
  - **시작 시 Foreground Service (FGS) 시작 제약**: `Application.onCreate()` 또는 `Activity.onCreate()` 시점에 백그라운드 상태 판정으로 `Context.startForegroundService()` 호출 시 `ForegroundServiceStartNotAllowedException` 예외가 발생하여 시작 직후 프로세스가 종료될 수 있음.
  - **SplashScreen API 필수화**: 커스텀 테마 기반 스플래시 구현 시 시스템 스플래시 창과의 이중 렌더링으로 TTID 가 왜곡될 수 있으므로 `androidx.core.splashscreen` API 로 통합 필수.
- **Android 15 (API 35)**:
  - **16KB Page Size 지원 의무화**: NDK/C++ 라이브러리를 포함하는 앱은 ELF segment 가 16KB boundary 로 정렬되지 않은 경우 Android 15+ 기기/에뮬레이터에서 앱 프로세스가 시작 도중 즉시 사망함.
    - CLI 확인: `readelf -l libexample.so | grep LOAD` 명령으로 `Align` 값이 `0x4000` (16384) 이상인지 검증.
  - **Edge-to-Edge 기본 적용**: Android 15 target SDK 앱은 Edge-to-edge 가 기본 활성화되어 첫 Activity 의 WindowInset 계산 및 UI layout pass 시간축이 변경될 수 있음.
- **Android 16 (API 36)**:
  - **Advanced Cached Apps Freezer**: 백그라운드 태스크 초기화 후 동결(Freezer) 정책이 강화되어, 시작 시점에 비동기로 띄운 초기화 Coroutine 이 시스템에 의해 동결되어 TTFD 가 기하급수적으로 느려질 수 있음.

---

### 8. 다음 조사 경로 (Next Investigation Paths)

- ANR 다이얼로그 또는 메인 스레드 차단 관찰 시 → [ANR runbook](02-anr.md) 으로 이동.
- TTFD 만 느리고 TTID 는 정상인 경우 → 데이터 로딩 및 도메인/로컬 캐시 계층 문제이므로 [Learning Spine 8장](../learning-spine/08-data-storage-network-and-offline-recovery.md) 확인.
- 특정 기기/제조사에서만 시작 속도 이슈가 몰리는 경우 → Android Vitals 현장 분포 및 OEM 전력 정책 확인 ([Learning Spine 11장](../learning-spine/11-observation-testing-and-quality-feedback.md)).

---

### 9. 관련 자료 및 연결 노트 (Related Notes & Worked Examples)

- [Worked Example: 앱 아이콘 탭에서 첫 프레임까지](../worked-examples/01-app-icon-tap-to-first-frame.md)
- [Android 시작 성능은 TTID와 TTFD로 나눈다](../../06_testing_performance/performance/performance-contracts/startup-performance-is-measured-by-ttid-and-ttfd.md)
- [Profiler, Perfetto, dumpsys는 벤치마크가 아니라 진단 도구다](../../06_testing_performance/performance/performance-contracts/profiler-perfetto-dumpsys-are-diagnosis-tools-not-benchmarks.md)
- [Learning Spine 6장 메인 스레드, Binder, coroutine과 durable scheduler](../learning-spine/06-main-thread-binder-coroutine-and-durable-work-lifetime.md)
- [Learning Spine 8장 데이터 저장소, 네트워크와 offline recovery](../learning-spine/08-data-storage-network-and-offline-recovery.md)
- [Learning Spine 11장 관찰, 테스트와 품질 feedback](../learning-spine/11-observation-testing-and-quality-feedback.md)

---

### 10. 공식 근거 (Official References)

- [App startup time (Android Developers)](https://developer.android.com/topic/performance/vitals/launch-time)
- [Support 16 KB page sizes (Android Developers)](https://developer.android.com/guide/practices/page-sizes)
- [Diagnose ANRs (Android Developers)](https://developer.android.com/topic/performance/vitals/anr)

검증일: 2026-08-04. `Displayed` 로그 형식, `am start-activity -W` 사용법, Android 15 16KB Page Alignment 요구사항 및 ApplicationExitInfo API 쿼리는 공식 문서와 실기기 진단 CLI 로 검증 완료함.
