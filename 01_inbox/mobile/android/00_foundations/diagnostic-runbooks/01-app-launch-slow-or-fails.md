---
title: 01-app-launch-slow-or-fails
tags: ["android", "android/foundations", "diagnostic-runbook"]
aliases: ["Runbook: app launch is slow or fails"]
date modified: 2026-08-04 10:28:24 +09:00
date created: 2026-08-04 10:30:00 +09:00
---

## 앱 실행이 느리거나 첫 프레임이 뜨지 않는다

### 증상

다음 중 하나 이상이 관찰된다.

- 앱 아이콘을 탭한 뒤 첫 화면이 뜨기까지 체감상 오래 걸린다.
- 첫 화면(첫 프레임)은 빨리 뜨지만 콘텐츠가 없는 빈 화면이 오래 유지된다.
- 실행 중 ANR 다이얼로그가 뜨거나 실행 자체가 실패한다(이 경우 [ANR runbook](02-anr.md) 으로 넘어간다).

### 재현 조건

- **냉시작인지 온시작인지 먼저 구분한다.** 냉시작은 프로세스가 없는 상태에서 시작하는 경우다. `adb shell am force-stop <pkg>` 뒤 실행하면 냉시작을, 홈 버튼으로 백그라운드로 보낸 뒤 다시 열면 그보다 가벼운 경로를 재현한다.
- 기기 모델, OS 버전, 빌드 타입(반드시 release 와 유사한 빌드 — debug 빌드의 로그·검증 코드는 시작 비용을 왜곡한다), 배터리 잔량과 열 상태를 고정하고 여러 번 반복해 중앙값을 본다.

### 가능한 실패 경계와 우선순위

1. **`Application.onCreate()` 또는 첫 Activity 의 `onCreate()` 가 무겁다.** 가장 흔한 원인. DI 그래프 생성, 로깅/원격설정/SDK 초기화가 대표적이다.
2. **TTID 는 양호한데 TTFD 가 늦다.** 첫 프레임은 빠르지만 실제 콘텐츠(목록 데이터 등)가 나중에 채워진다 — 데이터 계층 지연 문제([데이터 계층 Worked Example](../worked-examples/01-app-icon-tap-to-first-frame.md) 참고).
3. **프로세스 생성 자체가 느리다.** 기기 전반의 메모리 압박이나 시스템 부하로 Zygote fork·specialization 이 지연되는 경우로, 이 앱만의 문제가 아닐 수 있다.
4. **main thread 가 완전히 막혀 첫 프레임조차 안 뜬다.** [ANR runbook](02-anr.md) 으로 넘어간다.

### 조사 절차

1. **`adb shell am start -W -n <pkg>/<activity>` 로 TTID 를 측정한다.**
   출력의 `TotalTime`(ms)이 핵심 필드다. 이 값은 요청이 시스템에 전달된 시점부터 첫 프레임이 그려질 때까지의 시간이다.
   - 정상 신호: 빌드/기기 기준으로 일관된 낮은 값(수백 ms 대).
   - 실패 신호: 값이 크거나, 명령이 오래 대기하다 `ANR` 메시지와 함께 끝난다.

2. **logcat 에서 `Displayed` 라인을 확인한다.**
   ```
   ActivityManager: Displayed com.example.app/.MainActivity: +3s534ms
   ```

   이 값이 위 `TotalTime` 과 같은 구간(TTID)을 가리킨다. `(total +1m22s643ms)` 처럼 괄호 안에 total 값이 추가로 나오면, 이는 앱 프로세스 시작부터 걸린 전체 시간이며 화면에 아무것도 표시하지 않는 선행 Activity 가 있었다는 뜻일 수 있다.

   - 왜 이 필드를 보는가: `am start -W` 는 개발자가 수동으로 트리거한 한 번의 측정이지만, `Displayed` 로그는 실제 사용자 실행에서도 남으므로 현장 재현에 쓸 수 있다.

3. **`reportFullyDrawn()` 호출 시점을 확인해 TTFD 를 분리한다.**
   TTID(첫 프레임)와 TTFD(콘텐츠가 실제로 준비된 시점)는 시스템이 자동으로 구분하지 못한다. 앱이 `reportFullyDrawn()` 을 호출하지 않으면 TTFD 자체가 측정되지 않는다.
   - 정상 신호: `reportFullyDrawn()` 호출 시점이 TTID 직후에 가깝다.
   - 실패 신호: TTID 이후 한참 지나서야 호출되거나, 아예 호출되지 않는다 — 데이터 로딩이 콘텐츠 표시를 늦추고 있다는 뜻이다.

4. **Perfetto trace 로 시작 구간의 시간축을 본다.**
   `Choreographer#doFrame` 이전의 `ActivityThread.main` → `Application.onCreate` → `Activity.onCreate` 구간 중 어디가 가장 긴지 확인한다.
   - 왜 이 필드를 보는가: `am start -W` 의 `TotalTime` 은 "얼마나 걸렸는지"만 말해주고 "어디서 걸렸는지"는 말해주지 않는다. trace 의 구간별 길이가 그다음 조사 방향(초기화 코드 축소 vs 데이터 로딩 지연 vs 레이아웃 비용)을 정한다.

5. **`dumpsys activity activities` 로 현재 최상단 액티비티와 프로세스 상태를 확인한다.**
   같은 컴포넌트를 실행하는 요청이라도 대상 프로세스가 foreground/visible 상태로 살아 있었는지, 메모리 압박으로 회수된 cached 상태였는지에 따라 체감 지연이 달라진다. 이 출력으로 재현이 정말 냉시작이었는지 확인할 수 있다.

### OS/API/target SDK 조건

- `TotalTime`/`Displayed` 로그는 API 레벨과 무관하게 안정적으로 존재하는 오래된 진단 신호다.
- `reportFullyDrawn()` 은 모든 API 레벨에서 사용 가능하지만, TTFD 측정 자체는 앱이 명시적으로 호출해야만 의미를 갖는다는 점은 버전과 무관하게 동일하다.
- Baseline Profile 적용 여부는 특히 냉시작 비용에 영향을 준다. 최근에 이 문제가 새로 생겼다면 Baseline Profile 관련 빌드 변경이 있었는지 확인한다.

### 다음 조사 경로

- ANR 다이얼로그가 관찰되면 → [ANR runbook](02-anr.md)
- TTFD 만 늦고 TTID 는 정상이면 → 데이터 계층 문제이므로 [Learning Spine 8장](../learning-spine/08-data-storage-network-and-offline-recovery.md) 의 로컬 우선 관찰 모델을 확인
- 특정 기기·OS 버전군에서만 느리다면 → [관찰/테스트 runbook 방법론](../learning-spine/11-observation-testing-and-quality-feedback.md) 의 Android vitals 현장 분포 확인으로 넘어간다

### 관련 자료

- [Worked Example: 앱 아이콘 탭에서 첫 프레임까지](../worked-examples/01-app-icon-tap-to-first-frame.md)
- [Android 시작 성능은 TTID와 TTFD로 나눈다](../../06_testing_performance/performance/performance-contracts/startup-performance-is-measured-by-ttid-and-ttfd.md)
- [Profiler, Perfetto, dumpsys는 벤치마크가 아니라 진단 도구다](../../06_testing_performance/performance/performance-contracts/profiler-perfetto-dumpsys-are-diagnosis-tools-not-benchmarks.md)
- [Learning Spine 6장 메인 스레드, Binder, coroutine과 durable scheduler](../learning-spine/06-main-thread-binder-coroutine-and-durable-work-lifetime.md)
- [Learning Spine 11장 관찰, 테스트와 품질 feedback](../learning-spine/11-observation-testing-and-quality-feedback.md)

### 공식 근거

- [App startup time](https://developer.android.com/topic/performance/vitals/launch-time)
- [Diagnose ANRs](https://developer.android.com/topic/performance/vitals/anr)

검증일: 2026-08-04. `Displayed` 로그 형식과 `am start -W` 사용법은 공식 문서 원문으로 확인했다.
