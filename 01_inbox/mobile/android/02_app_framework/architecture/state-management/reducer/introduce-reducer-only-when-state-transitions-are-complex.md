# Reducer는 상태 계산이 반복되고 전이 규칙이 복잡해질 때만 도입한다

상위 문서: [Android Reducer](01_inbox/mobile/android/02_app_framework/architecture/state-management/reducer/reducer.md)


## 핵심 주장

Reducer는 모든 화면에 기본으로 추가하는 계층이 아니다.
작은 화면은 ViewModel의 `_uiState.update { it.copy(...) }`가 가장 읽기 쉽고, 상태 계산이 반복되거나 전이 규칙을 한 곳에서 읽어야 할 때만 Reducer를 도입한다.

## 아직 필요하지 않은 경우

- 단순 조회나 목록 화면
- 상태 필드가 적은 상세 화면
- 몇 개의 명시적 callback만 있는 설정 화면
- ViewModel 테스트만으로 전이가 충분히 읽히는 화면

## 도입을 검토할 경우

- 입력 필드와 action 종류가 크게 늘어난다.
- 여러 함수에 `copy`와 검증 계산이 반복된다.
- 특정 action이 어떤 상태를 만드는지 ViewModel 전체를 읽어야 한다.
- 회원가입, 결제, 주문, 예약, wizard처럼 단계 전이가 많다.
- Reducer 단위 순수 JVM 테스트가 ViewModel 테스트보다 명확하다.

## 도입 원칙

1. 먼저 단순한 ViewModel로 시작한다.
2. 반복되는 상태 계산만 Reducer로 옮긴다.
3. Repository, coroutine, Flow, event stream은 ViewModel에 남긴다.
4. `oldState + action -> newState` 계약을 테스트한다.
5. 새 아키텍처를 도입하기보다 ViewModel 내부 계산을 분리한 리팩터링으로 다룬다.

Reducer가 생겼다는 이유만으로 Store, Processor, Result 계층을 추가하지 않는다.
복잡도를 줄이는 만큼만 추상화하고, 상태 전이 규칙이 단순해지면 직접 `update`로 되돌릴 수도 있다.

## 복잡도의 신호

코드 줄 수 자체보다 상태 전이의 추적 비용을 본다.
`copy`가 몇 번 있는지는 참고 지표일 뿐이며, 작은 화면에서 Reducer를 추가하면 Action과 dispatch가 오히려 잡음을 만든다.
반대로 필드가 많지 않아도 한 action이 여러 필드의 검증, 단계, 오류를 함께 바꾸면 분리가 유용할 수 있다.

## 도입 후 점검

- Reducer 이름만 있고 실제 계산은 ViewModel에 남아 있지 않은가?
- 외부 의존성이 Reducer 안으로 새어 들어오지 않았는가?
- action 목록이 화면의 실제 사용자 행동과 결과를 설명하는가?
- 순수 JVM 테스트가 전이 표를 읽기 쉽게 표현하는가?

이 질문에 부정적이면 Reducer가 복잡도를 줄이는지 다시 확인한다.
