---
title: ANR(Application Not Responding)이 발생한다
tags: ["android", "android/foundations", "diagnostic-runbook"]
aliases: ["Runbook: ANR"]
date modified: 2026-08-04 10:35:00 +09:00
date created: 2026-08-04 10:35:00 +09:00
---

## ANR(Application Not Responding)이 발생한다

### 증상

사용자에게 "앱이 응답하지 않습니다" 다이얼로그가 뜨거나, Play Console/Android vitals에서 ANR율이 상승했다는 리포트를 받는다.

### 재현 조건

- 어떤 사용자 동작 직후에 ANR이 뜨는지 특정한다(앱 실행 직후, 특정 화면 진입, 특정 버튼 탭, 백그라운드 브로드캐스트 수신 등). ANR은 원인이 다양하므로 "언제" 발생했는지가 조사 방향을 절반쯤 정한다.
- 같은 빌드·기기·시나리오로 반복 재현을 시도한다. 간헐적이라면 [process death runbook](03-process-death-state-loss.md)의 재현 도구(디버거가 타이밍을 바꿀 수 있다는 점)도 함께 고려한다.

### 가능한 실패 경계와 우선순위

공식 문서는 ANR이 발생하는 조건을 다섯 가지로 명시한다.

> "Input dispatching timed out: If your app has not responded to an input event (such as key press or screen touch) within 5 seconds."
>
> "Executing service: If a service declared by your app cannot finish executing Service.onCreate() and Service.onStartCommand()/Service.onBind() within a few seconds."
>
> "Service.startForeground() not called: If your app uses Context.startForegroundService() to start a new service in the foreground, but the service then does not call startForeground() within 5 seconds."
>
> "Broadcast of intent: If a BroadcastReceiver hasn't finished executing within a set amount of time. If the app has any activity in the foreground, this timeout is 5 seconds."
>
> "JobScheduler interactions: If a JobService does not return from JobService.onStartJob() or JobService.onStopJob() within a few seconds..."

가장 흔한 순서로 의심한다.

1. **Input dispatching timeout(5초)** — 화면이 보이는 상태에서 main thread가 막혀 터치/키 입력에 응답하지 못한 경우. 가장 흔하다.
2. **Broadcast timeout** — `BroadcastReceiver.onReceive()`가 무거운 작업을 동기로 수행하는 경우.
3. **Service 관련 timeout** — `onCreate()`/`onStartCommand()`/`onBind()`가 오래 걸리거나, foreground service가 `startForeground()`를 제때 호출하지 않은 경우.
4. **JobScheduler 관련 timeout** — `JobService`의 콜백이 제때 반환되지 않은 경우.

### 조사 절차

1. **ANR trace 파일을 확보한다.**
   ```bash
   adb root
   adb shell ls /data/anr
   adb pull /data/anr/<filename>
   ```
   구버전 OS는 `/data/anr/traces.txt` 단일 파일에, 최신 OS는 `/data/anr/anr_*` 여러 파일에 남는다.
   - 왜 이 파일을 보는가: logcat만으로는 ANR 발생 사실만 알 수 있고, 실제로 main thread가 무엇을 하고 있었는지(스택 트레이스)는 이 trace 파일에만 있다.

2. **logcat에서 ANR 키워드로 발생 시점과 대상 컴포넌트를 먼저 특정한다.**
   ```bash
   adb logcat | grep ANR
   ```
   여기서 어떤 컴포넌트(Activity/Service/Receiver)가 관련됐는지, 위 5가지 트리거 중 어느 것에 해당하는지 단서를 얻는다.

3. **trace 파일에서 main thread의 스택을 읽는다.**
   `"main"` 스레드 스택 상단에서 지금 무엇을 실행 중이었는지 확인한다.
   - main thread가 CPU를 쓰고 있었다면(BLOCKED가 아닌 RUNNABLE): 무거운 연산이나 반복문을 의심한다.
   - lock을 기다리고 있었다면(`waiting to lock`): 어느 스레드가 그 lock을 쥐고 있는지 다른 스레드 스택에서 찾는다(데드락/경합).
   - Binder 응답을 기다리고 있었다면: 원격 서비스나 다른 프로세스의 지연 문제로 조사 범위를 옮긴다.
   - I/O(디스크·네트워크)를 기다리고 있었다면: main thread에서 동기 I/O를 호출한 코드를 찾는다.

4. **Perfetto trace와 함께 본다(가능하면).**
   trace 파일의 스택은 ANR 시점의 스냅샷 하나뿐이다. Perfetto로 그 직전 구간의 시간축을 함께 보면 "얼마나 오래" 막혀 있었는지, 반복적으로 짧은 구간이 쌓여 5초를 넘긴 것인지 한 번에 오래 걸린 것인지 구분할 수 있다.

5. **디버거로 재현을 시도할 때는 결과를 단독 증거로 삼지 않는다.**
   디버거가 연결되면 스레드 타이밍이 바뀌어 race 조건이나 lock 경합이 사라질 수 있다. trace/logcat 같은 실행 타이밍을 바꾸지 않는 수단과 교차 확인한다.

### OS/API/target SDK 조건

- `/data/anr/anr_*` 다중 파일 구조와 `/data/anr/traces.txt` 단일 파일 구조는 OS 버전에 따라 다르므로, 대상 기기의 OS 버전에 맞는 경로부터 확인한다.
- foreground service의 `startForeground()` 타임아웃은 Android 버전과 대상 SDK에 따라 조건이 달라질 수 있으므로, 이 유형이 의심되면 대상 API 레벨의 공식 behavior changes 문서를 함께 확인한다.

### 다음 조사 경로

- main thread가 Binder 응답을 기다리고 있었다면 → 시스템 서비스 호출 지연이므로 [Learning Spine 6장](../learning-spine/06-main-thread-binder-coroutine-and-durable-work-lifetime.md)의 Binder thread pool 모델 확인
- 냉시작 직후 ANR이라면 → [app launch runbook](01-app-launch-slow-or-fails.md)
- 특정 브로드캐스트나 백그라운드 작업이 원인이라면 → [background delay runbook](05-background-work-delayed-or-not-running.md)

### 관련 자료

- [ANR은 단일 timeout이 아니라 responsiveness 계약 위반이다](../../01_system_internals/boot-and-runtime/system-server-contracts/anr-is-responsiveness-contract-violation-not-single-timeout.md)
- [Binder thread pool은 service concurrency와 deadlock 경계다](../../01_system_internals/ipc-and-process/ipc-process-contracts/binder-thread-pool-is-service-concurrency-and-deadlock-boundary.md)
- [Logcat, crash, ANR, debugger는 서로 다른 질문에 답한다](../../06_testing_performance/debugging/debugging-contracts/logcat-crash-anr-and-debugger-answer-different-questions.md)
- [Worked Example: 앱 아이콘 탭에서 첫 프레임까지](../worked-examples/01-app-icon-tap-to-first-frame.md)
- [Learning Spine 6장 메인 스레드, Binder, coroutine과 durable scheduler](../learning-spine/06-main-thread-binder-coroutine-and-durable-work-lifetime.md)

### 공식 근거

- [Diagnose ANRs](https://developer.android.com/topic/performance/vitals/anr)

검증일: 2026-08-04. ANR 트리거 5가지와 trace 파일 경로는 공식 문서 원문으로 확인했다. 세부 timeout 값은 Android 버전과 foreground/background 조건에 따라 달라질 수 있으므로 하나의 고정 숫자로 외우지 않는다.
