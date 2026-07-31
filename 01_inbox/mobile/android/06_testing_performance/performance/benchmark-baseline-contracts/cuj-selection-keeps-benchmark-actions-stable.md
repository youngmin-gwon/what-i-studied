# CUJ 선택은 벤치마크 행동을 안정화한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [Benchmark와 Baseline Profile 계약](01_inbox/mobile/android/06_testing_performance/performance/benchmark-baseline-contracts/benchmark-baseline-contracts.md)
관련 정본: [Android 성능은 측정 후 최적화한다](01_inbox/mobile/android/06_testing_performance/performance/performance-contracts/measure-before-optimizing-android-performance.md)

## CUJ란 무엇인가

- CUJ는 Critical User Journey, 즉 핵심 사용자 여정이다.
- 성능 테스트의 CUJ는 사용자가 반복적으로 수행하고 결과를 체감하는 흐름이어야 한다.
- 모든 화면을 벤치마크에 넣는 것이 목적은 아니다.
- 제품 가치와 성능 위험이 만나는 소수의 흐름을 우선 선택한다.

## 선정 기준

- 앱 시작과 첫 유효 화면 도달
- 로그인 후 핵심 기능 진입
- 긴 목록의 초기 로드와 스크롤
- 검색어 입력 후 결과 표시
- 상세 화면 열기와 주요 상호작용
- 결제나 저장처럼 실패 비용이 큰 동작

## 좋은 CUJ의 조건

- 시작 상태가 재현 가능하다.
- 종료 상태를 UI 신호로 판별할 수 있다.
- 사용자의 실제 행동 순서를 따른다.
- 측정 대상 병목이 여정 안에서 충분히 발생한다.
- 매 반복에 필요한 데이터와 권한이 준비되어 있다.

## UI Automator와 Compose

- Macrobenchmark 테스트는 대상 앱과 분리된 프로세스에서 실행된다.
- Compose 요소는 안정적인 테스트 태그나 접근 가능한 식별자를 제공해야 한다.
- 텍스트 검색만 사용하면 다국어와 카피 변경에 취약할 수 있다.
- 리소스 ID, 콘텐츠 설명, 테스트 태그 중 팀의 규칙을 정한다.
- 클릭 후 화면 전환이 끝났는지 명시적인 UI 조건으로 확인한다.

## 측정 블록 구성

1. setup에서 홈 이동과 초기 화면 준비를 수행한다.
2. 측정 블록에는 사용자가 수행하는 핵심 액션만 둔다.
3. 네트워크 대기나 애니메이션 종료는 안정적인 조건으로 기다린다.
4. 측정 끝에는 여정의 완료 상태가 실제로 도달했는지 확인한다.
5. 동일한 CUJ를 Baseline Profile 생성과 검증에 재사용한다.

## 피해야 할 패턴

- 임의의 좌표 클릭으로 화면 구조에 강하게 결합하기
- 너무 짧은 timeout으로 간헐적 실패를 만들기
- 성능과 무관한 긴 sleep을 매 반복에 포함하기
- 프로필 생성용 흐름과 측정용 흐름을 다르게 만들기
- 한 테스트에 너무 많은 독립 여정을 넣어 원인을 흐리기

## 공식 참고

- [Macrobenchmark 개요](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
- [Baseline Profile 생성](https://developer.android.com/topic/performance/baselineprofiles/create-baselineprofile)
