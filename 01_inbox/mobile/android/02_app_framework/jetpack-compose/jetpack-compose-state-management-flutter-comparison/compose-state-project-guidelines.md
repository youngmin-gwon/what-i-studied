# 이 프로젝트 기준

상위 노트: [[jetpack-compose-state-management-flutter-comparison]]

현재 프로젝트에서는 다음 기준으로 나누는 편이 좋습니다.

| 대상                        | 위치                                                       |
|:--------------------------|:---------------------------------------------------------|
| Root session 판정           | `AppSessionViewModel` 또는 root ViewModel                  |
| session 저장                | `feature:session:impl`의 repository/DataStore             |
| session 상태 contract       | `feature:session:api`                                    |
| 로그인 form 입력값              | 처음에는 `rememberSaveable`, 검증/로그인 로직이 커지면 `AuthViewModel`  |
| 복잡한 form 상태 전이            | 처음에는 ViewModel의 `_uiState.update`, 반복이 커지면 선택적으로 Reducer |
| Auth flow back stack      | auth shell/flow Composable 내부의 navigation state          |
| Main tab 선택               | `rememberSaveable` 또는 Navigation 3 back stack            |
| Main tab별 화면 상태           | 각 feature impl의 route/ViewModel                          |
| foldable/tablet layout 선택 | window size/posture state를 읽고 shell에서 adaptive UI 결정     |
| deep link 처리              | app/root navigation layer에서 route key로 변환                |

중요한 기준은 다음입니다.

```text
UI만 알면 되는 상태인가?
-> remember / rememberSaveable

화면 정책, 로딩, API 결과, validation이 섞이는가?
-> ViewModel

앱을 껐다 켜도 남아야 하는가?
-> DataStore / Room

여러 feature가 공유해야 하는 contract인가?
-> api module

실제 Android 저장소, 네트워크, 암호화 구현인가?
-> impl module
```

---
