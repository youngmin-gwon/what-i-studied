---
title: "Reducer는 Repository, Coroutine, Flow, Android API에 의존하지 않는다"
tags: [android, android/architecture, android/state-management, android/reducer]
aliases: ["Reducer는 Repository, Coroutine, Flow, Android API에 의존하지 않는다"]
date modified: 2026-08-01 00:00:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

# Reducer는 Repository, Coroutine, Flow, Android API에 의존하지 않는다

상위 문서: [Android Reducer](01_inbox/mobile/android/02_app_framework/architecture/state-management/reducer/reducer.md)


## 핵심 주장

Reducer는 순수 상태 전이만 담당하므로 Repository, `suspend` 함수, coroutine scope, Flow, `Context`, `NavController`에 의존하지 않는다.
이 경계를 지켜야 상태 전이가 빠르고 결정적인 순수 JVM 테스트 대상이 된다.

```text
Reducer에 허용
- 이전 UiState
- Action
- 순수 계산 함수

Reducer에 금지
- Repository/API 호출
- viewModelScope.launch
- Flow.collect 또는 emit
- Context/Resources/Android framework
- 현재 시간, 파일, 네트워크, 랜덤값 직접 참조
```

외부 작업은 ViewModel이나 UseCase가 수행하고 그 결과를 action으로 변환한다.

```text
SubmitClick
 -> ViewModel이 SubmitStarted dispatch
 -> Repository.signUp() 실행
 -> 성공/실패 action dispatch
 -> Reducer가 새 UiState 계산
```

이 구조에서 ViewModel은 작업의 수명과 취소를 조율하고, Reducer는 작업 결과를 화면 상태로 반영하는 규칙만 안다.
Reducer가 Repository를 직접 호출하면 테스트가 fake client, dispatcher, Android 환경에 끌려가고 상태 계산의 책임이 흐려진다.

Reducer 테스트는 다음처럼 작아야 한다.

```kotlin
val next = reducer.reduce(oldState, SignUpAction.SubmitStarted)
assertTrue(next.isSubmitting)
```

## 의존성 경계의 의미

순수성은 테스트 편의만을 위한 규칙이 아니다.
Reducer가 플랫폼과 데이터 계층을 몰라야 상태 전이 규칙을 다른 UI toolkit이나 실행 환경에서도 재사용할 수 있다.
또한 외부 작업의 실패, 취소, 재시도 정책을 ViewModel 또는 UseCase에서 명시적으로 결정하게 만든다.

시간이나 랜덤값이 정말 상태 전이에 필요하다면 Reducer가 직접 읽지 말고 action의 값으로 전달한다.
그러면 시간과 랜덤성은 경계에서 한 번만 결정되고 Reducer는 여전히 결정적이다.

```text
Bad: reducer가 Clock.now()를 직접 호출
Good: dispatch(Action.Timeout(now = clock.now()))
```
