# 예외 처리 가이드: runCatching vs try-catch

Android 앱 개발 시 예외(Exception) 처리 도구로 `runCatching` 과 `try-catch` 를 많이 사용합니다.두 방식은 처리 목적과 코루틴 취소 메커니즘
전파에 중요한 차이가 있습니다.

| 구분         | `try-catch`                   | `runCatching`                                         |
|:-----------|:------------------------------|:------------------------------------------------------|
| **스타일**    | 명령형 (Imperative)              | 함수형 / 표현식 (Functional)                                |
| **결과 반환**  | 블록 반환값 또는 직접 흐름 제어            | `Result<T>` (`Success` 또는 `Failure`)                  |
| **체이닝**    | 불가 (`try` 블록 내부 처리)           | 가능 (`map`, `recover`, `onSuccess`, `onFailure`)       |
| **코루틴 취소** | `CancellationException` 정상 전파 | ⚠️ `CancellationException`까지 잡아서 `Failure`로 변환할 위험 있음 |

#### 1) Repository / Data 계층: `runCatching` 권장

Repository나 DataSource에서 파일 IO, JSON 파싱 결과를 `Result<T>`로 감싸 반환할 때 적합합니다.

```kotlin
// Data Layer (RepositoryImpl)
override suspend fun getOpenSourceLicenses(): Result<List<OpenSourceArtifact>> =
    withContext(Dispatchers.IO) {
        runCatching {
            val jsonString =
                assetManager.open("licenses/artifacts.json").bufferedReader().use { it.readText() }
            LicenseJsonParser.parseJson(jsonString)
        }.map { dtos ->
            dtos.map { it.toDomain() }
        }
    }
```

#### 2) 특정 예외 조준 및 Coroutine 취소 보장: `try-catch` 권장

부모-자식 코루틴 간 취소 신호(`CancellationException`)를 정상적으로 위로 전달해야 하거나, 특정 예외(`IOException` 등)만 핀포인트로 잡고 싶을
때는 `try-catch`를 사용해야 합니다.

```kotlin
suspend fun syncData() {
    try {
        apiService.uploadLogs()
    } catch (e: IOException) {
        // 네트워크/IO 예외만 복구 처리
        logger.e(e) { "로그 업로드 실패" }
    }
    // CancellationException이나 RuntimeException은 그대로 상위 코루틴으로 전파됨
}
```

Compose는 상태 타입에 따라 화면을 분기합니다.

```kotlin
@Composable
fun BenefitScreen(uiState: BenefitUiState) {
    when (uiState) {
        BenefitUiState.Loading -> LoadingScreen()
        is BenefitUiState.Ready -> BenefitList(uiState.benefits)
        is BenefitUiState.Error -> ErrorScreen(uiState.message)
    }
}
```
