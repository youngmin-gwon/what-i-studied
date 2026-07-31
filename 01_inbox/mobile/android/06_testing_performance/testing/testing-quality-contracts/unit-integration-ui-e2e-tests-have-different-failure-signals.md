---
title: "Unit, Integration, UI, E2E 테스트는 실패 신호가 다르다"
tags: ["android", "android/testing-performance"]
---

# Unit, Integration, UI, E2E 테스트는 실패 신호가 다르다

상위 문서: [Android 성능, 품질, 빌드 최적화 지도](01_inbox/mobile/android/06_testing_performance/performance/android-performance-quality-and-build-optimization.md)
관련 지도: [테스트 품질 계약](01_inbox/mobile/android/06_testing_performance/testing/testing-quality-contracts/testing-quality-contracts.md)

테스트 이름보다 중요한 것은 무엇을 실제로 연결했는지다.
경계는 실행 환경, 의존성, 관찰 가능한 결과로 정의한다.

## Unit

Unit 테스트는 하나의 규칙 또는 변환을 격리해 검증한다.
UseCase, reducer, mapper, validator, formatter가 대표적인 대상이다.
시간, 난수, dispatcher, 네트워크, 저장소는 주입 가능한 인터페이스로 둔다.
테스트는 입력, 실행, 결과의 세 단계가 분명해야 한다.
mock 호출 횟수보다 반환 상태와 도메인 결과를 우선 검증한다.

## Integration

Integration 테스트는 둘 이상의 실제 구성요소가 계약대로 연결되는지 확인한다.
Repository와 database, client와 serializer, ViewModel과 UseCase가 예시다.
외부 서버 대신 통제 가능한 fake 또는 MockWebServer를 사용할 수 있다.
실제 구현을 연결하되 외부 시스템의 불안정성은 테스트 경계 밖으로 둔다.
통합 테스트는 매핑 누락, transaction, dispatcher 연결 같은 오류를 잡는다.

## UI

UI 테스트는 사용자에게 보이는 상태와 상호작용을 검증한다.
ComposeTestRule로 content를 설정하고 노드를 찾아 행동과 assertion을 수행한다.
화면 내부의 로직 전체를 UI 테스트에 복제하지 않는다.
UI 테스트는 클릭 후 상태, 입력 오류, 로딩, 빈 상태, 접근성 노출을 다룬다.
문구 자체가 계약이면 semantics를 검증하고, 단순 타깃이면 안정적인 식별자를 쓴다.

## E2E

E2E는 앱 설치부터 여러 화면을 거치는 사용자 여정을 검증한다.
navigation, 권한, 앱 재시작, 시스템 키보드처럼 낮은 레이어가 재현하기 어려운 문제를 다룬다.
모든 분기를 E2E로 만들면 실패 원인과 실행 시간이 함께 커진다.
대표 여정만 남기고 세부 규칙은 unit, integration, UI로 내린다.
외부 API는 테스트 서버나 고정 fixture로 통제해 네트워크 변동을 줄인다.

## 경계 위반 신호

- Unit 테스트가 Android device를 필요로 한다.
- UI 테스트가 내부 private 함수의 호출 횟수를 검증한다.
- E2E 실패가 어느 화면에서 발생했는지 알 수 없다.
- 테스트가 실제 시간, 실제 네트워크, 공유 계정에 의존한다.
- 하나의 테스트가 너무 많은 준비와 정리를 수행한다.

경계가 흐려졌다면 테스트를 삭제하기보다 책임을 낮은 레이어로 이동한다.
테스트 이름에는 검증하는 계약을 적고 구현 세부사항은 적게 노출한다.

공식 참고: [Android 테스트에서 로컬 및 계측 테스트](https://developer.android.com/training/testing/local-tests)
공식 참고: [Android 테스트에서 계측 테스트](https://developer.android.com/training/testing/instrumented-tests)
