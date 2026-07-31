# `remember`는 캐시보다 Composition 저장공간에 가깝다

상위 노트: [jetpack-compose-automatic-state-observation-for-flutter-developers](01_inbox/mobile/android/02_app_framework/jetpack-compose/runtime/jetpack-compose-automatic-state-observation-for-flutter-developers.md)

Flutter 개발자는 `remember`를 단순 memoization으로 이해하기 쉽습니다. 하지만 Compose에서 더 중요한 관점은
**Composition에 귀속된 저장공간**입니다.

```kotlin
@Composable
fun SearchBar() {
    var query by remember { mutableStateOf("") }

    TextField(
        value = query,
        onValueChange = { query = it },
    )
}
```

이 값은 `SearchBar`가 Composition에 남아 있는 동안 유지됩니다.

```text
recomposition
-> 유지

SearchBar가 composition에서 제거됨
-> 사라짐

Activity recreation/process death 복원
-> 기본 remember만으로는 보장하지 않음
```

화면 회전이나 process death 후에도 작은 UI 값을 복원해야 하면 `rememberSaveable`을 선택합니다. 화면 정책, API 결과, validation처럼
Composable보다 오래 살아야 하는 상태는 ViewModel이나 repository로 올립니다.

---
