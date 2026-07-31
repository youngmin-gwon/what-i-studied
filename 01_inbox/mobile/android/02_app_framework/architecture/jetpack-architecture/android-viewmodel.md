---
title: android-viewmodel
tags: []
aliases: []
date modified: 2026-04-05 17:43:19 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [mobile-security](01_inbox/mobile/mobile-security.md) > [android-viewmodel](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel.md)

### ViewModel: State Preservation

안드로이드 UI 상태를 유지하고 비즈니스 로직을 캡슐화하는 **ViewModel**의 아키텍처와 내부 동작을 분석합니다.

단순히 데이터를 저장하는 공간을 넘어, 화면 회전 등의 설정 변경(Configuration Changes) 시에도 데이터가 어떻게 보존되는지, 그리고 [android-coroutines-flow](01_inbox/mobile/android/02_app_framework/data/async-flow/android-coroutines-flow.md) 와 어떻게 유기적으로 결합되는지 이해하는 것이 목표입니다.

---

---

## 원자 노트

- [💡 Context: UI 와 데이터의 분리](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel/01-context-ui-%EC%99%80-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%9D%98-%EB%B6%84%EB%A6%AC.md)
- [ViewModel 의 목적](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel/02-viewmodel-%EC%9D%98-%EB%AA%A9%EC%A0%81.md)
- [ViewModel 생명주기](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel/03-viewmodel-%EC%83%9D%EB%AA%85%EC%A3%BC%EA%B8%B0.md)
- [기본 구현](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel/04-%EA%B8%B0%EB%B3%B8-%EA%B5%AC%ED%98%84.md)
- [SavedStateHandle](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel/05-savedstatehandle.md)
- [ViewModelScope 와 코루틴](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel/06-viewmodelscope-%EC%99%80-%EC%BD%94%EB%A3%A8%ED%8B%B4.md)
- [상태 관리: LiveData vs StateFlow](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel/07-%EC%83%81%ED%83%9C-%EA%B4%80%EB%A6%AC-livedata-vs-stateflow.md)
- [Factory 패턴](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel/08-factory-%ED%8C%A8%ED%84%B4.md)
- [모범 사례](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel/09-%EB%AA%A8%EB%B2%94-%EC%82%AC%EB%A1%80.md)
- [안티패턴](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel/10-%EC%95%88%ED%8B%B0%ED%8C%A8%ED%84%B4.md)
- [디버깅](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel/android-viewmodel-11-%EB%94%94%EB%B2%84%EA%B9%85.md)
- [테스팅](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel/android-viewmodel-12-%ED%85%8C%EC%8A%A4%ED%8C%85.md)
- [See Also](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-viewmodel/13-see-also.md)

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
