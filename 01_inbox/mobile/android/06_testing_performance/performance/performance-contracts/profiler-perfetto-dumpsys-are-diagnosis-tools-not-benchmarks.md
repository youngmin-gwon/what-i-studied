# Profiler, Perfetto, dumpsys는 벤치마크가 아니라 진단 도구다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [런타임 성능 계약](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/performance-contracts.md)

도구는 많지만 각 도구가 답하는 질문은 다르다.

Android Studio Profiler는 앱 실행 중 CPU, 메모리, 네트워크, 에너지를 탐색한다.

CPU Profiler의 샘플링은 낮은 오버헤드로 넓은 병목을 찾는 데 적합하다.

메서드 tracing은 상세하지만 측정 오버헤드가 커질 수 있다.

Memory Profiler는 힙 덤프, 객체 인스턴스, 할당 위치를 조사한다.

Perfetto는 앱과 Android 시스템을 같은 시간축에서 본다.

스케줄링, 메인 스레드, 프레임, Binder, 전원 이벤트의 관계를 확인할 수 있다.

앱 코드에는 `Trace.beginSection`으로 의미 있는 작업 구간을 표시한다.

표시 이름은 짧고 안정적으로 유지해 trace 비교를 가능하게 한다.

`simpleperf`는 CPU 샘플링과 네이티브 함수 병목을 조사할 때 사용한다.

심볼 정보가 없으면 네이티브 주소를 함수 이름으로 해석하기 어렵다.

`dumpsys`는 시스템 서비스가 현재 보고하는 상태의 스냅샷이다.

`dumpsys gfxinfo`는 프레임 통계를, `meminfo`는 메모리 구성을 보여 준다.

`batterystats`는 배터리 관련 사용량을, `netstats`는 네트워크 통계를 보여 준다.

스냅샷은 원인을 직접 설명하지 않으므로 시간축 trace와 함께 해석한다.

Macrobenchmark는 시작과 스크롤 같은 사용자 여정을 반복해 수치화한다.

프로파일러는 탐색에, 벤치마크는 회귀 판정에 더 적합하다.

[Android Studio 프로파일러](https://developer.android.com/studio/profile)를 앱 수준의 실시간 조사에 사용한다.

[Perfetto로 시스템 추적](https://developer.android.com/topic/performance/tracing)은 스케줄링과 프레임 관계를 확인할 때 기준이다.

[dumpsys 명령](https://developer.android.com/tools/dumpsys)은 서비스별 상태를 조회하는 방법을 설명한다.

[Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)는 반복 가능한 사용자 흐름을 측정한다.

질문이 “어디서 시간이 걸렸나”라면 Profiler나 Perfetto를 먼저 선택한다.

질문이 “현재 상태가 어떤가”라면 `dumpsys`를 선택한다.

질문이 “다음 릴리스에서 나빠졌나”라면 Macrobenchmark를 선택한다.

도구를 겹쳐 사용할 때는 같은 시나리오와 같은 시간 구간을 유지한다.

관찰 결과에는 기기, 빌드, 명령, 측정 시각을 기록한다.
