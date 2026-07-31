# 테스트 레이어는 피드백 비용으로 선택한다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [테스트 품질 계약](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/testing-quality-contracts.md)

테스트 레이어의 선택 기준은 테스트 종류의 유행이 아니라 피드백 비용이다.
피드백 비용은 실행 시간, 실패 재현성, 원인 파악 난이도, 유지보수 비용을 합친 값이다.
빠른 테스트는 개발 중 자주 실행할 수 있다.
느린 테스트는 실제 환경을 더 잘 재현하지만 실패 원인을 좁히는 데 시간이 든다.

## 기본 원칙

- 가능한 낮은 레이어에서 동작을 검증한다.
- 낮은 레이어로 표현할 수 없는 계약만 높은 레이어로 올린다.
- 하나의 E2E 테스트에 너무 많은 규칙을 넣지 않는다.
- 테스트가 실패했을 때 수정 위치를 바로 추정할 수 있어야 한다.
- 테스트 수의 비율보다 피드백 흐름의 질을 관리한다.

## 레이어별 선택

순수 계산, 상태 전이, 유효성 검사는 JVM 단위 테스트가 적합하다.
단위 테스트는 Android 프레임워크와 네트워크를 제거할수록 빨라진다.
ViewModel은 가짜 저장소와 테스트용 dispatcher를 주입해 상태 변화를 검증한다.
Composable의 노드, 클릭, 입력, 접근성 상태는 Compose UI 테스트로 확인한다.
여러 컴포넌트가 함께 동작하는 데이터 흐름은 통합 테스트로 확인한다.
권한, 시스템 UI, 실제 navigation, 설치 상태는 기기 기반 테스트가 필요하다.
핵심 사용자 여정은 적은 수의 E2E 테스트로 보호한다.

## 결정 질문

이 실패가 순수 Kotlin만으로 재현되는가?
그렇다면 단위 테스트로 내려서 반복 비용을 줄인다.
실패에 Android lifecycle이나 실제 저장소가 필요한가?
그렇다면 계측 또는 통합 테스트로 경계를 올린다.
문제에 실제 창, 권한, 키보드, 백그라운드 프로세스가 포함되는가?
그렇다면 에뮬레이터나 실제 기기에서 검증한다.
여러 화면의 연결이 핵심인가?
그렇다면 전체 흐름을 대표하는 E2E 하나를 추가한다.

## 실행 순서

로컬 저장 시 관련 단위 테스트를 먼저 실행한다.
변경한 feature의 UI 및 통합 테스트를 다음으로 실행한다.
Pull request에서는 빠른 테스트와 핵심 회귀 테스트를 함께 실행한다.
nightly 또는 release 단계에서는 기기 매트릭스와 E2E를 실행한다.
실패가 잦은 높은 레이어 테스트는 원인을 낮은 레이어 테스트로 분해한다.

공식 참고: [Android 테스트 개요](https://developer.android.com/training/testing)
공식 참고: [Compose 테스트](https://developer.android.com/develop/ui/compose/testing)
