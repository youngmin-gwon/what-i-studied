# `@Inject`: 생성자 주입

상위 노트: [[metro-di-get-it-guide]]

Metro에서 가장 기본은 **생성자 주입(Constructor Injection)**입니다.

```kotlin
@Inject
class SessionRepository(
    private val storage: SessionStorage,
    private val api: SessionApi,
)
```

뜻:

```text
Metro야, SessionRepository를 만들 때
SessionStorage와 SessionApi를 찾아서 생성자에 넣어줘.
```

생성자 주입이 좋은 이유:

* 어떤 의존성이 필요한지 클래스 선언만 봐도 알 수 있음
* 테스트에서 fake 객체를 넣기 쉬움
* `lateinit` 주입보다 안전함
* 객체가 만들어진 뒤 의존성이 비어 있는 상태가 없음

get_it에서는 보통 이렇게 했을 것입니다.

```dart
getIt.registerFactory<SessionRepository>(
  () => SessionRepository(
    getIt<SessionStorage>(),
    getIt<SessionApi>(),
  ),
);
```

Metro에서는 클래스 쪽에 `@Inject`만 붙이고, 나머지는 그래프가 해결하게 합니다.

---
