---
title: savedstatehandle-state-restoration
tags: [android, android/architecture, android/state-management, android/viewmodel]
aliases: ["SavedStateHandle은 프로세스 사망 후 복원해야 하는 작은 상태에 사용한다"]
date modified: 2026-08-05 16:15:00 +09:00
date created: 2026-08-01 00:00:00 +09:00
---

## SavedStateHandle 은 프로세스 사망 후 복원해야 하는 작은 상태에 사용한다

상위 문서: [Android ViewModel](viewmodel.md)

### 핵심 주장

`SavedStateHandle` 은 프로세스가 종료된 뒤 화면을 다시 만들 때

복원해야 하는 작은 상태를 [viewmodel](viewmodel.md) 과 함께 저장한다.

대표적인 값은 선택된 ID, 검색어, 필터, 탭 위치, 페이징 위치다.

이 값으로 다시 데이터를 조회할 수 있어야 한다.

```kotlin
class DetailViewModel(
    private val savedStateHandle: SavedStateHandle,
    private val repository: UserRepository
) : ViewModel() {
    val userId: StateFlow<String?> = savedStateHandle
        .getStateFlow("user_id", null)

    fun selectUser(id: String) {
        savedStateHandle["user_id"] = id
    }
}
```

### 적합한 데이터

- 문자열, 숫자, Boolean
- 선택된 항목의 식별자
- 복원 가능한 정렬·필터 값
- 작은 `Parcelable` 또는 지원되는 상태 값

큰 목록, 이미지, 캐시, 데이터베이스 레코드를 넣지 않는다.

저장 한도와 직렬화 비용을 고려하면 원본 데이터보다 식별자를 저장하는 편이 낫다.

```kotlin
class SearchViewModel(
    private val state: SavedStateHandle
) : ViewModel() {
    var query: String
        get() = state["query"] ?: ""
        set(value) { state["query"] = value }
}
```

복원된 ID 로 Repository 를 다시 조회하는 것은 ViewModel 의 조율 책임이다.

영구 보존이 필요한 데이터는 데이터베이스나 파일 저장소에 기록한다.

`SavedStateHandle` 은 영구 저장소를 대체하지 않는다.

### 사용 순서

1. 복원할 상태를 식별자와 작은 값으로 정의한다.
2. 상태 키를 상수처럼 일관되게 관리한다.
3. 복원된 값을 사용해 필요한 데이터를 다시 조회한다.
4. 조회 결과 자체는 ViewModel 상태나 Repository 캐시에 둔다.

키에 전체 응답 객체를 넣으면 저장 크기와 호환성 문제가 커진다.

화면 상태가 바뀔 때마다 큰 객체를 저장하는 것도 피한다.

`SavedStateHandle` 의 값은 프로세스 복원을 위한 입력이지,

현재 화면이 소비할 최종 UI 상태와 동일한 저장소가 아니다.

복원 시점에 값이 없을 수 있으므로 기본값과 null 처리도 정의한다.

이 경계를 지키면 화면은 짧은 복원 정보만 저장하고,

실제 데이터의 최신성은 Repository 정책에 맡길 수 있다.
