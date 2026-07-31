# Compose Navigation (Type-safe / Modern ✅)

상위 노트: [[android-jetpack-architecture]]

Android Gradle Plugin 8.2+ 및 Jetpack Navigation 2.8.0+ 부터는 Kotlin Serialization 을 활용한 **완전한 타입 안정성(Full Type-safety)**을 지원합니다.

```kotlin
// 1. Route 정의 (Serialization 필수)
@Serializable object Home
@Serializable data class Detail(val id: String)

// 2. NavHost 설정
val navController = rememberNavController()
NavHost(navController = navController, startDestination = Home) {
    composable<Home> {
        HomeScreen(onDetailClick = { id -> 
            navController.navigate(Detail(id)) 
        })
    }
    
    // 3. 타입 안정성이 보장된 인자 수집
    composable<Detail> { backStackEntry ->
        val detail: Detail = backStackEntry.toRoute<Detail>()
        DetailScreen(detail.id)
    }
}
```

>[!TIP] **왜 타입 안정성인가?**
 기존의 경로 문자열(`"detail/{id}"`) 방식은 오타에 취약하고 런타임 에러를 유발했습니다. Serialization 기반 방식은 컴파일 타임에 경로와 인자를 검증하므로 안전합니다.
```

### Paging 3

대량 데이터를 효율적으로 로드.

```kotlin
// PagingSource
class UserPagingSource(
    private val api: ApiService
) : PagingSource<Int, User>() {
    
    override suspend fun load(params: LoadParams<Int>): LoadResult<Int, User> {
        return try {
            val page = params.key ?: 1
            val response = api.getUsers(page, params.loadSize)
            
            LoadResult.Page(
                data = response.users,
                prevKey = if (page == 1) null else page - 1,
                nextKey = if (response.users.isEmpty()) null else page + 1
            )
        } catch (e: Exception) {
            LoadResult.Error(e)
        }
    }
    
    override fun getRefreshKey(state: PagingState<Int, User>): Int? {
        return state.anchorPosition?.let { anchorPosition ->
            state.closestPageToPosition(anchorPosition)?.prevKey?.plus(1)
                ?: state.closestPageToPosition(anchorPosition)?.nextKey?.minus(1)
        }
    }
}

// Repository
class UserRepository(private val api: ApiService) {
    fun getUsersPaged(): Flow<PagingData<User>> {
        return Pager(
            config = PagingConfig(
                pageSize = 20,
                enablePlaceholders = false,
                prefetchDistance = 5
            ),
            pagingSourceFactory = { UserPagingSource(api) }
        ).flow
    }
}

// ViewModel
class UserViewModel(private val repository: UserRepository) : ViewModel() {
    val users: Flow<PagingData<User>> = repository.getUsersPaged()
        .cachedIn(viewModelScope)
}

// Adapter
class UserAdapter : PagingDataAdapter<User, UserViewHolder>(USER_COMPARATOR) {
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): UserViewHolder {
        // ViewHolder 생성
    }
    
    override fun onBindViewHolder(holder: UserViewHolder, position: Int) {
        val user = getItem(position)
        holder.bind(user)
    }
    
    companion object {
        private val USER_COMPARATOR = object : DiffUtil.ItemCallback<User>() {
            override fun areItemsTheSame(oldItem: User, newItem: User) =
                oldItem.id == newItem.id
            
            override fun areContentsTheSame(oldItem: User, newItem: User) =
                oldItem == newItem
        }
    }
}

// Fragment 에서 사용
class UserListFragment : Fragment() {
    private val viewModel: UserViewModel by viewModels()
    private val adapter = UserAdapter()
    
    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        recyclerView.adapter = adapter
        
        lifecycleScope.launch {
            viewModel.users.collectLatest { pagingData ->
                adapter.submitData(pagingData)
            }
        }
        
        // 로딩 상태 표시
        adapter.addLoadStateListener { loadState ->
            progressBar.isVisible = loadState.refresh is LoadState.Loading
            errorText.isVisible = loadState.refresh is LoadState.Error
        }
    }
}
```
