# Repository는 Room과 DataStore를 Flow로 연결한다

상위 문서: [영속 저장소 계약](01_inbox/mobile/android/02_app_framework/data/storage/persistence-contracts/persistence-contracts.md)
관련 정본: [Repository는 데이터 흐름을 Flow로 제공하고 ViewModel은 화면 상태로 조합한다](01_inbox/mobile/android/02_app_framework/data/async-flow/flow-state-contracts/repository-exposes-flow-and-viewmodel-composes-screen-state.md)


저장소 구현은 데이터 레이어에 캡슐화하고 UI에는 의미 있는 상태를 제공한다.

Repository는 Room DAO와 DataStore를 조합하는 경계가 될 수 있다.

```kotlin
class UserRepository @Inject constructor(
    private val userDao: UserDao,
    private val preferences: DataStore<UserPreferences>,
) {
    val users: Flow<List<User>> = userDao.observeUsers()
    val preferences: Flow<UserPreferences> = preferences.data

    suspend fun addUser(user: User) {
        userDao.insert(user)
    }
}
```

DAO의 읽기 API는 `Flow`로 반환한다.

DataStore의 읽기도 `data`에서 시작하는 `Flow`로 반환한다.

쓰기 작업은 `suspend` 함수로 제공하고 적절한 coroutine scope에서 호출한다.

## UI와의 연결

ViewModel은 Repository의 여러 흐름을 화면 상태로 결합한다.

화면은 데이터베이스나 DataStore 파일을 직접 읽지 않는다.

`stateIn`이나 `WhileSubscribed` 같은 정책은 ViewModel의 화면 수명에 맞춰 선택한다.

수집은 lifecycle-aware API를 사용해 화면이 보이지 않을 때 불필요한 작업을 줄인다.

## Entity 노출을 줄이기

작은 프로젝트에서는 Entity를 바로 반환할 수 있지만 경계가 커지면 변환 모델을 둔다.

Repository가 `UserEntity`를 `User`나 `UserUiState`로 바꾸면 schema와 UI 계약이 분리된다.

DataStore의 Preferences도 Repository 밖으로 노출하지 않는다.

키 이름과 기본값은 데이터 레이어가 소유한다.

## 쓰기 규칙

같은 DataStore 파일을 여러 singleton으로 생성하지 않는다.

Room 쓰기와 DataStore 쓰기는 각각의 저장소 transaction 의미를 가진다.

두 저장소의 쓰기를 하나의 원자적 transaction이라고 가정하지 않는다.

둘을 함께 갱신해야 한다면 실패 순서와 재시도 정책을 명시한다.

## 테스트 경계

Repository 테스트는 DAO와 DataStore를 대체해 읽기 흐름과 쓰기 명령을 검증한다.

Room migration 테스트는 별도로 schema 경로를 검증한다.

Flow 테스트는 초기값, 변경 전파, 오류 처리를 확인한다.

이 구조는 [Android 앱 아키텍처 공식 문서](https://developer.android.com/topic/architecture)의 data layer 원칙과 맞는다.
