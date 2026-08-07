---
title: stateflow-and-sharedflow
tags: [android, coroutines, flow, kotlin, sharedflow, stateflow]
aliases: [StateFlow and SharedFlow, StateFlow와 SharedFlow]
date modified: 2026-08-07 13:44:13 +09:00
date created: 2026-08-06 16:35:00 +09:00
---

## StateFlow 와 SharedFlow (Kotlin Hot Stream)

### 1. 개요 (Overview)

Kotlin Coroutines 환경에서 **Cold Stream(구독 시점에 구동)** 과 달리, 데이터 생산자가 생성되는 즉시 데이터를 전송할 준비가 된 흐름을 **Hot Stream** 이라고 부르며, 대표적인 클래스로 **`StateFlow`** 와 **`SharedFlow`** 가 존재한다.

UI 상태 관리와 이벤트 전송을 분리하여 안드로이드 아키텍처의 반응형 데이터 흐름을 만드는 데 핵심적인 역할을 한다.

---

#### 초보자를 위한 쉽게 이해하는 비유

- **Cold Stream (`Flow`)**:
  - 주문이 들어와야 비로소 수도꼭지를 틀어 물을 보내주는 방식 (구독자가 없으면 아무 작업도 안 함).
- **Hot Stream (`StateFlow` / `SharedFlow`)**:
  - 중앙 라디오 방송국처럼 이미 계속 신호를 송출하고 있으며, 사용자가 라디오를 켜면(구독) 송출 중인 신호를 즉시 듣는 방식.

---

### 2. StateFlow 와 SharedFlow 의 역할 분담

- **`StateFlow`**: 화면의 현재 상태(`UiState`)를 항상 1 개 보관하고 있으며, 화면 회전이나 Recomposition 발생 시 UI 에 최신 상태를 끊김 없이 제공한다.
- **`SharedFlow`**: 화면 이동, Toast 메시지 팝업 등 일회성 비즈니스 이벤트를 구독자들에게 부하 없이 브로드캐스팅한다.

---

### 3. StateFlow 대 SharedFlow 의 상세 비교

두 Hot Stream 클래스 간의 초기값 필요 여부, `replay` 캐시 메커니즘 및 이벤트 유실 위험성에 관한 종합 비교표는 독립된 [StateFlow vs SharedFlow 비교 문서](stateflow-vs-sharedflow.md) 를 참고한다.

---

### 4. 연결 문서 (Related Links)

- [StateFlow vs SharedFlow 비교](stateflow-vs-sharedflow.md) - StateFlow 와 SharedFlow 의 특성 및 비유 비교표
- [ViewModel](viewmodel.md) - StateFlow 기반 상태 관리를 총괄하는 UI 아키텍처 컴포넌트
- [Single Source of Truth](single-source-of-truth.md) - UDF 데이터 흐름과 단일 진실 출처 원칙
