---
title: android-task-and-app-back-stack-are-different-stacks
tags: [android, android/navigation, android/navigation3]
aliases: ["Android Task 와 앱 back stack 은 다른 상태다"]
date modified: 2026-08-03 18:11:58 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android Task 와 앱 back stack 은 다른 상태다

상위 문서: [Navigation 3 계약](./navigation3-contracts.md)

### 두 back 의 의미

Android `Task` 는 OS 가 관리하는 Activity 실행 이력이다.

Navigation 3 `NavBackStack` 은 앱이 관리하는 Compose destination key 목록이다.

Single Activity 앱에서는 하나의 Activity 안에서 여러 화면이 바뀌므로 둘을 동일시하면 안 된다.

| 개념 | 주 소유자 | 담는 것 |
| --- | --- | --- |
| Activity | Android OS 와 앱 | 앱 창과 intent 진입점 |
| Task | Android OS | Activity 실행 이력과 최근 앱 문맥 |
| NavBackStack | 앱 navigation layer | Compose 화면 key 와 이동 순서 |

일반적인 앱 내부 이동은 `NavBackStack` 을 수정한다.

사용자가 뒤로 가면 현재 entry 를 제거하고, stack 이 더 이상 없을 때 Activity 나 상위 시스템에 back 처리를 위임할 수 있다.

```kotlin
NavDisplay(
    backStack = backStack,
    onBack = { backStack.removeLastOrNull() },
    entryProvider = appEntryProvider,
)
```

외부 Activity 가 개입하는 본인 인증, 결제, 파일 선택에서는 Task 의 전환이 보인다.

그 Activity 에서 돌아오는 결과는 intent callback 으로 받고, 앱 내부의 다음 화면은 다시 typed key 와 back stack 으로 결정한다.

외부 Activity 가 있었다는 사실을 앱 화면 이력에 그대로 복제할 필요는 없다.

Task 복원과 NavBackStack 복원도 별개다.

OS 가 Activity 를 다시 만들 수 있고, 앱은 저장된 navigation state 에서 유효한 key stack 을 재구성해야 한다.

key 에 큰 객체를 넣지 말아야 하는 이유도 이 복원 경계 때문이다.

테스트에서도 두 계층을 나눠 검증한다.

route reducer 테스트는 push, pop, deep link stack 이 올바른지 확인한다.

Activity 테스트는 intent 가 앱에 도착하고 외부 Activity 결과가 앱 상태로 되돌아오는지만 확인한다.

최근 앱에서 task 를 다시 열었을 때 마지막 화면을 복원하는 동작은 process death 와 함께 별도로 점검한다.

deep link 로 앱이 새로 열릴 때 OS 는 Activity 를 만들지만 원하는 `[root, detail]` stack 을 자동으로 보장하지 않는다.

앱이 URI 를 route key 로 바꾸고 필요한 root 를 직접 구성해야 한다.

결론적으로 Task 는 앱 실행 문맥, NavBackStack 은 앱 화면 문맥이다.

두 상태를 연결하는 지점은 Activity 의 intent 와 back dispatch 이며, 각 상태의 소유권은 분리한다.

이 구분을 문서와 코드의 용어에도 반영하면 복원 버그와 back 처리의 오해를 줄일 수 있다.

앱 내부 화면의 정답은 OS task 가 아니라 현재 유효한 `NavKey` stack 에서 찾아야 한다.
