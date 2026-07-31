# 중위 함수(Infix Function) — `togetherWith`
```kotlin
fadeIn() togetherWith fadeOut()
```
* Kotlin에서 `infix` 키워드가 붙은 함수는 **점(`.`)과 괄호 없이 마치 연산자처럼** 호출할 수 있습니다.
* 위 코드는 사실 다음과 완전히 동일합니다:
```kotlin
fadeIn().togetherWith(fadeOut())
```
* `togetherWith`는 Compose Animation 라이브러리가 제공하는 중위 함수로, 두 개의 전환 효과를 결합하여 하나의 `ContentTransform`을 만들어 줍니다.
