---
title: viewmodel
tags: [android, architecture, ssot, viewmodel]
aliases: [ViewModel 아키텍처 노드]
date modified: 2026-08-06 18:35:51 +09:00
date created: 2026-07-31 23:04:26 +09:00
---

## ViewModel (아키텍처 레이어 지침)

### 1. 개요

이 노드는 아키텍처 상태 관리 레이어 내 ViewModel 지침 문서입니다. Android ViewModel 의 5 단계 초보자 비유, 구성 변경(Configuration Change) 생존 원리, 내부 수명주기 및 코드 예시는 단일 진실 출처(SSOT)인 [ViewModel 표준 레퍼런스](../../../viewmodel.md) 를 참고하십시오.

---

### 2. ViewModel 관련 5 대 원자 계약 (Atomic Contracts)

- [ViewModel 표준 레퍼런스](../../../viewmodel.md) - ViewModel 단일 진실 출처 (SSOT)
- [ViewModel Read-Only State 규칙](viewmodel-exposes-read-only-state.md)
- [ViewModel 과 UI Controller/Context 분리 규칙](viewmodel-does-not-retain-ui-controller-or-context.md)
- [ViewModel 구성 변경 생존 규칙](viewmodel-survives-configuration-change-not-process-death.md)
- [viewModelScope 수명주기 규칙](viewmodelscope-binds-external-work-to-viewmodel-lifetime.md)
- [ViewModel 화면 상태 조율 규칙](viewmodel-orchestrates-screen-state-and-external-work.md)
