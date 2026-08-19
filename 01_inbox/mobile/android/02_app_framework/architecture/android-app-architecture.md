---
title: android-app-architecture
tags: [android, android/architecture]
aliases: ["Android 앱 아키텍처는 UI 패턴보다 수명과 OS 진입점을 나누는 문제다", "Android App Architecture"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## Android 앱 아키텍처는 UI 패턴보다 수명과 OS 진입점을 나누는 문제다

안드로이드 앱 아키텍처 설계의 본질은 MVVM, MVI 와 같은 단순 화면 표시 패턴 선택에 있지 않다. **운영체제(OS)가 관리하는 다중 프로세스/컴포넌트 진입점(Activity, Service, Receiver, Provider)과 상태 소유자(Owner)의 수명 주기(Lifecycle), 그리고 프로세스 데스(Process Death)에 대응하는 영속성 계약(Persistence Contract)을 결정하는 문제**다.

---

### 1. 개념 및 핵심 구조 (What)

안드로이드 권장 아키텍처(Guide to App Architecture)는 모듈성과 테스트 용이성을 극대화하기 위해 다음과 같이 관심사(Separation of Concerns)를 3개의 핵심 레이어로 분리한다.

```mermaid
graph TD
    subgraph UI Layer ["UI Layer (Single Activity + Compose Window)"]
        UI["Compose UI (Declarative Render)"]
        VM"StateHolder / [viewmodel (UiState Provider)"]
    end
    
    subgraph Domain Layer ["Domain Layer (Optional Business Logic)"]
        UC["UseCases (Pure Business Rules)"]
    end
    
    subgraph Data Layer "Data Layer ([single source of truth)"]
        Repo["Repository (Data Aggregation & Caching)"]
        LocalDS["Local DataSource (Room DB / DataStore)"]
        RemoteDS["Remote DataSource (Ktor / Retrofit API)"]
    end

    UI -->|"Sends User Actions"| VM
    VM -->|"Exposes stateflow"| UI
    VM --> UC
    UC --> Repo
    VM --> Repo
    Repo --> LocalDS
    Repo --> RemoteDS

    style UI Layer fill:#e1f5fe,stroke:#01579b,stroke-width:2f
    style Data Layer fill:#e8f5e9,stroke:#1b5e20,stroke-width:2f
```

- **UI Layer**: 선언형 UI(Jetpack Compose)와 관찰 가능한 UI State(`StateFlow`)를 연결하며, 사용자 액션을 상위 StateHolder 로 전달한다.
- **Domain Layer**: 캡슐화된 순수 비즈니스 로직(UseCase)을 소유하며, Android API 의존성을 갖지 않는다.
- **Data Layer**: 데이터의 **단일 출처(Single Source of Truth)**로서, 로컬 캐시(Room, DataStore)와 원격 API 데이터 간의 동기화 및 맵핑을 담당한다.

---

### 2. 왜 수명과 OS 진입점이 아키텍처의 중심인가? (Why)

1. **OS 의 불시 프로세스 회수 (Process Death)**:
   사용자가 앱을 백그라운드로 전환했을 때 메모리가 부족하면 OS 는 언제든 앱 프로세스를 종료할 수 있다. ViewModel 은 회전(Configuration Change) 시에는 살아남지만 프로세스 데스 시 파기되므로, 아키텍처 관점에서 `SavedStateHandle` 및 Data Layer 영속 저장이 필수적이다.
2. **다중 시스템 진입점 (System Entry Points)**:
   안드로이드 앱은 단일 `main()` 함수로 실행되지 않으며, Deep Link, Notification, Alarm, App Widget 등 다양한 OS 컴포넌트를 통해 앱 프로세스가 독립적으로 기상하고 진입할 수 있다.

---

### 3. 상태 수명 및 복구 전략 (How)

| 복구 시나리오 | ViewModel 인메모리 상태 | SavedStateHandle | Persistent Storage (Room/DataStore) |
| :--- | :---: | :---: | :---: |
| **화면 회전 (Configuration Change)** | ✅ 보존 | ✅ 보존 | ✅ 보존 |
| **프로세스 데스 (Process Death)** | ❌ 파기 | ✅ 보존 (소량의 ID/검색어) | ✅ 보존 (전체 복구) |
| **앱 강제 종료 / 재부팅** | ❌ 파기 | ❌ 파기 | ✅ 보존 |

---

### 4. 서브 아키텍처 영역 지도

- [Jetpack Architecture Map](./jetpack-architecture/android-jetpack-architecture-map.md)
- [App Component Contracts](./app-components/app-component/app-component.md)
- [Android Context Boundaries](./context-and-modularity/android-context-boundaries.md)
- [Android State Management](./state-management/android-state-management.md)
- [Multiplatform Contracts](./multiplatform/multiplatform.md)

---

### 5. 관측 가능 증거 및 진단 (Observability)

- **Doze 모드 및 Process Death 강제 테스트**:
  ```bash
  adb shell am kill <package_name>
  ```
  *(앱 백그라운드 전환 후 프로세스 강제 사멸 시 재진입 시 상태 복구 여부 진단)*

---

### 6. 참고 및 공식 문서

- 공식 가이드: [Guide to App Architecture](https://developer.android.com/topic/architecture)

검증일: 2026-08-05. 안드로이드 아키텍처 가이드 3-Layer 구조 원문 검증 완료.
