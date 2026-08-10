---
title: 11-observation-testing-and-quality-feedback
tags: ["android", "android/foundations", "learning-spine"]
aliases: ["Observation, testing, and quality feedback"]
date modified: 2026-08-10 00:00:00 +09:00
date created: 2026-08-03 23:55:00 +09:00
---

## 관찰, 테스트와 품질 **피드백**(feedback, 사용자 또는 시스템이 제공하는 개선 신호)

1 장부터 10 장까지, 이 Learning Spine 은 여러 장에 걸쳐 `dumpsys`, Perfetto, logcat, `WorkInfo`, `canAuthenticate()` 의 오류 코드 같은 도구를 진단 방법으로 언급했다. 그러나 이 도구들이 서로 어떤 종류의 증거를 제공하는지, 그리고 그 증거가 테스트와 릴리스 이후 현장 피드백으로 어떻게 이어지는지는 하나로 묶어 다루지 않았다. 이 장은 그 방법론을 다룬다.

이 장의 핵심 질문은 다음과 같다.

>보이지 않는 Android 상태를 어떤 증거로 확인하며, 재현에서 로그·상태·**trace**(시간축 기반 이벤트 기록), 테스트·벤치마크, 릴리스 이후 현장 피드백까지는 어떻게 하나의 순환으로 이어지는가?

이 장은 각 도구의 명령어 옵션을 처음부터 가르치지 않는다. 개별 도구의 상세 사용법은 `06_testing_performance` 의 원자 노트가 다루는 수준으로 남겨두고, 여기서는 지금까지의 장들이 흩어놓은 진단 도구 언급을 하나의 순환 모델로 연결한다.

### 1. 테스트와 진단 도구는 다른 질문에 답한다

테스트는 문제가 다시 발생하는지 확인하고, 진단 도구는 왜 발생했는지 좁힌다. 이 둘을 같은 목적으로 쓰면 로그를 과도하게 남기거나 재현 절차 자체를 놓치게 된다.

재현 가능한 문제는 조건을 고정해 여러 번 다시 만들 수 있다. 빌드 타입과 앱 버전, 기기 모델과 OS 버전, 배터리 잔량과 열 상태, 냉시작/온시작 여부를 고정하고 여러 번 반복해 중앙값과 분산을 함께 봐야 한다. 재현하기 어려운 문제(특정 기기, 특정 계정, 특정 시점에서만 나타나는 문제)는 다른 접근이 필요하다. 이런 문제는 개발자 기기에서 재현되지 않을 수 있으므로, 뒤에서 다룰 현장 피드백(Android vitals)과 함께 봐야 한다.

### 2. 로그, 상태, trace 는 서로 다른 질문에 답한다

지금까지 여러 장에서 언급한 도구들은 각각 다른 질문에 답한다.

- **Logcat**은 시간 순서로 사건을 수집하는 1 차 관찰 도구다. 재현 전에 관련 tag 만 필터링하고, 로그만 보고 원인을 단정하지 않는다.
- **Crash**는 예외 타입과 메시지, 앱 코드의 첫 stack frame 을 읽는 것에서 시작한다. release 빌드라면 3 장에서 다룬 R8 축소·난독화 때문에 동일 버전의 mapping 으로 stack trace 를 복원해야 한다.
- **ANR**은 main thread trace 에서 block, lock, disk, network, 긴 계산을 찾는 문제다. 이는 6 장에서 다룬 "main thread 는 유일한 이벤트 큐"라는 사실과 9 장의 gate 들이 실제로 무엇을 기다리게 만들었는지가 만나는 지점이다.
- **Debugger**는 특정 입력에서 변수와 호출 순서를 볼 때 쓴다. 다만 디버거가 연결되면 timing 이 바뀌어 race 나 ANR 이 사라질 수 있으므로, 디버거 결과만 단독 증거로 삼지 않고 로그·trace 와 교차 확인해야 한다.
- **Profiler**는 CPU/메모리/네트워크/에너지를 탐색하는 도구다.
- **Perfetto**는 앱과 시스템을 같은 시간축에서 본다. 7 장에서 다룬 스케줄링, main thread, 프레임, Binder, 전원 이벤트의 관계를 확인할 때 기준이 된다.
- **`dumpsys`**는 시스템 서비스가 보고하는 현재 상태의 스냅샷이다. 2·4·8·9 장에서 각각 `dumpsys location`, `dumpsys activity`, `dumpsys jobscheduler`, `dumpsys appops` 로 이미 등장했다. 스냅샷은 원인을 직접 설명하지 않으므로 시간축 trace 와 함께 해석해야 한다.
- **Macrobenchmark**는 시작과 스크롤 같은 사용자 여정을 반복해 수치화하는 회귀 판정 도구다.

이 구분을 압축하면 다음과 같다. 질문이 "어디서 시간이 걸렸나"라면 Profiler 나 Perfetto 를, "현재 상태가 어떤가"라면 `dumpsys` 를, "다음 릴리스에서 나빠졌나"라면 Macrobenchmark 를 먼저 선택한다.

### 3. 이 도구들은 지금까지의 장에서 이미 각자의 자리를 갖고 있었다

이 장이 새로 하는 일은 개별 도구를 소개하는 것이 아니라, 지금까지 흩어져 있던 사용을 하나의 표로 되짚는 것이다.

| 장 | 등장한 진단 신호 | 답한 질문 |
| --- | --- | --- |
| 2 장 | `dumpsys location`, `dumpsys sensorservice` | system_server 쪽 서비스가 실제로 어떤 상태인가 |
| 4 장 | "Permission Denial" 로그, `adb shell am start` | 컴포넌트 실행이 registry/Intent/exported 중 어디서 끊겼는가 |
| 6 장 | Perfetto 의 main thread/Binder 구간 | main thread 가 CPU 를 썼는가, 무엇을 기다렸는가 |
| 8 장 | `WorkInfo.state`, `dumpsys jobscheduler` | 동기화 작업이 실제로 예약·실행됐는가 |
| 9 장 | `dumpsys appops`, `dumpsys package` | permission 과 AppOps 상태가 각각 무엇인가 |
| 10 장 | `canAuthenticate()` 류의 사전 확인 반환값 | capability 부재, 미등록, 거부 중 무엇인가 |

이 표가 보여주는 것은, 이 Learning Spine 이 설명한 각 장의 모델이 모두 "관찰 가능한 신호"를 하나씩 갖고 있었다는 것이다. 이 장은 그 신호들을 개별로 외우는 대신 이 방법론으로 묶어 다시 꺼내 쓸 수 있게 한다.

### 4. 테스트 레이어는 유행이 아니라 피드백 비용으로 고른다

테스트 레이어의 선택 기준은 종류의 유행이 아니라 피드백 비용, 즉 실행 시간·실패 재현성·원인 파악 난이도·유지보수 비용을 합친 값이다.

- **Unit**: 하나의 규칙이나 변환을 격리해 검증한다. 시간, 난수, dispatcher, 네트워크, 저장소는 주입 가능한 인터페이스로 둔다.
- **Integration**: 둘 이상의 실제 구성요소가 계약대로 연결되는지 확인한다(예: Repository 와 database).
- **UI**: 사용자에게 보이는 상태와 상호작용을 검증한다.
- **E2E**: navigation, 권한, 앱 재시작처럼 낮은 레이어가 재현하기 어려운 문제를 다룬다.

결정 규칙은 단순하다. 실패가 순수 Kotlin 만으로 재현되면 단위 테스트로 내리고, Android lifecycle 이나 실제 저장소가 필요하면 계측·통합 테스트로 올리고, 실제 창·권한·백그라운드 프로세스가 포함되면 기기 기반 테스트가 필요하다. 모든 분기를 E2E 로 만들면 실패 원인과 실행 시간이 함께 커진다.

### 5. Profiler 는 탐색 도구이고 Macrobenchmark 는 회귀 판정 도구다

이 둘을 같은 용도로 쓰면 안 된다. 프로파일러를 켠 상태의 수치는 오버헤드가 있을 수 있으므로 방향을 찾는 증거로만 쓰고, 최종 회귀 판정은 동일한 릴리스 조건에서 Macrobenchmark 로 다시 측정한다. "코드를 바꿨다"는 사실이 아니라 사용자 지표의 변화가 개선을 판정하는 기준이다.

### 6. 회귀와 **flaky**(간헐적으로 실패) 테스트는 **릴리스 게이트**(release gate, 새 버전 배포를 승인하는 기준) 자체의 신뢰도 문제다

회귀 방지는 테스트를 많이 만드는 일이 아니라 신뢰할 수 있는 신호를 유지하는 일이다. 같은 코드와 환경에서 성공과 실패가 번갈아 나타나는 flaky test 를 방치하면, 팀은 결국 실패를 무시하기 시작하고 안전망 자체가 사라진다. flaky test 는 소유자와 재현 정보를 남기고 격리하되 만료일과 복구 조건을 함께 둬야 하며, 계속 실패하는 테스트를 무기한 제외하면 진짜 회귀가 조용히 통과한다.

### 7. 릴리스 이후에는 테스트 트랙과 단계적 출시가 관찰을 이어간다

테스트가 통과했다는 사실은 실제 사용자 기기에서의 동작까지 보장하지 않는다. Google Play 의 내부 테스트, 비공개 테스트, 공개 테스트는 배포 대상과 피드백 범위가 다른 트랙이며, 권장 흐름은 내부 → 소규모 비공개 → 필요 시 공개 → production 순이다.

기존 앱의 업데이트는 단계적 출시로 작은 비율의 사용자에게 먼저 제공하고, 충돌률·ANR·핵심 기능 오류·배터리·네트워크 지표를 관찰한 뒤에만 대상 비율을 수동으로 늘린다. 문제를 발견하면 rollout 을 중지해 아직 받지 않은 사용자에게 확산을 막을 수 있지만, 이미 받은 사용자는 자동으로 이전 버전으로 돌아가지 않는다.

### 8. Android vitals 는 개발자 기기에서 재현되지 않는 문제를 현장 분포로 보완한다

공식 문서는 이 데이터의 성격을 이렇게 설명한다.

>"When a user allows it, their Android-powered device tracks app quality metrics such as stability, performance, battery use, and permission issues. Google Play collects this data, which can be accessed through the Android vitals dashboard in the Play Console."
>
>"Sometimes, device hardware or software problems cause high error rates. Android vitals alerts you to possible links between high error rates and things like RAM, Android version, and processor type."

이 신호가 중요한 이유는, 지금까지의 장에서 다룬 여러 조건(9 장의 AppOps 자동 회수, 10 장의 OEM 구현 차이, 5 장의 process death 빈도)이 특정 기기·특정 OS 버전·특정 제조사에서만 다르게 나타날 수 있기 때문이다. 개발자의 테스트 기기 몇 대로는 이 분포를 재현할 수 없다. Android vitals 는 사용자 인지 충돌률(user-perceived crash rate), 사용자 인지 ANR 비율, 과도한 partial wake lock 같은 core vitals 를 통해 이 분포를 보여준다.

### 하나의 순환으로 정리한다

`재현 조건 고정 → 로그/crash/ANR/debugger/Perfetto/dumpsys로 원인 좁히기 → 가설을 재현 가능한 테스트로 전환 → 적절한 테스트 레이어에서 회귀 방지 → Macrobenchmark로 회귀 여부 수치화 → 테스트 트랙에서 사전 검증 → 단계적 출시로 관찰하며 확대 → Android vitals로 현장 분포 확인 → 이상 발견 시 다시 재현 조건 고정`

이 순환에서 어느 한 단계를 건너뛰면 문제가 생긴다. 진단 없이 테스트만 추가하면 원인을 모른 채 증상만 고정하게 되고, 현장 피드백 없이 테스트만 신뢰하면 특정 기기·버전에서만 나타나는 문제를 놓친다.

### Worked example: 특정 기기에서만 앱 시작이 느리다는 현장 리포트

1. Android vitals 에서 특정 기기 모델·OS 버전군에서만 시작 시간이 나쁘다는 분포를 확인한다.
2. 팀의 개발 기기에서는 재현되지 않으므로, 유사한 사양의 실기기를 확보하거나 재현 조건(냉시작, 배터리 상태, 열 상태)을 최대한 맞춘다.
3. Perfetto 로 시작 구간의 시간축을 보고, main thread 가 CPU 를 쓰고 있었는지 아니면 무언가(디스크, Binder, lock)를 기다리고 있었는지 구분한다.
4. 원인을 특정 초기화 코드로 좁히면, 그 코드를 재현 가능한 가설로 바꾸고 해당 조건을 고정한 Macrobenchmark 테스트를 추가한다.
5. 수정 후 같은 조건에서 다시 측정해 회귀가 해소됐는지 수치로 확인한다.
6. 내부 테스트 → 비공개 테스트를 거쳐 단계적 출시로 배포하고, 확대하면서 Android vitals 의 해당 지표가 실제로 개선됐는지 관찰한다.

이 사례는 이 장의 순환 전체를 지나간다. 어느 단계에서 멈췄다면("현장 데이터만 보고 기기 없이 추측 수정" 또는 "로컬에서만 확인하고 vitals 로 재확인하지 않음") 문제가 해결됐는지 실제로 알 수 없다.

### 실패 사례: 디버거가 문제를 사라지게 만든다

간헐적으로 발생하는 ANR 을 재현하기 위해 디버거를 연결하고 breakpoint 를 걸었더니, 그 이후로는 문제가 재현되지 않는다. 이것은 문제가 해결됐다는 뜻이 아니라, 디버거 연결로 인해 스레드 타이밍이 바뀌어 원래의 race 조건이나 lock 경합이 사라졌을 가능성이 크다. 이런 경우 디버거 결과를 유일한 증거로 삼지 말고, 로그와 Perfetto trace 처럼 실행 타이밍을 바꾸지 않는 관찰 수단으로 교차 확인해야 한다.

### 반드시 교정해야 할 오해

| 오해 | 교정 |
| --- | --- |
| 로그를 최대한 많이 남기면 원인을 더 잘 찾을 수 있다. | 테스트는 재발 여부를, 진단 도구는 원인을 좁히는 다른 목적이며, 과도한 로그는 오히려 재현 절차를 흐린다. |
| `dumpsys` 로 본 상태가 문제의 원인을 직접 설명한다. | `dumpsys` 는 순간 스냅샷이므로 시간축 trace(Perfetto)와 함께 해석해야 원인을 알 수 있다. |
| Profiler 로 측정한 수치가 곧 회귀 판정 기준이다. | 프로파일러 수치는 오버헤드가 섞인 탐색용이며, 회귀 판정은 동일 조건의 Macrobenchmark 로 다시 측정해야 한다. |
| flaky test 는 우선 무시하고 나중에 고치면 된다. | 방치된 flaky test 는 팀이 실패 신호 전체를 무시하게 만들어 릴리스 게이트의 안전망을 없앤다. |
| 테스트를 통과했으면 실제 사용자 기기에서도 문제없다. | 테스트 통과는 알려진 조건에서의 검증일 뿐이며, 기기·OS·제조사 분포에 따른 문제는 Android vitals 같은 현장 신호로 별도 확인해야 한다. |
| 디버거로 재현이 안 되면 문제가 사라진 것이다. | 디버거 연결이 타이밍을 바꿔 race 나 ANR 을 일시적으로 감출 수 있으므로 다른 수단으로 교차 확인해야 한다. |

### 확인 질문

1. 테스트와 진단 도구는 각각 어떤 질문에 답하는가?
2. Logcat, crash, ANR, debugger 는 각각 무엇을 관찰 대상으로 삼는가?
3. Profiler/Perfetto 와 `dumpsys` 는 각각 "언제"의 상태를 보여주는가?
4. 테스트 레이어를 고를 때 유행이 아니라 무엇을 기준으로 삼아야 하는가?
5. Profiler 와 Macrobenchmark 의 역할이 왜 다른가?
6. flaky test 를 방치하면 릴리스 게이트에 어떤 일이 생기는가?
7. 단계적 출시에서 어느 지표들을 관찰한 뒤에야 대상 비율을 늘리는가?
8. Android vitals 가 개발자 기기 테스트만으로는 부족한 이유는 무엇인가?

### 다음 장으로 이어지는 질문

이 장은 보이지 않는 상태를 증거로 확인하고 릴리스 이후 피드백까지 잇는 순환을 다뤘다. 그러나 같은 앱이 기기와 Android 버전에 따라 달라지는 축 자체는 아직 다루지 않았다.

다음 장에서는 `compileSdk`/`minSdk`/`targetSdk`, 기기 API, SDK extension, 라이브러리 버전, Play 정책, Mainline·OEM 구현, 폼 팩터가 서로 어떤 결정을 제한하는지를 다룬다.

- 같은 코드가 기기마다 다르게 동작할 때 어느 호환성 축을 먼저 의심해야 하는가?
- SDK 버전 하나로 모든 실행 환경 차이를 설명할 수 없는 이유는 무엇인가?
- 이 Learning Spine 전체가 다룬 계약들은 버전과 폼 팩터에 따라 어떻게 달라지는가?

### 관련 정본

- [Logcat, crash, ANR, debugger는 서로 다른 질문에 답한다](../../06_testing_performance/debugging/debugging-contracts/logcat-crash-anr-and-debugger-answer-different-questions.md)
- [Profiler, Perfetto, dumpsys는 벤치마크가 아니라 진단 도구다](../../06_testing_performance/performance/performance-contracts/profiler-perfetto-dumpsys-are-diagnosis-tools-not-benchmarks.md)
- [Android 성능은 측정 후 최적화한다](../../06_testing_performance/performance/performance-contracts/measure-before-optimizing-android-performance.md)
- [테스트 레이어는 피드백 비용으로 선택한다](../../06_testing_performance/testing/testing-quality-contracts/test-layer-is-chosen-by-feedback-cost-and-risk.md)
- [Unit, Integration, UI, E2E 테스트는 실패 신호가 다르다](../../06_testing_performance/testing/testing-quality-contracts/unit-integration-ui-e2e-tests-have-different-failure-signals.md)
- [회귀와 flaky 테스트는 릴리즈 게이트의 신뢰도를 낮춘다](../../06_testing_performance/testing/testing-quality-contracts/regression-and-flaky-tests-are-release-gate-risks.md)
- [Google Play 테스트 트랙은 배포 대상과 피드백 범위를 나눈다](../../03_packaging_deployment/distribution/release-distribution-contracts/google-play-testing-tracks-split-audience-and-feedback-scope.md)
- [단계적 출시는 관측 가능한 릴리스 운영 절차다](../../03_packaging_deployment/distribution/release-distribution-contracts/staged-rollout-is-observable-release-operation.md)

### 공식 근거

- [Logcat command-line tool](https://developer.android.com/tools/logcat)
- [Diagnose ANRs](https://developer.android.com/topic/performance/vitals/anr)
- [Inspect trace events with the System Trace app](https://developer.android.com/topic/performance/tracing)
- [Android vitals overview](https://developer.android.com/topic/performance/vitals)
- [Set up an open, closed, or internal test](https://support.google.com/googleplay/android-developer/answer/9845334)
- [Roll out a staged release](https://support.google.com/googleplay/android-developer/answer/6346149)

검증일: 2026-08-03. Play Console 트랙 명칭, 단계적 출시 UI, Android vitals 의 세부 지표 정의는 콘솔 업데이트에 따라 변경될 수 있으므로 실제 운영 시점에 다시 확인한다.
