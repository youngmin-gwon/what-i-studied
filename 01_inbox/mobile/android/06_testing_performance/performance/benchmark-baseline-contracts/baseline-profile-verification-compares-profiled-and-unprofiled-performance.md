# Baseline Profile 검증은 profiled와 unprofiled 성능을 비교한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [Benchmark와 Baseline Profile 계약](01_inbox/mobile/android/06_testing_performance/performance/benchmark-baseline-contracts/benchmark-baseline-contracts.md)
관련 노트: [Android 성능은 측정 후 최적화한다](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/measure-before-optimizing-android-performance.md)

## 두 작업의 차이

- 생성은 대표 사용자 여정을 실행해 프로필을 수집하는 단계다.
- 검증은 그 프로필이 실제 성능을 개선했는지 측정하는 단계다.
- 생성이 성공했다고 해서 앱 시작이나 스크롤이 빨라졌다는 뜻은 아니다.
- 검증은 Macrobenchmark로 동일한 CUJ의 결과를 비교해야 한다.

## 검증 설계

1. 프로필이 없는 기준 빌드를 준비한다.
2. 동일한 코드와 데이터로 프로필 포함 빌드를 준비한다.
3. 두 빌드를 같은 물리 기기에서 실행한다.
4. 같은 compilation mode와 startup mode를 적용한다.
5. 같은 metric, 반복 횟수, 초기화 절차를 사용한다.
6. 결과 분포와 트레이스를 함께 비교한다.

## 검증 대상

- cold startup 시간
- warm 또는 hot startup 시간
- 첫 화면의 완전한 표시 시간
- 주요 화면 전환 시간
- 스크롤 프레임 시간과 jank
- 생성에 포함한 CUJ의 실제 체감 지표

## 결과 해석

- 프로필 포함 빌드가 항상 모든 지표를 개선한다고 가정하지 않는다.
- 프로필 효과가 시작에 집중되고 이후 화면에는 작을 수 있다.
- 차이가 작으면 측정 분산, 프로필 적용 상태, CUJ 대표성을 먼저 확인한다.
- 결과를 중앙값 하나로만 결론 내리지 말고 이상치와 백분위도 본다.
- 코드 변경이 섞였다면 해당 실행은 프로필 효과의 순수 비교가 아니다.

## 적용 상태 확인

- 올바른 릴리스 변형에 프로필 파일이 포함되었는지 확인한다.
- 테스트가 의도한 앱 패키지를 실행하는지 확인한다.
- 설치·재설치 절차가 비교군마다 동일한지 확인한다.
- 요구한 프로필을 찾지 못한 실행을 성공 결과로 취급하지 않는다.
- 성능 리포트에 프로필 파일 버전과 생성 시나리오를 기록한다.

## 결론의 형태

- “프로필 생성 성공”은 산출물 생성에 대한 결론이다.
- “프로필 적용 후 cold startup 개선”은 측정 결과에 대한 결론이다.
- 두 문장을 하나의 테스트 통과 의미로 합치지 않는다.

## 공식 참고

- [Baseline Profile 생성](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
- [Baseline Profile 측정](https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile)
