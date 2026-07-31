# Reducer가 하지 말아야 할 일

상위 노트: [[viewmodel-ui-state-reducer]]

Reducer의 가치는 "예측 가능한 상태 계산"에 있습니다. 아래가 들어가기 시작하면 Reducer가 아니라 작은 ViewModel이나 UseCase가 되어버립니다.

Reducer에 넣지 않습니다.

- `Repository` 호출
- `suspend` 함수 호출
- `viewModelScope.launch`
- `Flow.collect`
- `Context`, `Resources`, `NavController`
- 현재 시간, 랜덤값, 파일, 네트워크처럼 외부 상태에 직접 의존하는 계산

외부 작업은 ViewModel이나 UseCase가 하고, 그 결과만 action으로 Reducer에 넘깁니다.

```text
SubmitClick
 -> ViewModel
 -> dispatch(SubmitStarted)
 -> Repository.signUp()
 -> dispatch(SubmitSucceeded or SubmitFailed)
```

이렇게 나누면 ViewModel은 외부 작업 조율을 담당하고, Reducer는 상태 전이 규칙만 담당합니다.

---
