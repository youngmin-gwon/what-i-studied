# Flutter BuildContext와 Android Context는 다르다

상위 노트: [[android-context]]

이름은 같지만 역할은 꽤 다릅니다.

| 구분    | Flutter `BuildContext`                        | Android `Context`                                   |
|:------|:----------------------------------------------|:----------------------------------------------------|
| 정체    | Widget tree 안의 위치                             | 앱/컴포넌트가 OS와 연결되는 환경 핸들                              |
| 주된 역할 | inherited widget lookup, theme, navigation 위치 | resource, storage, system service, component 실행     |
| 수명    | widget tree 위치에 묶임                            | Application/Activity/Service 등 종류별로 다름              |
| 사용 예  | `Theme.of(context)`, `Navigator.of(context)`  | `getSystemService()`, `startActivity()`, `filesDir` |

Flutter의 `BuildContext`는 "UI 트리에서 내가 어디 있나"에 가깝고, Android의 `Context`는 "내 앱/컴포넌트가 OS와 어떻게 연결되어 있나"에
가깝습니다.

Compose에서 Flutter의 `BuildContext`와 더 비슷한 개념은 `CompositionLocal`과 `Modifier` 체계에 가깝고, Android
`Context`는 그보다 더 플랫폼적인 객체입니다.

---
