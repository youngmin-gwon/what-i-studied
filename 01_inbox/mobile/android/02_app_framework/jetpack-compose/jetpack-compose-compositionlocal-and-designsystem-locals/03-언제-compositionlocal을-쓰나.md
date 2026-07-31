# 언제 CompositionLocal을 쓰나?

상위 노트: [[jetpack-compose-compositionlocal-and-designsystem-locals]]

CompositionLocal은 아무 값이나 숨겨서 전달하는 도구가 아닙니다.

적합한 경우:

- 앱 또는 하위 tree 전체에 넓게 적용되는 값
- 중간 Composable이 굳이 몰라도 되는 환경값
- 화면 대부분이 공통으로 읽을 수 있는 design system 값
- preview/test 기본값을 둘 수 있는 값

부적합한 경우:

- 특정 화면의 `ViewModel`
- 버튼 클릭 callback
- form field 값
- 한두 Composable만 쓰는 임시 상태
- 명시적으로 parameter로 넘기는 편이 더 읽기 쉬운 값

이 프로젝트에서 `ViewModel`을 `Local`로 만들지 않는 이유도 여기에 있습니다. `ViewModel`은 화면 상태와 이벤트 처리의 구체적인 owner입니다. 이를
Local로 숨기면 어떤 UI가 어떤 상태에 의존하는지 추적하기 어려워집니다.

---
