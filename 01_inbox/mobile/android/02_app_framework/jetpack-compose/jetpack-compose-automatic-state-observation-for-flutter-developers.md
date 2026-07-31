# Compose Automatic State Observation: Flutter 개발자 관점

이 문서는 Android Developers 영상
[A Compose State of Mind - Using Jetpack Compose's Automatic State Observation](https://www.youtube.com/watch?v=rmv2ug-wW4U)
의
핵심을 Flutter 개발자 관점에서 정리합니다.

이 문서의 범위는 `remember`, `mutableStateOf`, ViewModel API 사용법 자체가 아니라, Compose Runtime이 상태를 어떻게 관찰하고
recomposition 범위를 어떻게 결정하는지 이해하는 것입니다. API 선택은
[[jetpack-compose-state-management-flutter-comparison]]와
[[jetpack-compose-state-lifetime-api-selection]]를 기준으로 봅니다.

관련 공식 문서:

- [Thinking in Compose](https://developer.android.com/develop/ui/compose/mental-model)
- [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
- [State hoisting](https://developer.android.com/develop/ui/compose/state-hoisting)
- [Side-effects in Compose](https://developer.android.com/develop/ui/compose/side-effects)

---

---

## 원자 노트

- [[01-이-영상의-핵심|이 영상의 핵심]]
- [[02-flutter식-rebuild-사고와-compose식-observation-사고|Flutter식 rebuild 사고와 Compose식 observation 사고]]
- [[03-state-changes-need-to-be-tracked-by-compose|State changes need to be tracked by Compose]]
- [[04-automatic-state-observation의-실제-의미|Automatic State Observation의 실제 의미]]
- [[05-remember는-캐시보다-composition-저장공간에-가깝다|`remember`는 캐시보다 Composition 저장공간에 가깝다]]
- [[06-state-down-events-up|State Down, Events Up]]
- [[07-state는-가장-낮은-공통-owner에-둔다|State는 가장 낮은 공통 owner에 둔다]]
- [[08-viewmodel은-composition보다-오래-사는-state-holder다|ViewModel은 Composition보다 오래 사는 state holder다]]
- [[09-영상-흐름-기준-해설|영상 흐름 기준 해설]]
- [[10-실무-판단-규칙|실무 판단 규칙]]
- [[11-한-문장-요약|한 문장 요약]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H2 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
