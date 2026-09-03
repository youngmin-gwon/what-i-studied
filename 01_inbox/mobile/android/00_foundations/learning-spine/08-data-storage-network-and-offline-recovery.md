---
title: 08-data-storage-network-and-offline-recovery
tags: ["android", "android/foundations", "learning-spine"]
aliases: ["Data, storage, network, and offline recovery"]
date modified: 2026-08-04 10:10:43 +09:00
date created: 2026-08-03 22:30:00 +09:00
---

## 데이터, 저장소, 네트워크와 offline recovery

7 장은 입력과 configuration 이 UI 상태를 거쳐 화면 프레임이 되는 경로를 다뤘다. 그러나 그 화면이 보여주는 데이터 자체가 어디에서 오고, 네트워크가 끊기거나 프로세스가 죽어도 유실되지 않으려면 무엇이 필요한지는 아직 다루지 않았다. 이 장은 그 질문을 다룬다.

이 장의 핵심 질문은 다음과 같다.

>화면이 보여주는 데이터는 어느 owner 가 보존하고, 네트워크 실패나 프로세스 종료 이후에는 어떻게 복구되는가?

이 장은 Room 이나 DataStore 의 API 사용법을 처음부터 가르치지 않는다. 개별 저장소 API 의 상세는 원자 노트가 다루는 수준으로 남겨두고, 여기서는 UI 이벤트에서 시작해 로컬 저장소, 지속 가능한 동기화, 서버 반영을 거쳐 다시 UI 관찰로 돌아오는 순환을 하나로 연결한다.

### 1. 화면이 보는 데이터는 화면이 소유하지 않는다

5 장은 `ViewModel` 이 configuration change 는 견디지만 process death 는 견디지 못한다는 것을 다뤘다. 이 사실은 하나의 결론으로 이어진다. 사용자에게 의미 있는 데이터를 `ViewModel` 이나 화면의 메모리 상태에만 두면 안 된다는 것이다.

Repository 는 데이터의 출처와 갱신 방식을 감추고 관찰 가능한 원천 데이터를 `Flow` 로 노출한다. `ViewModel` 은 이 흐름을 화면이 이해할 수 있는 `UiState` 로 변환하고, 화면은 그 결과만 관찰한다. 화면은 데이터베이스나 네트워크의 존재를 알 필요가 없다. 이 구조에서 화면이 사라지거나 다시 만들어져도, 심지어 process death 이후 새 프로세스가 다시 이 흐름을 구독해도, 실제 데이터는 여전히 Repository 아래의 저장소에 남아 있다.

### 2. 저장소는 데이터의 수명과 소유권으로 고른다

저장소 선택은 API 이름을 고르는 문제가 아니라 다음을 먼저 묻는 문제다.

- 앱 프로세스가 끝나도 이 값이 남아야 하는가?
- 값 하나를 읽는가, row 가 계속 쌓이는가?
- 검색, 정렬, 관계 무결성이 필요한가?

| 데이터 성격 | 우선 선택 |
| --- | --- |
| 현재 세션, 설정, 작은 상태 | DataStore |
| 누적되는 구조화 데이터 | Room |
| 앱 전용 바이너리나 임시 파일 | app-specific files |
| 사용자가 고르고 다른 앱과 공유할 파일 | Storage Access Framework / MediaStore |

메모리 상태는 화면이나 프로세스 수명에만 속한다. DataStore 와 Room 은 프로세스가 재시작돼도 남는다. 이 구분이 있어야 "왜 이 값은 process death 뒤에도 남고 저 값은 사라지는가"라는 질문에 저장소 선택으로 답할 수 있다.

### 3. 로컬에 먼저 쓰고, 서버 반영은 별도 작업으로 미룬다

로컬 데이터베이스를 화면의 유일한 관찰 대상으로 두는 원칙은 공식 아키텍처 문서에서도 명시한다.

>"The local data source is the canonical source of truth for the app. It should be the exclusive source of any data that higher layers of the app read. This ensures data consistency between connection states."
>
>"Write any updates to the local data source first, so that the local data source updates its consumers since it is observable."

이 원칙에서 자연스럽게 나오는 패턴이 공식 문서가 "lazy writes"라고 부르는 것이다.

>"Write to the local data source first, then queue the write to notify the network at the earliest opportunity."

사용자가 오프라인에서 어떤 작업을 하면, 그 변경은 먼저 로컬 저장소에 반영되고, 서버에 알려야 한다는 사실은 별도의 대기 작업(흔히 outbox 라고 부르는 패턴)으로 기록된다. 이 두 단계는 하나의 원자적 트랜잭션이 아니다. 로컬 쓰기는 즉시 끝나고, 서버 반영은 네트워크가 돌아왔을 때 별도로 처리되는 지연된 사건이다. 두 저장소(예: Room 과 DataStore)에 걸쳐 쓰기가 필요하다면, 그 쓰기들을 하나의 원자적 트랜잭션이라고 가정해서는 안 되며 실패 순서와 재시도 정책을 명시해야 한다.

### 4. 지속 가능한 재시도는 process death 와 중복 실행을 정상 조건으로 놓는다

이 "서버에 알리는" 작업은 화면의 lifetime 에 묶으면 안 된다. 6 장에서 본 것처럼 WorkManager 는 이 요청을 메모리가 아니라 내부 DB 에 저장하기 때문에 화면이 사라지거나 프로세스가 재시작돼도 남아 있다. 공식 문서는 이런 지연된 동기화 작업을 WorkManager 의 대표적인 용도로 제시한다.

>"If the synchronization fails, the doWork() method returns with Result.retry(). WorkManager will automatically retry synchronization with exponential backoff."

하지만 재시도가 자동으로 이뤄진다는 사실이 곧 안전하다는 뜻은 아니다. 재시도는 같은 요청이 여러 번 서버에 도착할 수 있다는 뜻이기도 하다. 그래서 지속 가능한 동기화를 설계할 때는 다음을 정상 조건으로 놓아야 한다.

- 프로세스가 도중에 죽어 완료 콜백이 오지 않을 수 있다.
- 같은 작업이 최소 한 번(at-least-once) 다시 실행될 수 있다.
- 이전 실행이 어디까지 끝났는지 다시 확인해야 한다.

실무 규칙은 다음과 같다. enqueue 전에 논리 작업 ID 와 재개 지점을 저장소에 남기고, 실행기는 그 상태를 다시 읽어 서버의 idempotency key 나 원자적 상태 전이로 중복 결과를 막는다. `onStopped()` 나 coroutine 취소로 자원을 정리하되, 프로세스가 강제 종료되면 이런 콜백조차 호출되지 않을 수 있으므로 콜백만 믿지 말고 checkpoint 를 먼저 저장해야 한다. 이 규칙은 5 장의 "process death 는 정리 콜백을 보장하지 않는다"는 사실을 데이터 동기화 영역에 적용한 것이다.

### 5. 네트워크가 연결됐다는 사실이 요청이 성공한다는 뜻은 아니다

앱은 `ConnectivityManager` 가 제공하는 `Network`, `NetworkCapabilities` 같은 상태를 통해 연결성을 판단하지만, 이는 system_server 의 `ConnectivityService` 가 계산하는 상태를 앱 쪽 API 로 옮겨 온 것이다. 실제 라우팅, DNS, 방화벽 정책은 native service(`netd`)와 그 아래 kernel/HAL 이 집행한다. 앱 코드가 직접 바꿀 수 있는 것은 이 중 첫 번째 계층뿐이다.

그래서 "네트워크가 연결돼 있다"는 신호와 "이 요청이 실제로 서버까지 도달해 성공한다"는 결과는 다른 문제다. metered 상태, VPN, private DNS, captive portal, 서버 지연은 모두 "연결됨" 상태와는 별개로 요청을 실패시킬 수 있다. 동기화 실패를 조사할 때는 앱이 본 네트워크 상태와 시스템이 실제로 적용한 정책 상태를 같은 시점에서 대조해야 한다.

### 6. 로컬과 서버 상태가 다를 때, 관찰 정책이 그 차이를 어떻게 다루는지 정한다

cold `Flow` 를 화면과 공유되는 `StateFlow` 로 바꾸는 `stateIn` 은 단순한 타입 변환이 아니라 언제 시작하고 언제 멈출지를 정하는 설계다. `WhileSubscribed(5_000)` 처럼 구독자가 없어진 뒤 일정 시간 후 upstream 을 멈추는 정책은, 화면 회전 같은 짧은 구독 공백에서 불필요한 재구독을 줄인다. 반대로 백그라운드에서도 최신 상태를 유지해야 한다면 화면 수명보다 긴 공유 범위가 필요하다.

이 선택은 5 절의 동기화 결과가 화면에 언제 반영되는지와도 연결된다. 화면이 로컬 저장소를 계속 관찰하고 있다면, 동기화 작업이 로컬 값을 갱신하는 순간 화면은 별도의 새로고침 없이 그 값을 반영한다. 이것이 "로컬 저장소를 유일한 source of truth 로 둔다"는 1 절 원칙의 실제 효과다.

다만 이 관찰 정책은 화면에 "언제" 값을 보여줄지를 정할 뿐, 오프라인 중 로컬에서 바꾼 값과 그사이 서버에 반영된 값이 실제로 다를 때 "어느 값이 맞는지"까지 정하지는 않는다. 이것이 진짜 충돌(conflict)이다. 공식 문서는 이 문제를 다음과 같이 설명한다.

>"If, when offline, the app writes data locally that is misaligned with the network data source, you must resolve the conflict before synchronization can happen."
>
>"Conflict resolution often requires versioning… The network data source then has the responsibility of providing the absolute source of truth…. a common approach is 'last write wins.'"

즉 로컬 저장소가 화면의 유일한 관찰 대상이라는 원칙과, 서버가 최종적으로 무엇이 맞는 값인지 판정하는 권한을 갖는다는 것은 서로 다른 층위의 이야기다. 화면은 로컬 값을 그대로 보여주지만, 동기화 시점에 서버가 "last write wins" 같은 정책으로 그 값을 그대로 받아들이거나 되돌릴 수 있다. 이 경우 로컬 값과 서버가 확정한 값 사이의 간극은 다시 동기화 결과로 로컬 저장소에 반영돼야 하며, 이는 4 절에서 다룬 idempotent 재시도·checkpoint 설계와 같은 원리를 공유한다.

### Worked example: 오프라인에서 즐겨찾기를 추가한다

1. 사용자가 오프라인 상태에서 "즐겨찾기 추가" 버튼을 누른다.
2. Repository 는 이 변경을 먼저 로컬 데이터베이스에 반영한다(3 절의 lazy write). 동시에 "서버에 아직 알리지 못한 변경"이라는 대기 상태를 함께 기록한다.
3. 화면은 로컬 데이터베이스를 관찰하는 `Flow` 를 통해 이 변경을 즉시 반영한다. 사용자는 네트워크 상태와 무관하게 결과를 바로 본다.
4. 이 동기화 요청은 화면의 lifetime 이 아니라 WorkManager 에 위임된다. 네트워크 constraint 가 만족되기를 기다린다.
5. 사용자가 화면을 벗어나거나 프로세스가 종료돼도 이 요청은 영속 저장소에 남아 있으므로 사라지지 않는다.
6. 네트워크가 돌아오면 WorkManager 가 이 작업을 실행한다. 이전에 이미 부분적으로 시도됐을 수 있으므로, 서버에는 idempotency key 로 중복 반영을 방지한다.
7. 성공하면 대기 상태를 지운다. 영구 오류(예: 인증 거부)라면 재시도 대신 실패로 표시하고 사용자에게 알릴 상태로 남긴다.

이 흐름 전체에서 화면 코드는 2 단계와 3 단계만 직접 다룬다. 나머지는 Repository 와 WorkManager 의 책임이다.

### 실패 사례: 두 저장소 쓰기를 하나의 트랜잭션으로 착각한다

Room 에 새 항목을 쓰고 DataStore 의 "마지막 동기화 시각"을 갱신하는 코드가 있다고 하자. 두 쓰기 사이에 프로세스가 종료되면, Room 쓰기는 성공했지만 DataStore 갱신은 실패한 채로 남을 수 있다. 이 둘을 하나의 트랜잭션으로 가정하고 설계하면, 다음 실행에서 "동기화가 이미 끝났다"고 잘못 판단하거나 반대로 이미 반영된 데이터를 중복 처리할 수 있다. 여러 저장소에 걸친 쓰기가 필요하다면 어느 쪽이 먼저 반영돼도 안전한 순서인지, 실패했을 때 무엇을 기준으로 재시도할지 미리 정해야 한다.

### 조사 방법: 동기화 실패를 분류한다

1. **로컬 값이 맞는가, 서버 값이 맞는가?** 화면에 보이는 값의 출처(로컬 캐시 vs 방금 받은 서버 응답)를 먼저 구분한다.
2. **동기화 작업이 실제로 예약됐는가?** `WorkInfo.state` 나 `dumpsys jobscheduler` 로 대기 중인지, constraint 미충족으로 멈춰 있는지 확인한다.
3. **앱이 본 네트워크 상태와 시스템 정책이 같은가?** `dumpsys connectivity`, `dumpsys netpolicy` 로 대조한다.
4. **재시도가 중복 부작용을 만들지 않는가?** 서버 idempotency key 나 로컬 checkpoint 가 실제로 중복 반영을 막고 있는지 확인한다.

### 반드시 교정해야 할 오해

| 오해 | 교정 |
| --- | --- |
| ViewModel 에 최신 데이터를 담아 두면 데이터가 안전하게 보존된다. | ViewModel 은 process death 를 견디지 못하므로 의미 있는 데이터는 Repository/저장소가 source of truth 여야 한다. |
| 로컬 쓰기와 서버 동기화는 사실상 한 번의 저장 동작이다. | 공식 아키텍처는 이를 "local 우선 쓰기 + 지연된 네트워크 알림"이라는 별도 단계(lazy writes)로 분리한다. |
| WorkManager 가 재시도해 주니 중복 실행은 걱정할 필요가 없다. | 재시도는 같은 요청이 여러 번 도달할 수 있다는 뜻이며, idempotency 와 checkpoint 없이는 중복 부작용이 생긴다. |
| 네트워크가 연결됐다고 표시되면 요청은 성공해야 한다. | 앱 API 가 보는 연결 상태와 시스템이 실제로 적용하는 라우팅·정책·서버 상태는 다른 계층이며 함께 대조해야 한다. |
| 화면이 새로고침 버튼을 눌러야 최신 데이터를 본다. | 화면이 로컬 저장소를 Flow 로 계속 관찰하고 있다면 동기화 결과는 별도 새로고침 없이 반영된다. |
| 두 저장소에 걸친 쓰기는 자동으로 원자적으로 처리된다. | Room 과 DataStore 같은 서로 다른 저장소의 쓰기는 각자의 트랜잭션 의미를 가지며 하나의 원자적 작업으로 가정하면 안 된다. |

### 확인 질문

1. 화면이 데이터를 직접 소유하면 안 되는 이유는 5 장의 어떤 사실과 연결되는가?
2. 저장소를 고를 때 먼저 물어야 할 질문은 무엇인가?
3. "lazy writes"는 로컬 쓰기와 서버 동기화를 어떻게 분리하는가?
4. process death 와 중복 실행을 정상 조건으로 놓아야 하는 이유는 무엇이며, 이는 6 장의 어떤 사실과 연결되는가?
5. 앱이 보는 네트워크 상태와 시스템이 실제로 적용하는 정책 상태는 왜 구분해야 하는가?
6. `stateIn` 의 공유 정책은 동기화 결과가 화면에 반영되는 시점과 어떤 관계가 있는가?
7. 오프라인 즐겨찾기 추가 사례에서 화면 코드가 직접 책임지는 단계는 어디까지인가?
8. 두 저장소에 걸친 쓰기를 하나의 트랜잭션으로 가정하면 어떤 문제가 생기는가?

### 다음 장으로 이어지는 질문

이 장은 데이터가 어느 owner 에 의해 보존되고 실패 이후 어떻게 복구되는지를 다뤘다. 그러나 권한이 있어 보이는데도 호출이 실패하는 이유, 그리고 identity 와 보안 경계가 어떻게 API 마다 다르게 적용되는지는 아직 다루지 않았다.

다음 장에서는 package/signing identity, 사용자별 UID 와 permission, AppOps, SELinux, server authorization 이 왜 하나의 순차 파이프라인이 아니라 API 와 자원마다 독립적으로 조합되는 gate 인지를 다룬다.

- 3 장이 다룬 package/서명 identity 와 사용자별 UID 는 권한 판정에 어떻게 연결되는가?
- 같은 permission 을 가졌는데도 호출이 실패하는 경우는 왜 생기는가?
- 어떤 실패가 앱 코드, framework policy, kernel/platform policy 중 어디에 속하는지 어떻게 구분하는가?

### 관련 정본

- [Repository는 Room과 DataStore를 Flow로 연결한다](../../02_app_framework/data/storage/repository-flow-integration.md)
- [Android 저장소는 데이터 수명과 소유권으로 선택한다](../../02_app_framework/data/storage/persistence-lifetime-selection.md)
- [Android Data Layer는 데이터 흐름과 영속 저장소, Paging을 분리한다](../../02_app_framework/data/android-data-layer-map.md)
- [Repository는 데이터 흐름을 Flow로 제공하고 ViewModel은 화면 상태로 조합한다](../../02_app_framework/async-flow/flow-state/repository-viewmodel-flow-composition.md)
- [Flow를 StateFlow로 바꿀 때는 stateIn의 수명과 공유 정책을 명시한다](../../02_app_framework/async-flow/flow-state/flow-statein-policy.md)
- [WorkManager는 지연 가능한 보장 작업의 기본 선택이다](../../04_system_services/background-and-notifications/work-manager.md)
- [백그라운드 실행 수단은 실패 비용으로 결정한다](../../04_system_services/background-and-notifications/background-api-selection.md)
- [백그라운드 제한은 작업 상태를 영속적으로 설계하게 만든다](../../04_system_services/background-and-notifications/background-restrictions-state.md)
- [Android 연결성과 네트워크 지도](../../01_system_internals/connectivity/android-connectivity.md)
- [네트워크 디버깅은 앱 API 상태와 system network state를 대조한다](../../01_system_internals/connectivity/network-debugging.md)
- [프로세스 종료 복구에는 saved state와 영속 source of truth가 필요하다](../../02_app_framework/architecture/app-components/process-death-state-recovery.md)

### 공식 근거

- [App architecture: Data layer](https://developer.android.com/topic/architecture/data-layer)
- [Build an offline-first app](https://developer.android.com/topic/architecture/data-layer/offline-first)
- [Persistent work with WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager)
- [Background tasks overview](https://developer.android.com/develop/background-work/background-tasks)

검증일: 2026-08-03. offline-first 문서의 "lazy writes" 예시 코드와 conflict 처리 세부는 앱마다 다를 수 있으므로 실제 설계 시점에 원문을 다시 확인한다.
