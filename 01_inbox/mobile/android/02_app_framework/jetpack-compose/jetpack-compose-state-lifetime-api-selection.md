# Compose State Lifetime & API 선택 가이드

이 문서는 Compose에서 상태나 작업을 **얼마나 오래 살릴지**에 따라 어떤 owner와 API를 선택해야 하는지 정리합니다.

핵심은 다음입니다.

```text
상태를 오래 살리고 싶다
-> 더 높은 owner로 hoist한다

상태를 같이 죽이고 싶다
-> 그 composable 안에서 remember/effect로 소유한다

navigation destination 수명에 묶고 싶다
-> entry-scoped ViewModel을 쓴다

앱/세션 수명에 묶고 싶다
-> root ViewModel, repository, DataStore/Room로 올린다
```

관련 공식 문서:

- [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
- [State hoisting](https://developer.android.com/develop/ui/compose/state-hoisting)
- [Side-effects in Compose](https://developer.android.com/develop/ui/compose/side-effects)
- [Lifecycle in Jetpack Compose](https://developer.android.com/topic/libraries/architecture/lifecycle)
- [Use Kotlin coroutines with lifecycle-aware components](https://developer.android.com/topic/libraries/architecture/coroutines)

---

---

## 원자 노트

- [[01-먼저-수명을-정한다|먼저 수명을 정한다]]
- [[02-하나의-composable과-같이-사라져야-하는-상태|하나의 Composable과 같이 사라져야 하는 상태]]
- [[03-composable보다-오래-살아야-하는-작은-ui-복원-상태|Composable보다 오래 살아야 하는 작은 UI 복원 상태]]
- [[04-비동기-작업이-composable과-같이-취소되어야-할-때|비동기 작업이 Composable과 같이 취소되어야 할 때]]
- [[05-이벤트-handler에서-coroutine이-필요할-때|이벤트 handler에서 coroutine이 필요할 때]]
- [[06-등록과-해제가-쌍이면-disposableeffect|등록과 해제가 쌍이면 DisposableEffect]]
- [[07-화면에-그릴-flow는-collectasstatewithlifecycle|화면에 그릴 Flow는 collectAsStateWithLifecycle]]
- [[08-view-system에서는-repeatonlifecycle|View system에서는 repeatOnLifecycle]]
- [[09-start-stop-또는-resume-pause에-맞춘-작업|START/STOP 또는 RESUME/PAUSE에 맞춘 작업]]
- [[10-navigation-entry-수명에-묶고-싶을-때|Navigation entry 수명에 묶고 싶을 때]]
- [[11-하나의-composable보다-오래-앱-전체보다는-짧게|하나의 Composable보다 오래, 앱 전체보다는 짧게]]
- [[12-앱-세션-수명-상태|앱/세션 수명 상태]]
- [[13-선택-규칙|선택 규칙]]
- [[14-흔한-실수|흔한 실수]]
- [[15-관련-문서|관련 문서]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
