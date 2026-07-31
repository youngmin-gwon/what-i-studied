# Macrobenchmark의 컴파일 모드는 테스트 계약의 일부다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [Benchmark와 Baseline Profile 계약](01_inbox/mobile/android/06_testing_performance/performance/benchmark-baseline-contracts/benchmark-baseline-contracts.md)
관련 노트: [Android 성능은 측정 후 최적화한다](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/measure-before-optimizing-android-performance.md)

## 왜 컴파일 상태를 고정하는가

- Android 앱 성능은 같은 코드라도 ART가 어떻게 컴파일했는지에 따라 달라진다.
- Macrobenchmark는 `CompilationMode`로 측정 전 컴파일 조건을 명시할 수 있다.
- 조건을 명시해야 Baseline Profile의 효과를 다른 변화와 분리할 수 있다.
- 프로필 적용 전후를 비교할 때는 컴파일 모드의 의미를 결과와 함께 기록한다.

## 주요 비교군

- `CompilationMode.None`은 프로필 기반 사전 컴파일이 없는 상태를 비교하는 기준이 된다.
- `CompilationMode.Partial`은 일부 코드가 사전 컴파일된 상태를 나타낸다.
- Partial에 Baseline Profile 요구 조건을 결합하면 프로필 적용을 검증할 수 있다.
- `CompilationMode.Full`은 전체 컴파일에 가까운 상한선 비교에 사용될 수 있다.
- 실제 프로젝트에서 지원되는 API와 라이브러리 버전에 맞춰 모드를 선택한다.

## 해석 규칙

1. 먼저 동일한 앱과 동일한 여정을 기준군으로 측정한다.
2. 다음으로 Baseline Profile이 포함된 릴리스 변형을 측정한다.
3. 두 결과의 차이를 프로필 효과의 후보 신호로 본다.
4. 차이가 없으면 프로필이 여정의 핫 경로를 충분히 포함하는지 확인한다.
5. 차이가 있어도 기기 열 상태와 반복 분산을 함께 검토한다.

## 주의할 점

- 컴파일 모드 이름만 보고 실제 사용자 설치 상태를 완전히 동일하다고 단정하지 않는다.
- 디버그 빌드의 계측, 로그, 최적화 설정은 릴리스 결과를 왜곡할 수 있다.
- 프로필이 없는 상태와 프로필이 적용된 상태의 APK 또는 설치 절차를 구분한다.
- 측정 중 앱이 이전 반복의 상태를 이어받지 않도록 시작 조건을 초기화한다.
- 모드 변경과 코드 변경을 한 번에 수행하면 원인 분석이 어려워진다.

## 보고서에 남길 항목

- 앱 버전과 빌드 변형
- 대상 기기와 Android 버전
- 컴파일 모드와 Baseline Profile 포함 여부
- startup mode와 반복 횟수
- 사용한 metric과 대표 통계량
- 측정 날짜와 실행 환경

## 공식 참고

- [Macrobenchmark 개요](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
- [Baseline Profile 측정](https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile)
