# 테스팅

상위 노트: [[android-viewmodel]]

```kotlin
class UserViewModelTest {
    private lateinit var viewModel: UserViewModel
    private lateinit var repository: FakeUserRepository
    
    @Before
    fun setup() {
        repository = FakeUserRepository()
        viewModel = UserViewModel(repository)
    }
    
    @Test
    fun `loadUsers updates state correctly`() = runTest {
        // Given
        val expectedUsers = listOf(User("1", "John"))
        repository.setUsers(expectedUsers)
        
        // When
        viewModel.loadUsers()
        
        // Then
        val state = viewModel.uiState.value
        assertEquals(expectedUsers, state.users)
        assertEquals(false, state.isLoading)
    }
    
    @Test
    fun `loadUsers handles error`() = runTest {
        // Given
        repository.setShouldFail(true)
        
        // When
        viewModel.loadUsers()
        
        // Then
        val state = viewModel.uiState.value
        assertNotNull(state.error)
        assertEquals(false, state.isLoading)
    }
}
```

더 자세한 내용은 [[android-testing-and-quality]] 참고.
