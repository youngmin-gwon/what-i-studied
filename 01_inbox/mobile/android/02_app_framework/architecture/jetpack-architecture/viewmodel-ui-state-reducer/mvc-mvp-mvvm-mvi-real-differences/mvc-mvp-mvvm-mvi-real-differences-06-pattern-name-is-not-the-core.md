# 패턴 이름보다 데이터 흐름이 핵심이다

그래서 "이름만 바뀐 것 아니냐"는 질문에 대한 답은 반쯤은 맞고, 반쯤은 틀립니다.

맞는 부분:

- 중간에서 입력을 받고 data/model layer와 연결하는 객체는 계속 존재합니다.
- MVC의 Controller, MVP의 Presenter, MVVM의 ViewModel, Flutter Bloc, Redux Store는 역할상 비교할 수 있습니다.
- 실무 코드에서는 이 객체들이 API 호출, 검증, 상태 갱신을 맡는 경우가 많습니다.

틀린 부분:

- MVI의 Intent는 중재자가 아닙니다. Intent는 사용자의 행동을 표현한 값입니다.
- 패턴의 차이는 객체 이름보다 데이터 흐름과 상태 표현 방식에서 생깁니다.
- 현대 선언형 UI에서는 View를 직접 조작하는지, State를 만들어 View가 그리게 하는지가 큰 차이를 만듭니다.
