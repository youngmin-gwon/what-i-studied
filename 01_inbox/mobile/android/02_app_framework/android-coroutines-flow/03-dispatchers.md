# Dispatchers

상위 노트: [[android-coroutines-flow]]

```kotlin
viewModelScope.launch {
    // 기본: Dispatchers.Main (UI 스레드)
    _isLoading.value = true
    
    val result = withContext(Dispatchers.IO) {
        // IO 스레드 풀: 네트워크, DB, 파일 I/O
        repository.fetchFromNetwork()
    }
    
    val processed = withContext(Dispatchers.Default) {
        // CPU 집약적 작업: 정렬, 파싱, 암호화
        processLargeData(result)
    }
    
    // 다시 Main 으로 자동 복귀
    _uiState.value = UiState.Success(processed)
}
```

| Dispatcher | 스레드 수 | 용도 |
|------------|-----------|------|
| `Main` | 1 (UI 스레드) | UI 업데이트, StateFlow 방출 |
| `IO` | 64+ (탄력적) | 네트워크, DB, 파일 |
| `Default` | CPU 코어 수 | 정렬, JSON 파싱, 암호화 |
| `Unconfined` | 호출 스레드 → 재개 스레드 | 테스트 용도 (실 사용 지양) |
