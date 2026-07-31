# 회귀와 flaky 테스트는 릴리즈 게이트의 신뢰도를 낮춘다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [테스트 품질 계약](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/testing-quality-contracts.md)

회귀 방지는 테스트를 많이 만드는 일이 아니라 신뢰할 수 있는 신호를 유지하는 일이다.
테스트가 실패했을 때 팀이 무시하기 시작하면 안전망이 사라진다.

## 변경 영향에 맞춘 실행

변경한 모듈의 단위 테스트를 먼저 실행한다.
공통 UI 토큰이나 navigation을 바꿨다면 영향 feature의 UI 테스트를 추가한다.
저장소 계약을 바꿨다면 integration 테스트와 대표 E2E를 실행한다.
release 전에는 기기 매트릭스, screenshot, 핵심 사용자 여정을 확인한다.
실행 범위를 줄이더라도 중요한 계약을 빼지 않도록 기준을 문서화한다.

## flaky test 판별

같은 코드와 환경에서 성공과 실패가 번갈아 나타나는 테스트를 의심한다.
공유 mutable state, 실제 시간, 네트워크, 애니메이션, 비결정적 순서가 흔한 원인이다.
테스트 간 데이터와 앱 상태를 초기화한다.
Compose에서는 idle 상태와 비동기 작업의 완료 조건을 명시한다.
고정 sleep을 늘리는 것은 원인을 숨길 뿐 재현성을 보장하지 않는다.

## 격리와 복구

flaky test는 소유자와 재현 정보가 있는 별도 목록으로 관리한다.
일시적으로 quarantine할 수 있지만 만료일과 복구 조건을 함께 둔다.
실패 로그, screenshot, device 정보, seed를 CI artifact로 남긴다.
수정 후에는 반복 실행으로 안정성을 확인하고 본래 게이트에 복귀시킨다.
계속 실패하는 테스트를 무기한 제외하면 회귀가 조용히 통과한다.

## 출시 게이트

필수 계약 테스트의 실패는 출시를 막는다.
비필수 실험 테스트의 실패는 원인과 위험을 기록한 뒤 판단한다.
커버리지는 목표 숫자보다 중요한 경로의 누락을 찾는 보조 지표다.
린트, 정적 분석, unit, integration, UI, screenshot의 책임을 구분한다.
게이트는 실패를 숨기는 장치가 아니라 수정 순서를 알려주는 신호여야 한다.

회귀가 발생하면 먼저 어떤 레이어가 놓쳤는지 찾는다.
그 레이어에 가장 작은 재현 테스트를 추가한 뒤 구현을 수정한다.
같은 종류의 실패가 반복되면 공통 fixture나 테스트 헬퍼를 개선한다.
테스트가 제공하는 신호의 신뢰도도 품질 지표로 기록한다.
신뢰할 수 없는 게이트는 통과율보다 먼저 운영 문제로 다룬다.

공식 참고: [Android 테스트 기본](https://developer.android.com/training/testing)
공식 참고: [Android Test Orchestrator](https://developer.android.com/training/testing/instrumented-tests/androidx-test-libraries/runner)
