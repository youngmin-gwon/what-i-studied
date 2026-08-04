---
title: 앱 아이콘 탭에서 첫 프레임까지
tags: ["android", "android/foundations", "worked-example"]
aliases: ["App icon tap to first frame"]
date modified: 2026-08-04 02:10:00 +09:00
date created: 2026-08-04 02:10:00 +09:00
---

## 앱 아이콘 탭에서 첫 프레임까지

이 예시는 Learning Spine 3·4·5·6·7·11장을 하나의 요청으로 잇는다. 컴포넌트 registry와 identity(3·4장), 프로세스 상태 확인과 Zygote(4장), Activity lifecycle과 main thread(5·6장), 입력에서 프레임까지의 렌더링 경로(7장), 그리고 이 전체 구간을 관찰하는 방법(11장)을 하나의 서사로 연결한다.

### 시작 상태

기기는 켜져 있고, 이 앱은 설치돼 있지만 지금은 실행 중이지 않다. 최근에 이 앱을 연 적이 없어 프로세스가 없거나, 시스템이 메모리 확보를 위해 이미 회수했다(냉시작). 공식 문서는 냉시작을 이렇게 정의한다.

> "A cold start refers to an app's starting from scratch. This means that until this start, the system's process creates the app's process."

### 입력

사용자가 홈 화면(런처)에서 이 앱의 아이콘을 탭한다.

### 단계별 흐름

1. **요청**: 런처는 이 아이콘이 어떤 컴포넌트로 이어지는지 이미 알고 있다. 설치 시 PackageManager가 매니페스트의 `<intent-filter>`(`action=MAIN`, `category=LAUNCHER`)를 컴포넌트 registry에 등록해뒀고, 런처는 이 registry를 조회해 아이콘-컴포넌트 매핑을 만들었기 때문이다. 탭은 이 특정 컴포넌트를 향한 사실상 명시적인 실행 요청으로 시스템에 전달된다.
2. **Identity**: 시스템이 실행할 코드는 이 패키지의 서명·숫자 appId·UID로 식별된 실행 단위다. 이 identity는 3장에서 다룬 설치 시점의 검증·등록 결과다.
3. **프로세스 상태 확인**: system_server의 ActivityManagerService(AMS)는 이 UID의 프로세스가 이미 살아 있는지 확인한다. 냉시작이므로 없다. AMS는 Zygote socket에 fork를 요청하고, Zygote는 새 프로세스의 UID/GID, 프로세스 이름 같은 specialization을 마친다.
4. **프로세스 attach**: specialization이 끝난 프로세스는 `ActivityThread.main()` 경로로 framework에 attach한다. 이 시점부터 `Application.onCreate()`가 실행된다. DI 그래프 생성, 로깅 초기화, 원격 설정 로드, SDK 초기화가 이 구간을 늘릴 수 있는 대표적인 지점이다.
5. **컴포넌트 생성과 lifecycle**: 대상 Activity 인스턴스가 이 프로세스 안에서 생성되고 `onCreate → onStart → onResume` 콜백이 main thread에서 순서대로 실행된다. main thread는 이 프로세스의 유일한 이벤트 큐이므로, 이 콜백들이 오래 걸리면 이후 모든 이벤트(입력, 그리기)가 함께 지연된다.
6. **Window 연결**: Activity의 `ViewRootImpl`이 WindowManagerService에 윈도우 정보를 알리고, View 또는 Compose 트리가 이 윈도우 크기에 맞춰 measure/layout을 수행한다.
7. **첫 프레임 합성**: 그려진 내용은 RenderThread를 거쳐 Surface 버퍼로 제출되고, SurfaceFlinger가 이를 다른 레이어와 합성해 화면에 표시한다.

### 성공 결과

사용자는 화면에 첫 프레임을 본다. 이 시점이 TTID(Time To Initial Display)다. 그러나 화면에 실제로 의미 있는 콘텐츠(예: 목록 데이터)가 채워지는 시점(TTFD, Time To Full Display)은 이보다 늦을 수 있다. 공식 문서는 이 차이를 이렇게 설명한다.

> "Although the system can determine TTID when the host window renders its initial frame, it can't automatically determine TTFD. Because apps often load their primary content asynchronously, the system doesn't know when the app is actually fully usable to the user."

그래서 TTFD는 시스템이 자동으로 감지하지 못하며, 앱이 직접 신호를 보내야 한다.

> "To find TTFD, signal the fully drawn state by calling the reportFullyDrawn method of the ComponentActivity. ... The TTFD is the time elapsed from when the system receives the app launch intent to when reportFullyDrawn is called."

### 관찰 가능한 신호

- `adb shell am start -W`의 출력은 `Starting: Intent`, `Activity`, `TotalTime`, `WaitTime`, `Complete`를 보여주며 시작 요청부터 첫 프레임까지의 시간을 담는다.
- 앱이 `reportFullyDrawn()`을 호출하는 시점이 TTFD를 시스템에 알린다. 이 호출이 없으면 TTFD는 측정되지 않는다.
- Perfetto trace에서 `ActivityThread.main` → `Application.onCreate` → `Activity.onCreate` → `Choreographer#doFrame`까지의 구간을 같은 시간축에서 볼 수 있다.
- Macrobenchmark의 `StartupTimingMetric`으로 냉시작을 반복 측정해 회귀를 판정할 수 있다.

### 실패 분기: 냉시작 중 ANR로 첫 프레임 자체가 나타나지 않는다

`Application.onCreate()`나 첫 Activity의 `onCreate()`에서 동기 네트워크 호출이나 큰 디스크 I/O를 수행하면, 이 프로세스의 유일한 이벤트 큐인 main thread가 막힌다. 사용자는 첫 프레임조차 보지 못하고 입력 디스패치 타임아웃을 넘겨 ANR 다이얼로그를 만난다.

조사 순서는 ANR trace에서 main thread가 무엇을 하고 있었는지 먼저 보는 것이다. CPU를 계속 쓰고 있었는지(무거운 초기화 연산), 아니면 lock, 디스크, 네트워크 응답을 기다리며 멈춰 있었는지에 따라 원인과 처방이 다르다. 이 진단 순서 자체는 "느린 코드 한 줄"보다 "main thread가 그 순간 무엇을 기다리게 됐는가"를 먼저 묻는 방법론이다.

### 코드 예시

```kotlin
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // 나쁜 예: 첫 프레임을 지연시키는 동기 초기화. main thread를 막아
        // ANR 위험을 만든다.
        // val config = fetchRemoteConfigSync()

        // 나은 예: 첫 프레임에 필요하지 않은 초기화는 별도 dispatcher로 옮긴다.
        applicationScope.launch(Dispatchers.IO) {
            initAnalyticsSdk()
        }
    }
}

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { AppRoot() }

        lifecycleScope.launch {
            viewModel.primaryContentReady.first { it }
            reportFullyDrawn() // 실제 콘텐츠가 준비된 시점을 TTFD로 알린다.
        }
    }
}
```

### 관련 원자 노트

- [AndroidManifest.xml은 OS에 앱의 컴포넌트를 선언한다](../../02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/android-manifest-declares-os-visible-components-and-entry-points.md)
- [action, category, data 매칭은 서로 다른 조건이다](../../02_app_framework/navigation/intents-and-deep-links/intent-manifest-contracts/intent-filter-matches-action-category-data.md)
- [AMS는 앱 프로세스와 컴포넌트 lifecycle을 조율한다](../../01_system_internals/boot-and-runtime/system-server-contracts/ams-coordinates-app-process-and-component-lifecycle.md)
- [Zygote socket은 system_server가 앱 프로세스를 요청하는 factory interface다](../../01_system_internals/boot-and-runtime/zygote-runtime-contracts/zygote-socket-is-system-server-process-factory-interface.md)
- [앱 프로세스는 specialization 뒤 ActivityThread로 framework에 attach한다](../../01_system_internals/boot-and-runtime/zygote-runtime-contracts/app-process-specializes-before-activitythread-attaches-to-framework.md)
- [Activity 콜백은 화면 인스턴스의 visibility와 interaction 경계를 알린다](../../02_app_framework/architecture/app-components/app-component-contracts/activity-lifecycle-callbacks-describe-visibility-and-interaction-boundaries.md)
- [Android 렌더링 파이프라인은 Surface 버퍼를 합성기로 넘기는 계약이다](../../01_system_internals/graphics-and-media/graphics-media-contracts/android-rendering-pipeline-is-surface-to-bufferqueue-to-compositor.md)
- [ANR은 단일 timeout이 아니라 responsiveness 계약 위반이다](../../01_system_internals/boot-and-runtime/system-server-contracts/anr-is-responsiveness-contract-violation-not-single-timeout.md)
- [Android 시작 성능은 TTID와 TTFD로 나눈다](../../06_testing_performance/performance/performance-contracts/startup-performance-is-measured-by-ttid-and-ttfd.md)

### 관련 Learning Spine 장

- [4장 매니페스트에서 컴포넌트 실행까지](../learning-spine/04-manifest-to-component-execution.md)
- [5장 화면, 프로세스, task와 사용자 상태는 독립적인 lifetime을 가진다](../learning-spine/05-independent-lifetimes-of-screen-process-task-and-state.md)
- [6장 메인 스레드, Binder, coroutine과 durable scheduler는 서로 다른 실행 책임을 진다](../learning-spine/06-main-thread-binder-coroutine-and-durable-work-lifetime.md)
- [7장 입력, 리소스 선택과 화면 프레임](../learning-spine/07-input-resource-selection-and-display-frame.md)

### 공식 근거

- [App startup time](https://developer.android.com/topic/performance/vitals/launch-time)
- [Diagnose ANRs](https://developer.android.com/topic/performance/vitals/anr)
- [Macrobenchmark overview](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)

검증일: 2026-08-04. 냉시작/온시작 정의, `reportFullyDrawn()`, `am start -W` 출력 필드는 공식 문서 원문으로 확인했다.
