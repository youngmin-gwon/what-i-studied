# 실수하기 쉬운 지점

상위 노트: [[jetpack-compose-state-management-flutter-comparison]]

### Composable body에서 직접 API 호출하지 않기

```kotlin
@Composable
fun BadScreen() {
    repository.load()
}
```

Composable은 recomposition될 수 있으므로 body에 직접 side effect를 두면 호출이 반복될 수 있습니다. ViewModel 또는
`LaunchedEffect`로 옮겨야 합니다.

### `remember`에 repository/client 저장하지 않기

```kotlin
val repository = remember { SessionRepository(...) }
```

DI로 조립할 객체를 UI 기억 장치에 넣으면 수명과 테스트 경계가 흐려집니다. Repository, HTTP client, DataStore, cipher 같은
dependency는 DI에서 만들고 주입하는 편이 맞습니다.

### `rememberSaveable`을 영구 저장소처럼 쓰지 않기

`rememberSaveable`은 UI 복원 장치입니다. sessionKey, auth token, 운동 기록, 측정 이력 같은 데이터는 DataStore나 Room에 저장해야
합니다.

### `by`를 상태 관리 도구로 오해하지 않기

`by`는 Kotlin 문법입니다. 상태를 관찰 가능하게 만드는 것은 `mutableStateOf`, `StateFlow`, `collectAsStateWithLifecycle`
같은 API입니다.

### Flutter BuildContext와 Android Context를 같은 것으로 보지 않기

Flutter의 `BuildContext`는 widget tree 안의 위치에 가깝고, Android의 `Context`는 앱/컴포넌트가 OS 리소스와 시스템 서비스에 접근하는
환경 핸들입니다.

Compose에서 Android `Context`가 필요하면 `LocalContext.current`를 사용하지만, Repository나 ViewModel에 오래 보관할 객체로
넘기는 것은 피하는 편이 좋습니다. 자세한
내용은 [[android-context]]를
참조하세요.

---
