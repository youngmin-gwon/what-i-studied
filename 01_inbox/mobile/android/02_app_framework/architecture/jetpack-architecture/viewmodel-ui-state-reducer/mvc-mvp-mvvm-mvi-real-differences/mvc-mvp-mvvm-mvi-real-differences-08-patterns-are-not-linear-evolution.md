# MVC에서 MVI로 직선 진화한 것이 아니다

마지막으로, `MVC -> MVI -> MVVM`처럼 직선적으로 진화했다고 보지는 않는 편이 좋습니다. 이 패턴들은 서로를 순서대로 대체한 후속 버전이라기보다, 각기 다른 시대와
플랫폼에서 나온 설계 철학입니다.

- MVC는 객체지향 GUI와 웹 프레임워크 맥락에서 널리 쓰였습니다.
- MVP는 Android 초기처럼 View를 interface로 분리하고 테스트하기 위해 많이 쓰였습니다.
- MVVM은 WPF의 data binding 맥락에서 강해졌고, Android에서는 ViewModel/StateFlow/Compose와 결합해 화면 상태 holder로 쓰입니다.
- MVI는 Elm, Redux 같은 함수형/단방향 데이터 흐름의 영향을 받아 Intent/Action, Reducer, 단일 State를 강조합니다.

따라서 이 문서에서는 아키텍처 이름보다 아래 질문을 더 중요하게 봅니다.

```text
화면 상태의 source of truth는 어디인가?
사용자 입력은 어떤 값/함수로 표현되는가?
상태 변화 규칙은 어디에 모여 있는가?
View를 직접 조작하는가, State를 렌더링하는가?
```
