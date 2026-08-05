---
title: remember-saveable-is-for-small-restorable-ui-state
tags: ["android", "android/app-framework"]
aliases: []
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-07-31 16:53:16 +09:00
---

## Composable 수명보다 오래 필요한 작은 복원 상태에만 rememberSaveable 을 사용한다

상위 문서: [Compose 상태와 Effect 계약](./compose-state-and-effect-contracts.md)

`**rememberSaveable**(화면 회전이나 프로세스 재시작 후에도 Bundle을 통해 UI 상태를 복원해 주는 저장 API)` 은 Composable 보다 오래 살아야 하는 작은 UI 값을 복원할 때 사용한다.

### 적합한 값

- 검색어 입력 초안
- 선택한 탭의 key
- 필터의 enum 또는 문자열 key
- 현재 페이지 번호
- 펼침 여부나 선택 여부처럼 작은 primitive 값

이 값들은 화면을 다시 만들었을 때 사용자의 직전 UI 맥락을 복원하는 데 의미가 있다.

복원 대상은 작고 직렬화 가능하며, 화면을 다시 구성해도 의미가 유지되어야 한다.

```kotlin
@Composable
fun SearchHeader() {
    var query by rememberSaveable { mutableStateOf("") }
    SearchField(value = query, onValueChange = { query = it })
}
```

### 저장소로 오해하지 않는다

`rememberSaveable` 은 앱의 영속 저장소가 아니다.

앱 설정, 인증 정보, 서버 데이터, 사용자 문서, 큰 목록을 보관하는 API 가 아니다.

앱을 다시 시작해도 반드시 남아야 하는 값은 [DataStore](https://developer.android.com/topic/libraries/architecture/datastore) 나 [Room](https://developer.android.com/training/data-storage/room) 에 둔다.

서버에서 다시 조회할 수 있는 화면 데이터는 ViewModel 과 repository 가 소유한다.

다음 값은 `rememberSaveable` 에 넣지 않는다.

- access token, session key, 개인정보
- bitmap, 큰 리스트, entity 전체
- repository, client, database 연결
- 화면의 최종 source of truth 인 도메인 상태
- 복원보다 재조회가 맞는 서버 응답

### 수명 질문

먼저 "이 값은 화면을 다시 만들었을 때 복원되어야 하는가?"를 묻는다.

아니오라면 `remember` 가 더 정확하다.

예라면 "작고 UI 전용인가?"를 다시 묻는다.

아니오라면 더 높은 owner 나 영속 계층으로 올린다.

화면이 navigation entry 와 함께 유지되어야 하는 복잡한 form 은 `rememberSaveable` 만으로 해결하지 않는다.

필요한 상태 범위를 확인하고 entry-scoped ViewModel 이나 별도 state holder 를 선택한다.

`rememberSaveable` 은 복원 가능한 값을 직접 소유한다.

복원된 값이 도메인 상태와 충돌한다면 어느 쪽이 source of truth 인지 먼저 정한다.

복원은 데이터 동기화 정책을 대신하지 않는다.

### 선택 요약

| 질문 | 선택 |
| --- | --- |
| recomposition 사이에만 필요하다 | `remember` |
| 구성 변경 뒤 작은 UI 값을 복원한다 | `rememberSaveable` |
| 여러 화면이 공유한다 | 상위 state holder 또는 ViewModel |
| 앱 재시작 뒤에도 보존한다 | DataStore, Room, repository |
| 큰 데이터를 다시 얻을 수 있다 | 화면 상태 owner 에서 재조회 |

참고: [Save UI state in Compose](https://developer.android.com/develop/ui/compose/state-saving), [State and Jetpack Compose](https://developer.android.com/develop/ui/compose/state)
