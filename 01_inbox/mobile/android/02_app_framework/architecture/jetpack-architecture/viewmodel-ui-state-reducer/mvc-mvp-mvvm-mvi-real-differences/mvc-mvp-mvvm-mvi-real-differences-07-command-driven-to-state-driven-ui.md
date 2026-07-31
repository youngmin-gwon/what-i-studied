# Command-driven UI에서 State-driven UI로

MVC에서는 Controller가 View를 직접 바꾸는 코드가 자연스러웠습니다.

```text
controller.login()
 -> model.login()
 -> view.showLoading()
 -> view.showSuccess()
```

MVP에서는 Presenter가 View interface를 호출했습니다.

```text
presenter.login()
 -> view.showLoading()
 -> model.login()
 -> view.showError()
```

MVVM에서는 ViewModel이 View를 직접 조작하지 않고 observable state를 노출합니다.

```text
View
 -> user action
ViewModel
 -> UiState
View
 -> render(UiState)
```

MVI에서는 이 흐름을 더 엄격하게 만듭니다.

```text
Intent / Action
 -> Reducer / Store / Processor
 -> State
 -> Render
```

여기서 핵심은 "중재자가 사라졌다"가 아닙니다. 중재자는 계속 있습니다. 바뀐 것은 화면을 바꾸는 방식입니다.

```text
MVC/MVP:
어떤 View 메서드를 호출해서 화면을 바꿀까?

MVVM:
어떤 UiState를 노출해서 화면이 다시 그리게 할까?

MVI:
어떤 Action이 어떤 규칙으로 State를 바꾸게 할까?
```

즉, 관심사가 명령형 View 조작에서 상태 중심 렌더링으로 이동했습니다.

```text
Command-driven UI
 -> State-driven UI
```

이 변화가 React, Flutter, SwiftUI, Jetpack Compose 같은 선언형 UI와 잘 맞습니다. 현대 UI는 대부분 아래 모델을 따릅니다.

```text
State
 -> Render
```
