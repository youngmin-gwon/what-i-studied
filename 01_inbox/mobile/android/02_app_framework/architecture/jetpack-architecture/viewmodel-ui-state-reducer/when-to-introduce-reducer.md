# Reducer 도입 기준

상위 노트: [[viewmodel-ui-state-reducer]]

Reducer는 생소한 패턴이 아닙니다. Elm, Redux, MVI, Flutter Bloc 계열에서 널리 쓰인 개념입니다. 다만 Android 공식 MVVM에서 별도
`Reducer` 클래스를 만드는 것은 필수 관례가 아닙니다.

따라서 이 프로젝트에서는 Reducer를 기본값으로 두지 않습니다.

Reducer가 필요 없는 경우:

- 단순 조회 화면
- 목록 화면
- 상세 화면
- 설정 화면
- 상태 필드가 적고 `copy()`가 몇 번 나오지 않는 화면
- ViewModel 테스트만으로 충분히 읽히는 화면

Reducer가 도움이 되는 경우:

- 회원가입, 결제, 주문, 예약, 복잡한 form, wizard
- user action이 20개 안팎으로 늘어나는 화면
- 상태 전이 규칙을 한 곳에서 읽어야 하는 화면
- 같은 검증과 파생 상태 계산이 여러 함수에 반복되는 화면
- Reducer 단위 순수 JVM 테스트가 ViewModel 테스트보다 훨씬 명확한 화면

실무 기준은 다음처럼 잡습니다.

```text
처음부터 Reducer를 만들지 않는다.
ViewModel 안의 상태 계산이 반복되고 읽기 어려워질 때 분리한다.
Reducer를 만들면 순수 상태 전이만 맡긴다.
새 아키텍처 도입이 아니라 ViewModel 내부 계산을 분리한 리팩터링으로 취급한다.
```

---
