# Screenshot testing은 시각 회귀를 검출한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [테스트 품질 계약](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/testing-quality-contracts.md)

동작 테스트가 통과해도 간격, 색, 폰트, 정렬은 깨질 수 있다.
Screenshot testing은 정해진 상태를 이미지로 기록하고 기준 이미지와 비교한다.
따라서 시각적 계약이 중요한 UI 컴포넌트의 회귀를 빠르게 발견한다.

## 적합한 대상

- 디자인 시스템의 버튼, 카드, 입력 상태
- 로딩, 오류, 빈 상태, 권한 안내처럼 상태가 많은 화면
- 다크 모드와 주요 화면 크기
- 디자인 변경의 영향 범위를 검토해야 하는 공통 컴포넌트

전체 앱을 한 장으로 캡처하면 차이의 원인을 찾기 어렵다.
독립적인 컴포넌트와 대표 화면 상태를 작은 단위로 캡처한다.
동적 시간, 네트워크, 사용자 이름은 고정 fixture로 바꾼다.

## 신뢰할 수 있는 기준 이미지

폰트, locale, density, 글꼴 배율, 화면 크기를 명시한다.
애니메이션과 커서처럼 매번 달라지는 요소는 고정하거나 제거한다.
기준 이미지 변경은 테스트 실패를 숨기는 승인 절차가 아니다.
제품 의도에 맞는 변경인지 사람이 확인한 뒤 golden을 갱신한다.
기준 이미지와 실제 이미지의 차이를 diff artifact로 보존한다.

## 실행 전략

JVM 기반 도구는 빠른 피드백에 적합하고 에뮬레이터 비용을 줄일 수 있다.
실제 렌더러, 폰트, 하드웨어 차이가 계약인 경우 기기 캡처를 추가한다.
기본 상태는 pull request에서 실행한다.
전체 locale과 화면 매트릭스는 nightly 또는 release 검증으로 분리할 수 있다.

## 실패를 해석하는 순서

먼저 레이아웃 크기와 위치가 바뀌었는지 확인한다.
다음으로 색상, 폰트, 시스템 설정, locale 차이를 확인한다.
의도된 디자인 변경이면 기준 이미지를 갱신한다.
의도하지 않은 차이면 원인이 된 토큰 또는 컴포넌트 테스트를 보강한다.
픽셀 차이를 무조건 허용하면 시각적 회귀 방지 기능이 약해진다.

Screenshot testing은 클릭 흐름을 대체하지 않는다.
동작은 UI 테스트로, 시각적 결과는 screenshot testing으로 분리한다.

공식 참고: [Android UI 테스트 개요](https://developer.android.com/training/testing/ui-testing)
공식 참고: [Compose 테스트](https://developer.android.com/develop/ui/compose/testing)
