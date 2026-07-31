# Deep Link 처리

Deep link는 app layer에서 route로 변환합니다.

```text
https://example.com/training/123
 -> TrainingDetailRoute("123")
```

session 상태에 따라 다르게 처리합니다.

```text
SignedIn:
 -> selectedDestination = Training
 -> trainingBackStack = [TrainingRoute, TrainingDetailRoute("123")]

SignedOut:
 -> pendingRoute = TrainingDetailRoute("123")
 -> AuthFlow(SignInRoute)
 -> 로그인 성공 후 MainScaffold로 이동
```

---
