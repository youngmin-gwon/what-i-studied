---
title: B3-data-layer
tags: [android, data, flow, room, datastore, topic-synthesis]
aliases: [Data Layer Topic, 데이터 레이어 합성]
date modified: 2026-08-04 16:30:00 +09:00
date created: 2026-08-04 16:00:00 +09:00
---

## B3 · 데이터 레이어: Flow · Room · DataStore · Paging

> **이 문서의 목적**: 로컬 저장소, 네트워크, 그리고 앱의 UI 를 잇는 데이터 레이어의 역할을 이해한다. 데이터를 어떻게 비동기적으로 흐르게 하고 (Flow), 영구히 저장하며 (Room, DataStore), 대용량으로 가져올지 (Paging) 다룬다.

---

### 1. 데이터 레이어 아키텍처 (Repository 패턴)

데이터 레이어는 앱의 데이터 소스 (네트워크, DB, 캐시)를 추상화하고 도메인/UI 레이어에 일관된 인터페이스를 제공한다. Repository 는 하나 이상의 데이터 소스를 조율하여 단일 진실의 원천 (SSOT)을 보장하며, 비즈니스 로직과 데이터 접근 로직을 분리한다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [Repository는 Room과 DataStore를 Flow로 연결한다](../../02_app_framework/data/storage/persistence-contracts/repository-connects-room-and-datastore-as-flow.md) | Repository 의 데이터 통합과 스트림 노출 역할 |
| [데이터 레이어는 단일 진실의 원천을 제공한다](../../02_app_framework/data/architecture/data-layer-provides-single-source-of-truth.md) | 네트워크 캐시와 로컬 저장소 동기화 원칙 |

---

### 2. Kotlin Flow: 비동기 데이터 스트림

Kotlin Flow 는 비동기적으로 계산되는 데이터 스트림을 표현한다. Room 과 DataStore 모두 데이터 변경을 Flow 로 발행할 수 있다. Flow 는 콜드 (Cold) 스트림으로 수집 (collect)이 시작될 때만 활성화되며, 연산자를 통해 데이터를 매핑하고 필터링할 수 있다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [Kotlin Flow는 비동기 값의 순차적 스트림을 나타낸다](../../02_app_framework/data/async-flow/kotlin-flow-represents-sequential-stream-of-async-values.md) | suspend 와 Flow 의 결합 구조 |
| [데이터 스트림 변환은 연산자를 통해 이루어진다](../../02_app_framework/data/async-flow/data-stream-transformation-uses-operators.md) | map, filter, combine 의 동작 방식 |

---

### 3. StateFlow vs SharedFlow 선택 기준

Flow 를 UI 에 노출할 때는 핫 (Hot) 스트림인 `StateFlow` 나 `SharedFlow` 로 변환해야 한다. `StateFlow` 는 단일 최신 상태를 유지하고 초기값이 필수인 반면, `SharedFlow` 는 이벤트 (에러 메시지 등)를 여러 구독자에게 방송할 때 사용하며 상태를 유지하지 않는다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [StateFlow는 항상 최신 상태를 유지하는 Hot 스트림이다](../../02_app_framework/data/async-flow/flow-state-contracts/stateflow-maintains-latest-state.md) | 화면 상태(UiState) 표시에 최적화된 스트림 |
| [SharedFlow는 일회성 이벤트를 여러 구독자에게 방송한다](../../02_app_framework/data/async-flow/flow-state-contracts/sharedflow-broadcasts-one-time-events.md) | 스낵바, 네비게이션 트리거 등 일회성 신호 전달 |

---

### 4. Room: 로컬 데이터베이스

Room 은 SQLite 에 대한 추상화를 제공하여 강력한 타입 검사와 편의성을 더한 ORM 라이브러리다. 누적되고 복잡하게 조회되는 정형 데이터를 저장할 때 사용한다. DAO (Data Access Object)에서 반환 타입을 Flow 로 설정하면 테이블 변경 시 자동으로 새 데이터가 발행된다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [Room은 누적되고 조회되는 로컬 데이터를 저장한다](../../02_app_framework/data/storage/persistence-contracts/room-stores-accumulated-queryable-local-data.md) | Entity, DAO 설계 및 데이터베이스 접근 |
| [SQLite와 Room의 경계는 엔진과 애플리케이션 API의 차이다](../../02_app_framework/data/storage/persistence-contracts/sqlite-is-storage-engine-room-is-app-access-layer.md) | 추상화 계층의 이점과 직접 SQL 을 써야 하는 예외 |

---

### 5. DataStore: 설정/소규모 데이터 영속

DataStore 는 SharedPreferences 를 대체하는 비동기, 트랜잭션 안전 저장소다. Preferences DataStore 는 키-값 쌍을 저장하고, Proto DataStore 는 타입 안전성이 보장된 커스텀 객체를 저장한다. 복잡한 쿼리가 필요 없는 설정이나 인증 토큰 같은 작은 상태 저장에 적합하다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [DataStore는 작은 설정과 현재 상태를 저장한다](../../02_app_framework/data/storage/persistence-contracts/datastore-stores-small-settings-and-current-state.md) | SharedPreferences 대비 동시성 문제 해결 |
| [DataStore와 Room 마이그레이션은 저장소 계약의 시간 경계다](../../02_app_framework/data/storage/persistence-contracts/datastore-and-room-migrations-are-time-boundaries.md) | 스키마 변경과 데이터 마이그레이션 전략 |
| [Android 저장소는 데이터 수명과 소유권으로 선택한다](../../02_app_framework/data/storage/persistence-contracts/choose-storage-by-data-lifetime-and-ownership.md) | 저장 매체별 적합한 데이터 타입 구분 |

---

### 6. Paging 3: 대용량 목록 로딩

대용량 리스트를 한 번에 메모리에 올리면 OOM 이 발생한다. Paging 3 라이브러리는 Room 이나 네트워크로부터 데이터를 청크(페이지) 단위로 요청하고 캐싱하여 RecyclerView 나 Compose LazyList 에 효율적으로 전달한다. 

| 원자 노트 | 핵심 명제 |
|---|---|
| [Paging 3은 데이터 청크를 점진적으로 로드하고 캐싱한다](../../02_app_framework/data/paging/paging3-loads-and-caches-data-chunks.md) | Pager, PagingConfig, PagingData 의 역할 |
| [RemoteMediator는 로컬 DB와 네트워크 캐시를 동기화한다](../../02_app_framework/data/paging/remotemediator-synchronizes-local-db-and-network.md) | 오프라인 우선 Paging 아키텍처 |

---

### 7. 네트워크 레이어와 연동

데이터 레이어의 또 다른 주축은 네트워크 통신이다. Retrofit 과 OkHttp 를 이용해 서버와 통신하며, 이 결과를 다시 Room 에 저장하거나 Flow 로 변환해 UI 로 전달한다. 네트워크 상태에 따른 에러 처리와 재시도 로직은 Repository 내부에 캡슐화된다.

| 원자 노트 | 핵심 명제 |
|---|---|
| [네트워크 응답은 안전한 Result 래퍼로 변환된다](../../02_app_framework/data/network/network-responses-are-converted-to-safe-result-wrappers.md) | 성공과 실패를 명시적으로 다루는 Result 클래스 패턴 |
| [Interceptor는 요청과 응답을 가로채어 공통 정책을 적용한다](../../02_app_framework/data/network/interceptor-applies-common-policies-to-requests.md) | 헤더 추가, 인증 갱신, 로깅의 중앙화 |

---

### 이 주제와 연결된 Worked Example

| Worked Example | 연결 포인트 |
|---|---|
| [WE 05 · Process Death Recovery Simulation](../worked-examples/05-process-death-recovery-simulation.md) | 프로세스 강제 종료 후 Room 과 DataStore 에서 상태를 재구성 |
| [WE 06 · Offline First Sync Strategy](../worked-examples/06-offline-first-sync-strategy.md) | Room 과 RemoteMediator 를 활용한 오프라인 동기화 |

---

### 이 주제와 연결된 Diagnostic Runbook

| Runbook | 연결 포인트 |
|---|---|
| [RB 03 · State Loss & Process Death](../diagnostic-runbooks/03-state-loss-and-process-death.md) | 데이터 손실 및 비동기 상태 복구 지연 트러블슈팅 |
| [RB 05 · Network Timeout & Retry](../diagnostic-runbooks/05-network-timeout-and-retry.md) | 불안정한 네트워크 환경에서의 재시도 및 로컬 캐시 활용 |

---

### 더 깊이 들어갈 때 (Learning Spine)

- **Chapter 04 · UI Layer** — Flow 스트림이 Compose 의 `collectAsStateWithLifecycle()` 로 소비되는 과정
- **Chapter 05 · Architecture** — Repository 패턴과 의존성 주입(Hilt) 결합
- **Chapter 09 · Security** — DataStore 암호화 및 안전한 토큰 보관
