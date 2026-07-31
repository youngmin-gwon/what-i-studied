# Flow 기본 연산자

Flow는 값을 그대로 받는 것보다 중간에 가공해서 쓰는 경우가 많습니다.

| 연산자                    | 역할                           |
|:-----------------------|:-----------------------------|
| `map`                  | 값 변환                         |
| `filter`               | 조건에 맞는 값만 통과                 |
| `combine`              | 여러 Flow의 최신값을 합침             |
| `debounce`             | 짧은 시간 동안 잦은 입력을 모아서 처리       |
| `distinctUntilChanged` | 같은 값이 반복되면 무시                |
| `flatMapLatest`        | 새 값이 오면 이전 작업 취소 후 최신 작업만 유지 |
| `catch`                | 에러 처리                        |
| `onStart`              | 시작 시 로딩 상태 방출                |

```kotlin
val uiState: Flow<SearchUiState> =
    searchKeyword
        .debounce(300)
        .distinctUntilChanged()
        .flatMapLatest { keyword ->
            repository.searchProducts(keyword)
        }
        .map { products ->
            SearchUiState.Success(products)
        }
        .onStart {
            emit(SearchUiState.Loading)
        }
        .catch {
            emit(SearchUiState.Error)
        }
```

이 패턴은 검색 화면에서 매우 자주 씁니다.

* 유저가 타이핑할 때마다 바로 API 호출하지 않음
* 300ms 동안 입력이 멈추면 검색
* 새 검색어가 들어오면 이전 검색 취소
* 결과를 UI 상태로 변환
* 로딩/에러 상태까지 한 파이프라인에서 처리
