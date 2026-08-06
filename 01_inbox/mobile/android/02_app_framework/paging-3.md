---
title: paging-3
tags: [android, architecture, paging3, flow, room, infinity-scroll]
---

# Paging 3 (무한 스크롤 & 대용량 데이터 로딩)

## 1. 개념 & 비유 (Concept & Real-World Analogy)

### 개념
**Paging 3**는 Android Jetpack 라이브러리의 일부로, 서버나 로컬 수천~수만 개의 대용량 데이터를 메모리 효율적으로 나누어(Chunk) 차례대로 로딩(Lazy Loading)하는 아키텍처 구성 요소입니다. Kotlin Flow 및 Coroutines와 완벽하게 결합되어 네트워크/DB 데이터 로딩 상태(Loading, Error, Idle) 관리 및 중복 요청 방지, 메모리 캐싱을 자동으로 처리합니다.

### 실생활 비유: 뷔페 음식 접시 교체 (Buffet Food Tray Replacement)
뷔페 식당에서 손님들에게 10,000인분의 음식을 한꺼번에 식탁에 차려놓지 않습니다. 식탁 공간(메모리)도 부족하고 음식도 굳어버리기 때문입니다.
대신 주방은 일정한 크기의 **음식 접시(Chunk Page)**를 만들어 두고, 손님이 음식을 다 먹어갈 즈음(스크롤 임계점 도달) 조용히 새 음식 접시(**PagingSource**)를 가져와 리필해 줍니다. 손님이 더 이상 음식을 먹지 않거나 다른 코너로 이동하면, 오래된 접시는 치워(**Memory Eviction**) 식탁을 쾌적하게 유지합니다.

---

## 2. 핵심 구성 요소 & 동작 원리 (Core Components & How It Works)

### 핵심 구성 요소
1. **`PagingSource<Key, Value>`**: 특정 데이터 소스(Network API 또는 Room Query)에서 한 번에 가져올 데이터 조각(Page)을 로딩하는 엔진입니다. `load()` 함수를 구현하여 `LoadResult.Page`, `Error`, `Invalid`를 반환합니다.
2. **`RemoteMediator<Key, Value>`**: 네트워크(Remote)와 로컬 DB(Local Room) 간의 오프라인 퍼스트(Offline-First) 동기화를 주도하는 컨트롤러입니다. DB 데이터가 고갈되면 네트워크에서 새 데이터를 받아와 DB에 캐싱합니다.
3. **`Pager`**: `PagingSource`와 `PagingConfig`를 결합하여 UI에 전달할 반응형 데이터 스트림(`Flow<PagingData<T>>`)을 생성합니다.
4. **`PagingData`**: 로딩된 개별 페이지 데이터들의 스냅샷 용기이며, `cachedIn(viewModelScope)`를 통해 ViewModel 생명주기 동안 메모리에 안전하게 유지됩니다.
5. **`CombinedLoadStates`**: UI가 데이터 로딩 중(`Loading`), 성공(`NotLoading`), 실패(`Error`) 상태를 개별 구간(Refresh, Prepend, Append)별로 감지하고 에러 처리나 로딩 스피너를 표시할 수 있게 해줍니다.

### 동작 흐름도 (Mermaid Diagram)

```mermaid
flowchart TD
    subgraph Data Layer
        API[Remote Server / REST API]
        DB[(Local Room Database)]
        RM[RemoteMediator]
        PS[PagingSource]
    end

    subgraph ViewModel Layer
        PGR[Pager]
        PDF[Flow<PagingData<T>>]
    end

    subgraph UI Layer (Compose / RecyclerView)
        UI[LazyColumn / collectAsLazyPagingItems]
        STATE[LoadState: Loading / Error / NotLoading]
    end

    API -->|"Fetch Next Page"| RM
    RM -->|"Cache Data"| DB
    DB -->|"Read Cached Page"| PS
    PS -->|"Emit Page Chunks"| PGR
    PGR -->|"cachedIn viewModelScope"| PDF
    PDF -->|"Collect Streams"| UI
    UI -->|"Scroll Threshold Trigger"| PS
    UI -->|"Render Loading Spinner / Error Toast"| STATE
```

---

## 3. 코드 예제 & 사용 방법 (Code Example & Implementation)

### Step 1: PagingSource 구현
```kotlin
import androidx.paging.PagingSource
import androidx.paging.PagingState

class UserPagingSource(
    private val apiService: UserApiService
) : PagingSource<Int, User>() {

    override suspend fun load(params: LoadParams<Int>): LoadResult<Int, User> {
        val pageKey = params.key ?: FIRST_PAGE_INDEX
        return try {
            val response = apiService.getUsers(page = pageKey, limit = params.loadSize)
            val users = response.data
            
            LoadResult.Page(
                data = users,
                prevKey = if (pageKey == FIRST_PAGE_INDEX) null else pageKey - 1,
                nextKey = if (users.isEmpty()) null else pageKey + 1
            )
        } catch (exception: Exception) {
            LoadResult.Error(exception)
        }
    }

    override fun getRefreshKey(state: PagingState<Int, User>): Int? {
        return state.anchorPosition?.let { anchorPosition ->
            val anchorPage = state.closestPageToPosition(anchorPosition)
            anchorPage?.prevKey?.plus(1) ?: anchorPage?.nextKey?.minus(1)
        }
    }

    companion object {
        private const val FIRST_PAGE_INDEX = 1
    }
}
```

### Step 2: Repository & ViewModel 구성
```kotlin
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import androidx.paging.Pager
import androidx.paging.PagingConfig
import androidx.paging.PagingData
import androidx.paging.cachedIn
import dagger.hilt.android.lifecycle.HiltViewModel
import javax.inject.Inject
import kotlinx.coroutines.flow.Flow

class UserRepository @Inject constructor(
    private val apiService: UserApiService
) {
    fun getUsersStream(): Flow<PagingData<User>> {
        return Pager(
            config = PagingConfig(
                pageSize = 20,
                enablePlaceholders = false,
                prefetchDistance = 5
            ),
            pagingSourceFactory = { UserPagingSource(apiService) }
        ).flow
    }
}

@HiltViewModel
class UserListViewModel @Inject constructor(
    private val repository: UserRepository
) : ViewModel() {

    val userPagingFlow: Flow<PagingData<User>> = repository
        .getUsersStream()
        .cachedIn(viewModelScope) // 화면 회전 시 중복 로딩 방지 및 캐싱
}
```

### Step 3: Jetpack Compose UI 바인딩
```kotlin
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.paging.LoadState
import androidx.paging.compose.collectAsLazyPagingItems
import androidx.paging.compose.itemKey

@Composable
fun UserListScreen(viewModel: UserListViewModel = hiltViewModel()) {
    val lazyUserItems = viewModel.userPagingFlow.collectAsLazyPagingItems()

    LazyColumn {
        items(
            count = lazyUserItems.itemCount,
            key = lazyUserItems.itemKey { it.id }
        ) { index ->
            val user = lazyUserItems[index]
            user?.let { UserRow(user = it) }
        }

        // 로딩 및 에러 처리 State 감지
        when (val appendState = lazyUserItems.loadState.append) {
            is LoadState.Loading -> {
                item { CircularProgressIndicator() }
            }
            is LoadState.Error -> {
                item { Text("에러 발생: ${appendState.error.localizedMessage}") }
            }
            else -> {}
        }
    }
}
```

---

## 4. 주의사항 & 팁 (Key Considerations & Best Practices)

1. **`cachedIn(viewModelScope)` 필수 사용**: ViewModel에서 PagingFlow에 `cachedIn(viewModelScope)`를 적용하지 않으면 화면 회전(Configuration Change) 시 데이터가 처음부터 다시 로딩되거나 프로세스 재생성 시 앱이 비정상 동작할 수 있습니다.
2. **Key 중복 및 Stable Key 지정**: Compose `LazyColumn`의 `items`에서 `lazyUserItems.itemKey { it.id }`처럼 고유한 키를 지정해야 스크롤 애니메이션과 리포지셔닝 성능이 보장됩니다.
3. **RemoteMediator 오프라인 퍼스트 활용**: 네트워크가 불안정한 환경에서는 Room DB와 RemoteMediator 조합을 사용하여 단일 출처(Single Source of Truth)를 Room DB로 일관되게 유지하는 아키텍처가 권장됩니다.
4. **Transform 연산 위치**: `map`, `filter` 등의 변환 연산은 `PagingData` 연산자를 사용해야 하며, `Flow` 수준에서 잘못 변환하면 리페이징 트리가 깨질 수 있습니다.

---

## 5. 연관 개념 & 참고 링크 (Related Concepts & Relative Markdown Links)

- [Hilt Dependency Injection](hilt-di.md) - PagingSource 및 Repository의 의존성 주입 구조
- [Dagger DI Architecture](dagger-di.md) - 커스텀 컴포넌트 기반 DI 구조
- [Push Notification & FCM](push-notification-and-fcm.md) - 실시간 메시징 수신 시 페이징 데이터 갱신 연동
