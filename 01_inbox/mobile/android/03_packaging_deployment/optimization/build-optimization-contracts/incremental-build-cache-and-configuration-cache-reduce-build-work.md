# 증분 빌드, 캐시, 구성 캐시는 빌드 작업량을 줄인다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [R8와 Gradle 빌드 최적화 계약](01_inbox/mobile/android/03_packaging_deployment/optimization/build-optimization-contracts/build-optimization-contracts.md)

## 캐시를 구분해서 운영하기

증분 빌드는 같은 작업 디렉터리에서 변경되지 않은 입력을 다시 처리하지 않는다.

로컬 또는 원격 Build Cache는 다른 실행에서 태스크 출력을 재사용할 수 있다.

Configuration Cache는 태스크 출력이 아니라 구성 단계의 결과를 재사용한다.

세 기능은 서로 보완하지만 하나가 다른 둘을 대체하지 않는다.

## 캐시 적중을 높이는 조건

- 태스크 입력과 출력이 명확하게 선언되어야 한다.
- 현재 시간, 사용자 홈, 머신 경로를 출력에 직접 섞지 않는다.
- 동적 버전과 불안정한 네트워크 입력을 줄인다.
- 커스텀 태스크를 가능한 한 결정적으로 만든다.
- CI와 로컬에서 캐시 정책과 키 생성 방식을 문서화한다.

`UP-TO-DATE`는 현재 작업의 이전 출력 재사용이다.

`FROM-CACHE`는 캐시에서 출력을 복원했다는 뜻이다.

캐시가 켜져 있어도 입력이 자주 바뀌면 적중률은 낮을 수 있다.

## Configuration Cache 도입 순서

1. 대표적인 `assembleDebug`와 테스트 명령을 선정한다.
2. `--configuration-cache`로 문제를 수집한다.
3. 플러그인의 프로젝트 상태 접근과 구성 시점 파일 읽기를 수정한다.
4. 캐시 재사용 두 번째 실행을 측정한다.
5. IDE sync와 CI 작업은 별도 지원 여부를 확인한다.

Gradle 문서상 모든 플러그인과 기능이 동일하게 지원되는 것은 아니다.

## 릴리즈 성능 테스트

앱 성능은 디버그 APK가 아니라 실제 릴리즈에 가까운 설정으로 측정한다.

R8 수축, 난독화, 리소스 수축, Baseline Profile 적용 여부를 명시한다.

시작 시간은 TTID와 TTFD를 분리해 기록한다.

스크롤과 핵심 사용자 여정은 Macrobenchmark로 반복 측정한다.

Baseline Profile이 있는 경우와 없는 경우를 같은 기기와 조건에서 비교한다.

에뮬레이터 결과만으로 배포 성능을 판단하지 않는다.

## 출시 게이트

- 빌드 시간 기준선과 캐시 적중률
- AAB와 대표 기기 다운로드 크기
- cold start TTID/TTFD
- 핵심 화면 프레임과 jank
- 난독화 오류와 Crash de-obfuscation

참고: [Incremental builds and build caching](https://docs.gradle.org/current/userguide/gradle_optimizations.html)

참고: [Benchmark Baseline Profiles with Macrobenchmark](https://developer.android.com/topic/performance/baselineprofiles/measure-baselineprofile)

참고: [Write a Macrobenchmark](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
