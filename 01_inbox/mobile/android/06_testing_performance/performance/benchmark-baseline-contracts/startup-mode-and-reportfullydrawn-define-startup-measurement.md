# Startup mode와 reportFullyDrawn이 시작 측정 기준을 정한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [Benchmark와 Baseline Profile 계약](01_inbox/mobile/android/06_testing_performance/performance/benchmark-baseline-contracts/benchmark-baseline-contracts.md)
관련 정본: [Android 성능은 측정 후 최적화한다](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/measure-before-optimizing-android-performance.md)

## 시작 성능의 범위

- 앱 시작 시간은 사용자가 앱을 실행한 뒤 첫 화면을 보기까지의 흐름이다.
- 시작 성능은 프로세스 상태와 첫 화면의 준비 기준에 따라 달라진다.
- Macrobenchmark는 시작 측정에 `StartupTimingMetric`을 사용할 수 있다.
- `StartupMode.COLD`는 프로세스가 새로 시작되는 상황을 대표하는 기준이다.
- warm과 hot 시작은 이미 실행된 프로세스나 화면을 재사용하는 조건을 다룬다.

## 모드 선택

- 콜드 시작은 신규 실행과 업데이트 직후의 체감 문제를 찾는 데 유용하다.
- 웜 시작은 프로세스가 남아 있을 때 재진입하는 비용을 본다.
- 핫 시작은 이미 화면이 준비된 상태에서 돌아오는 비용을 본다.
- 제품의 주요 사용자 경험에 맞춰 하나의 모드만 고집하지 않는다.
- 모드마다 setup 절차와 해석 기준을 별도로 기록한다.

## 종료 기준

- 첫 프레임이 그려진 시점은 화면의 모든 데이터가 준비된 시점과 다를 수 있다.
- 앱이 `reportFullyDrawn()`을 호출하면 완전한 초기 화면 기준을 측정에 활용할 수 있다.
- TTFD는 첫 화면이 사용자에게 충분히 표시되었다고 판단하는 시점까지의 시간이다.
- 화면이 비어 있는 상태를 먼저 그린 뒤 데이터를 채우는 앱은 기준을 명확히 해야 한다.
- 측정하려는 종료 지점이 사용자 체감과 일치하는지 제품 요구사항으로 합의한다.

## 설계 체크리스트

1. 시작 전 앱 프로세스와 화면 상태를 정한다.
2. `startActivityAndWait()` 이후 기다릴 UI 신호를 정한다.
3. 필요하면 `reportFullyDrawn()` 호출 조건을 코드로 명확히 한다.
4. 로딩 스피너가 사라지는 것과 데이터 콘텐츠가 보이는 것을 구분한다.
5. cold, warm, hot 결과를 같은 표에서 섞지 않는다.

## 흔한 오류

- 모든 시작을 cold로 부르면서 실제로는 이전 프로세스를 재사용한다.
- 고정된 sleep으로 화면 준비를 추정해 기기별 오차를 만든다.
- TTFD를 사용하면서 앱이 해당 신호를 올바른 시점에 보고하지 않는다.
- 첫 프레임과 완전한 화면을 동일한 품질 목표로 취급한다.
- 시작 후 추가 클릭을 포함하고도 시작 metric의 범위를 설명하지 않는다.

## 공식 참고

- [Macrobenchmark 개요](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
- [Baseline Profile 측정](https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile)
