# Paging 3 data loading

상위 노트: [android-jetpack-architecture](01_inbox/mobile/android/02_app_framework/architecture/jetpack-architecture/android-jetpack-architecture.md)


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
