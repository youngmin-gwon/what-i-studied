# Compose Automatic State Observation: Flutter 개발자 관점

이 문서는 Android Developers 영상
[A Compose State of Mind - Using Jetpack Compose's Automatic State Observation](https://www.youtube.com/watch?v=rmv2ug-wW4U)
의
핵심을 Flutter 개발자 관점에서 정리합니다.

이 문서의 범위는 `remember`, `mutableStateOf`, ViewModel API 사용법 자체가 아니라, Compose Runtime이 상태를 어떻게 관찰하고
recomposition 범위를 어떻게 결정하는지 이해하는 것입니다. API 선택은
[jetpack-compose-state-management-flutter-comparison](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-management-flutter-comparison.md)와
[jetpack-compose-state-lifetime-api-selection](01_inbox/mobile/android/02_app_framework/jetpack-compose/state-and-lifecycle/jetpack-compose-state-lifetime-api-selection.md)를 기준으로 봅니다.

관련 공식 문서:

- [Thinking in Compose](https://developer.android.com/develop/ui/compose/mental-model)
- [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
- [State hoisting](https://developer.android.com/develop/ui/compose/state-hoisting)
- [Side-effects in Compose](https://developer.android.com/develop/ui/compose/side-effects)

---

---

## 원자 노트

- [이 영상의 핵심](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/jetpack-compose-automatic-state-observation-for-flutter-developers/01-%EC%9D%B4-%EC%98%81%EC%83%81%EC%9D%98-%ED%95%B5%EC%8B%AC.md)
- [Flutter식 rebuild 사고와 Compose식 observation 사고](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/jetpack-compose-automatic-state-observation-for-flutter-developers/02-flutter%EC%8B%9D-rebuild-%EC%82%AC%EA%B3%A0%EC%99%80-compose%EC%8B%9D-observation-%EC%82%AC%EA%B3%A0.md)
- [State changes need to be tracked by Compose](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/jetpack-compose-automatic-state-observation-for-flutter-developers/03-state-changes-need-to-be-tracked-by-compose.md)
- [Automatic State Observation의 실제 의미](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/jetpack-compose-automatic-state-observation-for-flutter-developers/04-automatic-state-observation%EC%9D%98-%EC%8B%A4%EC%A0%9C-%EC%9D%98%EB%AF%B8.md)
- [`remember`는 캐시보다 Composition 저장공간에 가깝다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/jetpack-compose-automatic-state-observation-for-flutter-developers/05-remember%EB%8A%94-%EC%BA%90%EC%8B%9C%EB%B3%B4%EB%8B%A4-composition-%EC%A0%80%EC%9E%A5%EA%B3%B5%EA%B0%84%EC%97%90-%EA%B0%80%EA%B9%9D%EB%8B%A4.md)
- [State Down, Events Up](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/jetpack-compose-automatic-state-observation-for-flutter-developers/06-state-down-events-up.md)
- [State는 가장 낮은 공통 owner에 둔다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/jetpack-compose-automatic-state-observation-for-flutter-developers/07-state%EB%8A%94-%EA%B0%80%EC%9E%A5-%EB%82%AE%EC%9D%80-%EA%B3%B5%ED%86%B5-owner%EC%97%90-%EB%91%94%EB%8B%A4.md)
- [ViewModel은 Composition보다 오래 사는 state holder다](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/jetpack-compose-automatic-state-observation-for-flutter-developers/08-viewmodel%EC%9D%80-composition%EB%B3%B4%EB%8B%A4-%EC%98%A4%EB%9E%98-%EC%82%AC%EB%8A%94-state-holder%EB%8B%A4.md)
- [영상 흐름 기준 해설](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/jetpack-compose-automatic-state-observation-for-flutter-developers/09-%EC%98%81%EC%83%81-%ED%9D%90%EB%A6%84-%EA%B8%B0%EC%A4%80-%ED%95%B4%EC%84%A4.md)
- [실무 판단 규칙](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/jetpack-compose-automatic-state-observation-for-flutter-developers/10-%EC%8B%A4%EB%AC%B4-%ED%8C%90%EB%8B%A8-%EA%B7%9C%EC%B9%99.md)
- [한 문장 요약](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/jetpack-compose-automatic-state-observation-for-flutter-developers/11-%ED%95%9C-%EB%AC%B8%EC%9E%A5-%EC%9A%94%EC%95%BD.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
