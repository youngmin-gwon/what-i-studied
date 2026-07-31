# One-time event 처리

```kotlin
// LiveData로 일회성 이벤트 처리 (추천하지 않음)
class EventViewModel : ViewModel() {
    private val _navigationEvent = MutableLiveData<Event<String>>()
    val navigationEvent: LiveData<Event<String>> = _navigationEvent
    
    fun navigateToDetail() {
        _navigationEvent.value = Event("detail")
    }
}

// Event wrapper class
class Event<out T>(private val content: T) {
    private var hasBeenHandled = false
    
    fun getContentIfNotHandled(): T? {
        return if (hasBeenHandled) {
            null
        } else {
            hasBeenHandled = true
            content
        }
    }
}

// ✅ Channel 사용 (권장)
class EventViewModel : ViewModel() {
    private val _navigationEvents = Channel<String>()
    val navigationEvents = _navigationEvents.receiveAsFlow()
    
    fun navigateToDetail() {
        viewModelScope.launch {
            _navigationEvents.send("detail")
        }
    }
}

// Activity에서 수집
lifecycleScope.launch {
    repeatOnLifecycle(Lifecycle.State.STARTED) {
        viewModel.navigationEvents.collect { destination ->
            // 한 번만 처리됨
            navigate(destination)
        }
    }
}
```
