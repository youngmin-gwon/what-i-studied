---
title: android-viewmodel
tags: []
aliases: []
date modified: 2026-04-05 17:43:19 +09:00
date created: 2026-03-21 16:47:09 +09:00
---

## [[mobile-security]] > [[android-viewmodel]]

### ViewModel: State Preservation

안드로이드 UI 상태를 유지하고 비즈니스 로직을 캡슐화하는 **ViewModel**의 아키텍처와 내부 동작을 분석합니다.

단순히 데이터를 저장하는 공간을 넘어, 화면 회전 등의 설정 변경(Configuration Changes) 시에도 데이터가 어떻게 보존되는지, 그리고 [[android-coroutines-flow]] 와 어떻게 유기적으로 결합되는지 이해하는 것이 목표입니다.

---

---

## 원자 노트

- [[01-context-ui-와-데이터의-분리|💡 Context: UI 와 데이터의 분리]]
- [[02-viewmodel-의-목적|ViewModel 의 목적]]
- [[03-viewmodel-생명주기|ViewModel 생명주기]]
- [[04-기본-구현|기본 구현]]
- [[05-savedstatehandle|SavedStateHandle]]
- [[06-viewmodelscope-와-코루틴|ViewModelScope 와 코루틴]]
- [[07-상태-관리-livedata-vs-stateflow|상태 관리: LiveData vs StateFlow]]
- [[08-factory-패턴|Factory 패턴]]
- [[09-모범-사례|모범 사례]]
- [[10-안티패턴|안티패턴]]
- [[android-viewmodel-11-디버깅|디버깅]]
- [[android-viewmodel-12-테스팅|테스팅]]
- [[13-see-also|See Also]]

---

## 정리 기준

이 노트는 원래 긴 가이드였고, H4 섹션을 별도 원자 노트로 분리했습니다.
기존 링크 호환을 위해 이 파일은 허브 노트로 유지합니다.
