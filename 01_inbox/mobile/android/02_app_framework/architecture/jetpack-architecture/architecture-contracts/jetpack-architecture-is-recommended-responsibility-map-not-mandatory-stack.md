---
title: jetpack-architecture-is-recommended-responsibility-map-not-mandatory-stack
tags: [android, android/architecture, android/jetpack]
aliases: ["Jetpack Architecture는 필수 stack이 아니라 책임 분리 지도다"]
date modified: 2026-08-06 14:50:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Jetpack Architecture는 필수 stack이 아니라 책임 분리 지도다

안드로이드 공식 **Jetpack Architecture 권장 사항은 특정 프레임워크(Room, Hilt, Navigation 등)를 강제로 사용해야 하는 고정된 필수 기술 스택(Mandatory Stack)이 아니다.** 본질은 **관심사 분리(Separation of Concerns), 단방향 데이터 흐름(Unidirectional Data Flow), 데이터 단일 출처(Single Source of Truth) 원칙을 실현하기 위한 책임 분리 지도(Responsibility Map)**다.

---

### 1. 개념 및 핵심 명제 (What)

- **프레임워크 독립적 원칙**:
  `ViewModel` 대신 KMP 전용 StateHolder 를 쓸 수도 있고, `Room` 대신 `SQLDelight` 를 쓸 수 있으며, `Hilt` 대신 `Metro` 나 `Koin` 을 쓸 수 있다. 기술 스택이 바뀌어도 **UI 계층, 비즈니스 계층, 데이터 계층 간의 책임 경계**가 유지된다면 권장 아키텍처 원칙을 완벽히 준수하는 것이다.
- **수준별 유연한 아키텍처 설계**:
  간단한 도메인을 가진 화면은 Domain Layer(UseCase)를 생략하고 ViewModel 이 Repository 를 직접 참조할 수 있다. 필수 레이어는 **UI Layer 와 Data Layer** 이다.

---

### 2. 왜 유연한 지도(Map) 개념이어야 하는가? (Why)

1. **오버엔지니어링(Over-Engineering) 방지**: 단순 CRUD 앱에 무조건적인 UseCase 계층 및 과도한 데이터 모델 맵핑(DTO -> DomainEntity -> UiModel)을 적용하여 복잡도를 폭발시키는 잘못을 막는다.
2. **Multiplatform (KMP) 확장성 확보**: 안드로이드 전용 `androidx.lifecycle.ViewModel` 에 집착하지 않고 Kotlin 공통 모듈 기반 아키텍처로 유연하게 전환하기 위함이다.

---

### 3. 내부 메커니즘 (How)

```mermaid
graph LR
    subgraph Core Principles ["핵심 아키텍처 원칙 (Mandatory)"]
        SoC["Separation of Concerns"]
        UDF["Unidirectional Data Flow"]
        SSOT["Single Source of Truth"]
    end

    subgraph Flexible Implementations ["구현 기술 스택 (Flexible Choice)"]
        UI_Choice["Compose / Native View"]
        State_Choice["StateFlow / KMP StateHolder"]
        DI_Choice["Hilt / Koin / Metro / Manual DI"]
        DB_Choice["Room DB / SQLDelight / DataStore"]
    end

    Core Principles --> Flexible Implementations
```

---

### 4. 관측 가능 증거 및 진단 (Observability)

- **의존성 방향 단방향성 검증**:
  Data Layer 나 Domain Layer 모듈의 Gradle 빌드 파일(`build.gradle.kts`)에 UI/Android View 프레임워크 의존성이 없는지 컴파일 타임 검증.

---

### 5. 관련 문서 및 참조

- 상위 문서: [Architecture Contracts](./architecture-contracts.md)
- 관련 계약 문서:
  - [UI, domain, data layer는 rendering, policy, source of truth를 분리한다](./ui-domain-data-layers-separate-rendering-policy-and-source-of-truth.md)
  - [KMP는 공유 로직과 플랫폼 UI 또는 공유 UI를 선택할 수 있다](../../multiplatform-contracts/kmp-can-share-logic-with-native-ui-or-share-ui-with-compose-multiplatform.md)
- 공식 문서: [Guide to App Architecture - Architecture Principles](https://developer.android.com/topic/architecture#architecture-principles)

검증일: 2026-08-05. 아키텍처 유연성 및 책임 분리 가이드 원문 확인 완료.
