# 하나의 Composable보다 오래, 앱 전체보다는 짧게

상위 노트: [[jetpack-compose-state-lifetime-api-selection]]

상태가 child composable보다 오래 살아야 하면 더 높은 owner로 올립니다.

```text
child composable 내부에서만 필요
-> child remember

screen 전체에서 필요
-> route/screen rememberSaveable 또는 screen ViewModel

navigation destination 동안 필요
-> entry-scoped ViewModel

tab/flow 전체에서 공유
-> parent composable state 또는 parent ViewModel

앱/세션 전체에서 공유
-> root ViewModel, repository, DataStore
```

예를 들어 sign-in 화면 안에서 password visibility는 field composable의 `remember`로 충분합니다. 반면 auth flow 전체에서 "
회원가입 중 선택한 약관/단계"를 공유해야 한다면 auth flow parent state나 shared ViewModel이 더 적합합니다.

---
