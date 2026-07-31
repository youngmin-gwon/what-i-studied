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

- [먼저 수명을 정한다](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection/01-%EB%A8%BC%EC%A0%80-%EC%88%98%EB%AA%85%EC%9D%84-%EC%A0%95%ED%95%9C%EB%8B%A4.md)
- [하나의 Composable과 같이 사라져야 하는 상태](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection/02-%ED%95%98%EB%82%98%EC%9D%98-composable%EA%B3%BC-%EA%B0%99%EC%9D%B4-%EC%82%AC%EB%9D%BC%EC%A0%B8%EC%95%BC-%ED%95%98%EB%8A%94-%EC%83%81%ED%83%9C.md)
- [Composable보다 오래 살아야 하는 작은 UI 복원 상태](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection/03-composable%EB%B3%B4%EB%8B%A4-%EC%98%A4%EB%9E%98-%EC%82%B4%EC%95%84%EC%95%BC-%ED%95%98%EB%8A%94-%EC%9E%91%EC%9D%80-ui-%EB%B3%B5%EC%9B%90-%EC%83%81%ED%83%9C.md)
- [비동기 작업이 Composable과 같이 취소되어야 할 때](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection/04-%EB%B9%84%EB%8F%99%EA%B8%B0-%EC%9E%91%EC%97%85%EC%9D%B4-composable%EA%B3%BC-%EA%B0%99%EC%9D%B4-%EC%B7%A8%EC%86%8C%EB%90%98%EC%96%B4%EC%95%BC-%ED%95%A0-%EB%95%8C.md)
- [이벤트 handler에서 coroutine이 필요할 때](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection/05-%EC%9D%B4%EB%B2%A4%ED%8A%B8-handler%EC%97%90%EC%84%9C-coroutine%EC%9D%B4-%ED%95%84%EC%9A%94%ED%95%A0-%EB%95%8C.md)
- [등록과 해제가 쌍이면 DisposableEffect](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection/06-%EB%93%B1%EB%A1%9D%EA%B3%BC-%ED%95%B4%EC%A0%9C%EA%B0%80-%EC%8C%8D%EC%9D%B4%EB%A9%B4-disposableeffect.md)
- [화면에 그릴 Flow는 collectAsStateWithLifecycle](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection/07-%ED%99%94%EB%A9%B4%EC%97%90-%EA%B7%B8%EB%A6%B4-flow%EB%8A%94-collectasstatewithlifecycle.md)
- [View system에서는 repeatOnLifecycle](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection/08-view-system%EC%97%90%EC%84%9C%EB%8A%94-repeatonlifecycle.md)
- [START/STOP 또는 RESUME/PAUSE에 맞춘 작업](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection/09-start-stop-%EB%98%90%EB%8A%94-resume-pause%EC%97%90-%EB%A7%9E%EC%B6%98-%EC%9E%91%EC%97%85.md)
- [Navigation entry 수명에 묶고 싶을 때](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection/10-navigation-entry-%EC%88%98%EB%AA%85%EC%97%90-%EB%AC%B6%EA%B3%A0-%EC%8B%B6%EC%9D%84-%EB%95%8C.md)
- [하나의 Composable보다 오래, 앱 전체보다는 짧게](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection/11-%ED%95%98%EB%82%98%EC%9D%98-composable%EB%B3%B4%EB%8B%A4-%EC%98%A4%EB%9E%98-%EC%95%B1-%EC%A0%84%EC%B2%B4%EB%B3%B4%EB%8B%A4%EB%8A%94-%EC%A7%A7%EA%B2%8C.md)
- [앱/세션 수명 상태](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection/12-%EC%95%B1-%EC%84%B8%EC%85%98-%EC%88%98%EB%AA%85-%EC%83%81%ED%83%9C.md)
- [선택 규칙](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection/13-%EC%84%A0%ED%83%9D-%EA%B7%9C%EC%B9%99.md)
- [흔한 실수](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection/14-%ED%9D%94%ED%95%9C-%EC%8B%A4%EC%88%98.md)
- [관련 문서](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection/15-%EA%B4%80%EB%A0%A8-%EB%AC%B8%EC%84%9C.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
